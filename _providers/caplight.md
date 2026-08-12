---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Caplight Agentic Access
  operation_count: 26
  slug: caplight-agentic-access
  summary_line: 26 operations
api_count: 17
apis:
- description: Hosted, remote MCP server that connects Claude.ai and Claude Desktop to the Caplight dataset. Caplight documents 15 tools spanning live MarketPrice quotes and price history, the secondary order book a
  name: Caplight MCP Server
  slug: caplight-mcp-server
- description: The Companies API from Caplight — 1 operation(s) for companies.
  name: Caplight Companies API
  slug: caplight-companies-api
- description: The Company API from Caplight — 3 operation(s) for company.
  name: Caplight Company API
  slug: caplight-company-api
- description: 'Canonical Company resource: identity (name, legal name, location), descriptions, and the latest LLM-generated firmographic tags (sectors / verticals / keywords with attribution).'
  name: Caplight Company Details API
  slug: caplight-company-details-api
- description: COI (Certificate of Incorporation) filings and related company documents
  name: Caplight Company Filings API
  slug: caplight-company-filings-api
- description: Resolves company domains, PitchBook IDs and v1 company IDs to v2 company IDs, in batches.
  name: Caplight Company Lookup API
  slug: caplight-company-lookup-api
- description: The Composite Index API from Caplight — 3 operation(s) for composite index.
  name: Caplight Composite Index API
  slug: caplight-composite-index-api
- description: LLM-discovered comparable companies with an overall similarity score, a per-dimension breakdown, a classification, and a short rationale.
  name: Caplight Comps API
  slug: caplight-comps-api
- description: Mutual fund mark-to-market valuations from SEC filings
  name: Caplight Fund Marks API
  slug: caplight-fund-marks-api
- description: Funding round data including amounts, valuations, participants, and citations
  name: Caplight Funding Rounds API
  slug: caplight-funding-rounds-api
- description: Investor participation data for companies
  name: Caplight Investors API
  slug: caplight-investors-api
- description: The Live Orderbook API from Caplight — 1 operation(s) for live orderbook.
  name: Caplight Live Orderbook API
  slug: caplight-live-orderbook-api
- description: Caplight's proprietary MarketPrice estimate, calculated using executed trades, company primary rounds, bids/offers, fund marks, 409a valuations, and comps performance.
  name: Caplight Market Price API
  slug: caplight-marketprice-api
- description: Company news articles with sentiment analysis
  name: Caplight News API
  slug: caplight-news-api
- description: The Order History API from Caplight — 1 operation(s) for order history.
  name: Caplight Order History API
  slug: caplight-order-history-api
- description: The Stock Splits API from Caplight — 1 operation(s) for stock splits.
  name: Caplight Stock Splits API
  slug: caplight-stock-splits-api
- description: The Trade History API from Caplight — 1 operation(s) for trade history.
  name: Caplight Trade History API
  slug: caplight-trade-history-api
artifact_total: 22
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/caplight-rest-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/caplight-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.caplight.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.caplight.com/
- group: docs
  title: ''
  type: Documentation
  url: https://platform.caplight.com/api/documentation.html
- group: docs
  title: ''
  type: APIReference
  url: https://platform.caplight.com/api/documentation.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.caplight.com/products/api
- group: company
  title: ''
  type: Blog
  url: https://www.caplight.com/insights
- group: start
  title: ''
  type: SignUp
  url: https://platform.caplight.com/signup
- group: start
  title: ''
  type: Login
  url: https://platform.caplight.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caplight.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caplight.com/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.caplight.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/caplight-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/caplight-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/caplight-conventions.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/caplight-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/caplight-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/caplight-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/caplight-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/caplight-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/caplight-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/caplight-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/caplight-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/caplight-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/caplight-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/caplight-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-09'
description: Caplight Technologies is a San Francisco private-markets data and trading platform for institutional investors, covering 50,000+ VC-backed private companies with secondary-market pricing, a live institutional order book, trade and order history, funding rounds with valuations and participants, investor participation, SEC-derived fund marks, COI filings, stock splits, news, company signals and comparable-company indices. Its proprietary MarketPrice(TM) estimate is implied from live bids, asks and closed secondary trades. Caplight exposes the dataset through a versioned REST API (v1 and v2, api_key header auth, documented with a public OpenAPI 3.1.0 definition rendered in Redoc), a hosted OAuth-protected MCP server for Claude, and a one-line embeddable widget. Securities are offered through Caplight Markets LLC, member FINRA/SIPC.
image: https://www.caplight.com/assets/og/og-image-2026.png
layout: provider
mcp_servers:
- description: ''
  name: caplight-mcp.yml
  slug: caplight-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-09'
name: Caplight
nav: Providers
network: true
overview: 'Caplight publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Company API, Company Details API, and 13 more. Tagged areas include private-markets, secondary-market, market-data, venture-capital, and company-data.


  Caplight''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, changelog, authentication, and 21 more developer resources.'
random_paper: 32
score:
  band: developing
  composite: 46.2
  delta: -0.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 57.9
    developer_ergonomics: 64.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Caplight Authentication
  slug: caplight-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Caplight Domain Security
  slug: caplight-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: caplight
tags:
- private-markets
- secondary-market
- market-data
- venture-capital
- company-data
- investor-data
- funding-rounds
- pricing-data
- financial-data
- fintech
- mcp
- agent-native
website: https://www.caplight.com/
---
