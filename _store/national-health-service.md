---
aid: national-health-service
name: National Health Service
description: The National Health Service (NHS) of England publishes a catalogue of APIs for health and care providers, including the Ambulance Data Submission FHIR API used to submit ambulance data to the NHS Data Processing Service (DPS) for analysis and review by NHS England and ambulance trusts.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Ambulance
  - Health
  - Healthcare
  - National Health Service
created: '2025-01-07'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/national-health-service/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: national-health-service:ambulance-data-submission-fhir
    name: NHS Ambulance Data Submission FHIR API
    description: Use this API to submit ambulance data to the NHS Data Processing Service (DPS) so that it can be made available for analysis and review by NHS England and ambulance trusts.
    humanURL: https://digital.nhs.uk/developer/api-catalogue/ambulance-data-submission-fhir
    baseURL: https://api.service.nhs.uk/ambulance-data-submission-fhir
    tags:
      - Ambulance
      - FHIR
      - Health
      - Healthcare
    properties:
      - type: Documentation
        url: https://digital.nhs.uk/developer/api-catalogue/ambulance-data-submission-fhir
      - type: Portal
        url: https://digital.nhs.uk/developer
common:
  - type: Website
    url: https://www.nhs.uk/
  - type: Portal
    url: https://digital.nhs.uk/developer
  - type: ApiCatalog
    url: https://digital.nhs.uk/developer/api-catalogue
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
