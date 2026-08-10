---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Vendure Agentic Access
  operation_count: 4
  slug: vendure-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- description: The Assets API from Vendure — 2 operation(s) for assets.
  name: Vendure Assets API
  slug: vendure-assets-api
- description: The Vendure Admin API API from Vendure — 1 operation(s) for vendure admin api.
  name: Vendure Vendure Admin API API
  slug: vendure-vendure-admin-api-api
- description: The Vendure Shop API API from Vendure — 1 operation(s) for vendure shop api.
  name: Vendure Vendure Shop API API
  slug: vendure-vendure-shop-api-api
artifact_total: 24
collections:
- collection_type: open
  name: Vendure Admin API
  slug: open-vendure-admin-api
- collection_type: open
  name: Vendure Asset Server API
  slug: open-vendure-asset-server
- collection_type: open
  name: Vendure Shop API
  slug: open-vendure-shop-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vendure-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vendure-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vendure-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vendure.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vendure.io/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/vendurehq
- group: other
  title: ''
  type: Repository
  url: https://github.com/vendurehq/vendure
- group: other
  title: ''
  type: Platform
  url: https://vendure.io/platform
- group: other
  title: ''
  type: Cloud
  url: https://vendure.io/cloud
- group: commercial
  title: ''
  type: Pricing
  url: https://vendure.io/pricing
- group: other
  title: ''
  type: Hub
  url: https://vendure.io/hub
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vendure
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.vendure.io/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vendure.io/mcp
- group: commercial
  title: ''
  type: License
  url: https://github.com/vendurehq/vendure/blob/master/LICENSE
- group: commercial
  title: ''
  type: Plans
  url: plans/vendure-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vendure-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vendure-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vendure-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vendure-vocabulary.yml
- group: design
  title: ''
  type: Rules
  url: rules/vendure-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://www.vendure.io/blog
created: '2026-05-23'
description: Vendure is an open-source headless commerce framework built in TypeScript on top of NestJS, GraphQL, and TypeORM. A Vendure server exposes two GraphQL APIs — the Shop API (consumed by storefronts) and the Admin API (consumed by the Dashboard and back-office tooling) — plus an Asset Server REST surface for uploads and image previews, and a plugin system that extends data, services, jobs, and resolvers. The project is GPLv3-licensed Vendure Core, complemented by a commercial Vendure Platform layer of 20+ enterprise plugins, a managed Vendure Cloud offering, an official MCP server, and a starter ecosystem (Next.js, Remix, Qwik, SvelteKit, Angular, Gatsby).
examples:
- key_count: 3
  name: Vendure Admin Create Product Example
  slug: vendure-admin-create-product-example
- key_count: 3
  name: Vendure Asset Preview Example
  slug: vendure-asset-preview-example
- key_count: 3
  name: Vendure Shop Active Order Example
  slug: vendure-shop-active-order-example
- key_count: 3
  name: Vendure Shop Add Item Example
  slug: vendure-shop-add-item-example
- key_count: 3
  name: Vendure Shop Search Example
  slug: vendure-shop-search-example
finops:
- name: Vendure Finops
  service_category: Software
  slug: vendure-finops
graphqls:
- description: Public GraphQL API consumed by storefronts and end-customer clients — product and collection browse, faceted search, active order / cart, checkout, eligible shipping and payment methods, customer regi
  name: Vendure GraphQL API
  slug: vendure-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vendure.png
json_schemas:
- name: Vendure Customer
  property_count: 13
  slug: vendure-customer
- name: Vendure Order
  property_count: 26
  slug: vendure-order
- name: Vendure Product
  property_count: 16
  slug: vendure-product
jsonld:
- class_count: 47
  name: Vendure Context
  property_count: 7
  slug: vendure-context
layout: provider
modified: '2026-05-25'
name: Vendure
nav: Providers
network: true
overview: 'Vendure publishes 3 APIs on the [APIs.io](https://apis.io/) network: Assets API, Vendure Admin API API, and Vendure Shop API API. Tagged areas include Commerce, Headless Commerce, eCommerce, GraphQL, and Open Source.


  The Vendure catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vendure''s developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Vendure Plans Pricing
  plan_count: 3
  slug: vendure-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 0
  name: Vendure Rate Limits
  slug: vendure-rate-limits
rules:
- name: Vendure API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: vendure-jsonschema-spectral-rules
- name: Vendure API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: vendure-rules
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 74.9
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 5.3
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vendure/refs/heads/main/screenshots/vendure-2026-06-20T200911.png
security:
- kind: authentication
  name: Vendure Authentication
  slug: vendure-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Vendure Domain Security
  slug: vendure-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vendure
tags:
- Commerce
- Headless Commerce
- eCommerce
- GraphQL
- Open Source
- TypeScript
- NestJS
- B2B
- B2C
- Storefront
- Plugins
website: https://vendure.io/
---
