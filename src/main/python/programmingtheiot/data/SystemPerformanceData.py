#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.BaseIotData import BaseIotData
import programmingtheiot.common.ConfigConst as ConfigConst

class SystemPerformanceData(BaseIotData):
	"""
	Shell representation of class for student implementation.
	
	"""
	DEFAULT_VAL = 0.0
	
	def __init__(self, d = None):
		"""
		Constructor
		"""
		
		super(SystemPerformanceData, self).__init__(name = ConfigConst.SYS_PERF_DATA, d = d)
		
		if d:
			self.cpuUtilization = d['cpuUtil']
			self.memoryUtilization = d['memUtil']
		else:
			self.cpuUtilization = self.DEFAULT_VAL
			self.memoryUtilization = self.DEFAULT_VAL
	
	def getCpuUtilization(self):
		return self.cpuUtilization
	
	def getMemoryUtilization(self):
		return self.memoryUtilization
	
	def setCpuUtilization(self, cpuUtil):
		self.cpuUtilization = cpuUtil
	
	def setMemoryUtilization(self, memUtil):
		self.memoryUtilization = memUtil
	
	def _handleUpdateData(self, data):
		"""
		if there is no err in the data, renew the util field with new dataSystem
		"""
		if data.hasErrorFlag() == False:
			self.setCpuUtilization(data.cpuUtilization)
			self.setMemoryUtilization(data.memoryUtilization)
