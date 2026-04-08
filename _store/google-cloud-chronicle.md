---
aid: google-cloud-chronicle
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-chronicle/refs/heads/main/apis.yml
apis:
- name: Chronicle API
  description: The Chronicle API provides programmatic access to Chronicle's security analytics platform. Developers can use the API to ingest security telemetry, search across normalized security data using UDM (Unified Data Model), manage detection rules, investigate alerts, and retrieve threat intelligence. The API supports creating and managing detection rules, running retrohunts, and accessing curated threat detections.
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  humanURL: https://cloud.google.com/chronicle/docs
  baseURL: https://chronicle.googleapis.com
  tags:
  - Detection Rules
  - Security Events
  - Threat Intelligence
  - UDM Search
  properties:
  - type: Documentation
    url: https://cloud.google.com/chronicle/docs/reference/rest
  - type: OpenAPI
    url: openapi/chronicle-api-openapi.yml
  - type: Authentication
    url: https://cloud.google.com/chronicle/docs/reference/rest#authentication
  - type: JSONSchema
    url: json-schema/google-cloud-chronicle-event-schema.json
name: Google Cloud Chronicle
tags:
- Incident Response
- Log Management
- Security Analytics
- Security Operations
- SIEM
- Threat Detection
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Cloud Chronicle is a cloud-native security information and event management (SIEM) platform that enables enterprises to store, search, and analyze massive volumes of security telemetry data. Built on Google infrastructure, Chronicle provides sub-second search across petabytes of security data, threat detection using rules and intelligence, and investigation tools for security operations teams.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

