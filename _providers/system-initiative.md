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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'Workspace-scoped REST API (the "luminork" server) for automating System Initiative: create and apply change sets, model/discover/import components, run functions, and manage actions and secrets. Beare'
  name: System Initiative Public API
  slug: system-initiative-public-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.systeminit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.systeminit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.systeminit.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.systeminit.com/reference/public-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.systeminit.com/how-tos/use-public-api
- group: company
  title: ''
  type: Blog
  url: https://www.systeminit.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.systeminit.com/changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/system-initiative-changelog.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/systeminit
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/systeminit/si
- group: auth
  title: ''
  type: Authentication
  url: authentication/system-initiative-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/system-initiative-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/system-initiative-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/system-initiative-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/system-initiative-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/system-initiative-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/system-initiative-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/system-initiative-llms.txt
created: '2026-07-17'
description: System Initiative is an AI-native infrastructure automation platform. It builds an interactive digital twin of your cloud infrastructure — modeling every resource as a "component" inside reviewable "change sets" — so that engineers and AI agents can discover, simulate, and safely apply changes to production. It works alongside Terraform, Pulumi, and GitOps and can be adopted incrementally. System Initiative exposes a workspace-scoped Public API (the "luminork" server) with bearer-token auth, first-party Python and JavaScript/TypeScript SDKs, and a first-party Model Context Protocol (MCP) server so agents can model and automate infrastructure programmatically. Backed by Amplify Partners and Battery Ventures.
image: https://github.com/systeminit.png
layout: provider
mcp_servers:
- description: ''
  name: system-initiative-mcp.yml
  slug: system-initiative-mcpyml
modified: '2026-07-21'
name: System Initiative
nav: Providers
network: true
overview: 'System Initiative publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Developer Tools, Infrastructure Automation, DevOps, and Infrastructure as Code.


  System Initiative''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, authentication, and 13 more developer resources.'
random_paper: 105
score:
  band: thin
  composite: 31.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 32.3
    developer_ergonomics: 64.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.3
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: System Initiative Authentication
  slug: system-initiative-authentication
  summary_line: http · 1 scheme
slug: system-initiative
tags:
- Company
- Developer Tools
- Infrastructure Automation
- DevOps
- Infrastructure as Code
- AI Agents
- Cloud
- MCP
website: https://www.systeminit.com/
---
