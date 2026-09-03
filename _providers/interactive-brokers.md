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
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Interactive Brokers Agentic Access
  operation_count: 9
  slug: interactive-brokers-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- description: The Interactive Brokers Client Portal API is a REST API accessed through a locally running Java gateway that routes authenticated requests to IBKR systems. It provides a lightweight interface for trad
  name: Interactive Brokers Client Portal API
  slug: client-portal-api
- baseURL: https://localhost:5000/v1/api
  baseurl_source: declared
  description: Account information and management
  name: Interactive Brokers Accounts API
  slug: interactive-brokers-accounts-api
- baseURL: https://localhost:5000/v1/api
  baseurl_source: declared
  description: Contract and instrument search
  name: Interactive Brokers Contracts API
  slug: interactive-brokers-contracts-api
- baseURL: https://localhost:5000/v1/api
  baseurl_source: declared
  description: Real-time and historical market data
  name: Interactive Brokers Market Data API
  slug: interactive-brokers-market-data-api
- baseURL: https://localhost:5000/v1/api
  baseurl_source: declared
  description: Order placement and management
  name: Interactive Brokers Orders API
  slug: interactive-brokers-orders-api
- baseURL: https://localhost:5000/v1/api
  baseurl_source: declared
  description: Portfolio positions and account summaries
  name: Interactive Brokers Portfolio API
  slug: interactive-brokers-portfolio-api
- baseURL: https://localhost:5000/v1/api
  baseurl_source: declared
  description: Authentication and session management
  name: Interactive Brokers Sessions API
  slug: interactive-brokers-sessions-api
artifact_total: 24
asyncapis:
- description: 'AsyncAPI definition for the Interactive Brokers (IBKR) Client Portal Web API streaming WebSocket endpoint. The Client Portal API exposes a single WebSocket endpoint at `/v1/api/ws` over which clients '
  name: Interactive Brokers Client Portal API WebSocket
  slug: interactive-brokers-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Interactive Brokers Web Accounts API
  slug: open-interactive-brokers-accounts-api
- collection_type: open
  name: Interactive Brokers Web Accounts Contracts API
  slug: open-interactive-brokers-contracts-api
- collection_type: open
  name: Interactive Brokers Web Accounts Market Data API
  slug: open-interactive-brokers-market-data-api
- collection_type: open
  name: Interactive Brokers Web Accounts Orders API
  slug: open-interactive-brokers-orders-api
- collection_type: open
  name: Interactive Brokers Web Accounts Portfolio API
  slug: open-interactive-brokers-portfolio-api
- collection_type: open
  name: Interactive Brokers Web Accounts Sessions API
  slug: open-interactive-brokers-sessions-api
- collection_type: open
  name: Interactive Brokers Web API
  slug: open-interactive-brokers-web-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/interactive-brokers-capability-edges.yml
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
overview: 'Interactive Brokers publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contracts API, Market Data API, and 3 more. Tagged areas include Brokerage, Market Data, Order, Portfolio, and Trading.


  The Interactive Brokers catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Interactive Brokers'' developer surface includes authentication, developer portal, documentation, GitHub presence, and 7 more developer resources.'
plans:
- name: Interactive Brokers Plans Pricing
  plan_count: 3
  slug: interactive-brokers-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Interactive Brokers Rate Limits
  slug: interactive-brokers-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Interactive Brokers API Rules
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
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 13
    catalog_gap: 69.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 13.6
    contract_quality: 53.7
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 13.2
  previous_composite: 35.1
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Order
- Portfolio
- Trading
website: https://www.interactivebrokers.com/
---
