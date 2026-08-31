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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Microsoft Dynamics 365 Sales Agentic Access
  operation_count: 31
  slug: microsoft-dynamics-365-sales-agentic-access
  summary_line: 31 operations · 18 acting
api_count: 1
apis:
- description: OData v4.0 RESTful Web API for Microsoft Dataverse used to create, read, update, and delete Dynamics 365 Sales records (leads, opportunities, accounts, contacts, quotes, orders, invoices, products) an
  name: Microsoft Dataverse Web API (Dynamics 365 Sales)
  slug: dataverse-web-api
- description: Account (customer organization) records
  name: Microsoft Dynamics 365 Sales Accounts API
  slug: microsoft-dynamics-365-sales-accounts-api
- description: The $batch API from Microsoft Dynamics 365 Sales — 1 operation(s) for $batch.
  name: Microsoft Dynamics 365 Sales $batch API
  slug: microsoft-dynamics-365-sales-batch-api
- description: Contact (person) records
  name: Microsoft Dynamics 365 Sales Contacts API
  slug: microsoft-dynamics-365-sales-contacts-api
- description: Invoice records
  name: Microsoft Dynamics 365 Sales Invoices API
  slug: microsoft-dynamics-365-sales-invoices-api
- description: Sales lead records
  name: Microsoft Dynamics 365 Sales Leads API
  slug: microsoft-dynamics-365-sales-leads-api
- description: Sales opportunity records
  name: Microsoft Dynamics 365 Sales Opportunities API
  slug: microsoft-dynamics-365-sales-opportunities-api
- description: Product records
  name: Microsoft Dynamics 365 Sales Products API
  slug: microsoft-dynamics-365-sales-products-api
- description: Sales quote records
  name: Microsoft Dynamics 365 Sales Quotes API
  slug: microsoft-dynamics-365-sales-quotes-api
- description: Sales order records
  name: Microsoft Dynamics 365 Sales SalesOrders API
  slug: microsoft-dynamics-365-sales-salesorders-api
- description: Activity tasks
  name: Microsoft Dynamics 365 Sales Tasks API
  slug: microsoft-dynamics-365-sales-tasks-api
- description: Microsoft's hosted Model Context Protocol server for Dynamics 365 Sales. Exposes 20 sales tools to any MCP-capable agent — lead and account research, competitor research, engagement summaries, lead qu
  name: Dynamics 365 Sales MCP Server
  slug: dynamics-365-sales-mcp-server
artifact_total: 34
asyncapis:
- description: ''
  name: Microsoft Dynamics 365 Sales Webhooks
  slug: microsoft-dynamics-365-sales-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts API
  slug: open-microsoft-dynamics-365-sales-accounts-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts $batch API
  slug: open-microsoft-dynamics-365-sales-batch-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Contacts API
  slug: open-microsoft-dynamics-365-sales-contacts-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Invoices API
  slug: open-microsoft-dynamics-365-sales-invoices-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Leads API
  slug: open-microsoft-dynamics-365-sales-leads-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Opportunities API
  slug: open-microsoft-dynamics-365-sales-opportunities-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Products API
  slug: open-microsoft-dynamics-365-sales-products-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Quotes API
  slug: open-microsoft-dynamics-365-sales-quotes-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts SalesOrders API
  slug: open-microsoft-dynamics-365-sales-salesorders-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales) Accounts Tasks API
  slug: open-microsoft-dynamics-365-sales-tasks-api
- collection_type: open
  name: Microsoft Dataverse Web API (Dynamics 365 Sales)
  slug: open-microsoft-dynamics-365-sales
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-dynamics-365-sales-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-dynamics-365-sales-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-dynamics-365-sales-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-dynamics-365-sales-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-dynamics-365-sales-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-dynamics-365-sales-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MicrosoftDocs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-dynamics-365-sales
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/dynamics-365/products/sales
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/dynamics365/sales/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/dynamics-365/products/sales/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dynamics.microsoft.com/en-us/sales/overview/
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/dynamics-365/blog/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/overview
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/reference/about
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/perform-operations-web-api
- group: operate
  title: ''
  type: Support
  url: https://www.microsoft.com/en-us/dynamics-365/support
