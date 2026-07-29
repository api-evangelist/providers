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
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 169
  human_in_the_loop: 1
  name: Cube Planning Agentic Access
  operation_count: 296
  slug: cube-planning-agentic-access
  summary_line: 296 operations · 169 acting · 1 human-in-the-loop
api_count: 42
apis:
- description: The Agents API from Cube Planning — 7 operation(s) for agents.
  name: Cube Planning Agents API
  slug: cube-planning-agents-api
- description: Attributes are additional metadata that can be applied to values in the cube. They show up as additional columns in drilldowns, for instance.
  name: Cube Planning Attributes API
  slug: cube-planning-attributes-api
- description: The audit trail tracks the changes of values within the cube and helps with governance.
  name: Cube Planning Audit Trail API
  slug: cube-planning-audit-trail-api
- description: The Auth API from Cube Planning — 3 operation(s) for auth.
  name: Cube Planning Auth API
  slug: cube-planning-auth-api
- description: The Cube API supports user authentication via OAuth2 using the OAuth2 Authorization Code Flow. To authenticate via OAuth2, an application must first be registered.
  name: Cube Planning Authentication API
  slug: cube-planning-authentication-api
- description: The Canvases API from Cube Planning — 10 operation(s) for canvases.
  name: Cube Planning Canvases API
  slug: cube-planning-canvases-api
- description: The ChatMessages API from Cube Planning — 2 operation(s) for chatmessages.
  name: Cube Planning ChatMessages API
  slug: cube-planning-chatmessages-api
- description: The ChatSessions API from Cube Planning — 2 operation(s) for chatsessions.
  name: Cube Planning ChatSessions API
  slug: cube-planning-chatsessions-api
- description: The ChatSettings API from Cube Planning — 1 operation(s) for chatsettings.
  name: Cube Planning ChatSettings API
  slug: cube-planning-chatsettings-api
- description: The Comments API from Cube Planning — 2 operation(s) for comments.
  name: Cube Planning Comments API
  slug: cube-planning-comments-api
- description: A user in Cube belongs to one or more companies. Companies are how various teams of employees manage their data (dimensions, etc) and permissions (users, etc).
  name: Cube Planning Companies API
  slug: cube-planning-companies-api
- description: The Company Groups API from Cube Planning — 4 operation(s) for company groups.
  name: Cube Planning Company Groups API
  slug: cube-planning-company-groups-api
- description: The compliance API from Cube Planning — 1 operation(s) for compliance.
  name: Cube Planning compliance API
  slug: cube-planning-compliance-api
- description: Connections to external source systems allow Cube to automatically import source dimensions and transaction data.
  name: Cube Planning Connections API
  slug: cube-planning-connections-api
- description: The ContentType API from Cube Planning — 2 operation(s) for contenttype.
  name: Cube Planning ContentType API
  slug: cube-planning-contenttype-api
- description: The cube API from Cube Planning — 2 operation(s) for cube.
  name: Cube Planning cube API
  slug: cube-planning-cube-api
- description: The data stored in a cube for a company, organized by their dimensions.
  name: Cube Planning Cube Data API
  slug: cube-planning-cube-data-api
- description: The Cube Value Range API from Cube Planning — 4 operation(s) for cube value range.
  name: Cube Planning Cube Value Range API
  slug: cube-planning-cube-value-range-api
- description: The Currencies API from Cube Planning — 13 operation(s) for currencies.
  name: Cube Planning Currencies API
  slug: cube-planning-currencies-api
- description: Access the underlying Dashboards of Cube
  name: Cube Planning Dashboard API
  slug: cube-planning-dashboard-api
- description: Cube often uses uploads as a way to load in transaction data for a given data table or connection. You can use the API to create new uploads, send files, and track the status of an upload.
  name: Cube Planning Data Table Uploads API
  slug: cube-planning-data-table-uploads-api
