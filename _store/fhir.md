---
aid: fhir
name: Fast Healthcare Interoperability Resources
description: FHIR (Fast Healthcare Interoperability Resources) is a platform specification developed by HL7 that defines a set of capabilities for use across the healthcare process, in all jurisdictions, and in many different clinical and administrative contexts. It standardizes how electronic health information is exchanged between systems via REST APIs.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Healthcare
  - Standards
  - Interoperability
url: https://raw.githubusercontent.com/api-evangelist/fhir/refs/heads/main/apis.yml
created: '2024-07-11'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: fhir:fast-healthcare-interoperability-resources-api
    name: US Core Server CapabilityStatement
    description: This section describes the expected capabilities of the US Core Server actor which is responsible for providing responses to the queries submitted by US Core Requestors. Implementations meet ONC 2015 Common Clinical Data Set (CCDS) Patient Selection 170.315(g)(7) and Application Access - Data Category Request 170.315(g)(8) requirements as well as USCDI Version 4 (July 2023).
    humanURL: https://www.hl7.org/fhir/
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Healthcare
      - Standards
      - Interoperability
    properties:
      - type: Documentation
        url: https://www.hl7.org/fhir/
      - type: OpenAPI
        url: openapi/fhir-openapi-original.yml
      - type: PostmanCollection
        url: https://www.postman.com/api-evangelist/fast-healthcare-interoperability-resources-fhir/collection/35240-f4ba6100-8f52-4e08-8071-afb9f06e2668
common:
  - type: Website
    url: https://www.hl7.org/fhir/
  - type: PostmanWorkspace
    url: https://www.postman.com/api-evangelist/fast-healthcare-interoperability-resources-fhir/overview
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
