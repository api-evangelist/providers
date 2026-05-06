---
aid: google-cloud-chronicle
name: Google Cloud Chronicle
description: Google Cloud Chronicle is a cloud-native security information and event management (SIEM) platform that enables enterprises to store, search, and analyze massive volumes of security telemetry data. Built on Google infrastructure, Chronicle provides sub-second search across petabytes of security data, threat detection using rules and intelligence, and investigation tools for security operations teams.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-cloud-chronicle/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.19'
type: Index
tags:
  - Incident Response
  - Log Management
  - Security Analytics
  - Security Operations
  - SIEM
  - Threat Detection
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
common:
  - type: Portal
    url: https://cloud.google.com/chronicle
  - type: Getting Started
    url: https://cloud.google.com/chronicle/docs/get-started
  - type: Documentation
    url: https://cloud.google.com/chronicle/docs
  - type: Authentication
    url: https://cloud.google.com/chronicle/docs/reference/rest#authentication
  - type: Pricing
    url: https://cloud.google.com/chronicle/pricing
  - type: Terms of Service
    url: https://cloud.google.com/terms
  - type: Privacy Policy
    url: https://policies.google.com/privacy
  - type: Status
    url: https://status.cloud.google.com
  - type: Support
    url: https://cloud.google.com/chronicle/docs/support
  - type: JSON-LD
    url: json-ld/google-cloud-chronicle-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
