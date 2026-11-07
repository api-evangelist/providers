---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Carbonguru Io Agentic Access
  operation_count: 61
  slug: carbonguru-io-agentic-access
  summary_line: 61 operations · 23 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Carbon footprint analysis, history and reference data for a developer's own server.
  name: CarbonGuru API
  slug: carbonguru-api
- baseURL: https://carbonguru.io
  baseurl_source: declared
  description: Submit an analysis and read its session.
  name: CarbonGuru Analysis API
  slug: carbonguru-io-analysis-api
- baseURL: https://carbonguru.io
  baseurl_source: declared
  description: Past analyses, footprints and account usage.
  name: CarbonGuru History API
  slug: carbonguru-io-history-api
- baseURL: https://carbonguru.io
  baseurl_source: declared
  description: The Offsets API from CarbonGuru — 13 operation(s) for offsets.
  name: CarbonGuru Offsets API
  slug: carbonguru-io-offsets-api
- baseURL: https://carbonguru.io
  baseurl_source: declared
  description: NAICS, industry sectors, emission factors, countries.
  name: CarbonGuru Reference API
  slug: carbonguru-io-reference-api
- baseURL: https://carbonguru.io
  baseurl_source: declared
  description: Health and the API contract.
  name: CarbonGuru Service API
  slug: carbonguru-io-service-api
- baseURL: https://carbonguru.io
  baseurl_source: declared
  description: The Store API from CarbonGuru — 17 operation(s) for store.
  name: CarbonGuru Store API
  slug: carbonguru-io-store-api
- baseURL: https://carbonguru.io
  baseurl_source: declared
  description: Endpoint registrations and the per-attempt delivery log.
  name: CarbonGuru Webhooks API
  slug: carbonguru-io-webhooks-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/carbonguru-io/agentic-access/carbonguru-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/carbonguru-io-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/carbonguru-io/plans/carbonguru-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carbonguru-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/carbonguru-io/rules/carbonguru-io-rules.yml
  title: ''
  type: Spectral
  url: rules/carbonguru-io-rules.yml
- group: design
  href: https://artifacts.apis.io/carbonguru-io/json-ld/carbonguru-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/carbonguru-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/carbonguru-io/vocabulary/carbonguru-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/carbonguru-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/carbonguru-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/carbonguru-io/data-model/carbonguru-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/carbonguru-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/carbonguru-io/conventions/carbonguru-io-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/carbonguru-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/carbonguru-io/conventions/carbonguru-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/carbonguru-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/carbonguru-io/authentication/carbonguru-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/carbonguru-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/carbonguru-io/errors/carbonguru-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/carbonguru-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/carbonguru-io/conformance/carbonguru-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carbonguru-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carbonguru-io/well-known/carbonguru-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carbonguru-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/carbonguru-io/hosts/carbonguru-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbonguru-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carbonguru.io/terms/
- group: operate
  title: ''
  type: Support
  url: https://carbonguru.io/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carbonguru.io/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://carbonguru.io/plans/
- group: company
  title: ''
  type: Blog
  url: https://carbonguru.io/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.carbonguru.io/onboarding/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.carbonguru.io/
- group: auth
  href: https://artifacts.apis.io/carbonguru-io/security/carbonguru-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbonguru-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbonguru.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://carbonguru.io/v1/openapi.json
  - status: null
    url: https://dev.carbonguru.io/v1/openapi.json
  - status: 401
    url: https://carbonguru.io/mcp
  - status: 401
    url: https://dev.carbonguru.io/mcp
  - status: 200
    url: https://carbonguru.io/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: CarbonGuru provides merchants with embedded carbon‑footprint data and automated climate‑offsetting for every product sold in online stores, catalogs, or marketplaces. The service works for both B2C and B2B sellers and integrates with platforms such as WooCommerce, Shopify, Stripe, PayPal, BigCommerce, Wix and Squarespace, allowing customers to see footprints without additional charges while the seller offsets the impact automatically.
image: https://carbonguru.io/app/themes/carbonguru-theme-v2/assets/images/og/home-card.png
jsonld:
- class_count: 21
  name: Carbonguru Io Context
  property_count: 183
  slug: carbonguru-io-context
layout: provider
modified: '2026-11-03'
name: CarbonGuru
nav: Providers
network: true
overview: 'CarbonGuru publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analysis API, History API, Offsets API, and 5 more. Tagged areas include Carbon Footprinting, Automated Offsetting, E-Commerce, Marketplace, and B2B.


  The CarbonGuru catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CarbonGuru''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Carbonguru Io Plans Pricing
  plan_count: 5
  slug: carbonguru-io-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: CarbonGuru API Rules
  rule_count: 62
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 9
  slug: carbonguru-io-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 58.1
    developer_ergonomics: 28.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Carbonguru Io Authentication
  slug: carbonguru-io-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Carbonguru Io Domain Security
  slug: carbonguru-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: carbonguru-io-activate-store-product
  slug: carbonguru-io-activate-store-product
- name: carbonguru-io-buy-offsets
  slug: carbonguru-io-buy-offsets
- name: carbonguru-io-manage-webhook-endpoints
  slug: carbonguru-io-manage-webhook-endpoints
- name: carbonguru-io-run-analysis-workflow
  slug: carbonguru-io-run-analysis-workflow
slug: carbonguru-io
tags:
- Carbon Footprinting
- Automated Offsetting
- E-Commerce
- Marketplace
- B2B
- Consumer
- Sustainability
website: https://carbonguru.io/
---
