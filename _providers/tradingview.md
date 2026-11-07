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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Tradingview Agentic Access
  operation_count: 47
  slug: tradingview-agentic-access
  summary_line: 47 operations · 18 acting
api_count: 1
apis:
- description: Open-source (Apache-2.0) HTML5-canvas financial charting library — the flagship first-party client SDK, distributed on npm as lightweight-charts.
  name: TradingView Lightweight Charts
  slug: tradingview-lightweight-charts
- description: Free, self-hosted Charting Library plus the Datafeed API and the Broker Integration REST API that brokerages implement for in-chart trading.
  name: TradingView Advanced Charts & Broker API
  slug: tradingview-advanced-charts-broker-api
- description: Official remote MCP server (beta) authenticated with OAuth 2.1 against a TradingView account; anonymous calls to the endpoint return 401.
  name: TradingView MCP Server
  slug: tradingview-mcp-server
- baseURL: https://your-rest-implementation.com/api
  baseurl_source: declared
  description: The Account API from TradingView — 21 operation(s) for account.
  name: TradingView Account API
  slug: tradingview-account-api
- baseURL: https://your-rest-implementation.com/api
  baseurl_source: declared
  description: The Authorization API from TradingView — 2 operation(s) for authorization.
  name: TradingView Authorization API
  slug: tradingview-authorization-api
- baseURL: https://your-rest-implementation.com/api
  baseurl_source: declared
  description: The Broker Configuration API from TradingView — 2 operation(s) for broker configuration.
  name: TradingView Broker Configuration API
  slug: tradingview-broker-configuration-api
- baseURL: https://your-rest-implementation.com/api
  baseurl_source: declared
  description: The Data Integration API from TradingView — 4 operation(s) for data integration.
  name: TradingView Data Integration API
  slug: tradingview-data-integration-api
- baseURL: https://your-rest-implementation.com/api
  baseurl_source: declared
  description: The Data Permissions API from TradingView — 2 operation(s) for data permissions.
  name: TradingView Data Permissions API
  slug: tradingview-data-permissions-api
- baseURL: https://your-rest-implementation.com/api
  baseurl_source: declared
  description: The Market Data API from TradingView — 4 operation(s) for market data.
  name: TradingView Market Data API
  slug: tradingview-market-data-api
- baseURL: https://your-rest-implementation.com/api
  baseurl_source: declared
  description: The Trading API from TradingView — 10 operation(s) for trading.
  name: TradingView Trading API
  slug: tradingview-trading-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/tradingview/agentic-access/tradingview-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tradingview-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tradingview/rate-limits/tradingview-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tradingview-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tradingview/plans/tradingview-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tradingview-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tradingview/rules/tradingview-rules.yml
  title: ''
  type: Spectral
  url: rules/tradingview-rules.yml
- group: design
  href: https://artifacts.apis.io/tradingview/json-ld/tradingview-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tradingview-context.jsonld
- group: design
  href: https://artifacts.apis.io/tradingview/vocabulary/tradingview-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tradingview-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tradingview/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tradingview/data-model/tradingview-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tradingview-data-model.yml
- group: design
  href: https://artifacts.apis.io/tradingview/conventions/tradingview-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tradingview-conventions.yml
- group: operate
  href: https://artifacts.apis.io/tradingview/lifecycle/tradingview-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/tradingview-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tradingview/errors/tradingview-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/tradingview-error-codes.yml
- group: design
  href: https://artifacts.apis.io/tradingview/conformance/tradingview-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tradingview-conformance.yml
- group: other
  href: https://artifacts.apis.io/tradingview/overlays/tradingview-broker-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tradingview-broker-rest-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/tradingview/llms/tradingview-lightweight-charts-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tradingview-lightweight-charts-llms.txt
- group: agent
  href: https://artifacts.apis.io/tradingview/llms/tradingview-advanced-charts-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tradingview-advanced-charts-llms.txt
- group: build
  href: https://artifacts.apis.io/tradingview/mcp/tradingview-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tradingview-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/tradingview/mcp/tradingview-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tradingview-mcp.yml
- group: other
  href: https://artifacts.apis.io/tradingview/hosts/tradingview-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tradingview-hosts.yml
- group: build
  href: https://artifacts.apis.io/tradingview/integrations/tradingview-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/tradingview-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/tradingview/vendors/tradingview-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tradingview-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.tradingview.com/news/
- group: auth
  href: https://artifacts.apis.io/tradingview/scopes/tradingview-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tradingview-scopes.yml
- group: auth
  href: https://artifacts.apis.io/tradingview/authentication/tradingview-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tradingview-authentication.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.tradingview.com/feed/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tradingview/lightweight-charts/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/tradingview/lightweight-charts/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/tradingview/lightweight-charts/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/tradingview/lightweight-charts/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.tradingview.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tradingview.com/charting-library-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.tradingview.com/charting-library-docs/latest/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tradingview.com/charting-library-docs/latest/getting_started/
- group: operate
  title: ''
  type: Support
  url: https://www.tradingview.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.tradingview.com/blog/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tradingview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tradingview.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tradingview.com/policies/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tradingview.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tradingview.com/
