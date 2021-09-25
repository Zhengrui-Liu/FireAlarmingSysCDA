#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 
import logging
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask
import programmingtheiot.common.ConfigConst as ConfigConst

class HumidifierActuatorSimTask(BaseActuatorSimTask):
	"""
	This is a simple wrapper for an Actuator abstraction - it provides
	a container for the actuator's state, value, name, and status. A
	command variable is also provided to instruct the actuator to
	perform a specific function (in addition to setting a new value
	via the 'val' parameter.
	
	"""

	def __init__(self):
		"""
		Constructor:
		
		"""
		super(HumidifierActuatorSimTask, self).__init__(actuatorName = ConfigConst.HUMIDIFIER_ACTUATOR_NAME, actuatorType = ActuatorData.HUMIDIFIER_ACTUATOR_TYPE, simpleName = "HUMIDIFIER")
		
	def activateActuator(self, val: float) -> bool:
		"""
		Turn actuator on:
		@param val: float
		@return: bool
		"""
		logging.info("Emulating HUMIDIFIER actuator ON:")
		super().activateActuator(val)
		print("*******")
		print("* O N *")
		print("*******")
		print("HUMIDIFIER VALUE -> ", val)
		print("=======")
		
	def deactivateActuator(self) -> bool:
		"""
		Turn actuator off:
		@return: bool
		"""
		logging.info("Emulating HUMIDIFIER actuator OFF:")
		super().deactivateActuator()
		print("*******")
		print("* OFF *")
		print("*******")
		
	def updateActuator(self, data: ActuatorData) -> ActuatorData:
		"""
		Renew the latest actuator data
		@param data: ActuatorData
		@return: ActuatorData
		"""
		if(super().updateActuator(data) == True):
			return self.latestActuatorData
		