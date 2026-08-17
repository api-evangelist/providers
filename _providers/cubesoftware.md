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
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 169
  human_in_the_loop: 1
  name: Cubesoftware Agentic Access
  operation_count: 296
  slug: cubesoftware-agentic-access
  summary_line: 296 operations · 169 acting · 1 human-in-the-loop
api_count: 42
apis:
- description: The Agents API from Cube — 7 operation(s) for agents.
  name: Cube Agents API
  slug: cubesoftware-agents-api
- description: Attributes are additional metadata that can be applied to values in the cube. They show up as additional columns in drilldowns, for instance.
  name: Cube Attributes API
  slug: cubesoftware-attributes-api
- description: The audit trail tracks the changes of values within the cube and helps with governance.
  name: Cube Audit Trail API
  slug: cubesoftware-audit-trail-api
- description: The Auth API from Cube — 3 operation(s) for auth.
  name: Cube Auth API
  slug: cubesoftware-auth-api
- description: The Cube API supports user authentication via OAuth2 using the OAuth2 Authorization Code Flow. To authenticate via OAuth2, an application must first be registered.
  name: Cube Authentication API
  slug: cubesoftware-authentication-api
- description: The Canvases API from Cube — 10 operation(s) for canvases.
  name: Cube Canvases API
  slug: cubesoftware-canvases-api
- description: The ChatMessages API from Cube — 2 operation(s) for chatmessages.
  name: Cube ChatMessages API
  slug: cubesoftware-chatmessages-api
- description: The ChatSessions API from Cube — 2 operation(s) for chatsessions.
  name: Cube ChatSessions API
  slug: cubesoftware-chatsessions-api
- description: The ChatSettings API from Cube — 1 operation(s) for chatsettings.
  name: Cube ChatSettings API
  slug: cubesoftware-chatsettings-api
- description: The Comments API from Cube — 2 operation(s) for comments.
  name: Cube Comments API
  slug: cubesoftware-comments-api
- description: A user in Cube belongs to one or more companies. Companies are how various teams of employees manage their data (dimensions, etc) and permissions (users, etc).
  name: Cube Companies API
  slug: cubesoftware-companies-api
- description: The Company Groups API from Cube — 4 operation(s) for company groups.
  name: Cube Company Groups API
  slug: cubesoftware-company-groups-api
- description: The compliance API from Cube — 1 operation(s) for compliance.
  name: Cube compliance API
  slug: cubesoftware-compliance-api
- description: Connections to external source systems allow Cube to automatically import source dimensions and transaction data.
  name: Cube Connections API
  slug: cubesoftware-connections-api
- description: The ContentType API from Cube — 2 operation(s) for contenttype.
  name: Cube ContentType API
  slug: cubesoftware-contenttype-api
- description: The cube API from Cube — 2 operation(s) for cube.
  name: Cube cube API
  slug: cubesoftware-cube-api
- description: The data stored in a cube for a company, organized by their dimensions.
  name: Cube Cube Data API
  slug: cubesoftware-cube-data-api
- description: The Cube Value Range API from Cube — 4 operation(s) for cube value range.
  name: Cube Cube Value Range API
  slug: cubesoftware-cube-value-range-api
- description: The Currencies API from Cube — 13 operation(s) for currencies.
  name: Cube Currencies API
  slug: cubesoftware-currencies-api
- description: Access the underlying Dashboards of Cube
  name: Cube Dashboard API
  slug: cubesoftware-dashboard-api
- description: Cube often uses uploads as a way to load in transaction data for a given data table or connection. You can use the API to create new uploads, send files, and track the status of an upload.
  name: Cube Data Table Uploads API
  slug: cubesoftware-data-table-uploads-api
