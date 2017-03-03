# -*- coding: UTF-8 -*-

'''
管理设备的文件资源
'''

from tinyui.uimanager import uimanager
from filesui import FileUI
from tinyui.listmodel import QObjectListModel
from PyQt5.QtCore import QObject, pyqtProperty, QVariant, QAbstractListModel,QModelIndex, Qt, pyqtSignal

class FileManager:
    '''管理手机文件'''

    __instance = None
    def __new__(cls):
        if FileManager.__instance is None:
            FileManager.__instance = object.__new__(cls)
        return FileManager.__instance

    def __init__(self):
        '''初始化'''
        pass

    def show(self):
        '''显示界面'''
        self.ui = uimanager.create_ui(FileUI)
        self.infos = self.dir("/")
        self.ui.set_context_property("pathmodel", self.infos)

    def dir(self,path):
        '''获取path目录下的文件信息'''
        #infos = QObjectListModel()
        infos = list()
        infos.append(PathInfo("xx", False))
        infos.append(PathInfo("folder", True))

        self.curpath = path

        return PathInfoListModel(infos)
        #return infos

    def back(self):
        '''返回上一级'''
        self.dir(self.curpath)

class PathInfo(QObject):
    '''目录信息'''
    def __init__(self, path, folder):
        super(PathInfo, self).__init__(None)
        self._path = path
        self._folder = folder

    #@pyqtProperty(str)
    def get_path(self):
        return self._path

    #@pyqtProperty(str)
    def get_folder(self):
        return self._folder

    pathChanged = pyqtSignal()
    folderChanged = pyqtSignal()
    path = pyqtProperty(str, get_path, notify=pathChanged)
    folder = pyqtProperty(bool, get_folder, notify=folderChanged)

class PathInfoListModel(QAbstractListModel):

    path_role = Qt.UserRole + 1
    folder_role = Qt.UserRole + 2

    def __init__(self, plist, parent=None):
        super(PathInfoListModel, self).__init__(parent)
        self.listdata = plist

    def roleNames(self):
        '''
        要暴露给qml使用的role。可以理解为，qml通过role名，索引到roleid，然后当使用role时，
        会调用data方法，参数role就是对应的roleid. 然后，在data里返回对应的数据即可。
        roleid和rolename的映射就是qml和c++数据沟通的桥梁。
        qt文档中，使用的是QHash，pyqt里没有QHash。还让我纠结了很久:(
        '''
        roles = {}
        roles[self.path_role] = b"path"
        roles[self.folder_role] = b"folder"
        return roles

    def rowCount(self, parent=QModelIndex()): 
        print(len(self.listdata))
        return len(self.listdata) 

    def data(self, index, role): 
        #print("called data " + str(index.row()) + " " + str(role))
        if index.isValid():
            if role == self.path_role:
                return self.listdata[index.row()].path
            if role == self.folder_role:
                return self.listdata[index.row()].folder
        else: 
            return QVariant()


