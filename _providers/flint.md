---
access_model:
  confidence: high
  label: Free tier plus 14-day paid trial
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - https://www.flint.com/pricing
  - plans/flint-plans-pricing.yml
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Flint Agentic Access
  operation_count: 2
  slug: flint-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: Start and monitor background AI agent tasks on a Flint site.
  name: Flint Agent Tasks API
  slug: flint-agent-tasks-api
- description: Flint's official hosted remote MCP server. Four tools — list_sites, run_background_agent, check_background_agent_status and publish_site — let an MCP client discover Flint sites, run background design
  name: Flint MCP Server
  slug: flint-mcp-server
artifact_total: 14
asyncapis:
- description: ''
  name: Flint Webhooks
  slug: flint-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Flint Agent Tasks API
  slug: open-flint-agent-tasks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/flint-agent-tasks-overlay.yaml
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/flint-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/flint-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flint-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/flint-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.flint.com/status
- group: operate
  title: ''
  type: SLA
  url: https://www.flint.com/docs/slas
- group: auth
  title: ''
  type: Compliance
  url: https://www.flint.com/docs/data-residency-gdpr
- group: operate
  title: ''
  type: Support
  url: https://www.flint.com/contact-support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tryflint
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tryflint/claude-code-plugin
- group: docs
  title: ''
  type: Guides
  url: https://www.flint.com/docs/guides
- group: operate
  title: ''
  type: FAQ
  url: https://www.flint.com/docs/faq
- group: company
  title: ''
  type: Careers
  url: https://www.flint.com/careers
created: '2026-07-17'
description: Flint (Flint Technologies Inc., tryflint.com / flint.com) is an AI web platform for marketing teams that programmatically generates on-brand, high-converting landing pages and runs autonomous agents — including a Google Ad agent — to keep ad accounts optimized. Its products are Pages (AI-generated landing pages), Agents (autonomous campaign upkeep), and an Agent Tasks REST API plus a hosted MCP server that let developers create, modify, and publish pages from Claude, Clay, Relay.app, or any HTTP client. Backed by Accel. This profile was enriched from Flint's public developer documentation, MCP OAuth discovery metadata, and security surface.
image: https://www.flint.com/images/favicon-144x144.png
layout: provider
mcp_servers:
- description: ''
  name: flint-mcp.yml
  slug: flint-mcpyml
modified: '2026-08-13'
name: Flint
nav: Providers
network: true
overview: 'Flint publishes 1 API on the [APIs.io](https://apis.io/) network: Agent Tasks API. Tagged areas include Company, AI, Marketing, Landing Pages, and Agents.


  The Flint catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Flint''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, authentication, and 37 more developer resources.'
plans:
- name: Flint Plans Pricing
  plan_count: 3
  slug: flint-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 0
  name: Flint Rate Limits
  slug: flint-rate-limits
scopes:
- name: Flint Scopes
  scope_count: 7
  slug: flint-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: exemplar
  composite: 66.1
  delta: 13.6
  facets:
    commercial_clarity: 92.1
    contract_quality: 71.6
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 55.3
  previous_composite: 52.5
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
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
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
- Google Ads
- Website Builder
website: https://www.flint.com/
---
