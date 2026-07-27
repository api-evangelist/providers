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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sap Bydesign Agentic Access
  operation_count: 26
  slug: sap-bydesign-agentic-access
  summary_line: 26 operations · 7 acting
api_count: 11
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
- description: Access pre-processed analytical data, reports, and KPIs from Business ByDesign data sources.
  name: SAP Business ByDesign Analytics API
  slug: sap-bydesign-analytics-api
- description: Manage leads, opportunities, and customer relationship data.
  name: SAP Business ByDesign CRM API
  slug: sap-bydesign-crm-api
- description: Access payments, bank statements, house bank accounts, and financial documents.
  name: SAP Business ByDesign Financials API
  slug: sap-bydesign-financials-api
- description: Access and manage organizational structures, materials, service products, customers, suppliers, employees, and other master data objects.
  name: SAP Business ByDesign Master Data API
  slug: sap-bydesign-master-data-api
- description: Access purchase orders, supplier invoices, and procurement-related business objects.
  name: SAP Business ByDesign Procurement API
  slug: sap-bydesign-procurement-api
- description: Read and manage project data.
  name: SAP Business ByDesign Projects API
  slug: sap-bydesign-projects-api
- description: Manage sales quotes, sales orders, customer invoices, customer returns, and related sales processes.
  name: SAP Business ByDesign Sales API
  slug: sap-bydesign-sales-api
- description: Manage inbound and outbound deliveries, goods receipts, goods issues, and production orders.
  name: SAP Business ByDesign Supply Chain API
  slug: sap-bydesign-supply-chain-api
artifact_total: 20
common:
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
modified: '2026-06-13'
name: SAP Business ByDesign
nav: Providers
network: true
overview: 'SAP Business ByDesign publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, CRM API, Financials API, and 5 more. Tagged areas include ERP, Cloud, Midmarket, Financials, and CRM.


  The SAP Business ByDesign catalog on APIs.io includes 1 JSON-LD context.


  SAP Business ByDesign''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Sap Bydesign Plans Pricing
  plan_count: 4
  slug: sap-bydesign-plans-pricing
random_paper: 66
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
  composite: 47.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.7
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 47.1
  schema_version: 0.5
  scored_at: '2026-07-27'
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
- Midmarket
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
