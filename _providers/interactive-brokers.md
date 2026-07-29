---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Interactive Brokers Agentic Access
  operation_count: 9
  slug: interactive-brokers-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 7
apis:
- description: The Interactive Brokers Client Portal API is a REST API accessed through a locally running Java gateway that routes authenticated requests to IBKR systems. It provides a lightweight interface for trad
  name: Interactive Brokers Client Portal API
  slug: client-portal-api
- description: Account information and management
  name: Interactive Brokers Accounts API
  slug: interactive-brokers-accounts-api
- description: Contract and instrument search
  name: Interactive Brokers Contracts API
  slug: interactive-brokers-contracts-api
- description: Real-time and historical market data
  name: Interactive Brokers Market Data API
  slug: interactive-brokers-market-data-api
- description: Order placement and management
  name: Interactive Brokers Orders API
  slug: interactive-brokers-orders-api
- description: Portfolio positions and account summaries
  name: Interactive Brokers Portfolio API
  slug: interactive-brokers-portfolio-api
- description: Authentication and session management
  name: Interactive Brokers Sessions API
  slug: interactive-brokers-sessions-api
artifact_total: 17
asyncapis:
- description: 'AsyncAPI definition for the Interactive Brokers (IBKR) Client Portal Web API streaming WebSocket endpoint. The Client Portal API exposes a single WebSocket endpoint at `/v1/api/ws` over which clients '
  name: Interactive Brokers Client Portal API WebSocket
  slug: interactive-brokers-asyncapi
collections:
- collection_type: open
  name: Interactive Brokers Web API
  slug: open-interactive-brokers-web-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/interactive-brokers-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/interactive-brokers-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/interactive-brokers-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/interactive-brokers-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/interactive-brokers
- group: start
  title: ''
  type: Portal
  url: https://www.interactivebrokers.com/campus/ibkr-api-page/ibkr-api-home/
- group: docs
  title: ''
  type: Documentation
  url: https://www.interactivebrokers.com/campus/ibkr-api-page/webapi-doc/
- group: company
  title: ''
  type: Website
  url: https://www.interactivebrokers.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nicholasgasior/interactive-brokers-api
- group: start
  title: ''
  type: Login
  url: https://www.interactivebrokers.com/sso/Login
created: '2026-03-21'
description: Interactive Brokers is an online brokerage firm providing trading access to stocks, options, futures, currencies, bonds, and funds across 150+ markets worldwide. IBKR offers comprehensive REST APIs that enable developers and traders to programmatically access trading, portfolio management, market data, and account management capabilities through the IBKR Web API and Client Portal API.
finops:
- name: Interactive Brokers Finops
  service_category: API
  slug: interactive-brokers-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/interactive-brokers.png
layout: provider
modified: '2026-05-29'
name: Interactive Brokers
nav: Providers
network: true
overview: 'Interactive Brokers publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contracts API, Market Data API, and 3 more. Tagged areas include Brokerage, Market Data, Orders, Portfolio, and Trading.


  The Interactive Brokers catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Interactive Brokers'' developer surface includes authentication, developer portal, documentation, GitHub presence, and 6 more developer resources.'
plans:
- name: Interactive Brokers Plans Pricing
  plan_count: 3
  slug: interactive-brokers-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Interactive Brokers Rate Limits
  slug: interactive-brokers-rate-limits
rules:
- name: Interactive Brokers API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: interactive-brokers-asyncapi-spectral-rules
scopes:
- name: Interactive Brokers Scopes
  scope_count: 18
  slug: interactive-brokers-scopes
  summary_line: 18 scopes · authorizationCode
score:
  band: developing
  composite: 48.4
  delta: -3.9
  facets:
    commercial_clarity: 52.6
    contract_quality: 61.9
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 52.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 46.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/interactive-brokers/refs/heads/main/screenshots/interactive-brokers-2026-06-20T183445.png
security:
- kind: authentication
  name: Interactive Brokers Authentication
  slug: interactive-brokers-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Interactive Brokers Domain Security
  slug: interactive-brokers-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: interactive-brokers
tags:
- Brokerage
- Market Data
- Orders
- Portfolio
- Trading
website: https://www.interactivebrokers.com/
---
