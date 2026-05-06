---
aid: cnh
url: https://raw.githubusercontent.com/api-evangelist/cnh/refs/heads/main/apis.yml
name: CNH
x-type: company
tags:
  - Agriculture
  - Construction
  - Telematics
  - Equipment
  - FieldOps
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-23'
specificationVersion: '0.19'
description: CNH Industrial is a global leader in the manufacturing and distribution of agricultural and construction equipment, with brands including Case IH, New Holland, STEYR, Case CE, and New Holland Construction. Through develop.cnh.com CNH operates a developer portal that exposes the FieldOps API - a unified, ISO 15143-3 compliant REST API for vehicle telemetry, equipment management, farm/grower hierarchy, operations, prescription Rx delivery, and webhook subscriptions across both agronomic machinery and construction equipment.
apis:
  - aid: cnh:cnh-fieldops-api
    name: CNH FieldOps API
    tags:
      - Agriculture
      - Construction
      - ISO 15143-3
      - OAuth2
      - Telemetry
      - Vehicles
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://develop.cnh.com/api-guides/fieldops-api
    baseURL: https://api.fieldops.cnh.com
    properties:
      - url: https://develop.cnh.com/get-started
        type: GettingStarted
      - url: https://develop.cnh.com/api-guides
        type: Documentation
      - url: https://develop.cnh.com/api-guides/fieldops-api
        type: Reference
      - url: https://develop.cnh.com/api-guides/fieldops-api/vehicle-telemetry
        type: Reference
      - url: openapi/cnh-fieldops-openapi.yml
        type: OpenAPI
      - url: json-schema/cnh-equipment-schema.json
        type: JSONSchema
      - url: json-schema/cnh-telemetry-schema.json
        type: JSONSchema
      - url: json-ld/cnh-context.jsonld
        type: JSONLDContext
      - url: rules/cnh-rules.yml
        type: SpectralRuleset
      - url: capabilities/cnh-fieldops-capabilities.yml
        type: NaftikoCapabilities
    description: The CNH FieldOps API replaces the previously available CNH Ag Data and CONNECT Machine Data APIs and provides a unified, OAuth 2.0 secured REST API for both agronomic machinery and construction equipment connected to a FieldOps account. Vehicle telemetry follows the ISO 15143-3 specification with two profiles - CP (CAN Parameter, default) and MH (Machine Health) - and supports time-series data such as locations, operating hours, idle hours, fuel and DEF remaining, peak speed, distance, fault codes, and engine condition. Additional endpoint groups cover Equipment, Operations By Vehicle, Prescriptions (send Rx files), Farm Setup (Grower / Farm / Field / Boundary), Files, and Webhooks.
    x-features:
      - name: ISO 15143-3 Telemetry
        description: Standards-based vehicle telemetry across CNH brands and equipment classes.
      - name: CP and MH Profiles
        description: CAN Parameter (default) and Machine Health telemetry profiles.
      - name: Fault Codes
        description: Fault, caution, and engine-condition codes per vehicle.
      - name: Aggregated Metrics
        description: Daily metrics including operating hours, idle hours, fuel ratio, distance, and peak speed.
      - name: Prescription Rx Delivery
        description: Push prescription files directly to a vehicle or FieldOps field.
      - name: Farm Hierarchy
        description: Grower / Farm / Field / Boundary management.
      - name: Operations by Vehicle
        description: Recorded field operations per vehicle.
      - name: Webhooks
        description: Subscribe to FieldOps event notifications.
      - name: OAuth 2.0
        description: Refresh and access token authentication via develop.cnh.com.
    x-useCases:
      - name: Fleet Telematics
        description: Power third-party fleet-management systems with CNH equipment telemetry.
      - name: Predictive Maintenance
        description: Use Machine Health telemetry and fault codes to anticipate maintenance.
      - name: Precision Agriculture
        description: Push prescription Rx files into the workflow for variable-rate application.
      - name: Farm Management Systems
        description: Hydrate FMS dashboards with grower / farm / field hierarchies and operations.
      - name: Construction Equipment Tracking
        description: Track Case CE and New Holland Construction equipment via standardized ISO telematics.
  - aid: cnh:cnh-developer-portal
    name: CNH Developer Portal
    tags:
      - Developer Portal
      - Documentation
      - OAuth2
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://develop.cnh.com/
    properties:
      - url: https://develop.cnh.com/
        type: Portal
      - url: https://develop.cnh.com/get-started
        type: GettingStarted
    description: The CNH Developer Portal at develop.cnh.com hosts onboarding, authentication guidance, API guides, Postman collections, and curated SwaggerHub documentation for FieldOps and related CNH APIs. Developers register for credentials, obtain refresh tokens, and progress from sandbox to live data through the portal.
common:
  - url: https://www.cnhindustrial.com/
    type: Website
  - url: https://develop.cnh.com/
    type: Portal
  - url: https://develop.cnh.com/get-started
    type: GettingStarted
  - url: https://develop.cnh.com/api-guides
    type: Documentation
  - url: openapi/cnh-fieldops-openapi.yml
    type: OpenAPI
  - url: json-schema/cnh-equipment-schema.json
    type: JSONSchema
  - url: json-schema/cnh-telemetry-schema.json
    type: JSONSchema
  - url: json-ld/cnh-context.jsonld
    type: JSONLDContext
  - url: rules/cnh-rules.yml
    type: SpectralRuleset
  - url: capabilities/cnh-fieldops-capabilities.yml
    type: NaftikoCapabilities
  - url: https://www.cnhindustrial.com/en-us/privacy/pages/default.aspx
    type: PrivacyPolicy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
