#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.SensorData import SensorData

class TemperatureSensorSimTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, dataSet = None):
		"""
		Constructor:
		@param dataSet: dataSet = None
		"""
		super(TemperatureSensorSimTask, self).__init__(sensorName = ConfigConst.TEMP_SENSOR_NAME, sensorType =  SensorData.TEMP_SENSOR_TYPE, dataSet = dataSet, minVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP, maxVal = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
	
	def generateTelemetry(self) -> SensorData:
		"""
		Get the current sensor data based on the dataset and its index
		@return: SensorData
		"""
		#a = super().generateTelemetry()
		#logging.info("temp data value:"+ str(a.getValue()))
		return super().generateTelemetry()
	
	
	def getTelemetryValue(self) -> float:
		"""
		Get the value of SensorData got from two paths
		@return: float
		"""
		return super().getTelemetryValue()
	