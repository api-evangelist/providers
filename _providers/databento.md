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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 72.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 88
  human_in_the_loop: 2
  name: Databento Agentic Access
  operation_count: 203
  slug: databento-agentic-access
  summary_line: 203 operations · 88 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: Streams historical market data over HTTP for a requested date/time range. A single request selects a dataset, one or more symbols, a schema (MBO full order book, MBP-1/MBP-10, trades, OHLCV bars, stat
  name: Databento Historical Timeseries API
  slug: databento-historical-timeseries-api
- description: Discovery and cost-estimation endpoints for the historical catalog. List publishers, datasets, schemas, and fields; look up per-dataset date ranges and data-quality conditions; and pre-compute the rec
  name: Databento Metadata API
  slug: databento-metadata-api
- description: Resolves symbols between Databento's symbology systems - raw symbol, instrument ID, parent, and continuous contract - for a dataset over a date range. Lets consumers map tickers, exchange instrument I
  name: Databento Symbology API
  slug: databento-symbology-api
- description: 'Submits asynchronous batch jobs that materialize large historical requests into downloadable flat files (DBN, CSV, or JSON), optionally split by day, symbol, or size. Submit a job, list your jobs and '
  name: Databento Batch API
  slug: databento-batch-api
- description: 'Low-latency live market data delivered over a raw TCP binary streaming protocol using Databento Binary Encoding (DBN) - the same normalized schemas as the historical API. Sessions authenticate with a '
  name: Databento Live Streaming API
  slug: databento-live-streaming-api
- description: Reference and non-price data that complements the market data feeds - a security master (instrument definitions and identifiers), corporate actions (splits, dividends, symbol changes, and other events
  name: Databento Reference API
  slug: databento-reference-api
artifact_total: 15
collections:
- collection_type: open
  name: Databento Historical and Reference API
  slug: open-databento
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/databento-platform-openapi-official.json
- group: other
  title: ''
  type: Overlay
  url: overlays/databento-platform-official-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/databento-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/databento-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/databento-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/databento-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/databento-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/databento-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/databento-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.databento.com
- group: operate
  title: ''
  type: Deprecation
  url: https://databento.com/docs/api-reference-historical/basics/versioning
- group: design
  title: ''
  type: Conventions
  url: conventions/databento-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/databento-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/databento-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/databento-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.databento.com
- group: commercial
  title: ''
  type: Pricing
  url: https://databento.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://databento.com/support
- group: start
  title: ''
  type: SignUp
  url: https://databento.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.databento.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.databento.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://databento.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://databento.com/docs/api-reference-historical
- group: build
  title: ''
  type: Postman
  url: collections/databento.postman_collection.json
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://databento.com/docs/release-notes
- group: auth
  title: ''
  type: DomainSecurity
  url: security/databento-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/databento-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/databento-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/databento-agentic-access.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/databento
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/databento
- group: company
  title: ''
  type: Website
  url: https://databento.com
- group: docs
  title: ''
  type: Documentation
  url: https://databento.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/databento-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/databento-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/databento-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://databento.com/blog
created: '2026-07-11'
description: Databento is a market data platform that delivers historical and live financial market data through a single, normalized API. It covers equities, futures, options, and other asset classes across major venues, with full order book depth (MBO/MBP), trades, OHLCV bars, and reference data. Historical data is served over a REST HTTP API (hist.databento.com) with pay-as-you-go billing per byte streamed, while live data is delivered over a low-latency raw TCP binary protocol using Databento Binary Encoding (DBN). Official Python, C++, and Rust client libraries wrap both surfaces, and a Reference API provides security master, corporate actions, and adjustment factor data.
finops:
- name: Databento Finops
  service_category: Market Data and Financial Data
  slug: databento-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/databento.png
layout: provider
mcp_servers:
- description: ''
  name: databento-mcp.yml
  slug: databento-mcpyml
modified: '2026-07-22'
name: Databento
nav: Providers
network: true
overview: 'Databento publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Historical Timeseries API, Metadata API, Symbology API, and 2 more. Tagged areas include Market Data, Financial Data, Reference Data, Historical Market Data, and Trading.


  Databento''s developer surface includes changelog, CLI, pricing, support, signup flow, getting-started guide, API reference, and 31 more developer resources.'
plans:
- name: Databento Plans Pricing
  plan_count: 5
  slug: databento-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Databento Rate Limits
  slug: databento-rate-limits
scopes:
- name: Databento Scopes
  scope_count: 0
  slug: databento-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 68.7
  delta: 2.7
  facets:
    commercial_clarity: 84.2
    contract_quality: 59.1
    developer_ergonomics: 76.1
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 81.6
  previous_composite: 66.0
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/databento/refs/heads/main/screenshots/databento-2026-07-22T202314.png
security:
- kind: authentication
  name: Databento Authentication
  slug: databento-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Databento Domain Security
  slug: databento-domain-security
  summary_line: TLSv1.3 · DMARC
slug: databento
tags:
- Market Data
- Financial Data
- Reference Data
- Historical Market Data
- Trading
website: https://databento.com
---
