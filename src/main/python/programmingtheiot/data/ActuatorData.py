#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.BaseIotData import BaseIotData
import programmingtheiot.common.ConfigConst as ConfigConst

class ActuatorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_COMMAND = 0
	COMMAND_OFF = DEFAULT_COMMAND
	COMMAND_ON = 1

	# for now, actuators will be 1..99
	# and displays will be 100..1999
	DEFAULT_ACTUATOR_TYPE = 0
	
	HVAC_ACTUATOR_TYPE = 1
	HUMIDIFIER_ACTUATOR_TYPE = 2
	LED_DISPLAY_ACTUATOR_TYPE = 100
	
	DEFAULT_STATE_DATA = None
	DEFAULT_ASRESPONSE = False

	def __init__(self, actuatorType = DEFAULT_ACTUATOR_TYPE, name = ConfigConst.NOT_SET, d = None):
		"""
		Constructor:
		@param actuatorType = DEFAULT_ACTUATOR_TYPE
		@param d = None
		"""
		super(ActuatorData, self).__init__(name = name,d = d)
		
		self.asResponse = False
		self.actuatorType = actuatorType
		
		if d:
			self.command = d['command']
			self.stateData = d['stateData']
			self.value = d['curValue']
			self.actuatorType = d['actuatorType']
		else:
			self.command = self.DEFAULT_COMMAND
			self.stateData = None
			self.value = self.DEFAULT_VAL
			self.actuatorType = actuatorType
		
	
	def getCommand(self) -> int:
		"""
		Get Command
		@return int
		"""
		return self.command
	
	def getStateData(self) -> str:
		"""
		Get StateData
		@return: str
		"""
		return self.stateData
	
	def getValue(self) -> float:
		"""
		Get Value
		@return: float
		"""
		return self.value
	
	def getActuatorType(self) -> str:
		"""
		Get Actuator Type
		@return:  str
		"""
		return self.actuatorType
	
	def isResponseFlagEnabled(self) -> bool:
		"""
		Judge if it is a Response
		@return: bool
		"""
		return False
	
	def setCommand(self, command: int):
		"""
		Set command:
		@param command: int
		"""
		self.command = command
	
	def setAsResponse(self):
		"""
		Set asResponse
		"""
		self.asResponse = True
		
	def setStateData(self, stateData: str):
		"""
		setStateData
		@param stateData: str
		"""
		self.stateData = stateData
	
	def setValue(self, val: float):
		"""
		setValue
		@param val: float
		"""
		self.value = val
		
	def setActuatorType(self, val: str):
		"""
		setActuatorType
		@param val: str
		"""
		self.actuatorType = val
		
	def _handleUpdateData(self, data):
		"""
		use data to renew the class data
		@param: data 
		"""
		if data.hasErrorFlag() == False:
			self.setValue(data.value)
			self.setCommand(data.command)
			self.setStateData(data.stateData)
		