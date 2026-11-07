---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 64.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Alpaca Agentic Access
  operation_count: 119
  slug: alpaca-agentic-access
  summary_line: 119 operations · 39 acting
api_count: 9
apis:
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Accounts API from Alpaca — 14 operation(s) for accounts.
  name: Alpaca Accounts API
  slug: alpaca-accounts-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Assets API from Alpaca — 2 operation(s) for assets.
  name: Alpaca Assets API
  slug: alpaca-assets-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Calendar API from Alpaca — 2 operation(s) for calendar.
  name: Alpaca Calendar API
  slug: alpaca-calendar-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Clock API from Alpaca — 2 operation(s) for clock.
  name: Alpaca Clock API
  slug: alpaca-clock-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Corporate Actions API from Alpaca — 1 operation(s) for corporate actions.
  name: Alpaca Corporate Actions API
  slug: alpaca-corporate-actions-api
- baseURL: https://data.alpaca.markets
  baseurl_source: declared
  description: The Crypto Pricing Data API API from Alpaca — 17 operation(s) for crypto pricing data api.
  name: Alpaca Crypto Pricing Data API
  slug: alpaca-crypto-pricing-data-api-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Documents API from Alpaca — 3 operation(s) for documents.
  name: Alpaca Documents API
  slug: alpaca-documents-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Events API from Alpaca — 4 operation(s) for events.
  name: Alpaca Events API
  slug: alpaca-events-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Funding API from Alpaca — 7 operation(s) for funding.
  name: Alpaca Funding API
  slug: alpaca-funding-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Journals API from Alpaca — 4 operation(s) for journals.
  name: Alpaca Journals API
  slug: alpaca-journals-api
- baseURL: https://data.alpaca.markets
  baseurl_source: declared
  description: The Logo API from Alpaca — 1 operation(s) for logo.
  name: Alpaca Logo API
  slug: alpaca-logo-api
- baseURL: https://data.alpaca.markets
  baseurl_source: declared
  description: The News API from Alpaca — 1 operation(s) for news.
  name: Alpaca News API
  slug: alpaca-news-api
- baseURL: https://data.alpaca.markets
  baseurl_source: declared
  description: The Screener API from Alpaca — 1 operation(s) for screener.
  name: Alpaca Screener API
  slug: alpaca-screener-api
