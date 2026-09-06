---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 119
  human_in_the_loop: 119
  name: Dxfeed Agentic Access
  operation_count: 269
  slug: dxfeed-agentic-access
  summary_line: 269 operations · 119 acting · 119 human-in-the-loop
api_count: 1
apis:
- description: REST service over the core dxFeed API with /events (snapshot), /eventSource (Server-Sent Events stream), /addSubscription, and /removeSubscription resources across 20+ market event types (Quote, Trade
  name: dxFeed REST Web Service API
  slug: dxfeed-rest-api
- baseURL: wss://demo.dxfeed.com/dxlink-ws
  baseurl_source: declared
  description: dxLink is dxFeed's WebSocket protocol for real-time market data streaming with multiplexed virtual channels, authorization, and FEED/DOM (order book) service channels. The protocol is publicly specifi
  name: dxFeed dxLink WebSocket API
  slug: dxfeed-dxlink-websocket-api
- description: Reference-data web service for requesting instrument profiles in dxFeed's Instrument Profile Format (IPF), including live incremental updates, covering the 3.5M instruments in the dxFeed symbology uni
  name: dxFeed Instrument Profile (IPF) Web Service
  slug: dxfeed-ipf-webservice
- description: Industry-standard FIX protocol access to dxFeed market data for trading systems. Session endpoints and credentials are provisioned during onboarding; no public FIX gateway host is documented.
  name: dxFeed FIX API
  slug: dxfeed-fix-api
- description: Historical data access covering candle/aggregated data and raw tick data extraction (dxFeed stores up to 10TB of raw data per day). The knowledge base documents how to request tick data and read extra
  name: dxFeed Historical Data Services
  slug: dxfeed-historical-data-services
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The alpha-beta-controller API from dxFeed — 6 operation(s) for alpha-beta-controller.
  name: dxFeed Alpha Beta Controller API
  slug: dxfeed-alpha-beta-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The asset-classification-controller API from dxFeed — 5 operation(s) for asset-classification-controller.
  name: dxFeed Asset Classification Controller API
  slug: dxfeed-asset-classification-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The balance-statement-controller API from dxFeed — 6 operation(s) for balance-statement-controller.
  name: dxFeed Balance Statement Controller API
  slug: dxfeed-balance-statement-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The cash-flow-statement-controller API from dxFeed — 6 operation(s) for cash-flow-statement-controller.
  name: dxFeed Cash Flow Statement Controller API
  slug: dxfeed-cash-flow-statement-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The company-profile-controller API from dxFeed — 5 operation(s) for company-profile-controller.
  name: dxFeed Company Profile Controller API
  slug: dxfeed-company-profile-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The consensus-estimate-controller API from dxFeed — 6 operation(s) for consensus-estimate-controller.
  name: dxFeed Consensus Estimate Controller API
  slug: dxfeed-consensus-estimate-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The corporate-action-controller API from dxFeed — 8 operation(s) for corporate-action-controller.
  name: dxFeed Corporate Action Controller API
  slug: dxfeed-corporate-action-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The corporate-calendar-controller API from dxFeed — 7 operation(s) for corporate-calendar-controller.
  name: dxFeed Corporate Calendar Controller API
  slug: dxfeed-corporate-calendar-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The crypto-reference-controller API from dxFeed — 5 operation(s) for crypto-reference-controller.
  name: dxFeed Crypto Reference Controller API
  slug: dxfeed-crypto-reference-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The crypto-summary-controller API from dxFeed — 6 operation(s) for crypto-summary-controller.
  name: dxFeed Crypto Summary Controller API
  slug: dxfeed-crypto-summary-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The earning-controller API from dxFeed — 6 operation(s) for earning-controller.
  name: dxFeed Earning Controller API
  slug: dxfeed-earning-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The earning-ratio-controller API from dxFeed — 6 operation(s) for earning-ratio-controller.
  name: dxFeed Earning Ratio Controller API
  slug: dxfeed-earning-ratio-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The earning-report-controller API from dxFeed — 6 operation(s) for earning-report-controller.
  name: dxFeed Earning Report Controller API
  slug: dxfeed-earning-report-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The economic-calendar-controller API from dxFeed — 7 operation(s) for economic-calendar-controller.
  name: dxFeed Economic Calendar Controller API
  slug: dxfeed-economic-calendar-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The historical-return-controller API from dxFeed — 6 operation(s) for historical-return-controller.
  name: dxFeed Historical Return Controller API
  slug: dxfeed-historical-return-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The history-controller API from dxFeed — 2 operation(s) for history-controller.
  name: dxFeed History Controller API
  slug: dxfeed-history-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The income-statement-controller API from dxFeed — 6 operation(s) for income-statement-controller.
  name: dxFeed Income Statement Controller API
  slug: dxfeed-income-statement-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The insider-ownership-summary-controller API from dxFeed — 6 operation(s) for insider-ownership-summary-controller.
  name: dxFeed Insider Ownership Summary Controller API
  slug: dxfeed-insider-ownership-summary-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The institutional-ownership-summary-controller API from dxFeed — 6 operation(s) for institutional-ownership-summary-controller.
  name: dxFeed Institutional Ownership Summary Controller API
  slug: dxfeed-institutional-ownership-summary-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The instrument-daily-summary-controller API from dxFeed — 6 operation(s) for instrument-daily-summary-controller.
  name: dxFeed Instrument Daily Summary Controller API
  slug: dxfeed-instrument-daily-summary-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The instrument-reference-controller API from dxFeed — 5 operation(s) for instrument-reference-controller.
  name: dxFeed Instrument Reference Controller API
  slug: dxfeed-instrument-reference-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The ipo-calendar-controller API from dxFeed — 6 operation(s) for ipo-calendar-controller.
  name: dxFeed Ipo Calendar Controller API
  slug: dxfeed-ipo-calendar-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The merger-and-acquisition-controller API from dxFeed — 7 operation(s) for merger-and-acquisition-controller.
  name: dxFeed Merger And Acquisition Controller API
  slug: dxfeed-merger-and-acquisition-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The mutual-fund-ownership-summary-controller API from dxFeed — 6 operation(s) for mutual-fund-ownership-summary-controller.
  name: dxFeed Mutual Fund Ownership Summary Controller API
  slug: dxfeed-mutual-fund-ownership-summary-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The operation-ratio-controller API from dxFeed — 6 operation(s) for operation-ratio-controller.
  name: dxFeed Operation Ratio Controller API
  slug: dxfeed-operation-ratio-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The price-controller API from dxFeed — 6 operation(s) for price-controller.
  name: dxFeed Price Controller API
  slug: dxfeed-price-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The reference-change-controller API from dxFeed — 7 operation(s) for reference-change-controller.
  name: dxFeed Reference Change Controller API
  slug: dxfeed-reference-change-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The shares-ownership-summary-controller API from dxFeed — 6 operation(s) for shares-ownership-summary-controller.
  name: dxFeed Shares Ownership Summary Controller API
  slug: dxfeed-shares-ownership-summary-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The snapshot-controller API from dxFeed — 2 operation(s) for snapshot-controller.
  name: dxFeed Snapshot Controller API
  slug: dxfeed-snapshot-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The symbol-state-change-controller API from dxFeed — 2 operation(s) for symbol-state-change-controller.
  name: dxFeed Symbol State Change Controller API
  slug: dxfeed-symbol-state-change-controller-api
- baseURL: https://demo.dxfeed.com/webservice/rest
  baseurl_source: declared
  description: The valuation-ratio-controller API from dxFeed — 6 operation(s) for valuation-ratio-controller.
  name: dxFeed Valuation Ratio Controller API
  slug: dxfeed-valuation-ratio-controller-api
artifact_total: 42
asyncapis:
- description: '## Overview dxLink.WebSocket is a WebSocket-based protocol that allows you to receive market data from dxFeed services. ## Terminology - **Connection** - an instance of the WebSocket connection - **Cl'
  name: dxLink WebSocket
  slug: dxfeed-dxlink-asyncapi
collections:
- collection_type: open
  name: dxFeed Fundamentals API
  slug: open-dxfeed-fundamentals
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/dxfeed-fundamentals-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dxfeed-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dxfeed-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/dxfeed-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dxfeed-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dxfeed-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/dxfeed-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dxfeed-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dxfeed-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dxfeed.com/trust-center/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dxfeed-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dxfeed-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dxfeed-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://kb.dxfeed.com/en/getting-started.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dxfeed.com/dxfeed/api/index.html
- group: auth
  title: ''
  type: TrustCenter
  url: security/dxfeed-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dxfeed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dxfeed.com/
- group: start
  title: ''
  type: Portal
  url: https://kb.dxfeed.com/en/getting-started.html
- group: docs
  title: ''
  type: Documentation
  url: https://kb.dxfeed.com/en/index-en.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dxFeed
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dxfeed
- group: company
  title: ''
  type: Blog
  url: https://dxfeed.com/dxfeed-news/
- group: start
  title: ''
  type: SignUp
  url: https://get.dxfeed.com/
- group: operate
  title: ''
  type: Support
  url: https://dxfeed.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dxfeed.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dxfeed.com/privacy-policy/
created: '2026-07-21'
description: dxFeed is a market data distributor and subsidiary of Devexperts, headquartered in Munich, delivering real-time, delayed, historical, and on-demand financial market data across equities, ETFs, futures, options, indices, FX, fixed income, and crypto (3.5M instruments, ~200,000 simultaneous streaming clients), plus reference data (instrument profiles, corporate actions, trading schedules), Morningstar-sourced fundamentals, options analytics, and news feeds. Delivery is developer-documented but sales-gated - production credentials (endpoint URLs, login, password) arrive via onboarding after contacting sales - across a REST web service with Server-Sent Events streaming, the dxLink WebSocket protocol (public AsyncAPI spec and live demo endpoint), a binary QD protocol over TCP, FIX, file-based historical/tick data extraction, and Java/C++/.NET/Swift/Go/JavaScript/Python client libraries.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dxfeed.png
layout: provider
modified: '2026-07-22'
name: dxFeed
nav: Providers
network: true
overview: 'dxFeed publishes 32 APIs on the [APIs.io](https://apis.io/) network, including dxLink WebSocket API, Alpha Beta Controller API, Asset Classification Controller API, and 29 more. Tagged areas include Financial, Market Data, Real-Time, Historical Data, and Equities.


  The dxFeed catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  dxFeed''s developer surface includes authentication, sandbox, getting-started guide, API reference, developer portal, documentation, engineering blog, and 21 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 45.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 50.5
    developer_ergonomics: 73.2
    discoverability: 59.3
    governance: 4.5
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 45.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dxfeed/refs/heads/main/screenshots/dxfeed-2026-07-22T202337.png
security:
- kind: authentication
  name: Dxfeed Authentication
  slug: dxfeed-authentication
  summary_line: http-basic (login/password credentials)/dxLink AUTH token (protocol message) · 3 schemes
- kind: domain-security
  name: Dxfeed Domain Security
  slug: dxfeed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Dxfeed Trust Center
  slug: dxfeed-trust-center
  summary_line: SOC 2
slug: dxfeed
tags:
- Financial
- Market Data
- Real-Time
- Historical Data
- Equities
- Options
- Futures
- Crypto
- Reference Data
- Fundamentals
website: https://dxfeed.com/
---
