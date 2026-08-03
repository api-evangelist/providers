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
api_count: 2
apis:
- description: REST Web Services API for creating, reading, updating, and deleting NetSuite records such as customers, vendors, sales orders, invoices, items, and journal entries. Authentication uses OAuth 2.0 (auth
  name: Oracle NetSuite SuiteTalk REST Record API
  slug: suitetalk-rest-record-api
- description: REST endpoint for executing SuiteQL (SQL-like) queries against NetSuite records and transactions for reporting and integration use cases. Returns paginated JSON results and uses the same OAuth 2.0 flo
  name: Oracle NetSuite SuiteQL Query API
  slug: suiteql-query-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-netsuite-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netsuite
- group: company
  title: ''
  type: Website
  url: https://www.netsuite.com
- group: other
  title: ''
  type: Oracle NetSuite Site
  url: https://www.oracle.com/netsuite/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/cloud/saas/netsuite/index.html
- group: docs
  title: ''
  type: SuiteTalk Guide
  url: https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/book_1559132836.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.netsuite.com/portal/products/erp/pricing.shtml
- group: start
  title: ''
  type: Signup
  url: https://www.netsuite.com/portal/forms/contact-netsuite.shtml
- group: start
  title: ''
  type: Login
  url: https://system.netsuite.com/pages/customerlogin.jsp
- group: operate
  title: ''
  type: Support
  url: https://www.netsuite.com/portal/services/customer-support.shtml
- group: other
  title: ''
  type: SuiteAnswers
  url: https://netsuite.custhelp.com
- group: other
  title: ''
  type: Developer Resources
  url: https://www.netsuite.com/portal/developers.shtml
created: '2026-05-11'
description: Oracle NetSuite is a cloud-based ERP suite covering financials, accounting, order management, inventory, CRM, ecommerce, HR, and professional services automation for businesses of all sizes worldwide. As Oracle's flagship SaaS ERP, NetSuite powers core back-office operations and global subsidiaries. Oracle NetSuite exposes its SuiteTalk REST Web Services API for record access and SuiteQL queries, secured via OAuth 2.0 issued by each customer account-specific suitetalk.api.netsuite.com endpoint.
graphqls:
- description: This conceptual GraphQL schema represents the Oracle NetSuite ERP platform, covering financials, accounting, order management, inventory, CRM, HR, and professional services automation. The schema is d
  name: Oracle NetSuite GraphQL Schema
  slug: oracle-netsuite-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-netsuite.png
layout: provider
modified: '2026-05-11'
name: Oracle NetSuite
nav: Providers
network: true
overview: 'Oracle NetSuite publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include ERP, Financials, Accounting, CRM, and Inventory.


  Oracle NetSuite''s developer surface includes documentation, pricing, signup flow, support, and 9 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 26.9
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 48.1
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.9
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-netsuite/refs/heads/main/screenshots/oracle-netsuite-2026-06-20T191136.png
security:
- kind: domain-security
  name: Oracle Netsuite Domain Security
  slug: oracle-netsuite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: oracle-netsuite
tags:
- ERP
- Financials
- Accounting
- CRM
- Inventory
- SaaS
- Oracle
website: https://www.netsuite.com
---
