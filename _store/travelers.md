---
aid: travelers
name: Travelers
description: Travelers is one of the largest property casualty insurance companies in the United States and a Fortune 500 company. Through their developer portal, Travelers provides APIs for business insurance claim reporting, commercial quoting, and policy management to enable agents, brokers, and partners to programmatically manage insurance workflows.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Insurance
  - Property Casualty
  - Commercial Insurance
  - Claims
  - Fintech
  - Fortune 500
created: '2026-05-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/travelers/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: travelers:travelers
    name: Travelers API
    description: Business insurance APIs for claim reporting, commercial lines quoting, and policy management. Enables agents, brokers, and commercial clients to programmatically manage insurance workflows across property, casualty, workers compensation, and commercial auto lines.
    humanURL: https://developer.travelers.com/s/
    baseURL: https://api.travelers.com/v1
    tags:
      - Insurance
      - Property Casualty
      - Commercial Insurance
      - Claims
      - Quoting
      - Fortune 500
    properties:
      - type: Documentation
        url: https://developer.travelers.com/s/apis
      - type: OpenAPI
        url: openapi/travelers-openapi.yml
      - type: JSONSchema
        url: json-schema/travelers-claim-schema.json
      - type: JSONStructure
        url: json-structure/travelers-claim-structure.json
      - type: JSONLD
        url: json-ld/travelers-context.jsonld
      - type: SpectralRules
        url: rules/travelers-rules.yml
      - type: NaftikoCapabilities
        url: capabilities/commercial-insurance-workflow.yaml
      - type: Vocabulary
        url: vocabulary/travelers-vocabulary.yml
      - type: Sign Up
        url: https://developer.travelers.com/s/
    x-apis:
      - Business Insurance Claim Reporting API
      - Commercial Quoting API
      - Policy Management API
    x-policy-types:
      - property
      - casualty
      - workers-compensation
      - commercial-auto
      - general-liability
      - business-owners-policy
common:
  - type: Website
    url: https://www.travelers.com/
  - type: Developer Portal
    url: https://developer.travelers.com/s/
  - type: Documentation
    url: https://developer.travelers.com/s/apis
  - type: Sign Up
    url: https://developer.travelers.com/s/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
