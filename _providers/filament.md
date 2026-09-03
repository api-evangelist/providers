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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.4
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://orderbook.filament.finance/sei
  baseurl_source: declared
  description: Signature-authenticated REST + WebSocket order-book API for the Filament perpetual DEX on Sei. Place limit/market orders, cancel orders, manage isolated collateral, set TP/SL, read tradable assets wit
  name: Filament API
  slug: filament-api
artifact_total: 4
asyncapis:
- description: 'Real-time WebSocket streams for the Filament perpetual DEX on Sei: order-book state, live asset price feed, and per-account order updates.'
  name: Filament Orderbook Streaming API
  slug: filament-orderbook-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://filament.finance/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.filament.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.filament.finance/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.filament.finance/market-makers/filament-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.filament.finance/guides/trading
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@filament.finance
- group: other
  title: ''
  type: X
  url: https://twitter.com/FilamentFinance
- group: start
  title: ''
  type: Sandbox
  url: sandbox/filament-sandbox.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/filament-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/filament-conventions.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/filament-mcp.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/filament-orderbook-asyncapi.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/filament-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/filament-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/filament-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/filament-domain-security.yml
- group: auth
  title: ''
  type: SecurityAudit
  url: https://docs.filament.finance/resources/security-audits
- group: other
  title: ''
  type: BrandKit
  url: https://docs.filament.finance/resources/brand-kit
created: '2026-07-17'
description: Filament (Filament Finance) is a hybrid on-chain perpetual / derivatives DEX built on the Sei Network. It pairs an off-chain orderbook with a Compartment-Based (COMB) liquidity pool to deliver deep liquidity even in thin markets, offering up to 30x leverage on crypto perpetuals using USDC collateral and oracle-based mark prices. Filament Pro is the flagship trading platform, and the project exposes a signature-authenticated REST + WebSocket order-book API at orderbook.filament.finance for market makers and programmatic traders. The team draws on experience from Goldman Sachs, BlackRock, Persistence, and Nethermind; the protocol's smart contracts were audited by PeckShield. Added to the API Evangelist network as a portfolio-lead stub and enriched from the provider's public documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/filament.png
layout: provider
modified: '2026-07-19'
name: Filament
nav: Providers
network: true
overview: 'Filament publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, DeFi, Derivatives, and Perpetuals.


  The Filament catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Filament''s developer surface includes documentation, API reference, getting-started guide, engineering blog, sandbox, authentication, and 13 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 41.7
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 24.2
  provenance:
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/filament/refs/heads/main/screenshots/filament-2026-07-25T214446.png
security:
- kind: authentication
  name: Filament Authentication
  slug: filament-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Filament Domain Security
  slug: filament-domain-security
  summary_line: TLSv1.3 · HSTS
slug: filament
tags:
- Company
- Crypto
- DeFi
- Derivatives
- Perpetuals
- DEX
- Trading
- Blockchain
- SEI
- Web3
website: https://filament.finance/
---
