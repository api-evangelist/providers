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
  band: agent-ready
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Microsoft Dynamics 365 Agentic Access
  operation_count: 58
  slug: microsoft-dynamics-365-agentic-access
  summary_line: 58 operations · 29 acting
api_count: 1
apis:
- description: API for managing financial operations, accounting, budgeting, and enterprise resource planning.
  name: Dynamics 365 Finance & Operations API
  slug: dynamics-365-finance-operations-api
- description: API for managing marketing campaigns, customer journeys, email marketing, and lead scoring.
  name: Dynamics 365 Marketing API
  slug: dynamics-365-marketing-api
- description: API for managing inventory, warehouse operations, procurement, and supply chain processes.
  name: Dynamics 365 Supply Chain Management API
  slug: dynamics-365-supply-chain-management-api
- description: API for managing e-commerce operations, retail stores, omnichannel commerce, and customer experiences.
  name: Dynamics 365 Commerce API
  slug: dynamics-365-commerce-api
- description: API for building applications based on unified customer data, enabling customer data unification, segmentation, and enrichment through programmatic access.
  name: Dynamics 365 Customer Insights Data API
  slug: dynamics-365-customer-insights-data-api
- description: API for managing real-time customer journeys, segments, and event-driven marketing interactions programmatically.
  name: Dynamics 365 Customer Insights Journeys API
  slug: dynamics-365-customer-insights-journeys-api
- description: API for managing field service operations including work orders, scheduling, resource availability, and work hour calendars.
  name: Dynamics 365 Field Service API
  slug: dynamics-365-field-service-api
- description: API for managing human resources operations including employee data, payroll integration, applicant tracking, and benefits administration.
  name: Dynamics 365 Human Resources API
  slug: dynamics-365-human-resources-api
- description: API for managing project operations including project scheduling, resource management, time and expense tracking, and project financials.
  name: Dynamics 365 Project Operations API
  slug: dynamics-365-project-operations-api
- baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Business that represents a customer or potential customer. The company that is billed in business transactions.
  name: Microsoft Dynamics 365 Accounts API
  slug: microsoft-dynamics-365-accounts-api
- baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Person with whom a business unit has a relationship, such as a customer, supplier, or colleague.
  name: Microsoft Dynamics 365 Contacts API
  slug: microsoft-dynamics-365-contacts-api
- baseURL: https://[org].api.crm.dynamics.com/api/data/v9.2
  baseurl_source: declared
  description: Potential revenue-generating event or sale to an account that needs to be tracked through the sales process to completion.
  name: Microsoft Dynamics 365 Opportunities API
  slug: microsoft-dynamics-365-opportunities-api
- baseURL_template: https://{organization}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: spec_template
  description: The Activities API from Microsoft Dynamics — 1 operation(s) for activities.
  name: Microsoft Dynamics 365 Activities API
  slug: microsoft-dynamics-activities-api
- baseURL_template: https://{organization}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: spec_template
  description: The Cases API from Microsoft Dynamics — 1 operation(s) for cases.
  name: Microsoft Dynamics 365 Cases API
  slug: microsoft-dynamics-cases-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Companies API from Microsoft Dynamics — 1 operation(s) for companies.
  name: Microsoft Dynamics 365 Companies API
  slug: microsoft-dynamics-companies-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Customers API from Microsoft Dynamics — 3 operation(s) for customers.
  name: Microsoft Dynamics 365 Customers API
  slug: microsoft-dynamics-customers-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Employees API from Microsoft Dynamics — 1 operation(s) for employees.
  name: Microsoft Dynamics 365 Employees API
  slug: microsoft-dynamics-employees-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The General Ledger API from Microsoft Dynamics — 2 operation(s) for general ledger.
  name: Microsoft Dynamics 365 General Ledger API
  slug: microsoft-dynamics-general-ledger-api
