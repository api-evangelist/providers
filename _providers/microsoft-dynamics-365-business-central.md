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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Microsoft Dynamics 365 Business Central Agentic Access
  operation_count: 26
  slug: microsoft-dynamics-365-business-central-agentic-access
  summary_line: 26 operations · 14 acting
api_count: 9
apis:
- description: OData v4 endpoints exposing published Business Central pages and queries as web services for custom integrations, reporting, and Power Platform connectors when standard API v2.0 entities are insuffici
  name: Business Central OData Web Services
  slug: odata-web-services
- description: Administration Center REST API for managing Business Central environments, tenants, telemetry, update settings, and notifications programmatically for ISVs and delegated administrators.
  name: Business Central Administration Center API
  slug: admin-center-api
- description: Business Central company entities
  name: Microsoft Dynamics 365 Business Central Companies API
  slug: microsoft-dynamics-365-business-central-companies-api
- description: Customer master data
  name: Microsoft Dynamics 365 Business Central Customers API
  slug: microsoft-dynamics-365-business-central-customers-api
- description: Item master data
  name: Microsoft Dynamics 365 Business Central Items API
  slug: microsoft-dynamics-365-business-central-items-api
- description: Purchase order documents
  name: Microsoft Dynamics 365 Business Central PurchaseOrders API
  slug: microsoft-dynamics-365-business-central-purchaseorders-api
- description: Sales invoice documents
  name: Microsoft Dynamics 365 Business Central SalesInvoices API
  slug: microsoft-dynamics-365-business-central-salesinvoices-api
- description: Sales order documents
  name: Microsoft Dynamics 365 Business Central SalesOrders API
  slug: microsoft-dynamics-365-business-central-salesorders-api
- description: Vendor master data
  name: Microsoft Dynamics 365 Business Central Vendors API
  slug: microsoft-dynamics-365-business-central-vendors-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies API
  slug: open-microsoft-dynamics-365-business-central-companies-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies Customers API
  slug: open-microsoft-dynamics-365-business-central-customers-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies Items API
  slug: open-microsoft-dynamics-365-business-central-items-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies PurchaseOrders API
  slug: open-microsoft-dynamics-365-business-central-purchaseorders-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies SalesInvoices API
  slug: open-microsoft-dynamics-365-business-central-salesinvoices-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies SalesOrders API
  slug: open-microsoft-dynamics-365-business-central-salesorders-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies Vendors API
  slug: open-microsoft-dynamics-365-business-central-vendors-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0
  slug: open-microsoft-dynamics-365-business-central
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-dynamics-365-business-central-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-dynamics-365-business-central-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-dynamics-365-business-central-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-dynamics-365-business-central-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-dynamics-365-business-central-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-dynamics-365-business-central-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/dynamics-365/products/business-central
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/dynamics-365/products/business-central/pricing
- group: start
  title: ''
  type: Signup
  url: https://signup.microsoft.com/get-started/signup?products=22b1949b-c5dd-4b06-9c19-1d2fa17e7a9d
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/dynamics-365/blog/feed/
created: '2026-05-11'
description: Microsoft Dynamics 365 Business Central is an all-in-one cloud ERP solution for small and mid-sized businesses that brings together finance, sales, service, project management, supply chain, manufacturing, and operations on the Microsoft Cloud. Business Central exposes a standard REST API (v2.0) plus custom and OData web services so partners can build Connect apps, automate processes, and integrate Business Central with Power Platform and third-party systems using OAuth 2.0 authentication via Microsoft Entra ID.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-dynamics-365-business-central.png
layout: provider
modified: '2026-05-11'
name: Microsoft Dynamics 365 Business Central
nav: Providers
network: true
overview: 'Microsoft Dynamics 365 Business Central publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Companies API, Customers API, Items API, and 4 more. Tagged areas include ERP, Cloud ERP, Finance, Accounting, and Supply Chain.


  Microsoft Dynamics 365 Business Central''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 7 more developer resources.'
random_paper: 17
scopes:
- name: Microsoft Dynamics 365 Business Central Scopes
  scope_count: 1
  slug: microsoft-dynamics-365-business-central-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 31.4
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 31.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics-365-business-central/refs/heads/main/screenshots/microsoft-dynamics-365-business-central-2026-06-20T185459.png
security:
- kind: authentication
  name: Microsoft Dynamics 365 Business Central Authentication
  slug: microsoft-dynamics-365-business-central-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Dynamics 365 Business Central Domain Security
  slug: microsoft-dynamics-365-business-central-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Dynamics 365 Business Central Vulnerability Disclosure
  slug: microsoft-dynamics-365-business-central-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Dynamics 365 Business Central Trust Center
  slug: microsoft-dynamics-365-business-central-trust-center
  summary_line: GDPR
slug: microsoft-dynamics-365-business-central
tags:
- ERP
- Cloud ERP
- Finance
- Accounting
- Supply Chain
- Small Business
- Mid-Market
- Microsoft Dynamics 365
website: https://www.microsoft.com/en-us/dynamics-365/products/business-central
---
