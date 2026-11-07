---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Vendure Agentic Access
  operation_count: 4
  slug: vendure-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 3
apis:
- baseURL: http://localhost:3000/shop-api
  baseurl_source: declared
  description: The Assets API from Vendure — 2 operation(s) for assets.
  name: Vendure Assets API
  slug: vendure-assets-api
- baseURL: http://localhost:3000/shop-api
  baseurl_source: declared
  description: The Vendure Admin API API from Vendure — 1 operation(s) for vendure admin api.
  name: Vendure Admin API
  slug: vendure-vendure-admin-api-api
artifact_total: 26
collections:
- collection_type: open
  name: Vendure Admin API
  slug: open-vendure-admin-api
- collection_type: open
  name: Vendure Asset Server API
  slug: open-vendure-asset-server
- collection_type: open
  name: Vendure Admin Assets API
  slug: open-vendure-assets-api
- collection_type: open
  name: Vendure Shop API
  slug: open-vendure-shop-api
- collection_type: open
  name: Vendure Admin Assets Vendure Admin API API
  slug: open-vendure-vendure-admin-api-api
- collection_type: open
  name: Vendure Admin Assets Vendure Shop API API
  slug: open-vendure-vendure-shop-api-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/vendurehq/vendure/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/vendurehq/vendure/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/vendurehq/vendure/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/vendurehq/vendure/blob/master/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/vendurehq/vendure/blob/master/CONTRIBUTING.md
- group: agent
  href: https://artifacts.apis.io/vendure/agentic-access/vendure-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vendure-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/vendure/security/vendure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vendure-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/vendure/authentication/vendure-authentication.yml
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
  href: https://artifacts.apis.io/vendure/plans/vendure-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vendure-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/vendure/rate-limits/vendure-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vendure-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/vendure/finops/vendure-finops.yml
  title: ''
  type: FinOps
  url: finops/vendure-finops.yml
- group: design
  href: https://artifacts.apis.io/vendure/json-ld/vendure-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vendure-context.jsonld
- group: design
  href: https://artifacts.apis.io/vendure/vocabulary/vendure-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vendure-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/vendure/rules/vendure-rules.yml
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
- has_sources: false
  method: generated
  name: Vendure Finops
  primary_unit: ''
  service_category: Software
  slug: vendure-finops
  template: true
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
modified: '2026-09-16'
name: Vendure
nav: Providers
network: true
overview: 'Vendure publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Assets API and Admin API. Tagged areas include Commerce, Headless Commerce, E-Commerce, GraphQL, and Open Source.


  The Vendure catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vendure''s developer surface includes authentication, documentation, GitHub presence, pricing, engineering blog, and 22 more developer resources.'
plans:
- name: Vendure Plans Pricing
  plan_count: 3
  slug: vendure-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Vendure Rate Limits
  slug: vendure-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Vendure — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: vendure-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Vendure API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: vendure-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 27.3
    contract_quality: 57.2
    developer_ergonomics: 23.8
    discoverability: 71.7
    operational_transparency: 31.6
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/vendure/vendure-2026-06-20T200911.png
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
- E-Commerce
- GraphQL
- Open Source
- TypeScript
- NestJS
- B2B
- Consumer
- Storefront
- Plugins
website: https://vendure.io/
---
