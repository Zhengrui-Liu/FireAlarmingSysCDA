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

from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst

class BaseSensorSimTask():
	"""
	Shell representation of class for student implementation.
	
	"""

	DEFAULT_MIN_VAL = 0.0
	DEFAULT_MAX_VAL = 1000.0
	
	def __init__(self, sensorName = ConfigConst.NOT_SET, sensorType: int = SensorData.DEFAULT_SENSOR_TYPE, dataSet = None, minVal: float = DEFAULT_MIN_VAL, maxVal: float = DEFAULT_MAX_VAL):
		"""
		Constructor:
		@param sensorType: int = SensorData.DEFAULT_SENSOR_TYPE
		@param dataSet : dataSet = None
		@param minVal: float = DEFAULT_MIN_VAL
		@param maxVal: float = DEFAULT_MAX_VAL
		
		"""
		self.sensorName = sensorName
		self.sensorType = sensorType
		self.dataSet = dataSet
		self.minVal = minVal
		self.maxVal =maxVal
		self.latestSensorData = None
		self.curDataIndex = 0
		self.useRandomizer = False
		if(dataSet == None):
			self.useRandomizer = True
	
	def generateTelemetry(self) -> SensorData:
		"""
		Get the current sensor data based on the dataset and its index
		@return: SensorData
		"""
		sd = SensorData(name = self.sensorName)
		sd.setSensorType(self.sensorType)
		if self.useRandomizer == True:
			sd.setValue(random.uniform(self.minVal,self.maxVal))
		else:
			sd.setValue(self.dataSet.getDataEntry(self.curDataIndex))
			#logging.info(str(sd.getValue()))
			self.curDataIndex = self.curDataIndex+1
			if(self.curDataIndex >= self.dataSet.dataEntries.size):
				self.curDataIndex = 0
		self.latestSensorData = sd
		return self.latestSensorData
	
	def getTelemetryValue(self) -> float:
		"""
		Get the value of SensorData got from two paths
		@return: float
		"""
		if(self.latestSensorData != None):
			return self.latestSensorData.getValue()
		else:
			return self.generateTelemetry()
	