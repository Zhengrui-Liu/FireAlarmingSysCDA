# Constrained Device Application (Connected Devices)

## Lab Module 04

Be sure to implement all the PIOT-CDA-* issues (requirements) listed at [PIOT-INF-04-001 - Chapter 04](https://github.com/orgs/programming-the-iot/projects/1#column-10488379).

### Description

Configure a senceHAT emulator together with with its environment. Then build emulator tasks and use them instead of sensor data generator. 

- Install PyGObject and GTK into the virtualenv.
- Install a SensorHat emulator into the environment.
- Run a simple test to check if installed all the packages correctly.
- Create all sensor emulator modules.
- Create all actuator emulator modules.
- Add emulator functionality to SensorAdapterManager.
- Add emulator functionality to ActuatorAdapterManager.
- Add emulator functionality to ActuatorAdapterManager.

### Code Repository and Branch


URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-Zhengrui-Liu/tree/chapter04

### UML Design Diagram(s)

![image](./CDA-chapter04.svg)


### Unit Tests Executed

- piot-python-components/src/test/python/programmingtheiot/part01/unit/common/ConfigUtilTest.py
- poit-python-components/src/test/python/programmingtheiot/part01/unit/system/SystemCpuUtilTaskTest.py
- poit-python-components/src/test/python/programmingtheiot/part01/unit/system/SystemMemUtilTaskTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/unit/data/ActuatorDataTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/unit/data/SensorDataTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/unit/data/SystemPerformanceDataTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/unit/sim/HumidifierActuatorSimTaskTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/unit/sim/HumidifierSensorSimTaskTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/unit/sim/HvacActuatorSimTaskTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/unit/sim/PressureSensorSimTaskTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/unit/sim/TemperatureSeneorSimTaskTest.py


### Integration Tests Executed

- poit-python-components/src/test/python/programmingtheiot/part01/integration/app/ConstrainedDeviceAppTest.py
- poit-python-components/src/test/python/programmingtheiot/part01/integration/system/SystemPerformanceManagerTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/integration/app/DeviceDataManagerNoCommsTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/integration/system/ActuatorAdapterManagerTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/integration/system/SensorAdapterManagerTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/integration/emulated/all
