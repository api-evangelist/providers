---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Barcodes Gg Agentic Access
  operation_count: 19
  slug: barcodes-gg-agentic-access
  summary_line: 19 operations
api_count: 1
apis:
- baseURL: https://barcodes.gg/api
  baseurl_source: declared
  description: Usage of the calling token.
  name: Barcodes.GG Account API
  slug: barcodes-gg-account-api
- baseURL: https://barcodes.gg/api
  baseurl_source: declared
  description: Barcode to product, and style code to barcodes (v2).
  name: Barcodes.GG Barcodes API
  slug: barcodes-gg-barcodes-api
- baseURL: https://barcodes.gg/api
  baseurl_source: declared
  description: Product images. No token needed.
  name: Barcodes.GG Images API
  slug: barcodes-gg-images-api
- baseURL: https://barcodes.gg/api
  baseurl_source: declared
  description: Unversioned v1 endpoints that remain available. They do not add the v2 response metadata to error responses.
  name: Barcodes.GG Legacy v1 API
  slug: barcodes-gg-legacy-v1-api
- baseURL: https://barcodes.gg/api
  baseurl_source: declared
  description: Product search, lookup, details and release lists (v2).
  name: Barcodes.GG Products API
  slug: barcodes-gg-products-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/barcodes-gg/agentic-access/barcodes-gg-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/barcodes-gg-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/barcodes-gg/plans/barcodes-gg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/barcodes-gg-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/barcodes-gg/rules/barcodes-gg-rules.yml
  title: ''
  type: Spectral
  url: rules/barcodes-gg-rules.yml
- group: design
  href: https://artifacts.apis.io/barcodes-gg/json-ld/barcodes-gg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/barcodes-gg-context.jsonld
- group: design
  href: https://artifacts.apis.io/barcodes-gg/vocabulary/barcodes-gg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/barcodes-gg-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/barcodes-gg/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/barcodes-gg/data-model/barcodes-gg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/barcodes-gg-data-model.yml
- group: auth
  href: https://artifacts.apis.io/barcodes-gg/authentication/barcodes-gg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/barcodes-gg-authentication.yml
- group: design
  href: https://artifacts.apis.io/barcodes-gg/errors/barcodes-gg-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/barcodes-gg-problem-types.yml
- group: design
  href: https://artifacts.apis.io/barcodes-gg/conformance/barcodes-gg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/barcodes-gg-conformance.yml
- group: agent
  href: https://artifacts.apis.io/barcodes-gg/llms/barcodes-gg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/barcodes-gg-llms.txt
- group: other
  href: https://artifacts.apis.io/barcodes-gg/hosts/barcodes-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/barcodes-gg-hosts.yml
- group: build
  href: https://artifacts.apis.io/barcodes-gg/packages/barcodes-gg-packages.yml
  title: ''
  type: SDKs
  url: packages/barcodes-gg-packages.yml
- group: build
  href: https://artifacts.apis.io/barcodes-gg/packages/barcodes-gg-packages.yml
  title: ''
  type: Packages
  url: packages/barcodes-gg-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://barcodes.gg/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://barcodes.gg/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://barcodes.gg/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://barcodes.gg/auth/login
- group: company
  title: ''
  type: Blog
  url: https://barcodes.gg/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://barcodes.gg/blog/getting-started-barcodes-gg-api
- group: docs
  title: ''
  type: APIReference
  url: https://barcodes.gg/llms.txt
- group: auth
  href: https://artifacts.apis.io/barcodes-gg/security/barcodes-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/barcodes-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://barcodes.gg/barcode-lookup-api
- group: docs
  title: ''
  type: Documentation
  url: https://barcodes.gg/guide/docs/introduction
created: '2026-10-21'
description: Barcodes.GG provides a sneaker and streetwear barcode lookup API that translates UPC, EAN, or style codes into detailed product information such as model, colorway, size, release date, retail price, and images. The service powers developers and retailers with access to over 3 million barcodes covering more than 1.5 million products. Plans start at €19 per month with a free trial, and the API is designed for production use, offering clean, normalized data through simple GET requests.
image: https://barcodes.gg/og/pages/barcode-lookup-api.png?v=7d6ad42c84d3
json_schemas:
- name: Barcode
  property_count: 4
  slug: barcodes-gg-barcode
- name: Error
  property_count: 5
  slug: barcodes-gg-error
- name: ProductDetails
  property_count: 30
  slug: barcodes-gg-product-details
- name: Product
  property_count: 18
  slug: barcodes-gg-product
- name: SkuBarcode
  property_count: 4
  slug: barcodes-gg-sku-barcode
- name: Usage
  property_count: 5
  slug: barcodes-gg-usage
jsonld:
- class_count: 11
  name: Barcodes Gg Context
  property_count: 76
  slug: barcodes-gg-context
layout: provider
modified: '2026-10-21'
name: Barcodes.GG
nav: Providers
network: true
overview: 'Barcodes.GG publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Barcodes API, Images API, and 2 more. Tagged areas include Company, Barcodes, Sneaker, and Streetwear.


  The Barcodes.GG catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Barcodes.GG''s developer surface includes authentication, support, engineering blog, getting-started guide, API reference, documentation, and 18 more developer resources.'
plans:
- name: Barcodes Gg Plans Pricing
  plan_count: 8
  slug: barcodes-gg-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: Barcodes.GG API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: barcodes-gg-rules
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 68.6
    developer_ergonomics: 38.7
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/barcodes-gg/barcodes-gg-2026-11-03T121541.png
security:
- kind: authentication
  name: Barcodes Gg Authentication
  slug: barcodes-gg-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Barcodes Gg Domain Security
  slug: barcodes-gg-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: barcodes-gg-search-and-detail
  slug: barcodes-gg-search-and-detail
slug: barcodes-gg
tags:
- Company
- Barcodes
- Sneaker
- Streetwear
website: https://barcodes.gg/barcode-lookup-api
---
