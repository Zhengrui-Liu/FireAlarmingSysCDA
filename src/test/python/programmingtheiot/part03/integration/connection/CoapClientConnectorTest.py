#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# Copyright (c) 2020 by Andrew D. King
# 

import logging
import unittest

from time import sleep

import programmingtheiot.common.ConfigConst as ConfigConst

from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.common.ResourceNameEnum import ResourceNameEnum

from programmingtheiot.cda.connection.CoapClientConnector import CoapClientConnector

class CoapClientConnectorTest(unittest.TestCase):
	"""
	This test case class contains very basic integration tests for
	CoapClientConnector. It should not be considered complete,
	but serve as a starting point for the student implementing
	additional functionality within their Programming the IoT
	environment.
	"""
	
	@classmethod
	def setUpClass(self):
		logging.basicConfig(format = '%(asctime)s:%(module)s:%(levelname)s:%(message)s', level = logging.DEBUG)
		logging.info("Testing CoapClientConnector class...")
		
		self.cfg = ConfigUtil()
		self.mcc = CoapClientConnector()
		
	def setUp(self):
		pass
		#self.mcc._initClient()
		#self.mcc = CoapClientConnector()

	def tearDown(self):
		sleep(5)
		self.mcc.disconnectClient()

	def testConnectAndDiscover(self):
		"""Test protocol
		Test coap: connect
		"""
		self.mcc.sendDiscoveryRequest(timeout = 10)
		#self.mcc.disconnectClient()
		#self.mcc.disconnectClient()
	#@unittest.skip("Ignore for now.")
	def testConnectAndPostCon(self):
		"""Test protocol
		Test coap: post con
		"""
		msg = "This is a test."
		self.mcc.sendPostRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, payload = msg, enableCON = True, timeout = 5)
		#self.mcc.disconnectClient()
		#self.mcc.disconnectClient()
		
	#@unittest.skip("Ignore for now.")
	def testConnectAndPostNon(self):
		"""Test protocol
		Test coap: post non 
		"""
		msg = "This is a test."
		self.mcc.sendPostRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, payload = msg, enableCON = False, timeout = 5)
		#self.mcc.disconnectClient()
		#self.mcc.disconnectClient()
	#@unittest.skip("Ignore for now.")
	def testConnectAndGet(self):
		"""Test protocol
		Test coap: get 
		"""
		# TODO: implement this
		pass
	#@unittest.skip("Ignore for now.")
	def testConnectAndGetCon(self):
		"""Test protocol
		Test coap: get con
		"""
		self.mcc.sendGetRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, enableCON = True, timeout = 5)
		#self.mcc.disconnectClient()
		#self.mcc.disconnectClient()

	#@unittest.skip("Ignore for now.")
	def testConnectAndGetNon(self):
		"""Test protocol
		Test coap: get non
		"""
		self.mcc.sendGetRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, enableCON = False, timeout = 5)
		self.mcc.disconnectClient()
		#self.mcc.disconnectClient()
	
	#@unittest.skip("Ignore for now.")
	def testConnectAndPutCon(self):
		"""Test protocol
		Test coap: put con
		"""
		msg = "This is a test."
		self.mcc.sendPutRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, payload = msg, enableCON = True, timeout = 5)
		#self.mcc.disconnectClient()
		#self.mcc.disconnectClient()

	#@unittest.skip("Ignore for now.")
	def testConnectAndPutNon(self):
		"""Test protocol
		Test coap: put non
		"""
		msg = "This is a test."
		self.mcc.sendPutRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, payload = msg, enableCON = False, timeout = 5)
		#self.mcc.disconnectClient()
		#self.mcc.disconnectClient()
		
	#@unittest.skip("Ignore for now.")
	def testConnectAndDeleteCon(self):
		"""Test protocol
		Test coap: delete con
		"""
		self.mcc.sendDeleteRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, enableCON = True, timeout = 5)
		#self.mcc.disconnectClient()
		#self.mcc.disconnectClient()
		
	#@unittest.skip("Ignore for now.")
	def testConnectAndDeleteNon(self):
		"""Test protocol
		Test coap: delete non
		"""
		self.mcc.sendDeleteRequest(resource = ResourceNameEnum.CDA_MGMT_STATUS_MSG_RESOURCE, enableCON = False, timeout = 5)
		#self.mcc.disconnectClient()
		#self.mcc.disconnectClient()
		

if __name__ == "__main__":
	unittest.main()
	