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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.7
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Flint Agentic Access
  operation_count: 2
  slug: flint-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Start and monitor background AI agent tasks on a Flint site.
  name: Flint Agent Tasks API
  slug: flint-agent-tasks-api
artifact_total: 9
asyncapis:
- description: ''
  name: Flint Webhooks
  slug: flint-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flint-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/flint-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.flint.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.flint.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.flint.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.flint.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.flint.com/docs/guides/flint-mcp-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flint.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.flint.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.tryflint.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.tryflint.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flint.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flint.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flint-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flint-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flint-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flint-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flint-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flint-lifecycle.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flint-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flint-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flint-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flint-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/flint-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/flint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.flint.com/security/vdp
- group: auth
  title: ''
  type: TrustCenter
  url: security/flint-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flint-llms.txt
created: '2026-07-17'
description: Flint (Flint Technologies Inc., tryflint.com / flint.com) is an AI web platform for marketing teams that programmatically generates on-brand, high-converting landing pages and runs autonomous agents — including a Google Ad agent — to keep ad accounts optimized. Its products are Pages (AI-generated landing pages), Agents (autonomous campaign upkeep), and an Agent Tasks REST API plus a hosted MCP server that let developers create, modify, and publish pages from Claude, Clay, Relay.app, or any HTTP client. Backed by Accel. This profile was enriched from Flint's public developer documentation, MCP OAuth discovery metadata, and security surface.
image: https://www.flint.com/
layout: provider
mcp_servers:
- description: ''
  name: flint-mcp.yml
  slug: flint-mcpyml
modified: '2026-07-19'
name: Flint
nav: Providers
network: true
overview: 'Flint publishes 1 API on the [APIs.io](https://apis.io/) network: Agent Tasks API. Tagged areas include Company, AI, Marketing, Landing Pages, and Agents.


  The Flint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flint''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, authentication, and 22 more developer resources.'
random_paper: 77
scopes:
- name: Flint Scopes
  scope_count: 7
  slug: flint-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 53.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 74.4
    developer_ergonomics: 58.2
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 18.4
  previous_composite: 53.2
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
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flint/refs/heads/main/screenshots/flint-2026-07-25T214758.png
security:
- kind: authentication
  name: Flint Authentication
  slug: flint-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Flint Domain Security
  slug: flint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flint Vulnerability Disclosure
  slug: flint-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Flint Trust Center
  slug: flint-trust-center
  summary_line: SOC 2 Type II
slug: flint
tags:
- Company
- AI
- Marketing
- Landing Pages
- Agents
- MCP
- Web
- Advertising
website: https://www.flint.com/
---
