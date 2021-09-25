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

from programmingtheiot.cda.system.SystemCpuUtilTask import SystemCpuUtilTask
from programmingtheiot.cda.system.SystemMemUtilTask import SystemMemUtilTask
from programmingtheiot.data.SystemPerformanceData import SystemPerformanceData

class SystemPerformanceManager(object):
	"""
	Shell representation of class for student implementation.
	
	"""

	def __init__(self, pollRate: int = 30):
		"""
		Initialize the SystemPerformanceManager (pollRate:[30s] execution interval of handleTelemetry)
		
		@param pollRate: 30 
		"""
		self.cpuUtilTask = SystemCpuUtilTask() # New instance of SystemCpuUtilTask
		self.memUtilTask = SystemMemUtilTask() # New instance of SystemMemUtilTask
		self.scheduler = BackgroundScheduler()
		self.scheduler.add_job(self.handleTelemetry, 'interval', seconds = pollRate) # add handleTelemetry to the scheduler
		self.dataMessageListener = IDataMessageListener()
		
	def handleTelemetry(self):
		"""
		Get CPU & Memory usage information and log them out
		
		"""
		print("*****************handleTelemetry")
		self.cpuUtilPct = self.cpuUtilTask.getTelemetryValue() # Get CPU usage performance
		self.memUtilPct = self.memUtilTask.getTelemetryValue() # Get Memory usage performance
		sysData = SystemPerformanceData()
		sysData.setCpuUtilization(self.cpuUtilPct)
		sysData.setMemoryUtilization(self.memUtilPct)
		self.dataMessageListener.handleSystemPerformanceMessage(sysData)
		logging.info('CPU utilization is %s percent, and memory utilization is %s percent.', str(self.cpuUtilPct), str(self.memUtilPct))
		# Log out the usage performance
	def setDataMessageListener(self, listener: IDataMessageListener) -> bool:
		self.dataMessageListener = listener
	
	def startManager(self):
		"""
		start SystemPerformanceManager
		
		"""
		self.scheduler.start() # start the scheduler
		logging.info("SystemPerformanceManager started successfully.")
		
	def stopManager(self):
		"""
		stop SystemPerformanceManager
		
		"""
		self.scheduler.shutdown() # stop the scheduler
		logging.info("SystemPerformanceManager is stopped.")
