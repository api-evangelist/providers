---
aid: wellcare-health-plans
url: https://raw.githubusercontent.com/api-evangelist/wellcare-health-plans/refs/heads/main/apis.yml
modified: '2026-05-03'
description: WellCare Health Plans was a managed care company that focused exclusively on government-sponsored managed care services through Medicaid, Medicare Advantage, and Medicare Prescription Drug Plans before being acquired by Centene Corporation. Now operating under Centene, WellCare provides FHIR- compliant APIs for interoperability and patient access as required by CMS Interoperability and Patient Access final rules (CMS-9115-F). The Centene Developer Partner Portal at partners.centene.com/apis provides access to WellCare FHIR APIs.
common:
  - type: Website
    url: https://www.wellcare.com
  - type: DeveloperPortal
    url: https://partners.centene.com/apis
  - type: InteroperabilityPortal
    url: https://www.wellcare.com/en/interoperability-and-patient-access
  - type: GitHubOrg
    url: https://github.com/wellcare-health-plans
  - type: JSONLDContext
    url: json-ld/wellcare-health-plans-context.jsonld
  - type: Vocabulary
    url: vocabulary/wellcare-health-plans-vocabulary.yml
apis:
  - aid: wellcare-health-plans:fhir-patient-access-api
    name: WellCare FHIR Patient Access API
    tags:
      - Healthcare
      - FHIR
      - Interoperability
      - Patient Access
      - Managed Care
      - Medicaid
      - Medicare
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://partners.centene.com
    humanURL: https://www.wellcare.com/en/interoperability-and-patient-access
    properties:
      - url: https://www.wellcare.com/en/interoperability-and-patient-access
        type: Documentation
      - url: https://partners.centene.com/apis
        type: Portal
      - url: openapi/wellcare-fhir-patient-access-api-openapi.yml
        type: OpenAPI
      - url: json-schema/wellcare-fhir-patient-schema.json
        type: JSONSchema
      - url: json-schema/wellcare-fhir-eob-schema.json
        type: JSONSchema
      - url: json-structure/wellcare-fhir-patient-structure.json
        type: JSONStructure
      - url: examples/wellcare-fhir-patient-access-api-getPatient-example.json
        type: Example
      - url: examples/wellcare-fhir-patient-access-api-listExplanationOfBenefit-example.json
        type: Example
      - url: rules/wellcare-health-plans-rules.yml
        type: SpectralRuleset
      - url: capabilities/shared/fhir-patient-access.yaml
        type: NaftikoCapability
    description: The WellCare FHIR Patient Access API enables members and authorized third-party applications to securely access and exchange health data including medical, pharmacy, dental, and vision claims and clinical information. The API supports HL7 FHIR R4 standards and SMART on FHIR authorization, providing access to up to 5 years of historical health information. Required under CMS Interoperability and Patient Access final rule (CMS-9115-F) for Medicaid and Medicare Advantage plans.
  - aid: wellcare-health-plans:fhir-provider-directory-api
    name: WellCare FHIR Provider Directory API
    tags:
      - Healthcare
      - FHIR
      - Interoperability
      - Provider Directory
      - Managed Care
      - Medicaid
      - Medicare
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://partners.centene.com
    humanURL: https://www.wellcare.com/en/interoperability-and-patient-access
    properties:
      - url: https://www.wellcare.com/en/interoperability-and-patient-access
        type: Documentation
      - url: https://partners.centene.com/apis
        type: Portal
      - url: openapi/wellcare-fhir-provider-directory-api-openapi.yml
        type: OpenAPI
      - url: examples/wellcare-fhir-provider-directory-api-searchPractitioners-example.json
        type: Example
      - url: rules/wellcare-health-plans-rules.yml
        type: SpectralRuleset
      - url: capabilities/shared/fhir-provider-directory.yaml
        type: NaftikoCapability
    description: The WellCare FHIR Provider Directory API provides access to up-to-date provider directory information, enabling third-party applications to query in-network physicians, specialists, hospitals, and other healthcare providers. The API follows HL7 FHIR R4 standards and Da Vinci Provider Directory implementation guide (PDex Plan-Net), supporting CMS interoperability requirements for Medicaid and Medicare Advantage plans.
---
