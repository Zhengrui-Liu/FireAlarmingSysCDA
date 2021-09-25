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

class SensorData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
	DEFAULT_SENSOR_TYPE = 0
	HUMIDITY_SENSOR_TYPE = 1
	PRESSURE_SENSOR_TYPE = 2
	TEMP_SENSOR_TYPE = 3
		
	def __init__(self, sensorType = DEFAULT_SENSOR_TYPE, name = ConfigConst.NOT_SET,d = None):
		"""
		Constructor:
		@param sensorType = DEFAULT_SENSOR_TYPE
		@param d = None
		
		"""
		super(SensorData, self).__init__(name = name, d = d)
		
		if d:
			self.value = d['value']
			self.sensorType = d['sensorType']
		else:
			self.value = self.DEFAULT_VAL
			self.sensorType = sensorType
	
	def getSensorType(self) -> int:
		"""
		Returns the sensor type to the caller.
		
		@return int
		"""
		return self.sensorType
	
	def setSensorType(self, newType):
		"""
		setSensorType
		@param newType
		"""
		self.sensorType = newType
	
	def getValue(self) -> float:
		"""
		getValue
		@return: float
		"""
		return self.value
	
	def setValue(self, newVal: float):
		"""
		setValue
		@param: newVal:float
		"""
		self.value = newVal
		
	def _handleUpdateData(self, data):
		"""
		If there is no err in data: set a new value to it
		@param data 
		"""
		if data.hasError == False:
			self.setValue(data.value)
