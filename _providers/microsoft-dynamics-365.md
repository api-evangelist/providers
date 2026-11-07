---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Microsoft Dynamics 365 Agentic Access
  operation_count: 58
  slug: microsoft-dynamics-365-agentic-access
  summary_line: 58 operations · 29 acting
api_count: 17
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
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Activities API from Microsoft Dynamics 365 — 1 operation(s) for activities.
  name: Microsoft Dynamics 365 Activities API
  slug: microsoft-dynamics-365-activities-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Cases API from Microsoft Dynamics 365 — 1 operation(s) for cases.
  name: Microsoft Dynamics 365 Cases API
  slug: microsoft-dynamics-365-cases-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Companies API from Microsoft Dynamics 365 — 1 operation(s) for companies.
  name: Microsoft Dynamics 365 Companies API
  slug: microsoft-dynamics-365-companies-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Customers API from Microsoft Dynamics 365 — 3 operation(s) for customers.
  name: Microsoft Dynamics 365 Customers API
  slug: microsoft-dynamics-365-customers-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Employees API from Microsoft Dynamics 365 — 1 operation(s) for employees.
  name: Microsoft Dynamics 365 Employees API
  slug: microsoft-dynamics-365-employees-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The General Ledger API from Microsoft Dynamics 365 — 2 operation(s) for general ledger.
  name: Microsoft Dynamics 365 General Ledger API
  slug: microsoft-dynamics-365-general-ledger-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Human Resources API from Microsoft Dynamics 365 — 1 operation(s) for human resources.
  name: Microsoft Dynamics 365 Human Resources API
  slug: microsoft-dynamics-365-human-resources-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Items API from Microsoft Dynamics 365 — 1 operation(s) for items.
  name: Microsoft Dynamics 365 Items API
  slug: microsoft-dynamics-365-items-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Journals API from Microsoft Dynamics 365 — 1 operation(s) for journals.
  name: Microsoft Dynamics 365 Journals API
  slug: microsoft-dynamics-365-journals-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Leads API from Microsoft Dynamics 365 — 2 operation(s) for leads.
  name: Microsoft Dynamics 365 Leads API
  slug: microsoft-dynamics-365-leads-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Products API from Microsoft Dynamics 365 — 1 operation(s) for products.
  name: Microsoft Dynamics 365 Products API
  slug: microsoft-dynamics-365-products-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Purchase Invoices API from Microsoft Dynamics 365 — 1 operation(s) for purchase invoices.
  name: Microsoft Dynamics 365 Purchase Invoices API
  slug: microsoft-dynamics-365-purchase-invoices-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Purchase Orders API from Microsoft Dynamics 365 — 2 operation(s) for purchase orders.
  name: Microsoft Dynamics 365 Purchase Orders API
  slug: microsoft-dynamics-365-purchase-orders-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Sales Invoices API from Microsoft Dynamics 365 — 1 operation(s) for sales invoices.
  name: Microsoft Dynamics 365 Sales Invoices API
  slug: microsoft-dynamics-365-sales-invoices-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Sales Orders API from Microsoft Dynamics 365 — 2 operation(s) for sales orders.
  name: Microsoft Dynamics 365 Sales Orders API
  slug: microsoft-dynamics-365-sales-orders-api
- baseURL: https://[org].operations.dynamics.com/data
  baseurl_source: declared
  description: The Vendors API from Microsoft Dynamics 365 — 2 operation(s) for vendors.
  name: Microsoft Dynamics 365 Vendors API
  slug: microsoft-dynamics-365-vendors-api
