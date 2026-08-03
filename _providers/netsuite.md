---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 16.2
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: REST-based interface to NetSuite business objects as JSON resources with CRUD operations, SuiteQL high-performance queries, and an OpenAPI 3.0 definition that provides rich object metadata for records
  name: NetSuite SuiteTalk REST Web Services
  slug: suitetalk-rest
- description: Long-standing SOAP-based integration API to NetSuite records and business logic, suitable for bulk operations, custom records, and legacy ERP integration scenarios.
  name: NetSuite SuiteTalk SOAP Web Services
  slug: suitetalk-soap
- description: Framework for exposing custom server-side SuiteScript as REST endpoints hosted in NetSuite, enabling tailored integrations and custom business logic over HTTP.
  name: NetSuite RESTlets
  slug: restlets
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netsuite-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/netsuite
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netsuite
- group: company
  title: ''
  type: Website
  url: https://www.netsuite.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/saas/netsuite/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.netsuite.com/portal/platform/developer/suitecloud-developer-tools.shtml
- group: other
  title: ''
  type: SuiteTalk Platform
  url: https://www.netsuite.com/portal/platform/developer/suitetalk.shtml
- group: start
  title: ''
  type: Signup
  url: https://www.netsuite.com/portal/forms/free-product-tour.shtml
created: '2026-05-11'
description: Oracle NetSuite is a cloud-based business management suite that combines ERP, financials, CRM, inventory, supply chain, ecommerce, and human capital management into a single platform for mid-market and enterprise companies. NetSuite's SuiteCloud platform exposes both REST web services (SuiteTalk REST, with OpenAPI 3.0 metadata, SuiteQL queries, and CRUD on standard and custom records) and SOAP web services (SuiteTalk SOAP), plus the RESTlets framework for exposing custom server-side SuiteScript as REST endpoints.
graphqls:
- description: This conceptual GraphQL schema represents the Oracle NetSuite cloud ERP data model, derived from the SuiteTalk REST Web Services API, REST Record API, SuiteAnalytics Connect, and the SuiteQL query lay
  name: Oracle NetSuite GraphQL Schema
  slug: netsuite-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netsuite.png
layout: provider
modified: '2026-05-11'
name: Oracle NetSuite
nav: Providers
network: true
overview: 'Oracle NetSuite publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, CRM, Financials, Accounting, and Inventory.


  Oracle NetSuite''s developer surface includes documentation, signup flow, and 6 more developer resources.'
random_paper: 26
score:
  band: emerging
  composite: 23.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 48.1
    developer_ergonomics: 17.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netsuite/refs/heads/main/screenshots/netsuite-2026-06-20T190208.png
security:
- kind: domain-security
  name: Netsuite Domain Security
  slug: netsuite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: netsuite
tags:
- ERP
- CRM
- Financials
- Accounting
- Inventory
- Ecommerce
- Business Management
- Cloud ERP
website: https://www.netsuite.com/
---
