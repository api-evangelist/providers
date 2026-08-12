---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bitwise Agentic Access
  operation_count: 6
  slug: bitwise-agentic-access
  summary_line: 6 operations
api_count: 3
apis:
- description: Bitwise exchange-traded fund listings and details.
  name: Bitwise ETFs API
  slug: bitwise-etfs-api
- description: Per-fund market data (NAV, AUM, holdings, performance).
  name: Bitwise Funds API
  slug: bitwise-funds-api
- description: Bitwise crypto index metadata, history, and constituents.
  name: Bitwise Indexes API
  slug: bitwise-indexes-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bitwise-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/bitwise-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bitwise-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bitwise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitwiseinvestments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.bitwiseinvestments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bitwiseinvestments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.bitwiseinvestments.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.bitwiseinvestments.com/
- group: build
  title: ''
  type: Postman
  url: https://developers.bitwiseinvestments.com/
- group: operate
  title: ''
  type: Support
  url: mailto:api@bitwiseinvestments.com
- group: company
  title: ''
  type: Blog
  url: https://bitwiseinvestments.com/crypto-market-insights
- group: start
  title: ''
  type: SignUp
  url: https://experts.bitwiseinvestments.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.bitwiseinvestments.com/investor-portal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bitwiseinvestments.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bitwiseinvestments.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bitwise-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Bitwise Asset Management is a crypto-focused investment manager (founded 2017, offices in San Francisco, New York, London, and Frankfurt) offering crypto index funds, ETFs, separately managed accounts, private funds, and staking products across 70+ vehicles including the Bitwise 10 Crypto Index (BITW) and spot Bitcoin (BITB) and Ethereum (ETHW) ETFs. Bitwise publishes a read-only market-data API for its indexes, ETFs, and fund data via a public Postman developer portal, covering index metadata, historical daily index values, index constituents (prices/supplies/weights), and per-fund data (NAV, AUM, holdings, crypto-per-share, performance). API keys are issued on request. This profile was enriched by the API Evangelist pipeline from the provider's public developer surface.
image: https://bitwiseinvestments.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: bitwise-mcp.yml
  slug: bitwise-mcpyml
modified: '2026-07-18'
name: Bitwise
nav: Providers
network: true
overview: 'Bitwise publishes 3 APIs on the [APIs.io](https://apis.io/) network: ETFs API, Funds API, and Indexes API. Tagged areas include Company, Fintech, Cryptocurrency, Asset Management, and Market Data.


  Bitwise''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 12 more developer resources.'
random_paper: 63
score:
  band: thin
  composite: 39.1
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 62.7
    developer_ergonomics: 49.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 40.2
  provenance:
    agentic_access: derived
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
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bitwise/refs/heads/main/screenshots/bitwise-2026-07-25T203218.png
security:
- kind: authentication
  name: Bitwise Authentication
  slug: bitwise-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bitwise Domain Security
  slug: bitwise-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitwise
tags:
- Company
- Fintech
- Cryptocurrency
- Asset Management
- Market Data
- Index Funds
- ETFs
- Financial Services
website: https://bitwiseinvestments.com/
---
