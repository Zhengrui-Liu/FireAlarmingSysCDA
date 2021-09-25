'''
Created on Dec 13, 2020

@author: liu.zhengr
'''


import logging
import unittest

from time import sleep

from programmingtheiot.cda.connection.ImageSocketConnector import ImageSocketConnector





class testSocket(unittest.TestCase):
    
     
    def testConnect(self):
        """Test socket send picture
        Using Socket
        """
        self.skt = ImageSocketConnector()
        self.skt.send("/Users/liu.zhengr/Downloads/fire01.jpeg")
        