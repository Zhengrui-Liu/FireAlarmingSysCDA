#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import unittest

from time import sleep

from programmingtheiot.cda.system.ActuatorAdapterManager import ActuatorAdapterManager
from programmingtheiot.common.DefaultDataMessageListener import DefaultDataMessageListener

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.common.ConfigUtil import ConfigUtil
import programmingtheiot.common.ConfigConst as ConfigConst

class ActuatorAdapterManagerTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	ActuatorSimAdapterManager. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing ActuatorAdapterManager class...")
		configUtil = ConfigUtil()
		useEmulator = configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY)
		logging.info(str(useEmulator))
		self.defaultMsgListener = DefaultDataMessageListener()
		self.actuatorAdapterMgr = ActuatorAdapterManager(useEmulator)
		self.actuatorAdapterMgr.setDataMessageListener(self.defaultMsgListener)
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testHumidifierSimulation(self):
		"""Test Actuators
		Test simulation of Humidifier
		"""
		ad = ActuatorData(actuatorType = ActuatorData.HUMIDIFIER_ACTUATOR_TYPE)
		ad.setValue(50.0)
		
		ad.setCommand(ActuatorData.COMMAND_ON)
		self.actuatorAdapterMgr.sendActuatorCommand(ad)
		
		ad.setCommand(ActuatorData.COMMAND_OFF)
		self.actuatorAdapterMgr.sendActuatorCommand(ad)

	def testHvacSimulation(self):
		"""Test Actuators
		Test simulation of HVAC
		"""
		ad = ActuatorData(actuatorType = ActuatorData.HVAC_ACTUATOR_TYPE)
		ad.setValue(22.5)
		
		ad.setCommand(ActuatorData.COMMAND_ON)
		self.actuatorAdapterMgr.sendActuatorCommand(ad)
		
		ad.setCommand(ActuatorData.COMMAND_OFF)
		self.actuatorAdapterMgr.sendActuatorCommand(ad)

if __name__ == "__main__":
	unittest.main()
	