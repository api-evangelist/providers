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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: REST API for tables data (datatables) — row and column filtered access to hundreds of financial, economic, and alternative datasets, with JSON, XML, and CSV formats, cursor-based pagination, and an as
  name: Nasdaq Data Link Tables API
  slug: nasdaq-data-link-tables-api
- description: REST API (Nasdaq Cloud Data Service) for real-time or delayed exchange data — Nasdaq Basic, Last Sale+, BBO, Global Index Data Service, and Smart Options — authenticated with client credentials exchan
  name: Nasdaq Data Link REST API for Real-Time or Delayed Data
  slug: nasdaq-data-link-rest-api-for-real-time-or-delayed-data
- description: Streaming API (Nasdaq Cloud Data Service) for real-time products — Nasdaq Basic, Last Sale+, TotalView, Consolidated Quotes and Trades, Global Index Data Service, Smart Options, and Benzinga MarketNew
  name: Nasdaq Data Link Streaming API
  slug: nasdaq-data-link-streaming-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://data.nasdaq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://data.nasdaq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.data.nasdaq.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.data.nasdaq.com/docs/in-depth-usage-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.data.nasdaq.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.data.nasdaq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nasdaq
- group: operate
  title: ''
  type: StatusPage
  url: https://status.data.nasdaq.com/
- group: start
  title: ''
  type: SignUp
  url: https://data.nasdaq.com/users/sign_up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://data.nasdaq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nasdaq.com/privacy-statement
- group: build
  title: ''
  type: Postman
  url: https://github.com/Nasdaq/NasdaqCloudDataService-REST-API/tree/main/restapi/postman
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nasdaq-data-link-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/nasdaq-data-link-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nasdaq-data-link-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nasdaq-data-link-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nasdaq-data-link-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nasdaq-data-link-well-known.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nasdaq-data-link-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nasdaq-data-link-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nasdaq-data-link-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nasdaq-data-link-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nasdaq-data-link-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nasdaq-data-link-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nasdaq-data-link-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasdaq-data-link-domain-security.yml
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Nasdaq Data Link (formerly Quandl) is Nasdaq's financial, economic, and alternative data platform, offering hundreds of free and premium datasets from publishers like Zacks, Sharadar, QuoteMedia, and the World Bank. Data is delivered through a REST API for tables data, a REST API for real-time or delayed exchange data, and a streaming API (Nasdaq Cloud Data Service), with official Python, R, Excel, and CLI tooling.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasdaq-data-link.png
layout: provider
mcp_servers:
- description: ''
  name: Nasdaq Data Link MCP Server
  slug: nasdaq-data-link-mcp-server
modified: '2026-07-22'
name: Nasdaq Data Link
nav: Providers
network: true
overview: 'Nasdaq Data Link publishes 1 API on the [APIs.io](https://apis.io/) network: REST API for Real-Time or Delayed Data. Tagged areas include Financial Data, Stock Market, Market Data, Economic Data, and Alternative Data.


  Nasdaq Data Link''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, CLI, authentication, and 20 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 10
  name: Nasdaq Data Link Rate Limits
  slug: nasdaq-data-link-rate-limits
scopes:
- name: Nasdaq Data Link Scopes
  scope_count: 9
  slug: nasdaq-data-link-scopes
  summary_line: 9 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 14
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 67.9
    discoverability: 88.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 38.6
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 55.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasdaq-data-link/refs/heads/main/screenshots/nasdaq-data-link-2026-06-20T185954.png
security:
- kind: authentication
  name: Nasdaq Data Link Authentication
  slug: nasdaq-data-link-authentication
  summary_line: apiKey/oauth2/http-bearer · 3 schemes
- kind: domain-security
  name: Nasdaq Data Link Domain Security
  slug: nasdaq-data-link-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nasdaq-data-link
tags:
- Financial Data
- Stock Market
- Market Data
- Economic Data
- Alternative Data
- Time Series
- Open Data
- Public APIs
website: https://data.nasdaq.com/
---
