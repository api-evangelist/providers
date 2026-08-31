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
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Official hosted Model Context Protocol (MCP) server that acts as the task layer for AI agents. Exposes tools to add, get, update, complete, delete, move, assign, label, and search tasks and lists, plu
  name: Superlist MCP Server
  slug: superlist-mcp-server
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superlist-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://superlist.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.superlist.com/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://help.superlist.com/en/articles/658028-superlist-mcp-server
- group: operate
  title: ''
  type: Support
  url: https://help.superlist.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.superlist.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.superlist.com/updates
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.superlist.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.superlist.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.superlist.com/
- group: start
  title: ''
  type: Login
  url: https://app.superlist.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.superlist.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.superlist.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/superlistapp
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superlist-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/superlist-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/superlist-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/superlist-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superlist-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superlist-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/superlist-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/superlist-problem-types.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/superlist-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Superlist is an AI-powered task and list management application from the team behind Wunderlist, combining to-dos, notes, and lightweight project planning in a single collaborative workspace across Mac, Web, iOS, and Android. Its primary programmatic surface is an official hosted Model Context Protocol (MCP) server that lets Claude, ChatGPT, Cursor, and any MCP-compatible agent read and manage tasks, lists, labels, and views over natural language. The MCP endpoint is secured with a standards-based OAuth 2.0 authorization server (PKCE, dynamic client registration, RFC 8414 / RFC 9728 discovery). Superlist does not publish a traditional public REST API or OpenAPI; the MCP server is the agent-native integration layer.
image: https://framerusercontent.com/assets/xlouachsGTVuJaHXsYmxxI66e2s.png
layout: provider
mcp_servers:
- description: ''
  name: Superlist MCP Server
  slug: superlist-mcp-server
modified: '2026-07-21'
name: Superlist
nav: Providers
network: true
overview: 'Superlist publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Project Management Sector, Task Management, Productivity, and To-Do Lists.


  Superlist''s developer surface includes documentation, support, engineering blog, changelog, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 29.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Superlist Authentication
  slug: superlist-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Superlist Domain Security
  slug: superlist-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: superlist
tags:
- Company
- Project Management Sector
- Task Management
- Productivity
- To-Do Lists
- Collaboration
- MCP
- Agents
- AI Assistant
website: https://superlist.com
---