- group: build
  href: https://artifacts.apis.io/tradingview/packages/tradingview-packages.yml
  title: ''
  type: Packages
  url: packages/tradingview-packages.yml
- group: build
  href: https://artifacts.apis.io/tradingview/packages/tradingview-packages.yml
  title: ''
  type: SDKs
  url: packages/tradingview-packages.yml
- group: design
  href: https://artifacts.apis.io/tradingview/components/tradingview-components.yml
  title: ''
  type: Components
  url: components/tradingview-components.yml
- group: operate
  href: https://artifacts.apis.io/tradingview/changelog/tradingview-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tradingview-changelog.yml
- group: design
  href: https://artifacts.apis.io/tradingview/lifecycle/tradingview-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tradingview-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/tradingview/well-known/tradingview-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tradingview-well-known.yml
- group: auth
  href: https://artifacts.apis.io/tradingview/well-known/tradingview-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tradingview-security.txt
- group: auth
  href: https://artifacts.apis.io/tradingview/security/tradingview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tradingview-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tradingview/security/tradingview-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tradingview-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.tradingview.com/bounty/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.tradingview.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tradingview.com/widget-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tradingview.com/mcp/docs
- group: company
  title: ''
  type: Partners
  url: https://www.tradingview.com/brokerage-integration/
created: '2026-07-17'
description: 'TradingView is a charting, social, and market-data platform for traders and investors, and one of the most-visited finance sites in the world. Its developer surface is delivered primarily as client-side, embeddable UI components and self-hosted JavaScript charting libraries rather than a hosted market-data REST API: the open-source (Apache-2.0) Lightweight Charts library, the free self-hosted Advanced Charts (Charting Library) with its custom Datafeed API, the Trading Platform library, and a large catalog of copy-paste embeddable widgets (charts, tickers, heatmaps, screeners, economic calendars). For brokerages, TradingView publishes a Broker Integration REST API contract that a broker implements to enable order entry and account management directly from the chart. Client libraries ship on npm (lightweight-charts), with official iOS and Android wrappers, and the organization runs a self-hosted bug bounty program. TradingView also operates an official remote MCP server (beta)
  at https://mcp.tradingview.com/mcp, authenticated with OAuth 2.1 against a TradingView account and included in Essential plans and above.'
image: https://www.tradingview.com/static/images/logo-preview.png
json_schemas:
- name: OrdersHistoryResponse
  property_count: 3
  slug: tradingview-orders-history-response
- name: OrdersResponse
  property_count: 2
  slug: tradingview-orders-response
- name: PlaceModifyPreviewOrderCommon
  property_count: 14
  slug: tradingview-place-modify-preview-order-common
- name: StreamNotificationsMessage
  property_count: 4
  slug: tradingview-stream-notifications-message
- name: StreamPositionsMessage
  property_count: 0
  slug: tradingview-stream-positions-message
- name: StreamingDailyBarResponse
  property_count: 8
  slug: tradingview-streaming-daily-bar-response
jsonld:
- class_count: 112
  name: Tradingview Context
  property_count: 278
  slug: tradingview-context
layout: provider
mcp_servers:
- description: TradingView's official remote MCP server (beta). One Streamable HTTP endpoint for every client; authentication is OAuth 2.1 with a TradingView account (no API keys). MCP access is included in Essentia
  name: TradingView MCP Server
  slug: tradingview
modified: '2026-11-05'
name: TradingView
nav: Providers
network: true
overview: 'TradingView publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Authorization API, Broker Configuration API, and 7 more. Tagged areas include Company, Consumer, Charts, Charting Library, and Financial Data.


  The TradingView catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TradingView''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 46 more developer resources.'
plans:
- name: Tradingview Plans Pricing
  plan_count: 6
  slug: tradingview-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Tradingview Rate Limits
  slug: tradingview-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: TradingView API Rules
  rule_count: 57
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 11
  slug: tradingview-rules
scopes:
- name: Tradingview Scopes
  scope_count: 1
  slug: tradingview-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 35.1
  facets:
    access_clarity: 71.1
    contract_governance: 35.6
    contract_quality: 61.2
    developer_ergonomics: 56.5
    discoverability: 76.7
    operational_transparency: 73.7
  open_source:
    applies: true
    score: 50.0
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 48.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tradingview/tradingview-2026-09-02T164111.png
security:
- kind: authentication
  name: Tradingview Authentication
  slug: tradingview-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Tradingview Domain Security
  slug: tradingview-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tradingview Vulnerability Disclosure
  slug: tradingview-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: tradingview-broker-market-data
  slug: tradingview-broker-market-data
- name: tradingview-broker-order-lifecycle
  slug: tradingview-broker-order-lifecycle
- name: tradingview-broker-position-management
  slug: tradingview-broker-position-management
slug: tradingview
tags:
- Company
- Consumer
- Charts
- Charting Library
- Financial Data
- Market Data
- Widgets
- Trading
- Fintech
- Embeddable Components
website: https://www.tradingview.com/
---
