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
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 66.2
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Clear Street Agentic Access
  operation_count: 98
  slug: clear-street-agentic-access
  summary_line: 98 operations · 35 acting
api_count: 4
apis:
- description: 'A unified RESTful API for client interactions with the Clear Street Active trading platform: accounts and balances, order submission/replacement/cancellation, executions, positions and position instru'
  name: Clear Street Trading API
  slug: trading-api
- description: The Clear Street Studio prime-brokerage API — an integrated Risk Management, Portfolio Management and Execution Management surface. Covers entities and accounts, holdings, orders and bulk orders, trad
  name: Clear Street Studio API
  slug: studio-api
- description: Clear Street's official remote Model Context Protocol server, exposing the Clear Street Trading API to AI assistants such as Claude and Gemini. OAuth-protected per RFC 9728 — an anonymous request retu
  name: Clear Street MCP Server
  slug: mcp
- description: Clear Street's legacy post-trade API for booking and cancelling trades and for submitting bulk trade-file uploads. Published as a Swagger 2.0 document in the clear-street/docs GitHub repository alongs
  name: Clear Street API (Trades and Uploads)
  slug: legacy-api
artifact_total: 12
asyncapis:
- description: ''
  name: Clear Street Studio Events
  slug: clear-street-studio-events
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
overview: 'Clear Street publishes 3 APIs on the [APIs.io](https://apis.io/) network: Trading API, Studio API, and API (Trades and Uploads). Tagged areas include Company, Financial Services, Capital Markets, Prime Brokerage, and Trading.


  The Clear Street catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Clear Street''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, CLI, and 31 more developer resources.'
random_paper: 97
scopes:
- name: Clear Street Scopes
  scope_count: 5
  slug: clear-street-scopes
  summary_line: 5 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 64.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.9
    developer_ergonomics: 87.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 64.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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
