# Constrained Device Application (Connected Devices)

## Lab Module 06

Be sure to implement all the PIOT-CDA-* issues (requirements) listed at [PIOT-INF-06-001 - Chapter 06](https://github.com/orgs/programming-the-iot/projects/1#column-10488379).

### Description

Implemented mqtt functions

1.Implemented publish,subscribe and unsubscribe functions.
2.Inplemented a simple version of callback functions.
3.Connected mqttClientConnector with DDM.

### Code Repository and Branch


URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-Zhengrui-Liu/tree/chapter06

### UML Design Diagram(s)

![image](./CDA-chapter06.svg)


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
- poit-python-components/src/test/python/programmingtheiot/part02/unit/data/DataUtilTest


### Integration Tests Executed

- poit-python-components/src/test/python/programmingtheiot/part01/integration/app/ConstrainedDeviceAppTest.py
- poit-python-components/src/test/python/programmingtheiot/part01/integration/system/SystemPerformanceManagerTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/integration/app/DeviceDataManagerNoCommsTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/integration/system/ActuatorAdapterManagerTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/integration/system/SensorAdapterManagerTest.py
- poit-python-components/src/test/python/programmingtheiot/part02/integration/emulated/all
- poit-python-components/src/test/python/programmingtheiot/part03/integration/data/DataIntegrationTest
- poit-python-components/src/test/python/programmingtheiot/part03/integration/connection/MqttClientConnectorTest.py


### MQTT 14 Control Packets (QoS 1 and 2)

CONNECT

![image](./mqtt/connect.png)

CONNACK

![image](./mqtt/connectack.png)

PUBLISH

![image](./mqtt/pub.png)

PUBACK(QoS1 only)

![image](./mqtt/puback.png)

PUBREC(QoS2 only)

![image](./mqtt/pubrec.png)

PUBREL(QoS2 only)

![image](./mqtt/pubrel.png)

PUBCOMP(QoS2 only)

![image](./mqtt/pubcmp.png)

SUBSCRIBE

![image](./mqtt/subreq.png)

SUBACK

![image](./mqtt/suback.png)

UNSUBSCRIBE

![image](./mqtt/unsub.png)

UNSUBACK

![image](./mqtt/unsuback.png)

PINGREQ

![image](./mqtt/ping.png)

PINGRESP

![image](./mqtt/pingres.png)

DISCONNECT

![image](./mqtt/disconnect.png)



