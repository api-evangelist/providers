---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Oracle Financials Agentic Access
  operation_count: 32
  slug: oracle-financials-agentic-access
  summary_line: 32 operations · 11 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: Manage budget transactions and view budgetary control validation results
  name: Oracle Financials Budgetary Control API
  slug: oracle-financials-budgetary-control-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: Create and manage chart of accounts filters and filter criteria
  name: Oracle Financials Chart of Accounts API
  slug: oracle-financials-chart-of-accounts-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: Retrieve currency conversion rates used for multi-currency accounting
  name: Oracle Financials Currency Rates API
  slug: oracle-financials-currency-rates-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: Manage journal batches including headers, lines, action logs, and attachments
  name: Oracle Financials Journal Batches API
  slug: oracle-financials-journal-batches-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: View balance amounts for account combinations or accounts defined as part of an account group
  name: Oracle Financials Ledger Balances API
  slug: oracle-financials-ledger-balances-api
- description: APIs for managing supplier invoices, payments, expense reports, and procurement transactions.
  name: Oracle Accounts Payable REST API
  slug: accounts-payable
- description: APIs for managing customer invoices, receipts, credit memos, and revenue recognition.
  name: Oracle Accounts Receivable REST API
  slug: accounts-receivable
- description: REST APIs for Oracle Enterprise Performance Management Cloud including Planning, Financial Consolidation and Close, Tax Reporting, and Account Reconciliation.
  name: Oracle EPM Cloud REST API
  slug: epm-cloud
- description: APIs for creating, managing, and executing financial reports, including Smart View integration.
  name: Oracle Financial Reporting REST API
  slug: reporting
- description: APIs for Financial Consolidation and Close Cloud Service for consolidations, eliminations, currency translation, and intercompany management.
  name: Oracle FCCS REST API
  slug: fccs
- description: APIs for Account Reconciliation Cloud Service for managing reconciliations, certifications, and compliance workflows.
  name: Oracle ARCS REST API
  slug: arcs
- description: APIs for Planning and Budgeting Cloud Service including data management, business rules, and planning operations.
  name: Oracle Planning REST API
  slug: planning
- baseURL_template: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: spec_template
  description: Bank accounts and statements.
  name: Oracle Financials Cash Management API
  slug: oracle-financial-applications-cash-management-api
- baseURL_template: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: spec_template
  description: Asset lifecycle resources.
  name: Oracle Financials Fixed Assets API
  slug: oracle-financial-applications-fixed-assets-api
- baseURL_template: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: spec_template
  description: General Ledger journal batches and currency rates.
  name: Oracle Financials General Ledger API
  slug: oracle-financial-applications-general-ledger-api
- baseURL_template: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: spec_template
  description: Accounts Payable invoices.
  name: Oracle Financials Payables API
  slug: oracle-financial-applications-payables-api
- baseURL_template: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: spec_template
  description: Customer transactions.
  name: Oracle Financials Receivables API
  slug: oracle-financial-applications-receivables-api
- description: REST API for viewing accounting period statuses in Oracle Fusion Cloud General Ledger. The accounting period status list of values resource provides period details in a calendar, including ledger iden
  name: Oracle Financials Accounting Period Status REST API
  slug: accounting-period-status
- description: REST API for managing chart of accounts filter configurations in Oracle Fusion Cloud General Ledger. The chart of accounts filters resource returns filter ID values for chart of accounts filter criter
  name: Oracle Financials Chart of Accounts Filters REST API
  slug: chart-of-accounts-filters
- description: REST API for managing intercompany transactions in Oracle Fusion Cloud Financials. The intercompany resources support agreement-based intercompany transactions, intercompany transaction source documen
  name: Oracle Intercompany Transactions REST API
  slug: intercompany-transactions
- description: REST API for managing joint venture general ledger transactions in Oracle Fusion Cloud Financials. The joint venture GL transactions and joint venture subledger transactions resources enable viewing a
  name: Oracle Joint Venture General Ledger Transactions REST API
  slug: joint-venture-transactions
- baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The Accounting Periods API from Oracle General Ledger — 1 operation(s) for accounting periods.
  name: Oracle Financials Accounting Periods API
  slug: oracle-general-ledger-accounting-periods-api
- baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The Budgetary Control API from Oracle General Ledger — 1 operation(s) for budgetary control.
  name: Oracle Financials Budgetary Control API
  slug: oracle-general-ledger-budgetary-control-api
- baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The ERP Integrations API from Oracle General Ledger — 1 operation(s) for erp integrations.
  name: Oracle Financials ERP Integrations API
  slug: oracle-general-ledger-erp-integrations-api
- baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The Intercompany API from Oracle General Ledger — 1 operation(s) for intercompany.
  name: Oracle Financials Intercompany API
  slug: oracle-general-ledger-intercompany-api
- baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The Journal Batches API from Oracle General Ledger — 2 operation(s) for journal batches.
  name: Oracle Financials Journal Batches API
  slug: oracle-general-ledger-journal-batches-api
- baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The Ledger Balances API from Oracle General Ledger — 1 operation(s) for ledger balances.
  name: Oracle Financials Balances API
  slug: oracle-general-ledger-ledger-balances-api
- baseURL: https://{instance}.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The Ledger Options API from Oracle General Ledger — 1 operation(s) for ledger options.
  name: Oracle Financials Options API
  slug: oracle-general-ledger-ledger-options-api
- description: API for managing purchase orders, requisitions, and procurement operations.
  name: Oracle Purchasing API
  slug: purchasing
- description: API for managing employee expenses, expense reports, and reimbursements.
  name: Oracle Expenses API
  slug: expenses
- description: API for managing projects, project costs, and project billing.
  name: Oracle Projects API
  slug: projects
artifact_total: 53
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Financials General Ledger Budgetary Control API
  slug: open-oracle-financials-budgetary-control-api
- collection_type: open
  name: Oracle Financials General Ledger Budgetary Control Chart of Accounts API
  slug: open-oracle-financials-chart-of-accounts-api
- collection_type: open
  name: Oracle Financials General Ledger Budgetary Control Currency Rates API
  slug: open-oracle-financials-currency-rates-api
- collection_type: open
  name: Oracle Financials General Ledger API
  slug: open-oracle-financials-general-ledger
- collection_type: open
  name: Oracle Financials General Ledger Budgetary Control Journal Batches API
  slug: open-oracle-financials-journal-batches-api
- collection_type: open
  name: Oracle Financials General Ledger Budgetary Control Ledger Balances API
  slug: open-oracle-financials-ledger-balances-api
common:
- group: company
  title: ''
  type: Website
  url: https://oracle.com
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oracle-financials/refs/heads/main/capabilities/oracle-financials-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-financials-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/oracle-financials/refs/heads/main/agentic-access/oracle-financials-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-financials-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oracle-financials/refs/heads/main/security/oracle-financials-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oracle-financials-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oracle-financials/refs/heads/main/authentication/oracle-financials-authentication.yml
  title: ''
  type: Authentication
  url: authentication/oracle-financials-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/getting-started.html
- group: docs
  title: ''
  type: Authentication Guide
  url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/Authentication.html
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.oracle.com/en/cloud/saas/financials/23r3/farfa/rate-limits.html
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/corporate/contracts/cloud-services/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
created: '2024-01-15'
description: Collection of Oracle Financials Cloud APIs for financial management, accounting, and reporting.
finops:
- name: Oracle Financials Finops
  service_category: ERP / Financials
  slug: oracle-financials-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-financials.png
json_schemas:
- name: BudgetaryControlResult
  property_count: 5
  slug: oracle-financials-budgetarycontrolresult
- name: BudgetTransaction
  property_count: 6
  slug: oracle-financials-budgettransaction
- name: ChartOfAccountsFilter
  property_count: 4
  slug: oracle-financials-chartofaccountsfilter
- name: CurrencyRate
  property_count: 5
  slug: oracle-financials-currencyrate
- name: JournalBatch
  property_count: 13
  slug: oracle-financials-journalbatch
- name: JournalBatchUpdate
  property_count: 3
  slug: oracle-financials-journalbatchupdate
- name: LedgerBalance
  property_count: 10
  slug: oracle-financials-ledgerbalance
json_structures:
- name: Oracle Financials Structure
  property_count: 0
  slug: oracle-financials-structure
layout: provider
modified: '2026-09-16'
name: Oracle Financials
nav: Providers
network: true
overview: 'Oracle Financials publishes 31 APIs on the [APIs.io](https://apis.io/) network, including Budgetary Control API, Chart of Accounts API, Currency Rates API, and 28 more. Tagged areas include Accounting, Accounts Payable, Accounts Receivable, Cash Management, and ERP.


  The Oracle Financials catalog on APIs.io includes 1 Spectral governance ruleset.


  Oracle Financials'' developer surface includes authentication, getting-started guide, support, and 10 more developer resources.'
plans:
- name: Oracle Financials Plans Pricing
  plan_count: 2
  slug: oracle-financials-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Oracle Financials Rate Limits
  slug: oracle-financials-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Oracle Financials API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: oracle-financials-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 33.3
    catalog_earned_first_party: 0.0
    catalog_gap: 81.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 49.2
    developer_ergonomics: 52.4
    discoverability: 39.3
    operational_transparency: 42.1
  previous_composite: 41.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-financials/refs/heads/main/screenshots/oracle-financials-2026-06-20T191131.png
security:
- kind: authentication
  name: Oracle Financials Authentication
  slug: oracle-financials-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Oracle Financials Domain Security
  slug: oracle-financials-domain-security
  summary_line: TLSv1.3 · DMARC
slug: oracle-financials
tags:
- Accounting
- Accounts Payable
- Accounts Receivable
- Cash Management
- ERP
- Expense Management
- Financial Management
- General Ledger
website: https://oracle.com
---
