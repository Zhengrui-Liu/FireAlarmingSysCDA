#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from json import JSONEncoder
import json

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.data.SensorData import SensorData
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class DataUtil():
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, encodeToUtf8 = False):
		pass
	
	def actuatorDataToJson(self, actuatorData) -> str:
		"""
		transfer actuator data to json data
		@param actuatorData:ActuatorData
		@return: str 
		"""
		jsonData = json.dumps(actuatorData, indent = 4, cls = JsonDataEncoder, ensure_ascii = True)
		return jsonData
	
	def sensorDataToJson(self, sensorData)-> str:
		"""
		transfer sensor data to json data
		@param sensorData:SensorData
		@return: str 
		"""
		jsonData = json.dumps(sensorData, indent = 4, cls = JsonDataEncoder, ensure_ascii = True)
		return jsonData
	
	def systemPerformanceDataToJson(self, sysPerfData)-> str:
		"""
		transfer system performance data to json data
		@param sysPerfData:SystemPerformanceData
		@return: str 
		"""
		jsonData = json.dumps(sysPerfData, indent = 4, cls = JsonDataEncoder, ensure_ascii = True)
		return jsonData
	
	def jsonToActuatorData(self, jsonData) -> ActuatorData:
		"""
		transfer json data to actuator data
		@param jsonData: str
		@return:  ActuatorData
		"""
		jsonData = jsonData.replace("\'", "\"").replace('False','false').replace('True', 'true')
		ad = ActuatorData()
		mvDict = vars(ad)
		adDict = json.loads(jsonData)
		for key in adDict:
			if key in mvDict:
				setattr(ad, key, adDict[key])
		return ad
	
	def jsonToSensorData(self, jsonData) -> SensorData:
		"""
		transfer json data to sensor data
		@param jsonData: str
		@return:  SensorData
		"""
		jsonData = jsonData.replace("\'", "\"").replace('False','false').replace('True', 'true')
		sd = SensorData()
		mvDict = vars(sd)
		sdDict = json.loads(jsonData)
		for key in sdDict:
			if key in mvDict:
				setattr(sd, key, sdDict[key])
		return sd
	
	def jsonToSystemPerformanceData(self, jsonData) -> SystemPerformanceData:
		"""
		transfer json data to system perform data
		@param jsonData: str
		@return:  SystemPerformanceData
		"""
		jsonData = jsonData.replace("\'", "\"").replace('False','false').replace('True', 'true')
		spd = SystemPerformanceData()
		mvDict = vars(spd)
		spdDict = json.loads(jsonData)
		for key in spdDict:
			if key in mvDict:
				setattr(spd, key, spdDict[key])
		return spd
	
class JsonDataEncoder(JSONEncoder):
	"""
	Convenience class to facilitate JSON encoding of an object that
	can be converted to a dict.
	
	"""
	def default(self, o):
			return o.__dict__
	