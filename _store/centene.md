---
aid: centene
url: https://raw.githubusercontent.com/api-evangelist/centene/refs/heads/main/apis.yml
name: Centene
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CMS Interoperability
  - FHIR
  - Formulary
  - Healthcare
  - Insurance
  - Interoperability
  - Managed Care
  - Patient Access
  - Provider Directory
created: '2024-01-15'
modified: '2026-04-23'
specificationVersion: '0.19'
description: Centene Corporation is a leading managed care organization providing government-sponsored healthcare programs including Medicaid, Medicare, and Health Insurance Marketplace plans. Centene operates a developer portal at partners.centene.com publishing FHIR-based interoperability APIs under the 21st Century Cures Act and CMS Interoperability and Patient Access Rule, including Patient Access, Provider Directory, and Provider RTR (Payer Data Exchange) APIs.
apis:
  - aid: centene:centene-fhir-patient-access
    name: Centene FHIR Patient Access API
    tags:
      - FHIR
      - Patient Access
      - CMS Interoperability
    humanURL: https://partners.centene.com/apiDetail/2718669d-6e2e-42b5-8c90-0a82f13a30ba
    properties:
      - url: https://partners.centene.com/apiDetail/2718669d-6e2e-42b5-8c90-0a82f13a30ba
        type: Documentation
      - url: https://partners.centene.com/apis
        type: Catalog
    description: The Centene FHIR Patient Access API lets members of Centene health plans access their clinical, financial, and formulary data through third-party applications, as required by the CMS Interoperability and Patient Access Rule.
  - aid: centene:centene-fhir-provider-directory
    name: Centene FHIR Provider Directory API
    tags:
      - FHIR
      - Provider Directory
      - CMS Interoperability
    humanURL: https://partners.centene.com/apiDetail/8122bc9c-43d6-4a2a-b6be-2272df8b8566
    properties:
      - url: https://partners.centene.com/apiDetail/8122bc9c-43d6-4a2a-b6be-2272df8b8566
        type: Documentation
      - url: https://partners.centene.com/apis
        type: Catalog
    description: The Centene FHIR Provider Directory API exposes in-network provider information for Centene members and the public via HL7 FHIR PDEX Provider Directory resources.
  - aid: centene:centene-fhir-pdex-rtr
    name: Centene Provider RTR - FHIR PDEX Directory API
    tags:
      - FHIR
      - PDEX
      - Payer Data Exchange
    humanURL: https://partners.centene.com/apiDetail/6b5c0001-8b47-4f1c-864f-9193971f5c62
    properties:
      - url: https://partners.centene.com/apiDetail/6b5c0001-8b47-4f1c-864f-9193971f5c62
        type: Documentation
      - url: https://partners.centene.com/apis
        type: Catalog
    description: The Provider RTR FHIR Payer Data Exchange (PDEX) Directory API delivers provider directory data between payers and authorized external partners using HL7 FHIR PDEX profiles.
common:
  - type: Website
    url: https://www.centene.com
  - type: Developer Portal
    url: https://partners.centene.com/
  - type: API Catalog
    url: https://partners.centene.com/apis
  - type: Application Developer
    url: https://partners.centene.com/applicationDeveloper
  - type: Interoperability
    url: https://www.superiorhealthplan.com/members/medicaid/resources/interoperability-and-patient-access/interoperability-for-developers.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
