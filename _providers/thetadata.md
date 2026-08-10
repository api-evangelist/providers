---
access_model:
  confidence: high
  label: Freemium, self-service signup
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://thetadata.net/pricing
  - https://docs.thetadata.us/Articles/Getting-Started/Subscriptions.html
  - https://docs.thetadata.us/Articles/Getting-Started/Sample-Data.html
  trial: true
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-08-10'
api_count: 14
apis:
- description: JSON WebSocket streaming of US stock trade/quote, options trade/quote, and index price streams, served locally by the Theta Terminal at ws://127.0.0.1:25520/v1/events. Requires a paid subscription wit
  name: ThetaData Streaming WebSocket API
  slug: thetadata-streaming-websocket-api
- description: Model Context Protocol server built into Theta Terminal v3, exposing the full v3 API to LLM CLIs (documented for Claude CLI and Gemini CLI) over SSE at http://127.0.0.1:25503/mcp/sse. Requires the ter
  name: ThetaData MCP Server
  slug: thetadata-mcp-server
- description: The At-Time API from ThetaData — 5 operation(s) for at-time.
  name: ThetaData At-Time API
  slug: thetadata-at-time-api
- description: The Calendar API from ThetaData — 3 operation(s) for calendar.
  name: ThetaData Calendar API
  slug: thetadata-calendar-api
- description: The FlatFile API from ThetaData — 6 operation(s) for flatfile.
  name: ThetaData FlatFile API
  slug: thetadata-flatfile-api
- description: The History API from ThetaData — 26 operation(s) for history.
  name: ThetaData History API
  slug: thetadata-history-api
- description: The Index API from ThetaData — 10 operation(s) for index.
  name: ThetaData Index API
  slug: thetadata-index-api
- description: The Interest Rate API from ThetaData — 1 operation(s) for interest rate.
  name: ThetaData Interest Rate API
  slug: thetadata-interest-rate-api
- description: The List API from ThetaData — 9 operation(s) for list.
  name: ThetaData List API
  slug: thetadata-list-api
- description: The Option API from ThetaData — 37 operation(s) for option.
  name: ThetaData Option API
  slug: thetadata-option-api
- description: The Single Day API from ThetaData — 2 operation(s) for single day.
  name: ThetaData Single Day API
  slug: thetadata-single-day-api
- description: The Snapshot API from ThetaData — 17 operation(s) for snapshot.
  name: ThetaData Snapshot API
  slug: thetadata-snapshot-api
- description: The Stock API from ThetaData — 15 operation(s) for stock.
  name: ThetaData Stock API
  slug: thetadata-stock-api
- description: The Year API from ThetaData — 1 operation(s) for year.
  name: ThetaData Year API
  slug: thetadata-year-api
artifact_total: 32
asyncapis:
- description: JSON WebSocket streaming of US stock trade/quote, option trade/quote/full-trade, and index price/market-value streams, served locally by Theta Terminal v3. A single connection per user is permitted; a
  name: ThetaData Streaming WebSocket API (derived)
  slug: thetadata-streaming-asyncapi
collections:
- collection_type: postman
  name: Theta Data v3 At-Time API
  slug: postman-thetadata-at-time-api
- collection_type: postman
  name: Theta Data v3 At-Time Calendar API
  slug: postman-thetadata-calendar-api
- collection_type: postman
  name: Theta Data v3 At-Time FlatFile API
  slug: postman-thetadata-flatfile-api
- collection_type: postman
  name: Theta Data v3 At-Time History API
  slug: postman-thetadata-history-api
- collection_type: postman
  name: Theta Data v3 At-Time Index API
  slug: postman-thetadata-index-api
- collection_type: postman
  name: Theta Data v3 At-Time Interest Rate API
  slug: postman-thetadata-interest-rate-api
- collection_type: postman
  name: Theta Data v3 At-Time List API
  slug: postman-thetadata-list-api
