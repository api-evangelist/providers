---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tiingo Agentic Access
  operation_count: 37
  slug: tiingo-agentic-access
  summary_line: 37 operations
api_count: 1
apis:
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The BOATS API from Tiingo — 2 operation(s) for boats.
  name: Tiingo BOATS API
  slug: tiingo-boats-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The Corporate Actions API from Tiingo — 5 operation(s) for corporate actions.
  name: Tiingo Corporate Actions API
  slug: tiingo-corporate-actions-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The Crypto API from Tiingo — 3 operation(s) for crypto.
  name: Tiingo Crypto API
  slug: tiingo-crypto-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The Crypto Yield API from Tiingo — 4 operation(s) for crypto yield.
  name: Tiingo Crypto Yield API
  slug: tiingo-crypto-yield-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The End-of-Day API from Tiingo — 2 operation(s) for end-of-day.
  name: Tiingo End Of Day API
  slug: tiingo-end-of-day-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The Equity Realtime API from Tiingo — 2 operation(s) for equity realtime.
  name: Tiingo Equity Realtime API
  slug: tiingo-equity-realtime-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The Forex API from Tiingo — 2 operation(s) for forex.
  name: Tiingo Forex API
  slug: tiingo-forex-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The Fund Fees API from Tiingo — 2 operation(s) for fund fees.
  name: Tiingo Fund Fees API
  slug: tiingo-fund-fees-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The Fundamentals API from Tiingo — 4 operation(s) for fundamentals.
  name: Tiingo Fundamentals API
  slug: tiingo-fundamentals-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The IEX API from Tiingo — 2 operation(s) for iex.
  name: Tiingo IEX API
  slug: tiingo-iex-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The News API from Tiingo — 3 operation(s) for news.
  name: Tiingo News API
  slug: tiingo-news-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The Small Exchange API from Tiingo — 4 operation(s) for small exchange.
  name: Tiingo Small Exchange API
  slug: tiingo-small-exchange-api
- baseURL: https://api.tiingo.com/tiingo/daily
  baseurl_source: declared
  description: The Utilities API from Tiingo — 2 operation(s) for utilities.
  name: Tiingo Utilities API
  slug: tiingo-utilities-api
artifact_total: 23
asyncapis:
- description: Tiingo's WebSocket streaming interface for real-time market data. Clients subscribe and unsubscribe to data feeds by sending a JSON request containing eventName, an authorization API token, and eventD
  name: Tiingo WebSocket API
  slug: tiingo-websockets-asyncapi
collections:
- collection_type: postman
  name: Tiingo API
  slug: postman-tiingo
- collection_type: open
  name: Tiingo API
  slug: open-tiingo
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tiingo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tiingo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiingo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tiingo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiingo
- group: start
  title: ''
  type: Portal
  url: https://www.tiingo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tiingo.com/documentation/general/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tiingo.com/about/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/tiingo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tiingo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tiingo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tiingo.com/blog/feed/
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/tiingo-websockets-asyncapi.yml
- group: build
  title: ''
  type: Packages
  url: packages/tiingo-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tiingo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tiingo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/tiingo-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/tiingo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tiingo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tiingo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tiingo.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tiingo-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tiingo-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tiingo-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tiingo-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tiingo-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.tiingo.com/documentation/general/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tiingo.com/documentation/general/connecting
- group: operate
  title: ''
  type: Support
  url: https://www.tiingo.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tiingo.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tiingo.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.tiingo.com/
created: '2026-05-08'
description: Tiingo provides high-quality financial market data APIs across US equities, crypto, FX, fundamentals, and news, popular among quantitative researchers. APIs include End-of-Day prices, IEX intraday data, Crypto, Forex, Fundamentals, and News, with REST and WebSocket access at api.tiingo.com.
finops:
- name: Tiingo Finops
  service_category: Fintech
  slug: tiingo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tiingo.png
layout: provider
mcp_servers:
- description: ''
  name: Tiingo MCP Server
  slug: tiingo-mcp-server
modified: '2026-07-22'
name: Tiingo
nav: Providers
network: true
overview: 'Tiingo publishes 13 APIs on the [APIs.io](https://apis.io/) network, including BOATS API, Corporate Actions API, Crypto API, and 10 more. Tagged areas include Fintech, Market Data, Stocks, Crypto, and FX.


  The Tiingo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tiingo''s developer surface includes developer portal, documentation, pricing, engineering blog, changelog, authentication, sandbox, and 26 more developer resources.'
plans:
- name: Tiingo Plans Pricing
  plan_count: 4
  slug: tiingo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Tiingo Rate Limits
  slug: tiingo-rate-limits
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 25
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 20.4
    developer_ergonomics: 70.8
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tiingo/refs/heads/main/screenshots/tiingo-2026-06-20T195345.png
security:
- kind: authentication
  name: Tiingo Authentication
  slug: tiingo-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Tiingo Domain Security
  slug: tiingo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tiingo
tags:
- Fintech
- Market Data
- Stocks
- Crypto
- FX
- News
- Fundamentals
- WebSockets
website: https://www.tiingo.com/
---
