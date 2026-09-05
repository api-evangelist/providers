---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  score: 20.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Capital Com Public Api Agentic Access
  operation_count: 27
  slug: capital-com-public-api-agentic-access
  summary_line: 27 operations · 11 acting
api_count: 8
apis:
- description: The Capital.com WebSocket API streams real-time market data, supporting up to 40 concurrent instruments and OHLC candlestick subscriptions for low-latency trading applications.
  name: Capital.com WebSocket API
  slug: capital-com-websocket-api
- baseURL: https://api-capital.backend-capital.com
  baseurl_source: spec
  description: Account information, preferences, and demo top-up.
  name: Capital.com Public API Accounts API
  slug: capital-com-public-api-accounts-api
- baseURL: https://api-capital.backend-capital.com
  baseurl_source: spec
  description: Server time, ping, and encryption-key utility endpoints.
  name: Capital.com Public API General API
  slug: capital-com-public-api-general-api
- baseURL: https://api-capital.backend-capital.com
  baseurl_source: spec
  description: Account activity and transaction history.
  name: Capital.com Public API History API
  slug: capital-com-public-api-history-api
- baseURL: https://api-capital.backend-capital.com
  baseurl_source: spec
  description: Market navigation and instrument lookup.
  name: Capital.com Public API Markets API
  slug: capital-com-public-api-markets-api
- baseURL: https://api-capital.backend-capital.com
  baseurl_source: spec
  description: Operations for opening, updating, and closing trading positions.
  name: Capital.com Public API Positions API
  slug: capital-com-public-api-positions-api
- baseURL: https://api-capital.backend-capital.com
  baseurl_source: spec
  description: Operations for creating, switching, and ending API sessions.
  name: Capital.com Public API Session API
  slug: capital-com-public-api-session-api
- baseURL: https://api-capital.backend-capital.com
  baseurl_source: spec
  description: Operations for managing limit and stop working orders.
  name: Capital.com Public API Working Orders API
  slug: capital-com-public-api-working-orders-api
artifact_total: 26
asyncapis:
- description: Real-time streaming API from Capital.com for market data and OHLC candlestick updates. Clients connect over WebSocket using session tokens (CST and X-SECURITY-TOKEN) obtained from the Capital.com REST
  name: Capital.com WebSocket Streaming API
  slug: capital-com-public-api-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Capital.com REST Accounts API
  slug: open-capital-com-public-api-accounts-api
- collection_type: open
  name: Capital.com REST API
  slug: open-capital-com-public-api-capital-com-rest-api
- collection_type: open
  name: Capital.com REST Accounts General API
  slug: open-capital-com-public-api-general-api
- collection_type: open
  name: Capital.com REST Accounts History API
  slug: open-capital-com-public-api-history-api
- collection_type: open
  name: Capital.com REST Accounts Markets API
  slug: open-capital-com-public-api-markets-api
- collection_type: open
  name: Capital.com REST Accounts Positions API
  slug: open-capital-com-public-api-positions-api
- collection_type: open
  name: Capital.com REST Accounts Session API
  slug: open-capital-com-public-api-session-api
- collection_type: open
  name: Capital.com REST Accounts Working Orders API
  slug: open-capital-com-public-api-working-orders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/capital-com-public-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/capital-com-public-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/capital-com-public-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/capital-com-public-api-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/capital-com-sv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/capitalcom
- group: company
  title: ''
  type: Website
  url: https://capital.com/
- group: docs
  title: ''
  type: Documentation
  url: https://open-api.capital.com
- group: start
  title: ''
  type: Sandbox
  url: https://demo-api-capital.backend-capital.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://capital.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://capital.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://capital.com/help
- group: company
  title: ''
  type: Blog
  url: https://capital.com/news-and-analysis
created: '2024-12-03'
description: Capital.com is a European trading platform offering CFDs across shares, indices, commodities, forex, and cryptocurrencies. The Capital.com Public API provides direct access to the trading engine for automated strategies, giving programmatic control of positions, working orders, account preferences, and historical and streaming market data. A companion WebSocket API streams real-time prices and OHLC candles for up to 40 concurrent instruments.
finops:
- name: Capital Com Public Api Finops
  service_category: API
  slug: capital-com-public-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/capital-com-public-api.png
layout: provider
modified: '2026-05-29'
name: Capital.com Public API
nav: Providers
network: true
overview: 'Capital.com Public API publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Capital.com WebSocket API, Accounts API, General API, and 5 more. Tagged areas include CFD, Commodities, Cryptocurrency, Financial, and Forex.


  The Capital.com Public API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Capital.com Public API''s developer surface includes authentication, documentation, sandbox, support, engineering blog, and 8 more developer resources.'
plans:
- name: Capital Com Public Api Plans Pricing
  plan_count: 3
  slug: capital-com-public-api-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Capital Com Public Api Rate Limits
  slug: capital-com-public-api-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Capital.com Public API API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: capital-com-public-api-asyncapi-spectral-rules
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 48.5
    catalog_earned_first_party: 0.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 63.1
    developer_ergonomics: 25.0
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 10.5
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 40.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/capital-com-public-api/refs/heads/main/screenshots/capital-com-public-api-2026-06-20T173937.png
security:
- kind: authentication
  name: Capital Com Public Api Authentication
  slug: capital-com-public-api-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Capital Com Public Api Domain Security
  slug: capital-com-public-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Capital Com Public Api Vulnerability Disclosure
  slug: capital-com-public-api-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: capital-com-public-api
tags:
- CFD
- Commodities
- Cryptocurrency
- Financial
- Forex
- Indices
- Market Data
- Shares
- Streaming
- Trading
- WebSocket
website: https://capital.com/
---
