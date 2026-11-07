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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Ecomscout Com Agentic Access
  operation_count: 72
  slug: ecomscout-com-agentic-access
  summary_line: 72 operations · 14 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.ecomscout.com
  baseurl_source: declared
  description: Market rollups for briefing / screening
  name: EcomScout Analytics API
  slug: ecomscout-com-analytics-api
- baseURL: https://api.ecomscout.com
  baseurl_source: declared
  description: Shopify app catalog + install base
  name: EcomScout Apps API
  slug: ecomscout-com-apps-api
- baseURL: https://api.ecomscout.com
  baseurl_source: declared
  description: Segment sizing, compact exports, enrichment, lookalikes, saved audiences. Rows are tiers, not raw metrics; per-store detail stays on /v1/stores/{domain}.
  name: EcomScout Audiences API
  slug: ecomscout-com-audiences-api
- baseURL: https://api.ecomscout.com
  baseurl_source: declared
  description: Observation diffs
  name: EcomScout Changes API
  slug: ecomscout-com-changes-api
- baseURL: https://api.ecomscout.com
  baseurl_source: declared
  description: Docs and health — no API key
  name: EcomScout Discovery API
  slug: ecomscout-com-discovery-api
- baseURL: https://api.ecomscout.com
  baseurl_source: declared
  description: Product ideas, store listings, and price changes
  name: EcomScout Products API
  slug: ecomscout-com-products-api
- baseURL: https://api.ecomscout.com
  baseurl_source: declared
  description: On-demand store scrape — same as Request a store (async + callback)
  name: EcomScout Scrapes API
  slug: ecomscout-com-scrapes-api
- baseURL: https://api.ecomscout.com
  baseurl_source: declared
  description: Your competitor watches — sales, ads, insights (user-scoped)
  name: EcomScout Signals API
  slug: ecomscout-com-signals-api
- baseURL: https://api.ecomscout.com
  baseurl_source: declared
  description: 'Merchant search, profile, compare, contacts. Subresources: traffic, products, apps, history, changes, contacts.'
  name: EcomScout Stores API
  slug: ecomscout-com-stores-api
artifact_total: 24
common:
- group: auth
  title: ''
  type: Security
  url: https://ecomscout.com/security-policy
- group: agent
  href: https://artifacts.apis.io/ecomscout-com/agentic-access/ecomscout-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ecomscout-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/ecomscout-com/plans/ecomscout-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ecomscout-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ecomscout-com/rules/ecomscout-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ecomscout-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ecomscout-com/json-ld/ecomscout-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ecomscout-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ecomscout-com/vocabulary/ecomscout-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ecomscout-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ecomscout-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ecomscout-com/data-model/ecomscout-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ecomscout-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ecomscout-com/errors/ecomscout-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ecomscout-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ecomscout-com/conformance/ecomscout-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ecomscout-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ecomscout-com/llms/ecomscout-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ecomscout-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/ecomscout-com/well-known/ecomscout-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ecomscout-com-security.txt
- group: agent
  href: https://artifacts.apis.io/ecomscout-com/well-known/ecomscout-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ecomscout-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ecomscout-com/hosts/ecomscout-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecomscout-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ecomscout-com/vendors/ecomscout-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ecomscout-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.ecomscout.com/sign-in
- group: auth
  href: https://artifacts.apis.io/ecomscout-com/authentication/ecomscout-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ecomscout-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ecomscout-com/security/ecomscout-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ecomscout-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ecomscout-com/security/ecomscout-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecomscout-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ecomscout.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ecomscout.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.ecomscout.com/v1/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://ecomscout.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ecomscout.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ecomscout.com/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.ecomscout.com/
created: '2026-11-06'
description: EcomScout provides a Shopify store database and analytics platform that tracks competitor revenue, discovers trending products, and offers tools, reports, and an API for e‑commerce intelligence. Founded in 2025, the service aggregates data from over 1 million stores, delivering insights to help merchants outsmart competition and optimize their Shopify stores.
image: https://ecomscout.com/opengraph-image?d2ca908f3e140500
json_schemas:
- name: AudienceDefinition
  property_count: 39
  slug: ecomscout-com-audience-definition
- name: CompetitorStore
  property_count: 17
  slug: ecomscout-com-competitor-store
- name: ProductInventoryProbe
  property_count: 9
  slug: ecomscout-com-product-inventory-probe
- name: StoreInventoryProbe
  property_count: 12
  slug: ecomscout-com-store-inventory-probe
jsonld:
- class_count: 11
  name: Ecomscout Com Context
  property_count: 118
  slug: ecomscout-com-context
layout: provider
modified: '2026-11-06'
name: EcomScout
nav: Providers
network: true
overview: 'EcomScout publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analytics API, Apps API, Audiences API, and 6 more. Tagged areas include Company, Shopify, Analytics, E-Commerce, and Data.


  The EcomScout catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  EcomScout''s developer surface includes authentication, documentation, API reference, pricing, and 22 more developer resources.'
plans:
- name: Ecomscout Com Plans Pricing
  plan_count: 3
  slug: ecomscout-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: EcomScout API Rules
  rule_count: 46
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 5
  slug: ecomscout-com-rules
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 53.5
    developer_ergonomics: 39.9
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ecomscout Com Authentication
  slug: ecomscout-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ecomscout Com Domain Security
  slug: ecomscout-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ecomscout Com Vulnerability Disclosure
  slug: ecomscout-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: ecomscout-com-audience-export-workflow
  slug: ecomscout-com-audience-export-workflow
- name: ecomscout-com-create-and-view-signal-stats
  slug: ecomscout-com-create-and-view-signal-stats
- name: ecomscout-com-queue-and-poll-scrape
  slug: ecomscout-com-queue-and-poll-scrape
- name: ecomscout-com-verify-store-contacts
  slug: ecomscout-com-verify-store-contacts
slug: ecomscout-com
tags:
- Company
- Shopify
- Analytics
- E-Commerce
- Data
website: https://ecomscout.com/
---
