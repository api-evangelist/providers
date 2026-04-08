---
aid: epic
url: https://raw.githubusercontent.com/api-evangelist/epic/refs/heads/main/apis.yml
apis:
- aid: epic:epic-fhir-r4-api
  name: Epic FHIR R4 API
  tags:
  - Clinical
  - EHR
  - FHIR
  - Healthcare
  - HL7
  - OAuth2
  - R4
  - SMART on FHIR
  image: https://raw.githubusercontent.com/api-evangelist/epic/refs/heads/main/image.png
  humanURL: https://fhir.epic.com/
  baseURL: https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4
  properties:
  - url: https://fhir.epic.com/Documentation
    type: Documentation
  - url: https://fhir.epic.com/Specifications?api=1
    type: Reference
  - url: https://fhir.epic.com/Documentation?docId=developerguidelines
    type: GettingStarted
  - url: https://fhir.epic.com/Documentation?docId=oauth2tutorial
    type: Authentication
  - url: https://fhir.epic.com/FAQ
    type: FAQ
  - url: https://fhir.epic.com/Resources/Terms
    type: TermsOfService
  - url: https://raw.githubusercontent.com/api-evangelist/epic/refs/heads/main/openapi/epic-fhir-r4-openapi.yml
    type: OpenAPI
  description: Epic FHIR R4 API provides standards-based access to patient health records via HL7 FHIR R4 resources including Patient, Observation, Condition, Medication, Appointment, DiagnosticReport, and 100+ additional resource types. Uses SMART on FHIR (OAuth 2.0) authentication supporting patient-facing, clinician-facing, and backend system-to-system flows. Supports DSTU2, STU3, and R4 versions. Available at no cost to developers via open.epic.com.
- aid: epic:epic-open-epic-api
  name: Epic open.epic API
  tags:
  - CDS Hooks
  - Clinical
  - EHR
  - FHIR
  - FHIRcast
  - Healthcare
  - HL7
  - Web Services
  image: https://raw.githubusercontent.com/api-evangelist/epic/refs/heads/main/image.png
  humanURL: https://open.epic.com/
  baseURL: https://open.epic.com
  properties:
  - url: https://open.epic.com/TechnicalSpecifications
    type: Documentation
  - url: https://open.epic.com/DeveloperResources
    type: GettingStarted
  - url: https://open.epic.com/Home/TermsOfUse
    type: TermsOfService
  - url: https://open.epic.com/Home/PrivacyPolicy
    type: PrivacyPolicy
  - url: https://open.epic.com/Interface/WebServices
    type: Reference
  - url: https://open.epic.com/Playbooks
    type: Documentation
  description: open.epic provides access to 750+ no-cost APIs and interfaces for Epic EHR integration including FHIR APIs, CDS Hooks, FHIRcast, HL7 v2, ASC X12, NCPDP, DICOM, and public web services (speech-to-text, credit card, wait times). Supports 50+ CMS-0057 Interoperability and Prior Authorization Final Rule APIs. Developer registration and client app management are available through the portal.
- aid: epic:epic-smart-on-fhir-api
  name: Epic SMART on FHIR API
  tags:
  - Clinical Apps
  - EHR
  - Healthcare
  - OAuth2
  - Patient Apps
  - SMART on FHIR
  image: https://raw.githubusercontent.com/api-evangelist/epic/refs/heads/main/image.png
  humanURL: https://fhir.epic.com/Documentation?docId=oauth2tutorial
  baseURL: https://fhir.epic.com/interconnect-fhir-oauth
  properties:
  - url: https://fhir.epic.com/Documentation?docId=oauth2tutorial
    type: Documentation
  - url: https://fhir.epic.com/Documentation?docId=oauth2tutorial
    type: Authentication
  description: Epic SMART on FHIR implements OAuth 2.0 for both patient-facing and clinician-facing app launches from within Epic's EHR (Hyperspace). Supports authorization code flows with refresh tokens, backend service JWT authentication for system-to-system integrations, and embedded launches within Epic workflows.
- aid: epic:epic-cds-hooks-api
  name: Epic CDS Hooks API
  tags:
  - CDS Hooks
  - Clinical Decision Support
  - EHR
  - Healthcare
  image: https://raw.githubusercontent.com/api-evangelist/epic/refs/heads/main/image.png
  humanURL: https://fhir.epic.com/Documentation?docId=cds-hooks
  baseURL: https://fhir.epic.com/interconnect-fhir-oauth
  properties:
  - url: https://fhir.epic.com/Documentation?docId=cds-hooks
    type: Documentation
  description: Epic CDS Hooks API enables clinical decision support services to integrate with Epic's EHR workflow. External CDS services receive patient context and provide evidence-based recommendations, alerts, and suggestions to clinicians at the point of care.
- aid: epic:epic-fhir-bulk-data-api
  name: Epic FHIR Bulk Data API
  tags:
  - Bulk Export
  - EHR
  - FHIR
  - Healthcare
  - Population Health
  image: https://raw.githubusercontent.com/api-evangelist/epic/refs/heads/main/image.png
  humanURL: https://fhir.epic.com/Documentation?docId=fhir_bulk_data
  baseURL: https://fhir.epic.com/interconnect-fhir-oauth
  properties:
  - url: https://fhir.epic.com/Documentation?docId=fhir_bulk_data
    type: Documentation
  - url: https://fhir.epic.com/Documentation?docId=fhir_bulk_data
    type: GettingStarted
  description: Epic FHIR Bulk Data API enables asynchronous export of large FHIR datasets for population health management, research, and analytics. Implements the HL7 FHIR Bulk Data Access specification, supporting group-level and system-level exports using backend service OAuth 2.0 authentication.
name: Epic
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Join us at the Open@Epic conference.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

