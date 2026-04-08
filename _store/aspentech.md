---
aid: aspentech
url: https://raw.githubusercontent.com/api-evangelist/aspentech/refs/heads/main/apis.yml
apis:
- aid: aspentech:aspentech-inmation-web-api
  name: AspenTech Inmation Web API
  tags:
  - Industrial IoT
  - Manufacturing
  - Process Optimization
  - REST
  - Time Series
  - WebSocket
  image: https://raw.githubusercontent.com/api-evangelist/aspentech/refs/heads/main/image.png
  humanURL: https://atdocs.inmation.com/api/1.108/webapi/index.html
  baseURL: http://hostname:8002
  properties:
  - url: https://atdocs.inmation.com/api/1.108/webapi/index.html
    type: Documentation
  - url: https://atdocs.inmation.com/api/1.108/webapi/index.html
    type: Reference
  - url: https://atdocs.inmation.com/home/index.html
    type: Documentation
  - url: https://raw.githubusercontent.com/api-evangelist/aspentech/refs/heads/main/openapi/aspentech-inmation-web-openapi.yml
    type: OpenAPI
  description: The AspenTech Inmation Web API provides HTTP and WebSocket interfaces for external applications to interact with AspenTech Inmation industrial IoT and time-series data platforms. RPC-based REST APIs enable access to process data, system services, and automation functions for manufacturing and energy operations.
- aid: aspentech:aspentech-aspen-one-api
  name: AspenTech Aspen One API
  tags:
  - Energy
  - Manufacturing
  - Process Engineering
  - Process Optimization
  - Simulation
  image: https://raw.githubusercontent.com/api-evangelist/aspentech/refs/heads/main/image.png
  humanURL: https://www.aspentech.com/
  baseURL: https://api.aspentech.example.com
  properties:
  - url: https://www.aspentech.com/en/getting-started-guides
    type: GettingStarted
  - url: https://dev.knowledgecenter.aspentech.com/
    type: Documentation
  description: AspenTech provides process optimization and simulation software for energy, chemicals, and manufacturing industries. The Aspen One platform APIs enable access to process simulation models, performance monitoring, and optimization data for AI-driven operational workflows.
- aid: aspentech:aspentech-inmation-sci-api
  name: AspenTech Inmation Simple Call Interface (SCI) API
  tags:
  - Industrial IoT
  - Manufacturing
  - Process Optimization
  - REST
  image: https://raw.githubusercontent.com/api-evangelist/aspentech/refs/heads/main/image.png
  humanURL: https://atdocs.inmation.com/api/1.102/sci/index.html
  baseURL: http://hostname:8002
  properties:
  - url: https://atdocs.inmation.com/api/1.102/sci/index.html
    type: Documentation
  - url: https://atdocs.inmation.com/api/1.102/sci/index.html
    type: Reference
  description: The AspenTech Inmation Simple Call Interface (SCI) API provides a simplified HTTP interface for communicating with the Inmation industrial data platform. Designed for straightforward read/write access to process data and configuration items in manufacturing and energy environments.
name: Aspentech
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Web API (Application Programming Interface) is created using Remote Procedure-Call’s (RPC) and is hosted in a Windows Service. It can be used by any external application as an interface to AspenTech Inmation, using the HTTP or WebSocket Interface.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

