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
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 15
  name: Ninox Agentic Access
  operation_count: 23
  slug: ninox-agentic-access
  summary_line: 23 operations · 15 acting · 15 human-in-the-loop
api_count: 5
apis:
- description: The Fields API from Ninox — 3 operation(s) for fields.
  name: Ninox Fields API
  slug: ninox-fields-api
- description: The Modules API from Ninox — 2 operation(s) for modules.
  name: Ninox Modules API
  slug: ninox-modules-api
- description: The Records API from Ninox — 2 operation(s) for records.
  name: Ninox Records API
  slug: ninox-records-api
- description: The Tables API from Ninox — 2 operation(s) for tables.
  name: Ninox Tables API
  slug: ninox-tables-api
- description: The Workspace API from Ninox — 1 operation(s) for workspace.
  name: Ninox Workspace API
  slug: ninox-workspace-api
arazzos:
- description: Create a table in a module, add fields in batch, insert records, then read them back.
  name: Ninox — Create a table and add records
  slug: ninox-create-table-and-add-records
- description: Create a module in a workspace, add a table, and define its fields.
  name: Ninox — Provision a module with tables and fields
  slug: ninox-provision-module
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ninox Public Fields API
  slug: open-ninox-fields-api
- collection_type: open
  name: Ninox Public Fields Modules API
  slug: open-ninox-modules-api
- collection_type: open
  name: Ninox Public Fields Records API
  slug: open-ninox-records-api
- collection_type: open
  name: Ninox Public Fields Tables API
  slug: open-ninox-tables-api
- collection_type: open
  name: Ninox Public Fields Workspace API
  slug: open-ninox-workspace-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/ninox-public-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ninox.com/ninox-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ninox.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ninox.com/ninox-api/api-reference/api-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ninox.com/ninox-api/api-reference/introduction-to-ninox-public-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/ninox-authentication.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://go.ninox.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://go.ninox.com/user/signup
- group: start
  title: ''
  type: Login
  url: https://go.ninox.com/user/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://go.ninox.com/en/legal-notices/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://go.ninox.com/en/legal-notices/privacy
- group: operate
  title: ''
  type: Support
  url: https://go.ninox.com/en/resources/support
- group: company
  title: ''
  type: Blog
  url: https://go.ninox.com/en/resources/blog
- group: operate
  title: ''
  type: Community
  url: https://forum.ninox.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://forum.ninox.com/category/service-status
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ninox-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ninox-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ninox-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ninox-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/ninox-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ninox-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ninox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ninox-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ninox-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ninox-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ninox-create-table-and-add-records.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ninox-provision-module.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ninox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ninox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ninox.com/
created: '2026-07-17'
description: Ninox is an AI-native low-code database and application platform that lets business teams build custom apps, databases, and workflows without traditional coding. Teams model data as modules, tables, fields, and records, automate processes with the Ninox scripting language, generate documents, and collaborate across organizations and workspaces. The Ninox Public REST API provides programmatic access to workspace resources — creating and managing modules, tables, fields, and records, plus CSV import — authenticated with per-workspace API keys sent as bearer tokens. Ninox is delivered as public cloud, private cloud, and on-premises deployments, and is backed by Techstars.
image: https://ninox.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: ninox-mcp.yml
  slug: ninox-mcpyml
modified: '2026-07-20'
name: Ninox
nav: Providers
network: true
overview: 'Ninox publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Fields API, Modules API, Records API, and 2 more. Tagged areas include Company, Low-Code, Database, No-Code, and Application Development.


  Ninox''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, support, and 24 more developer resources.'
random_paper: 109
score:
  band: developing
  composite: 40.8
  delta: -7.7
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 16.7
    contract_quality: 52.0
    developer_ergonomics: 61.3
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ninox/refs/heads/main/screenshots/ninox-2026-08-07T185329.png
security:
- kind: authentication
  name: Ninox Authentication
  slug: ninox-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ninox Domain Security
  slug: ninox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ninox
tags:
- Company
- Low-Code
- Database
- No-Code
- Application Development
- Workflow Automation
- Business Apps
- Productivity
website: https://ninox.com/
---