- description: Data Tables are a generic way to organize the source dimensions, mappings, uploads, and imports from an outside source into Cube (e.g. ERP connections, imported flat files, spreadsheet updates, employ
  name: Cube Data Tables API
  slug: cubesoftware-data-tables-api
- description: 'Dimensions store the organizational hierarchy for a company and outline how their data is structured. All companies have top level dimensions called Account, Scenario, Department, and Time. They also '
  name: Cube Dimensions API
  slug: cubesoftware-dimensions-api
- description: The Drilldown API from Cube — 1 operation(s) for drilldown.
  name: Cube Drilldown API
  slug: cubesoftware-drilldown-api
- description: The ERP API from Cube — 4 operation(s) for erp.
  name: Cube ERP API
  slug: cubesoftware-erp-api
- description: This endpoint can be used to track generic events completed by users.
  name: Cube Events API
  slug: cubesoftware-events-api
- description: 'Cube uses formulas to calculate values for a dimension, based on other dimensions. Examples: - Gross Margin = "Revenue" - "Cost of Goods Sold" - Net Income = "Gross Margin" - "Expense" You can use for'
  name: Cube Formulas API
  slug: cubesoftware-formulas-api
- description: The Integrations API from Cube — 7 operation(s) for integrations.
  name: Cube Integrations API
  slug: cubesoftware-integrations-api
- description: The Invitations API from Cube — 3 operation(s) for invitations.
  name: Cube Invitations API
  slug: cubesoftware-invitations-api
- description: The Library API from Cube — 12 operation(s) for library.
  name: Cube Library API
  slug: cubesoftware-library-api
- description: The Notifications API from Cube — 2 operation(s) for notifications.
  name: Cube Notifications API
  slug: cubesoftware-notifications-api
- description: The Permissions API from Cube — 2 operation(s) for permissions.
  name: Cube Permissions API
  slug: cubesoftware-permissions-api
- description: The permissionsets API from Cube — 2 operation(s) for permissionsets.
  name: Cube permissionsets API
  slug: cubesoftware-permissionsets-api
- description: The PlanModeSessions API from Cube — 1 operation(s) for planmodesessions.
  name: Cube PlanModeSessions API
  slug: cubesoftware-planmodesessions-api
- description: The Planning Table API from Cube — 4 operation(s) for planning table.
  name: Cube Planning Table API
  slug: cubesoftware-planning-table-api
- description: The Scenarios API from Cube — 1 operation(s) for scenarios.
  name: Cube Scenarios API
  slug: cubesoftware-scenarios-api
- description: Alternative hierarchies & grouping of dimensions in Cube
  name: Cube Tags API
  slug: cubesoftware-tags-api
- description: The Taskflow API from Cube — 11 operation(s) for taskflow.
  name: Cube Taskflow API
  slug: cubesoftware-taskflow-api
- description: The Team API from Cube — 1 operation(s) for team.
  name: Cube Team API
  slug: cubesoftware-team-api
- description: User endpoints allow for various functionality tied to users.
  name: Cube User API
  slug: cubesoftware-user-api
- description: The UserCompanies API from Cube — 3 operation(s) for usercompanies.
  name: Cube UserCompanies API
  slug: cubesoftware-usercompanies-api
- description: The Workflow API from Cube — 5 operation(s) for workflow.
  name: Cube Workflow API
  slug: cubesoftware-workflow-api
artifact_total: 91
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cube Agents API
  slug: open-cubesoftware-agents-api
- collection_type: open
  name: Cube Agents Attributes API
  slug: open-cubesoftware-attributes-api
- collection_type: open
  name: Cube Agents Audit Trail API
  slug: open-cubesoftware-audit-trail-api
- collection_type: open
  name: Cube Agents Auth API
  slug: open-cubesoftware-auth-api
- collection_type: open
  name: Cube Agents Authentication API
  slug: open-cubesoftware-authentication-api
- collection_type: open
  name: Cube Agents Canvases API
  slug: open-cubesoftware-canvases-api
- collection_type: open
  name: Cube Agents ChatMessages API
  slug: open-cubesoftware-chatmessages-api
- collection_type: open
  name: Cube Agents ChatSessions API
  slug: open-cubesoftware-chatsessions-api
- collection_type: open
  name: Cube Agents ChatSettings API
  slug: open-cubesoftware-chatsettings-api
- collection_type: open
  name: Cube Agents Comments API
  slug: open-cubesoftware-comments-api
- collection_type: open
  name: Cube Agents Companies API
  slug: open-cubesoftware-companies-api
- collection_type: open
  name: Cube Agents Company Groups API
  slug: open-cubesoftware-company-groups-api
- collection_type: open
  name: Cube Agents compliance API
  slug: open-cubesoftware-compliance-api
- collection_type: open
  name: Cube Agents Connections API
  slug: open-cubesoftware-connections-api
- collection_type: open
  name: Cube Agents ContentType API
  slug: open-cubesoftware-contenttype-api
- collection_type: open
  name: Agents cube API
  slug: open-cubesoftware-cube-api
- collection_type: open
  name: Cube Agents Cube Data API
  slug: open-cubesoftware-cube-data-api
- collection_type: open
  name: Cube Agents Cube Value Range API
  slug: open-cubesoftware-cube-value-range-api
- collection_type: open
  name: Cube Agents Currencies API
  slug: open-cubesoftware-currencies-api
- collection_type: open
  name: Cube Agents Dashboard API
  slug: open-cubesoftware-dashboard-api
- collection_type: open
  name: Cube Agents Data Table Uploads API
  slug: open-cubesoftware-data-table-uploads-api
- collection_type: open
  name: Cube Agents Data Tables API
  slug: open-cubesoftware-data-tables-api
- collection_type: open
  name: Cube Agents Dimensions API
  slug: open-cubesoftware-dimensions-api
- collection_type: open
  name: Cube Agents Drilldown API
  slug: open-cubesoftware-drilldown-api
- collection_type: open
  name: Cube Agents ERP API
  slug: open-cubesoftware-erp-api
- collection_type: open
  name: Cube Agents Events API
  slug: open-cubesoftware-events-api
- collection_type: open
  name: Cube Agents Formulas API
  slug: open-cubesoftware-formulas-api
- collection_type: open
  name: Cube Agents Integrations API
  slug: open-cubesoftware-integrations-api
- collection_type: open
  name: Cube Agents Invitations API
  slug: open-cubesoftware-invitations-api
- collection_type: open
  name: Cube Agents Library API
  slug: open-cubesoftware-library-api
- collection_type: open
  name: Cube Agents Notifications API
  slug: open-cubesoftware-notifications-api
- collection_type: open
  name: Cube Agents Permissions API
  slug: open-cubesoftware-permissions-api
- collection_type: open
  name: Cube Agents permissionsets API
  slug: open-cubesoftware-permissionsets-api
- collection_type: open
  name: Cube Agents PlanModeSessions API
  slug: open-cubesoftware-planmodesessions-api
- collection_type: open
  name: Cube Agents Planning Table API
  slug: open-cubesoftware-planning-table-api
- collection_type: open
  name: Cube Agents Scenarios API
  slug: open-cubesoftware-scenarios-api
- collection_type: open
  name: Cube Agents Tags API
  slug: open-cubesoftware-tags-api
- collection_type: open
  name: Cube Agents Taskflow API
  slug: open-cubesoftware-taskflow-api
- collection_type: open
  name: Cube Agents Team API
  slug: open-cubesoftware-team-api
- collection_type: open
  name: Cube Agents User API
  slug: open-cubesoftware-user-api
- collection_type: open
  name: Cube Agents UserCompanies API
  slug: open-cubesoftware-usercompanies-api
- collection_type: open
  name: Cube Agents Workflow API
  slug: open-cubesoftware-workflow-api
common:
- group: company
  title: ''
  type: Website
  url: https://cubesoftware.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cubesoftware.com/developer-center
- group: docs
  title: ''
  type: Documentation
  url: https://help.cubesoftware.com/hc/en-us
- group: docs
  title: ''
  type: APIReference
  url: https://api.cubesoftware.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cubesoftware.com/developer-center
- group: operate
  title: ''
  type: Support
  url: https://help.cubesoftware.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.cubesoftware.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.cubesoftware.com/blog/rss.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cubesoftware.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.cubesoftware.com/book-a-demo
- group: start
  title: ''
  type: Login
  url: https://portal.cubesoftware.com/account/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cubesoftware.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cubesoftware.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.cubesoftware.com/product-updates
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cubesoftware.com
- group: auth
  title: ''
  type: Compliance
  url: https://security.cubesoftware.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cubesoftware-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cubesoftware-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cubesoftware-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cubesoftware-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cubesoftware-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/cubesoftware-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/cubesoftware-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cubesoftware-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cubesoftware-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cubesoftware-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cubesoftware-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cubesoftware-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cubesoftware-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cubesoftware-domain-security.yml
created: '2026-07-17'
description: Cube is an AI-powered financial planning and analysis (FP&A) platform for finance teams. It connects a company's source systems and spreadsheets into a single financial data model, letting teams budget, forecast, run scenario and what-if analysis, and report from the comfort of Excel and Google Sheets. The Cube API (OAuth 2.0, 296 operations across data tables, dimensions, formulas, exports, and company administration) exposes the same functionality that powers Cube's universal spreadsheet add-ons and integrations, so teams can push and pull their financial data programmatically. Cube is SOC 2 Type II certified and GDPR-compliant, built on AWS.
image: https://8159624.fs1.hubspotusercontent-na1.net/hubfs/8159624/Cube%20website%20-%202024/Logos/cube-logo-navy.svg
layout: provider
mcp_servers:
- description: ''
  name: cubesoftware-mcp.yml
  slug: cubesoftware-mcpyml
modified: '2026-07-18'
name: Cube
nav: Providers
network: true
overview: 'Cube publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Attributes API, Audit Trail API, and 39 more. Tagged areas include Company, FP&A, Financial Planning, Finance, and Budgeting.


  Cube''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 98
scopes:
- name: Cubesoftware Scopes
  scope_count: 3
  slug: cubesoftware-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 52.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 52.5
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 31.6
  previous_composite: 52.3
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
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cubesoftware/refs/heads/main/screenshots/cubesoftware-2026-07-25T210859.png
security:
- kind: authentication
  name: Cubesoftware Authentication
  slug: cubesoftware-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cubesoftware Domain Security
  slug: cubesoftware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cubesoftware Trust Center
  slug: cubesoftware-trust-center
  summary_line: SOC 2 Type II
slug: cubesoftware
tags:
- Company
- FP&A
- Financial Planning
- Finance
- Budgeting
- Forecasting
- Analytics
- Spreadsheets
- SaaS
website: https://cubesoftware.com
---