artifact_total: 71
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
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365/rules/microsoft-dynamics-365-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-dynamics-365-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365/rules/microsoft-dynamics-365-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-dynamics-365-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365/vocabulary/microsoft-dynamics-365-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-dynamics-365-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365/data-model/microsoft-dynamics-365-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-dynamics-365-data-model.yml
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365/cli/microsoft-dynamics-365-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-dynamics-365-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365/conventions/microsoft-dynamics-365-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-dynamics-365-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365/errors/microsoft-dynamics-365-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-dynamics-365-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365/conformance/microsoft-dynamics-365-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-dynamics-365-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365/llms/microsoft-dynamics-365-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-dynamics-365-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365/mcp/microsoft-dynamics-365-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-dynamics-365-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365/mcp/microsoft-dynamics-365-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-dynamics-365-mcp.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365/well-known/microsoft-dynamics-365-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-dynamics-365-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365/well-known/microsoft-dynamics-365-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-dynamics-365-well-known.yml
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365/integrations/microsoft-dynamics-365-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-dynamics-365-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365/packages/microsoft-dynamics-365-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-dynamics-365-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365/packages/microsoft-dynamics-365-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-dynamics-365-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/dynamics365/get-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dynamics.com/
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365/security/microsoft-dynamics-365-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-dynamics-365-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365/security/microsoft-dynamics-365-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-dynamics-365-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-dynamics-365/plans/microsoft-dynamics-365-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-dynamics-365-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-dynamics-365/rate-limits/microsoft-dynamics-365-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-dynamics-365-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-dynamics-365/finops/microsoft-dynamics-365-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-dynamics-365-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: other
  href: https://artifacts.apis.io/microsoft-dynamics-365/capabilities/microsoft-dynamics-365-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-dynamics-365-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-dynamics-365/overview
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365/agentic-access/microsoft-dynamics-365-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-dynamics-365-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365/security/microsoft-dynamics-365-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-dynamics-365-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365/authentication/microsoft-dynamics-365-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-dynamics-365-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365/scopes/microsoft-dynamics-365-scopes.yml
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
- has_sources: true
  method: generated
  name: Microsoft Dynamics 365 Finops
  primary_unit: user-month
  service_category: Business Applications / CRM-ERP
  slug: microsoft-dynamics-365-finops
  template: false
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
  property_count: 1
  slug: microsoft-dynamics-365-accountcreate
- name: AccountUpdate
  property_count: 42
  slug: microsoft-dynamics-365-accountupdate
- name: Contact
  property_count: 76
  slug: microsoft-dynamics-365-contact
- name: ContactCreate
  property_count: 1
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
  property_count: 1
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
mcp_servers:
- description: Microsoft Dataverse (the data platform under Dynamics 365 customer engagement apps) acts as a remote MCP server per Power Platform environment, once an admin enables it and its allowed clients.
  name: Dataverse MCP server
  slug: dataverse-mcp-server
modified: '2026-05-19'
name: Microsoft Dynamics 365
nav: Providers
network: true
overview: 'Microsoft Dynamics 365 publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Contacts API, Opportunities API, and 25 more. Tagged areas include Business Applications, Cloud, CRM, Enterprise, and ERP.


  The Microsoft Dynamics 365 catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Microsoft Dynamics 365''s developer surface includes CLI, changelog, getting-started guide, documentation, authentication, developer portal, support, and 42 more developer resources.'
plans:
- name: Microsoft Dynamics 365 Plans Pricing
  plan_count: 19
  slug: microsoft-dynamics-365-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 3
  name: Microsoft Dynamics 365 Rate Limits
  slug: microsoft-dynamics-365-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Microsoft Dynamics 365 — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-dynamics-365-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Microsoft Dynamics 365 API Rules
  rule_count: 65
  severity_counts:
    error: 60
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-dynamics-365-rules
scopes:
- name: Microsoft Dynamics 365 Scopes
  scope_count: 1
  slug: microsoft-dynamics-365-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 63.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 80.8
    catalog_earned_first_party: 12.0
    catalog_gap: 34.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 14.5
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 66.6
    developer_ergonomics: 62.5
    discoverability: 78.3
    operational_transparency: 76.3
  previous_composite: 49.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-dynamics-365/microsoft-dynamics-365-2026-06-20T185452.png
security:
- kind: authentication
  name: Microsoft Dynamics 365 Authentication
  slug: microsoft-dynamics-365-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Dynamics 365 Domain Security
  slug: microsoft-dynamics-365-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Dynamics 365 Vulnerability Disclosure
  slug: microsoft-dynamics-365-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Dynamics 365 Trust Center
  slug: microsoft-dynamics-365-trust-center
  summary_line: GDPR
skill_count: 1
skills:
- name: manage-accounts
  slug: microsoft-dynamics-365-manage-accounts
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
