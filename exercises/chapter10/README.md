# Constrained Device Application (Connected Devices)

## Lab Module 10


### Description

Integration.

### Code Repository and Branch


URL: https://github.com/NU-CSYE6530-Fall2020/constrained-device-app-Zhengrui-Liu/tree/chapter10

### UML Design Diagram(s)

![image](./CDA-chapter09.svg)


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
- poit-python-components/src/test/python/programmingtheiot/part03/integration/connection/CoapClientConnectorTest.py

### CDA MQTT Client Performance Test Results

#####QoS0

Connect time: 3013.128 ms
Disconnect time: 7362.995 ms

2020-12-02 14:40:37,933:ConfigUtil:INFO:Loading config: ../../../../../../../config/PiotConfig.props
2020-12-02 14:40:37,935:ConfigUtil:DEBUG:Config: ['Mqtt.GatewayService', 'Coap.GatewayService', 'ConstrainedDevice']
2020-12-02 14:40:37,935:ConfigUtil:INFO:Created instance of ConfigUtil: <programmingtheiot.common.ConfigUtil.ConfigUtil object at 0x10833bbe0>
2020-12-02 14:40:37,935:MqttClientConnector:INFO:	MQTT Broker Host: localhost
2020-12-02 14:40:37,935:MqttClientConnector:INFO:	MQTT Broker Port: 1883
2020-12-02 14:40:37,935:MqttClientConnector:INFO:	MQTT Keep Alive:  30
/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/programmingtheiot/cda/connection/MqttClientConnector.py:94: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("MQTT client is already connected. (onConnect)")
2020-12-02 14:40:37,943:MqttClientConnector:WARNING:MQTT client is already connected. (onConnect)
/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/programmingtheiot/cda/connection/MqttClientConnector.py:97: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("MQTT client is already connected. (ondisConnect)")
2020-12-02 14:40:40,948:MqttClientConnector:WARNING:MQTT client is already connected. (ondisConnect)
/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/programmingtheiot/cda/connection/MqttClientConnector.py:84: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("MQTT client is disconnected.")
2020-12-02 14:40:40,948:MqttClientConnector:WARNING:MQTT client is disconnected.
2020-12-02 14:40:40,949:MqttClientPerformanceTest:INFO:Connect and Disconnect: 3013.128 ms
.2020-12-02 14:40:40,949:MqttClientConnector:INFO:	MQTT Broker Host: localhost
2020-12-02 14:40:40,949:MqttClientConnector:INFO:	MQTT Broker Port: 1883
2020-12-02 14:40:40,949:MqttClientConnector:INFO:	MQTT Keep Alive:  30
2020-12-02 14:40:40,951:MqttClientConnector:WARNING:MQTT client is already connected. (onConnect)
2020-12-02 14:40:48,314:MqttClientConnector:WARNING:MQTT client is already connected. (ondisConnect)
2020-12-02 14:40:48,314:MqttClientConnector:WARNING:MQTT client is disconnected.
2020-12-02 14:40:48,314:MqttClientPerformanceTest:INFO:Publish message - QoS 0 [100000]: 7362.995 ms
.ss

#####QoS1

Connect time: 3009.153 ms
Disconnect time: 12204.694 ms


2020-12-02 14:44:02,685:ConfigUtil:INFO:Loading config: ../../../../../../../config/PiotConfig.props
2020-12-02 14:44:02,686:ConfigUtil:DEBUG:Config: ['Mqtt.GatewayService', 'Coap.GatewayService', 'ConstrainedDevice']
2020-12-02 14:44:02,686:ConfigUtil:INFO:Created instance of ConfigUtil: <programmingtheiot.common.ConfigUtil.ConfigUtil object at 0x10f44dbe0>
2020-12-02 14:44:02,686:MqttClientConnector:INFO:	MQTT Broker Host: localhost
2020-12-02 14:44:02,686:MqttClientConnector:INFO:	MQTT Broker Port: 1883
2020-12-02 14:44:02,686:MqttClientConnector:INFO:	MQTT Keep Alive:  30
/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/programmingtheiot/cda/connection/MqttClientConnector.py:94: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("MQTT client is already connected. (onConnect)")
2020-12-02 14:44:02,694:MqttClientConnector:WARNING:MQTT client is already connected. (onConnect)
/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/programmingtheiot/cda/connection/MqttClientConnector.py:97: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("MQTT client is already connected. (ondisConnect)")
2020-12-02 14:44:05,695:MqttClientConnector:WARNING:MQTT client is already connected. (ondisConnect)
/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/programmingtheiot/cda/connection/MqttClientConnector.py:84: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("MQTT client is disconnected.")
2020-12-02 14:44:05,696:MqttClientConnector:WARNING:MQTT client is disconnected.
2020-12-02 14:44:05,696:MqttClientPerformanceTest:INFO:Connect and Disconnect: 3009.153 ms
.s2020-12-02 14:44:05,696:MqttClientConnector:INFO:	MQTT Broker Host: localhost
2020-12-02 14:44:05,696:MqttClientConnector:INFO:	MQTT Broker Port: 1883
2020-12-02 14:44:05,696:MqttClientConnector:INFO:	MQTT Keep Alive:  30
2020-12-02 14:44:05,698:MqttClientConnector:WARNING:MQTT client is already connected. (onConnect)
2020-12-02 14:44:17,903:MqttClientConnector:WARNING:MQTT client is already connected. (ondisConnect)
2020-12-02 14:44:17,903:MqttClientConnector:WARNING:MQTT client is disconnected.
2020-12-02 14:44:17,903:MqttClientPerformanceTest:INFO:Publish message - QoS 1 [100000]: 12204.694 ms
.s

