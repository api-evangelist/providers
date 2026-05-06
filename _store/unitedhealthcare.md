---
aid: unitedhealthcare
url: https://raw.githubusercontent.com/api-evangelist/unitedhealthcare/refs/heads/main/apis.yml
name: UnitedHealthcare
description: UnitedHealthcare is one of the largest health insurance providers in the United States, offering employer-sponsored health benefits, individual and family plans, Medicare and Medicaid plans, and managed care services. UnitedHealthcare provides APIs for healthcare providers through the UHC API Marketplace for eligibility verification, claims management, and prior authorization, and FHIR R4-compliant Interoperability APIs for patient data access and provider directory services per CMS mandates.
tags:
  - Health Insurance
  - Healthcare
  - FHIR
  - Claims
  - Eligibility
type: Company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-05-03'
position: Consuming
specificationVersion: '0.19'
apis:
  - aid: unitedhealthcare:provider-api
    name: UnitedHealthcare Provider API
    tags:
      - Health Insurance
      - Healthcare
      - Eligibility
      - Claims
      - Prior Authorization
    humanURL: https://apimarketplace.uhcprovider.com/#/
    baseURL: https://api.uhcprovider.com
    description: The UnitedHealthcare Provider API provides real-time access to eligibility verification, claims management, prior authorization, and provider directory services through the UHC API Marketplace. Enables healthcare providers to verify member coverage, check claim status, validate claims before submission, check prior authorization requirements, and access provider demographic data.
    properties:
      - url: https://apimarketplace.uhcprovider.com/#/
        type: Documentation
      - url: openapi/unitedhealthcare-provider-api-openapi.yml
        type: OpenAPI
      - url: json-schema/provider-eligibility-response-schema.json
        type: Schema
      - url: json-schema/provider-claim-inquiry-response-schema.json
        type: Schema
      - url: json-ld/unitedhealthcare-provider-api-context.jsonld
        type: JSON-LD Context
      - url: examples/provider-eligibility-response-example.json
        type: Example
  - aid: unitedhealthcare:interoperability-api
    name: UnitedHealthcare Interoperability API
    tags:
      - Health Insurance
      - Healthcare
      - FHIR
      - Patient Access
      - Provider Directory
      - Formulary
    humanURL: https://www.uhc.com/legal/interoperability-apis
    baseURL: https://api.uhc.com/fhir/R4
    description: The UnitedHealthcare Interoperability APIs provide FHIR R4-compliant access to patient health data in compliance with CMS Interoperability and Patient Access final rule (CMS-9115-F). Includes Patient Access API for member claims history, coverage, and health records, Provider Directory API for network provider search, and Formulary API for drug coverage information.
    properties:
      - url: https://www.uhc.com/legal/interoperability-apis
        type: Documentation
      - url: openapi/unitedhealthcare-interoperability-api-openapi.yml
        type: OpenAPI
      - url: json-schema/interoperability-fhir-bundle-schema.json
        type: Schema
      - url: json-schema/interoperability-fhir-patient-schema.json
        type: Schema
      - url: json-ld/unitedhealthcare-interoperability-api-context.jsonld
        type: JSON-LD Context
      - url: examples/interoperability-fhir-bundle-example.json
        type: Example
features:
  - name: Real-Time Eligibility Verification
    description: Verify UnitedHealthcare member eligibility and benefits in real time at the point of care, reducing claim denials and improving patient financial transparency.
  - name: Claim Pre-Check
    description: Validate claims before submission to identify errors, missing authorizations, and billing issues that would cause denials, accelerating payment cycles.
  - name: Prior Authorization Check
    description: Determine prior authorization requirements for procedures and check existing authorization status to streamline clinical workflows.
  - name: FHIR R4 Patient Access
    description: CMS-mandated FHIR R4 APIs enabling patients and authorized applications to access claims history, coverage data, and clinical information.
  - name: Provider Directory
    description: FHIR R4 Provider Directory implementing Da Vinci PDex Plan Net IG for searching UnitedHealthcare network providers, organizations, and locations.
  - name: Drug Formulary
    description: FHIR-based formulary API providing drug coverage tier information, prior authorization requirements, and quantity limits for prescription medications.
  - name: Claims Inquiry
    description: Real-time claim status inquiry returning payment details, denial reasons, adjustment codes, and explanation of benefits data.
