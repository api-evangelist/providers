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
common:
  - url: https://docs.aveva.com/
    type: Portal
  - url: https://docs.aveva.com/
    type: Documentation
  - url: https://docs.aveva.com/bundle/pi-web-api-getting-started
    type: GettingStarted
  - url: https://www.aveva.com/
    type: Website
  - url: https://softwaresupport.aveva.com/
    type: Support
  - url: https://community.aveva.com/
    type: Support
  - url: https://learningacademy.aveva.com/
    type: Documentation
  - url: https://github.com/aveva
    type: GitHubOrganization
  - url: https://github.com/aveva
    type: SDKs
  - url: openapi/osisoft-pi-web-api-openapi.yml
    type: OpenAPI
  - url: json-schema/osisoft-pi-point-schema.json
    type: JSONSchema
  - url: json-schema/osisoft-pi-timed-value-schema.json
    type: JSONSchema
  - url: json-ld/osisoft-pi-context.jsonld
    type: JSONLDContext
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
modified: '2026-03-18'
description: OSIsoft PI System is a real-time data management platform used by industrial organizations to capture, analyze, and visualize operational data from sensors, devices, and applications.
---
