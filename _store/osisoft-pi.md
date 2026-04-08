---
aid: osisoft-pi
url: https://raw.githubusercontent.com/api-evangelist/osisoft-pi/refs/heads/main/apis.yml
apis:
- aid: osisoft-pi:pi-web-api
  name: OSIsoft PI Web API
  tags:
  - Energy
  - Manufacturing
  - Process Historian
  - REST
  - SCADA
  - Time Series
  image: https://raw.githubusercontent.com/api-evangelist/osisoft-pi/refs/heads/main/image.png
  humanURL: https://docs.aveva.com/bundle/pi-web-api-reference
  baseURL: https://piwebapi.example.com/piwebapi
  properties:
  - url: https://docs.aveva.com/bundle/pi-web-api-reference
    type: Documentation
  - url: https://docs.aveva.com/bundle/pi-web-api-reference
    type: Reference
  - url: https://docs.aveva.com/bundle/pi-web-api-getting-started
    type: GettingStarted
  - url: https://github.com/aveva/sample-pi_web_api-common_actions-python
    type: SDKs
  - url: https://github.com/aveva/sample-pi_web_api-common_actions-angular
    type: SDKs
  - url: openapi/osisoft-pi-web-api-openapi.yml
    type: OpenAPI
  description: OSIsoft PI Web API (now part of AVEVA) provides a REST interface for accessing the PI System process historian. APIs enable real-time and historical time-series data retrieval, event frame queries, asset framework hierarchy navigation, and calculated data for industrial process monitoring.
- aid: osisoft-pi:aveva-connect-api
  name: AVEVA CONNECT Data Services API
  tags:
  - Cloud
  - IoT
  - Manufacturing
  - REST
  - Time Series
  image: https://raw.githubusercontent.com/api-evangelist/osisoft-pi/refs/heads/main/image.png
  humanURL: https://docs.aveva.com/bundle/aveva-data-hub-api-reference
  baseURL: https://api.aveva.com
  properties:
  - url: https://docs.aveva.com/bundle/aveva-data-hub-api-reference
    type: Documentation
  description: AVEVA CONNECT (formerly AVEVA Data Hub / OSIsoft Cloud Services) provides cloud-native REST APIs for industrial time-series data management, data views, event data, and secure cloud-based data sharing across operational technology environments.
- aid: osisoft-pi:pi-af-sdk
  name: OSIsoft PI AF SDK
  tags:
  - .NET
  - Asset Framework
  - Manufacturing
  - SDK
  image: https://raw.githubusercontent.com/api-evangelist/osisoft-pi/refs/heads/main/image.png
  humanURL: https://docs.aveva.com/
  baseURL: https://piwebapi.example.com/piwebapi
  properties:
  - url: https://docs.aveva.com/
    type: Documentation
  - url: https://github.com/aveva/sample-afsdk-getting_started-dotnet
    type: SDKs
  description: OSIsoft PI Asset Framework SDK (AF SDK) is a .NET client library for programmatic access to the PI System asset hierarchy, time-series data, and event frames from on-premises PI servers.
name: Osisoft Pi
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: OSIsoft PI System is a real-time data management platform used by industrial organizations to capture, analyze, and visualize operational data from sensors, devices, and applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

