---
aid: reolink
url: https://raw.githubusercontent.com/api-evangelist/reolink/refs/heads/main/apis.yml
apis:
- aid: reolink:camera-http-api
  name: Reolink Camera HTTP API
  tags:
  - IoT
  - Security Cameras
  - Surveillance
  humanURL: https://community.reolink.com/topic/4196/reolink-camera-api-user-guide_v8-updated-in-april-2023
  properties:
  - url: https://community.reolink.com/topic/4196/reolink-camera-api-user-guide_v8-updated-in-april-2023
    type: Documentation
  - url: openapi/reolink-camera-api-openapi.yml
    type: OpenAPI
  - url: json-schema/device-info.json
    type: JSONSchema
  - url: json-schema/command-request.json
    type: JSONSchema
  - url: json-schema/command-response.json
    type: JSONSchema
  - url: json-schema/login.json
    type: JSONSchema
  - url: json-schema/ptz-control.json
    type: JSONSchema
  - url: json-schema/recording-search.json
    type: JSONSchema
  - url: json-schema/alarm-settings.json
    type: JSONSchema
  - url: json-schema/network-settings.json
    type: JSONSchema
  - url: json-ld/reolink-context.jsonld
    type: JSONLD
  description: The Reolink Camera HTTP API provides a JSON-based interface for controlling and configuring Reolink IP cameras and NVRs. All commands are sent as HTTP POST requests to the /cgi-bin/api.cgi endpoint. The API covers 11 functional modules including authentication, system management, security, network configuration, video and image settings, encoding, recording and playback, PTZ control, alarm and motion detection, LED control, and AI-powered object detection with auto-tracking.
name: Reolink
tags:
- IoT
- Security Cameras
- Surveillance
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Reolink is a provider of security cameras and smart home surveillance technology. Their cameras offer an HTTP API that enables direct device control and configuration through JSON-based POST requests. The API supports comprehensive camera management including PTZ control, video encoding settings, recording search and playback, motion and AI-powered object detection, network configuration, LED control, and user authentication. The API is accessible on the local network via the device IP address.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

