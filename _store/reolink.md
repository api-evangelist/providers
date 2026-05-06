---
aid: reolink
name: Reolink
description: Reolink is a provider of security cameras and smart home surveillance technology. Their cameras offer an HTTP API that enables direct device control and configuration through JSON-based POST requests. The API supports comprehensive camera management including PTZ control, video encoding settings, recording search and playback, motion and AI-powered object detection, network configuration, LED control, and user authentication. The API is accessible on the local network via the device IP address.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - IoT
  - Security Cameras
  - Surveillance
  - Smart Home
  - AI Detection
url: https://raw.githubusercontent.com/api-evangelist/reolink/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: reolink:camera-http-api
    name: Reolink Camera HTTP API
    description: The Reolink Camera HTTP API provides a JSON-based interface for controlling and configuring Reolink IP cameras and NVRs. All commands are sent as HTTP POST requests to the /cgi-bin/api.cgi endpoint. The API covers 11 functional modules including authentication, system management, security, network configuration, video and image settings, encoding, recording and playback, PTZ control, alarm and motion detection, LED control, and AI-powered object detection with auto-tracking.
    humanURL: https://community.reolink.com/topic/4196/reolink-camera-api-user-guide_v8-updated-in-april-2023
    tags:
      - IoT
      - Security Cameras
      - Surveillance
      - Smart Home
      - AI Detection
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
      - url: rules/reolink-rules.yml
        type: Rules
      - url: capabilities/camera-management.yaml
        type: Capabilities
      - url: json-structure/reolink-device-structure.json
        type: JSONStructure
      - url: vocabulary/reolink-vocabulary.yml
        type: Vocabulary
      - url: examples/reolink-login-example.json
        type: Example
      - url: examples/reolink-ptz-control-example.json
        type: Example
common:
  - url: https://reolink.com
    name: Reolink
    type: Website
    description: Reolink security camera manufacturer homepage
  - url: https://community.reolink.com/
    name: Reolink Community Forum
    type: Forum
    description: Community discussion and API documentation
  - url: https://support.reolink.com/
    name: Reolink Support
    type: Support
    description: Official technical support portal
  - url: https://reolink.com/blog/
    name: Reolink Blog
    type: Blog
    description: Product news and smart home tips
  - url: https://github.com/ReolinkCameraAPI
    name: Reolink Camera API Community
    type: GitHubOrganization
    description: Community-maintained Reolink API SDKs and documentation
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