- collection_type: postman
  name: Theta Data v3 At-Time Option API
  slug: postman-thetadata-option-api
- collection_type: postman
  name: Theta Data v3 At-Time Single Day API
  slug: postman-thetadata-single-day-api
- collection_type: postman
  name: Theta Data v3 At-Time Snapshot API
  slug: postman-thetadata-snapshot-api
- collection_type: postman
  name: Theta Data v3 At-Time Stock API
  slug: postman-thetadata-stock-api
- collection_type: postman
  name: Theta Data v3 At-Time Year API
  slug: postman-thetadata-year-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/thetadata/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thetadata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thetadata.net/
- group: start
  title: ''
  type: Portal
  url: https://thetadata.net/portal
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thetadata.us/
- group: company
  title: ''
  type: Blog
  url: https://thetadata.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://thetadata.net/pricing
- group: start
  title: ''
  type: SignUp
  url: https://thetadata.net/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thetadata.net/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thetadata.net/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.thetadata.us/
- group: operate
  title: ''
  type: StatusPage
  url: https://thetadata.statuspage.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axiomx-theta-data
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thetadata.us/Articles/Getting-Started/Getting-Started.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thetadata.us/
- group: operate
  title: ''
  type: Roadmap
  url: https://thetadata.net/roadmap
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AXIOMXLLC
- group: build
  title: ''
  type: SampleData
  url: https://docs.thetadata.us/Articles/Getting-Started/Sample-Data.html
- group: build
  title: ''
  type: Packages
  url: packages/thetadata-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/thetadata-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thetadata-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thetadata-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/thetadata-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/thetadata-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thetadata-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.thetadata.us/Articles/Getting-Started/v2-migration-guide.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/thetadata-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thetadata-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/thetadata-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/thetadata-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thetadata-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/thetadata-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/thetadata-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thetadata-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/thetadata-plans.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-21'
description: ThetaData is a developer-first US market data vendor founded in 2022 by Bailey Danseglio, selling real-time and historical options, stocks, indices, and interest-rates data with unfiltered tick-level trades, quotes, and Greeks. Delivery is self-serve via the Theta Terminal, a local Java application that authenticates with an API key or account credentials and exposes a local REST API (127.0.0.1:25503/v3), a WebSocket streaming API (127.0.0.1:25520), and an MCP server, backed by a published OpenAPI 3.1 spec, Python library, flat files, and tiered monthly subscriptions.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thetadata.png
layout: provider
mcp_servers:
- description: ''
  name: thetadata-mcp.yml
  slug: thetadata-mcpyml
modified: '2026-07-22'
name: ThetaData
nav: Providers
network: true
overview: 'ThetaData publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Streaming WebSocket API, At-Time API, Calendar API, and 10 more. Tagged areas include Financial, Market Data, Options, Stocks, and Indices.


  The ThetaData catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ThetaData''s developer surface includes developer portal, documentation, engineering blog, pricing, signup flow, support, getting-started guide, and 29 more developer resources.'
plans:
- name: Thetadata Plans
  plan_count: 7
  slug: thetadata-plans
random_paper: 16
rate_limits:
- limit_count: 6
  name: Thetadata Rate Limits
  slug: thetadata-rate-limits
score:
  band: strong
  composite: 63.5
  delta: 0.0
  facets:
    commercial_clarity: 76.3
    contract_quality: 59.2
    developer_ergonomics: 71.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 81.6
  previous_composite: 63.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 51.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thetadata/refs/heads/main/screenshots/thetadata-2026-07-22T202634.png
security:
- kind: authentication
  name: Thetadata Authentication
  slug: thetadata-authentication
  summary_line: apiKey/credentials · 2 schemes
- kind: domain-security
  name: Thetadata Domain Security
  slug: thetadata-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: thetadata
tags:
- Financial
- Market Data
- Options
- Stocks
- Indices
- Real-Time
- Historical Data
- Trading
website: https://thetadata.net/
---
