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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.2
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Alpaca Agentic Access
  operation_count: 119
  slug: alpaca-agentic-access
  summary_line: 119 operations · 39 acting
api_count: 2
apis:
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Alpaca Trading API enables commission-free trading of US-listed equities, options, and crypto. It exposes endpoints for orders, positions, account information, watchlists, calendar, clock, and ass
  name: Alpaca Trading API
  slug: trading-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Accounts API from Alpaca — 14 operation(s) for accounts.
  name: Alpaca Accounts API
  slug: alpaca-accounts-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Assets API from Alpaca — 2 operation(s) for assets.
  name: Alpaca Assets API
  slug: alpaca-assets-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Calendar API from Alpaca — 2 operation(s) for calendar.
  name: Alpaca Calendar API
  slug: alpaca-calendar-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Clock API from Alpaca — 2 operation(s) for clock.
  name: Alpaca Clock API
  slug: alpaca-clock-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Corporate Actions API from Alpaca — 1 operation(s) for corporate actions.
  name: Alpaca Corporate Actions API
  slug: alpaca-corporate-actions-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Crypto Pricing Data API API from Alpaca — 17 operation(s) for crypto pricing data api.
  name: Alpaca Crypto Pricing Data API
  slug: alpaca-crypto-pricing-data-api-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Documents API from Alpaca — 3 operation(s) for documents.
  name: Alpaca Documents API
  slug: alpaca-documents-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Events API from Alpaca — 4 operation(s) for events.
  name: Alpaca Events API
  slug: alpaca-events-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Funding API from Alpaca — 7 operation(s) for funding.
  name: Alpaca Funding API
  slug: alpaca-funding-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Journals API from Alpaca — 4 operation(s) for journals.
  name: Alpaca Journals API
  slug: alpaca-journals-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Logo API from Alpaca — 1 operation(s) for logo.
  name: Alpaca Logo API
  slug: alpaca-logo-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The News API from Alpaca — 1 operation(s) for news.
  name: Alpaca News API
  slug: alpaca-news-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Screener API from Alpaca — 1 operation(s) for screener.
  name: Alpaca Screener API
  slug: alpaca-screener-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Stock Pricing Data API API from Alpaca — 16 operation(s) for stock pricing data api.
  name: Alpaca Stock Pricing Data API
  slug: alpaca-stock-pricing-data-api-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The Watchlist API from Alpaca — 2 operation(s) for watchlist.
  name: Alpaca Watchlist API
  slug: alpaca-watchlist-api
- baseURL: https://api.alpaca.markets/v2
  baseurl_source: declared
  description: The OAuth API from Alpaca — 3 operation(s) for oauth.
  name: Alpaca O Auth API
  slug: alpaca-oauth-api
artifact_total: 77
asyncapis:
- description: AsyncAPI 2.6 description of Alpaca's public WebSocket streaming APIs. Covers real-time stock market data (IEX / SIP / delayed SIP / BOATS), real-time crypto market data (US and Global), real-time news
  name: Alpaca WebSocket Streaming APIs
  slug: alpaca-asyncapi
collections:
- collection_type: postman
  name: Broker Account Activities API
  slug: postman-alpaca-account-activities-api
- collection_type: postman
  name: Broker Account Activities Accounts API
  slug: postman-alpaca-accounts-api
- collection_type: postman
  name: Broker Account Activities Assets API
  slug: postman-alpaca-assets-api
- collection_type: postman
  name: Broker Account Activities Calendar API
  slug: postman-alpaca-calendar-api
- collection_type: postman
  name: Broker Account Activities Clock API
  slug: postman-alpaca-clock-api
- collection_type: postman
  name: Broker Account Activities Corporate Actions API
  slug: postman-alpaca-corporate-actions-api
- collection_type: postman
  name: Broker Account Activities Crypto Pricing Data API API
  slug: postman-alpaca-crypto-pricing-data-api-api
- collection_type: postman
  name: Broker Account Activities Documents API
  slug: postman-alpaca-documents-api
- collection_type: postman
  name: Broker Account Activities Events API
  slug: postman-alpaca-events-api
- collection_type: postman
  name: Broker Account Activities Funding API
  slug: postman-alpaca-funding-api
