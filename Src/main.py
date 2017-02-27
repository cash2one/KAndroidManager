# -*- coding: UTF-8 -*-

'''
主入口文件
PyQt5 API http://pyqt.sourceforge.net/Docs/PyQt5/
'''

import sys
from mainui import MainUI
from tinyui.uimanager import uimanager
from PyQt5.QtGui import QGuiApplication

if __name__ == '__main__':

    # Create the application instance.
    app = QGuiApplication(sys.argv)
    uimanager.init()

    main_ui = uimanager.create_ui(MainUI)

    app.exec()


    

