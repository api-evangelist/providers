---
aid: agechecker-net
url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/apis.yml
apis:
  - aid: agechecker-net:agechecker-net-age-verification-api
    name: AgeChecker.Net Age Verification API
    tags:
      - Age Verification
      - Identity
      - Compliance
    humanURL: https://agechecker.net/age-verification-api
    baseURL: https://api.agechecker.net/v1
    properties:
      - url: https://agechecker.net/age-verification-api
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/openapi/agechecker-net-age-verification-openapi.yml
        type: OpenAPI
    description: The AgeChecker.Net Age Verification API provides seamless age verification for online transactions. Send customer data directly to verify age without requiring a popup for most customers. Only customers requiring photo ID will be prompted for additional verification.
    contact:
      - FN: AgeChecker.Net Support
        url: https://agechecker.net/contact
name: AgeChecker.Net
tags:
  - Age Verification
  - Identity
  - Compliance
  - Regulatory
  - E-Commerce
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-07'
modified: '2026-04-19'
position: Consuming
description: AgeChecker.Net provides age verification API services for e-commerce businesses selling age-restricted products such as alcohol, tobacco, cannabis, and firearms. The API enables seamless background verification for most customers and guided photo ID verification for those who cannot be automatically verified.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
features:
  - Seamless Background Age Verification
  - Photo ID Upload and Verification
  - Webhook Notifications for Verification Events
  - Session-Based Verification Tracking
  - Support for Multiple Age Thresholds (18, 21+)
  - US Address Verification Integration
  - COPPA and CIPA Compliance Support
useCases:
  - Alcohol and Beverage E-Commerce Age Gating
  - Tobacco and Vape Product Age Verification
  - Cannabis Dispensary Online Order Verification
  - Firearms and Ammunition Purchase Compliance
  - Adult Content Platform Age Gates
  - Regulated Pharmaceutical Online Sales
integrations:
  - Shopify Age Verification
  - WooCommerce Age Gate Plugin
  - BigCommerce Age Verification
  - Magento Age Check Integration
  - Custom E-Commerce Platform Integration
common:
  - url: https://agechecker.net
    type: Portal
  - url: https://agechecker.net/age-verification-api
    type: GettingStarted
  - url: https://agechecker.net/terms
    type: TermsOfService
  - url: https://agechecker.net/privacy
    type: PrivacyPolicy
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/rules/agechecker-net-spectral-rules.yml
    type: SpectralRules
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/capabilities/age-verification.yaml
    type: NaftikoCapability
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/capabilities/shared/age-verification-api.yaml
    type: NaftikoCapability
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/json-schema/agechecker-verification-request-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/json-schema/agechecker-verification-response-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/json-schema/agechecker-session-schema.json
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/json-ld/agechecker-verification-context.jsonld
    type: JSONLDContext
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/examples/agechecker-verification-request-example.json
    type: Example
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/examples/agechecker-verification-response-example.json
    type: Example
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/examples/agechecker-session-example.json
    type: Example
  - url: https://raw.githubusercontent.com/api-evangelist/agechecker-net/refs/heads/main/vocabulary/agechecker-net-vocabulary.yaml
    type: Vocabulary
---
