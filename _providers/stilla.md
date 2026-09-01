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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Programmatic access to Stilla's capabilities. The REST API and the remote MCP server are protected by OAuth 2.0 / OIDC (WorkOS AuthKit). The OpenAPI document is served at api.stilla.ai/openapi.json bu
  name: Stilla API
  slug: stilla-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://stilla.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://stilla.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://stilla.ai/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://stilla.ai/docs/support
- group: company
  title: ''
  type: Blog
  url: https://stilla.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stilla-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://stilla.ai/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.stilla.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://stilla.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.stilla.ai
- group: start
  title: ''
  type: Login
  url: https://app.stilla.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stilla.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stilla.ai/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stilla
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stillaai
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stilla-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stilla-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/stilla-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stilla-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/stilla-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stilla-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/stilla-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://stilla.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/stilla-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://trust.stilla.ai
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stilla-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stilla-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stilla-domain-security.yml
created: '2026-07-17'
description: 'Stilla is an AI teammate for the whole company — an AI agent that connects to a team''s tools (Slack, Microsoft Teams, GitHub, Linear, Notion, Google Workspace and 3,000+ more) and turns chats, meetings, and conversations into finished work: ads, code, reports, tasks, and documents. Team members mention @Stilla to delegate work, and reusable agents configured in natural language search across connected tools, take actions, transcribe meetings, and persist context in collaborative canvases. Stilla exposes a REST API and an official remote Model Context Protocol (MCP) server so external AI tools (Claude Code, Cursor, and other MCP clients) can access a workspace''s notes, decisions, and workflow outputs. Built by the team behind Shop Pay at Shopify, Stilla is SOC 2 Type II certified, GDPR compliant, and CASA Tier 2 assessed. Backed by General Catalyst.'
image: https://stilla.ai/favicon.svg
layout: provider
mcp_servers:
- description: Official remote MCP server that gives MCP-compatible clients (Claude Code, Cursor, Claude Desktop, etc.) authenticated access to a Stilla workspace — meeting notes, decisions, canvases, transcripts, a
  name: Stilla MCP Server
  slug: stilla-mcp-server
modified: '2026-07-21'
name: Stilla
nav: Providers
network: true
overview: 'Stilla publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Agentic, and Productivity.


  Stilla''s developer surface includes documentation, getting-started guide, support, engineering blog, changelog, pricing, signup flow, and 21 more developer resources.'
random_paper: 19
scopes:
- name: Stilla Scopes
  scope_count: 4
  slug: stilla-scopes
  summary_line: 4 scopes · authorizationCode/deviceCode
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 32.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Stilla Authentication
  slug: stilla-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Stilla Domain Security
  slug: stilla-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Stilla Trust Center
  slug: stilla-trust-center
  summary_line: SOC 2 Type II, GDPR, CASA Tier 2
slug: stilla
tags:
- Company
- Artificial Intelligence
- AI Agents
- Agentic
- Productivity
- Collaboration
- MCP
- Automation
- Developer Tools
- Enterprise
website: https://stilla.ai/docs
---
