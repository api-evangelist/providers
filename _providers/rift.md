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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.5
  scored_at: '2026-09-04'
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
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: OpenAPI
  url: openapi/_original/rift-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rift-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rift-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/rift-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rift-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rift-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rift-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rift-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/rift-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rift-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/rift-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rift-domain-security.yml
created: '2026-07-17'
description: Rift is a decentralized exchange (DEX) aggregator that routes swap orders across 20+ trading venues and cross-chain bridges to guarantee best-price execution with zero added fees. Its Router API (v3, currently in beta) lets developers request a best-price market quote for an asset swap, create a market order against that quote with an idempotency key, and check the online status of both the Rift service and each downstream execution provider (Across, CCTP, Hyperliquid, KyberSwap, and more). Rift is backed by Paradigm, WTG Ventures, Edge Capital, and 20+ angel investors.
image: https://www.rift.trade/images/logos/rift_logo_new_glow.png
layout: provider
modified: '2026-07-21'
name: Rift
nav: Providers
network: true
overview: 'Rift publishes 3 APIs on the [APIs.io](https://apis.io/) network: Orders API, Quotes API, and Status API. Tagged areas include Company, Crypto Defi, DEX Aggregator, Cross-Chain, and Trading.


  Rift''s developer surface includes documentation, API reference, getting-started guide, authentication, and 15 more developer resources.'
random_paper: 17
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 51.5
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 30.3
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
    score: 28.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rift/refs/heads/main/screenshots/rift-2026-09-02T153815.png
security:
- kind: authentication
  name: Rift Authentication
  slug: rift-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rift Domain Security
  slug: rift-domain-security
  summary_line: TLSv1.3 · HSTS
slug: rift
tags:
- Company
- Crypto Defi
- DEX Aggregator
- Cross-Chain
- Trading
- Swaps
- Bridge
- Best Execution
website: https://rift.trade
---
