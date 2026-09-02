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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: End Game Agentic Access
  operation_count: 5
  slug: end-game-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 2
apis:
- description: The public Threads API from Endgame — 5 operations (create, get, list, rename, delete) rooted at /api/v1 on https://app.endgame.io, authenticated with a Bearer eak_ API key or a WorkOS M2M access toke
  name: Endgame Threads API
  slug: end-game-threads-api
- description: The Internal API from Endgame — 3 operation(s) for internal.
  name: Endgame Internal API
  slug: end-game-internal-api
- description: The Protected Static API from Endgame — 2 operation(s) for protected static.
  name: Endgame Protected Static API
  slug: end-game-protected-static-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Endgame Public Threads API
  slug: open-end-game-threads-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/Endgame-Labs/endgame-cli/blob/main/LICENSE
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
  url: https://status.endgame.io
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
- group: agent
  title: ''
  type: AgentSkill
  url: skills/end-game-published-skill.md
- group: other
  title: ''
  type: AgentCard
  url: a2a/end-game-a2a.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/end-game-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/end-game-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/end-game-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/end-game-cli.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/end-game-tool-crosswalk.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/end-game-plans-pricing.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Endgame-Labs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Endgame-Labs/endgame-cli
- group: auth
  title: ''
  type: TrustCenter
  url: https://app.drata.com/trust/9cbf820f-0c38-11ee-865f-029d78a187d9
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/end-game-website-llms.txt
created: '2026-07-17'
description: Endgame (Endgame Labs, Inc.) is a context graph platform for go-to-market teams and AI agents that turns sales calls, CRM records, emails, Slack conversations, meeting transcripts, and uploaded documents into structured, queryable revenue intelligence. Sales and RevOps users ask questions across their book of business in natural language, and connected AI assistants reach the same knowledge through the Endgame MCP Server. The public REST API (rooted at /api/v1) lets developers create and manage Endgame threads programmatically over HTTPS with Bearer-token authentication, while a broad connector surface ingests context from Salesforce, Gong, Chorus, Clari Copilot, Zoom, Notion, Confluence, Highspot, Seismic, Snowflake, Slack, Microsoft Teams/SharePoint/Outlook, and Google Drive. Endgame was surfaced through the API Evangelist VC-portfolio pipeline and has been enriched from its published developer documentation, OpenAPI, MCP server, and trust/security programs.
image: https://www.endgame.io/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: Endgame MCP Server
  slug: endgame-mcp-server
modified: '2026-08-13'
name: Endgame
nav: Providers
network: true
overview: 'Endgame publishes 3 APIs on the [APIs.io](https://apis.io/) network: Threads API, Internal API, and Protected Static API. Tagged areas include Company, Sales, Revenue Intelligence, Go-To-Market, and Artificial Intelligence.


  Endgame''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, support, engineering blog, and 38 more developer resources.'
plans:
- name: End Game Plans Pricing
  plan_count: 0
  slug: end-game-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 1
  name: End Game Rate Limits
  slug: end-game-rate-limits
scopes:
- name: End Game Scopes
  scope_count: 4
  slug: end-game-scopes
  summary_line: 4 scopes
score:
  band: strong
  composite: 55.5
  coverage:
    artifact_dirs: 24
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 51.7
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 55.5
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/end-game/refs/heads/main/screenshots/end-game-2026-07-25T213310.png
security:
- kind: authentication
  name: End Game Authentication
  slug: end-game-authentication
  summary_line: http/oauth2 · 2 schemes
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
