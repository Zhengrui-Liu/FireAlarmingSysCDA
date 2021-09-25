#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#
import string
import logging
import paho.mqtt.client as mqttClient

from programmingtheiot.common import ConfigUtil
from programmingtheiot.common import ConfigConst
from programmingtheiot.data.DataUtil import DataUtil

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.cda.connection.IPubSubClient import IPubSubClient
from argparse import _StoreFalseAction

DEFAULT_QOS = 1

class MqttClientConnector(IPubSubClient):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, clientID: str = None):
		"""
		Default constructor. This will set remote broker information and client connection
		information based on the default configuration file contents.
		
		@param clientID Defaults to None. Can be set by caller. If this is used, it's
		critically important that a unique, non-conflicting name be used so to avoid
		causing the MQTT broker to disconnect any client using the same name. With
		auto-reconnect enabled, this can cause a race condition where each client with
		the same clientID continuously attempts to re-connect, causing the broker to
		disconnect the previous instance.
		"""
		self.mc = None
		self.config = ConfigUtil.ConfigUtil()
		self.clientID = clientID
		self.dataUtil = DataUtil()

		self.host = self.config.getProperty(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)

		self.port = self.config.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_MQTT_PORT)

		self.keepAlive = self.config.getInteger(ConfigConst.MQTT_GATEWAY_SERVICE, ConfigConst.KEEP_ALIVE_KEY, ConfigConst.DEFAULT_KEEP_ALIVE)

		self.dataMsgListener = None
		logging.info('\tMQTT Broker Host: ' + self.host)
		logging.info('\tMQTT Broker Port: ' + str(self.port))
		logging.info('\tMQTT Keep Alive:  ' + str(self.keepAlive))

	def connectClient(self) -> bool:
		"""
		connect the mqtt client
		"""
		if not self.mc:
			self.mc = mqttClient.Client(client_id = self.clientID, clean_session = True)
			
			self.mc.on_connect = self.onConnect
			self.mc.on_disconnect = self.onDisconnect
			self.mc.on_message = self.onMessage
			self.mc.on_publish = self.onPublish
			self.mc.on_subscribe = self.onSubscribe

		if not self.mc.is_connected():
			self.mc.connect(self.host, self.port, self.keepAlive)
			self.mc.loop_start()
			return True
		else:
			logging.warn("MQTT client is already connected. Ignoring connect request.")
			return False
		
	def disconnectClient(self) -> bool:
		"""
		disconnect the mqtt client
		"""
		if self.mc.is_connected():
			self.mc.disconnect()
			self.mc.loop_stop()
			logging.warn("MQTT client is disconnected.")
			return True
		else:
			logging.warn("MQTT client is not connected. Ignoring disconnect request.")
			return False
	
	"""
	callback functions
	"""	
	def onConnect(self, client, userdata, flags, rc):
		"""callback function called when connect succeed
		client: mqtt client
		userdata: userdata
		flags: unused
		rc:  unused
		"""	
		logging.warn("MQTT client is already connected. (onConnect)")
		logging.info('[Callback] Connected to MQTT broker. Result code: ' + str(rc))

		# NOTE: Use the QoS of your choice - '1' is only an example
		self.mc.subscribe(topic = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE.value, qos = 0)
		self.mc.message_callback_add(sub = ResourceNameEnum.CDA_ACTUATOR_CMD_RESOURCE.value, callback = self.onActuatorCommandMessage)
		
		
	def onDisconnect(self, client, userdata, rc):
		"""callback function called when disconnect succeed
		client: mqtt client
		userdata: userdata
		flags: unused
		rc:  unused 
		"""	
		logging.warn("MQTT client is already connected. (ondisConnect)")
		
	def onMessage(self, client, userdata, msg):
		"""callback function called when receiving a message
		client: mqtt client
		userdata: userdata
		flags: unused
		rc:  unused
		"""	
		logging.warn("MQTT client received a new request.")
			
	def onPublish(self, client, userdata, mid):
		"""callback function called when publish succeed
		client: mqtt client
		userdata: userdata
		flags: unused
		rc:  unused
		"""	
		pass
		#logging.warn("On Publish: "+ str(mid))
	
	def onSubscribe(self, client, userdata, mid, granted_qos):
		"""callback function called when subscribe succeed
		client: mqtt client
		userdata: userdata
		flags: unused
		rc:  unused
		mid: message id
		"""	
		logging.warn("On Subscribe: "+ str(mid))
	
	
	def publishMessage(self, resource: ResourceNameEnum, msg: string, qos: int = DEFAULT_QOS):
		"""publish a new message of a topic
		resource: ResourceNameEnum
		msg: string
		qos: int
		"""
		if qos > 2 or qos < 0:
			qos = self.DEFAULT_QOS
		if resource is None:
			return False
		#for topic in resource.value():
		#print(resource.getResourceNameByValue(resource.name))
		myPublish = self.mc.publish(resource.value,msg,qos)
		myPublish.wait_for_publish()	
		if myPublish.is_published() is True:
			pass
			#logging.warn('Published')
		else:
			return False
		return True
		
	
	def subscribeToTopic(self, resource: ResourceNameEnum, qos: int = DEFAULT_QOS):
		"""subscribe a new topic
		resource: ResourceNameEnum
		qos: int
		"""
		if qos > 2 or qos < 0:
			qos = self.DEFAULT_QOS
		if resource is None:
			return False
		if self.mc.subscribe(resource.value, qos) is True:
			logging.warn('Subscribed')
		else:
			return False
		return True	
	
	def unsubscribeFromTopic(self, resource: ResourceNameEnum):
		"""unsubscribe a topic
		resource: ResourceNameEnum
		"""
		self.mc.unsubscribe("topic")
		return True

	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		"""setter to data listener
		"""
		if listener:
			self.dataMsgListener = listener
			return True
	
		return False
	
	def onActuatorCommandMessage(self, client, userdata, msg):
		"""callback function called when get an actruator data
		client: mqtt client
		userdata: userdata
		flags: unused
		"""	
		logging.info('[Callback] Actuator command message received. Topic: %s.', msg.topic)
		
		if self.dataMsgListener:
			try:
				logging.info(str(msg.payload.decode("utf-8")))
				actuatorData = self.dataUtil.jsonToActuatorData(str(msg.payload.decode("utf-8")))
				
				self.dataMsgListener.handleActuatorCommandMessage(actuatorData)
			except:
				logging.exception("Failed to convert incoming actuation command payload to ActuatorData: ")