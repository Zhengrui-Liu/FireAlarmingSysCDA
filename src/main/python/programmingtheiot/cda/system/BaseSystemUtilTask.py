#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#
import logging
from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst

class BaseSystemUtilTask():
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self,sensorName = ConfigConst.NOT_SET):
		###
		# TODO: fill in the details here
		"""
		Constructor
		"""
		self.latestSensorData = None
		self.sensorName = sensorName
		
		
		pass
	
	def generateTelemetry(self) -> SensorData:
		"""
		return a new sensorData
		@return: SensorData
		"""
		
		sData = SensorData(name = self.sensorName)
		self.latestSensorData = sData
		self.latestSensorData.setValue(self._getSystemUtil())
		return self.latestSensorData
	
		
	def getTelemetryValue(self) -> float:
		"""
		get, log out and return the system usage info
		
		@return: float
		"""
		if self.latestSensorData is None:
			self.generateTelemetry()
			return self.latestSensorData.getValue()
		
		val  = self._getSystemUtil()
		logging.info("Create a instance of " + self.__class__.__name__) # log out class name
		logging.info("val = " + str(val)) # log out usage information
		return val;
	
	def _getSystemUtil(self) -> float:
		"""
		Template method implemented by sub-class.
		
		Retrieve the system utilization value as a float.
		
		@return float
		"""
		pass
		