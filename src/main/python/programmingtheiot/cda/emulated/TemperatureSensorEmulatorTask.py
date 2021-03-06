#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.SensorData import SensorData
import logging
import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator

from pisense import SenseHAT

class TemperatureSensorEmulatorTask(BaseSensorSimTask):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, dataSet = None):
		"""Constructor: determine if emulator is used
		dataSet: DataSet
		"""
		super(TemperatureSensorEmulatorTask, self).__init__(sensorName=ConfigConst.TEMP_SENSOR_NAME, sensorType = SensorData.TEMP_SENSOR_TYPE, minVal = SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP, maxVal = SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
		self.configUtil = ConfigUtil()
		if self.configUtil.getBoolean(self, ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_SENSE_HAT_KEY) is False:
			self.sh = SenseHAT(emulate = True)
		else:
			self.sh = SenseHAT(emulate = False)
	
	def generateTelemetry(self) -> SensorData:
		"""Get pressure data from emulator
		return SensorData
		"""
		sensorData = SensorData(name = ConfigConst.TEMP_SENSOR_NAME, sensorType = self.sensorType)
		sensorVal = self.sh.environ.temperature		
		sensorData.setValue(sensorVal)
		self.latestSensorData = sensorData
		logging.info("Debug   generateTelemetry TempSensorEmulatorTask value= "+str(sensorVal))
		return sensorData
