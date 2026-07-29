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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Tradier Agentic Access
  operation_count: 28
  slug: tradier-agentic-access
  summary_line: 28 operations · 9 acting
api_count: 3
apis:
- description: The Tradier Brokerage API provides REST endpoints for placing equity, option, and multileg orders, retrieving account balances, positions, orders, and history, and accessing market data including quot
  name: Tradier Brokerage API
  slug: brokerage-api
- description: The Tradier Streaming API delivers real-time market and account events over HTTP and WebSocket. Quote, trade, summary, timesale, and order events are streamed; client first creates a session via the b
  name: Tradier Streaming API
  slug: streaming-api
- description: Tradier's official hosted MCP server (launched July 2026) connects AI assistants like ChatGPT, Claude, Gemini CLI, and Cursor directly to a Tradier brokerage account over Streamable HTTP. It exposes 2
  name: Tradier MCP Server
  slug: mcp-server
artifact_total: 14
asyncapis:
- description: AsyncAPI 2.6 description of Tradier's WebSocket streaming for market events and account events. A streaming session must first be created via the brokerage REST endpoints (POST /v1/markets/events/sess
  name: Tradier Streaming WebSocket API
  slug: tradier-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tradier-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tradier-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tradier-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradier-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tradier
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tradier
- group: start
  title: ''
  type: Portal
  url: https://tradier.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tradier.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://tradier.com/individuals/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tradier.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/tradier-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tradier-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tradier-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.tradier.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.tradier.com/blog/rss.xml
- group: auth
  title: ''
  type: Security
  url: https://tradier.com/legal/vulnerability-disclosure-policy
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tradier.com/reference/brokerage-api-user-get-profile
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tradier.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.tradier.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tradier.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tradier.com/legal/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://dash.tradier.com/sign-up
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tradier-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tradier-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tradier-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tradier-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tradier-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/tradier-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tradier-packages.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tradier-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tradier-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tradier-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tradier-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tradier-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tradier-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tradier-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tradier-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tradier-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tradier-brokerage-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-05-08'
description: Tradier is a brokerage platform offering REST and WebSocket APIs for trading US equities, options, and futures, plus market data and account-opening services. The Tradier Brokerage API exposes account, trading, market data, fundamentals, watchlist, and streaming endpoints under a single base URL.
finops:
- name: Tradier Finops
  service_category: Fintech
  slug: tradier-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tradier.png
layout: provider
mcp_servers:
- description: ''
  name: tradier-mcp.yml
  slug: tradier-mcpyml
modified: '2026-07-22'
name: Tradier
nav: Providers
network: true
overview: 'Tradier publishes 2 APIs on the [APIs.io](https://apis.io/) network: Brokerage API and Streaming API. Tagged areas include Fintech, Trading, Stocks, Options, and Brokerage.


  The Tradier catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Tradier''s developer surface includes authentication, developer portal, documentation, pricing, engineering blog, API reference, getting-started guide, and 33 more developer resources.'
plans:
- name: Tradier Plans Pricing
  plan_count: 3
  slug: tradier-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 4
  name: Tradier Rate Limits
  slug: tradier-rate-limits
rules:
- name: Tradier API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: tradier-asyncapi-spectral-rules
scopes:
- name: Tradier Scopes
  scope_count: 5
  slug: tradier-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.0
  delta: -3.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 56.8
    developer_ergonomics: 75.5
    discoverability: 92.6
    governance: 53.1
    operational_transparency: 78.9
  previous_composite: 76.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 78.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tradier/refs/heads/main/screenshots/tradier-2026-06-20T195526.png
security:
- kind: authentication
  name: Tradier Authentication
  slug: tradier-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Tradier Domain Security
  slug: tradier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tradier Vulnerability Disclosure
  slug: tradier-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tradier
tags:
- Fintech
- Trading
- Stocks
- Options
- Brokerage
- Streaming
website: https://tradier.com/
---
