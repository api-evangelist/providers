---
aid: unitedhealth
url: https://raw.githubusercontent.com/api-evangelist/unitedhealth/refs/heads/main/apis.yml
name: UnitedHealth Group
description: UnitedHealth Group is a diversified health care company with two distinct platforms, UnitedHealthcare for health benefits and Optum for health services, serving more than 100 million people worldwide. The company offers FHIR R4-compliant Interoperability APIs through the Optum platform, providing patient access to health records, claims history, provider directory, and drug formulary data in compliance with CMS Interoperability and Patient Access final rule (CMS-9115-F) and HL7 FHIR standards.
tags:
  - Healthcare
  - Health Insurance
  - FHIR
  - Claims
  - Interoperability
type: Company
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-21'
modified: '2026-05-03'
position: Consuming
specificationVersion: '0.19'
apis:
  - aid: unitedhealth:optum-api
    name: UnitedHealth Group Optum API
    tags:
      - Healthcare
      - FHIR
      - Patient Access
      - Provider Directory
      - Drug Formulary
      - CMS Interoperability
    baseURL: https://api.uhc.com/fhir/R4
    humanURL: https://www.uhc.com/legal/interoperability-apis
    description: The UnitedHealth Group interoperability APIs provide FHIR R4-compliant access to healthcare data including patient records, claims history, provider directories, and formulary information in compliance with CMS interoperability rules. Operates under the Optum platform serving UnitedHealthcare, Medicare & Retirement, Community & State, and Optum health services.
    properties:
      - url: https://www.uhc.com/legal/interoperability-apis
        type: Documentation
      - url: openapi/unitedhealth-optum-api-openapi.yml
        type: OpenAPI
      - url: json-schema/optum-fhir-bundle-schema.json
        type: Schema
      - url: json-schema/optum-fhir-patient-schema.json
        type: Schema
      - url: json-ld/unitedhealth-optum-api-context.jsonld
        type: JSON-LD Context
      - url: examples/optum-fhir-patient-example.json
        type: Example
features:
  - name: FHIR R4 Patient Access API
    description: CMS-mandated FHIR R4 Patient Access API providing members and third-party applications with access to claims, EOBs, coverage details, and clinical data.
  - name: Provider Directory API
    description: FHIR R4 Provider Directory implementing Da Vinci PDex Plan Net IG for searching UnitedHealth Group network practitioners and organizations.
  - name: Drug Formulary API
    description: FHIR R4 Drug Formulary API implementing Da Vinci Drug Formulary IG for accessing prescription drug coverage tiers, prior auth requirements, and quantity limits.
  - name: Claims History Access
    description: FHIR ExplanationOfBenefit resources providing comprehensive claims history including service details, diagnosis codes, and payment adjudication.
  - name: Clinical Data Exchange
    description: FHIR Condition and clinical data resources for member health history as reflected in claims and available clinical records.
  - name: Coverage Information
    description: FHIR Coverage resources for current and historical insurance coverage details across UnitedHealthcare commercial, Medicare, and Medicaid plans.
useCases:
  - name: Patient Portal Health Data
    description: Enable patient portals to display complete health records including claims, coverage, and conditions using FHIR Patient Access APIs.
  - name: Care Coordination Apps
    description: Build care management tools that aggregate member health history, coverage, and clinical data for population health management.
  - name: Provider Network Search
    description: Develop provider search applications using the FHIR Provider Directory to help members find in-network physicians and specialists.
  - name: Prescription Benefit Transparency
    description: Integrate drug formulary data into clinical and patient-facing applications to show coverage tiers and prior authorization requirements.
  - name: CMS Compliance Applications
    description: Build CMS-compliant third-party applications leveraging UnitedHealth Group's FHIR R4 interoperability infrastructure for data portability.
  - name: Claims Analytics
    description: Access structured claims data as FHIR ExplanationOfBenefit resources for population health analytics and care gap identification.
integrations:
  - name: Apple Health Records
    description: UnitedHealth Group FHIR Patient Access API integrates with Apple Health Records for member health data access on iOS devices.
  - name: CommonWell Health Alliance
    description: UnitedHealth Group participates in CommonWell for FHIR-based health information exchange across provider networks.
  - name: Carequality
    description: FHIR data exchange integration through Carequality framework for nationwide health information network connectivity.
  - name: Da Vinci Project
    description: UnitedHealth Group implements Da Vinci IGs for payer data exchange including PDex Plan Net for provider directory and Drug Formulary IG.
artifacts:
  openapi:
    - name: UnitedHealth Group Optum API
      url: openapi/unitedhealth-optum-api-openapi.yml
  jsonSchema:
    - url: json-schema/optum-fhir-bundle-schema.json
    - url: json-schema/optum-fhir-patient-schema.json
    - url: json-schema/optum-fhir-explanation-of-benefit-schema.json
    - url: json-schema/optum-fhir-coverage-schema.json
    - url: json-schema/optum-fhir-practitioner-schema.json
    - url: json-schema/optum-fhir-medication-knowledge-schema.json
  jsonStructure:
    - url: json-structure/optum-fhir-bundle-structure.json
    - url: json-structure/optum-fhir-patient-structure.json
    - url: json-structure/optum-fhir-explanation-of-benefit-structure.json
    - url: json-structure/optum-fhir-coverage-structure.json
    - url: json-structure/optum-fhir-practitioner-structure.json
    - url: json-structure/optum-fhir-medication-knowledge-structure.json
  jsonLd:
    - url: json-ld/unitedhealth-optum-api-context.jsonld
  examples:
    - url: examples/optum-fhir-patient-example.json
    - url: examples/optum-fhir-bundle-example.json
    - url: examples/optum-fhir-coverage-example.json
    - url: examples/optum-fhir-practitioner-example.json
    - url: examples/optum-fhir-medication-knowledge-example.json
  spectralRules:
    - url: rules/unitedhealth-spectral-rules.yml
  capabilities:
    shared:
      - url: capabilities/shared/optum-api.yaml
    workflows:
      - url: capabilities/health-data-interoperability.yaml
  vocabulary:
    - url: vocabulary/unitedhealth-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
