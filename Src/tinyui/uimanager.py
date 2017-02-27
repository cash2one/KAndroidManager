# -*- coding: UTF-8 -*-

'''
Qml UI界面管理器。
提供创建，销毁等操作。
'''

from PyQt5.QtQml import QQmlApplicationEngine

class UIManager:
    '''UI 管理器'''
    def __init__(self):
        '''对象初始化'''
        #self.qml_engine = QQmlApplicationEngine()

    def init(self):
        '''
        因为采用模块的方式来实现单例。所以qmlengine的初始化要在QApplication object创建
        之后显示调用
        '''
        self.qml_engine = QQmlApplicationEngine()

    def create_ui(self, uiclass):
        '''
        创建UI。ui对象生命周期由调用者管理。
        return: ui object
        '''
        ui = uiclass()
        ui.load_qml(self.qml_engine)
        return ui

uimanager = UIManager()