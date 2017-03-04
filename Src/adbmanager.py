# -*- coding:UTF-8 -*-

'''
adb 管理
'''

import os.path as op
import subprocess
import chardet

class AdbManager:
    '''
    adb管理器
    '''

    __instance = None
    def __new__(cls):
        if AdbManager.__instance is None:
            AdbManager.__instance = object.__new__(cls)
        return AdbManager.__instance

    def __init__(self):
        '''init'''
        pass
    def connect(self):
        '''
        连接android设备
        return: str设备编码 or None
        '''
        return self.adb_devices()

    def adb_devices(self):
        out = self.adb_commond("devices")
        outs = str(out, chardet.detect(out)['encoding'])
        lines = outs.split('\n')
        if lines[0] == 'List of devices attached':
            if len(lines) > 1 and lines[1] != '':
                device = lines[1].split('\t')
                return device[0]
            else:
                print("no find device")
                return None
        else:
            print(outs)
            return None

    def adb_commond(self, cmd):
        return subprocess.check_output(['adb', cmd])