---
aid: scada
name: SCADA
description: SCADA (Supervisory Control and Data Acquisition) is an industrial control system architecture used to monitor and control industrial processes, infrastructure, and facility-based equipment. It is widely used in manufacturing, energy, water treatment, oil and gas, transportation, and other critical infrastructure sectors to collect real-time data from remote sensors and control equipment. Modern SCADA systems increasingly expose REST APIs, OPC-UA endpoints, and MQTT brokers for integration with enterprise systems, cloud platforms, and AI/ML workloads.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Critical Infrastructure
  - ICS
  - Industrial Automation
  - Industrial IoT
  - OT Security
  - SCADA
url: https://raw.githubusercontent.com/api-evangelist/scada/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scada:opc-ua
    name: OPC Unified Architecture (OPC-UA)
    description: OPC-UA (IEC 62541) is the industrial interoperability standard for secure, reliable data exchange in industrial automation and IoT environments. It provides a platform-independent, service-oriented architecture for accessing real-time and historical data from PLCs, sensors, and SCADA systems. OPC-UA supports both client/server and pub/sub communication models.
    humanURL: https://opcfoundation.org/about/opc-technologies/opc-ua/
    tags:
      - IEC 62541
      - Industrial Interoperability
      - OPC-UA
      - Real-Time Data
    properties:
      - type: Documentation
        url: https://opcfoundation.org/about/opc-technologies/opc-ua/
      - type: Specification
        url: https://reference.opcfoundation.org/Core/Part1/v105/docs/
  - aid: scada:mqtt
    name: MQTT Protocol
    description: MQTT (Message Queuing Telemetry Transport, ISO/IEC 20922) is a lightweight pub/sub messaging protocol widely used in SCADA and IIoT applications for sensor data collection and device control. MQTT brokers (Mosquitto, EMQX, HiveMQ) are commonly deployed in SCADA architectures for real-time telemetry streaming.
    humanURL: https://mqtt.org/
    tags:
      - IoT
      - MQTT
      - Messaging
      - Pub/Sub
      - Telemetry
    properties:
      - type: Documentation
        url: https://mqtt.org/
      - type: Specification
        url: https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html
  - aid: scada:modbus
    name: Modbus Protocol
    description: Modbus is a serial communication protocol widely used in industrial automation and SCADA systems for connecting electronic devices. Modbus TCP/IP enables integration over standard Ethernet networks, making it one of the most common field device protocols in SCADA deployments.
    humanURL: https://modbus.org/
    tags:
      - Field Protocol
      - Industrial Automation
      - Modbus
      - PLC
    properties:
      - type: Documentation
        url: https://modbus.org/
      - type: Specification
        url: https://modbus.org/docs/Modbus_Application_Protocol_V1_1b3.pdf
  - aid: scada:ignition-api
    name: Ignition SCADA REST API
    description: Inductive Automation's Ignition SCADA platform provides a REST API for reading and writing tag values, managing alarms, retrieving historical data, and controlling system resources. Ignition is one of the most widely deployed SCADA platforms in North America.
    humanURL: https://docs.inductiveautomation.com/
    baseURL: https://{ignition-host}/system/webdev
    tags:
      - Ignition
      - Industrial Automation
      - SCADA Platform
    properties:
      - type: Documentation
        url: https://docs.inductiveautomation.com/
  - aid: scada:had-api
    name: Historian and Alarm Data APIs
    description: SCADA historians store time-series process data for analysis, reporting, and compliance. Major historian vendors (OSIsoft PI, Aspen InfoPlus.21, GE Proficy Historian) expose REST APIs for querying historical process data. The OSIsoft PI Web API provides a RESTful interface to PI System data assets.
    humanURL: https://techsupport.osisoft.com/Documentation/PI-Web-API/
    tags:
      - Historian
      - OSIsoft PI
      - Time-Series
    properties:
      - type: Documentation
        url: https://techsupport.osisoft.com/Documentation/PI-Web-API/
common:
  - type: Website
    url: https://www.isa.org/
  - type: Standards Body
    url: https://opcfoundation.org/
  - type: Standards Body
    url: https://www.iec.ch/
  - type: Documentation
    url: https://www.cisa.gov/topics/industrial-control-systems
  - type: GitHub
    url: https://github.com/topics/scada
  - type: Vocabulary
    url: vocabulary/scada-vocabulary.yml
  - type: JSONLD
    url: json-ld/scada-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
