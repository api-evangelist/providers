---
aid: cerner
url: https://raw.githubusercontent.com/api-evangelist/cerner/refs/heads/main/apis.yml
name: Cerner (Oracle Health)
tags:
  - Cerner Millennium
  - Code Console
  - EHR
  - Electronic Health Records
  - FHIR
  - HL7
  - Healthcare
  - Interoperability
  - OAuth 2.0
  - Oracle Health
  - Patient Access
  - Provider Directory
  - SMART on FHIR
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-23'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: Cerner is a global healthcare technology company that designs and develops electronic health record (EHR) and health information technology solutions for hospitals, clinics, and integrated delivery networks. Cerner was acquired by Oracle in June 2022 and is now branded as Oracle Health, with the Cerner Millennium EHR platform's developer program operating as the Oracle Health Developer Program. Millennium exposes HL7 FHIR R4 and DSTU2 APIs, SMART on FHIR app launching, Bulk FHIR, the CareAware device and integration APIs, and the Code Console developer portal for registering applications and obtaining sandbox and production credentials.
apis:
  - aid: cerner:oracle-health-fhir-r4-api
    name: Oracle Health Millennium Platform FHIR R4 API
    tags:
      - CMS Interoperability
      - FHIR
      - HL7
      - Patient Access
      - R4
      - USCDI
    humanURL: https://docs.oracle.com/en/industries/health/millennium-platform-apis/mfrap/r4_overview.html
    properties:
      - url: https://docs.oracle.com/en/industries/health/millennium-platform-apis/mfrap/r4_overview.html
        type: Documentation
      - url: https://docs.oracle.com/en/industries/health/millennium-platform-apis/index.html
        type: Portal
      - url: https://www.oracle.com/health/developer/
        type: DeveloperProgram
    description: The Oracle Health Millennium Platform FHIR R4 API provides OAuth 2.0-secured access to Cerner Millennium EHR data in the HL7 FHIR R4 format, exposing USCDI-aligned resources such as Patient, Practitioner, Observation, Condition, MedicationRequest, DocumentReference, and Encounter for patient-access apps, provider apps, and interoperability partners.
  - aid: cerner:oracle-health-fhir-dstu2-api
    name: Oracle Health Millennium FHIR DSTU2 API
    tags:
      - DSTU2
      - FHIR
      - Legacy
      - SMART on FHIR
    humanURL: https://fhir.cerner.com/millennium/dstu2/
    properties:
      - url: https://fhir.cerner.com/millennium/dstu2/
        type: Documentation
      - url: https://fhir.cerner.com/
        type: Portal
    description: The Cerner Millennium DSTU2 FHIR API supports legacy SMART on FHIR applications and integrations with Meaningful Use 2015 CEHRT certification criteria, and remains available alongside the newer R4 implementation for backward compatibility.
  - aid: cerner:oracle-health-code-console
    name: Oracle Health Code Console (Developer Portal)
    tags:
      - Code Console
      - Developer Portal
      - OAuth 2.0
      - Registration
      - Sandbox
    humanURL: https://code.cerner.com/
    properties:
      - url: https://code.cerner.com/
        type: Website
      - url: https://www.oracle.com/health/developer/api/
        type: APIAccess
      - url: https://fhir.cerner.com/authorization/
        type: Authorization
    description: The Oracle Health Code Console (formerly Cerner Code) is the developer portal used to register SMART on FHIR and system-level applications, configure redirect URIs and launch parameters, manage OAuth 2.0 client credentials, and access the Millennium sandbox for initial testing.
  - aid: cerner:oracle-health-bulk-fhir-api
    name: Oracle Health Millennium Bulk FHIR API
    tags:
      - Bulk Data
      - FHIR
      - Flat FHIR
      - Population Health
    humanURL: https://fhir.cerner.com/millennium/r4/
    properties:
      - url: https://fhir.cerner.com/millennium/r4/
        type: Documentation
      - url: https://docs.oracle.com/en/industries/health/millennium-platform-apis/mfrap/r4_overview.html
        type: Reference
    description: Oracle Health Millennium supports the HL7 Bulk Data Access (Flat FHIR) specification for exporting group-level patient data in NDJSON format for population health, research, and payer-provider data exchange scenarios.
  - aid: cerner:cerner-careaware
    name: Cerner CareAware Integration APIs
    tags:
      - CareAware
      - Device Integration
      - HL7 v2
      - Medical Device
    humanURL: https://www.cerner.com/solutions/careaware-interoperability
    properties:
      - url: https://www.cerner.com/solutions/careaware-interoperability
        type: Website
    description: Cerner CareAware provides device and third-party application integration APIs for medical device data capture, bi-directional HL7 v2 messaging, and workflow embedding into Millennium, supporting medical device manufacturers and hospital biomedical teams.
  - aid: cerner:oracle-health-smart-on-fhir
    name: Oracle Health SMART on FHIR App Launch
    tags:
      - App Launch
      - Clinician App
      - Patient App
      - SMART on FHIR
    humanURL: https://fhir.cerner.com/authorization/openid-connect/
    properties:
      - url: https://fhir.cerner.com/authorization/openid-connect/
        type: Documentation
      - url: https://fhir.cerner.com/
        type: Portal
    description: Oracle Health implements the SMART on FHIR App Launch framework (standalone and EHR-launch) with OpenID Connect identity tokens, enabling third-party clinician and patient-facing applications to embed inside Millennium PowerChart and Oracle Health portals.
common:
  - type: Website
    url: https://www.cerner.com
  - type: Corporate
    url: https://www.oracle.com/health/
  - type: Developer
    url: https://www.oracle.com/health/developer/
  - type: APIReference
    url: https://docs.oracle.com/en/industries/health/millennium-platform-apis/index.html
  - type: FHIR
    url: https://fhir.cerner.com/
  - type: CodeConsole
    url: https://code.cerner.com/
  - type: OpenSource
    url: https://github.com/cerner
  - type: Privacy Policy
    url: https://www.oracle.com/legal/privacy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
