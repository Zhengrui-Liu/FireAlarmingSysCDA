#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import _thread

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector
from programmingtheiot.cda.connection.MqttClientConnector import MqttClientConnector
from programmingtheiot.cda.connection.ImageSocketConnector import ImageSocketConnector

from programmingtheiot.cda.system.ActuatorAdapterManager import ActuatorAdapterManager
from programmingtheiot.cda.system.SensorAdapterManager import SensorAdapterManager
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.DefaultDataMessageListener import DefaultDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.data.DataUtil import DataUtil
from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData
from programmingtheiot.common.ConfigConst import CONSTRAINED_DEVICE


class DeviceDataManager(IDataMessageListener):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, enableMqtt: bool = True, enableCoap: bool = False):
		"""Constructor:
		enableMqtt: bool = True
		enableCoap: bool = False
		"""
		#ConfigUtil.getCredentials(self, CONSTRAINED_DEVICE)
		self.counter = 0
		self.enableMqttClient = enableMqtt
		if self.enableMqttClient is True:
			self.mqttClient = MqttClientConnector() 
			self.mqttClient.setDataMessageListener(self)
		self.configUtil = ConfigUtil()
		self.sysPerfManager = SystemPerformanceManager()
		self.sysPerfManager.setDataMessageListener(self)
		self.sensorAdapterManager = SensorAdapterManager()
		self.sensorAdapterManager.setDataMessageListener(self)
		self.actuatorAdapterManager = ActuatorAdapterManager()
		self.actuatorAdapterManager.setDataMessageListener(self)
		self.enableHandleTempChangeOnDevice = self.configUtil.getBoolean(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_HANDLE_TEMP_CHANGE_ON_DEVICE_KEY)
		self.triggerHvacTempFloor = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_FLOOR_KEY);
		self.triggerHvacTempCeiling = self.configUtil.getFloat(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.TRIGGER_HVAC_TEMP_CEILING_KEY);
		self.socketSender = ImageSocketConnector()	
		self.imageSent = 0;
			
			
	def handleActuatorCommandResponse(self, data: ActuatorData) -> bool:
		"""
		Actuator data to Json form
		data: ActuatorData
		 bool
		"""
		logging.info("handleActuatorCommandResponse has been called!")
		jsonData = DataUtil.actuatorDataToJson(self, data)
		logging.info(jsonData)
		#xia ci gai
		#jsonData = data
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_ACTUATOR_RESPONSE_RESOURCE, jsonData)
		
	
	def handleIncomingMessage(self, resourceEnum: ResourceNameEnum, msg: str) -> bool:
		"""
		Json data to Actuator data
		msg: str
		resourceEnum: ResourceNameEnum
		 bool
		"""
		logging.info("handleIncomingMessage has been called!")
		actuatorMsg = DataUtil.jsonToActuatorData(resourceEnum, msg)
		self._handleIncomingDataAnalysis(ResourceNameEnum.CDA_ACTUATOR_RESPONSE_RESOURCE,actuatorMsg)
		

	def handleSensorMessage(self, data: SensorData) -> bool:
		"""
		Sensor data to Json form
		data: SensorData
		 bool
		"""
		logging.info("handleSensorMessage has been called!")
		sensorMsg = DataUtil.sensorDataToJson(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, data)
		self._handleSensorDataAnalysis(data)
		return True
		#pass
		
	def handleSystemPerformanceMessage(self, data: SystemPerformanceData) -> bool:
		"""
		PerformanceData to Json data
		data: SystemPerformanceData
		bool

		"""
		logging.info("handleSystemPerformanceMessage has been called!")
		sysPerfMsg = DataUtil.systemPerformanceDataToJson(ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, data)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SYSTEM_PERF_MSG_RESOURCE, sysPerfMsg)
	
	def startManager(self):
		""" start trigger of this class
		"""
		logging.info("DeviceDataManager started!")
		self.mqttClient.connectClient()
		self.sysPerfManager.startManager()
		self.sensorAdapterManager.startManager()
		
	def stopManager(self):
		"""stop trigger of this class
		"""
		logging.info("DeviceDataManager stopped!")
		self.mqttClient.disconnectClient()
		self.sysPerfManager.stopManager()
		self.sensorAdapterManager.stopManager()

	def _handleIncomingDataAnalysis(self, msg: str):
		"""
		Call this from handleIncomeMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Validate msg: Most will be ActuatorData, but you may pass other info as well.
		2) Convert msg: Use DataUtil to convert if appropriate.
		3) Act on msg: Determine what - if any - action is required, and execute.
		"""
		logging.debug("_handleIncomingDataAnalysis has been called!")
		try:
			actMsg = DataUtil.jsonToActuatorData(self, DataUtil.actuatorDataToJson(self, msg))
		except:
			logging.error("wrong data type!")
		
		self.actuatorAdapterManager.sendActuateorCommand(actMsg)
		
		
		
	def _handleSensorDataAnalysis(self, data: SensorData):
		"""
		Call this from handleSensorMessage() to determine if there's
		any action to take on the message. Steps to take:
		1) Check config: Is there a rule or flag that requires immediate processing of data?
		2) Act on data: If # 1 is true, determine what - if any - action is required, and execute.
		"""
		logging.debug("_handleSensorDataAnalysis/get a new sensor data/dataname="+data.getName())
		jsonData = DataUtil.sensorDataToJson(self, data)
		logging.debug("_handleSensorDataAnalysis/sensordata has been sent to GDA/")
		if data.getSensorType() is SensorData.TEMP_SENSOR_TYPE:
			if self.enableHandleTempChangeOnDevice is True:
				actData = ActuatorData(ActuatorData.HVAC_ACTUATOR_TYPE)
				val = data.getValue()
				actData.setValue(val)
				if val > self.triggerHvacTempCeiling:
					actData.setCommand(ActuatorData.COMMAND_ON)
					if self.imageSent is 0:
						self.socketSender.send("/Users/liu.zhengr/Downloads/fire01.jpeg")
						self.imageSent = 1;
				else:
					actData.setCommand(ActuatorData.COMMAND_OFF)
					self.imageSent = 0
				self.actuatorAdapterManager.sendActuatorCommand(actData)
		self._handleUpstreamTransmission(ResourceNameEnum.CDA_SENSOR_MSG_RESOURCE, jsonData)
		
		
	def _handleUpstreamTransmission(self, resourceName: ResourceNameEnum, msg: str):
		"""
		Call this from handleActuatorCommandResponse(), handlesensorMessage(), and handleSystemPerformanceMessage()
		to determine if the message should be sent upstream. Steps to take:
		1) Check connection: Is there a client connection configured (and valid) to a remote MQTT or CoAP server?
		2) Act on msg: If # 1 is true, send message upstream using one (or both) client connections.
		"""
		logging.debug("_handleUpstreamTransmission")
		qos = 0;
		#self.mqttClient.publishMessage(resourceName, msg, qos)
		_thread.start_new_thread (self.mqttClient.publishMessage,(resourceName, msg, qos,))
		self.counter = self.counter + 1
			
	def handleActuatorCommandMessage(self, data: ActuatorData) -> bool:
		if data:
			logging.info("Processing actuator command message.")
			
			# TODO: add further validation before sending the command
			self.actuatorAdapterManager.sendActuatorCommand(data)
			return True
		else:
			logging.warning("Received invalid ActuatorData command message. Ignoring.")
			return False

