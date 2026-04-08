---
aid: hl7-fhir
url: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/apis.yml
apis:
- aid: hl7-fhir:hl7-fhir-r5-api
  name: HL7 FHIR R5 Healthcare API
  tags:
  - Clinical
  - FHIR
  - Healthcare
  - HL7
  - Interoperability
  - JSON
  - XML
  image: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/image.png
  humanURL: https://www.hl7.org/fhir/
  baseURL: https://fhir-server.example.com/fhir/R5
  properties:
  - url: https://www.hl7.org/fhir/
    type: Documentation
  - url: https://www.hl7.org/fhir/http.html
    type: Reference
  - url: https://www.hl7.org/fhir/security.html
    type: Authentication
  - url: https://www.hl7.org/fhir/history.html
    type: Change Log
  description: HL7 FHIR R5 (Release 5) is the current published FHIR standard for healthcare data exchange. FHIR R5 REST APIs provide access to patient demographics, observations, conditions, medications, encounters, and care plans in both JSON and XML formats across EHR systems, published March 2023.
- aid: hl7-fhir:hl7-fhir-r4-api
  name: HL7 FHIR R4 Healthcare API
  tags:
  - Clinical
  - FHIR
  - Healthcare
  - HL7
  - Interoperability
  - JSON
  - XML
  image: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/image.png
  humanURL: https://www.hl7.org/fhir/R4/
  baseURL: https://fhir-server.example.com/fhir/R4
  properties:
  - url: https://www.hl7.org/fhir/R4/
    type: Documentation
  - url: https://www.hl7.org/fhir/R4/http.html
    type: Reference
  - url: http://hl7.org/fhir/R4/history.html
    type: Change Log
  - url: openapi/hl7-fhir-r4-openapi.yml
    type: OpenAPI
  description: HL7 FHIR R4 (v4.0.1) is a widely adopted normative FHIR standard for healthcare data exchange. FHIR R4 REST APIs are the most commonly implemented version across US healthcare systems, supporting patient data, clinical resources, medications, diagnostics, and financial resources.
- aid: hl7-fhir:hl7-smart-on-fhir-api
  name: SMART on FHIR Authentication
  tags:
  - Authentication
  - FHIR
  - Healthcare
  - OAuth2
  - SMART
  image: https://raw.githubusercontent.com/api-evangelist/hl7-fhir/refs/heads/main/image.png
  humanURL: http://hl7.org/fhir/smart-app-launch/ImplementationGuide/hl7.fhir.uv.smart-app-launch
  baseURL: https://fhir-server.example.com/fhir
  properties:
  - url: http://hl7.org/fhir/smart-app-launch/ImplementationGuide/hl7.fhir.uv.smart-app-launch
    type: Documentation
  - url: http://hl7.org/fhir/smart-app-launch/ImplementationGuide/hl7.fhir.uv.smart-app-launch
    type: Authentication
  description: SMART on FHIR (v2.2.0) defines OAuth 2.0-based authorization patterns for client applications to authorize, authenticate, and integrate with FHIR-based data systems. It enables EHR launch, standalone launch, and backend service authorization workflows.
name: Hl7 Fhir
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: 'This page is part of the FHIR Specification (v5.0.0: R5 - STU). This is the current published version. For a full list of available versions, see the Directory of published versions . Page versions: R5 R4B R4 R3 R2.'
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

