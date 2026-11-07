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
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wisepim Agentic Access
  operation_count: 10
  slug: wisepim-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: https://wisepim.com/api/open/v1
  baseurl_source: declared
  description: Barcode validation and GS1 prefix lookup.
  name: WISEPIM Open Data API GTIN API
  slug: wisepim-gtin-api
- baseURL: https://wisepim.com/api/open/v1
  baseurl_source: declared
  description: EU Combined Nomenclature and US HTS customs tariff codes.
  name: WISEPIM Open Data API HS codes API
  slug: wisepim-hs-codes-api
- baseURL: https://wisepim.com/api/open/v1
  baseurl_source: declared
  description: Sourced seller fees of European marketplaces.
  name: WISEPIM Open Data API Marketplace fees API
  slug: wisepim-marketplace-fees-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/wisepim/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/wisepim/agentic-access/wisepim-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wisepim-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/wisepim/plans/wisepim-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wisepim-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wisepim/rules/wisepim-rules.yml
  title: ''
  type: Spectral
  url: rules/wisepim-rules.yml
- group: design
  href: https://artifacts.apis.io/wisepim/json-ld/wisepim-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wisepim-context.jsonld
- group: design
  href: https://artifacts.apis.io/wisepim/vocabulary/wisepim-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wisepim-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wisepim/data-model/wisepim-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wisepim-data-model.yml
- group: design
  href: https://artifacts.apis.io/wisepim/conventions/wisepim-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wisepim-conventions.yml
- group: auth
  href: https://artifacts.apis.io/wisepim/authentication/wisepim-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wisepim-authentication.yml
- group: design
  href: https://artifacts.apis.io/wisepim/errors/wisepim-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wisepim-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wisepim/conformance/wisepim-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wisepim-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wisepim/llms/wisepim-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wisepim-llms.txt
- group: other
  href: https://artifacts.apis.io/wisepim/a2a/wisepim-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/wisepim-a2a.yml
- group: agent
  href: https://artifacts.apis.io/wisepim/well-known/wisepim-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wisepim-well-known.yml
- group: other
  href: https://artifacts.apis.io/wisepim/hosts/wisepim-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wisepim-hosts.yml
- group: other
  href: https://artifacts.apis.io/wisepim/vendors/wisepim-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wisepim-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wisepim.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wisepim.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://wisepim.com/pricing
- group: start
  title: ''
  type: Login
  url: https://wisepim.com/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://wisepim.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://wisepim.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://wisepim.com/developers/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wisepim.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/wisepim/security/wisepim-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wisepim-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wisepim.com
- group: docs
  title: ''
  type: Documentation
  url: https://wisepim.com/developers/open-data
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://wisepim.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: WISEPIM provides AI‑powered product information management for e‑commerce brands. It enriches, translates and validates product data, then syncs it across channels such as Shopify, Magento, WooCommerce and marketplaces. Free plan up to 100 products, with paid tiers offering advanced automation, bulk editing and multi‑language support. The platform includes a REST API for custom integrations, a no‑code automation builder, and AI‑driven content generation.
image: https://wisepim.com/wisepim-og-image.jpg
json_schemas:
- name: FeeCalculation
  property_count: 14
  slug: wisepim-fee-calculation
- name: FeeComparison
  property_count: 7
  slug: wisepim-fee-comparison
- name: FeeIndex
  property_count: 6
  slug: wisepim-fee-index
- name: GtinResult
  property_count: 9
  slug: wisepim-gtin-result
- name: HsBrowse
  property_count: 6
  slug: wisepim-hs-browse
- name: HsSearch
  property_count: 6
  slug: wisepim-hs-search
jsonld:
- class_count: 14
  name: Wisepim Context
  property_count: 67
  slug: wisepim-context
layout: provider
modified: '2026-11-03'
name: WISEPIM Open Data API
nav: Providers
network: true
overview: 'WISEPIM Open Data API publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: GTIN API, HS codes API, and Marketplace fees API. Tagged areas include Product Information Management, Artificial Intelligence, E-Commerce, Catalog Enrichment, and Translation.


  The WISEPIM Open Data API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  WISEPIM Open Data API''s developer surface includes authentication, pricing, changelog, engineering blog, getting-started guide, API reference, documentation, and 20 more developer resources.'
plans:
- name: Wisepim Plans Pricing
  plan_count: 7
  slug: wisepim-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: WISEPIM Open Data API API Rules
  rule_count: 50
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 2
  slug: wisepim-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 60.1
    developer_ergonomics: 33.8
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Wisepim Authentication
  slug: wisepim-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Wisepim Domain Security
  slug: wisepim-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wisepim
tags:
- Product Information Management
- Artificial Intelligence
- E-Commerce
- Catalog Enrichment
- Translation
- Wholesale
- Retail
website: https://wisepim.com
---
