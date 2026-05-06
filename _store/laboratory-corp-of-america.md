---
aid: laboratory-corp-of-america
url: https://raw.githubusercontent.com/api-evangelist/laboratory-corp-of-america/refs/heads/main/apis.yml
name: Laboratory Corporation of America (Labcorp)
type: Index
tags:
  - Alias
  - Diagnostics
  - FHIR
  - Fortune 500
  - Healthcare
  - Laboratory
  - Life Sciences
created: '2026-03-24'
modified: '2026-04-28'
position: Consuming
access: 3rd-Party
specificationVersion: '0.19'
description: Laboratory Corporation of America Holdings, doing business as Labcorp, is a leading global life sciences company providing diagnostic, drug development, and technology-enabled solutions to improve health and lives. This repository is an alias of the labcorp index and tracks the same FHIR / HL7 integration surface.
apis:
  - aid: laboratory-corp-of-america:labcorp-fhir-api
    name: Labcorp FHIR API
    tags:
      - FHIR
      - HL7
      - Healthcare
      - Interoperability
      - Laboratory
    humanURL: https://www.labcorp.com/organizations/health-systems
    description: Labcorp supports HL7 FHIR-based exchange of laboratory orders, results, and diagnostic reports with provider and health-system EHR systems. Typical FHIR resources exposed include ServiceRequest, DiagnosticReport, Observation, Patient, Practitioner, Specimen, and Organization. Access is provisioned through Labcorp integration services.
    properties:
      - url: https://www.labcorp.com/organizations/health-systems
        type: Documentation
      - url: https://www.labcorp.com/help/contact-us
        type: Support
  - aid: laboratory-corp-of-america:labcorp-link-api
    name: Labcorp Link Provider Integration
    tags:
      - EHR
      - Healthcare
      - Orders
      - Results
    humanURL: https://www.labcorp.com/labcorp-link
    description: Labcorp Link is the provider-facing platform for ordering laboratory tests and receiving results, supporting HL7 v2 and FHIR-based EHR integration.
    properties:
      - url: https://www.labcorp.com/labcorp-link
        type: Documentation
      - url: https://www.labcorp.com/help/contact-us
        type: Support
common:
  - url: https://www.labcorp.com
    type: Website
  - url: https://github.com/api-evangelist/labcorp
    type: AliasOf
  - url: https://www.labcorp.com/help
    type: Support
  - url: https://ir.labcorp.com/
    type: Investor Relations
  - url: https://www.labcorp.com/hipaa-privacy
    type: Privacy Policy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
