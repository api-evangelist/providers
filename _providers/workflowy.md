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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://workflowy.com/api/v1
  baseurl_source: declared
  description: Create, read, update, move, complete, and delete outline nodes.
  name: Workflowy Nodes API
  slug: workflowy-nodes-api
- baseURL: https://workflowy.com/api/v1
  baseurl_source: declared
  description: System targets and user-defined shortcuts that point at nodes.
  name: Workflowy Targets API
  slug: workflowy-targets-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workflowy Nodes API
  slug: open-workflowy-nodes-api
- collection_type: open
  name: Workflowy Nodes Targets API
  slug: open-workflowy-targets-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/workflowy-api-overlay.yaml
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
- description: Workflowy MCP is a desktop app that lets you connect your Workflowy account to external AI agents over the Model Context Protocol. Documented on Workflowy's official help site; releases are distribute
  name: Workflowy MCP
  slug: workflowy-mcp
modified: '2026-07-21'
name: Workflowy
nav: Providers
network: true
overview: 'Workflowy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Nodes API and Targets API. Tagged areas include Productivity, Notes, Outliner, Task Management, and List.


  Workflowy''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 17.5
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 35.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workflowy/refs/heads/main/screenshots/workflowy-2026-08-17T083141.png
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
- List
- Collaboration
- Knowledge-Management
- AI Assistant
website: https://workflowy.com/
---
