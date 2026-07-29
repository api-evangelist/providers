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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Robinhood Agentic Access
  operation_count: 9
  slug: robinhood-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 5
apis:
- description: Crypto trading account details and buying power.
  name: Robinhood Account API
  slug: robinhood-account-api
- description: Current cryptocurrency positions.
  name: Robinhood Holdings API
  slug: robinhood-holdings-api
- description: Best bid/ask quotes and estimated execution prices.
  name: Robinhood Market Data API
  slug: robinhood-market-data-api
- description: Place, list, retrieve, and cancel crypto orders.
  name: Robinhood Orders API
  slug: robinhood-orders-api
- description: Supported crypto trading pairs and their constraints.
  name: Robinhood Trading Pairs API
  slug: robinhood-trading-pairs-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/robinhood-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/robinhood
- group: auth
  title: ''
  type: DomainSecurity
  url: security/robinhood-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://robinhood.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.robinhood.com/crypto/trading/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.robinhood.com/crypto/trading/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.robinhood.com/crypto/trading/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.robinhood.com/crypto/trading/
- group: operate
  title: ''
  type: Support
  url: https://robinhood.com/us/en/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.robinhood.com
- group: company
  title: ''
  type: Blog
  url: https://newsroom.aboutrobinhood.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/robinhoodmarkets
- group: commercial
  title: ''
  type: TermsOfService
  url: https://robinhood.com/us/en/about/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://robinhood.com/us/en/about/legal/
- group: auth
  title: ''
  type: Authentication
  url: authentication/robinhood-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/robinhood-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/robinhood-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/robinhood-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/robinhood-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/robinhood-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/robinhood-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/robinhood-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/robinhood-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/robinhood-crypto-trading-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/robinhood-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/robinhood-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/robinhood-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Robinhood Markets is a US financial-services company offering commission-free trading of stocks, ETFs, options, and cryptocurrency, plus retirement accounts, a cash/spending card, and 24-hour markets. For developers, Robinhood publishes the Crypto Trading API, a REST interface at trading.robinhood.com that lets an account holder view buying power and holdings, pull market data (best bid/ask and estimated fill prices), enumerate supported trading pairs, and place, retrieve, and cancel crypto orders (market, limit, stop-loss, and stop-limit). The API authenticates each request with an API key plus an Ed25519 request signature carried in the x-api-key, x-timestamp, and x-signature headers. Robinhood was added to the API Evangelist network as a VC-portfolio lead and enriched from its public developer surface.
image: https://robinhood.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: robinhood-mcp.yml
  slug: robinhood-mcpyml
modified: '2026-07-21'
name: Robinhood
nav: Providers
network: true
overview: 'Robinhood publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Holdings API, Market Data API, and 2 more. Tagged areas include Company, Fintech, Cryptocurrency, Trading, and Brokerage.


  Robinhood''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 22 more developer resources.'
random_paper: 4
score:
  band: developing
  composite: 46.7
  delta: -4.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 62.5
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Robinhood Authentication
  slug: robinhood-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Robinhood Domain Security
  slug: robinhood-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Robinhood Vulnerability Disclosure
  slug: robinhood-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: robinhood
tags:
- Company
- Fintech
- Cryptocurrency
- Trading
- Brokerage
- Investing
- Financial Services
- Crypto
website: https://robinhood.com
---
