---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://api.upstox.com
  baseurl_source: declared
  description: The Upstox Developer API is a free OAuth 2.0 REST and WebSocket suite for building trading and investment applications against a live SEBI-registered brokerage account. It covers order placement, modi
  name: Upstox Developer API
  slug: upstox-developer-api
- description: Upstox operates a hosted, OAuth-protected Model Context Protocol server at https://mcp.upstox.com/mcp that gives AI assistants — Claude Desktop and the Claude web app, Claude Code, ChatGPT in Develope
  name: Upstox MCP Server
  slug: upstox-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Upstox Webhooks
  slug: upstox-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://upstox.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://upstox.com/trading-api/
- group: docs
  title: ''
  type: Documentation
  url: https://upstox.com/developer/api-documentation/open-api
- group: docs
  title: ''
  type: APIReference
  url: https://upstox.com/developer/api-documentation/api-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://upstox.com/developer/api-documentation/installing-sdk
- group: operate
  title: ''
  type: Support
  url: https://upstox.com/help-center/
- group: operate
  title: ''
  type: Community
  url: https://community.upstox.com/
- group: company
  title: ''
  type: Blog
  url: https://upstox.com/market-talk/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upstox
- group: commercial
  title: ''
  type: Pricing
  url: https://upstox.com/brokerage-charges/
- group: start
  title: ''
  type: SignUp
  url: https://upstox.com/open-demat-account/
- group: start
  title: ''
  type: Login
  url: https://login.upstox.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upstox.com/terms-of-use-and-privacy-policy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upstox.com/terms-of-use-and-privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://gist.github.com/Rahulzz/a0da2ad28a7dcc81e887f24cfdbc80a8
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upstox.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/upstox-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/upstox-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/upstox-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://upstox.com/bug-bounty/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/upstox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/upstox-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/upstox-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/upstox-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upstox-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upstox-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/upstox-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/upstox-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/upstox-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/upstox-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/upstox-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/upstox-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/upstox-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/upstox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/upstox-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/upstox-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/upstox-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/upstox-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/upstox-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/upstox-webhooks.yml
created: '2026-09-02'
description: Upstox is a SEBI-registered Indian retail brokerage operated by Upstox Securities Private Limited, a wholly owned subsidiary of RKSV Securities India Private Limited, serving over 1.3 crore customers across equities, futures and options, commodities, currency, mutual funds, IPOs, NCDs, fixed deposits and insurance on NSE, BSE and MCX. Its Upstox Developer API is a free, OAuth 2.0 protected REST and WebSocket suite of 101 published operations covering order placement (including V3 slicing, multi-order and GTT/trailing-stop-loss), portfolio holdings and positions, funds and margin, brokerage and charge calculation, market quotes with option greeks, historical and intraday candles, expired-instrument history, company fundamentals, IPO application, mutual funds, payouts, news and market-information analytics. Upstox also runs a hosted, OAuth-protected Model Context Protocol server at mcp.upstox.com giving AI agents read-only access to a user's holdings, orders, positions, mutual
  funds, funds and profile, and publishes an official Agent Skill and Claude plugin marketplace alongside first-party SDKs for Python, Node.js, Java, PHP and .NET.
image: https://assets.upstox.com/website/images/upstox-new-logo.svg
layout: provider
mcp_servers:
- description: 'Upstox operates a first-party hosted Model Context Protocol server that gives an AI assistant read-only access to a connected Upstox brokerage account. It is a genuine agent surface: an MCP client POS'
  name: Upstox MCP Server
  slug: upstox-mcp-server
modified: '2026-09-02'
name: Upstox
nav: Providers
network: true
overview: 'Upstox publishes 1 API on the [APIs.io](https://apis.io/) network: Developer API. Tagged areas include Company, Financial Services, Stock Trading, Brokerage, and Market Data.


  The Upstox catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Upstox''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Upstox Plans Pricing
  plan_count: 3
  slug: upstox-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 17
  name: Upstox Rate Limits
  slug: upstox-rate-limits
scopes:
- name: Upstox Scopes
  scope_count: 2
  slug: upstox-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: exemplar
  composite: 79.8
  coverage:
    artifact_dirs: 20
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 62.6
    developer_ergonomics: 83.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 94.7
  previous_composite: 79.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 86.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Upstox Authentication
  slug: upstox-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Upstox Domain Security
  slug: upstox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Upstox Vulnerability Disclosure
  slug: upstox-vulnerability-disclosure
  summary_line: Hackerone · security.txt
- kind: trust-center
  name: Upstox Trust Center
  slug: upstox-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO 22301:2019
slug: upstox
tags:
- Company
- Financial Services
- Stock Trading
- Brokerage
- Market Data
- Investing
- Capital Markets
- Mutual Funds
- Algorithmic Trading
- India
website: https://upstox.com/
---
