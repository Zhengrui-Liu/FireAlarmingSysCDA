#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.BaseActuatorSimTask import BaseActuatorSimTask

from pisense import SenseHAT

class LedDisplayEmulatorTask(BaseActuatorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		"""Constructor
		check the configuration file to determine if use a emulator
		"""
		super(LedDisplayEmulatorTask, self).__init__(actuatorName = ConfigConst.LED_ACTUATOR_NAME, actuatorType = ActuatorData.LED_DISPLAY_ACTUATOR_TYPE, simpleName = "LED_Display")
		configUtil = ConfigUtil()
		if configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_SENSE_HAT_KEY)  is False:
			self.sh = SenseHAT(emulate = True)
		else:
			self.sh = SenseHAT(emulate = False)
		self.state = "OFF"

	def _handleActuation(self, cmd: int, val: float = 0.0, stateData: str = None) -> int:
		"""Implement the function of showing related value on led screen
		cmd: int
		val: float = 0.0
		stateData: str = None
		
		return int 
		"""
		if cmd == ActuatorData.COMMAND_ON:
			if self.sh.screen:
				if self.state is "OFF" :
					self.sh.screen.scroll_text("Pressure below 600!")
					self.state = "ON";
				return 0
			else:
				logging.warning("No SenseHAT LED screen instance to update.")
				return -1
		else:
			if self.sh.screen:
				if self.state is "ON" :
					self.sh.screen.scroll_text("Normal Pressure...")
					self.state = "OFF";
				return 0
			else:
				logging.warning("No SenseHAT LED screen instance to clear / close.")
				return -1
	