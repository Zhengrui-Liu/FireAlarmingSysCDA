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
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataSet
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
import programmingtheiot.common.ConfigConst as ConfigConst


from programmingtheiot.data.SensorData import SensorData

class HumiditySensorSimTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, dataSet = None):
		"""
		Constructor:
		@param dataSet: dataSet = None
		"""
		super(HumiditySensorSimTask, self).__init__(sensorName = ConfigConst.HUMIDITY_SENSOR_NAME, sensorType = SensorData.HUMIDITY_SENSOR_TYPE, dataSet = dataSet, minVal = SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY, maxVal = SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
	
	def generateTelemetry(self) -> SensorData:
		"""
		Get the current sensor data based on the dataset and its index
		@return: SensorData
		"""
		#a = super().generateTelemetry()
		#logging.info("humidify data value:"+ str(a.getValue()))
		return super().generateTelemetry()
	
	def getTelemetryValue(self) -> float:
		"""
		Get the value of SensorData got from two paths
		@return: float
		"""
		return super().getTelemetryValue()
	