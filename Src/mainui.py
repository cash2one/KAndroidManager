# -*- coding: UTF-8 -*-

from tinyui.uibase import UIBase

class MainUI(UIBase):
    '''主界面'''
    def qml_url(self):
        return 'ui/mainui.qml'

    def connect_signal(self):
        '''
        参考：http://doc.qt.io/qt-5/qtqml-cppintegration-interactqmlfromcpp.html
        '''
        self.rootObject.sig_connect.connect(self.on_connect)

    def on_connect(self):
        print('mainui on connect')