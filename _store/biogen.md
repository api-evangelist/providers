---
aid: biogen
url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/apis.yml
apis:
  - aid: biogen:developer-api
    name: Biogen Developer API
    tags:
      - Biotechnology
      - Healthcare
      - Life Sciences
      - Pharmaceuticals
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://developer.biogen.com
    humanURL: https://developer.biogen.com/
    properties:
      - type: Portal
        url: https://developer.biogen.com/
      - type: Documentation
        url: https://developer.biogen.com/io-docs
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/openapi/biogen-developer-api-openapi.yml
    description: The Biogen Developer API provides programmatic access to Biogen services including the CCS-CRX API following REST standard specifications. The portal offers interactive I/O docs for testing API services, access key management, usage reporting, and detailed documentation covering supported methods, HTTP headers, request/response formats, and response codes.
description: Biogen is a global biotechnology company that discovers, develops, and delivers therapies for people living with serious neurological diseases including multiple sclerosis, Alzheimer's, and spinal muscular atrophy.
name: Biogen
type: Contract
access: 3rd-Party
position: Consuming
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Biotechnology
  - Healthcare
  - Life Sciences
  - Pharmaceuticals
  - Neurology
created: '2025-01-01'
modified: '2026-04-21'
specificationVersion: '0.19'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developer.biogen.com/
  - type: Website
    url: https://www.biogen.com/
  - type: Documentation
    url: https://developer.biogen.com/io-docs
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/rules/biogen-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/vocabulary/biogen-vocabulary.yaml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/biogen/refs/heads/main/capabilities/api-access-management.yaml
  - type: Features
    data:
      - name: CCS-CRX API
        description: Programmatic access to Copaxone CRX pharmaceutical service.
      - name: API Key Management
        description: Self-service API key creation and usage monitoring via developer portal.
      - name: Interactive I/O Docs
        description: Interactive API documentation for testing endpoints directly in the browser.
      - name: Usage Reporting
        description: Monitor API request volumes and usage statistics per key.
      - name: REST Standards
        description: REST-compliant API design following standard HTTP methods and response codes.
  - type: UseCases
    data:
      - name: Pharmaceutical Service Integration
        description: Integrate with Biogen pharmaceutical services like CCS-CRX programmatically.
      - name: Developer Onboarding
        description: Self-service API key registration and service access via developer portal.
      - name: Healthcare System Integration
        description: Connect healthcare systems to Biogen services for patient program support.
  - type: Integrations
    data:
      - name: Healthcare IT Systems
        description: Connect EHR and healthcare IT systems to Biogen pharmaceutical APIs.
      - name: Patient Support Programs
        description: Integrate with Biogen patient support and copay assistance programs.
---
