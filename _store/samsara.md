---
aid: samsara
name: Samsara
description: 'Samsara is a leading connected operations platform for physical operations industries including transportation, logistics, construction, field services, and energy. The Samsara REST API provides programmatic access to fleet telematics, driver safety, compliance (ELD/HOS), vehicle diagnostics, route management, industrial IoT sensors, and workforce management. With over two million connected devices, the platform offers real-time GPS tracking, AI-powered safety cameras, digital inspection forms (DVIRs), IFTA reporting, and data streaming via webhooks and Kafka. Base URL: https://api.samsara.com. Authentication uses Bearer tokens with OAuth 2.0 support.'
url: https://www.samsara.com/
tags:
  - Asset Tracking
  - Connected Operations
  - ELD
  - Fleet Management
  - GPS Tracking
  - IoT
  - Logistics
  - Safety
  - Telematics
  - Transportation
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-11-07'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: samsara:samsara
    name: Samsara API
    description: The Samsara REST API provides comprehensive access to fleet and industrial IoT data including vehicles, drivers, assets, routes, compliance (ELD/HOS), safety events, sensor readings, DVIR inspections, documents, forms, addresses, tags, users, and messaging. Supports real-time data, historical queries, webhooks, and Kafka data streaming.
    humanURL: https://developers.samsara.com/
    baseURL: https://api.samsara.com
    tags:
      - Addresses
      - Assets
      - Compliance
      - Documents
      - Drivers
      - DVIR
      - ELD
      - Fleet
      - Forms
      - Hours Of Service
      - IoT
      - Routes
      - Safety
      - Sensors
      - Tags
      - Telematics
      - Users
      - Vehicles
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.samsara.com/docs/rest-api-overview
      - type: OpenAPI
        url: openapi/samsara-openapi.yml
      - type: GitHubRepository
        url: https://github.com/samsarahq/api-docs
      - type: PythonSDK
        url: https://github.com/samsarahq/samsara-python
      - type: JavaScriptSDK
        url: https://github.com/samsarahq/samsara-js
      - type: SDKDocumentation
        url: https://developers.samsara.com/docs/sdks
common:
  - type: Documentation
    url: https://developers.samsara.com/
    title: Samsara Developer Portal
  - type: Documentation
    url: https://developers.samsara.com/docs/getting-started
    title: Getting Started Guide
  - type: GitHubOrganization
    url: https://github.com/samsarahq
    title: Samsara GitHub Organization
  - type: Authentication
    url: https://developers.samsara.com/docs/authentication
    title: API Authentication
  - type: SpectralRules
    url: rules/samsara-rules.yml
    title: Samsara API Spectral Rules
  - type: NaftikoCapability
    url: capabilities/fleet-operations.yaml
    title: Samsara Fleet Operations Capability
  - type: NaftikoCapability
    url: capabilities/safety-compliance.yaml
    title: Samsara Safety and Compliance Capability
  - type: JSONSchema
    url: json-schema/samsara-vehicle-schema.json
    title: Samsara Vehicle Schema
  - type: JSONSchema
    url: json-schema/samsara-driver-schema.json
    title: Samsara Driver Schema
  - type: JSONSchema
    url: json-schema/samsara-safety-event-schema.json
    title: Samsara Safety Event Schema
  - type: JSONStructure
    url: json-structure/samsara-vehicle-structure.json
    title: Samsara Vehicle Structure
  - type: JSONStructure
    url: json-structure/samsara-driver-structure.json
    title: Samsara Driver Structure
  - type: JSONLDContext
    url: json-ld/samsara-context.jsonld
    title: Samsara JSON-LD Context
  - type: Example
    url: examples/samsara-list-vehicles-example.json
    title: Samsara List Vehicles Example
  - type: Example
    url: examples/samsara-list-safety-events-example.json
    title: Samsara List Safety Events Example
  - type: Vocabulary
    url: vocabulary/samsara-vocabulary.yml
    title: Samsara Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