- description: Data Tables are a generic way to organize the source dimensions, mappings, uploads, and imports from an outside source into Cube (e.g. ERP connections, imported flat files, spreadsheet updates, employ
  name: Cube Planning Data Tables API
  slug: cube-planning-data-tables-api
- description: 'Dimensions store the organizational hierarchy for a company and outline how their data is structured. All companies have top level dimensions called Account, Scenario, Department, and Time. They also '
  name: Cube Planning Dimensions API
  slug: cube-planning-dimensions-api
- description: The Drilldown API from Cube Planning — 1 operation(s) for drilldown.
  name: Cube Planning Drilldown API
  slug: cube-planning-drilldown-api
- description: The ERP API from Cube Planning — 4 operation(s) for erp.
  name: Cube Planning ERP API
  slug: cube-planning-erp-api
- description: This endpoint can be used to track generic events completed by users.
  name: Cube Planning Events API
  slug: cube-planning-events-api
- description: 'Cube uses formulas to calculate values for a dimension, based on other dimensions. Examples: - Gross Margin = "Revenue" - "Cost of Goods Sold" - Net Income = "Gross Margin" - "Expense" You can use for'
  name: Cube Planning Formulas API
  slug: cube-planning-formulas-api
- description: The Integrations API from Cube Planning — 7 operation(s) for integrations.
  name: Cube Planning Integrations API
  slug: cube-planning-integrations-api
- description: The Invitations API from Cube Planning — 3 operation(s) for invitations.
  name: Cube Planning Invitations API
  slug: cube-planning-invitations-api
- description: The Library API from Cube Planning — 12 operation(s) for library.
  name: Cube Planning Library API
  slug: cube-planning-library-api
- description: The Notifications API from Cube Planning — 2 operation(s) for notifications.
  name: Cube Planning Notifications API
  slug: cube-planning-notifications-api
- description: The Permissions API from Cube Planning — 2 operation(s) for permissions.
  name: Cube Planning Permissions API
  slug: cube-planning-permissions-api
- description: The permissionsets API from Cube Planning — 2 operation(s) for permissionsets.
  name: Cube Planning permissionsets API
  slug: cube-planning-permissionsets-api
- description: The PlanModeSessions API from Cube Planning — 1 operation(s) for planmodesessions.
  name: Cube Planning PlanModeSessions API
  slug: cube-planning-planmodesessions-api
- description: The Planning Table API from Cube Planning — 4 operation(s) for planning table.
  name: Cube Planning Planning Table API
  slug: cube-planning-planning-table-api
- description: The Scenarios API from Cube Planning — 1 operation(s) for scenarios.
  name: Cube Planning Scenarios API
  slug: cube-planning-scenarios-api
- description: Alternative hierarchies & grouping of dimensions in Cube
  name: Cube Planning Tags API
  slug: cube-planning-tags-api
- description: The Taskflow API from Cube Planning — 11 operation(s) for taskflow.
  name: Cube Planning Taskflow API
  slug: cube-planning-taskflow-api
- description: The Team API from Cube Planning — 1 operation(s) for team.
  name: Cube Planning Team API
  slug: cube-planning-team-api
- description: User endpoints allow for various functionality tied to users.
  name: Cube Planning User API
  slug: cube-planning-user-api
- description: The UserCompanies API from Cube Planning — 3 operation(s) for usercompanies.
  name: Cube Planning UserCompanies API
  slug: cube-planning-usercompanies-api
- description: The Workflow API from Cube Planning — 5 operation(s) for workflow.
  name: Cube Planning Workflow API
  slug: cube-planning-workflow-api
artifact_total: 48
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cube-planning-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cube-planning-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cube-planning-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cube-planning-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cube-planning-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cube-planning-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cube-planning-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cube-planning-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cube-planning-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cubesoftware.com
- group: design
  title: ''
  type: Conformance
  url: conformance/cube-planning-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.cubesoftware.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/cube-planning-trust-center.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cube-planning-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cube-planning-llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://www.cubesoftware.com/developer-center
- group: docs
  title: ''
  type: APIReference
  url: https://api.cubesoftware.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://help.cubesoftware.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.cubesoftware.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cubesoftware.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://portal.cubesoftware.com/account/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cubesoftware.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cubesoftware.com/privacy-policy
created: '2026-07-17'
description: Cube (Cube Software) is a financial planning & analysis (FP&A) platform that positions itself as an "agentic finance layer" — giving finance teams clean, decision-ready data everywhere FP&A happens by harmonizing data across their existing tool stack (ERPs, accounting, HRIS, CRM, data warehouses, and spreadsheets like Excel and Google Sheets) and automating planning, budgeting, and forecasting workflows. Cube exposes a public REST API at api.cubesoftware.com with 296 operations across 16 tags — dimensions, formulas, data tables, cube data exports, dashboards, connections, tags, attributes, and company/user administration — secured with OAuth 2.0 authorization-code + PKCE and multi-tenant via an X-Company-ID header. Cube is a Battery Ventures portfolio company. Enriched by the API Evangelist pipeline from Cube's public OpenAPI and developer surface.
image: https://www.cubesoftware.com/hubfs/cube-favicon-2.png
layout: provider
mcp_servers:
- description: ''
  name: cube-planning-mcp.yml
  slug: cube-planning-mcpyml
modified: '2026-07-18'
name: Cube Planning
nav: Providers
network: true
overview: 'Cube Planning publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Attributes API, Audit Trail API, and 39 more. Tagged areas include Company, FP&A, Financial Planning, Finance, and Budgeting.


  Cube Planning''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 6
scopes:
- name: Cube Planning Scopes
  scope_count: 3
  slug: cube-planning-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 46.3
  delta: -0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 52.5
    developer_ergonomics: 36.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 15.8
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cube-planning/refs/heads/main/screenshots/cube-planning-2026-07-25T210914.png
security:
- kind: authentication
  name: Cube Planning Authentication
  slug: cube-planning-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cube Planning Domain Security
  slug: cube-planning-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Cube Planning Trust Center
  slug: cube-planning-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: cube-planning
tags:
- Company
- FP&A
- Financial Planning
- Finance
- Budgeting
- Forecasting
- Analytics
- Planning
---
