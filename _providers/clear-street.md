---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 61.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Clear Street Agentic Access
  operation_count: 98
  slug: clear-street-agentic-access
  summary_line: 98 operations · 35 acting
api_count: 23
apis:
- description: Clear Street's official remote Model Context Protocol server, exposing the Clear Street Trading API to AI assistants such as Claude and Gemini. OAuth-protected per RFC 9728 — an anonymous request retu
  name: Clear Street MCP Server
  slug: mcp
- description: Clear Street's legacy post-trade API for booking and cancelling trades and for submitting bulk trade-file uploads. Published as a Swagger 2.0 document in the clear-street/docs GitHub repository alongs
  name: Clear Street API (Trades and Uploads)
  slug: legacy-api
- description: The Accounts API from Clear Street — 6 operation(s) for accounts.
  name: Clear Street Accounts API
  slug: clear-street-accounts-api
- description: Endpoints for API service metadata.
  name: Clear Street API version API
  slug: clear-street-api-version-api
- description: Access clocks and financial calendars for market sessions and events.
  name: Clear Street Calendar API
  slug: clear-street-calendar-api
- description: The Entities API from Clear Street — 2 operation(s) for entities.
  name: Clear Street Entities API
  slug: clear-street-entities-api
- description: The Holdings API from Clear Street — 1 operation(s) for holdings.
  name: Clear Street Holdings API
  slug: clear-street-holdings-api
- description: Retrieve instrument analytics, market data, news, and related reference data.
  name: Clear Street Instrument Data API
  slug: clear-street-instrument-data-api
- description: The Instruments API from Clear Street — 6 operation(s) for instruments.
  name: Clear Street Instruments API
  slug: clear-street-instruments-api
- description: The Inventories API from Clear Street — 1 operation(s) for inventories.
  name: Clear Street Inventories API
  slug: clear-street-inventories-api
- description: The Locates API from Clear Street — 2 operation(s) for locates.
  name: Clear Street Locates API
  slug: clear-street-locates-api
- description: The Margin API from Clear Street — 2 operation(s) for margin.
  name: Clear Street Margin API
  slug: clear-street-margin-api
- description: The Margin Simulations API from Clear Street — 2 operation(s) for margin simulations.
  name: Clear Street Margin Simulations API
  slug: clear-street-margin-simulations-api
- description: Thread-centric AI assistant for conversational trading. Create threads to start conversations, poll response objects for in-progress output, and read finalized messages from thread history. Thread/mes
  name: Clear Street Omni AI API
  slug: clear-street-omni-ai-api
- description: The Orders API from Clear Street — 6 operation(s) for orders.
  name: Clear Street Orders API
  slug: clear-street-orders-api
- description: The Performance API from Clear Street — 1 operation(s) for performance.
  name: Clear Street Performance API
  slug: clear-street-performance-api
- description: The PNL API from Clear Street — 3 operation(s) for pnl.
  name: Clear Street PNL API
  slug: clear-street-pnl-api
- description: The Positions API from Clear Street — 6 operation(s) for positions.
  name: Clear Street Positions API
  slug: clear-street-positions-api
- description: The Rates API from Clear Street — 1 operation(s) for rates.
  name: Clear Street Rates API
  slug: clear-street-rates-api
- description: Search instruments and manage saved screeners.
  name: Clear Street Screener API
  slug: clear-street-screener-api
- description: Trade endpoints are used to insert or cancel trades into a our systems.
  name: Clear Street Trades API
  slug: clear-street-trades-api
- description: 'Upload endpoints allow you to upload a `CSV` file that contain trades, in the same format as our <b>[trade-file specification](https://github.com/clear-street/docs/blob/master/trade_file.md)</b>. You '
  name: Clear Street Uploads API
  slug: clear-street-uploads-api
- description: Create and manage watchlists.
  name: Clear Street Watchlist API
  slug: clear-street-watchlist-api
artifact_total: 53
asyncapis:
- description: ''
  name: Clear Street Studio Events
  slug: clear-street-studio-events
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clear Street Accounts API
  slug: open-clear-street-accounts-api
- collection_type: open
  name: Clear Street Trading API version API
  slug: open-clear-street-api-version-api
- collection_type: open
  name: Clear Street Trading Calendar API
  slug: open-clear-street-calendar-api
- collection_type: open
  name: Common API Models Entities API
  slug: open-clear-street-entities-api
- collection_type: open
  name: Common API Models Holdings API
  slug: open-clear-street-holdings-api
- collection_type: open
  name: Clear Street Trading Instrument Data API
  slug: open-clear-street-instrument-data-api
- collection_type: open
  name: Clear Street Instruments API
  slug: open-clear-street-instruments-api
- collection_type: open
  name: Common API Models Inventories API
  slug: open-clear-street-inventories-api
