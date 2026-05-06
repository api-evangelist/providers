---
name: Orion Health
description: Orion Health is a global healthcare technology company that provides health information technology solutions, including population health management, health information exchange, and clinical workflow tools.
image: https://www.orionhealth.com/assets/img/orion-health-logo.png
url: https://www.orionhealth.com
created: '2024'
modified: '2026-03-04'
specificationVersion: '0.18'
apis:
  - name: Orion Health FHIR API
    description: Fast Healthcare Interoperability Resources (FHIR) API for accessing and exchanging healthcare data.
    image: https://www.orionhealth.com/assets/img/orion-health-logo.png
    humanURL: https://www.orionhealth.com/products/rhapsody-integration-engine/
    baseURL: https://api.orionhealth.com/fhir
    tags:
      - EHR
      - FHIR
      - Healthcare
      - Interoperability
      - Patient Data
    properties:
      - type: Documentation
        url: https://www.orionhealth.com/developers/fhir-api
      - type: OpenAPI
        url: openapi/orion-fhir-openapi.yml
      - type: Authentication
        url: https://www.orionhealth.com/developers/authentication
      - type: JSONSchema
        url: json-schema/orion-patient-schema.json
      - type: JSONSchema
        url: json-schema/orion-observation-schema.json
      - type: JSONLD
        url: json-ld/orion-healthcare-context.jsonld
    contact:
      - FN: Orion Health API Support
        email: apisupport@orionhealth.com
        url: https://www.orionhealth.com/support
  - name: Orion Health Population Health API
    description: API for population health management, analytics, and care coordination.
    image: https://www.orionhealth.com/assets/img/orion-health-logo.png
    humanURL: https://www.orionhealth.com/products/population-health/
    baseURL: https://api.orionhealth.com/population-health
    tags:
      - Analytics
      - Care Coordination
      - Healthcare
      - Population Health
      - Risk Stratification
    properties:
      - type: Documentation
        url: https://www.orionhealth.com/developers/population-health-api
      - type: OpenAPI
        url: openapi/orion-population-health-openapi.yml
      - type: Sandbox
        url: https://sandbox.orionhealth.com/population-health
      - type: JSONSchema
        url: json-schema/orion-care-plan-schema.json
      - type: JSONLD
        url: json-ld/orion-healthcare-context.jsonld
    contact:
      - FN: Orion Health API Support
        email: apisupport@orionhealth.com
        url: https://www.orionhealth.com/support
  - name: Orion Health HIE API
    description: Health Information Exchange API for sharing patient information across healthcare organizations.
    image: https://www.orionhealth.com/assets/img/orion-health-logo.png
    humanURL: https://www.orionhealth.com/products/health-information-exchange/
    baseURL: https://api.orionhealth.com/hie
    tags:
      - Data Sharing
      - Health Information Exchange
      - HIE
      - Interoperability
      - Patient Records
    properties:
      - type: Documentation
        url: https://www.orionhealth.com/developers/hie-api
      - type: OpenAPI
        url: openapi/orion-hie-openapi.yml
      - type: Terms of Service
        url: https://www.orionhealth.com/terms-of-service
      - type: JSONLD
        url: json-ld/orion-healthcare-context.jsonld
    contact:
      - FN: Orion Health API Support
        email: apisupport@orionhealth.com
        url: https://www.orionhealth.com/support
  - name: Orion Health Rhapsody Integration API
    description: API for healthcare integration engine enabling connectivity between disparate healthcare systems.
    image: https://www.orionhealth.com/assets/img/orion-health-logo.png
    humanURL: https://www.orionhealth.com/products/rhapsody-integration-engine/
    baseURL: https://api.orionhealth.com/rhapsody
    tags:
      - FHIR
      - Healthcare
      - HL7
      - Integration
      - Interoperability
      - Messaging
    properties:
      - type: Documentation
        url: https://www.orionhealth.com/developers/rhapsody-api
      - type: OpenAPI
        url: openapi/orion-rhapsody-openapi.yml
      - type: AsyncAPI
        url: asyncapi/orion-rhapsody-messaging-asyncapi.yml
      - type: Getting Started
        url: https://www.orionhealth.com/developers/getting-started
      - type: JSONLD
        url: json-ld/orion-healthcare-context.jsonld
    contact:
      - FN: Orion Health API Support
        email: apisupport@orionhealth.com
        url: https://www.orionhealth.com/support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - EHR
  - FHIR
  - Health IT
  - Healthcare
  - HIE
  - HL7
  - Integration
  - Interoperability
  - Population Health
include: []
common:
  - type: Portal
    url: https://developer.orionhealth.io/
  - type: Getting Started
    url: https://www.orionhealth.com/developers/getting-started
  - type: Authentication
    url: https://www.orionhealth.com/developers/authentication
  - type: Support
    url: https://www.orionhealth.com/support
  - type: Terms of Service
    url: https://www.orionhealth.com/terms-of-service
  - type: Privacy Policy
    url: https://www.orionhealth.com/privacy-policy
  - type: Contact
    url: https://www.orionhealth.com/contact
  - type: Blog
    url: https://www.orionhealth.com/blog
  - type: Status
    url: https://status.orionhealth.com
  - type: Website
    url: https://www.orionhealth.com
  - type: GitHub Organization
    url: https://github.com/orionhealth
  - type: Community
    url: https://community.orionhealth.com
---
