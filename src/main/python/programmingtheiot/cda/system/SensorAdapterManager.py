#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from apscheduler.schedulers.background import BackgroundScheduler

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.DefaultDataMessageListener import DefaultDataMessageListener

from programmingtheiot.cda.sim.TemperatureSensorSimTask import TemperatureSensorSimTask
from programmingtheiot.cda.sim.HumiditySensorSimTask import HumiditySensorSimTask
from programmingtheiot.cda.sim.PressureSensorSimTask import PressureSensorSimTask
from programmingtheiot.cda.sim.SensorDataGenerator import SensorDataGenerator
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil


class SensorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, useEmulator: bool = True, pollRate: int = 5, allowConfigOverride: bool = True):
		"""
		Constructor:
		@note: 1. Check if s simulator is used
		@note: 2. create a dataSetGenerator and create a simulated data
		@param useEmulator: bool = False
		@param pollRate: int = 5
		@param allowConfigOverride: bool = True
		"""
		self.useEmulator = useEmulator
		self.pollRate = pollRate
		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self.handleTelemetry, 'interval', seconds = self.pollRate,max_instances=100)
		#self.dataMsgListener
		if(self.useEmulator == True):
			logging.info("Emulators will be used!")
			humidityModule = __import__('programmingtheiot.cda.emulated.HumiditySensorEmulatorTask', fromlist = ['HumiditySensorEmulatorTask'])
			heClazz = getattr(humidityModule, 'HumiditySensorEmulatorTask')
			self.humidityEmulator = heClazz()
			pressureModule = __import__('programmingtheiot.cda.emulated.PressureSensorEmulatorTask', fromlist = ['PressureSensorEmulatorTask'])
			heClazzP = getattr(pressureModule, 'PressureSensorEmulatorTask')
			self.pressureEmulator = heClazzP()
			tempModule = __import__('programmingtheiot.cda.emulated.TemperatureSensorEmulatorTask', fromlist = ['TemperatureSensorEmulatorTask'])
			heClazz2 = getattr(tempModule, 'TemperatureSensorEmulatorTask')
			self.tempEmulator = heClazz2()
		else:
			logging.info("Simulators will be used!")
			self.dataGenerator = SensorDataGenerator()
			configUtil = ConfigUtil()
			humidityFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.HUMIDITY_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_ENV_HUMIDITY)
			humidityCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.HUMIDITY_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_ENV_HUMIDITY)
			pressureFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.PRESSURE_SIM_FLOOR_KEY, SensorDataGenerator.LOW_NORMAL_ENV_PRESSURE)
			pressureCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.PRESSURE_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_ENV_PRESSURE)
			tempFloor = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TEMP_SIM_CEILING_KEY, SensorDataGenerator.LOW_NORMAL_INDOOR_TEMP)
			tempCeiling = configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TEMP_SIM_CEILING_KEY, SensorDataGenerator.HI_NORMAL_INDOOR_TEMP)
			humidityData = self.dataGenerator.generateDailyEnvironmentHumidityDataSet(minValue = humidityFloor, maxValue = humidityCeiling, useSeconds = False)
			pressureData = self.dataGenerator.generateDailyEnvironmentPressureDataSet(minValue = pressureFloor, maxValue = pressureCeiling, useSeconds = False)
			tempData = self.dataGenerator.generateDailyIndoorTemperatureDataSet(minValue = tempFloor, maxValue = tempCeiling, useSeconds = False)
			self.humiditySensorSimTask = HumiditySensorSimTask(humidityData)
			self.pressureSensorSimTask = PressureSensorSimTask(pressureData)
			self.tempSensorSimTask = TemperatureSensorSimTask(tempData)

	def handleTelemetry(self):
		"""
		Use listener to handle the generated dataset
		"""
		if(self.useEmulator == False and self.dataMsgListener != None):
			self.dataMsgListener.handleSensorMessage(self.humiditySensorSimTask.generateTelemetry())
			self.dataMsgListener.handleSensorMessage(self.pressureSensorSimTask.generateTelemetry())
			self.dataMsgListener.handleSensorMessage(self.tempSensorSimTask.generateTelemetry())
		else:
			self.dataMsgListener.handleSensorMessage(self.humidityEmulator.generateTelemetry())
			#logging.info("Debug   handleTelemetry SensorAdapterManager humi")
			self.dataMsgListener.handleSensorMessage(self.pressureEmulator.generateTelemetry())
			#logging.info("Debug   handleTelemetry SensorAdapterManager pres")
			self.dataMsgListener.handleSensorMessage(self.tempEmulator.generateTelemetry())
			#logging.info("Debug   handleTelemetry SensorAdapterManager temp")
			
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		"""
		Get a listener
		@param listener: IDataMessageListener
		@return: bool
		"""
		if(listener!=None):
			self.dataMsgListener = listener
			return True
		else:
			return False
			
	
	def startManager(self):
		"""
		Start schedular
		"""
		self.scheduler.start()
		
	def stopManager(self):
		"""
		Shutdown Schedular
		"""
		self.scheduler.shutdown()
