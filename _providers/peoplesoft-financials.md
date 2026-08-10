---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-10'
api_count: 8
apis:
- description: REST API for managing general ledger operations including journals, chartfields, budgets, and financial reporting.
  name: PeopleSoft General Ledger API
  slug: general-ledger
- description: REST API for vendor management, invoice processing, payments, and AP reporting.
  name: PeopleSoft Accounts Payable API
  slug: accounts-payable
- description: REST API for customer management, billing, receipts, and AR reporting.
  name: PeopleSoft Accounts Receivable API
  slug: accounts-receivable
- description: REST API for fixed asset tracking, depreciation, transfers, and asset reporting.
  name: PeopleSoft Asset Management API
  slug: asset-management
- description: REST API for purchase requisitions, purchase orders, receiving, and procurement reporting.
  name: PeopleSoft Purchasing API
  slug: purchasing
- description: REST API for expense reporting, reimbursements, and travel management.
  name: PeopleSoft Expenses API
  slug: expenses
- description: REST API for project costing, billing, resource management, and project reporting.
  name: PeopleSoft Projects API
  slug: projects
- description: REST API for executing PeopleSoft queries and retrieving data from various financial modules.
  name: PeopleSoft Query API
  slug: query
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peoplesoft-financials-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peoplesoft-inc
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/cd/E92519_02/pt856pbr3/eng/pt/tprs/index.html
- group: start
  title: ''
  type: Portal
  url: https://www.oracle.com/applications/peoplesoft/
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
created: '2024-01-01'
description: API collection for Oracle PeopleSoft Financials suite covering General Ledger, Accounts Payable, Accounts Receivable, Asset Management, and other financial modules.
finops:
- name: Peoplesoft Financials Finops
  service_category: API
  slug: peoplesoft-financials-finops
image: https://www.oracle.com/a/ocom/img/logo-peoplesoft.svg
layout: provider
modified: '2026-04-28'
name: PeopleSoft Financials
nav: Providers
network: true
overview: 'PeopleSoft Financials publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise, ERP, Financials, Oracle, and PeopleSoft.


  PeopleSoft Financials'' developer surface includes authentication, developer portal, support, and 4 more developer resources.'
plans:
- name: Peoplesoft Financials Plans Pricing
  plan_count: 3
  slug: peoplesoft-financials-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 5
  name: Peoplesoft Financials Rate Limits
  slug: peoplesoft-financials-rate-limits
score:
  band: emerging
  composite: 27.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peoplesoft-financials/refs/heads/main/screenshots/peoplesoft-financials-2026-06-20T191554.png
security:
- kind: domain-security
  name: Peoplesoft Financials Domain Security
  slug: peoplesoft-financials-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peoplesoft-financials
tags:
- Enterprise
- ERP
- Financials
- Oracle
- PeopleSoft
website: https://www.oracle.com/applications/peoplesoft/
---
