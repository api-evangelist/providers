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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Bullet Agentic Access
  operation_count: 37
  slug: bullet-agentic-access
  summary_line: 37 operations · 3 acting
api_count: 1
apis:
- baseURL: https://tradingapi.bullet.xyz
  baseurl_source: declared
  description: The Account API from Bullet — 8 operation(s) for account.
  name: Bullet Account API
  slug: bullet-account-api
- baseURL: https://tradingapi.bullet.xyz
  baseurl_source: declared
  description: The Address API from Bullet — 1 operation(s) for address.
  name: Bullet Address API
  slug: bullet-address-api
- baseURL: https://tradingapi.bullet.xyz
  baseurl_source: declared
  description: The Health API from Bullet — 4 operation(s) for health.
  name: Bullet Health API
  slug: bullet-health-api
- baseURL: https://tradingapi.bullet.xyz
  baseurl_source: declared
  description: The Market-Data API from Bullet — 11 operation(s) for market-data.
  name: Bullet Market-Data API
  slug: bullet-market-data-api
- baseURL: https://tradingapi.bullet.xyz
  baseurl_source: declared
  description: The Rollup API from Bullet — 3 operation(s) for rollup.
  name: Bullet Rollup API
  slug: bullet-rollup-api
- baseURL: https://tradingapi.bullet.xyz
  baseurl_source: declared
  description: The SolanaOffchainTx API from Bullet — 1 operation(s) for solanaoffchaintx.
  name: Bullet SolanaOffchainTx API
  slug: bullet-solanaoffchaintx-api
- baseURL: https://tradingapi.bullet.xyz
  baseurl_source: declared
  description: The Trading API from Bullet — 2 operation(s) for trading.
  name: Bullet Trading API
  slug: bullet-trading-api
- baseURL: https://tradingapi.bullet.xyz
  baseurl_source: declared
  description: The Tx API from Bullet — 1 operation(s) for tx.
  name: Bullet Tx API
  slug: bullet-tx-api
- baseURL: https://tradingapi.bullet.xyz
  baseurl_source: declared
  description: The User Data (Beta) API from Bullet — 6 operation(s) for user data (beta).
  name: Bullet User Data (Beta) API
  slug: bullet-user-data-beta-api
arazzos:
- description: Discover markets then pull the order book, 24h ticker, and recent trades for a symbol.
  name: Bullet market-data snapshot
  slug: bullet-market-data-snapshot
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bullet Trading Account API
  slug: open-bullet-account-api
- collection_type: open
  name: Bullet Trading Account Address API
  slug: open-bullet-address-api
- collection_type: open
  name: Bullet Trading Account Health API
  slug: open-bullet-health-api
- collection_type: open
  name: Bullet Trading Account Market-Data API
  slug: open-bullet-market-data-api
- collection_type: open
  name: Bullet Trading Account Rollup API
  slug: open-bullet-rollup-api
- collection_type: open
  name: Bullet Trading Account SolanaOffchainTx API
  slug: open-bullet-solanaoffchaintx-api
- collection_type: open
  name: Bullet Account Trading API
  slug: open-bullet-trading-api
- collection_type: open
  name: Bullet Trading Account Tx API
  slug: open-bullet-tx-api
- collection_type: open
  name: Bullet Trading Account User Data (Beta) API
  slug: open-bullet-user-data-beta-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/bullet-trading-api-openapi.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.bullet.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bullet.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://tradingapi.bullet.xyz/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://tradingapi.bullet.xyz/docs/getting-started.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/bullet-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/bullet-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/bullet-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bullet-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bullet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bullet-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bullet-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bullet.xyz/
- group: design
  title: ''
  type: Conformance
  url: conformance/bullet-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bullet-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/bullet-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bullet-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/bullet-trading-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/bullet-market-data-snapshot.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bullet-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bullet-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bullet-agentic-access.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bulletxyz
- group: operate
  title: ''
  type: Support
  url: https://docs.bullet.xyz/exchange/help-center/contact-support.md
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.bullet.xyz/exchange/trading/fees.md
- group: start
  title: ''
  type: SignUp
  url: https://app.bullet.xyz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.bullet.xyz/legals/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.bullet.xyz/legals/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.bullet.xyz/
- group: other
  title: ''
  type: X
  url: https://x.com/bulletxyz
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/QuP3YsRAtx
- group: other
  title: ''
  type: Telegram
  url: https://t.me/bullet_xyz
created: '2026-07-17'
description: Bullet is Solana's high-performance trading layer — a decentralized exchange offering perpetual futures (derivatives), spot, and lending under one unified margin engine. The Bullet Trading API is a Binance USD-M Futures (FAPI) compatible REST and WebSocket interface for market data, account and position management, and order placement via ed25519-signed transactions, with official Rust and WASM/TypeScript SDKs. Bullet runs as a sovereign rollup settling to Solana mainnet-beta, with a testnet environment for building and testing against mock assets.
image: https://tradingapi.bullet.xyz/docs/favicon-de23e50b.svg
layout: provider
modified: '2026-07-18'
name: Bullet
nav: Providers
network: true
overview: 'Bullet publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Address API, Health API, and 6 more. Tagged areas include Company, DeFi, Solana, Cryptocurrency, and Derivatives.


  Bullet''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, support, pricing, and 26 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 49.4
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 44.9
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
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bullet/refs/heads/main/screenshots/bullet-2026-07-25T204059.png
security:
- kind: authentication
  name: Bullet Authentication
  slug: bullet-authentication
  summary_line: signature · 1 scheme
- kind: domain-security
  name: Bullet Domain Security
  slug: bullet-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bullet
tags:
- Company
- DeFi
- Solana
- Cryptocurrency
- Derivatives
- Exchange
- Trading
- Perpetuals
- Lending
- Blockchain
website: https://www.bullet.xyz/
---
