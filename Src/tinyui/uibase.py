# -*- coding: UTF-8 -*-

'''
UI界面基础类。
定义和Qml.ui的交互接口
'''
from abc import ABCMeta, abstractmethod
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot, QUrl
from PyQt5.QtQml import QQmlContext
from PyQt5.QtQml import QQmlComponent
from PyQt5.QtQuick import QQuickView, QQuickWindow


class UIBase(QObject):
    '''
    本想定义：metaclass=ABCMeta，实现抽象借口。但是会报错：
    class UIBase(QObject, metaclass=ABCMeta):
    TypeError: metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases

    '''

    # ui 加载完毕信号
    ui_load_finish = pyqtSignal()

    ''' UI界面基础类'''
    def __init__(self):
        '''对象初始化'''
        super(UIBase, self).__init__()
        self.name_in_qml = 'this_model'

    #@abstractmethod
    def qml_url(self):
        '''qml ui 文件路径.string 类型'''
        pass

    def connect_signal(self):
        '''建立qml对象和c++对象的signal连接'''
        pass

    def load_qml(self, qml_engine):
        ''' 加载qml ui描述文件 '''
        self.context = QQmlContext(qml_engine.rootContext())
        self.context.setContextProperty(self.name_in_qml, self)
        self.component = QQmlComponent(qml_engine)
        self.component.statusChanged.connect(self.qml_load_status_changed)
        self.component.loadUrl(QUrl(self.qml_url()))

    @pyqtSlot(QQmlComponent.Status)
    def qml_load_status_changed(self,status):
        '''qml ui 描述文件加载状态通知'''
        #print('qml load status ' + status)
        if status == 0:#QQmlComponent.Status.NULL:
            return
        if status == 2:#QQmlComponent.Status.Loading:
            return
        if status == 1:#QQmlComponent.Status.Ready:
            self.ui_qml_object = self.component.create(self.context)
            if type(self.ui_qml_object) == QQuickWindow:
                self.rootObject = self.ui_qml_object.contentItem()
            self.ui_qml_object.show()
            self.connect_signal()
            self.ui_load_finish.emit()
            return
        if status == 3:#QQmlComponent::Error
            for err in self.component.errors():
                print(err.toString())

