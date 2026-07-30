---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Power Apps Agentic Access
  operation_count: 7
  slug: power-apps-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 7
apis:
- description: REST API for managing Power Apps environments, apps, flows, and connectors.
  name: Power Apps Management API
  slug: power-apps-management-api
- description: APIs for building custom components using the Power Apps Component Framework (PCF).
  name: Power Apps Component Framework API
  slug: power-apps-component-framework-api
- description: The Power Platform API provides a unified REST endpoint at api.powerplatform.com for managing environments, licensing, app management, and tenant-level governance across the entire Power Platform.
  name: Microsoft Power Platform API
  slug: microsoft-power-platform-api
- description: Client API reference for model-driven apps providing JavaScript libraries for form scripting, UI manipulation, data access, and the Xrm object model including Xrm.WebApi for data operations.
  name: Model-Driven Apps Client API
  slug: model-driven-apps-client-api
- description: Custom connectors allow you to create wrappers around REST or SOAP APIs for use in Power Apps, Power Automate, Logic Apps, and Copilot Studio, enabling integration with services not available as prebu
  name: Custom Connectors API
  slug: custom-connectors-api
- description: System operations and functions exposed by the Web API.
  name: Microsoft Power Apps System API
  slug: power-apps-system-api
- description: CRUD operations against Dataverse tables (entities).
  name: Microsoft Power Apps Tables API
  slug: power-apps-tables-api
artifact_total: 62
collections:
- collection_type: open
  name: Microsoft Dataverse Web API (Power Apps)
  slug: open-power-apps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/power-apps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/power-apps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/power-apps-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/power-apps-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://make.powerapps.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://powerapps.microsoft.com/en-us/developers/
- group: operate
  title: ''
  type: Support
  url: https://powerusers.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://powerapps.microsoft.com/en-us/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://powerapps.microsoft.com/en-us/pricing/
- group: operate
  title: ''
  type: Support
  url: https://powerapps.microsoft.com/en-us/support/
- group: learn
  title: ''
  type: Training
  url: https://docs.microsoft.com/en-us/learn/powerplatform/power-apps
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft/PowerApps-Samples
- group: operate
  title: ''
  type: StatusPage
  url: https://status.powerplatform.microsoft.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/power-platform/developer/get-started
- group: other
  title: ''
  type: Resources
  url: https://learn.microsoft.com/en-us/power-platform/alm/overview-alm
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/powerapps-cli
- group: other
  title: ''
  type: Resources
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/developer-tools
- group: other
  title: ''
  type: Resources
  url: https://learn.microsoft.com/en-us/power-platform/alm/devops-github-actions
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authentication
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/power-platform/admin/programmability-whats-new-changed
- group: other
  title: ''
  type: Resources
  url: https://learn.microsoft.com/en-us/connectors/connector-reference/
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/powerplatform/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/microsoft/powerbi-modeling-mcp
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/microsoft/power-platform-skills
created: '2024'
description: Microsoft Power Apps is a suite of apps, services, and connectors, as well as a data platform, that provides a rapid development environment to build custom apps for your business needs.
features:
- Low-code and no-code app development
- Microsoft Dataverse data platform
- Power Apps Component Framework (PCF)
- Model-driven and canvas app types
- Custom connectors for REST and SOAP APIs
- Power Platform unified administration API
- Client-side scripting with Xrm object model
- AI Builder integration for intelligent apps
finops:
- name: Power Apps Finops
  service_category: API
  slug: power-apps-finops
image: https://powerusers.microsoft.com/t5/image/serverpage/image-id/98171i62B0C7ECED0A0B8B/image-size/large
integrations:
- Microsoft 365
- Microsoft Teams
- Microsoft Azure
- Power Automate
- Power BI
- Dynamics 365
- SharePoint
- SQL Server
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Microsoft Power Apps
nav: Providers
network: true
overview: 'Microsoft Power Apps publishes 2 APIs on the [APIs.io](https://apis.io/) network: System API and Tables API. Tagged areas include App Development, Business Applications, Cloud Platform, Low-Code, and Microsoft.


  Microsoft Power Apps'' developer surface includes authentication, developer portal, support, engineering blog, pricing, training material, getting-started guide, and 17 more developer resources.'
plans:
- name: Power Apps Plans Pricing
  plan_count: 3
  slug: power-apps-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 5
  name: Power Apps Rate Limits
  slug: power-apps-rate-limits
scopes:
- name: Power Apps Scopes
  scope_count: 2
  slug: power-apps-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 50.5
  delta: -1.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 55.9
    developer_ergonomics: 52.2
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/power-apps/refs/heads/main/screenshots/power-apps-2026-06-20T192021.png
security:
- kind: authentication
  name: Power Apps Authentication
  slug: power-apps-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Power Apps Domain Security
  slug: power-apps-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 52
skills:
- name: activate-site
  slug: activate-site
- name: add-azuredevops
  slug: add-azuredevops
- name: add-cloud-flow
  slug: add-cloud-flow
- name: add-connector
  slug: add-connector
- name: add-data-source
  slug: add-data-source
- name: add-datasource
  slug: add-datasource
- name: add-dataverse
  slug: add-dataverse
- name: add-excel
  slug: add-excel
- name: add-mcscopilot
  slug: add-mcscopilot
- name: add-office365
  slug: add-office365
- name: add-onedrive
  slug: add-onedrive
- name: add-sample-data
  slug: add-sample-data
- name: add-seo
  slug: add-seo
- name: add-server-logic
  slug: add-server-logic
- name: add-sharepoint
  slug: add-sharepoint
- name: add-teams
  slug: add-teams
- name: audit-permissions
  slug: audit-permissions
- name: canvas-app
  slug: canvas-app
- name: configure-canvas-mcp
  slug: configure-canvas-mcp
- name: configure-env-variables
  slug: configure-env-variables
- name: create-code-app
  slug: create-code-app
- name: create-site
  slug: create-site
- name: create-webroles
  slug: create-webroles
- name: deploy-pipeline
  slug: deploy-pipeline
slug: power-apps
tags:
- App Development
- Business Applications
- Cloud Platform
- Low-Code
- Microsoft
- No-Code
use_cases:
- Custom business application development
- Data-driven enterprise app creation
- Legacy system modernization
- Citizen developer enablement
- Mobile workforce applications
- Process automation with Power Automate integration
website: https://powerapps.microsoft.com/en-us/developers/
---
