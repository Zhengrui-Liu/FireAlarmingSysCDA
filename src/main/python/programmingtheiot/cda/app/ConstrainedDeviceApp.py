#####
# 
# This class is part of the Programming the Internet of Things
# project, and is available via the MIT License, which can be
# found in the LICENSE file at the top level of this repository.
# 
# You may find it more helpful to your design to adjust the
# functionality, constants and interfaces (if there are any)
# provided within in order to meet the needs of your specific
# Programming the Internet of Things project.
# 

import logging

from time import sleep
from programmingtheiot.cda.app.DeviceDataManager import DeviceDataManager
from programmingtheiot.cda.system.SystemPerformanceManager import SystemPerformanceManager

logging.basicConfig(format = '%(asctime)s:%(name)s:%(levelname)s:%(message)s', level = logging.DEBUG)

class ConstrainedDeviceApp():
	"""Definition of the ConstrainedDeviceApp class.
	
	"""
	
	def __init__(self): # Initialize the CDA with SystemPerformanceManager
		"""Initialization of class.
		
		path The name of the resource to apply to the URI.
		
		"""
		logging.info("Initializing CDA...")
		self.devDataManager = DeviceDataManager()

	def startApp(self):  
		"""Start CDA
		Start the CDA. Calls startManager() on the device data manager instance.
		
		"""
		logging.info("Starting CDA...")
		self.devDataManager.startManager()
		logging.info("CDA started.")

	def stopApp(self, code: int): # Stop CDA
		"""Stop CDA
		Stop the CDA. Calls stopManager() on the device data manager instance.
		code: int
		
		"""
		logging.info("CDA stopping...")
		self.devDataManager.stopManager()
		logging.info("CDA stopped with exit code %s.", str(code))
		
	def parseArgs(self, args):
		"""Parse command line args.
		
		args The arguments to parse.
		"""
		logging.info("Parsing command line args...")


def main():
	"""Main function definition for running client as application.
	
	Current implementation runs for 60 seconds then exits.
	"""
	cda = ConstrainedDeviceApp()
	cda.startApp()
	
	while True:
		sleep(60)
	
		
	cda.stopApp()

if __name__ == '__main__':
	"""
	Attribute definition for when invoking as app via command line
	
	"""
	main()
	