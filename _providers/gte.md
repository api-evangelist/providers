---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Gte Agentic Access
  operation_count: 18
  slug: gte-agentic-access
  summary_line: 18 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api-testnet.gte.xyz/v1
  baseurl_source: declared
  description: The Exchange API from GTE — 1 operation(s) for exchange.
  name: GTE Exchange API
  slug: gte-exchange-api
- baseURL: https://api-testnet.gte.xyz/v1
  baseurl_source: declared
  description: The Health API from GTE — 1 operation(s) for health.
  name: GTE Health API
  slug: gte-health-api
- baseURL: https://api-testnet.gte.xyz/v1
  baseurl_source: declared
  description: The Info API from GTE — 1 operation(s) for info.
  name: GTE Info API
  slug: gte-info-api
- baseURL: https://api-testnet.gte.xyz/v1
  baseurl_source: declared
  description: The Markets API from GTE — 6 operation(s) for markets.
  name: GTE Markets API
  slug: gte-markets-api
- baseURL: https://api-testnet.gte.xyz/v1
  baseurl_source: declared
  description: The Tokens API from GTE — 3 operation(s) for tokens.
  name: GTE Tokens API
  slug: gte-tokens-api
- baseURL: https://api-testnet.gte.xyz/v1
  baseurl_source: declared
  description: The Users API from GTE — 6 operation(s) for users.
  name: GTE Users API
  slug: gte-users-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: GTE Exchange API
  slug: open-gte-exchange-api
- collection_type: open
  name: GTE Exchange Health API
  slug: open-gte-health-api
- collection_type: open
  name: GTE Exchange Info API
  slug: open-gte-info-api
- collection_type: open
  name: GTE Exchange Markets API
  slug: open-gte-markets-api
- collection_type: open
  name: GTE Exchange Tokens API
  slug: open-gte-tokens-api
- collection_type: open
  name: GTE Exchange Users API
  slug: open-gte-users-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gte-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gte-agentic-access.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gte.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gte.xyz
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gte-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/gte-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gte-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/gte-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gte-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gte-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gte-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gte-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gte-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/gte-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gte-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gte-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gte-openapi-overlay.yaml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Liquid-Labs-Inc
- group: company
  title: ''
  type: Blog
  url: https://www.gte.xyz/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/gte-xyz
- group: start
  title: ''
  type: SignUp
  url: https://testnet.gte.xyz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gte.xyz/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gte.xyz/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/GTE_XYZ
- group: company
  title: ''
  type: Website
  url: https://www.gte.xyz
created: '2026-07-17'
description: GTE (Global Token Exchange) is a non-custodial, permissionless decentralized exchange built on MegaETH, offering a central limit order book (CLOB) with CEX-level speed — advertised at 100,000 orders per second and ~1ms latency — combined with DeFi security properties. Users trade crypto and tokenized assets 24/7 from a self-custodied wallet, with spot and leveraged/perpetual markets, shortable positions, and on-chain settlement. GTE exposes a public HTTP + WebSocket API (GTE API v1) covering tokens, markets, candles, trades, order books, and per-wallet portfolio/order data, plus a signed POST /exchange endpoint for submitting orders and trades. An official Python SDK (gte-py) constructs the signed transaction bodies. GTE is developed by Liquid Labs and backed by Paradigm.
image: https://framerusercontent.com/images/dmNBRSvrpcZRlw2DSNsXF7eY0MA.png
layout: provider
modified: '2026-07-19'
name: GTE
nav: Providers
network: true
overview: 'GTE publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Exchange API, Health API, Info API, and 3 more. Tagged areas include Company, Crypto Defi, Decentralized Exchange, Trading, and Market Data.


  GTE''s developer surface includes documentation, authentication, sandbox, engineering blog, support, signup flow, and 20 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 4.5
    contract_quality: 41.2
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gte/refs/heads/main/screenshots/gte-2026-07-25T220408.png
security:
- kind: authentication
  name: Gte Authentication
  slug: gte-authentication
  summary_line: signature · 0 schemes
- kind: domain-security
  name: Gte Domain Security
  slug: gte-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gte
tags:
- Company
- Crypto Defi
- Decentralized Exchange
- Trading
- Market Data
- Order Book
- Perpetuals
- MegaETH
- Blockchain
website: https://www.gte.xyz
---
