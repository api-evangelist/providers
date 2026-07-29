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
  score: 28.4
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: API for managing general ledger operations including journals, budgets, and financial reporting.
  name: Oracle General Ledger API
  slug: oracle-general-ledger-api
- description: API for managing supplier invoices, payments, and payables operations.
  name: Oracle Accounts Payable API
  slug: oracle-accounts-payable-api
- description: API for managing customer invoices, receipts, and receivables operations.
  name: Oracle Accounts Receivable API
  slug: oracle-accounts-receivable-api
- description: API for managing bank accounts, cash positions, and treasury operations.
  name: Oracle Cash Management API
  slug: oracle-cash-management-api
- description: API for managing fixed assets, depreciation, and asset lifecycle.
  name: Oracle Fixed Assets API
  slug: oracle-fixed-assets-api
- description: API for managing purchase orders, requisitions, and procurement operations.
  name: Oracle Purchasing API
  slug: oracle-purchasing-api
- description: API for managing employee expenses, expense reports, and reimbursements.
  name: Oracle Expenses API
  slug: oracle-expenses-api
- description: API for managing projects, project costs, and project billing.
  name: Oracle Projects API
  slug: oracle-projects-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-financials-12-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: start
  title: ''
  type: Portal
  url: https://support.oracle.com
- group: auth
  title: ''
  type: Authentication
  url: https://docs.oracle.com/en/cloud/saas/financials/r13-update17d/fafrs/authentication.html
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.oracle.com/en/cloud/saas/financials/r13-update17d/fafrs/rate-limits.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.oracle.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
created: '2024-01-15'
description: Collection of REST APIs for Oracle E-Business Suite Financials Release 12.
finops:
- name: Oracle Financials 12 Finops
  service_category: API
  slug: oracle-financials-12-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-financials-12.png
layout: provider
modified: '2026-04-28'
name: Oracle Financials 12
nav: Providers
network: true
overview: 'Oracle Financials 12 publishes 3 APIs on the [APIs.io](https://apis.io/) network: Oracle General Ledger API, Oracle Accounts Payable API, and Oracle Accounts Receivable API. Tagged areas include Accounting, E-Business Suite, Enterprise, ERP, and Financial Management.


  Oracle Financials 12''s developer surface includes developer portal, authentication, and 6 more developer resources.'
plans:
- name: Oracle Financials 12 Plans Pricing
  plan_count: 3
  slug: oracle-financials-12-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Oracle Financials 12 Rate Limits
  slug: oracle-financials-12-rate-limits
score:
  band: thin
  composite: 35.6
  delta: -2.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.3
    developer_ergonomics: 19.6
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 38.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-financials-12/refs/heads/main/screenshots/oracle-financials-12-2026-06-20T191134.png
security:
- kind: domain-security
  name: Oracle Financials 12 Domain Security
  slug: oracle-financials-12-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-financials-12
tags:
- Accounting
- E-Business Suite
- Enterprise
- ERP
- Financial Management
- Oracle
- Release 12
website: https://support.oracle.com
---
