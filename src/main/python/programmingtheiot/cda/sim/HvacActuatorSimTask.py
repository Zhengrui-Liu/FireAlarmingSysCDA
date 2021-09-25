#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import random

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask
import programmingtheiot.common.ConfigConst as ConfigConst

class HvacActuatorSimTask(BaseActuatorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		"""
		Constructor:
		
		"""
		super(HvacActuatorSimTask, self).__init__(actuatorName = ConfigConst.HVAC_ACTUATOR_NAME, actuatorType = ActuatorData.HVAC_ACTUATOR_TYPE, simpleName = "HVAC")
		
	def activateActuator(self, val: float) -> bool:
		"""
		Turn actuator on:
		@param val: float
		@return: bool
		"""
		logging.info("Emulating HVAC actuator ON:")
		super().activateActuator(val)
		print("*******")
		print("* O N *")
		print("*******")
		print("HVAC VALUE ->", val)
		print("=======")
		
		
	def deactivateActuator(self) -> bool:
		"""
		Turn actuator off:
		@return: bool
		"""
		logging.info("Emulating HVAC actuator OFF:")
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
		if super().updateActuator(data) == True:
			return self.latestActuatorData
