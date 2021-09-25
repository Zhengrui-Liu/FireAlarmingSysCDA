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

class HumidifierEmulatorTask(BaseActuatorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		"""
		Constructor
		check the configuration file to determine if use a emulator
		"""
		super(HumidifierEmulatorTask, self).__init__(actuatorName = ConfigConst.HUMIDIFIER_ACTUATOR_NAME, actuatorType = ActuatorData.HUMIDIFIER_ACTUATOR_TYPE, simpleName = "HUMIDIFIER")
		# Create an instance of SenseHAT and set the emulate flag to True if running the emulator, or False if using real hardware
		# This can be read from ConfigUtil using the ConfigConst.CONSTRAINED_DEVICE section and the ConfigConst.ENABLE_SENSE_HAT_KEY
		# If the ConfigConst.ENABLE_SENSE_HAT_KEY is False, set the emulate flag to True, otherwise set to False
		configUtil = ConfigUtil()
		if configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_SENSE_HAT_KEY) is False:
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
		# NOTE: use the API instructions for pisense for help
		if cmd == ActuatorData.COMMAND_ON:
			self.activateActuator(val)
			if self.sh.screen:
				# create a message with the value and an 'ON' message, then scroll it across the LED display
				if self.state is "OFF":
					message = str("Humidifier: ON / Target HMD is: "+str(val))
					self.state = "ON"
					self.sh.screen.scroll_text(message)
				return 0
			else:
				logging.warning("No SenseHAT LED screen instance to update.")
				return -1
		else:
			self.deactivateActuator()
			if self.sh.screen:
				if self.state is "ON":
					message = str("Humidifier: OFF")
					self.state = "OFF"
					self.sh.screen.scroll_text(message)
				return 0
			else:
				logging.warning("No SenseHAT LED screen instance to clear / close.")
				return -1