useCases:
  - name: Point-of-Care Eligibility
    description: Verify patient UnitedHealthcare coverage and benefits at check-in using the real-time eligibility API to collect accurate copays and reduce billing errors.
  - name: Revenue Cycle Management
    description: Integrate claim pre-check and claim inquiry APIs into practice management systems to automate claim validation and track payment status.
  - name: Prior Authorization Workflows
    description: Embed prior authorization checking in clinical workflows to immediately determine if approval is needed before scheduling procedures or prescribing medications.
  - name: Patient Portal Integration
    description: Enable patient portals to display claims history, coverage details, and EOBs using the FHIR Patient Access API for transparent member engagement.
  - name: Provider Search Applications
    description: Build provider search tools and care coordination apps using the FHIR Provider Directory API to find in-network physicians, specialists, and facilities.
  - name: Formulary Management
    description: Integrate the Formulary API into EHR and e-prescribing workflows to check drug coverage tiers and authorization requirements at point of prescribing.
integrations:
  - name: Epic Systems
    description: UnitedHealthcare APIs integrate with Epic EHR for real-time eligibility verification, prior authorization, and FHIR-based data exchange.
  - name: Cerner/Oracle Health
    description: FHIR R4 Interoperability APIs integrate with Cerner for patient data access and provider directory services.
  - name: Change Healthcare
    description: Provider APIs complement Change Healthcare clearinghouse services for comprehensive claims management and eligibility verification.
  - name: Availity
    description: UnitedHealthcare participates in Availity's real-time eligibility and claims network providing additional access pathways for providers.
artifacts:
  openapi:
    - name: UnitedHealthcare Provider API
      url: openapi/unitedhealthcare-provider-api-openapi.yml
    - name: UnitedHealthcare Interoperability API
      url: openapi/unitedhealthcare-interoperability-api-openapi.yml
  jsonSchema:
    - url: json-schema/provider-eligibility-request-schema.json
    - url: json-schema/provider-eligibility-response-schema.json
    - url: json-schema/provider-benefit-check-request-schema.json
    - url: json-schema/provider-benefit-check-response-schema.json
    - url: json-schema/provider-claim-pre-check-request-schema.json
    - url: json-schema/provider-claim-pre-check-response-schema.json
    - url: json-schema/provider-claim-inquiry-request-schema.json
    - url: json-schema/provider-claim-inquiry-response-schema.json
    - url: json-schema/provider-prior-auth-check-request-schema.json
    - url: json-schema/provider-prior-auth-check-response-schema.json
    - url: json-schema/provider-provider-demographics-schema.json
    - url: json-schema/interoperability-fhir-bundle-schema.json
    - url: json-schema/interoperability-fhir-patient-schema.json
  jsonStructure:
    - url: json-structure/provider-eligibility-response-structure.json
    - url: json-structure/provider-claim-inquiry-response-structure.json
    - url: json-structure/provider-provider-demographics-structure.json
    - url: json-structure/interoperability-fhir-bundle-structure.json
    - url: json-structure/interoperability-fhir-patient-structure.json
  jsonLd:
    - url: json-ld/unitedhealthcare-provider-api-context.jsonld
    - url: json-ld/unitedhealthcare-interoperability-api-context.jsonld
  examples:
    - url: examples/provider-eligibility-response-example.json
    - url: examples/provider-claim-inquiry-response-example.json
    - url: examples/provider-prior-auth-check-response-example.json
    - url: examples/interoperability-fhir-bundle-example.json
    - url: examples/interoperability-fhir-patient-example.json
  spectralRules:
    - url: rules/unitedhealthcare-spectral-rules.yml
  capabilities:
    shared:
      - url: capabilities/shared/provider-api.yaml
      - url: capabilities/shared/interoperability-api.yaml
    workflows:
      - url: capabilities/provider-operations.yaml
      - url: capabilities/patient-data-access.yaml
  vocabulary:
    - url: vocabulary/unitedhealthcare-vocabulary.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
