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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-07-28'
api_count: 13
apis:
- description: Constructed historical order books for the T7 trading venues of Deutsche Börse Group (Eurex, Xetra) with nanosecond granularity, accessed over REST with bearer-token authentication.
  name: A7 Analytics Platform - Order Book API
  slug: a7-order-book-api
- description: Un-normalized, genuine historical order-by-order market data from the T7 Enhanced Order Book Interface (EOBI) feed for Eurex and Xetra.
  name: A7 Analytics Platform - Market Data API (EOBI)
  slug: a7-market-data-eobi-api
- description: Historical CME Group market data from the MDP feed served through the A7 Analytics Platform REST API.
  name: A7 Analytics Platform - CME Market Data API (MDP)
  slug: a7-cme-market-data-mdp-api
- description: Reference data for T7 venues (markets, market segments, securities) from the Reference Data Interface, version 2 of the A7 reference data API.
  name: A7 Analytics Platform - Reference Data API (RDI) v2
  slug: a7-reference-data-rdi-api
- description: CME Group security-definition reference data served through the A7 Analytics Platform REST API.
  name: A7 Analytics Platform - CME Reference Data API (SD)
  slug: a7-cme-reference-data-sd-api
- description: Create, update, delete, and run custom algos over historical order book data and retrieve their results - a high-performance framework for custom analytics on A7.
  name: A7 Analytics Platform - Algo Management API
  slug: a7-algo-management-api
- description: Manage customer datasets on the A7 Analytics Platform (versions 1 and 2 of the Dataset API).
  name: A7 Analytics Platform - Dataset API
  slug: a7-dataset-api
- description: Off-the-shelf market data insights and analytics derived from A7 granular historical order book data.
  name: A7 Analytics Platform - Market Data Insights API
  slug: a7-market-data-insights-api
- description: Option analytics computed on the A7 Analytics Platform for Eurex-traded options.
  name: A7 Analytics Platform - Option Analytics API
  slug: a7-option-analytics-api
- description: Management of precalculated analytics runs on the A7 Analytics Platform.
  name: A7 Analytics Platform - Precalc API
  slug: a7-precalc-api
- description: Simulate Xetra auctions against historical order book data on the A7 Analytics Platform.
  name: A7 Analytics Platform - Auction Simulation API
  slug: a7-auction-simulation-api
- description: Free GraphQL API for Eurex T7 reference data (products, contracts, instrument attributes) in machine- and human-readable JSON, offered with a shared rate-limited public API key or a dedicated key from
  name: Eurex T7 Reference Data API
  slug: eurex-t7-reference-data-api
- description: Cloud-delivered real-time market data streaming over WebSocket (host md.deutsche-boerse.com) with Protocol Buffers or JSON message encoding and API-key authentication - the published sample client sub
  name: Deutsche Börse Cloud Stream Market Data API
  slug: cloud-stream-market-data-api
artifact_total: 18
asyncapis:
- description: 'Real-time market data streaming over WebSocket from Deutsche Börse Cloud Stream. Clients connect to md.deutsche-boerse.com with an API key generated in the GUI (passed as a token; the official Python '
  name: Deutsche Börse Cloud Stream Market Data
  slug: deutsche-boerse-cloud-stream-asyncapi
common:
- group: build
  title: ''
  type: Packages
  url: packages/deutsche-boerse-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/deutsche-boerse-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/deutsche-boerse-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/deutsche-boerse-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/deutsche-boerse-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/deutsche-boerse-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deutsche-boerse-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/deutsche-boerse-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deutsche-boerse-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deutsche-boerse-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.deutsche-boerse.com/dbg-en/markets-services/ps-technology/service-status
- group: auth
  title: ''
  type: Security
  url: https://www.deutsche-boerse.com/dbg-en/our-company/contact/report-vulnerabilities
- group: design
  title: ''
  type: Conventions
  url: conventions/deutsche-boerse-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/deutsche-boerse-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/deutsche-boerse-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/deutsche-boerse-cloud-stream-asyncapi.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/deutsche-boerse-eurex-t7-reference-data.graphql
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.developer.deutsche-boerse.com/docs/consumer/rate-limiting
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.developer.deutsche-boerse.com/
- group: docs
  title: ''
  type: APIReference
  url: https://a7.deutsche-boerse.com/doc/api/prod/PROD_API.Documentation.zip
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developer.deutsche-boerse.com/docs/consumer/getting-started/introduction
- group: operate
  title: ''
  type: Support
  url: https://www.deutsche-boerse.com/dbg-en/markets-services/ps-technology/ps-api-platform
- group: start
  title: ''
  type: Login
  url: https://console.developer.deutsche-boerse.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/deutsche-boerse-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deutsche-boerse-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deutsche-boerse-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.deutsche-boerse.com/dbg-en/
- group: start
  title: ''
  type: Portal
  url: https://console.developer.deutsche-boerse.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.deutsche-boerse.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Deutsche-Boerse
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deutscheboerse
- group: company
  title: ''
  type: Blog
  url: https://docs.developer.deutsche-boerse.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deutsche-boerse.com/dbg-en/meta/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deutsche-boerse.com/dbg-en/meta/disclaimer
created: '2026-07-21'
description: Deutsche Börse AG is the Frankfurt-based, publicly listed (FWB DB1) exchange organization behind the Frankfurt Stock Exchange and Xetra cash market, the Eurex derivatives exchange, EEX, 360T, Clearstream post-trade services, and the ISS STOXX index and analytics business. Its Market Data + Services arm sells real-time, historical, and reference market data, delivered through a self-serve Group API platform (developer.deutsche-boerse.com, API-key gated REST and GraphQL), the A7 Analytics Platform cloud REST API for nanosecond order-by-order Eurex/Xetra/EEX/CME history, a Cloud Stream WebSocket feed, licensed low-latency feeds, and the Datashop for commercial data purchases.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deutsche-boerse.png
layout: provider
mcp_servers:
- description: ''
  name: deutsche-boerse-mcp.yml
  slug: deutsche-boerse-mcpyml
modified: '2026-07-22'
name: Deutsche Börse
nav: Providers
network: true
overview: 'Deutsche Börse publishes 12 APIs on the [APIs.io](https://apis.io/) network, including A7 Analytics Platform - Order Book API, A7 Analytics Platform - Market Data API (EOBI), A7 Analytics Platform - CME Market Data API (MDP), and 9 more. Tagged areas include Financial, Market Data, Stocks, Derivatives, and Trading.


  The Deutsche Börse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Deutsche Börse''s developer surface includes changelog, API reference, getting-started guide, support, authentication, developer portal, documentation, and 28 more developer resources.'
random_paper: 80
score:
  band: developing
  composite: 52.3
  delta: -4.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.0
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 56.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 18
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
screenshot: https://raw.githubusercontent.com/api-evangelist/deutsche-boerse/refs/heads/main/screenshots/deutsche-boerse-2026-07-22T202326.png
security:
- kind: authentication
  name: Deutsche Boerse Authentication
  slug: deutsche-boerse-authentication
  summary_line: http/apiKey · 3 schemes
- kind: domain-security
  name: Deutsche Boerse Domain Security
  slug: deutsche-boerse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Deutsche Boerse Vulnerability Disclosure
  slug: deutsche-boerse-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deutsche-boerse
tags:
- Financial
- Market Data
- Stocks
- Derivatives
- Trading
- Real-Time
- Order Book
- Reference Data
- Exchange
- Analytics
website: https://www.deutsche-boerse.com/dbg-en/
---
