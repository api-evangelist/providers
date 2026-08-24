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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.3
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'Model Context Protocol server for tday, and the agent-facing entry point to the platform. It ships in two deployments that front the same nine tools: a hosted remote endpoint at https://tday.com/api/m'
  name: tday MCP Server
  slug: tday-mcp-server
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tdaycom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tday.com
- group: docs
  title: ''
  type: Documentation
  url: https://tday.com/mcp
- group: start
  title: ''
  type: Login
  url: https://tday.com/login
- group: start
  title: ''
  type: SignUp
  url: https://tday.com/signup
- group: operate
  title: ''
  type: Support
  url: https://tday.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://tday.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://tday.com/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tday.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tday.com/terms
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tdaycom-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tdaycom-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tdaycom-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tdaycom-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tdaycom-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/tdaycom-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tdaycom-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tdaycom-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tdaycom-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tdaycom-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tdaycom-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tdaycom-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tdaycom-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tdaycom-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tdaycom-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tdaycom-llms.txt
created: '2026-07-17'
description: 'tday (tday.com) is a Y Combinator-backed (Spring 2026) AI platform, operated by Altacomm Technologies Pty. Ltd. of Adelaide, South Australia, that turns what a software team ships into on-brand creative. It connects to a company''s GitHub repository or drives a live site through the browser like a user, and on every release produces a launch package — an end-to-end demo video recorded from real product flows, a promotional feature showcase, and on-brand social graphics — then publishes that creative to social channels and measures how it performs. A second surface generates brand-aware still designs from a text prompt against a stored brand, where a brand is created from a website URL and its colors, fonts and logos are extracted automatically. tday operates with no SDK embedded in the customer''s product, using isolated per-run workspaces and database branches, scoped repository access, secure credential storage, and secret redaction. Its developer surface is agent-shaped
  rather than REST-shaped: tday publishes no OpenAPI, and instead ships a hosted Model Context Protocol server at https://tday.com/api/mcp secured with OAuth 2.1 (PKCE, dynamic client registration, RFC 8414 / RFC 9728 discovery), a local stdio MCP server distributed on npm as @designtday/mcp, and five of its own packaged agent skills.'
image: https://tday.com/logo.svg
layout: provider
mcp_servers:
- description: 'Official hosted Model Context Protocol server for tday, the agent-facing surface of the tday design/launch-content platform. tday.com/mcp documents two ways in: a local stdio server installed from npm'
  name: Tdaycom MCP Server
  slug: tdaycom-mcp-server
modified: '2026-08-13'
name: Tdaycom
nav: Providers
network: true
overview: 'Tdaycom publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Artificial Intelligence, Content Generation, and Design.


  Tdaycom''s developer surface includes documentation, signup flow, support, pricing, changelog, authentication, CLI, and 20 more developer resources.'
plans:
- name: Tdaycom Plans Pricing
  plan_count: 3
  slug: tdaycom-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Tdaycom Rate Limits
  slug: tdaycom-rate-limits
scopes:
- name: Tdaycom Scopes
  scope_count: 1
  slug: tdaycom-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 36.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Tdaycom Authentication
  slug: tdaycom-authentication
  summary_line: oauth2/http-bearer · 2 schemes
- kind: domain-security
  name: Tdaycom Domain Security
  slug: tdaycom-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tdaycom
tags:
- Company
- Marketing
- Artificial Intelligence
- Content Generation
- Design
- Video
- Social-Media
- Developer Tools
- MCP
- Agents
- Y Combinator
website: https://tday.com
---
