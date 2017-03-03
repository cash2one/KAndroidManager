# -*- coding: UTF-8 -*-

from tinyui.uibase import UIBase
from PyQt5.QtCore import pyqtSlot
from filemanager import FileManager

class MainUI(UIBase):
    '''主界面'''
    def qml_url(self):
        return 'ui/mainui.qml'

    def connect_signal(self):
        '''
        参考：http://doc.qt.io/qt-5/qtqml-cppintegration-interactqmlfromcpp.html
        '''
        # 通过qmlengine component 创建的qml对象。应该直接代表qml的rootobject。
        self.ui_qml_object.sig_connect.connect(self.on_connect)

    def on_connect(self):
        '''连接/断开手机连接'''
        print('mainui on connect')

    @pyqtSlot()
    def open_filesmanager(self):
        '''
        打开文件管理
        '''
        print('open file manager')
        FileManager().show()
