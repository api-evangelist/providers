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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Sap Business One Agentic Access
  operation_count: 15
  slug: sap-business-one-agentic-access
  summary_line: 15 operations · 9 acting
api_count: 11
apis:
- description: RESTful OData v4 API for SAP Business One on HANA exposing nearly all business objects (business partners, items, orders, invoices, journal entries, inventory, production) for POST/GET/PATCH/DELETE op
  name: SAP Business One Service Layer API
  slug: service-layer
- description: COM-based Data Interface API for the SQL Server edition of SAP Business One providing programmatic access to business objects, master data, and transactional documents. The companion DI Server exposes
  name: SAP Business One DI API
  slug: di-api
- description: The BusinessPartners API from SAP Business One — 1 operation(s) for businesspartners.
  name: SAP Business One BusinessPartners API
  slug: sap-business-one-businesspartners-api
- description: The BusinessPartners('{CardCode}') API from SAP Business One — 1 operation(s) for businesspartners('{cardcode}').
  name: SAP Business One BusinessPartners('{CardCode}') API
  slug: sap-business-one-businesspartners-cardcode-api
- description: The CompanyService GetCompanyInfo API from SAP Business One — 1 operation(s) for companyservice getcompanyinfo.
  name: SAP Business One CompanyService GetCompanyInfo API
  slug: sap-business-one-companyservice-getcompanyinfo-api
- description: The Invoices API from SAP Business One — 1 operation(s) for invoices.
  name: SAP Business One Invoices API
  slug: sap-business-one-invoices-api
- description: The Items API from SAP Business One — 1 operation(s) for items.
  name: SAP Business One Items API
  slug: sap-business-one-items-api
- description: The Login API from SAP Business One — 1 operation(s) for login.
  name: SAP Business One Login API
  slug: sap-business-one-login-api
- description: The Logout API from SAP Business One — 1 operation(s) for logout.
  name: SAP Business One Logout API
  slug: sap-business-one-logout-api
- description: The Orders API from SAP Business One — 1 operation(s) for orders.
  name: SAP Business One Orders API
  slug: sap-business-one-orders-api
- description: The Orders({DocEntry}) API from SAP Business One — 1 operation(s) for orders({docentry}).
  name: SAP Business One Orders({DocEntry}) API
  slug: sap-business-one-orders-docentry-api
artifact_total: 16
collections:
- collection_type: open
  name: SAP Business One Service Layer API
  slug: open-sap-business-one
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-business-one-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-business-one-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-business-one-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-business-one-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/sap-business-one
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/erp/business-one.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/SAP_BUSINESS_ONE
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sap.com/products/erp/business-one.html
- group: start
  title: ''
  type: Signup
  url: https://www.sap.com/products/erp/business-one/contact.html
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com
- group: other
  title: ''
  type: Developer Resources
  url: https://api.sap.com
- group: build
  title: ''
  type: GitHub Samples
  url: https://github.com/SAP-samples
- group: company
  title: ''
  type: Blog
  url: https://news.sap.com/feed/
created: '2026-05-11'
description: SAP Business One is an affordable, on-premise or cloud ERP solution designed for small and midsize businesses, covering finance and accounting, purchasing, inventory, sales, CRM, production, and analytics in a single integrated application. It exposes programmatic access through the Service Layer, a modern REST/OData v4 API for the SAP HANA edition, alongside the legacy DI API and DI Server for SQL Server deployments. Authentication uses session-based login that returns a B1SESSION cookie used for subsequent OData calls against company databases.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sap-business-one.png
layout: provider
modified: '2026-05-11'
name: SAP Business One
nav: Providers
network: true
overview: 'SAP Business One publishes 9 APIs on the [APIs.io](https://apis.io/) network, including BusinessPartners API, BusinessPartners(''{CardCode}'') API, CompanyService GetCompanyInfo API, and 6 more. Tagged areas include ERP, Enterprise Resource Planning, Accounting, Inventory Management, and CRM.


  SAP Business One''s developer surface includes authentication, documentation, pricing, signup flow, support, engineering blog, and 7 more developer resources.'
random_paper: 73
score:
  band: emerging
  composite: 27.4
  delta: -3.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 50.7
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-business-one/refs/heads/main/screenshots/sap-business-one-2026-06-20T193419.png
security:
- kind: authentication
  name: Sap Business One Authentication
  slug: sap-business-one-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sap Business One Domain Security
  slug: sap-business-one-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Business One Vulnerability Disclosure
  slug: sap-business-one-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-business-one
tags:
- ERP
- Enterprise Resource Planning
- Accounting
- Inventory Management
- CRM
- Small Business
- Midsize Business
- SAP
website: https://www.sap.com/products/erp/business-one.html
---
