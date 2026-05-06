---
aid: charmhealth
name: CharmHealth
description: CharmHealth is a healthcare technology platform offering Electronic Health Records (EHR), Practice Management, Revenue Cycle Management, Patient Engagement, and TeleHealth tooling. CharmHealth exposes an HL7 FHIR R4 API conformant to the US Core Implementation Guide that lets third-party applications query patient medical records, manage clinical resources, and integrate with the EHR using SMART on FHIR OAuth 2.0 authorization.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/charmhealth/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
tags:
  - EHR
  - EMR
  - FHIR
  - Healthcare
  - HL7
  - Patient Engagement
  - Patients
  - SMART on FHIR
  - US Core
created: '2025-02-21'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: charmhealth:fhir-api
    name: CharmHealth FHIR API
    description: CharmHealth EHR FHIR API conforms to FHIR R4 (4.0.1) and the US Core STU 3.1.1 Implementation Guide. It supports 30+ FHIR resources covering clinical (AllergyIntolerance, Condition, Procedure, Immunization, MedicationRequest), care coordination (CarePlan, CareTeam, Goal, Encounter), administrative (Patient, Practitioner, Organization, Location, Appointment), diagnostic (DiagnosticReport, Observation), and documentation resources (DocumentReference, QuestionnaireResponse, Provenance). Authentication uses SMART on FHIR with OAuth 2.0 authorization code flow, PKCE for public clients, and JWT-assertion backend services authorization for system access.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.charmhealth.com/resources/fhir/index.html
    baseURL: https://ehr2.charmtracker.com/api/ehr/v2/fhir
    tags:
      - FHIR
      - HL7
      - Healthcare
      - SMART on FHIR
      - US Core
    properties:
      - type: Documentation
        url: https://www.charmhealth.com/resources/fhir/index.html
      - type: Authentication
        url: https://www.charmhealth.com/resources/fhir/authorization.html
      - type: SMARTOnFHIR
        url: https://www.charmhealth.com/resources/fhir/smart-on-fhir.html
      - type: BulkExport
        url: https://www.charmhealth.com/resources/fhir/bulk-data.html
      - type: USCore
        url: https://www.hl7.org/fhir/us/core/
      - type: OpenAPI
        url: openapi/charmhealth-fhir-api-openapi.yml
      - type: Spectral
        url: spectral/charmhealth-spectral.yml
common:
  - type: Website
    url: https://www.charmhealth.com/
  - type: Documentation
    url: https://www.charmhealth.com/resources/fhir/index.html
  - type: Developer
    url: https://www.charmhealth.com/developer/
  - type: News
    url: https://www.charmhealth.com/ehr/ehr-trade-shows.html
  - type: PressReleases
    url: https://www.charmhealth.com/ehr/press-release.html
  - type: CaseStudies
    url: https://casestudy.charmhealth.com/charmhealth-case-study-landing-page/
  - type: Blog
    url: https://www.charmhealth.com/blog/
  - type: Newsletter
    url: https://www.charmhealth.com/newsletter/
  - type: Webinars
    url: https://www.charmhealth.com/ehr/webinar.html
  - type: Pricing
    url: https://www.charmhealth.com/ehr/ehr-pricing.html
  - type: Support
    url: https://www.charmhealth.com/support/
  - type: TermsOfService
    url: https://www.charmhealth.com/ehr/termsofservice.html
  - type: PrivacyPolicy
    url: https://www.charmhealth.com/privacy-policy.html
  - type: JSONLD
    url: json-ld/charmhealth-context.jsonld
  - type: JSONSchema
    url: json-schema/charmhealth-patient-schema.json
  - type: JSONSchema
    url: json-schema/charmhealth-observation-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