- collection_type: postman
  name: Broker Account Activities Journals API
  slug: postman-alpaca-journals-api
- collection_type: postman
  name: Broker Account Activities Logo API
  slug: postman-alpaca-logo-api
- collection_type: postman
  name: Broker Account Activities News API
  slug: postman-alpaca-news-api
- collection_type: postman
  name: Broker Account Activities OAuth API
  slug: postman-alpaca-oauth-api
- collection_type: postman
  name: Broker Account Activities Orders API
  slug: postman-alpaca-orders-api
- collection_type: postman
  name: Broker Account Activities Portfolio History API
  slug: postman-alpaca-portfolio-history-api
- collection_type: postman
  name: Broker Account Activities Positions API
  slug: postman-alpaca-positions-api
- collection_type: postman
  name: Broker Account Activities Screener API
  slug: postman-alpaca-screener-api
- collection_type: postman
  name: Broker Account Activities Stock Pricing Data API API
  slug: postman-alpaca-stock-pricing-data-api-api
- collection_type: postman
  name: Broker Account Activities Trading API
  slug: postman-alpaca-trading-api
- collection_type: postman
  name: Broker Account Activities Watchlist API
  slug: postman-alpaca-watchlist-api
- collection_type: postman
  name: Broker Account Activities Watchlists API
  slug: postman-alpaca-watchlists-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Broker Account Activities API
  slug: open-alpaca-account-activities-api
- collection_type: open
  name: Broker Account Activities Account Configurations API
  slug: open-alpaca-account-configurations-api
- collection_type: open
  name: Broker Account Activities Accounts API
  slug: open-alpaca-accounts-api
- collection_type: open
  name: Broker Account Activities Assets API
  slug: open-alpaca-assets-api
- collection_type: open
  name: Broker API
  slug: open-alpaca-broker-api
- collection_type: open
  name: Broker Account Activities Calendar API
  slug: open-alpaca-calendar-api
- collection_type: open
  name: Broker Account Activities Clock API
  slug: open-alpaca-clock-api
- collection_type: open
  name: Broker Account Activities Corporate Actions API
  slug: open-alpaca-corporate-actions-api
- collection_type: open
  name: Broker Account Activities Crypto Pricing Data API API
  slug: open-alpaca-crypto-pricing-data-api-api
- collection_type: open
  name: Market Data API
  slug: open-alpaca-data-api
- collection_type: open
  name: Broker Account Activities Documents API
  slug: open-alpaca-documents-api
- collection_type: open
  name: Broker Account Activities Events API
  slug: open-alpaca-events-api
- collection_type: open
  name: Broker Account Activities Funding API
  slug: open-alpaca-funding-api
- collection_type: open
  name: Broker Account Activities Journals API
  slug: open-alpaca-journals-api
- collection_type: open
  name: Broker Account Activities Logo API
  slug: open-alpaca-logo-api
- collection_type: open
  name: Broker Account Activities News API
  slug: open-alpaca-news-api
- collection_type: open
  name: Broker Account Activities OAuth API
  slug: open-alpaca-oauth-api
- collection_type: open
  name: Broker Account Activities Orders API
  slug: open-alpaca-orders-api
- collection_type: open
  name: Broker Account Activities Portfolio History API
  slug: open-alpaca-portfolio-history-api
- collection_type: open
  name: Broker Account Activities Positions API
  slug: open-alpaca-positions-api
- collection_type: open
  name: Broker Account Activities Screener API
  slug: open-alpaca-screener-api
- collection_type: open
  name: Broker Account Activities Stock Pricing Data API API
  slug: open-alpaca-stock-pricing-data-api-api
- collection_type: open
  name: Broker Account Activities Trading API
  slug: open-alpaca-trading-api
- collection_type: open
  name: Broker Account Activities Watchlist API
  slug: open-alpaca-watchlist-api
