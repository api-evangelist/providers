---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: 'IQX is the IntelligentCross proprietary market data feed. It disseminates all visible ASPEN resting orders, cancels for ASPEN visible orders, and all ASPEN executions, plus per-symbol reference data, '
  name: IntelligentCross IQX Market Data Feed
  slug: intelligentcross-iqx-market-data-feed
- description: Order entry into the IntelligentCross ATS books (Midpoint, ASPEN Fee/Fee, ASPEN Maker/Taker, ASPEN Taker/Maker) is accepted only over FIX connections; the ATS currently supports FIX 4.2. Subscribers m
  name: IntelligentCross FIX Order Entry API
  slug: intelligentcross-fix-order-entry-api
artifact_total: 5
asyncapis:
- description: ''
  name: Imperative Execution Iqx Asyncapi
  slug: imperative-execution-iqx-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.imperativex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.imperativex.com/market-data
- group: docs
  title: ''
  type: APIReference
  url: http://iqx.imperativex.com/IntelligentCrossMarketDataFeedSpec.v.1.11.pdf
- group: operate
  title: ''
  type: Support
  url: https://www.imperativex.com/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.imperativex.com/faq
- group: company
  title: ''
  type: Blog
  url: https://www.imperativex.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.imperativex.com/disclaimers
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.imperativex.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001746102&type=ATS-N&dateb=&owner=include&count=40
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/imperative-execution_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/imperative-execution-llms.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/imperative-execution-iqx-asyncapi.yml
- group: build
  title: ''
  type: Examples
  url: examples/imperative-execution-iqx-sample-data.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/imperative-execution-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/imperative-execution-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/imperative-execution-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imperative-execution-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/imperative-execution-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/imperative-execution-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/imperative-execution-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imperative-execution-domain-security.yml
created: '2026-08-04'
description: Imperative Execution is a New York financial technology company and the parent of IntelligentCross, an SEC-registered US equities Alternative Trading System (ATS) that applies machine learning to order matching and price discovery. IntelligentCross operates a non-displayed Midpoint book and ASPEN, a full limit order book with optional displayed capability that is split into three independent books by fee model (Fee/Fee, Maker/Taker, Taker/Maker), all under MPID INCR, with primary matching engines in the Equinix NY4 data center in Secaucus, New Jersey. Registered broker-dealer subscribers reach the venue for order entry over FIX 4.2 across Pico cross-connects, and the venue publishes its own IQX market data feed - a binary, multicast-UDP full depth-of-book and execution feed whose message specification, recovery/rerequest specification, daily symbol mapping file and sample PCAP captures are all published openly.
image: https://cdn.prod.website-files.com/5ee92e3bd621402efc7f2d3f/67e1c4d359b8c0966be92f8d_intelligentCross-logo.png
layout: provider
modified: '2026-08-04'
name: Imperative Execution
nav: Providers
network: true
overview: 'Imperative Execution publishes 1 API on the [APIs.io](https://apis.io/) network: IntelligentCross IQX Market Data Feed. Tagged areas include Company, Financial Services, Capital Markets, Trading, and Market Data.


  The Imperative Execution catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Imperative Execution''s developer surface includes documentation, API reference, support, engineering blog, code examples, sandbox, changelog, and 14 more developer resources.'
random_paper: 63
score:
  band: thin
  composite: 36.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 39.5
    developer_ergonomics: 39.1
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 36.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imperative-execution/refs/heads/main/screenshots/imperative-execution-2026-08-07T170628.png
security:
- kind: authentication
  name: Imperative Execution Authentication
  slug: imperative-execution-authentication
  summary_line: none-public/network-access-control/contractual-eligibility · 4 schemes
- kind: domain-security
  name: Imperative Execution Domain Security
  slug: imperative-execution-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imperative-execution
tags:
- Company
- Financial Services
- Capital Markets
- Trading
- Market Data
- Equities
- Alternative Trading System
- FIX Protocol
- Multicast Market Data
- Fintech
website: https://www.imperativex.com/
---
