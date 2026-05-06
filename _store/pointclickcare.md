---
aid: pointclickcare
name: PointClickCare
description: PointClickCare is the leading cloud-based software platform for the senior care and post-acute care industry, providing electronic health records (EHR), care coordination, financial management, and clinical decision support to skilled nursing facilities, senior living communities, and home health agencies. PointClickCare publishes both a partner EHR API and a HL7 FHIR API for clinical interoperability across the long-term and post-acute care (LTPAC) ecosystem.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Healthcare
  - Long-Term Care
  - Post-Acute Care
  - EHR
  - FHIR
  - Senior Care
  - Interoperability
url: https://raw.githubusercontent.com/api-evangelist/pointclickcare/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: pointclickcare:pointclickcare-ehr-api
    name: PointClickCare Long-Term Care EHR API
    description: PointClickCare provides EHR and care coordination APIs for long-term and post-acute care facilities. APIs enable access to resident records, medication administration, clinical assessments, and care plan data for skilled nursing facilities and senior living communities.
    humanURL: https://developer.pointclickcare.com/spa
    baseURL: https://api.pointclickcare.com/v2
    tags:
      - Healthcare
      - Long-Term Care
      - EHR
      - Senior Care
      - REST
    properties:
      - type: Documentation
        url: https://developer.pointclickcare.com/spa
      - type: Portal
        url: https://developer.pointclickcare.com/spa
      - type: OpenAPI
        url: openapi/pointclickcare-ehr-openapi.yml
      - type: JSONSchema
        url: json-schema/pointclickcare-patient-schema.json
      - type: JSONLDContext
        url: json-ld/pointclickcare-context.jsonld
  - aid: pointclickcare:pointclickcare-fhir-api
    name: PointClickCare FHIR API
    description: PointClickCare FHIR API provides HL7 FHIR-compliant access to resident clinical data for post-acute and long-term care settings, supporting interoperability with other healthcare systems and care coordination platforms.
    humanURL: https://developer.pointclickcare.com/spa
    tags:
      - Healthcare
      - Long-Term Care
      - FHIR
      - HL7
      - Interoperability
      - REST
    properties:
      - type: Documentation
        url: https://developer.pointclickcare.com/spa
common:
  - type: Portal
    url: https://developer.pointclickcare.com/spa
  - type: Documentation
    url: https://developer.pointclickcare.com/spa
  - type: Website
    url: https://www.pointclickcare.com/
  - type: Support
    url: https://pointclickcare.com/customer-support/
  - type: Blog
    url: https://pointclickcare.com/blog/
  - type: PrivacyPolicy
    url: https://pointclickcare.com/privacy-policy/
  - type: TermsOfService
    url: https://pointclickcare.com/legal/terms-conditions/
  - type: Status
    url: https://status.pointclickcare.com/
  - type: GitHubOrganization
    url: https://github.com/PointClickCare
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
