---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Microsoft Dynamics Agentic Access
  operation_count: 59
  slug: microsoft-dynamics-agentic-access
  summary_line: 59 operations · 29 acting
api_count: 19
apis:
- description: The Accounts API from Microsoft Dynamics — 3 operation(s) for accounts.
  name: Microsoft Dynamics Accounts API
  slug: microsoft-dynamics-accounts-api
- description: The Activities API from Microsoft Dynamics — 1 operation(s) for activities.
  name: Microsoft Dynamics Activities API
  slug: microsoft-dynamics-activities-api
- description: The Cases API from Microsoft Dynamics — 1 operation(s) for cases.
  name: Microsoft Dynamics Cases API
  slug: microsoft-dynamics-cases-api
- description: The Companies API from Microsoft Dynamics — 1 operation(s) for companies.
  name: Microsoft Dynamics Companies API
  slug: microsoft-dynamics-companies-api
- description: The Contacts API from Microsoft Dynamics — 2 operation(s) for contacts.
  name: Microsoft Dynamics Contacts API
  slug: microsoft-dynamics-contacts-api
- description: The Customers API from Microsoft Dynamics — 3 operation(s) for customers.
  name: Microsoft Dynamics Customers API
  slug: microsoft-dynamics-customers-api
- description: The Employees API from Microsoft Dynamics — 1 operation(s) for employees.
  name: Microsoft Dynamics Employees API
  slug: microsoft-dynamics-employees-api
- description: The General Ledger API from Microsoft Dynamics — 2 operation(s) for general ledger.
  name: Microsoft Dynamics General Ledger API
  slug: microsoft-dynamics-general-ledger-api
- description: The Human Resources API from Microsoft Dynamics — 1 operation(s) for human resources.
  name: Microsoft Dynamics Human Resources API
  slug: microsoft-dynamics-human-resources-api
- description: The Items API from Microsoft Dynamics — 1 operation(s) for items.
  name: Microsoft Dynamics Items API
  slug: microsoft-dynamics-items-api
- description: The Journals API from Microsoft Dynamics — 1 operation(s) for journals.
  name: Microsoft Dynamics Journals API
  slug: microsoft-dynamics-journals-api
- description: The Leads API from Microsoft Dynamics — 2 operation(s) for leads.
  name: Microsoft Dynamics Leads API
  slug: microsoft-dynamics-leads-api
- description: The Opportunities API from Microsoft Dynamics — 2 operation(s) for opportunities.
  name: Microsoft Dynamics Opportunities API
  slug: microsoft-dynamics-opportunities-api
- description: The Products API from Microsoft Dynamics — 1 operation(s) for products.
  name: Microsoft Dynamics Products API
  slug: microsoft-dynamics-products-api
- description: The Purchase Invoices API from Microsoft Dynamics — 1 operation(s) for purchase invoices.
  name: Microsoft Dynamics Purchase Invoices API
  slug: microsoft-dynamics-purchase-invoices-api
- description: The Purchase Orders API from Microsoft Dynamics — 2 operation(s) for purchase orders.
  name: Microsoft Dynamics Purchase Orders API
  slug: microsoft-dynamics-purchase-orders-api
- description: The Sales Invoices API from Microsoft Dynamics — 1 operation(s) for sales invoices.
  name: Microsoft Dynamics Sales Invoices API
  slug: microsoft-dynamics-sales-invoices-api
- description: The Sales Orders API from Microsoft Dynamics — 2 operation(s) for sales orders.
  name: Microsoft Dynamics Sales Orders API
  slug: microsoft-dynamics-sales-orders-api
- description: The Vendors API from Microsoft Dynamics — 2 operation(s) for vendors.
  name: Microsoft Dynamics Vendors API
  slug: microsoft-dynamics-vendors-api
artifact_total: 44
collections:
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API
  slug: open-microsoft-dynamics-business-central
- collection_type: open
  name: Microsoft Dynamics 365 / Dataverse Webhooks
  slug: open-microsoft-dynamics-dataverse-webhooks-asyncapi
- collection_type: open
  name: Microsoft Dynamics 365 Dataverse Web API
  slug: open-microsoft-dynamics-dataverse
- collection_type: open
  name: Microsoft Dynamics 365 Finance & Operations Data API
  slug: open-microsoft-dynamics-finance-operations
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-dynamics-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-dynamics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-dynamics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-dynamics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-dynamics-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-dynamics
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/dynamics365/
- group: operate
  title: ''
  type: Support
  url: https://community.dynamics.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/dynamics365/get-started/
- group: company
  title: ''
  type: Blog
  url: https://cloudblogs.microsoft.com/dynamics365/
created: '2025-01-01'
description: 'Microsoft Dynamics 365 is a suite of enterprise resource planning (ERP) and customer relationship management (CRM) applications. It provides APIs across three main platforms: Business Central for small and mid-sized business ERP, Dataverse Web API for CRM and customer engagement, and Finance & Operations for enterprise-grade ERP covering finance, supply chain, manufacturing, and human resources. All APIs use OData v4 conventions and authenticate via Microsoft Entra ID.'
finops:
- name: Microsoft Dynamics Finops
  service_category: Business Applications / CRM-ERP
  slug: microsoft-dynamics-finops
graphqls:
- description: This conceptual GraphQL schema represents the Microsoft Dynamics 365 CRM and ERP platform, covering
  name: Microsoft Dynamics 365 GraphQL Schema
  slug: microsoft-dynamics-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-dynamics.png
json_schemas:
- name: Account
  property_count: 19
  slug: account
- name: Contact
  property_count: 18
  slug: contact
- name: Customer
  property_count: 18
  slug: customer
- name: Employee
  property_count: 22
  slug: employee
- name: Item
  property_count: 13
  slug: item
- name: Lead
  property_count: 21
  slug: lead
- name: Opportunity
  property_count: 16
  slug: opportunity
- name: Sales Invoice
  property_count: 13
  slug: sales-invoice
- name: Sales Order
  property_count: 12
  slug: sales-order
- name: Vendor
  property_count: 16
  slug: vendor
jsonld:
- class_count: 0
  name: Microsoft Dynamics Context
  property_count: 10
  slug: microsoft-dynamics-context
layout: provider
modified: '2026-05-30'
name: Microsoft Dynamics
nav: Providers
network: true
overview: 'Microsoft Dynamics publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Cases API, and 16 more. Tagged areas include CRM, ERP, and Microsoft Dynamics.


  The Microsoft Dynamics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Dynamics'' developer surface includes authentication, documentation, support, getting-started guide, engineering blog, and 6 more developer resources.'
plans:
- name: Microsoft Dynamics Plans Pricing
  plan_count: 13
  slug: microsoft-dynamics-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Microsoft Dynamics Rate Limits
  slug: microsoft-dynamics-rate-limits
rules:
- name: Microsoft Dynamics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-dynamics-jsonschema-spectral-rules
scopes:
- name: Microsoft Dynamics Scopes
  scope_count: 3
  slug: microsoft-dynamics-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 51.0
  delta: -2.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 75.7
    developer_ergonomics: 37.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 53.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 95.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics/refs/heads/main/screenshots/microsoft-dynamics-2026-06-20T185452.png
security:
- kind: authentication
  name: Microsoft Dynamics Authentication
  slug: microsoft-dynamics-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Dynamics Domain Security
  slug: microsoft-dynamics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Dynamics Vulnerability Disclosure
  slug: microsoft-dynamics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-dynamics
tags:
- CRM
- ERP
- Microsoft Dynamics
---
