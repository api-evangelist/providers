---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Shopware Agentic Access
  operation_count: 26
  slug: shopware-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 10
apis:
- description: Customer registration, login and profile management
  name: Shopware Account API
  slug: shopware-account-api
- description: High-throughput bulk upsert and delete operations
  name: Shopware Bulk API
  slug: shopware-bulk-api
- description: Manage the shopping cart and its line items
  name: Shopware Cart API
  slug: shopware-cart-api
- description: Manage the product category tree
  name: Shopware Category API
  slug: shopware-category-api
- description: Complete the purchase workflow
  name: Shopware Checkout API
  slug: shopware-checkout-api
- description: Manage customer accounts and addresses
  name: Shopware Customer API
  slug: shopware-customer-api
- description: Fetch storefront navigation menus
  name: Shopware Navigation API
  slug: shopware-navigation-api
- description: Access and manage orders and their line items
  name: Shopware Order API
  slug: shopware-order-api
- description: Create, read, update, and delete products and variants
  name: Shopware Product API
  slug: shopware-product-api
- description: DAL-powered search with filter, sort, and aggregation
  name: Shopware Search API
  slug: shopware-search-api
artifact_total: 26
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shopware-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/shopware-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopware-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopware-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/shopware-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.shopware.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shopware.com/docs/concepts/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopware-ag/
- group: company
  title: ''
  type: Blog
  url: https://www.shopware.com/en/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shopware.com/en/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shopware.com/
- group: other
  title: ''
  type: X
  url: https://x.com/shopwaredevs
- group: commercial
  title: ''
  type: Plans
  url: plans/shopware-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shopware-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shopware-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/shopware-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/shopware-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/shopware-product-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/shopware-cart-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/shopware-order-schema.json
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-12'
description: 'Shopware is an open-source, API-first e-commerce platform built on Symfony and Vue.js, serving mid-market and enterprise merchants across B2C, D2C, and B2B use cases. The platform exposes two primary HTTP APIs: an Admin API for back-office integrations and automation, and a Store API for building headless customer-facing storefronts. Both APIs publish machine-readable OpenAPI 3 specifications directly from each running instance. Shopware is available as a free Community Edition (MIT-licensed), and as paid SaaS and self-hosted tiers (Rise, Evolve, Beyond) unlocking additional commerce capabilities.'
examples:
- key_count: 3
  name: Shopware Add To Cart Example
  slug: shopware-add-to-cart-example
- key_count: 3
  name: Shopware Create Product Example
  slug: shopware-create-product-example
- key_count: 3
  name: Shopware Search Products Example
  slug: shopware-search-products-example
finops:
- name: Shopware Finops
  service_category: E-Commerce Platform
  slug: shopware-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopware.png
json_schemas:
- name: Shopware Cart
  property_count: 11
  slug: shopware-cart
- name: Shopware Order
  property_count: 29
  slug: shopware-order
- name: Shopware Product
  property_count: 29
  slug: shopware-product
jsonld:
- class_count: 9
  name: Shopware Context
  property_count: 54
  slug: shopware-context
layout: provider
modified: '2026-06-12'
name: Shopware
nav: Providers
network: true
overview: 'Shopware publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Bulk API, Cart API, and 7 more. Tagged areas include E-Commerce, Open Source, Headless Commerce, B2B, and B2C.


  The Shopware catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shopware''s developer surface includes authentication, documentation, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Shopware Plans Pricing
  plan_count: 5
  slug: shopware-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Shopware Rate Limits
  slug: shopware-rate-limits
rules:
- name: Shopware API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: shopware-jsonschema-spectral-rules
scopes:
- name: Shopware Scopes
  scope_count: 1
  slug: shopware-scopes
  summary_line: 1 scope · clientCredentials/password
score:
  band: developing
  composite: 53.2
  delta: -5.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 65.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/shopware/refs/heads/main/screenshots/shopware-2026-06-20T193839.png
security:
- kind: authentication
  name: Shopware Authentication
  slug: shopware-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Shopware Domain Security
  slug: shopware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shopware Vulnerability Disclosure
  slug: shopware-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: shopware
tags:
- E-Commerce
- Open Source
- Headless Commerce
- B2B
- B2C
- REST
- OAuth2
website: https://www.shopware.com
---
