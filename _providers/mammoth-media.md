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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: REST + GraphQL API for TokenBot copy-trading — manage exchange accounts, strategies, copiers, trades, notifications, rewards, withdrawals, API keys, and webhooks. API-key or secp256k1 signed-request a
  name: TokenBot API
  slug: tokenbot-api
artifact_total: 6
asyncapis:
- description: ''
  name: Mammoth Media Webhooks
  slug: mammoth-media-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.tokenbot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tokenbot.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tokenbot.com/home/api-docs/readme
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tokenbot.com/home/api-docs/rest-api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tokenbot.com/home/api-docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/mammoth-media-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tokenbot-org
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tokenbot.com
- group: start
  title: ''
  type: SignUp
  url: https://dev.tokenbot.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.tokenbot.com/home/legal-information/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.tokenbot.com/home/legal-information/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@tokenbot.com
- group: other
  title: ''
  type: X
  url: https://x.com/tokenbot
- group: build
  title: ''
  type: Packages
  url: packages/mammoth-media-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mammoth-media-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/mammoth-media-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mammoth-media-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mammoth-media-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mammoth-media-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mammoth-media-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mammoth-media-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mammoth-media-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mammoth-media-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mammoth-media-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mammoth-media-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mammoth-media-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mammoth-media-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mammoth-media-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mammoth-media-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mammoth Media is a Greylock-backed consumer technology company whose current product is TokenBot (mammoth.la now redirects to tokenbot.com) — a social, copy-trading platform for cryptocurrency communities on Discord and Telegram that synchronizes algorithmic trades across 12+ exchanges in real time. For developers TokenBot exposes a documented REST API (api.tokenbot.com/v1), a GraphQL API, HMAC-signed webhooks with 46 event types, a stdio Model Context Protocol (MCP) server exposing 25 tools, and a first-party `tokenbot` CLI distributed via npm and Homebrew. Authentication is API-key (tb_live_/tb_test_) or a secp256k1 signed-request fast-path; the CLI-first design keeps exchange keys under user control (trade-only permissions, no withdrawal access).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mammoth-media.png
layout: provider
mcp_servers:
- description: ''
  name: mammoth-media-mcp.yml
  slug: mammoth-media-mcpyml
modified: '2026-07-20'
name: Mammoth Media
nav: Providers
network: true
overview: 'Mammoth Media publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Cryptocurrency, Trading, and Copy Trading.


  The Mammoth Media catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mammoth Media''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, support, CLI, and 23 more developer resources.'
random_paper: 36
rate_limits:
- limit_count: 2
  name: Mammoth Media Rate Limits
  slug: mammoth-media-rate-limits
score:
  band: developing
  composite: 49.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 79.9
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 50.0
  previous_composite: 49.9
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mammoth-media/refs/heads/main/screenshots/mammoth-media-2026-07-25T230015.png
security:
- kind: authentication
  name: Mammoth Media Authentication
  slug: mammoth-media-authentication
  summary_line: apiKey/http/signed-request/jwt · 5 schemes
- kind: domain-security
  name: Mammoth Media Domain Security
  slug: mammoth-media-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mammoth-media
tags:
- Company
- Consumer
- Cryptocurrency
- Trading
- Copy Trading
- Fintech
- Webhooks
- MCP
- Developer Tools
- CLI
website: https://www.tokenbot.com
---
