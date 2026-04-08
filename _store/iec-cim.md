---
aid: iec-cim
url: https://raw.githubusercontent.com/api-evangelist/iec-cim/refs/heads/main/apis.yml
apis:
- aid: iec-cim:iec-cim-61968-distribution-api
  name: IEC CIM 61968 Distribution Management API
  tags:
  - CIM
  - Distribution
  - Energy
  - Smart Grid
  - Utilities
  - XML
  image: https://raw.githubusercontent.com/api-evangelist/iec-cim/refs/heads/main/image.png
  humanURL: https://www.iec.ch/
  baseURL: https://ami-gateway.utility.example.com/cim/61968
  properties:
  - url: https://www.iec.ch/
    type: Documentation
  - url: https://cimug.ucaiug.org/
    type: Reference
  - url: openapi/iec-cim-61968-distribution-openapi.yml
    type: OpenAPI
  description: The IEC CIM 61968 standard defines interfaces for distribution management systems (DMS), enabling integration of outage management, network management, meter reading, and work management systems using CIM XML message exchange.
- aid: iec-cim:iec-cim-61970-ems-api
  name: IEC CIM 61970 Energy Management API
  tags:
  - CIM
  - EMS
  - Energy
  - Transmission
  - Utilities
  - XML
  image: https://raw.githubusercontent.com/api-evangelist/iec-cim/refs/heads/main/image.png
  humanURL: https://www.iec.ch/
  baseURL: https://ems-gateway.utility.example.com/cim/61970
  properties:
  - url: https://www.iec.ch/
    type: Documentation
  - url: https://cimug.ucaiug.org/
    type: Reference
  description: The IEC CIM 61970 standard defines the Common Information Model for energy management systems (EMS), enabling data exchange for power system network models, measurements, and topology across transmission utility systems.
- aid: iec-cim:iec-cim-ami-smart-meter-api
  name: IEC CIM AMI Smart Meter API
  tags:
  - AMI
  - CIM
  - Energy
  - Metering
  - Smart Meter
  - Utilities
  - XML
  image: https://raw.githubusercontent.com/api-evangelist/iec-cim/refs/heads/main/image.png
  humanURL: https://www.iec.ch/
  baseURL: https://ami-gateway.utility.example.com/cim
  properties:
  - url: https://www.iec.ch/
    type: Documentation
  - url: https://cimug.ucaiug.org/
    type: Reference
  description: The IEC CIM AMI (Advanced Metering Infrastructure) APIs from AMI head-end systems provide smart meter readings, interval data, usage points, and demand response signals using CIM XML data models compliant with IEC 61968-9 for utility grid operations.
name: Iec Cim
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: IEC Common Information Model (CIM) is an international standard developed by the International Electrotechnical Commission for representing electrical power system data and facilitating data exchange between applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

