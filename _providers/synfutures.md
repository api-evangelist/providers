---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 22
  human_in_the_loop: 1
  name: Synfutures Agentic Access
  operation_count: 43
  slug: synfutures-agentic-access
  summary_line: 43 operations · 22 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://base-api.synfutures.com/rwa/trading
  baseurl_source: declared
  description: Cash (USD) deposits and withdrawals
  name: SynFutures Cash API
  slug: synfutures-cash-api
- baseURL: https://base-api.synfutures.com/rwa/trading
  baseurl_source: declared
  description: On-chain market config, symbols, prices, and corporate actions
  name: SynFutures Market Data API
  slug: synfutures-market-data-api
- baseURL: https://base-api.synfutures.com/rwa/trading
  baseurl_source: declared
  description: One Click Trading (1CT) delegation lifecycle
  name: SynFutures One Click API
  slug: synfutures-one-click-api
- baseURL: https://base-api.synfutures.com/rwa/trading
  baseurl_source: declared
  description: Order list, calldata build, One Click send/cancel, and tx recording
  name: SynFutures Orders API
  slug: synfutures-orders-api
- baseURL: https://base-api.synfutures.com/rwa/trading
  baseurl_source: declared
  description: User info, balances, and positions
  name: SynFutures Portfolio API
  slug: synfutures-portfolio-api
- baseURL: https://base-api.synfutures.com/rwa/trading
  baseurl_source: declared
  description: Tokenized stock deposits and withdrawals
  name: SynFutures Stock API
  slug: synfutures-stock-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SynFutures RWA Trading Cash API
  slug: open-synfutures-cash-api
- collection_type: open
  name: SynFutures RWA Trading Cash Market Data API
  slug: open-synfutures-market-data-api
- collection_type: open
  name: SynFutures RWA Trading Cash One Click API
  slug: open-synfutures-one-click-api
- collection_type: open
  name: SynFutures RWA Trading Cash Orders API
  slug: open-synfutures-orders-api
- collection_type: open
  name: SynFutures RWA Trading Cash Portfolio API
  slug: open-synfutures-portfolio-api
- collection_type: open
  name: SynFutures RWA Trading Cash Stock API
  slug: open-synfutures-stock-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/synfutures-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synfutures-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.synfutures.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.synfutures.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.synfutures.com/rwa-trading-apis/readme
- group: docs
  title: ''
  type: APIReference
  url: https://docs.synfutures.com/rwa-trading-apis/reference/endpoint-index
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.synfutures.com/rwa-trading-apis/guides/quickstart-first-trade
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SynFutures
- group: start
  title: ''
  type: SignUp
  url: https://app.synfutures.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/synfutures-rwa-trading-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synfutures-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synfutures-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/synfutures-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/synfutures-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/synfutures-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/synfutures-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synfutures-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synfutures-lifecycle.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/synfutures-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/synfutures-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/synfutures-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: SynFutures is an on-chain derivatives and real-world-asset (RWA) trading protocol that brings crypto perpetuals, tokenized stocks, and ETFs on-chain across Base, Ethereum, and Monad. For developers it exposes a RESTful RWA Trading API (market data, portfolio, order placement, cash and stock operations, and One Click delegated trading) secured with HMAC-SHA256 signed, IP-whitelisted API keys, plus TypeScript SDKs (@synfutures/sdks-perp and oyster-sdk) and on-chain smart contracts for the Oyster (V3) protocol. Backed by Pantera Capital and Polychain.
image: https://www.synfutures.com/assets/trade_every_asset.png
layout: provider
modified: '2026-07-21'
name: SynFutures
nav: Providers
network: true
overview: 'SynFutures publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Cash API, Market Data API, One Click API, and 3 more. Tagged areas include Company, Crypto, DeFi, Trading, and Derivatives.


  SynFutures'' developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, and 17 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 1
  name: Synfutures Rate Limits
  slug: synfutures-rate-limits
score:
  band: thin
  composite: 34.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 51.7
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
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
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synfutures/refs/heads/main/screenshots/synfutures-2026-09-02T161503.png
security:
- kind: authentication
  name: Synfutures Authentication
  slug: synfutures-authentication
  summary_line: apiKey/hmac · 6 schemes
- kind: domain-security
  name: Synfutures Domain Security
  slug: synfutures-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: synfutures
tags:
- Company
- Crypto
- DeFi
- Trading
- Derivatives
- Real World Assets
- Blockchain
website: https://www.synfutures.com/
---