- baseURL_template: https://{environment}.operations.dynamics.com/data
  baseurl_source: spec_template
  description: The Human Resources API from Microsoft Dynamics — 1 operation(s) for human resources.
  name: Microsoft Dynamics 365 Human Resources API
  slug: microsoft-dynamics-human-resources-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Items API from Microsoft Dynamics — 1 operation(s) for items.
  name: Microsoft Dynamics 365 Items API
  slug: microsoft-dynamics-items-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Journals API from Microsoft Dynamics — 1 operation(s) for journals.
  name: Microsoft Dynamics 365 Journals API
  slug: microsoft-dynamics-journals-api
- baseURL_template: https://{organization}.api.crm.dynamics.com/api/data/v9.2
  baseurl_source: spec_template
  description: The Leads API from Microsoft Dynamics — 2 operation(s) for leads.
  name: Microsoft Dynamics 365 Leads API
  slug: microsoft-dynamics-leads-api
- baseURL_template: https://{environment}.operations.dynamics.com/data
  baseurl_source: spec_template
  description: The Products API from Microsoft Dynamics — 1 operation(s) for products.
  name: Microsoft Dynamics 365 Products API
  slug: microsoft-dynamics-products-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Purchase Invoices API from Microsoft Dynamics — 1 operation(s) for purchase invoices.
  name: Microsoft Dynamics 365 Purchase Invoices API
  slug: microsoft-dynamics-purchase-invoices-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Purchase Orders API from Microsoft Dynamics — 2 operation(s) for purchase orders.
  name: Microsoft Dynamics 365 Purchase Orders API
  slug: microsoft-dynamics-purchase-orders-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Sales Invoices API from Microsoft Dynamics — 1 operation(s) for sales invoices.
  name: Microsoft Dynamics 365 Sales Invoices API
  slug: microsoft-dynamics-sales-invoices-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Sales Orders API from Microsoft Dynamics — 2 operation(s) for sales orders.
  name: Microsoft Dynamics 365 Sales Orders API
  slug: microsoft-dynamics-sales-orders-api
- baseURL_template: https://api.businesscentral.dynamics.com/v2.0/{tenantId}/{environment}/api/v2.0
  baseurl_source: spec_template
  description: The Vendors API from Microsoft Dynamics — 2 operation(s) for vendors.
  name: Microsoft Dynamics 365 Vendors API
  slug: microsoft-dynamics-vendors-api
artifact_total: 67
collections:
- collection_type: postman
  name: Microsoft Dynamics 365 Dataverse Web Accounts API
  slug: postman-microsoft-dynamics-365-accounts-api
- collection_type: postman
  name: Microsoft Dynamics 365 Dataverse Web Accounts Contacts API
  slug: postman-microsoft-dynamics-365-contacts-api
- collection_type: postman
  name: Microsoft Dynamics 365 Dataverse Web Accounts Opportunities API
  slug: postman-microsoft-dynamics-365-opportunities-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Dynamics 365 Dataverse Web Accounts API
  slug: open-microsoft-dynamics-365-accounts-api
- collection_type: open
  name: Microsoft Dynamics 365 Dataverse Web Accounts Contacts API
  slug: open-microsoft-dynamics-365-contacts-api
- collection_type: open
  name: Microsoft Dynamics 365 Dataverse Web API
  slug: open-microsoft-dynamics-365-dataverse-web-api
- collection_type: open
  name: Microsoft Dynamics 365 Dataverse Web Accounts Opportunities API
  slug: open-microsoft-dynamics-365-opportunities-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics-365/refs/heads/main/capabilities/microsoft-dynamics-365-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-dynamics-365-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-dynamics-365/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics-365/refs/heads/main/agentic-access/microsoft-dynamics-365-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-dynamics-365-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics-365/refs/heads/main/security/microsoft-dynamics-365-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-dynamics-365-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics-365/refs/heads/main/authentication/microsoft-dynamics-365-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-dynamics-365-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics-365/refs/heads/main/scopes/microsoft-dynamics-365-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-dynamics-365-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-dynamics
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.microsoft.com/azure/active-directory/develop/
- group: build
  title: ''
  type: SDKs
  url: https://docs.microsoft.com/powerapps/developer/data-platform/sdk/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dynamics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/licensing/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: operate
  title: ''
  type: Support
  url: https://dynamics.microsoft.com/support/
