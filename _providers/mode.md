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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Mode Agentic Access
  operation_count: 94
  slug: mode-agentic-access
  summary_line: 94 operations · 45 acting
api_count: 11
apis:
- description: The Account API from Mode — 1 operation(s) for account.
  name: Mode Account API
  slug: mode-account-api
- description: The Audit Logs API from Mode — 1 operation(s) for audit logs.
  name: Mode Audit Logs API
  slug: mode-audit-logs-api
- description: The Data Sources API from Mode — 6 operation(s) for data sources.
  name: Mode Data Sources API
  slug: mode-data-sources-api
- description: The Datasets API from Mode — 8 operation(s) for datasets.
  name: Mode Datasets API
  slug: mode-datasets-api
- description: The Definitions API from Mode — 2 operation(s) for definitions.
  name: Mode Definitions API
  slug: mode-definitions-api
- description: The Groups API from Mode — 4 operation(s) for groups.
  name: Mode Groups API
  slug: mode-groups-api
- description: The Invites API from Mode — 1 operation(s) for invites.
  name: Mode Invites API
  slug: mode-invites-api
- description: The Memberships API from Mode — 2 operation(s) for memberships.
  name: Mode Memberships API
  slug: mode-memberships-api
- description: The Reports API from Mode — 27 operation(s) for reports.
  name: Mode Reports API
  slug: mode-reports-api
- description: The Spaces API from Mode — 6 operation(s) for spaces.
  name: Mode Spaces API
  slug: mode-spaces-api
- description: The Verify API from Mode — 1 operation(s) for verify.
  name: Mode Verify API
  slug: mode-verify-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://mode.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mode.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://mode.com/developer/api-reference/introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://mode.com/developer/api-reference/introduction/
- group: start
  title: ''
  type: GettingStarted
  url: https://mode.com/developer/api-reference/introduction/
- group: operate
  title: ''
  type: Support
  url: https://mode.com/help/
- group: company
  title: ''
  type: Blog
  url: https://mode.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mode
- group: operate
  title: ''
  type: StatusPage
  url: https://status.modeanalytics.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://mode.com/compare-plans/
- group: start
  title: ''
  type: Login
  url: https://app.mode.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mode.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mode.com/legal/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/mode-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mode-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mode-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mode-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mode-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mode-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mode-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mode-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mode-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mode-domain-security.yml
created: '2026-07-17'
description: Mode is a collaborative business intelligence and analytics platform that unites data and business teams around a single analytical workflow. Built by analysts for analysts, Mode combines ad hoc SQL exploration, Python and R notebooks, interactive dashboards, self-serve reporting, and custom data applications on top of connected data warehouses. Mode was acquired by ThoughtSpot in 2023 and positions itself as the intelligence layer for the modern data stack. Mode exposes a REST API (documented at its Developer Hub) for programmatic management of workspaces, users, collections, data sources, reports, queries, charts, datasets, definitions, exports, report schedules, and subscriptions. The API uses HTTP Basic authentication with workspace or personal API tokens and returns HAL+JSON, and is available to workspaces on a paid Mode Business plan.
image: https://avatars.githubusercontent.com/u/5306870?v=4
layout: provider
mcp_servers:
- description: ''
  name: mode-mcp.yml
  slug: mode-mcpyml
modified: '2026-07-20'
name: Mode
nav: Providers
network: true
overview: 'Mode publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Audit Logs API, Data Sources API, and 8 more. Tagged areas include Company, Enterprise, Business Intelligence, Analytics, and Data.


  Mode''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, authentication, and 17 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 40.5
  delta: -4.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 32.3
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Mode Authentication
  slug: mode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Mode Domain Security
  slug: mode-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: mode
tags:
- Company
- Enterprise
- Business Intelligence
- Analytics
- Data
- Reporting
- Dashboards
- SQL
- Data Stack
website: https://mode.com
---
