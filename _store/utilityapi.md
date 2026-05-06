---
aid: utilityapi
name: UtilityAPI
description: UtilityAPI collects, standardizes, and shares utility data seamlessly and securely, providing a platform for accessing energy and utility billing data, meter intervals, and authorization workflows for energy companies, cleantech firms, and developers.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Utilities
  - Green Button
  - Billing Data
  - Meter Data
  - Clean Energy
created: '2025-05-02'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: utilityapi:utilityapi
    name: UtilityAPI
    description: UtilityAPI provides a REST API for accessing utility data including meters, bills, intervals, authorizations, and webhook events. Supports Green Button standard for energy data sharing.
    humanURL: https://utilityapi.com/
    baseURL: https://utilityapi.com/api/v2
    tags:
      - Energy
      - Utilities
      - Billing
      - Meter Data
      - Green Button
      - Webhooks
    properties:
      - type: Documentation
        url: https://utilityapi.com/docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/openapi/utilityapi-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/json-schema/utilityapi-meter-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/json-schema/utilityapi-bill-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/json-schema/utilityapi-interval-schema.json
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/rules/utilityapi-rules.yml
    contact:
      - FN: UtilityAPI Support
        url: https://utilityapi.com/contact
    features:
      - name: Meter Data Access
        description: Access utility service and meter data for authorized customers
      - name: Bill Retrieval
        description: Retrieve utility billing information and billing summaries
      - name: Interval Data
        description: Access meter usage intervals for energy monitoring
      - name: Authorization Workflows
        description: Manage customer authorization forms and submitted authorizations
      - name: Webhook Events
        description: Event notifications for authorization and data collection activities
      - name: Green Button Support
        description: Compatibility with Green Button standard including XML feeds and OAuth
      - name: Accounting
        description: Access billing accounts and billing summaries
    useCases:
      - name: Clean Energy Applications
        description: Enable cleantech apps to access utility data for energy analysis
      - name: EV Charging Optimization
        description: Access meter interval data to optimize EV charging schedules
      - name: Energy Benchmarking
        description: Retrieve billing data for energy benchmarking and reporting
      - name: Solar and Storage
        description: Access utility data for solar and battery storage sizing
    integrations:
      - name: Green Button
        description: Connect standard for energy data sharing
        url: https://www.greenbuttonalliance.org/
    solutions:
      - name: Energy Data Platform
        description: Comprehensive utility data collection and standardization platform
common:
  - type: Website
    url: https://utilityapi.com/
  - type: Documentation
    url: https://utilityapi.com/docs
  - type: Sign Up
    url: https://utilityapi.com/register
  - type: Pricing
    url: https://utilityapi.com/pricing
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/openapi/utilityapi-openapi.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/capabilities/energy-data-access.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/utilityapi/refs/heads/main/vocabulary/utilityapi-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