- group: docs
  title: ''
  type: REST API Reference
  url: https://learn.microsoft.com/en-us/rest/dynamics365/
- group: operate
  title: ''
  type: Release Plans
  url: https://learn.microsoft.com/en-us/dynamics365/release-plans/
- group: operate
  title: ''
  type: Community Forums
  url: https://community.dynamics.com/
- group: other
  title: ''
  type: Power Platform Admin Center
  url: https://learn.microsoft.com/en-us/power-platform/admin/admin-documentation
- group: other
  title: ''
  type: API Limits Overview
  url: https://learn.microsoft.com/en-us/power-apps/maker/data-platform/api-limits-overview
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/dynamics-365/blog/feed/
created: '2025-01-20'
description: Microsoft Dynamics 365 is a cloud-based suite of business applications that unify CRM and ERP capabilities to help organizations manage sales, marketing, customer service, finance, operations, and commerce.
finops:
- name: Microsoft Dynamics 365 Finops
  service_category: Business Applications / CRM-ERP
  slug: microsoft-dynamics-365-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-dynamics-365.png
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
- name: Microsoft Dynamics 365 Account
  property_count: 79
  slug: microsoft-dynamics-365-account
- name: AccountCreate
  property_count: 0
  slug: microsoft-dynamics-365-accountcreate
- name: AccountUpdate
  property_count: 42
  slug: microsoft-dynamics-365-accountupdate
- name: Contact
  property_count: 76
  slug: microsoft-dynamics-365-contact
- name: ContactCreate
  property_count: 0
  slug: microsoft-dynamics-365-contactcreate
- name: ContactUpdate
  property_count: 41
  slug: microsoft-dynamics-365-contactupdate
- name: ODataError
  property_count: 1
  slug: microsoft-dynamics-365-odataerror
- name: Opportunity
  property_count: 56
  slug: microsoft-dynamics-365-opportunity
- name: OpportunityCreate
  property_count: 0
  slug: microsoft-dynamics-365-opportunitycreate
- name: OpportunityUpdate
  property_count: 32
  slug: microsoft-dynamics-365-opportunityupdate
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
json_structures:
- name: Microsoft Dynamics 365 Structure
  property_count: 0
  slug: microsoft-dynamics-365-structure
jsonld:
- class_count: 0
  name: Microsoft Dynamics 365 Context
  property_count: 3
  slug: microsoft-dynamics-365-context
- class_count: 0
  name: Microsoft Dynamics Context
  property_count: 10
  slug: microsoft-dynamics-context
layout: provider
modified: '2026-05-19'
name: Microsoft Dynamics 365
nav: Providers
network: true
overview: 'Microsoft Dynamics 365 publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Contacts API, Opportunities API, and 25 more. Tagged areas include Business Applications, Cloud, CRM, Enterprise, and ERP.


  The Microsoft Dynamics 365 catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Microsoft Dynamics 365''s developer surface includes authentication, developer portal, support, engineering blog, and 18 more developer resources.'
plans:
- name: Microsoft Dynamics 365 Plans Pricing
  plan_count: 19
  slug: microsoft-dynamics-365-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 6
  name: Microsoft Dynamics 365 Rate Limits
  slug: microsoft-dynamics-365-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Dynamics 365 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-dynamics-365-jsonschema-spectral-rules
scopes:
- name: Microsoft Dynamics 365 Scopes
  scope_count: 1
  slug: microsoft-dynamics-365-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.3
    catalog_earned_first_party: 0.0
    catalog_gap: 56.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 63.4
    developer_ergonomics: 53.6
    discoverability: 58.9
    operational_transparency: 26.3
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-dynamics-365/refs/heads/main/screenshots/microsoft-dynamics-365-2026-06-20T185452.png
security:
- kind: authentication
  name: Microsoft Dynamics 365 Authentication
  slug: microsoft-dynamics-365-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Dynamics 365 Domain Security
  slug: microsoft-dynamics-365-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-dynamics-365
tags:
- Business Applications
- Cloud
- CRM
- Enterprise
- ERP
- Microsoft
- Microsoft Dynamics 365
website: https://www.microsoft.com/
---
