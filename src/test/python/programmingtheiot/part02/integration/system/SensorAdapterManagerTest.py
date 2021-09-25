#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 
import sys
import os
path = "/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/"
sys.path.append(path)
import logging
import unittest

from time import sleep
from programmingtheiot.common.ConfigUtil import ConfigUtil
import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.DefaultDataMessageListener import DefaultDataMessageListener
from programmingtheiot.cda.system.SensorAdapterManager import SensorAdapterManager

class SensorAdapterManagerTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	SensorAdapterManager. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing SensorAdapterManager class...")
		configUtil = ConfigUtil()
		useEmulator = configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
		logging.info(str(useEmulator))
		self.defaultMsgListener = DefaultDataMessageListener()
		self.sensorAdapterMgr = SensorAdapterManager(useEmulator)
		self.sensorAdapterMgr.setDataMessageListener(self.defaultMsgListener)
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testStartAndStopManager(self):
		"""Test Sensors
		Test simulation or emulation of sencehat
		"""
		self.sensorAdapterMgr.startManager()
		
		sleep(20)
		
		self.sensorAdapterMgr.stopManager()

if __name__ == "__main__":
	unittest.main()
	