- collection_type: open
  name: Common API Models Locates API
  slug: open-clear-street-locates-api
- collection_type: open
  name: Common API Models Margin API
  slug: open-clear-street-margin-api
- collection_type: open
  name: Common API Models Margin Simulations API
  slug: open-clear-street-margin-simulations-api
- collection_type: open
  name: Clear Street Trading Omni AI API
  slug: open-clear-street-omni-ai-api
- collection_type: open
  name: Clear Street Orders API
  slug: open-clear-street-orders-api
- collection_type: open
  name: Common API Models Performance API
  slug: open-clear-street-performance-api
- collection_type: open
  name: Common API Models PNL API
  slug: open-clear-street-pnl-api
- collection_type: open
  name: Clear Street Positions API
  slug: open-clear-street-positions-api
- collection_type: open
  name: Common API Models Rates API
  slug: open-clear-street-rates-api
- collection_type: open
  name: Clear Street Trading Screener API
  slug: open-clear-street-screener-api
- collection_type: open
  name: Clear Street Trades API
  slug: open-clear-street-trades-api
- collection_type: open
  name: Clear Street Uploads API
  slug: open-clear-street-uploads-api
- collection_type: open
  name: Clear Street Trading Watchlist API
  slug: open-clear-street-watchlist-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clear-street-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearstreet.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.clearstreet.com/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.clearstreet.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clearstreet.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clearstreet.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.clearstreet.com/
- group: start
  title: ''
  type: Login
  url: https://auth.clearstreet.io/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clearstreet.io/legal/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clearstreet.io/legal/regulatory-disclosures
- group: operate
  title: ''
  type: Support
  url: https://www.clearstreet.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.clearstreet.io/news/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clear-street
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clear-street-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/clear-street-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clear-street-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/clear-street-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clear-street-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/clear-street-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/clear-street-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clear-street-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clear-street-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/clear-street-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/clear-street-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clear-street-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clear-street-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.clearstreet.com/changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clear-street-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clear-street-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.clearstreet.io/legal/clear-street-trust-center
- group: auth
  title: ''
  type: TrustCenter
  url: security/clear-street-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.clearstreet.io/legal/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/clear-street-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clear-street-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/clear-street-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/clear-street-studio-events.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clear-street-data-model.yml
created: '2026-08-02'
description: 'Clear Street is a New York–based financial technology firm building independent, cloud-native prime brokerage, clearing, and execution infrastructure for institutional and active individual traders. It is a FINRA/SIPC member broker-dealer, a CFTC-registered Futures Commission Merchant, and FCA-authorised in the UK. Clear Street ships three public API surfaces: the Clear Street Trading API (OpenAPI 3.1, api.clearstreet.com) covering accounts, orders, executions, positions, instruments, market data, screeners, watchlists and the Omni AI financial copilot; the Clear Street Studio API (OpenAPI 3.0, prime-brokerage holdings, locates, easy-borrows, P&L, and Reg-T/portfolio margin) with a companion WebSocket activity stream; and an OAuth-protected remote MCP server for AI agents. First-party SDKs ship for Python, TypeScript, Go and Kotlin/Java, alongside a Go CLI (clst) and a published set of open Agent Skills.'
image: https://clear-street.github.io/docs/assets/logo.png
layout: provider
mcp_servers:
- description: ''
  name: clear-street-mcp.yml
  slug: clear-street-mcpyml
modified: '2026-08-02'
name: Clear Street
nav: Providers
network: true
overview: 'Clear Street publishes 22 APIs on the [APIs.io](https://apis.io/) network, including API (Trades and Uploads), Accounts API, API version API, and 19 more. Tagged areas include Company, Financial Services, Capital Markets, Prime Brokerage, and Trading.


  The Clear Street catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Clear Street''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, CLI, and 31 more developer resources.'
random_paper: 9
scopes:
- name: Clear Street Scopes
  scope_count: 5
  slug: clear-street-scopes
  summary_line: 5 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 66.8
  delta: 2.9
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 68.6
    developer_ergonomics: 85.7
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 44.7
  previous_composite: 63.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clear-street/refs/heads/main/screenshots/clear-street-2026-08-07T163444.png
security:
- kind: authentication
  name: Clear Street Authentication
  slug: clear-street-authentication
  summary_line: http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Clear Street Domain Security
  slug: clear-street-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clear Street Vulnerability Disclosure
  slug: clear-street-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Clear Street Trust Center
  slug: clear-street-trust-center
  summary_line: SOC 2 Type II
slug: clear-street
tags:
- Company
- Financial Services
- Capital Markets
- Prime Brokerage
- Trading
- Brokerage
- Clearing
- Market Data
- Fintech
- Investing
website: https://www.clearstreet.io/
---
