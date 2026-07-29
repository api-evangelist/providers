---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Marketdata App Agentic Access
  operation_count: 14
  slug: marketdata-app-agentic-access
  summary_line: 14 operations
api_count: 4
apis:
- description: Real-time and historical index candles and quotes.
  name: Market Data Indices API
  slug: marketdata-app-indices-api
- description: Reference and status data about the markets covered by Market Data.
  name: Market Data Markets API
  slug: marketdata-app-markets-api
- description: Options chains, per-contract quotes, expirations, strikes, and OCC symbol lookup.
  name: Market Data Options API
  slug: marketdata-app-options-api
- description: Real-time and historical stock candles, quotes, bulk data, prices, earnings, and news.
  name: Market Data Stocks API
  slug: marketdata-app-stocks-api
artifact_total: 16
collections:
- collection_type: postman
  name: Market Data Indices API
  slug: postman-marketdata-app-indices-api
- collection_type: postman
  name: Market Data Indices Markets API
  slug: postman-marketdata-app-markets-api
- collection_type: postman
  name: Market Data Indices Options API
  slug: postman-marketdata-app-options-api
- collection_type: postman
  name: Market Data Indices Stocks API
  slug: postman-marketdata-app-stocks-api
- collection_type: open
  name: Market Data API
  slug: open-marketdata-app
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/market-data/overview
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/marketdata-app-openapi-original.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marketdata-app-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/marketdata-app-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/marketdata-app-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/marketdata-app-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/marketdata-app-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/marketdata-app-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/marketdata-app-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/marketdata-app-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/marketdata-app-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/marketdata-app-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/marketdata-app-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.marketdata.app/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/marketdata-app-changelog.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://roadmap.marketdata.app/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/marketdata-app-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/marketdata-app-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/marketdata-app-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/marketdata-app-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Postman
  url: https://app.getpostman.com/run-collection/27146376-b1331cd2-4749-4708-96fe-2f1708b02854?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D27146376-b1331cd2-4749-4708-96fe-2f1708b02854%26entityType%3Dcollection%26workspaceId%3Dbd65af1d-3c36-4e62-ae64-f71008c154b4
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MarketDataApp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/marketdataapp
- group: company
  title: ''
  type: Website
  url: https://www.marketdata.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.marketdata.app/dashboard/
- group: docs
  title: ''
  type: Documentation
  url: https://www.marketdata.app/docs/api/
- group: docs
  title: ''
  type: APIReference
  url: https://www.marketdata.app/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.marketdata.app/docs/api/
- group: operate
  title: ''
  type: Support
  url: https://www.marketdata.app/helpdesk/
- group: start
  title: ''
  type: SignUp
  url: https://www.marketdata.app/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.marketdata.app/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.marketdata.app/privacy/
- group: commercial
  title: ''
  type: Plans
  url: plans/marketdata-app-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/marketdata-app-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/marketdata-app-finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.marketdata.app/pricing/
created: '2026-07-11'
description: Market Data (marketdata.app) is a financial market data provider offering a REST API for real-time and historical U.S. stock, options, and index data. The API (base https://api.marketdata.app/v1, Bearer-token authenticated) covers stock candles and quotes - single and bulk - plus earnings and news; full options chains with per-contract quotes, expirations, strikes, and OCC symbol lookup; index candles and quotes; and market open/closed status. Responses are JSON or CSV and are billed on a daily API-credit model, where multi-symbol responses (bulk quotes, options chains) consume one credit per symbol. A 30-day trial, a Free Forever tier, and paid Starter, Trader, and Prime plans are available. Note that the API may return HTTP 203 from its caching tier and clients must treat it as success.
finops:
- name: Marketdata App Finops
  service_category: Financial Market Data
  slug: marketdata-app-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marketdata-app.png
layout: provider
mcp_servers:
- description: ''
  name: marketdata-app-mcp.yml
  slug: marketdata-app-mcpyml
modified: '2026-07-22'
name: Market Data
nav: Providers
network: true
overview: 'Market Data publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Indices API, Markets API, Options API, and 1 more. Tagged areas include Market Data, Financial Data, Stocks, Options, and Indices.


  Market Data''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 30 more developer resources.'
plans:
- name: Marketdata App Plans Pricing
  plan_count: 6
  slug: marketdata-app-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 7
  name: Marketdata App Rate Limits
  slug: marketdata-app-rate-limits
score:
  band: strong
  composite: 64.0
  delta: -1.6
  facets:
    commercial_clarity: 84.2
    contract_quality: 59.3
    developer_ergonomics: 71.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 73.7
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marketdata-app/refs/heads/main/screenshots/marketdata-app-2026-07-22T202452.png
security:
- kind: authentication
  name: Marketdata App Authentication
  slug: marketdata-app-authentication
  summary_line: http/apiKey · 2 schemes
- kind: domain-security
  name: Marketdata App Domain Security
  slug: marketdata-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marketdata-app
tags:
- Market Data
- Financial Data
- Stocks
- Options
- Indices
- Real-Time Data
- Historical Data
- Quotes
website: https://www.marketdata.app
---
