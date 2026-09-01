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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The v1 REST API behind Cloutdesk''s Agent Platform — the programmatic surface agencies, brands, and talent representatives use to run influencer marketing through AI agents. Cursor-paginated, URI-path '
  name: Cloutdesk Agent Platform API
  slug: agent-platform
artifact_total: 7
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/cloutdesk/agents/blob/main/LICENSE
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloutjam-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://cloutdesk.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cloutdesk.com/agent-platform
- group: docs
  title: ''
  type: Documentation
  url: https://www.cloutdesk.com/agent-platform
- group: start
  title: ''
  type: Login
  url: https://dashboard.cloutdesk.com
- group: operate
  title: ''
  type: Support
  url: mailto:hello@cloutdesk.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cloutdesk.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/65621163/cookie-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloutjam-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloutjam-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloutjam-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cloutjam-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cloutjam-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloutjam-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloutjam-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/cloutjam-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloutjam-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloutjam-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cloutjam-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloutjam-rate-limits.yml
- group: build
  title: ''
  type: CLI
  url: cli/cloutjam-cli.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cloutdesk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/cloutdesk/agents
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/cloutdesk/agents#quick-start
created: '2026-07-17'
description: CloutDesk (formerly CloutJam) is a 500 Global-backed, New York-based platform for modern influencer marketing and creator management, building open infrastructure that lets agencies, brands, and talent representatives run creator partnerships end-to-end - outreach, relationship management, content approval, contract negotiation, invoicing, reporting, and payments. Its agent-first Agent Platform (closed beta) exposes every workflow to AI agents through an MCP server with six published tools, a cursor-paginated v1 REST API with RFC 7807 errors and idempotent writes, and a CLI. CloutDesk also publishes 16 MIT-licensed Agent Skills and four agent templates for Claude Code, OpenAI Codex, and Microsoft Agent Framework in its own public GitHub org.
image: https://cdn.prod.website-files.com/684989b6fb9b11bb4d485104/68cd29a469d19b89648e1d17_open-graph.avif
layout: provider
mcp_servers:
- description: ''
  name: CloutJam MCP Server
  slug: cloutjam-mcp-server
modified: '2026-08-13'
name: CloutJam
nav: Providers
network: true
overview: 'CloutJam publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Creator Management, Creator Economy, and Marketing.


  CloutJam''s developer surface includes documentation, support, authentication, CLI, getting-started guide, and 21 more developer resources.'
plans:
- name: Cloutjam Plans Pricing
  plan_count: 0
  slug: cloutjam-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Cloutjam Rate Limits
  slug: cloutjam-rate-limits
scopes:
- name: Cloutjam Scopes
  scope_count: 4
  slug: cloutjam-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 25.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 25.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloutjam/refs/heads/main/screenshots/cloutjam-2026-07-25T205717.png
security:
- kind: authentication
  name: Cloutjam Authentication
  slug: cloutjam-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Cloutjam Domain Security
  slug: cloutjam-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cloutjam
tags:
- Company
- Influencer Marketing
- Creator Management
- Creator Economy
- Marketing
- Agentic AI
- Agents
- MCP
- Agent Skills
- Talent Management
- Influencer Marketing Platform
website: https://cloutdesk.com
---