- collection_type: open
  name: Broker Account Activities Watchlists API
  slug: open-alpaca-watchlists-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/overlays/alpaca-oauth-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/alpaca-oauth-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.alpaca.markets/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/alpaca/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/agentic-access/alpaca-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alpaca-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/security/alpaca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpaca-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/authentication/alpaca-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alpaca-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/packages/alpaca-packages.yml
  title: ''
  type: Packages
  url: packages/alpaca-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/packages/alpaca-packages.yml
  title: ''
  type: SDKs
  url: packages/alpaca-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/well-known/alpaca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alpaca-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/mcp/alpaca-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alpaca-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/mcp/alpaca-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/alpaca-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/llms/alpaca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alpaca-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/sandbox/alpaca-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/alpaca-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/conventions/alpaca-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alpaca-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/conventions/alpaca-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/alpaca-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/changelog/alpaca-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alpaca-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/cli/alpaca-cli.yml
  title: ''
  type: CLI
  url: cli/alpaca-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/scopes/alpaca-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/alpaca-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/errors/alpaca-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alpaca-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/lifecycle/alpaca-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alpaca-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/lifecycle/alpaca-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/alpaca-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/conformance/alpaca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alpaca-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://alpaca.markets/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/security/alpaca-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/alpaca-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://alpaca.markets/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.alpaca.markets/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/data-model/alpaca-data-model.yml
  title: ''
  type: DataModel
  url: data-model/alpaca-data-model.yml
- group: build
  title: ''
  type: Postman
  url: https://github.com/alpacahq/alpaca-postman
- group: docs
  title: ''
  type: APIReference
  url: https://docs.alpaca.markets/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alpaca.markets/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://alpaca.markets/support
- group: start
  title: ''
  type: SignUp
  url: https://app.alpaca.markets/signup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alpacamarkets
- group: start
  title: ''
  type: Portal
  url: https://alpaca.markets/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alpaca.markets/
- group: commercial
  title: ''
  type: Pricing
  url: https://alpaca.markets/data
- group: build
  title: ''
  type: GitHub
  url: https://github.com/alpacahq
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alpaca.markets/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alpaca.markets/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alpaca.markets/privacy
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/plans/alpaca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alpaca-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/rate-limits/alpaca-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/alpaca-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/finops/alpaca-finops.yml
  title: ''
  type: FinOps
  url: finops/alpaca-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.alpaca.markets/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://alpaca.markets/blog/feed/
created: '2026-05-08'
description: Alpaca is an API-first commission-free stock and crypto trading broker offering trading, market data, options, and broker-as-a-service APIs. Alpaca publishes its OpenAPI specifications publicly via the alpacahq/alpaca-docs GitHub repository, with separate specs for Trading, Broker, Market Data, and OAuth.
finops:
- name: Alpaca Finops
  service_category: Fintech
  slug: alpaca-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alpaca.png
layout: provider
mcp_servers:
- description: ''
  name: Alpaca MCP Server
  slug: alpaca-mcp-server
modified: '2026-09-16'
name: Alpaca
nav: Providers
network: true
overview: 'Alpaca publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Trading API, Accounts API, Assets API, and 14 more. Tagged areas include Fintech, Trading, Stocks, Crypto, and Brokerage.


  The Alpaca catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Alpaca''s developer surface includes authentication, sandbox, changelog, CLI, API reference, getting-started guide, support, and 39 more developer resources.'
plans:
- name: Alpaca Plans Pricing
  plan_count: 3
  slug: alpaca-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Alpaca Rate Limits
  slug: alpaca-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Alpaca API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: alpaca-asyncapi-spectral-rules
scopes:
- name: Alpaca Scopes
  scope_count: 4
  slug: alpaca-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 59.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    contract_governance: 31.8
    contract_quality: 65.4
    developer_ergonomics: 53.6
    discoverability: 75.9
    operational_transparency: 63.2
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 73.3
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/alpaca/refs/heads/main/screenshots/alpaca-2026-06-20T171542.png
security:
- kind: authentication
  name: Alpaca Authentication
  slug: alpaca-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Alpaca Domain Security
  slug: alpaca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Alpaca Vulnerability Disclosure
  slug: alpaca-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Alpaca Trust Center
  slug: alpaca-trust-center
  summary_line: SOC 2 Type 2, ISO 27001:2022, GDPR, UK ICO Data Protection
slug: alpaca
tags:
- Fintech
- Trading
- Stocks
- Crypto
- Brokerage
- Market Data
- Options
website: https://www.alpaca.markets/
---
