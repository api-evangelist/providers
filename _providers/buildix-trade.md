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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Buildix Trade Agentic Access
  operation_count: 6
  slug: buildix-trade-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://www.buildix.trade/api/v1
  baseurl_source: declared
  description: The Deep View API from Buildix — 1 operation(s) for deep view.
  name: Buildix Deep View API
  slug: buildix-trade-deep-view-api
- baseURL: https://www.buildix.trade/api/v1
  baseurl_source: declared
  description: The Funding Arb API from Buildix — 1 operation(s) for funding arb.
  name: Buildix Funding Arb API
  slug: buildix-trade-funding-arb-api
- baseURL: https://www.buildix.trade/api/v1
  baseurl_source: declared
  description: The Pair API from Buildix — 1 operation(s) for pair.
  name: Buildix Pair API
  slug: buildix-trade-pair-api
- baseURL: https://www.buildix.trade/api/v1
  baseurl_source: declared
  description: The Screener API from Buildix — 1 operation(s) for screener.
  name: Buildix Screener API
  slug: buildix-trade-screener-api
- baseURL: https://www.buildix.trade/api/v1
  baseurl_source: declared
  description: The Signals API from Buildix — 1 operation(s) for signals.
  name: Buildix Signals API
  slug: buildix-trade-signals-api
- baseURL: https://www.buildix.trade/api/v1
  baseurl_source: declared
  description: The Smart Money API from Buildix — 1 operation(s) for smart money.
  name: Buildix Smart Money API
  slug: buildix-trade-smart-money-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/buildix-trade/agentic-access/buildix-trade-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/buildix-trade-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/buildix-trade/plans/buildix-trade-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildix-trade-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buildix-trade/rules/buildix-trade-rules.yml
  title: ''
  type: Spectral
  url: rules/buildix-trade-rules.yml
- group: design
  href: https://artifacts.apis.io/buildix-trade/json-ld/buildix-trade-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/buildix-trade-context.jsonld
- group: design
  href: https://artifacts.apis.io/buildix-trade/vocabulary/buildix-trade-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/buildix-trade-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/buildix-trade/data-model/buildix-trade-data-model.yml
  title: ''
  type: DataModel
  url: data-model/buildix-trade-data-model.yml
- group: design
  href: https://artifacts.apis.io/buildix-trade/conventions/buildix-trade-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/buildix-trade-conventions.yml
- group: design
  href: https://artifacts.apis.io/buildix-trade/conventions/buildix-trade-conventions.yml
  title: ''
  type: Conventions
  url: conventions/buildix-trade-conventions.yml
- group: design
  href: https://artifacts.apis.io/buildix-trade/conformance/buildix-trade-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildix-trade-conformance.yml
- group: other
  href: https://artifacts.apis.io/buildix-trade/hosts/buildix-trade-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildix-trade-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildix-trade/vendors/buildix-trade-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildix-trade-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buildix.trade/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buildix.trade/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buildix.trade/pricing
- group: start
  title: ''
  type: Login
  url: https://www.buildix.trade/auth/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.buildix.trade/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.buildix.trade/developers
- group: company
  title: ''
  type: Blog
  url: https://www.buildix.trade/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.buildix.trade/blog/hyperliquid-hype-unlock-july-6-660m-orderflow-setup
- group: auth
  href: https://artifacts.apis.io/buildix-trade/authentication/buildix-trade-authentication.yml
  title: ''
  type: Authentication
  url: authentication/buildix-trade-authentication.yml
- group: auth
  href: https://artifacts.apis.io/buildix-trade/security/buildix-trade-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildix-trade-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildix.trade/
created: '2026-11-03'
description: Buildix is a crypto orderflow analytics platform offering real-time VPIN, CVD, whale tracking and an AI strategy advisor across the 100 most liquid Hyperliquid perpetual contracts. It provides free screener access and tiered paid plans for traders and institutions, delivering deep market microstructure insights and on‑chain analytics.
json_schemas:
- name: DeepView
  property_count: 12
  slug: buildix-trade-deep-view
- name: FundingArb
  property_count: 7
  slug: buildix-trade-funding-arb
- name: PairDetail
  property_count: 11
  slug: buildix-trade-pair-detail
- name: Pair
  property_count: 6
  slug: buildix-trade-pair
- name: SignalScore
  property_count: 6
  slug: buildix-trade-signal-score
- name: WhalePosition
  property_count: 10
  slug: buildix-trade-whale-position
jsonld:
- class_count: 6
  name: Buildix Trade Context
  property_count: 35
  slug: buildix-trade-context
layout: provider
modified: '2026-11-03'
name: Buildix
nav: Providers
network: true
overview: 'Buildix publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Deep View API, Funding Arb API, Pair API, and 3 more. Tagged areas include Company, Cryptocurrency, Analytics, Orderflow, and Artificial Intelligence.


  The Buildix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Buildix''s developer surface includes pricing, documentation, engineering blog, getting-started guide, authentication, and 17 more developer resources.'
plans:
- name: Buildix Trade Plans Pricing
  plan_count: 8
  slug: buildix-trade-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Buildix API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: buildix-trade-rules
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 60.7
    developer_ergonomics: 28.6
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
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
  name: Buildix Trade Authentication
  slug: buildix-trade-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Buildix Trade Domain Security
  slug: buildix-trade-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buildix-trade
tags:
- Company
- Cryptocurrency
- Analytics
- Orderflow
- Artificial Intelligence
website: https://buildix.trade/
---
