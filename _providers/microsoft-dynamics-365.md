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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Microsoft Dynamics 365 Agentic Access
  operation_count: 15
  slug: microsoft-dynamics-365-agentic-access
  summary_line: 15 operations · 9 acting
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
artifact_total: 40
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-dynamics-365-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-dynamics-365/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-dynamics-365-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-dynamics-365-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-dynamics-365-authentication.yml
- group: auth
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
json_structures:
- name: Microsoft Dynamics 365 Structure
  property_count: 0
  slug: microsoft-dynamics-365-structure
jsonld:
- class_count: 0
  name: Microsoft Dynamics 365 Context
  property_count: 3
  slug: microsoft-dynamics-365-context
layout: provider
modified: '2026-05-19'
name: Microsoft Dynamics 365
nav: Providers
network: true
overview: 'Microsoft Dynamics 365 publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts API, Contacts API, and Opportunities API. Tagged areas include Business Applications, Cloud, CRM, Enterprise, and ERP.


  The Microsoft Dynamics 365 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Dynamics 365''s developer surface includes authentication, developer portal, support, engineering blog, and 17 more developer resources.'
plans:
- name: Microsoft Dynamics 365 Plans Pricing
  plan_count: 19
  slug: microsoft-dynamics-365-plans-pricing
random_paper: 7
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
  composite: 47.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 66.4
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
website: https://portal.azure.com/
---
