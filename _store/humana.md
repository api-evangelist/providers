---
aid: humana
name: Humana
description: Humana is a U.S. health insurance company that provides Medicare, Medicaid, and employer-sponsored health insurance plans, along with wellness programs and healthcare services. Humana publishes a suite of FHIR-compliant APIs that give third-party applications access to member health data, coverage information, drug formularies, and provider directories under CMS interoperability rules.
url: https://raw.githubusercontent.com/api-evangelist/humana/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - FHIR
  - Health Insurance
  - Healthcare
  - Interoperability
  - Medicare
created: '2025-01-07'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: humana:humana-fhir-clinical-api
    name: Humana FHIR Clinical Data API
    description: FHIR R4-compliant API surface providing clinical resources for member health data, including AllergyIntolerance, CarePlan, CareTeam, Condition, Goal, Immunization, Observation, and Procedure resources.
    humanURL: https://developers.humana.com/apis/allergyintolerance-api/doc
    baseURL: https://fhir.humana.com/api
    tags:
      - Clinical Data
      - FHIR
      - Healthcare
    properties:
      - type: Documentation
        url: https://developers.humana.com/apis/allergyintolerance-api/doc
      - type: CapabilityStatement
        url: https://fhir.humana.com/api/metadata
      - type: Sandbox
        url: https://sandbox-fhir.humana.com/api/
      - type: Getting Started
        url: https://developers.humana.com/
  - aid: humana:humana-fhir-medication-api
    name: Humana FHIR Medication API
    description: FHIR R4-compliant API surface for medication-related resources including Medication, MedicationKnowledge, MedicationRequest, drug formulary List resources, and supporting payer data.
    humanURL: https://developers.humana.com/
    baseURL: https://fhir.humana.com/api
    tags:
      - FHIR
      - Formulary
      - Medications
    properties:
      - type: Documentation
        url: https://developers.humana.com/
      - type: CapabilityStatement
        url: https://fhir.humana.com/api/metadata
      - type: Sandbox
        url: https://sandbox-fhir.humana.com/api/
  - aid: humana:humana-fhir-coverage-api
    name: Humana FHIR Coverage and Benefits API
    description: FHIR R4-compliant API surface for insurance coverage data, including Coverage, ExplanationOfBenefits, and InsurancePlan resources used to satisfy CMS Patient Access and Provider Directory rules.
    humanURL: https://developers.humana.com/
    baseURL: https://fhir.humana.com/api
    tags:
      - Coverage
      - FHIR
      - Insurance
    properties:
      - type: Documentation
        url: https://developers.humana.com/
      - type: CapabilityStatement
        url: https://fhir.humana.com/api/metadata
      - type: Sandbox
        url: https://sandbox-fhir.humana.com/api/
  - aid: humana:humana-fhir-provider-directory-api
    name: Humana FHIR Provider Directory API
    description: FHIR R4-compliant API surface for provider directory information, including Patient, Practitioner, PractitionerRole, Organization, Location, and DocumentReference resources.
    humanURL: https://developers.humana.com/
    baseURL: https://fhir.humana.com/api
    tags:
      - FHIR
      - Provider Directory
    properties:
      - type: Documentation
        url: https://developers.humana.com/
      - type: CapabilityStatement
        url: https://fhir.humana.com/api/metadata
      - type: Sandbox
        url: https://sandbox-fhir.humana.com/api/
common:
  - type: Portal
    url: https://developers.humana.com/
  - type: Website
    url: https://www.humana.com/
  - type: Privacy Policy
    url: https://www.humana.com/legal/privacy-policy
  - type: Terms of Service
    url: https://www.humana.com/legal/terms-conditions
  - type: Rules
    url: https://raw.githubusercontent.com/api-evangelist/humana/refs/heads/main/humana-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
