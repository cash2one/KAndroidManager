from tinyui.uibase import UIBase
from PyQt5.QtCore import pyqtSlot

class FileUI(UIBase):
    '''文件管理UI'''
    def qml_url(self):
        return 'ui/filesui.qml'
        