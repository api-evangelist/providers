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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Microsoft Dynamics 365 Sales Agentic Access
  operation_count: 31
  slug: microsoft-dynamics-365-sales-agentic-access
  summary_line: 31 operations · 18 acting
api_count: 11
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
artifact_total: 18
collections:
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
  type: Signup
  url: https://dynamics.microsoft.com/en-us/sales/overview/
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/dynamics-365/blog/feed/
created: '2026-05-11'
description: Microsoft Dynamics 365 Sales is Microsoft's enterprise CRM application for managing leads, opportunities, accounts, contacts, sales pipelines, forecasts, and customer relationships, built on the Microsoft Dataverse platform and integrated with Microsoft 365, Teams, Copilot, and Power Platform. Developers programmatically interact with Dynamics 365 Sales data through the Dataverse Web API, an OData v4.0 RESTful interface that exposes every table, action, and function in a Sales environment. The Dataverse Web API uses OAuth 2.0 (Microsoft Entra ID) Bearer token authentication and is reached at a per-environment endpoint such as https://{org}.api.crm.dynamics.com/api/data/v9.2/.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-dynamics-365-sales.png
layout: provider
modified: '2026-05-11'
name: Microsoft Dynamics 365 Sales
nav: Providers
network: true
overview: 'Microsoft Dynamics 365 Sales publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, $batch API, Contacts API, and 7 more. Tagged areas include CRM, Sales, Customer Relationship Management, Dynamics 365, and Microsoft.


  Microsoft Dynamics 365 Sales'' developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 9 more developer resources.'
random_paper: 115
scopes:
- name: Microsoft Dynamics 365 Sales Scopes
  scope_count: 1
  slug: microsoft-dynamics-365-sales-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: thin
  composite: 30.5
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 57.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
