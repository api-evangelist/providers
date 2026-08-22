---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Oracle Financial Applications Agentic Access
  operation_count: 12
  slug: oracle-financial-applications-agentic-access
  summary_line: 12 operations · 3 acting
api_count: 15
apis:
- description: APIs for managing chart of accounts, journal entries, budgets, allocations, and financial reporting in Oracle ERP Cloud.
  name: Oracle General Ledger REST API
  slug: oracle-general-ledger-rest-api
- description: APIs for managing supplier invoices, payments, expense reports, and procurement transactions.
  name: Oracle Accounts Payable REST API
  slug: oracle-accounts-payable-rest-api
- description: APIs for managing customer invoices, receipts, credit memos, and revenue recognition.
  name: Oracle Accounts Receivable REST API
  slug: oracle-accounts-receivable-rest-api
- description: APIs for bank account management, cash positioning, forecasting, and reconciliation.
  name: Oracle Cash Management REST API
  slug: oracle-cash-management-rest-api
- description: APIs for managing asset lifecycle, depreciation, mass additions, and asset tracking.
  name: Oracle Fixed Assets REST API
  slug: oracle-fixed-assets-rest-api
- description: REST APIs for Oracle Enterprise Performance Management Cloud including Planning, Financial Consolidation and Close, Tax Reporting, and Account Reconciliation.
  name: Oracle EPM Cloud REST API
  slug: oracle-epm-cloud-rest-api
- description: APIs for creating, managing, and executing financial reports, including Smart View integration.
  name: Oracle Financial Reporting REST API
  slug: oracle-financial-reporting-rest-api
- description: APIs for Financial Consolidation and Close Cloud Service for consolidations, eliminations, currency translation, and intercompany management.
  name: Oracle FCCS REST API
  slug: oracle-fccs-rest-api
- description: APIs for Account Reconciliation Cloud Service for managing reconciliations, certifications, and compliance workflows.
  name: Oracle ARCS REST API
  slug: oracle-arcs-rest-api
- description: APIs for Planning and Budgeting Cloud Service including data management, business rules, and planning operations.
  name: Oracle Planning REST API
  slug: oracle-planning-rest-api
- description: Bank accounts and statements.
  name: Oracle Financial Applications Cash Management API
  slug: oracle-financial-applications-cash-management-api
- description: Asset lifecycle resources.
  name: Oracle Financial Applications Fixed Assets API
  slug: oracle-financial-applications-fixed-assets-api
- description: General Ledger journal batches and currency rates.
  name: Oracle Financial Applications General Ledger API
  slug: oracle-financial-applications-general-ledger-api
- description: Accounts Payable invoices.
  name: Oracle Financial Applications Payables API
  slug: oracle-financial-applications-payables-api
- description: Customer transactions.
  name: Oracle Financial Applications Receivables API
  slug: oracle-financial-applications-receivables-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Financials Cloud REST Cash Management API
  slug: open-oracle-financial-applications-cash-management-api
- collection_type: open
  name: Oracle Financials Cloud REST Cash Management Fixed Assets API
  slug: open-oracle-financial-applications-fixed-assets-api
- collection_type: open
  name: Oracle Financials Cloud REST Cash Management General Ledger API
  slug: open-oracle-financial-applications-general-ledger-api
- collection_type: open
  name: Oracle Financials Cloud REST Cash Management Payables API
  slug: open-oracle-financial-applications-payables-api
- collection_type: open
  name: Oracle Financials Cloud REST Cash Management Receivables API
  slug: open-oracle-financial-applications-receivables-api
- collection_type: open
  name: Oracle Financials Cloud REST API
  slug: open-oracle-financial-applications
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-financial-applications-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-financial-applications-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-financial-applications-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: start
  title: ''
  type: Portal
  url: https://cloud.oracle.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/saas/financials/get-started.html
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/cloud/price-list.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
- group: learn
  title: ''
  type: Training
  url: https://education.oracle.com/
created: '2024-01-15'
description: Collection of APIs for Oracle's suite of financial management applications including ERP Cloud, EPM Cloud, and related financial services.
finops:
- name: Oracle Financial Applications Finops
  service_category: API
  slug: oracle-financial-applications-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-financial-applications.png
layout: provider
modified: '2026-04-28'
name: Oracle Financial Applications
nav: Providers
network: true
overview: 'Oracle Financial Applications publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cash Management API, Fixed Assets API, General Ledger API, and 2 more. Tagged areas include Accounting, Cloud Applications, Enterprise Performance Management, Enterprise Resource Planning, and EPM.


  Oracle Financial Applications'' developer surface includes authentication, developer portal, getting-started guide, support, pricing, training material, and 6 more developer resources.'
plans:
- name: Oracle Financial Applications Plans Pricing
  plan_count: 3
  slug: oracle-financial-applications-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Oracle Financial Applications Rate Limits
  slug: oracle-financial-applications-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -0.5
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 38.1
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-financial-applications/refs/heads/main/screenshots/oracle-financial-applications-2026-06-20T191129.png
security:
- kind: authentication
  name: Oracle Financial Applications Authentication
  slug: oracle-financial-applications-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Oracle Financial Applications Domain Security
  slug: oracle-financial-applications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-financial-applications
tags:
- Accounting
- Cloud Applications
- Enterprise Performance Management
- Enterprise Resource Planning
- EPM
- ERP
- Financial Management
- Financial Reporting
website: https://cloud.oracle.com/
---
