---
aid: tremendous
name: Tremendous
description: Tremendous allows businesses to send rewards, incentives, and payouts worldwide using their simple API and dashboard. Access 2000+ payout methods including US and global bank transfers, Amazon.com gift cards, Visa and Mastercard prepaid cards, PayPal, Venmo, and charity donations. Supports multi-product rewards (recipient choice) and single-product rewards.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Employee Incentives
  - Global Payouts
  - Incentives
  - Market Research
  - Payouts
  - Rewards
created: '2025-02-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tremendous/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tremendous:tremendous
    name: Tremendous API
    description: 'The Tremendous REST API enables businesses to programmatically send rewards, incentives, and payouts worldwide. The API covers orders, rewards, products, campaigns, funding sources, organizations, members, invoices, and webhooks. Authentication uses Bearer API keys or OAuth 2.0. Rate limit: 30 requests per 30 seconds.'
    humanURL: https://developers.tremendous.com/
    baseURL: https://testflight.tremendous.com/api/v2
    tags:
      - Employee Incentives
      - Global Payouts
      - Incentives
      - Market Research
      - Payouts
      - Rewards
    properties:
      - type: Documentation
        url: https://developers.tremendous.com/docs/introduction
      - type: Reference
        url: https://developers.tremendous.com/reference/api-endpoints-overview
      - type: GitHubOrganization
        url: https://github.com/tremendous-rewards
      - type: GitHubRepository
        url: https://github.com/tremendous-rewards/api-docs
      - type: GitHubRepository
        url: https://github.com/tremendous-rewards/tremendous-node
      - type: OpenAPI
        url: openapi/tremendous-api-openapi.yml
common:
  - type: Website
    url: https://www.tremendous.com/
  - type: Documentation
    url: https://developers.tremendous.com/
  - type: Sign Up
    url: https://app.tremendous.com/auth/sign_up
  - type: Sandbox
    url: https://testflight.tremendous.com
  - type: GitHubOrganization
    url: https://github.com/tremendous-rewards
  - type: SDK
    url: https://github.com/tremendous-rewards/tremendous-node
  - type: Changelog
    url: https://developers.tremendous.com/changelog
  - type: JSONSchema
    url: json-schema/tremendous-order-schema.json
  - type: JSONSchema
    url: json-schema/tremendous-product-schema.json
  - type: JSONStructure
    url: json-structure/tremendous-order-structure.json
  - type: JSON-LD
    url: json-ld/tremendous-context.jsonld
  - type: SpectralRules
    url: rules/tremendous-spectral-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/rewards-and-payouts.yaml
  - type: Vocabulary
    url: vocabulary/tremendous-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
