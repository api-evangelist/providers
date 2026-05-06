---
aid: ixon
name: IXON
description: IXON is an industrial IoT platform that enables machine builders and end-users to connect, monitor, and control industrial machines remotely. IXON provides APIs for accessing machine data, remote access management, and industrial IoT connectivity.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - IIoT
  - Industrial IoT
  - Machine Connectivity
  - Remote Access
url: https://raw.githubusercontent.com/api-evangelist/ixon/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: ixon:ixon-api
    name: IXON Cloud API
    description: The IXON Cloud API is an open, public REST API that provides programmatic access to the IXON industrial IoT platform, enabling management of devices, agents, access requests, machine data, and remote access connectivity. The API exposes 359 endpoints across the IXON Cloud platform.
    humanURL: https://developer.ixon.cloud/docs
    baseURL: https://portal.ixon.cloud/api/
    tags:
      - Industrial IoT
      - Machine Data
      - Remote Access
      - Device Management
    properties:
      - type: Documentation
        url: https://developer.ixon.cloud/docs
      - type: API Reference
        url: https://developer.ixon.cloud/v2/reference
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ixon/refs/heads/main/openapi/ixon-openapi.json
common:
  - type: Website
    url: https://www.ixon.cloud/
  - type: Portal
    url: https://developer.ixon.cloud/
  - type: Documentation
    url: https://developer.ixon.cloud/docs
  - type: Support
    url: https://support.ixon.cloud/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
