---
aid: vistra
name: Vistra
description: Vistra is a global corporate services provider operating in over 45 jurisdictions, offering entity management, incorporation, compliance, payroll, and fund administration services. The Vistra REST API enables developers to programmatically submit company incorporation requests in supported jurisdictions (initially British Virgin Islands), upload supporting documents to pre-signed storage URLs, and integrate Vistra's corporate services into business process workflows. Authentication uses OAuth2 bearer tokens obtained through the Vistra Developer Portal.
image: https://www.vistra.com/themes/custom/vistra/logo.svg
type: Index
tags:
  - Compliance
  - Corporate Services
  - Entity Management
  - Finance
  - Fortune 500
  - Legal
url: https://raw.githubusercontent.com/api-evangelist/vistra/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vistra:incorporations-api
    name: Vistra Incorporations API
    description: 'The Vistra Incorporations API enables programmatic submission of company incorporation requests in supported jurisdictions. Currently available for the British Virgin Islands (BVI) on an invite-only basis, the API supports the full incorporation workflow: generating pre-signed S3 document upload URLs, confirming document upload completion, and submitting incorporation requests with entity details, stakeholder information, shareholding structure, and compliance data. Authentication requires OAuth2 bearer tokens obtained from the Vistra Developer Portal.'
    humanURL: https://help.vistra.com/en/articles/10351085-vistra-incorporations-api-british-virgin-islands
    baseURL: https://api.vistra.com
    tags:
      - BVI
      - British Virgin Islands
      - Compliance
      - Corporate Services
      - Entity Management
      - Incorporation
      - Legal
      - OAuth2
    properties:
      - type: Documentation
        url: https://help.vistra.com/en/articles/10351085-vistra-incorporations-api-british-virgin-islands
      - type: Developer Portal
        url: https://devportal.vistra.com/
      - type: OpenAPI
        url: openapi/vistra-incorporations-openapi.yml
    contact:
      - FN: Vistra Support
        url: https://help.vistra.com/en/
common:
  - type: Website
    url: https://www.vistra.com
  - type: Developer Portal
    url: https://devportal.vistra.com/
  - type: Help Center
    url: https://help.vistra.com/en/
  - type: Client Portals
    url: https://www.vistra.com/client-portals
  - type: Entity Management
    url: https://www.vistra.com/corporate/entity-management
  - type: Privacy Policy
    url: https://www.vistra.com/privacy-policy
  - type: OpenAPI
    url: openapi/vistra-incorporations-openapi.yml
  - type: JSONSchema
    url: json-schema/vistra-incorporation-schema.json
  - type: JSONLD
    url: json-ld/vistra-context.jsonld
  - type: Vocabulary
    url: vocabulary/vistra-vocabulary.yml
  - type: SpectralRules
    url: rules/vistra-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
