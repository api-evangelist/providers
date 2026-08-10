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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: End Game Agentic Access
  operation_count: 5
  slug: end-game-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: The Threads API from Endgame — 2 operation(s) for threads.
  name: Endgame Threads API
  slug: end-game-threads-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/end-game-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/end-game-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/end-game-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/end-game-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.endgame.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.endgame.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.endgame.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.endgame.io/api-reference/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.endgame.io/api-reference/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://docs.endgame.io/api-reference/authentication
- group: agent
  title: ''
  type: MCPServer
  url: mcp/end-game-mcp.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/end-game-openapi.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/end-game-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.endgame.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.endgame.io/status
- group: operate
  title: ''
  type: Support
  url: https://docs.endgame.io/contact
- group: company
  title: ''
  type: Blog
  url: https://www.endgame.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.endgame.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.endgame.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.endgame.io/trust/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://docs.endgame.io/trust/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://docs.endgame.io/vdp
- group: auth
  title: ''
  type: Security
  url: https://docs.endgame.io/vdp
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/end-game-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/end-game-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/end-game-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/end-game-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/end-game-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/end-game-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/end-game-openapi-overlay.yaml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/end-game-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Endgame (Endgame Labs, Inc.) is a context graph platform for go-to-market teams and AI agents that turns sales calls, CRM records, emails, Slack conversations, meeting transcripts, and uploaded documents into structured, queryable revenue intelligence. Sales and RevOps users ask questions across their book of business in natural language, and connected AI assistants reach the same knowledge through the Endgame MCP Server. The public REST API (rooted at /api/v1) lets developers create and manage Endgame threads programmatically over HTTPS with Bearer-token authentication, while a broad connector surface ingests context from Salesforce, Gong, Chorus, Clari Copilot, Zoom, Notion, Confluence, Highspot, Seismic, Snowflake, Slack, Microsoft Teams/SharePoint/Outlook, and Google Drive. Endgame was surfaced through the API Evangelist VC-portfolio pipeline and has been enriched from its published developer documentation, OpenAPI, MCP server, and trust/security programs.
image: https://www.endgame.io/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: end-game-mcp.yml
  slug: end-game-mcpyml
modified: '2026-07-19'
name: Endgame
nav: Providers
network: true
overview: 'Endgame publishes 1 API on the [APIs.io](https://apis.io/) network: Threads API. Tagged areas include Company, Sales, Revenue Intelligence, Go-To-Market, and Artificial Intelligence.


  Endgame''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, support, engineering blog, and 25 more developer resources.'
random_paper: 70
rate_limits:
- limit_count: 1
  name: End Game Rate Limits
  slug: end-game-rate-limits
score:
  band: strong
  composite: 56.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 62.0
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/end-game/refs/heads/main/screenshots/end-game-2026-07-25T213310.png
security:
- kind: authentication
  name: End Game Authentication
  slug: end-game-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: End Game Domain Security
  slug: end-game-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: End Game Vulnerability Disclosure
  slug: end-game-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: End Game Trust Center
  slug: end-game-trust-center
  summary_line: SOC 2, ISO 27001
slug: end-game
tags:
- Company
- Sales
- Revenue Intelligence
- Go-To-Market
- Artificial Intelligence
- Agents
- MCP
- Knowledge Graph
- CRM
- Conversation Intelligence
website: https://www.endgame.io
---
