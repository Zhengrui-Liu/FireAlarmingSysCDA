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
import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.data.ActuatorData import ActuatorData

class BaseActuatorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, actuatorName = ConfigConst.NOT_SET, actuatorType: int = ActuatorData.DEFAULT_ACTUATOR_TYPE, simpleName: str = "Actuator"):
		"""
		Constructor:
		@param param: actuatorType: int = ActuatorData.DEFAULT_ACTUATOR_TYPE
		@param param: simpleName: str = "Actuator"
		"""
		self.actastorType = actuatorType
		self.simpleName = simpleName
		self.latestActuatorData = ActuatorData(name = actuatorName)
		
	def activateActuator(self, val: float) -> bool:
		"""
		Set the latestActuatorData's commond code : on
		@param val: float
		@return: bool
		"""
		logging.info("Received an ON commond: " + str(val))
		self.latestActuatorData.setCommand(ActuatorData.COMMAND_ON)
		return True
		
	def deactivateActuator(self) -> bool:
		"""
		Set the latestActuatorData's commond code : off
		@return: bool
		"""
		logging.info("Received an OFF commond.")
		self.latestActuatorData.setCommand(ActuatorData.COMMAND_OFF)
		return True
		
	def getLatestActuatorResponse(self) -> ActuatorData:
		"""
		getLatestActuatorResponse
		
		@return: ActuatorData
		"""
		return self.latestActuatorData
	
	def getSimpleName(self) -> str:
		"""
		getSimpleName
		@return: str
		"""
		return self.simpleName
	
	def updateActuator(self, data: ActuatorData) -> bool:
		"""
		Based on the new data, control the actuator
		@param  data: ActuatorData
		@return: bool
		"""
		#logging.info("************************"+str(data.value)+"**********************")
		if(data != None and data.getValue != None):
			logging.info("Actuator command received. Processing...")
			code = self._handleActuation(data.getCommand(),data.getValue(),data.getStateData())
			self.latestActuatorData = data
			self.latestActuatorData.setStatusCode(code)
			"""
			if(data.command == ActuatorData.COMMAND_OFF):
				self.deactivateActuator()
				self.latestActuatorData = data
				self.latestActuatorData.setStatusCode(ActuatorData.STATUS_IDLE)
			else:
				self.activateActuator(data.getValue())
				self.latestActuatorData = data
				self.latestActuatorData.setStatusCode(ActuatorData.STATUS_ACTIVE)
			"""
		self.latestActuatorData.setAsResponse()
		return True
			
	
	def _handleActuation(self, cmd: int, val: float = 0.0, stateData: str = None) -> int:
		"""
		`Simple implementation that invokes activate or deactivate in super class.
	
		@param cmd The actuation command to process.
		@param stateData The string state data to use in processing the command.
		@return int The status code from the actuation call.
		"""
		if cmd is ActuatorData.COMMAND_ON:
			self.activateActuator(val)
		elif cmd is ActuatorData.COMMAND_OFF:
			self.deactivateActuator()
	
		return 0
			
		