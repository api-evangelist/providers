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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Dialect Agentic Access
  operation_count: 40
  slug: dialect-agentic-access
  summary_line: 40 operations · 22 acting
api_count: 9
apis:
- description: The Blink API from Dialect — 2 operation(s) for blink.
  name: Dialect Blink API
  slug: dialect-blink-api
- description: The Blink Data Table API from Dialect — 1 operation(s) for blink data table.
  name: Dialect Blink Data Table API
  slug: dialect-blink-data-table-api
- description: The Blink Lists API from Dialect — 1 operation(s) for blink lists.
  name: Dialect Blink Lists API
  slug: dialect-blink-lists-api
- description: The Blink Preview API from Dialect — 1 operation(s) for blink preview.
  name: Dialect Blink Preview API
  slug: dialect-blink-preview-api
- description: The Channels API from Dialect — 7 operation(s) for channels.
  name: Dialect Channels API
  slug: dialect-channels-api
- description: The Inbox API from Dialect — 17 operation(s) for inbox.
  name: Dialect Inbox API
  slug: dialect-inbox-api
- description: The Markets API from Dialect — 3 operation(s) for markets.
  name: Dialect Markets API
  slug: dialect-markets-api
- description: The Positions API from Dialect — 3 operation(s) for positions.
  name: Dialect Positions API
  slug: dialect-positions-api
- description: The Send API from Dialect — 4 operation(s) for send.
  name: Dialect Send API
  slug: dialect-send-api
artifact_total: 14
asyncapis:
- description: ''
  name: Dialect Webhooks
  slug: dialect-webhooks
common:
- group: build
  title: ''
  type: Packages
  url: packages/dialect-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/dialect-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dialect-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dialect-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/dialect-alerts-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/dialect-blinks-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/dialect-markets-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/dialect-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dialect-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dialect-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dialect-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dialect-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/dialect-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dialect-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dialect-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/dialect-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dialect-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dialect-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dialect-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.dialect.to/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dialect.to/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dialect.to/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dialect.to/api-reference/send-alerts/send-alert
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dialect.to/alerts/quick-start
- group: company
  title: ''
  type: Blog
  url: https://www.dialect.to/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dialectlabs
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.dialect.to
- group: start
  title: ''
  type: Login
  url: https://dashboard.dialect.to
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/saydialect
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.dialect.to/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.dialect.to/privacy
created: '2026-07-17'
description: Dialect is a Web3 UX infrastructure company on Solana that provides onchain transactions and notifications native to any digital experience. Its two flagship products are Blinks (Blockchain Links — one-click, embeddable onchain transactions powered by a Standard Blinks Library of 40+ protocol integrations including Jupiter, Kamino, Drift and DeFiTuna) and the Alerts Stack (real-time, multi-channel notifications across push, email, Telegram and an in-app universal inbox, with event detection for price-change and trending-token signals). Dialect also exposes a Markets & Positions API for real-time DeFi rates, TVL and wallet position tracking, plus a hosted MCP server for agents. The developer surface spans three REST APIs (Alerts V2, Blinks, Markets), TypeScript/React SDKs, a no-code dashboard, and an open-source monitor framework. Backed by Electric Capital and Multicoin Capital.
image: https://www.dialect.to/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: dialect-mcp.yml
  slug: dialect-mcpyml
modified: '2026-07-18'
name: Dialect
nav: Providers
network: true
overview: 'Dialect publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Blink API, Blink Data Table API, Blink Lists API, and 6 more. Tagged areas include Company, Infrastructure, Web3, Blockchain, and Solana.


  The Dialect catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Dialect''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, engineering blog, and 25 more developer resources.'
random_paper: 30
score:
  band: developing
  composite: 49.6
  delta: -0.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 64.9
    developer_ergonomics: 75.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dialect/refs/heads/main/screenshots/dialect-2026-07-25T211909.png
security:
- kind: authentication
  name: Dialect Authentication
  slug: dialect-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Dialect Domain Security
  slug: dialect-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dialect
tags:
- Company
- Infrastructure
- Web3
- Blockchain
- Solana
- Notifications
- Messaging
- Alerts
- DeFi
- Payments
- Agents
- MCP
website: https://www.dialect.to/
---
