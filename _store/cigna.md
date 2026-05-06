---
aid: cigna
name: Cigna
description: Cigna Healthcare is a leading global health services company offering medical, dental, behavioral, and pharmacy plans for individuals, families, and employers. The Cigna Developer Portal exposes CMS-mandated FHIR APIs for Patient Access, Provider Directory, Drug Formulary, and Provider Access, along with member and provider service APIs that enable third-party applications, electronic health record systems, and partners to access member health data with consent and look up Cigna network providers and formulary information.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/cigna/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consumer
tags:
  - CMS Interoperability
  - Da Vinci
  - Drug Formulary
  - FHIR
  - Health Insurance
  - Healthcare
  - Patient Access
  - Provider Directory
  - SMART on FHIR
created: '2025-02-21'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: cigna:patient-access-api
    name: Cigna Patient Access API
    description: FHIR R4 API that allows authorized third-party applications to access a Cigna member's claims, encounters, clinical data, coverage, and pharmacy information after the member completes SMART on FHIR authorization. Conforms to the CMS Interoperability and Patient Access final rule and the HL7 Da Vinci PDex implementation guide.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cigna.com/docs/service-apis/patient-access/implementation-guide
    baseURL: https://fhir.cigna.com/PatientAccess/v1
    tags:
      - CMS Interoperability
      - FHIR
      - Patient Access
      - SMART on FHIR
    properties:
      - type: Documentation
        url: https://developer.cigna.com/docs/service-apis/patient-access/implementation-guide
      - type: OpenAPI
        url: openapi/cigna-patient-access-api-openapi.yml
  - aid: cigna:provider-directory-api
    name: Cigna Provider Directory API
    description: Public FHIR-based Provider Directory API listing Cigna's contracted network providers, organizations, locations, healthcare services, and practitioner roles. Conforms to the HL7 Da Vinci PDex Plan Network implementation guide and the CMS Provider Directory API requirements.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cigna.com/docs/service-apis/provider-directory/implementation-guide
    baseURL: https://fhir.cigna.com/ProviderDirectory/v1
    tags:
      - CMS Interoperability
      - FHIR
      - Provider Directory
      - Public API
    properties:
      - type: Documentation
        url: https://developer.cigna.com/docs/service-apis/provider-directory/implementation-guide
      - type: OpenAPI
        url: openapi/cigna-provider-directory-api-openapi.yml
  - aid: cigna:drug-formulary-api
    name: Cigna Drug Formulary API
    description: Public FHIR-based Drug Formulary API exposing Cigna's covered drug lists, formulary tiers, prior authorization requirements, step therapy, and quantity limits. Implements the HL7 Da Vinci PDex US Drug Formulary implementation guide required by the CMS Interoperability and Patient Access rule.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cigna.com/docs/service-apis
    baseURL: https://fhir.cigna.com/DrugFormulary/v1
    tags:
      - CMS Interoperability
      - Drug Formulary
      - FHIR
      - Public API
    properties:
      - type: Documentation
        url: https://developer.cigna.com/docs/service-apis
      - type: OpenAPI
        url: openapi/cigna-drug-formulary-api-openapi.yml
  - aid: cigna:provider-access-api
    name: Cigna Provider Access API
    description: FHIR API that allows in-network providers, with appropriate authorization, to retrieve a Cigna member's clinical and claims data to support care coordination. Implements the HL7 Da Vinci PDex Provider Access implementation guide and conforms to the CMS Interoperability and Prior Authorization final rule.
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.cigna.com/docs/service-apis
    baseURL: https://fhir.cigna.com/ProviderAccess/v1
    tags:
      - CMS Interoperability
      - FHIR
      - Provider Access
    properties:
      - type: Documentation
        url: https://developer.cigna.com/docs/service-apis
      - type: OpenAPI
        url: openapi/cigna-provider-access-api-openapi.yml
common:
  - type: Website
    url: https://www.cigna.com/
  - type: DeveloperPortal
    url: https://developer.cigna.com/
  - type: Portal
    url: https://developer.cigna.com/
  - type: Documentation
    url: https://developer.cigna.com/docs/service-apis
  - type: Support
    url: https://developer.cigna.com/support
  - type: TermsOfService
    url: https://www.cigna.com/legal/terms-of-use
  - type: PrivacyPolicy
    url: https://www.cigna.com/legal/privacy
  - type: JSONLDContext
    url: json-ld/cigna-context.jsonld
  - type: JSONSchema
    url: json-schema/cigna-patient-schema.json
  - type: Spectral
    url: spectral/cigna-spectral.yml
  - type: NaftikoCapabilities
    url: naftiko/cigna-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
