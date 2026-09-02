---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
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
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Ribbon Finance Agentic Access
  operation_count: 33
  slug: ribbon-finance-agentic-access
  summary_line: 33 operations · 10 acting
api_count: 2
apis:
- description: Real-time WebSocket API for Aevo exchange providing low-latency streams for orderbook updates, trade feeds, position fills, index price updates, funding rates, and ticker information. Supports both pu
  name: Aevo Exchange WebSocket API
  slug: aevo-exchange-websocket-api
- description: GraphQL API hosted on The Graph protocol providing indexed on-chain data for Ribbon Finance vaults including vault performance metrics, historical pricing per share, fee collection data, premium earni
  name: Ribbon Finance Subgraph API
  slug: ribbon-finance-subgraph-api
- description: Account management endpoints
  name: Ribbon Finance Account API
  slug: ribbon-finance-account-api
- description: API key management
  name: Ribbon Finance API Keys API
  slug: ribbon-finance-api-keys-api
- description: Instrument and market information
  name: Ribbon Finance Instruments API
  slug: ribbon-finance-instruments-api
- description: Public market data endpoints
  name: Ribbon Finance Market Data API
  slug: ribbon-finance-market-data-api
- description: Order management endpoints
  name: Ribbon Finance Orders API
  slug: ribbon-finance-orders-api
- description: Position and portfolio endpoints
  name: Ribbon Finance Positions API
  slug: ribbon-finance-positions-api
- description: Exchange statistics and analytics
  name: Ribbon Finance Statistics API
  slug: ribbon-finance-statistics-api
- description: Trade and transaction history endpoints
  name: Ribbon Finance Trade History API
  slug: ribbon-finance-trade-history-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Aevo Exchange Private REST Account API
  slug: open-ribbon-finance-account-api
- collection_type: open
  name: Aevo Exchange Private REST Account API Keys API
  slug: open-ribbon-finance-api-keys-api
- collection_type: open
  name: Aevo Exchange Private REST Account Instruments API
  slug: open-ribbon-finance-instruments-api
- collection_type: open
  name: Aevo Exchange Private REST Account Market Data API
  slug: open-ribbon-finance-market-data-api
- collection_type: open
  name: Aevo Exchange Private REST Account Orders API
  slug: open-ribbon-finance-orders-api
- collection_type: open
  name: Aevo Exchange Private REST Account Positions API
  slug: open-ribbon-finance-positions-api
- collection_type: open
  name: Aevo Exchange Private REST Account Statistics API
  slug: open-ribbon-finance-statistics-api
- collection_type: open
  name: Aevo Exchange Private REST Account Trade History API
  slug: open-ribbon-finance-trade-history-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ribbon-finance-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ribbon-finance-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ribbon-finance-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ribbon.finance/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aevo.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.aevo.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ribbon-finance
- group: company
  title: ''
  type: Website
  url: https://www.ribbon.finance/
- group: company
  title: ''
  type: Blog
  url: https://ribbonfinance.medium.com/
- group: other
  title: ''
  type: Governance
  url: https://gov.ribbon.finance/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/ribbon-finance/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/ribbon-finance/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/ribbon-finance/refs/heads/main/finops/finops.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/ribbon-finance/refs/heads/main/json-ld/ribbon-finance.json
created: '2026-06-14'
description: Ribbon Finance is a DeFi structured products platform that helps users access crypto structured products through automated options strategies. The platform offers Theta Vaults (Decentralized Options Vaults) for covered calls and cash-secured puts, Ribbon Earn for yield optimization, and Ribbon Lend for unsecured lending. Ribbon Finance merged with Aevo, a high-performance Layer-2 order-book decentralized exchange for options and perpetuals trading, providing REST and WebSocket APIs for querying vault performance, options strategies, yield data, and live exchange trading data.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: Ribbon Finance provides a GraphQL API via The Graph protocol, giving developers access to indexed on-chain data for Ribbon Finance Theta Vaults on Ethereum mainnet. The subgraph tracks vault performan
  name: Ribbon Finance GraphQL API
  slug: ribbon-finance-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ribbon-finance.png
layout: provider
modified: '2026-06-14'
name: Ribbon Finance
nav: Providers
network: true
overview: 'Ribbon Finance publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Instruments API, and 5 more. Tagged areas include DeFi, Finance, Options, Structured Products, and Ethereum.


  Ribbon Finance''s developer surface includes authentication, documentation, API reference, engineering blog, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 19
rate_limits:
- limit_count: 0
  name: Aevo Websocket
  slug: aevo-websocket
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.8
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ribbon-finance/refs/heads/main/screenshots/ribbon-finance-2026-06-20T193110.png
security:
- kind: authentication
  name: Ribbon Finance Authentication
  slug: ribbon-finance-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Ribbon Finance Domain Security
  slug: ribbon-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ribbon-finance
tags:
- DeFi
- Finance
- Options
- Structured Products
- Ethereum
- Layer 2
- Vault
- Perpetuals
- Yield
website: https://www.ribbon.finance/
---