- baseURL: https://data.alpaca.markets
  baseurl_source: declared
  description: The Stock Pricing Data API API from Alpaca — 16 operation(s) for stock pricing data api.
  name: Alpaca Stock Pricing Data API
  slug: alpaca-stock-pricing-data-api-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Watchlist API from Alpaca — 2 operation(s) for watchlist.
  name: Alpaca Watchlist API
  slug: alpaca-watchlist-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The OAuth API from Alpaca — 3 operation(s) for oauth.
  name: Alpaca O Auth API
  slug: alpaca-oauth-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: Endpoints for initiating and tracking ACATS transfers. Use the ACATS endpoints to create transfers and query their current state, and the [Admin Action Events Stream](#operation/subscribeToAdminAction
  name: Alpaca ACATS API
  slug: alpaca-acats-api
- baseURL: https://paper-api.alpaca.markets
  baseurl_source: declared
  description: The Account Activities API from Alpaca — 2 operation(s) for account activities.
  name: Alpaca Account Activities API
  slug: alpaca-account-activities-api
- baseURL: https://paper-api.alpaca.markets
  baseurl_source: declared
  description: The Account Configurations API from Alpaca — 1 operation(s) for account configurations.
  name: Alpaca Account Configurations API
  slug: alpaca-account-configurations-api
- baseURL: https://broker-api.eu.alpaca.markets
  baseurl_source: declared
  description: The Agreements API from Alpaca — 1 operation(s) for agreements.
  name: Alpaca Agreements API
  slug: alpaca-agreements-api
- baseURL: https://ext-api.giftcity.in.alpaca.markets
  baseurl_source: declared
  description: The Blocked Symbols API from Alpaca — 1 operation(s) for blocked symbols.
  name: Alpaca Blocked Symbols API
  slug: alpaca-blocked-symbols-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Cash Interest API from Alpaca — 2 operation(s) for cash interest.
  name: Alpaca Cash Interest API
  slug: alpaca-cash-interest-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Country Info API from Alpaca — 1 operation(s) for country info.
  name: Alpaca Country Info API
  slug: alpaca-country-info-api
- baseURL: https://data.alpaca.markets
  baseurl_source: declared
  description: Endpoints for cryptocurrencies.
  name: Alpaca Crypto API
  slug: alpaca-crypto-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Crypto Funding API from Alpaca — 16 operation(s) for crypto funding.
  name: Alpaca Crypto Funding API
  slug: alpaca-crypto-funding-api
- baseURL: https://data.alpaca.markets
  baseurl_source: declared
  description: Endpoints for fixed income data.
  name: Alpaca Fixed income API
  slug: alpaca-fixed-income-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The FPSL Program API from Alpaca — 3 operation(s) for fpsl program.
  name: Alpaca FPSL Program API
  slug: alpaca-fpsl-program-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Funding Wallets API from Alpaca — 8 operation(s) for funding wallets.
  name: Alpaca Funding Wallets API
  slug: alpaca-funding-wallets-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Instant Funding API from Alpaca — 7 operation(s) for instant funding.
  name: Alpaca Instant Funding API
  slug: alpaca-instant-funding-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: Endpoints for discovering and tracking IPO (Initial Public Offering) lifecycle data. Use [`GET /v1/ipos`](#operation/listIPOOfferings) and [`GET /v1/ipos/{offering_reference}`](#operation/getIPOOfferi
  name: Alpaca IPO API
  slug: alpaca-ipo-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The IRA API from Alpaca — 1 operation(s) for ira.
  name: Alpaca IRA API
  slug: alpaca-ira-api
- baseURL: https://broker-api.eu.alpaca.markets
  baseurl_source: declared
  description: The KYC API from Alpaca — 3 operation(s) for kyc.
  name: Alpaca KYC API
  slug: alpaca-kyc-api
- baseURL: https://paper-api.alpaca.markets
  baseurl_source: declared
  description: Endpoints for locate requests and quotes.
  name: Alpaca Locates API
  slug: alpaca-locates-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Logos API from Alpaca — 1 operation(s) for logos.
  name: Alpaca Logos API
  slug: alpaca-logos-api
- baseURL: https://authx.eu.alpaca.markets/v1
  baseurl_source: declared
  description: OAuth2 endpoints
  name: Alpaca O Auth2 API
  slug: alpaca-oauth2-api
- baseURL: https://data.alpaca.markets
  baseurl_source: declared
  description: Endpoints for option data.
  name: Alpaca Option API
  slug: alpaca-option-api
- baseURL: https://paper-api.alpaca.markets
  baseurl_source: declared
  description: The Orders API from Alpaca — 3 operation(s) for orders.
  name: Alpaca Orders API
  slug: alpaca-orders-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Portfolio History API from Alpaca — 2 operation(s) for portfolio history.
  name: Alpaca Portfolio History API
  slug: alpaca-portfolio-history-api
- baseURL: https://paper-api.alpaca.markets
  baseurl_source: declared
  description: The Positions API from Alpaca — 4 operation(s) for positions.
  name: Alpaca Positions API
  slug: alpaca-positions-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Rebalancing API from Alpaca — 6 operation(s) for rebalancing.
  name: Alpaca Rebalancing API
  slug: alpaca-rebalancing-api
- baseURL: https://broker-api.eu.alpaca.markets
  baseurl_source: declared
  description: The Reporting API from Alpaca — 3 operation(s) for reporting.
  name: Alpaca Reporting API
  slug: alpaca-reporting-api
- baseURL: https://data.alpaca.markets
  baseurl_source: declared
  description: Endpoints for stocks.
  name: Alpaca Stock API
  slug: alpaca-stock-api
- baseURL: https://broker-api.alpaca.markets
  baseurl_source: declared
  description: The Tokenization API from Alpaca — 11 operation(s) for tokenization.
  name: Alpaca Tokenization API
  slug: alpaca-tokenization-api
- baseURL: https://broker-api.eu.alpaca.markets
  baseurl_source: declared
  description: The Trading API from Alpaca — 12 operation(s) for trading.
  name: Alpaca Trading API
  slug: alpaca-trading-api
- baseURL: https://paper-api.alpaca.markets
  baseurl_source: declared
  description: The Watchlists API from Alpaca — 4 operation(s) for watchlists.
  name: Alpaca Watchlists API
  slug: alpaca-watchlists-api
artifact_total: 171
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
  href: https://artifacts.apis.io/alpaca/overlays/alpaca-trading-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/alpaca-trading-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/alpaca/rules/alpaca-rules.yml
  title: ''
  type: Spectral
  url: rules/alpaca-rules.yml
- group: design
  href: https://artifacts.apis.io/alpaca/rules/alpaca-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/alpaca-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/alpaca/json-ld/alpaca-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/alpaca-context.jsonld
- group: design
  href: https://artifacts.apis.io/alpaca/vocabulary/alpaca-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/alpaca-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/alpaca/hosts/alpaca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alpaca-hosts.yml
- group: build
  href: https://artifacts.apis.io/alpaca/integrations/alpaca-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/alpaca-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/alpaca/vendors/alpaca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alpaca-vendors.yml
- group: auth
  href: https://artifacts.apis.io/alpaca/security/alpaca-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/alpaca-trust-center.yml
- group: other
  href: https://artifacts.apis.io/alpaca/capabilities/alpaca-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/alpaca-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/alpaca/overlays/alpaca-oauth-api-overlay.yaml
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
  href: https://artifacts.apis.io/alpaca/agentic-access/alpaca-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/alpaca-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/alpaca/security/alpaca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alpaca-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/alpaca/authentication/alpaca-authentication.yml
  title: ''
  type: Authentication
  url: authentication/alpaca-authentication.yml
- group: build
  href: https://artifacts.apis.io/alpaca/packages/alpaca-packages.yml
  title: ''
  type: Packages
  url: packages/alpaca-packages.yml
- group: build
  href: https://artifacts.apis.io/alpaca/packages/alpaca-packages.yml
  title: ''
  type: SDKs
  url: packages/alpaca-packages.yml
- group: agent
  href: https://artifacts.apis.io/alpaca/well-known/alpaca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/alpaca-well-known.yml
- group: agent
  href: https://artifacts.apis.io/alpaca/mcp/alpaca-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/alpaca-mcp.yml
- group: build
  href: https://artifacts.apis.io/alpaca/mcp/alpaca-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/alpaca-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/alpaca/llms/alpaca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/alpaca-llms.txt
- group: agent
  href: https://artifacts.apis.io/alpaca/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/alpaca/sandbox/alpaca-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/alpaca-sandbox.yml
- group: design
  href: https://artifacts.apis.io/alpaca/conventions/alpaca-conventions.yml
  title: ''
  type: Conventions
  url: conventions/alpaca-conventions.yml
- group: design
  href: https://artifacts.apis.io/alpaca/conventions/alpaca-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/alpaca-conventions.yml
- group: operate
  href: https://artifacts.apis.io/alpaca/changelog/alpaca-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/alpaca-changelog.yml
- group: build
  href: https://artifacts.apis.io/alpaca/cli/alpaca-cli.yml
  title: ''
  type: CLI
  url: cli/alpaca-cli.yml
- group: auth
  href: https://artifacts.apis.io/alpaca/scopes/alpaca-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/alpaca-scopes.yml
- group: design
  href: https://artifacts.apis.io/alpaca/errors/alpaca-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/alpaca-problem-types.yml
- group: design
  href: https://artifacts.apis.io/alpaca/lifecycle/alpaca-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/alpaca-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/alpaca/lifecycle/alpaca-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/alpaca-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/alpaca/conformance/alpaca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alpaca-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://alpaca.markets/security
- group: auth
  href: https://artifacts.apis.io/alpaca/security/alpaca-vulnerability-disclosure.yml
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
  href: https://artifacts.apis.io/alpaca/data-model/alpaca-data-model.yml
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
  url: https://docs.alpaca.markets/us/reference
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
  url: https://files.alpaca.markets/disclosures/library/TermsAndConditions.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://s3.amazonaws.com/files.alpaca.markets/disclosures/PrivacyPolicy.pdf
- group: commercial
  href: https://artifacts.apis.io/alpaca/plans/alpaca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/alpaca-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/alpaca/rate-limits/alpaca-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/alpaca-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/alpaca/finops/alpaca-finops.yml
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
  url: https://alpaca.markets/blog/
- group: other
  title: ''
  type: RSSFeed
  url: https://alpaca.markets/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alpacahq
- group: operate
  title: ''
  type: Forum
  url: https://forum.alpaca.markets/
- group: company
  title: ''
  type: Newsroom
  url: https://alpaca.markets/newsroom
- group: operate
  title: ''
  type: ChangeLogPage
  url: https://docs.alpaca.markets/us/changelog
- group: docs
  title: ''
  type: SDKDocumentation
  url: https://docs.alpaca.markets/docs/sdks-and-tools
- group: start
  title: ''
  type: Login
  url: https://broker-app.alpaca.markets/login
- group: auth
  title: ''
  type: Disclosures
  url: https://alpaca.markets/disclosures
- group: company
  title: ''
  type: AboutUs
  url: https://alpaca.markets/about-us
- group: operate
  title: ''
  type: Contact
  url: https://alpaca.markets/contact
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AlpacaHQ
created: '2026-05-08'
description: Alpaca is an API-first commission-free stock and crypto trading broker offering trading, market data, options, and broker-as-a-service APIs. Alpaca publishes its OpenAPI specifications publicly via the alpacahq/alpaca-docs GitHub repository, with separate specs for Trading, Broker, Market Data, and OAuth.
finops:
- has_sources: true
  method: derived
  name: Alpaca Finops
  primary_unit: subscription
  service_category: ''
  slug: alpaca-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alpaca.png
json_schemas:
- name: AccountCreationRequest
  property_count: 22
  slug: alpaca-account-creation-request
- name: AccountExtended
  property_count: 33
  slug: alpaca-account-extended
- name: Account
  property_count: 34
  slug: alpaca-account
- name: AccountStatusEvent
  property_count: 8
  slug: alpaca-account-status-event
- name: ACHRelationship
  property_count: 10
  slug: alpaca-achrelationship
- name: Announcement
  property_count: 15
  slug: alpaca-announcement
- name: Asset
  property_count: 14
  slug: alpaca-asset
- name: Assets
  property_count: 19
  slug: alpaca-assets
- name: AuthorizeOAuthTokenResponse
  property_count: 4
  slug: alpaca-authorize-oauth-token-response
- name: Bank
  property_count: 14
  slug: alpaca-bank
- name: BarsResponse
  property_count: 3
  slug: alpaca-bars-response
- name: BatchJournalRequest
  property_count: 4
  slug: alpaca-batch-journal-request
- name: BatchJournalResponse
  property_count: 7
  slug: alpaca-batch-journal-response
- name: Calendar
  property_count: 5
  slug: alpaca-calendar
- name: Clock
  property_count: 4
  slug: alpaca-clock
- name: corporate_action_event
  property_count: 0
  slug: alpaca-corporate-action-event
- name: corporate_actions_resp
  property_count: 2
  slug: alpaca-corporate-actions-resp
- name: CreateACHRelationshipRequest
  property_count: 6
  slug: alpaca-create-achrelationship-request
- name: CreateJournalRequest
  property_count: 12
  slug: alpaca-create-journal-request
- name: CreateOrderRequest
  property_count: 18
  slug: alpaca-create-order-request
- name: CreateTransferRequest
  property_count: 7
  slug: alpaca-create-transfer-request
- name: CreateWatchlistRequest
  property_count: 2
  slug: alpaca-create-watchlist-request
- name: Document
  property_count: 0
  slug: alpaca-document
- name: fixed_income_latest_prices_resp
  property_count: 1
  slug: alpaca-fixed-income-latest-prices-resp
- name: fixed_income_latest_quotes_resp
  property_count: 1
  slug: alpaca-fixed-income-latest-quotes-resp
- name: GetNewsResponse
  property_count: 2
  slug: alpaca-get-news-response
- name: IPOEvent
  property_count: 8
  slug: alpaca-ipoevent
- name: IssueOAuthTokenResponse
  property_count: 3
  slug: alpaca-issue-oauth-token-response
- name: Journal
  property_count: 6
  slug: alpaca-journal
- name: JournalStatusEvent
  property_count: 6
  slug: alpaca-journal-status-event
- name: MarketMovers
  property_count: 4
  slug: alpaca-market-movers-response
- name: most_actives_resp
  property_count: 2
  slug: alpaca-most-actives-resp
- name: movers_resp
  property_count: 4
  slug: alpaca-movers-resp
- name: MultiBarsResponse
  property_count: 2
  slug: alpaca-multi-bars-response
- name: MultiQuotesReponse
  property_count: 2
  slug: alpaca-multi-quotes-reponse
- name: MultiSnapshotResponse
  property_count: 0
  slug: alpaca-multi-snapshot-response
- name: MultiTradesResponse
  property_count: 2
  slug: alpaca-multi-trades-response
- name: OathClientResponse
  property_count: 9
  slug: alpaca-oath-client-response
- name: OAuthTokenRequest
  property_count: 5
  slug: alpaca-oauth-token-request
- name: OptionContract
  property_count: 20
  slug: alpaca-option-contract
- name: Order
  property_count: 37
  slug: alpaca-order
- name: Position
  property_count: 22
  slug: alpaca-position
- name: Snapshot
  property_count: 5
  slug: alpaca-snapshot
- name: stock_auctions_resp
  property_count: 3
  slug: alpaca-stock-auctions-resp
- name: token_request
  property_count: 5
  slug: alpaca-token-request
- name: token_response
  property_count: 4
  slug: alpaca-token-response
- name: TradeAccount
  property_count: 49
  slug: alpaca-trade-account
- name: TradeUpdateEvent
  property_count: 7
  slug: alpaca-trade-update-event
- name: TradeUpdateEvent
  property_count: 16
  slug: alpaca-trade-update-event-v2
- name: Transfer
  property_count: 15
  slug: alpaca-transfer
- name: TransferStatusEvent
  property_count: 6
  slug: alpaca-transfer-status-event
- name: Watchlist
  property_count: 6
  slug: alpaca-watchlist
jsonld:
- class_count: 120
  name: Alpaca Context
  property_count: 385
  slug: alpaca-context
layout: provider
mcp_servers:
- description: Remote MCP server at broker-api.alpaca.markets requiring OAuth; 69 tools listed.
  name: Alpaca MCP Server
  slug: alpaca-mcp-yml
modified: '2026-11-05'
name: Alpaca
nav: Providers
network: true
overview: 'Alpaca publishes 45 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Assets API, Calendar API, and 42 more. Tagged areas include Fintech, Trading, Stocks, Cryptocurrency, and Brokerage.


  The Alpaca catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Alpaca''s developer surface includes authentication, sandbox, changelog, CLI, API reference, getting-started guide, support, and 60 more developer resources.'
plans:
- name: Alpaca Plans Pricing
  plan_count: 2
  slug: alpaca-plans-pricing
- name: Alpaca Price Estimates
  plan_count: 0
  slug: alpaca-price-estimates
random_paper: 10
rate_limits:
- limit_count: 12
  name: Alpaca Rate Limits
  slug: alpaca-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Alpaca — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: alpaca-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Alpaca API Rules
  rule_count: 65
  severity_counts:
    error: 46
    hint: 0
    info: 2
    warn: 17
  slug: alpaca-rules
scopes:
- name: Alpaca Scopes
  scope_count: 4
  slug: alpaca-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 69.9
  coverage:
    artifact_dirs: 40
    catalog_earned: 88.8
    catalog_earned_first_party: 20.0
    catalog_gap: 26.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 11.8
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 73.0
    developer_ergonomics: 75.0
    discoverability: 81.7
    operational_transparency: 86.8
  previous_composite: 58.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 3.8
      total: 53
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
    score: 40.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/alpaca/alpaca-2026-06-20T171542.png
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
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 12
skills:
- name: alpaca-broker-account-onboarding
  slug: alpaca-broker-api-account-onboarding
- name: alpaca-broker-funding-transfers
  slug: alpaca-broker-api-funding-transfers
- name: alpaca-broker-integration
  slug: alpaca-broker-api-integration
- name: alpaca-broker-journals
  slug: alpaca-broker-api-journals
- name: alpaca-broker-market-data
  slug: alpaca-broker-api-market-data
- name: alpaca-broker-money-precision
  slug: alpaca-broker-api-money-precision
- name: alpaca-broker-rate-limits-resilience
  slug: alpaca-broker-api-rate-limits-resilience
- name: alpaca-broker-reconciliation-idempotency
  slug: alpaca-broker-api-reconciliation-idempotency
- name: alpaca-broker-sse-events
  slug: alpaca-broker-api-sse-events
- name: alpaca-broker-trading-orders
  slug: alpaca-broker-api-trading-orders
- name: alpaca-trading-backtest
  slug: alpaca-trading-api-backtest
- name: alpaca-trading-order-lifecycle
  slug: alpaca-trading-api-order-lifecycle
slug: alpaca
tags:
- Fintech
- Trading
- Stocks
- Cryptocurrency
- Brokerage
- Market Data
- Options
- Real-Time
- Investing
- Financial Services
website: https://www.alpaca.markets/
---
