---
aid: community-health-systems
url: https://raw.githubusercontent.com/api-evangelist/community-health-systems/refs/heads/main/apis.yml
name: Community Health Systems
tags:
  - CMS-9115-F
  - FHIR
  - Healthcare
  - Hospitals
  - Interoperability
  - Patient Access
  - Provider Directory
  - SMART-on-FHIR
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2026-03-21'
modified: '2026-04-26'
position: Consumer
description: Community Health Systems (CHS) is a Fortune 500 hospital operator that owns, leases, and operates general acute care hospitals across the United States. In compliance with the CMS Interoperability and Patient Access Final Rule (CMS-9115-F), CHS publishes FHIR R4 healthcare interoperability APIs that allow third-party applications to access patient demographics and clinical data, adjudicated claims and encounters, formulary information, and provider directory data. The APIs use the HL7 FHIR R4 standard and SMART-on-FHIR authorization for patient-scoped access.
apis:
  - aid: community-health-systems:patient-access-api
    name: Community Health Systems Patient Access API
    tags:
      - CMS-9115-F
      - FHIR
      - Healthcare
      - Interoperability
      - Patient Access
      - SMART-on-FHIR
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.chs.net/fhir/r4
    humanURL: https://www.chs.net
    properties:
      - url: https://www.chs.net
        type: Documentation
      - url: https://www.cms.gov/regulations-and-guidance/guidance/interoperability/index
        type: CMSFinalRule
      - url: openapi/chs-patient-access-api-openapi.yml
        type: OpenAPI
    description: FHIR R4 API published pursuant to the CMS Interoperability and Patient Access Final Rule (CMS-9115-F). Allows third-party applications, with the patient's authorization, to retrieve adjudicated claims and encounters (ExplanationOfBenefit), formulary and medication data (MedicationKnowledge), and clinical data (Patient and related resources). Authentication uses SMART-on-FHIR OAuth2 with patient/launch scopes.
    x-features:
      - FHIR R4 conformance
      - SMART-on-FHIR OAuth2 authorization-code flow
      - patient/*.read and launch/patient scopes
      - Patient, ExplanationOfBenefit, MedicationKnowledge resource endpoints
      - Bundle search-set responses (application/fhir+json)
    x-use-cases:
      - Patient-authorized third-party app access to claims
      - Personal-health-record (PHR) integration for CHS patients
      - Pharmacy and formulary lookups for member-facing apps
      - Population-health analytics with patient consent
  - aid: community-health-systems:provider-directory-api
    name: Community Health Systems Provider Directory API
    tags:
      - CMS-9115-F
      - FHIR
      - Healthcare
      - Interoperability
      - Provider Directory
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.chs.net/fhir/r4
    humanURL: https://www.chs.net
    properties:
      - url: https://www.chs.net
        type: Documentation
      - url: https://www.cms.gov/regulations-and-guidance/guidance/interoperability/index
        type: CMSFinalRule
    description: FHIR R4 read API exposing provider and pharmacy directory data in compliance with CMS interoperability requirements. Third-party applications can search Practitioner, Organization, and Location resources without patient consent (no PHI is exposed by these directory endpoints).
    x-features:
      - FHIR R4 Practitioner, Organization, Location resources
      - Public read access (no patient consent required)
      - Search by name, specialty, location
    x-use-cases:
      - Public provider/pharmacy directory lookup
      - Network adequacy and accessibility reporting
      - Care coordination and referral apps
common:
  - type: Website
    url: https://www.chs.net
  - type: PatientPortal
    url: https://www.chs.net/patients-visitors/
  - type: Investors
    url: https://www.chs.net/investors/
  - type: PrivacyPolicy
    url: https://www.chs.net/privacy-statement/
  - type: CMSInteroperability
    url: https://www.cms.gov/regulations-and-guidance/guidance/interoperability/index
  - type: HL7FHIRR4
    url: https://hl7.org/fhir/R4/
  - url: json-ld/community-health-systems-context.jsonld
    type: JSON-LD
  - url: json-schema/chs-fhir-bundle-schema.json
    type: JSONSchema
  - url: rules/community-health-systems-rules.yml
    type: Spectral
  - url: capabilities/community-health-systems-fhir-capabilities.yml
    type: NaftikoCapabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
