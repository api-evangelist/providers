---
aid: hl7-fhir
name: HL7 FHIR
description: HL7 FHIR (Fast Healthcare Interoperability Resources) is the standard API specification for healthcare data exchange, published by Health Level Seven International (HL7). FHIR REST APIs provide access to patient, clinical, financial, and administrative healthcare data in JSON, XML, and RDF formats with a CC0 open license.
url: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/apis.yml
type: Index
image: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/image.png
tags:
  - Clinical
  - FHIR
  - Healthcare
  - HL7
  - Interoperability
created: '2025'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: hl7-fhir:hl7-fhir-r5-api
    name: HL7 FHIR R5 Healthcare API
    description: HL7 FHIR R5 (Release 5) is the current published FHIR standard for healthcare data exchange. FHIR R5 REST APIs provide access to patient demographics, observations, conditions, medications, encounters, and care plans in both JSON and XML formats across EHR systems, published March 2023.
    humanURL: https://www.hl7.org/fhir/
    baseURL: https://fhir-server.example.com/fhir/R5
    image: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/image.png
    tags:
      - Clinical
      - FHIR
      - Healthcare
      - HL7
      - Interoperability
      - JSON
      - XML
    properties:
      - type: Documentation
        url: https://www.hl7.org/fhir/
      - type: Reference
        url: https://www.hl7.org/fhir/http.html
      - type: Authentication
        url: https://www.hl7.org/fhir/security.html
      - type: Change Log
        url: https://www.hl7.org/fhir/history.html
  - aid: hl7-fhir:hl7-fhir-r4-api
    name: HL7 FHIR R4 Healthcare API
    description: HL7 FHIR R4 (v4.0.1) is a widely adopted normative FHIR standard for healthcare data exchange. FHIR R4 REST APIs are the most commonly implemented version across US healthcare systems, supporting patient data, clinical resources, medications, diagnostics, and financial resources.
    humanURL: https://www.hl7.org/fhir/R4/
    baseURL: https://fhir-server.example.com/fhir/R4
    image: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/image.png
    tags:
      - Clinical
      - FHIR
      - Healthcare
      - HL7
      - Interoperability
      - JSON
      - XML
    properties:
      - type: Documentation
        url: https://www.hl7.org/fhir/R4/
      - type: Reference
        url: https://www.hl7.org/fhir/R4/http.html
      - type: Change Log
        url: http://hl7.org/fhir/R4/history.html
      - type: OpenAPI
        url: openapi/hl7-fhir-r4-openapi.yml
  - aid: hl7-fhir:hl7-smart-on-fhir-api
    name: SMART on FHIR Authentication
    description: SMART on FHIR (v2.2.0) defines OAuth 2.0-based authorization patterns for client applications to authorize, authenticate, and integrate with FHIR-based data systems. It enables EHR launch, standalone launch, and backend service authorization workflows.
    humanURL: http://hl7.org/fhir/smart-app-launch/ImplementationGuide/hl7.fhir.uv.smart-app-launch
    baseURL: https://fhir-server.example.com/fhir
    image: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/image.png
    tags:
      - Authentication
      - FHIR
      - Healthcare
      - OAuth2
      - SMART
    properties:
      - type: Documentation
        url: http://hl7.org/fhir/smart-app-launch/ImplementationGuide/hl7.fhir.uv.smart-app-launch
      - type: Authentication
        url: http://hl7.org/fhir/smart-app-launch/ImplementationGuide/hl7.fhir.uv.smart-app-launch
common:
  - type: Portal
    url: https://www.hl7.org/fhir/
  - type: Documentation
    url: https://www.hl7.org/fhir/
  - type: Reference
    url: https://www.hl7.org/fhir/http.html
  - type: Authentication
    url: https://www.hl7.org/fhir/security.html
  - type: Change Log
    url: https://www.hl7.org/fhir/history.html
  - type: Getting Started
    url: https://www.hl7.org/fhir/downloads.html
  - type: Website
    url: https://www.hl7.org/
  - type: GitHub Organization
    url: https://github.com/HL7
  - type: OpenAPI
    url: openapi/hl7-fhir-r4-openapi.yml
  - type: JSONSchema
    url: json-schema/hl7-fhir-patient-schema.json
  - type: JSONLDContext
    url: json-ld/hl7-fhir-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
