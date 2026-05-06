---
aid: tropic
name: Tropic
description: Tropic is an intelligent procurement platform that combines AI-powered spend management, supplier management, and benchmark data to help organizations find and capture savings opportunities. Tropic's AI agents track renewals, spot shadow spend, flag compliance issues, and automate manual procurement tasks with SKU-level price benchmarks from thousands of actual deals.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Benchmarking
  - Contract Management
  - Cost Optimization
  - Procurement
  - Renewals
  - SaaS Management
  - SaaS Procurement
  - Spend Management
  - Supplier Management
url: https://raw.githubusercontent.com/api-evangelist/tropic/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tropic:rest-api
    name: Tropic API
    description: The Tropic public REST API enables organizations to connect Tropic with other software in their stack. It supports managing contracts, suppliers, procurement requests, webhook subscriptions, and users programmatically. Authentication uses API keys via Bearer tokens issued from the Tropic settings panel.
    humanURL: https://help.tropicapp.io/hc/en-us/sections/31190632406171-API-and-Webhooks
    baseURL: https://api.tropicapp.io/v1
    tags:
      - Contract Management
      - Integrations
      - Procurement
      - Spend Management
      - Supplier Management
      - Webhooks
    properties:
      - url: https://help.tropicapp.io/hc/en-us/sections/31190632406171-API-and-Webhooks
        type: Documentation
      - url: https://raw.githubusercontent.com/api-evangelist/tropic/refs/heads/main/openapi/tropic-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/tropic/refs/heads/main/rules/tropic-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/tropic/refs/heads/main/capabilities/procurement-management.yaml
        type: NaftikoCapabilities
      - url: https://raw.githubusercontent.com/api-evangelist/tropic/refs/heads/main/json-schema/tropic-contract-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/tropic/refs/heads/main/json-schema/tropic-supplier-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/tropic/refs/heads/main/json-ld/tropic-context.jsonld
        type: JSONLDContext
      - url: https://raw.githubusercontent.com/api-evangelist/tropic/refs/heads/main/vocabulary/tropic-vocabulary.yml
        type: Vocabulary
common:
  - type: Website
    url: https://www.tropicapp.io/
  - type: Documentation
    url: https://help.tropicapp.io/hc/en-us
  - type: Blog
    url: https://www.tropicapp.io/blog
  - type: Login
    url: https://app.tropicapp.io/portal/login
  - type: Integrations
    url: https://www.tropicapp.io/solutions/integrations
  - type: Pricing
    url: https://www.tropicapp.io/pricing
  - type: LinkedIn
    url: https://www.linkedin.com/company/tropicapp
  - type: Twitter
    url: https://x.com/tropicapp
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
