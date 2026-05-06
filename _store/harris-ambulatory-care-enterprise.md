---
aid: harris-ambulatory-care-enterprise
name: Harris Ambulatory Care Enterprise
description: Harris Ambulatory Care Enterprise (part of Harris Healthcare, a Harris Computer company) provides ambulatory healthcare software solutions including the Pulse electronic health record system. The platform supports a §170.315(g)(10) ONC certified FHIR API for third-party application developers to access patient data, provider information, and clinical resources. Pulse is deployed on-premises, so each provider hosts a separate API instance with its own base URL. Third-party developers must obtain an ONC 2015 Edition Certified API License and register with each provider organization.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Ambulatory Care
  - Electronic Health Records
  - FHIR
  - Health IT
  - Healthcare
  - ONC Certified
  - Pulse
url: https://raw.githubusercontent.com/api-evangelist/harris-ambulatory-care-enterprise/refs/heads/main/apis.yml
created: '2025-02-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: harris-ambulatory-care-enterprise:pulse-fhir-api
    name: Pulse FHIR API
    description: The Pulse §170.315(g)(10) ONC Certified FHIR API enables third-party application developers to register, authenticate, and integrate with providers using Harris Pulse EHR software. The documentation describes registration, syntax, supported FHIR resources, and error handling. Because Pulse is deployed per provider, each customer hosts a separate API instance with its own base URL.
    humanURL: https://harrisambulatory.com/pulse-api-documentation/
    baseURL: https://harrisambulatory.com/pulse-api-documentation/
    tags:
      - FHIR
      - Healthcare
      - Pulse
    properties:
      - type: Documentation
        url: https://harrisambulatory.com/pulse-api-documentation/
      - type: FHIR Documentation PDF
        url: https://harrisambulatory.com/wp-content/uploads/2023/01/Pulse-8.0-API-FHIR-Documentation.pdf
      - type: Provider Site
        url: https://harrisambulatory.com
  - aid: harris-ambulatory-care-enterprise:amazing-charts-api
    name: Amazing Charts API
    description: Amazing Charts is an EHR product within Harris Ambulatory Care Enterprise that exposes a §170.315(g)(10) ONC Certified FHIR API for third-party application developers.
    humanURL: https://harrisambulatory.com/ac-api-documentation/
    baseURL: https://harrisambulatory.com/ac-api-documentation/
    tags:
      - FHIR
      - Healthcare
      - Amazing Charts
    properties:
      - type: Documentation
        url: https://harrisambulatory.com/ac-api-documentation/
  - aid: harris-ambulatory-care-enterprise:caretracker-api
    name: CareTracker API
    description: CareTracker is a Harris Ambulatory Care Enterprise EHR product that provides a §170.315(g)(10) ONC Certified FHIR API for third-party developers.
    humanURL: https://harrisambulatory.com/caretracker-api-documentation/
    baseURL: https://harrisambulatory.com/caretracker-api-documentation/
    tags:
      - FHIR
      - Healthcare
      - CareTracker
    properties:
      - type: Documentation
        url: https://harrisambulatory.com/caretracker-api-documentation/
  - aid: harris-ambulatory-care-enterprise:picasso-api
    name: Picasso API
    description: Picasso is an ambulatory practice management product within Harris Ambulatory Care Enterprise that provides API documentation for third-party integrators.
    humanURL: https://harrisambulatory.com/picasso-api-documentation/
    baseURL: https://harrisambulatory.com/picasso-api-documentation/
    tags:
      - Healthcare
      - Picasso
    properties:
      - type: Documentation
        url: https://harrisambulatory.com/picasso-api-documentation/
common:
  - type: Website
    url: https://harrisambulatory.com
  - type: Pulse Documentation
    url: https://harrisambulatory.com/pulse-api-documentation/
  - type: Amazing Charts Documentation
    url: https://harrisambulatory.com/ac-api-documentation/
  - type: CareTracker Documentation
    url: https://harrisambulatory.com/caretracker-api-documentation/
  - type: Picasso Documentation
    url: https://harrisambulatory.com/picasso-api-documentation/
  - type: Parent Company
    url: https://www.harriscomputer.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
