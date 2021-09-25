#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging

from programmingtheiot.common.IDataMessageListener import IDataMessageListener

from programmingtheiot.data.ActuatorData import ActuatorData
from programmingtheiot.cda.sim.HumidifierActuatorSimTask import HumidifierActuatorSimTask
from programmingtheiot.cda.sim.HvacActuatorSimTask import HvacActuatorSimTask
from programmingtheiot.cda.emulated.HumidifierEmulatorTask import HumidifierEmulatorTask
from programmingtheiot.cda.emulated.HvacEmulatorTask import HvacEmulatorTask
from programmingtheiot.cda.emulated.LedDisplayEmulatorTask import LedDisplayEmulatorTask
from logging import StringTemplateStyle

class ActuatorAdapterManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""
	
	def __init__(self, useEmulator: bool = True):
		"""
		Constructor:
		@note: Decide if a simulator will be used
		@param useEmulator: bool = False
		"""
		self.hasPhoto = False
		self.useEmulator = useEmulator
		self.dataMsgListener = IDataMessageListener()
		if self.useEmulator is False:
			logging.info("The simulator will be used!")
			self.humidifierActuator = HumidifierActuatorSimTask()
			self.hvacActuator = HvacActuatorSimTask()
		else:
			logging.info("The emulator will be used!")
			# load the Humidifier actuation emulator
			humidifierModule = __import__('programmingtheiot.cda.emulated.HumidifierEmulatorTask', fromlist = ['HumidifierEmulatorTask'])
			hueClazz = getattr(humidifierModule, 'HumidifierEmulatorTask')
			self.humidifierEmulator = hueClazz()
			hvacModule = __import__('programmingtheiot.cda.emulated.HvacEmulatorTask', fromlist = ['HvacEmulatorTask'])
			hueClazzH = getattr(hvacModule, 'HvacEmulatorTask')
			self.hvacEmulator = hueClazzH()	
			ledDisplayModule = __import__('programmingtheiot.cda.emulated.LedDisplayEmulatorTask', fromlist = ['LedDisplayEmulatorTask'])
			hueClazzL = getattr(ledDisplayModule, 'LedDisplayEmulatorTask')
			self.ledDisplayEmulator = hueClazzL()
			"""
			self.humiEmuTsk = HumidifierEmulatorTask()
			self.havaEmuTsk = HvacEmulatorTask() 
			self.ledEmuTsk = LedDisplayEmulatorTask()
			"""

	def sendActuatorCommand(self, data: ActuatorData) -> bool:
		"""
		If use a simulator, get data from updater, use a listener to handle it
		@param data: ActuatorData
		@return: bool
		"""
		#logging.info("****************"+str(data.getValue())+"******************")
		latestdata = data
		print("sendActuatorCommand/useEmu="+str(self.useEmulator))
		print("sendActuatorCommand/actuatorType="+str(data.getActuatorType()))
		if(self.useEmulator == False):
			if data.getActuatorType() is ActuatorData.HUMIDIFIER_ACTUATOR_TYPE:
				self.humidifierActuator.updateActuator(data)
				latestdata = self.humidifierActuator.latestActuatorData
			elif data.getActuatorType() is ActuatorData.HVAC_ACTUATOR_TYPE:
				self.hvacActuator.updateActuator(data)
				latestdata = self.hvacActuator.latestActuatorData
			self.dataMsgListener.handleActuatorCommandResponse(latestdata)
			return True
		else:
			if data.getActuatorType() is ActuatorData.HUMIDIFIER_ACTUATOR_TYPE:
				print("sendActuatorCommand/humidAct")
				self.humidifierEmulator.updateActuator(data)
				latestdata = self.humidifierEmulator.latestActuatorData
			elif data.getActuatorType() is ActuatorData.HVAC_ACTUATOR_TYPE:
				print("sendActuatorCommand/HVACAct")
				self.hvacEmulator.updateActuator(data)
				latestdata = self.hvacEmulator.latestActuatorData
			elif data.getActuatorType() is ActuatorData.LED_DISPLAY_ACTUATOR_TYPE:
				print("sendActuatorCommand/LEDAct")
				self.ledDisplayEmulator.updateActuator(data)
				latestdata = self.ledDisplayEmulator.latestActuatorData
			self.dataMsgListener.handleActuatorCommandResponse(latestdata)
			return True
	
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		"""
		Get a new listener from outside
		@param listener: IDataMessageListener
		@return: bool
		"""
		if(listener != None):
			self.dataMsgListener = listener
			return True
		else:
			return False
