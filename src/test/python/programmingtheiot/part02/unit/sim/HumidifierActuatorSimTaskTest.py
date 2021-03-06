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

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.HumidifierActuatorSimTask import HumidifierActuatorSimTask

class HumidifierActuatorSimTaskTest(unittest.TestCase):
	"""
	This test case class contains very basic unit tests for
	HumidifierActuatorSimTask. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	DEFAULT_VAL_A = 18.2
	DEFAULT_VAL_B = 21.4
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing HumidifierActuatorSimTask class...")
		self.hSimTask = HumidifierActuatorSimTask()
		
	def setUp(self):
		pass

	def tearDown(self):
		pass

	def testUpdateActuator(self):
		"""Test Simulator
		Test Humidifier update
		"""
		ad = ActuatorData(actuatorType = ActuatorData.HUMIDIFIER_ACTUATOR_TYPE)
		ad.setCommand(ActuatorData.COMMAND_ON)
		ad.setValue(self.DEFAULT_VAL_A)
		self.assertTrue(self.hSimTask.updateActuator(ad))
		adr = self.hSimTask.getLatestActuatorResponse()
		
		self.assertIsNotNone(adr)
		self.assertEquals(adr.getValue(), self.DEFAULT_VAL_A)
		logging.info("ActuatorData: " + str(adr))
		
		ad.setValue(self.DEFAULT_VAL_B)
		self.assertTrue(self.hSimTask.updateActuator(ad))
		adr = self.hSimTask.getLatestActuatorResponse()
		
		self.assertIsNotNone(adr)
		self.assertEquals(adr.getValue(), self.DEFAULT_VAL_B)
		logging.info("ActuatorData: " + str(adr))
		
		ad.setCommand(ActuatorData.COMMAND_OFF)
		self.assertTrue(self.hSimTask.updateActuator(ad))
		adr = self.hSimTask.getLatestActuatorResponse()
		
		self.assertIsNotNone(adr)
		self.assertEquals(adr.getCommand(), ActuatorData.COMMAND_OFF)
		logging.info("ActuatorData: " + str(adr))
			
if __name__ == "__main__":
	unittest.main()
	