---
aid: state-farm-insurance
url: https://raw.githubusercontent.com/api-evangelist/state-farm-insurance/refs/heads/main/apis.yml
modified: '2026-05-02'
name: State Farm Insurance
description: State Farm Insurance refers to the primary insurance operations of State Farm Mutual Automobile Insurance Company and its affiliated entities, headquartered in Bloomington, Illinois. As the largest property and casualty insurer in the United States, State Farm Insurance provides auto, home, renters, life, health, commercial, and farm insurance products to over 83 million policies across 91 million accounts. The company operates through approximately 19,000 exclusive agents and has a robust digital platform. State Farm Insurance maintains a Partner Gateway developer portal (developer.statefarm.com) offering APIs for embedded insurance, partner integrations, and B2B connectivity. The company has also heavily invested in cloud infrastructure on AWS and has open-sourced numerous DevOps and infrastructure tools via its GitHub organization.
apis:
  - aid: state-farm-insurance:renters-insurance-api
    name: Renters Insurance API
    description: The State Farm Renters Insurance API allows property management companies, real estate platforms, and partner aggregators to embed renters insurance quoting and policy issuance directly into their workflows. Renters can receive a customized State Farm quote without leaving the partner application. State Farm is the top-ranked renters insurance provider in the United States. The API supports quote requests, coverage selection, policy binding, and policy status retrieval.
    humanURL: https://developer.statefarm.com/api/renters
    baseURL: https://api.statefarm.com/v1
    tags:
      - Insurance
      - Renters Insurance
      - Embedded Insurance
      - Property
      - Partner
    properties:
      - type: Documentation
        url: https://developer.statefarm.com/api/renters
      - type: OpenAPI
        url: openapi/state-farm-insurance-renters-openapi.yml
  - aid: state-farm-insurance:auto-insurance-api
    name: Auto Insurance API
    description: The State Farm Auto Insurance API enables partners in automotive, telematics, and financial services to embed State Farm auto insurance products into their platforms. Use cases include in-dealership insurance quoting at point of sale, connected car insurance integrations, and lender-required coverage verification. State Farm is the largest auto insurer in the US with over 40 million auto policies. The API supports quote generation, coverage retrieval, and policy status inquiries.
    humanURL: https://developer.statefarm.com/
    baseURL: https://api.statefarm.com/v1
    tags:
      - Insurance
      - Auto Insurance
      - Vehicles
      - Telematics
      - Partner
    properties:
      - type: Documentation
        url: https://developer.statefarm.com/
  - aid: state-farm-insurance:homeowners-insurance-api
    name: Homeowners Insurance API
    description: The State Farm Homeowners Insurance API enables mortgage lenders, real estate platforms, and partner networks to offer homeowners insurance quoting and policy integration. Supports closing day insurance coordination, escrow verification, and coverage inquiry for lenders requiring collateral protection evidence. State Farm is one of the largest homeowners insurance providers in the US.
    humanURL: https://developer.statefarm.com/
    baseURL: https://api.statefarm.com/v1
    tags:
      - Insurance
      - Homeowners Insurance
      - Mortgage
      - Real Estate
      - Partner
    properties:
      - type: Documentation
        url: https://developer.statefarm.com/
  - aid: state-farm-insurance:b2b-insurance-inquiry-api
    name: B2B Insurance Inquiry API
    description: The State Farm B2B Insurance Inquiry API provides home and auto lenders with a programmatic way to verify that borrowers maintain adequate insurance coverage on financed properties and vehicles. Lenders can query active policy status, coverage amounts, and expiration dates. This supports regulatory compliance requirements for collateral insurance verification and helps lenders reduce force-placed insurance costs.
    humanURL: https://b2b.statefarm.com/b2b-content/home-auto-lenders/ins-inquiry
    baseURL: https://b2b.statefarm.com/api/v1
    tags:
      - Insurance
      - B2B
      - Lenders
      - Verification
      - Compliance
    properties:
      - type: Documentation
        url: https://b2b.statefarm.com/b2b-content/home-auto-lenders/ins-inquiry
common:
  - type: Website
    url: https://www.statefarm.com
  - type: Developer Portal
    url: https://developer.statefarm.com
  - type: GitHub
    url: https://github.com/StateFarmIns
  - type: Engineering Blog
    url: https://engineering.statefarm.com/blog
  - type: B2B Portal
    url: https://b2b.statefarm.com
  - type: LinkedIn
    url: https://www.linkedin.com/company/state-farm
  - type: Twitter
    url: https://twitter.com/StateFarm
  - type: Newsroom
    url: https://newsroom.statefarm.com
  - type: Privacy Policy
    url: https://www.statefarm.com/customer-care/privacy-security/privacy/privacy-policy
  - type: Terms of Service
    url: https://www.statefarm.com/customer-care/legal-disclaimer
  - type: OpenAPI
    url: openapi/state-farm-insurance-renters-openapi.yml
  - type: JSONSchema
    url: json-schema/state-farm-insurance-renters-policy-schema.json
  - type: JSONStructure
    url: json-structure/state-farm-insurance-renters-policy-structure.json
  - type: JSONLD
    url: json-ld/state-farm-insurance-context.jsonld
  - type: Vocabulary
    url: vocabulary/state-farm-insurance-vocabulary.yml
  - type: SpectralRules
    url: rules/state-farm-insurance-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/embedded-insurance.yaml
---
