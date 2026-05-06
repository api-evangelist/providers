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
common:
  aid: iec-cim
  name: IEC CIM (Common Information Model)
  description: The IEC Common Information Model (CIM) standards (IEC 61968/61970) define data models and interfaces for electric utility systems including distribution management, energy management, and advanced metering infrastructure. The CIM User Group (CIMug) maintains open-source tools including CIMTool for working with CIM profiles and data exchange.
  image: https://raw.githubusercontent.com/api-evangelist/iec-cim/refs/heads/main/image.png
  tags:
    - Utilities
    - Energy
    - Smart Meter
    - CIM
    - XML
    - AMI
    - Smart Grid
  properties:
    - url: https://www.iec.ch/
      type: Portal
    - url: https://www.iec.ch/
      type: Documentation
    - url: https://cimug.ucaiug.org/
      type: Getting Started
    - url: https://www.iec.ch/
      type: Website
    - url: https://github.com/cimug-org
      type: GitHub Organization
    - url: https://github.com/cimug-org
      type: Developer Tools
    - url: openapi/iec-cim-61968-distribution-openapi.yml
      type: OpenAPI
    - url: json-schema/iec-cim-asset-schema.json
      type: JSONSchema
    - url: json-ld/iec-cim-context.jsonld
      type: JSONLDContext
maintainer:
  name: Kin Lane
  email: kin@apievangelist.com
modified: '2026-04-28'
description: IEC Common Information Model (CIM) is an international standard developed by the International Electrotechnical Commission for representing electrical power system data and facilitating data exchange between applications.
---
