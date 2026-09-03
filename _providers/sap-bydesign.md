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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sap Bydesign Agentic Access
  operation_count: 26
  slug: sap-bydesign-agentic-access
  summary_line: 26 operations · 7 acting
api_count: 1
apis:
- description: OData v2 REST API for UI-driven access to SAP Business ByDesign business objects. Supports querying, reading, creating, updating, deleting, and performing actions on business objects and documents acr
  name: SAP Business ByDesign OData Business Objects API
  slug: odata-business-objects
- description: OData API for accessing pre-processed and formatted analytical data from SAP Business ByDesign reports, KPIs, and data sources. Supports extraction of financial analytics, supply chain KPIs, sales rep
  name: SAP Business ByDesign OData Analytics API
  slug: odata-analytics
- description: SOAP-based web services API for system-to-system integration with SAP Business ByDesign. Provides access to business processes including financials, procurement, supply chain, CRM, and HR through stan
  name: SAP Business ByDesign SOAP Web Services
  slug: soap-web-services
- baseURL: https://{tenant}.bydesign.cloud.sap/sap/byd/odata/v1
  baseurl_source: declared
  description: Access pre-processed analytical data, reports, and KPIs from Business ByDesign data sources.
  name: SAP Business ByDesign Analytics API
  slug: sap-bydesign-analytics-api
- baseURL: https://{tenant}.bydesign.cloud.sap/sap/byd/odata/v1
  baseurl_source: declared
  description: Manage leads, opportunities, and customer relationship data.
  name: SAP Business ByDesign CRM API
  slug: sap-bydesign-crm-api
- baseURL: https://{tenant}.bydesign.cloud.sap/sap/byd/odata/v1
  baseurl_source: declared
  description: Access payments, bank statements, house bank accounts, and financial documents.
  name: SAP Business ByDesign Financials API
  slug: sap-bydesign-financials-api
- baseURL: https://{tenant}.bydesign.cloud.sap/sap/byd/odata/v1
  baseurl_source: declared
  description: Access and manage organizational structures, materials, service products, customers, suppliers, employees, and other master data objects.
  name: SAP Business ByDesign Master Data API
  slug: sap-bydesign-master-data-api
- baseURL: https://{tenant}.bydesign.cloud.sap/sap/byd/odata/v1
  baseurl_source: declared
  description: Access purchase orders, supplier invoices, and procurement-related business objects.
  name: SAP Business ByDesign Procurement API
  slug: sap-bydesign-procurement-api
- baseURL: https://{tenant}.bydesign.cloud.sap/sap/byd/odata/v1
  baseurl_source: declared
  description: Read and manage project data.
  name: SAP Business ByDesign Projects API
  slug: sap-bydesign-projects-api
- baseURL: https://{tenant}.bydesign.cloud.sap/sap/byd/odata/v1
  baseurl_source: declared
  description: Manage sales quotes, sales orders, customer invoices, customer returns, and related sales processes.
  name: SAP Business ByDesign Sales API
  slug: sap-bydesign-sales-api
- baseURL: https://{tenant}.bydesign.cloud.sap/sap/byd/odata/v1
  baseurl_source: declared
  description: Manage inbound and outbound deliveries, goods receipts, goods issues, and production orders.
  name: SAP Business ByDesign Supply Chain API
  slug: sap-bydesign-supply-chain-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAP Business ByDesign OData Analytics API
  slug: open-sap-bydesign-analytics-api
- collection_type: open
  name: SAP Business ByDesign OData Analytics CRM API
  slug: open-sap-bydesign-crm-api
- collection_type: open
  name: SAP Business ByDesign OData Analytics Financials API
  slug: open-sap-bydesign-financials-api
- collection_type: open
  name: SAP Business ByDesign OData Analytics Master Data API
  slug: open-sap-bydesign-master-data-api
- collection_type: open
  name: SAP Business ByDesign OData Analytics Procurement API
  slug: open-sap-bydesign-procurement-api
- collection_type: open
  name: SAP Business ByDesign OData Analytics Projects API
  slug: open-sap-bydesign-projects-api
- collection_type: open
  name: SAP Business ByDesign OData Analytics Sales API
  slug: open-sap-bydesign-sales-api
- collection_type: open
  name: SAP Business ByDesign OData Analytics Supply Chain API
  slug: open-sap-bydesign-supply-chain-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sap/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-bydesign-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-bydesign-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-bydesign-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-bydesign-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-bydesign-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/erp/business-bydesign.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/SAP_BUSINESS_BYDESIGN
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SAP-samples/byd-api-samples
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/sap-business-bydesign/
- group: company
  title: ''
  type: Blog
  url: https://community.sap.com/t5/c-khhcw49343/SAP+Business+ByDesign/pd-p/01200615320800000691
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sap.com/products/erp/business-bydesign/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: other
  title: ''
  type: X
  url: https://x.com/SAP
- group: commercial
  title: ''
  type: Plans
  url: plans/sap-bydesign-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sap-bydesign-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sap-bydesign-finops.yml
created: '2026-06-13'
description: SAP Business ByDesign is a cloud ERP solution for midmarket companies providing OData REST and SOAP web service APIs for managing financials, CRM, procurement, supply chain, project management, and analytics. APIs support full CRUD operations on business objects, analytical data extraction, KPI access, and end-to-end business process automation across lead-to-quote, order-to-cash, and procure-to-pay workflows.
finops:
- name: Sap Bydesign Finops
  service_category: ''
  slug: sap-bydesign-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sap-bydesign.png
jsonld:
- class_count: 0
  name: Sap Bydesign Context
  property_count: 0
  slug: sap-bydesign
layout: provider
modified: '2026-08-21'
name: SAP Business ByDesign
nav: Providers
network: true
overview: 'SAP Business ByDesign publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, CRM API, Financials API, and 5 more. Tagged areas include ERP, Cloud, Mid-Market, Financials, and CRM.


  The SAP Business ByDesign catalog on APIs.io includes 1 JSON-LD context.


  SAP Business ByDesign''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Sap Bydesign Plans Pricing
  plan_count: 4
  slug: sap-bydesign-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Sap Bydesign Rate Limits
  slug: sap-bydesign-rate-limits
scopes:
- name: Sap Bydesign Scopes
  scope_count: 1
  slug: sap-bydesign-scopes
  summary_line: 1 scope · clientCredentials/saml2Bearer
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 46.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 59.4
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 43.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-bydesign/refs/heads/main/screenshots/sap-bydesign-2026-06-20T193421.png
security:
- kind: authentication
  name: Sap Bydesign Authentication
  slug: sap-bydesign-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sap Bydesign Domain Security
  slug: sap-bydesign-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Bydesign Vulnerability Disclosure
  slug: sap-bydesign-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-bydesign
tags:
- ERP
- Cloud
- Mid-Market
- Financials
- CRM
- Procurement
- Supply Chain
- Project Management
- OData
- SOAP
- SAP
website: https://www.sap.com/products/erp/business-bydesign.html
---
