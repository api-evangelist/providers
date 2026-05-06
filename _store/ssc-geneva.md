---
aid: ssc-geneva
name: SS&C Geneva
description: SS&C Geneva is an enterprise-grade fund accounting and portfolio management platform for asset managers, hedge funds, and fund administrators. Geneva provides APIs for NAV calculation, trade processing, investor accounting, position management, and regulatory reporting across multi-asset portfolios including equities, fixed income, derivatives, and alternative investments.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Fund Accounting
  - Asset Management
  - Portfolio Management
  - Financial Services
  - Hedge Funds
  - NAV Calculation
url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/apis.yml
created: '2026-03-18'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: ssc-geneva:ssc-geneva-fund-accounting
    name: SS&C Geneva Fund Accounting API
    description: SS&C Geneva provides fund accounting and portfolio management APIs for asset managers, hedge funds, and fund administrators. APIs enable NAV calculation, trade processing, investor accounting, position management, and regulatory reporting across multi-asset portfolios. Geneva is an enterprise system with REST APIs for integration with external systems including OMS, custodians, and reporting platforms.
    humanURL: https://www.ssctech.com/
    baseURL: https://api.ssctech.example.com/geneva/v1
    tags:
      - Fund Accounting
      - Portfolio Management
      - Asset Management
      - Financial Services
      - NAV Calculation
      - Trade Processing
    properties:
      - type: Documentation
        url: https://www.ssctech.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/openapi/ssc-geneva-fund-accounting-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/json-schema/ssc-geneva-portfolio-schema.json
    contact:
      - FN: SS&C Technologies Support
        url: https://www.ssctech.com/about/support-client-portals
common:
  - type: Website
    url: https://www.ssctech.com/
  - type: Portal
    url: https://www.ssctech.com/products
  - type: Blog
    url: https://www.ssctech.com/blog
  - type: Support
    url: https://www.ssctech.com/about/support-client-portals
  - type: PrivacyPolicy
    url: https://www.ssctech.com/about/privacy
  - type: Documentation
    url: https://www.ssctech.com/resources
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/openapi/ssc-geneva-fund-accounting-openapi.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/json-schema/ssc-geneva-portfolio-schema.json
  - type: JSONStructure
    url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/json-structure/ssc-geneva-fund-structure.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/json-ld/ssc-geneva-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/rules/ssc-geneva-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/capabilities/fund-operations.yaml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/ssc-geneva/refs/heads/main/vocabulary/ssc-geneva-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