#####QoS2

Connect time: 3011.237 ms
Disconnect time: 19898.493 ms

2020-12-02 14:45:51,798:ConfigUtil:INFO:Loading config: ../../../../../../../config/PiotConfig.props
2020-12-02 14:45:51,798:ConfigUtil:DEBUG:Config: ['Mqtt.GatewayService', 'Coap.GatewayService', 'ConstrainedDevice']
2020-12-02 14:45:51,798:ConfigUtil:INFO:Created instance of ConfigUtil: <programmingtheiot.common.ConfigUtil.ConfigUtil object at 0x10c006be0>
2020-12-02 14:45:51,799:MqttClientConnector:INFO:	MQTT Broker Host: localhost
2020-12-02 14:45:51,799:MqttClientConnector:INFO:	MQTT Broker Port: 1883
2020-12-02 14:45:51,799:MqttClientConnector:INFO:	MQTT Keep Alive:  30
/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/programmingtheiot/cda/connection/MqttClientConnector.py:94: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("MQTT client is already connected. (onConnect)")
2020-12-02 14:45:51,806:MqttClientConnector:WARNING:MQTT client is already connected. (onConnect)
/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/programmingtheiot/cda/connection/MqttClientConnector.py:97: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("MQTT client is already connected. (ondisConnect)")
2020-12-02 14:45:54,809:MqttClientConnector:WARNING:MQTT client is already connected. (ondisConnect)
/Users/liu.zhengr/git/constrained-device-app-Zhengrui-Liu/src/main/python/programmingtheiot/cda/connection/MqttClientConnector.py:84: DeprecationWarning: The 'warn' function is deprecated, use 'warning' instead
  logging.warn("MQTT client is disconnected.")
2020-12-02 14:45:54,810:MqttClientConnector:WARNING:MQTT client is disconnected.
2020-12-02 14:45:54,810:MqttClientPerformanceTest:INFO:Connect and Disconnect: 3011.237 ms
.ss2020-12-02 14:45:54,810:MqttClientConnector:INFO:	MQTT Broker Host: localhost
2020-12-02 14:45:54,810:MqttClientConnector:INFO:	MQTT Broker Port: 1883
2020-12-02 14:45:54,811:MqttClientConnector:INFO:	MQTT Keep Alive:  30
2020-12-02 14:45:54,812:MqttClientConnector:WARNING:MQTT client is already connected. (onConnect)
2020-12-02 14:46:14,711:MqttClientConnector:WARNING:MQTT client is already connected. (ondisConnect)
2020-12-02 14:46:14,711:MqttClientConnector:WARNING:MQTT client is disconnected.
2020-12-02 14:46:14,711:MqttClientPerformanceTest:INFO:Publish message - QoS 2 [100000]: 19898.493 ms
.

##### Result

Run Time: QoS0 < QoS1 < QoS2
Connect Time: Same

### CDA COAP Client Performance Test Results

##### CON

Finding files... done.
Importing test modules ... done.

Testing POST - CON
POST message - useCON = True [10000]: 9839.919 ms
----------------------------------------------------------------------
Ran 2 tests in 9.851s

OK (skipped=1)


##### NON

Finding files... done.
Importing test modules ... done.

Testing POST - NON
POST message - useCON = False [10000]: 7956.18 ms
----------------------------------------------------------------------
Ran 2 tests in 7.965s

OK (skipped=1)

##### Result

Run Time: NON < CON