- group: operate
  title: ''
  type: Community
  url: https://community.dynamics.com/forums/thread/?groupid=d365sales
- group: operate
  title: ''
  type: Roadmap
  url: https://learn.microsoft.com/en-us/dynamics365/release-plans/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/servicesagreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: SLA
  url: https://www.microsoft.com/licensing/docs/view/Service-Level-Agreements-SLA-for-Online-Services
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-dynamics-365-sales-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/microsoft-dynamics-365-sales-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-dynamics-365-sales-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-dynamics-365-sales-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-dynamics-365-sales-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-dynamics-365-sales-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-dynamics-365-sales-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-dynamics-365-sales-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/en-us/msrc/cvd
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center/compliance/compliance-overview
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-dynamics-365-sales-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-dynamics-365-sales-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-dynamics-365-sales-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-dynamics-365-sales-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-dynamics-365-sales-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/power-platform/important-changes-coming
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-dynamics-365-sales-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/microsoft-dynamics-365-sales-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/microsoft-dynamics-365-sales-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/microsoft-dynamics-365-sales-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-dynamics-365-sales-rate-limits.yml
created: '2026-05-11'
description: Microsoft Dynamics 365 Sales is Microsoft's enterprise CRM application for managing leads, opportunities, accounts, contacts, sales pipelines, forecasts, and customer relationships, built on the Microsoft Dataverse platform and integrated with Microsoft 365, Teams, Copilot, and Power Platform. Developers programmatically interact with Dynamics 365 Sales data through the Dataverse Web API, an OData v4.0 RESTful interface that exposes every table, action, and function in a Sales environment. The Dataverse Web API uses OAuth 2.0 (Microsoft Entra ID) Bearer token authentication and is reached at a per-environment endpoint such as https://{org}.api.crm.dynamics.com/api/data/v9.2/.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-dynamics-365-sales.png
layout: provider
mcp_servers:
- description: ''
  name: Microsoft Dynamics 365 Sales MCP Server
  slug: microsoft-dynamics-365-sales-mcp-server
modified: '2026-08-13'
name: Microsoft Dynamics 365 Sales
nav: Providers
network: true
overview: 'Microsoft Dynamics 365 Sales publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, $batch API, Contacts API, and 7 more. Tagged areas include CRM, Sales, Customer Relationship Management, Dynamics 365, and Microsoft.


  The Microsoft Dynamics 365 Sales catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Microsoft Dynamics 365 Sales'' developer surface includes authentication, documentation, pricing, signup flow, engineering blog, API reference, getting-started guide, and 39 more developer resources.'
plans:
- name: Microsoft Dynamics 365 Sales Plans Pricing
  plan_count: 4
  slug: microsoft-dynamics-365-sales-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Microsoft Dynamics 365 Sales Rate Limits
  slug: microsoft-dynamics-365-sales-rate-limits
scopes:
- name: Microsoft Dynamics 365 Sales Scopes
  scope_count: 2
  slug: microsoft-dynamics-365-sales-scopes
  summary_line: 2 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 67.5
  coverage:
    artifact_dirs: 25
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 61.2
    developer_ergonomics: 80.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics-365-sales/refs/heads/main/screenshots/microsoft-dynamics-365-sales-2026-06-20T185455.png
security:
- kind: authentication
  name: Microsoft Dynamics 365 Sales Authentication
  slug: microsoft-dynamics-365-sales-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Dynamics 365 Sales Domain Security
  slug: microsoft-dynamics-365-sales-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Dynamics 365 Sales Vulnerability Disclosure
  slug: microsoft-dynamics-365-sales-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Dynamics 365 Sales Trust Center
  slug: microsoft-dynamics-365-sales-trust-center
  summary_line: GDPR
slug: microsoft-dynamics-365-sales
tags:
- CRM
- Sales
- Customer Relationship Management
- Dynamics 365
- Microsoft
- Dataverse
- OData
- Sales Automation
website: https://www.microsoft.com/en-us/dynamics-365/products/sales
---
