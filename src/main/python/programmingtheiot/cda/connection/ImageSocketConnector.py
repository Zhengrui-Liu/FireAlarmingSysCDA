'''
Created on Dec 12, 2020

@author: liu.zhengr
'''
import socket
import os
import sys
import struct


class ImageSocketConnector():
    
    def __init__(self):
        self.address = ('127.0.0.1', 5612)

    def send(self, filePath:str):
        """Send picture to server
        param: filePath  File path
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(self.address)
        except socket.error as msg:
            print(msg)
            sys.exit(1)

        if os.path.isfile(filePath):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fileinfo_size = struct.calcsize('128sl')
            # 定义文件头信息，包含文件名和文件大小
            #fhead = struct.pack('128sl', bytes(os.path.basename(filepath).encode('utf-8')),os.stat(filepath).st_size)
            #print("1")
            #s.send(fhead)
            print ('client filepath: {0}'.format(filePath))
            fp = open(filePath, 'rb')
            while 1:
                data = fp.read(1024)
                if not data:
                    print ('{0} file send over...'.format(filePath))
                    break
                s.send(data)
        s.close()