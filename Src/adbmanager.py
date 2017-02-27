# -*- coding:UTF-8 -*-

'''
adb 管理
'''

import os.path as op

from adb import adb_commands
from adb import sign_m2crypto

class AdbManager:
    '''
    adb管理器
    '''
    def __init__(self):
        '''init'''
        pass
    def connect(self):
        '''
        连接android设备
        '''
        # KitKat+ devices require authentication
        self.signer = sign_m2crypto.M2CryptoSigner(
            op.expanduser('~/.android/adbkey'))
        # Connect to the device
        self.device = adb_commands.AdbCommands.ConnectDevice(
            rsa_keys=[self.signer])

        print(self.device.Shell('pwd'))