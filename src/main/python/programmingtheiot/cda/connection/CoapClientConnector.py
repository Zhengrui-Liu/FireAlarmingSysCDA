#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import socket

from coapthon.client.helperclient import HelperClient
from coapthon.utils import parse_uri

from programmingtheiot.common import ConfigUtil
from programmingtheiot.common import ConfigConst

from programmingtheiot.common.IDataMessageListener import IDataMessageListener
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.cda.connection.IRequestResponseClient import IRequestResponseClient
from coapthon import defines
from coapthon.client.coap import CoAP
from coapthon.messages.message import Message
from coapthon.messages.request import Request
from coapthon.utils import generate_random_token


class CoapClientConnector(IRequestResponseClient):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self):
		"""
		Constructure: set the CoapClientConnector
		"""
		self.config = ConfigUtil.ConfigUtil()
		self.dataMsgListener = None
		self.coapClient = None

		self.host = self.config.getProperty(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.HOST_KEY, ConfigConst.DEFAULT_HOST)
		self.port = self.config.getInteger(ConfigConst.COAP_GATEWAY_SERVICE, ConfigConst.PORT_KEY, ConfigConst.DEFAULT_COAP_PORT)
		
		logging.info('\tCoAP Server Host: ' + self.host)
		logging.info('\tCoAP Server Port: ' + str(self.port))
		
		self.url = "coap://" + self.host + ":" + str(self.port) + "/"

		try:
			logging.info("Parsing URL: " + self.url)
	
			self.host, self.port, self.path = parse_uri(self.url)	
			tmpHost = socket.gethostbyname(self.host)
	
			if tmpHost:
				self.host = tmpHost
				self._initClient()
			else:
				logging.error("Can't resolve host: " + self.host)
	
		except socket.gaierror:
			logging.info("Failed to resolve host: " + self.host)
	
	def sendDiscoveryRequest(self, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		"""
		Send a discover request with coap
		timeout: int
		return bool
		"""
		#self._initClient()
		#self.coapClient.discover(callback = self._onDiscoveryResponse, timeout = 10)
		logging.info('Discovering remote resources...')
		self.coapClient.get(path = '/.well-known/core', callback = self._onDiscoveryResponse, timeout = timeout)

	def sendDeleteRequest(self, resource: ResourceNameEnum, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		"""
		send a delete request
		resource: ResourceNameEnum
		enableCON: bool
		timeout: int
		return bool
		"""
		#self._initClient()
		logging.info("sendDeleteRequest")
		if resource:
			logging.debug("Issuing DELETE with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.DELETE, path = resource.value)
			request.token = generate_random_token(2)
	
			if not enableCON:
				request.type = defines.Types["NON"]
		
			self.coapClient.send_request(request = request, callback = self._onDeleteResponse, timeout = timeout)
			return True
		else:
			logging.warning("Can't test DELETE - no path or path list provided.")
			return False

	def sendGetRequest(self, resource: ResourceNameEnum, enableCON = False,timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		"""
		send a get request
		resource: ResourceNameEnum
		enableCON: bool
		timeout: int
		return bool
		"""
		#self._initClient()
		logging.info("sendGetRequest")
		if resource:
			logging.debug("Issuing GET with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.GET, path = resource.value)
			request.token = generate_random_token(2)
	
			if not enableCON:
				request.type = defines.Types["NON"]
		
			self.coapClient.send_request(request = request, callback = self._onGetResponse, timeout = timeout)
			
			return True
		else:
			logging.warning("Can't test GET - no path or path list provided.")
			
			return False

	def sendPostRequest(self, resource: ResourceNameEnum, payload: str, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		"""
		send a post request
		resource: ResourceNameEnum
		payload: str
		enableCON: bool
		timeout: int
		return bool
		"""
		#self._initClient()
		#logging.info("sendPostRequest")
		if resource:
			#logging.debug("Issuing POST with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.POST, path = resource.value)
			request.token = generate_random_token(2)
			request.payload = payload
	
			if not enableCON:
				request.type = defines.Types["NON"]
			self.coapClient.send_request(request = request, timeout = timeout)
			self._onPostResponse
			self.coapClient.stop()
			#self.disconnectClient()
			return True
		else:
			#logging.warning("Can't test POST - no path or path list provided.")
			#self.disconnectClient()
			self.coapClient.stop()
			return False

	def sendPutRequest(self, resource: ResourceNameEnum, payload: str, enableCON = False, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		"""
		send a put request
		resource: ResourceNameEnum
		payload: str
		enableCON: bool
		timeout: int
		return bool
		"""
		#self._initClient()
		#logging.info("sendPutRequest")
		if resource:
			#logging.debug("Issuing PUT with path: " + resource.value)
			request = self.coapClient.mk_request(defines.Codes.PUT, path = resource.value)
			request.token = generate_random_token(2)
			request.payload = payload
	
			if not enableCON:
				request.type = defines.Types["NON"]
		
			response = self.coapClient.send_request(request = request, timeout = timeout)
			self._onPutResponse(response)
			
			return True
		else:
			#logging.warning("Can't test PUT - no path or path list provided.")
			return False

	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		"""
		setter to the data listener
		"""
		self.dataMsgListener = listener

	def startObserver(self, resource: ResourceNameEnum, ttl: int = IRequestResponseClient.DEFAULT_TTL) -> bool:
		pass

	def stopObserver(self, timeout: int = IRequestResponseClient.DEFAULT_TIMEOUT) -> bool:
		pass
	
	def _initClient(self):
		"""
		instantiate coap client
		"""
		if self.coapClient is None:
			self.coapClient = HelperClient(server = (self.host, self.port))
	
	def _onDiscoveryResponse(self, response):
		"""
		Call back function called when discover a response
		response: 
		"""
		if response:
			logging.info(response.pretty_print())
		
			# get the payload and convert to a list of paths
			self.pathList = response.payload.split(',')
			index = 0
		# the following is optional, but provides an easy way to track all the returned resource names
			for path in self.pathList:
				for char in '<\>':
					path = path.replace(char, '')
				
				self.pathList[index] = path
			
				logging.info('  Path entry [' + str(index) + ']:' + self.pathList[index])
				index += 1
		else:
			logging.info("No response received.")
			
	
	def disconnectClient(self):
		"""
		disconnect the coap client
		"""
		if self.coapClient:
			self.coapClient.close()
			
	def _onGetResponse(self,response):
		"""
		Callback function when get a get response
		"""
		logging.info('GET response received.')

		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
	
	#
	# NOTE: This next section is optional if you want to send a callback to the self.dataMsgListener instance
	#
	
	# TODO: get the URI and convert to ResourceNameEnum
		resource = None
	
		if self.dataMsgListener:
			self.dataMsgListener.handleIncomingMessage(resource, str(response.payload))
			
	
	def _onPutResponse(self,response):	
		"""
		Callback function when get a put response
		"""
		pass
		#self.disconnectClient()
		#logging.info('PUT response received.')

		#if response:
		#	logging.info('Token: ' + str(response.token))
		#	logging.info(str(response.location_path))
		#	logging.info(str(response.payload))

	def _onPostResponse(self,response):
		"""
		Callback function when get a post response
		"""
		pass
		#self.disconnectClient()
		#logging.info('POST response received.')

		#if response:
		#	logging.info('Token: ' + str(response.token))
		#	logging.info(str(response.location_path))
		#	logging.info(str(response.payload))
			
	def _onDeleteResponse(self, response):
		"""
		Callback function when get a delete response
		"""
		logging.info('DELETE response received.')

		if response:
			logging.info('Token: ' + str(response.token))
			logging.info(str(response.location_path))
			logging.info(str(response.payload))
			