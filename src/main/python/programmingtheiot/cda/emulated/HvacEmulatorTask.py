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

class HvacEmulatorTask(BaseActuatorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self):
		"""Constructor
		check the configuration file to determine if use a emulator
		"""
		super(HvacEmulatorTask, self).__init__(actuatorName = ConfigConst.HVAC_ACTUATOR_NAME, actuatorType = ActuatorData.HVAC_ACTUATOR_TYPE, simpleName = "HVAC")
		configUtil = ConfigUtil()
		if configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_SENSE_HAT_KEY)  is False:
			self.sh = SenseHAT(emulate = True)
		else:
			self.sh = SenseHAT(emulate = False)
		self.state = "OFF"


### need a update???

	def _handleActuation(self, cmd: int, val: float = 0.0, stateData: str = None) -> int:
		"""Implement the function of showing related value on led screen
		cmd: int
		val: float = 0.0
		stateData: str = None
		return int 
		"""
		print("HAVACEMUTSK/_handleActuation/commond="+str(cmd))
		if cmd == ActuatorData.COMMAND_ON:
			if self.sh.screen:
				# create a message with the value and an 'ON' message, then scroll it across the LED display
				if self.state is "OFF":
					self.state = "ON"
					message = str("TMP Actuation ON/Target TMP now is:"+str(val))
					self.sh.screen.scroll_text(message)
				return 0
			else:
				logging.warning("No SenseHAT LED screen instance to update.")
				return -1
		else:
			if self.sh.screen:
				if self.state is "ON":
					self.state = "OFF"
					message = str("HvacEmuTsk: OFF!")
					self.sh.screen.scroll_text(message)
				return 0
			else:
				logging.warning("No SenseHAT LED screen instance to clear / close.")
				return -1
	