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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 12.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pico-trading-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pico-trading-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pico-trading-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pico-trading-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pico-trading-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pico-trading-scopes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pico-trading-changelog.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.pico.net/products/corvil-analytics/corvil-api-sdk/
- group: company
  title: ''
  type: Website
  url: https://www.pico.net/
- group: start
  title: ''
  type: Portal
  url: https://portal.pico.net/
- group: company
  title: ''
  type: Blog
  url: https://www.pico.net/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/corvil
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/picotrading/
- group: operate
  title: ''
  type: Support
  url: https://www.pico.net/company/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pico.net/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pico.net/privacy-policy
created: '2026-07-21'
description: Pico (pico.net) is a trading-infrastructure and financial market data company - not the creator-CRM company of the same name - providing global exchange connectivity, colocation and managed infrastructure in 55+ data centers, Redline trading software (InRush ticker plant feed handlers and Execution Gateway, acquired 2021), RedlineFeed normalized market data from 230+ venues, and Corvil network and trading analytics (acquired 2019). Market data is delivered to entitled customers via multicast feeds and an embedded InRush software API rather than public HTTP endpoints, and Corvil exposes analytics via a REST API, SDK, and streaming to Kafka, Splunk, and Elastic. Privately held; everything is sales-gated - there is no public developer portal, no self-serve signup, and no public API reference, with product documentation and the Corvil API docs behind the login-gated customer portal at portal.pico.net.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pico-trading.png
layout: provider
modified: '2026-07-22'
name: Pico
nav: Providers
network: true
overview: 'Pico is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Trading, Real-Time, and Low Latency.


  Pico''s developer surface includes authentication, changelog, documentation, developer portal, engineering blog, support, and 10 more developer resources.'
random_paper: 62
scopes:
- name: Pico Trading Scopes
  scope_count: 36
  slug: pico-trading-scopes
  summary_line: 36 scopes · authorizationCode
score:
  band: emerging
  composite: 27.7
  delta: -1.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 29.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pico-trading/refs/heads/main/screenshots/pico-trading-2026-07-22T202550.png
security:
- kind: authentication
  name: Pico Trading Authentication
  slug: pico-trading-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Pico Trading Domain Security
  slug: pico-trading-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pico-trading
tags:
- Financial
- Market Data
- Trading
- Real-Time
- Low Latency
- Feed Handlers
- Order Execution
- Network Analytics
- Exchange Connectivity
website: https://www.pico.net/
---
