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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Create, read, update, move, complete, and delete outline nodes.
  name: Workflowy Nodes API
  slug: workflowy-nodes-api
- description: System targets and user-defined shortcuts that point at nodes.
  name: Workflowy Targets API
  slug: workflowy-targets-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://workflowy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://workflowy.com/help/
- group: docs
  title: ''
  type: APIReference
  url: https://workflowy.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://workflowy.com/help/get-started/
- group: operate
  title: ''
  type: Support
  url: https://community.workflowy.com
- group: company
  title: ''
  type: Blog
  url: https://blog.workflowy.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/workflowy
- group: commercial
  title: ''
  type: Pricing
  url: https://workflowy.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://workflowy.com/signup/
- group: start
  title: ''
  type: Login
  url: https://workflowy.com/login/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://workflowy.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.workflowy.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://workflowy.com/whats-new/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/workflowy-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/workflowy-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/workflowy-cli.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/workflowy-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/workflowy-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/workflowy-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workflowy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/workflowy-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/workflowy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/workflowy-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/workflowy-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/workflowy-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workflowy-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Workflowy is a minimalist infinite outliner for organizing notes, tasks, and ideas in a single infinitely nested, zoomable bullet list, with mirrors, kanban boards, real-time collaboration, an AI writing assistant, and apps for web, iOS, Android, macOS, and Windows. For developers Workflowy ships an official REST API (nodes and targets at workflowy.com/api/v1, API-key bearer auth), an open-source CLI (wf) with an embedded MCP server, a desktop MCP app for connecting AI agents like Claude and Cursor, and a published llms.txt. A Bloomberg Beta portfolio company.
image: https://workflowy.com/media/webflow/open-graph-image.png
layout: provider
mcp_servers:
- description: ''
  name: workflowy-mcp.yml
  slug: workflowy-mcpyml
modified: '2026-07-21'
name: Workflowy
nav: Providers
network: true
overview: 'Workflowy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Nodes API and Targets API. Tagged areas include Productivity, Notes, Outliner, Task Management, and Lists.


  Workflowy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 40
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 60.9
    developer_ergonomics: 60.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 49.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Workflowy Authentication
  slug: workflowy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Workflowy Domain Security
  slug: workflowy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: workflowy
tags:
- Productivity
- Notes
- Outliner
- Task Management
- Lists
- Collaboration
- Knowledge Management
- AI Assistant
website: https://workflowy.com/
---
