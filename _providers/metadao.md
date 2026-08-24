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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.5
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: API information and health
  name: MetaDAO Meta API
  slug: metadao-meta-api
- description: Token supply breakdown and allocation
  name: MetaDAO Supply API
  slug: metadao-supply-api
- description: DAO trading pairs, pricing, and volume
  name: MetaDAO Tickers API
  slug: metadao-tickers-api
- description: Aggregate trading volume
  name: MetaDAO Volume API
  slug: metadao-volume-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MetaDAO Futarchy DEX Meta API
  slug: open-metadao-meta-api
- collection_type: open
  name: MetaDAO Futarchy DEX Meta Supply API
  slug: open-metadao-supply-api
- collection_type: open
  name: MetaDAO Futarchy DEX Meta Tickers API
  slug: open-metadao-tickers-api
- collection_type: open
  name: MetaDAO Futarchy DEX Meta Volume API
  slug: open-metadao-volume-api
common:
- group: company
  title: ''
  type: Website
  url: https://metadao.fi
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.metadao.fi/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.metadao.fi/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.metadao.fi/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.metadao.fi/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metaDAOproject
- group: auth
  title: ''
  type: Authentication
  url: authentication/metadao-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metadao-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metadao-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metadao-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metadao-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metadao-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/metadao-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/metadao-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/metadao-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/metadao-market-data.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/metadao-token-supply.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metadao-llms.txt
created: '2026-07-17'
description: MetaDAO is a fundraising and governance platform for high-quality founders and their communities, built on the Solana Futarchy protocol. It runs early fair token launches (high-float ICOs) and market-driven ("futarchy") governance where decision markets control treasury and intellectual property, with performance-aligned insider token unlocks. For developers, MetaDAO operates the public Futarchy DEX API — a CoinGecko-compatible, read-only market-data API at market-api.metadao.fi that automatically discovers every DAO on the protocol and exposes real-time pricing, trading volume, liquidity, and token supply. Surfaced as a Paradigm portfolio company and enriched by the API Evangelist pipeline from MetaDAO's own published documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metadao.png
layout: provider
mcp_servers:
- description: ''
  name: MetaDAO MCP Server
  slug: metadao-mcp-server
modified: '2026-07-20'
name: MetaDAO
nav: Providers
network: true
overview: 'MetaDAO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Meta API, Supply API, Tickers API, and 1 more. Tagged areas include Company, Crypto Tools, DeFi, Solana, and DEX.


  MetaDAO''s developer surface includes documentation, API reference, getting-started guide, authentication, and 14 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 1
  name: Metadao Rate Limits
  slug: metadao-rate-limits
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 50.3
    developer_ergonomics: 51.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 35.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metadao/refs/heads/main/screenshots/metadao-2026-08-07T172641.png
security:
- kind: authentication
  name: Metadao Authentication
  slug: metadao-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Metadao Domain Security
  slug: metadao-domain-security
  summary_line: DNSSEC · DMARC
slug: metadao
tags:
- Company
- Crypto Tools
- DeFi
- Solana
- DEX
- Governance
- Market Data
- Futarchy
website: https://metadao.fi
---
