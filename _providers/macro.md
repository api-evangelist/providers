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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Official hosted (remote) Model Context Protocol server for Macro. Connects AI clients over OAuth to search, read and act across a Macro workspace — email, messages, tasks, docs, threads, entities and '
  name: Macro MCP Server
  slug: macro-mcp-server
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/macro-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.macro.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.macro.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.macro.com/AI/mcp/tools/index.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.macro.com/getting-started.md
- group: operate
  title: ''
  type: Support
  url: https://docs.macro.com/support.md
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.macro.com/account/billing.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/macro-inc
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/macro-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/macro-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/macro-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/macro-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/macro-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/macro-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/macro-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/macro-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/macro-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/macro-trust-center.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Macro is an all-in-one, keyboard-first work operating system that unifies email, team messages, documents, tasks, calls, agents, GitHub pull requests and CRM into a single fast database, linked together by @mentions and a shared AI memory. Backed by a16z and built in the open (AGPLv3, github.com/macro-inc/macro), Macro runs on AWS, is SOC 2 Type II audited, and exposes an official hosted Model Context Protocol (MCP) server so AI clients can search, read and act across a connected workspace.
image: https://avatars.githubusercontent.com/u/65687018?v=4
layout: provider
mcp_servers:
- description: 'Official hosted (remote) MCP server for Macro, the unified interface for email, messages, tasks, calls, agents, pull requests, docs and CRM linked together with shared AI memory. Lets AI clients read '
  name: Macro MCP Server
  slug: macro-mcp-server
modified: '2026-07-20'
name: Macro
nav: Providers
network: true
overview: 'Macro publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Productivity, Email, Collaboration, and Workspace.


  Macro''s developer surface includes documentation, API reference, getting-started guide, support, pricing, changelog, authentication, and 12 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 11
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 28.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/macro/refs/heads/main/screenshots/macro-2026-07-25T225820.png
security:
- kind: authentication
  name: Macro Authentication
  slug: macro-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Macro Domain Security
  slug: macro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Macro Trust Center
  slug: macro-trust-center
  summary_line: SOC 2 Type II
slug: macro
tags:
- Company
- Productivity
- Email
- Collaboration
- Workspace
- CRM
- Task
- AI Agents
- MCP
- Open-Source
website: https://docs.macro.com
---
