---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://router-gateway-v3-production.up.railway.app
  baseurl_source: declared
  description: Market order creation and execution
  name: Rift Orders API
  slug: rift-orders-api
- baseURL: https://router-gateway-v3-production.up.railway.app
  baseurl_source: declared
  description: Best-price quoting across routing venues
  name: Rift Quotes API
  slug: rift-quotes-api
- baseURL: https://router-gateway-v3-production.up.railway.app
  baseurl_source: declared
  description: Service and execution-provider health
  name: Rift Status API
  slug: rift-status-api
artifact_total: 9
collections:
- collection_type: open
  name: Rift Router Orders API
  slug: open-rift-orders-api
- collection_type: open
  name: Rift Router Orders Quotes API
  slug: open-rift-quotes-api
- collection_type: open
  name: Rift Router Orders Status API
  slug: open-rift-status-api
common:
- group: company
  title: ''
  type: Blog
  url: https://www.rift.trade/articles
- group: company
  title: ''
  type: Website
  url: https://rift.trade
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.rift.trade
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rift.trade
- group: docs
  title: ''
  type: APIReference
  url: https://docs.rift.trade/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rift.trade/what-is-rift
- group: other
  title: ''
  type: X
  url: https://x.com/RIFTHQ
- group: docs
  href: https://artifacts.apis.io/rift/openapi/_original/rift-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/rift-openapi.yml
- group: auth
  href: https://artifacts.apis.io/rift/authentication/rift-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rift-authentication.yml
- group: design
  href: https://artifacts.apis.io/rift/conventions/rift-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rift-conventions.yml
- group: design
  href: https://artifacts.apis.io/rift/conventions/rift-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/rift-conventions.yml
- group: design
  href: https://artifacts.apis.io/rift/errors/rift-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rift-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rift/data-model/rift-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rift-data-model.yml
- group: design
  href: https://artifacts.apis.io/rift/conformance/rift-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rift-conformance.yml
- group: design
  href: https://artifacts.apis.io/rift/lifecycle/rift-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rift-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/rift/mcp/rift-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rift-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rift/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/rift/llms/rift-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rift-llms.txt
- group: other
  href: https://artifacts.apis.io/rift/overlays/rift-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rift-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/rift/security/rift-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rift-domain-security.yml
created: '2026-07-17'
description: Rift is a decentralized exchange (DEX) aggregator that routes swap orders across 20+ trading venues and cross-chain bridges to guarantee best-price execution with zero added fees. Its Router API (v3, currently in beta) lets developers request a best-price market quote for an asset swap, create a market order against that quote with an idempotency key, and check the online status of both the Rift service and each downstream execution provider (Across, CCTP, Hyperliquid, KyberSwap, and more). Rift is backed by Paradigm, WTG Ventures, Edge Capital, and 20+ angel investors.
image: https://www.rift.trade/images/logos/rift_logo_new_glow.png
layout: provider
modified: '2026-10-06'
name: Rift
nav: Providers
network: true
overview: 'Rift publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Orders API, Quotes API, and Status API. Tagged areas include Company, Crypto Defi, DEX Aggregator, Cross-Chain, and Trading.


  Rift''s developer surface includes engineering blog, documentation, API reference, getting-started guide, authentication, and 15 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 46.3
    developer_ergonomics: 54.2
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 28.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rift/rift-2026-09-02T153815.png
security:
- kind: authentication
  name: Rift Authentication
  slug: rift-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rift Domain Security
  slug: rift-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: Swap assets with Rift
  slug: rift-swap
slug: rift
tags:
- Company
- Crypto Defi
- DEX Aggregator
- Cross-Chain
- Trading
- Swap
- Bridge
- Best Execution
website: https://rift.trade
---
