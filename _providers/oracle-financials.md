---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Oracle Financials Agentic Access
  operation_count: 32
  slug: oracle-financials-agentic-access
  summary_line: 32 operations · 11 acting · 1 human-in-the-loop
api_count: 13
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
- description: API for managing purchase orders, requisitions, and procurement operations.
  name: Oracle Purchasing API
  slug: purchasing
- description: API for managing employee expenses, expense reports, and reimbursements.
  name: Oracle Expenses API
  slug: expenses
- description: API for managing projects, project costs, and project billing.
  name: Oracle Projects API
  slug: projects
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The Accounting Periods API from Oracle Financials — 1 operation(s) for accounting periods.
  name: Oracle Financials Accounting Periods API
  slug: oracle-financials-accounting-periods-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: Bank accounts and statements.
  name: Oracle Financials Cash Management API
  slug: oracle-financials-cash-management-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The ERP Integrations API from Oracle Financials — 1 operation(s) for erp integrations.
  name: Oracle Financials ERP Integrations API
  slug: oracle-financials-erp-integrations-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: Asset lifecycle resources.
  name: Oracle Financials Fixed Assets API
  slug: oracle-financials-fixed-assets-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: General Ledger journal batches and currency rates.
  name: Oracle Financials General Ledger API
  slug: oracle-financials-general-ledger-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The Intercompany API from Oracle Financials — 1 operation(s) for intercompany.
  name: Oracle Financials Intercompany API
  slug: oracle-financials-intercompany-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: The Ledger Options API from Oracle Financials — 1 operation(s) for ledger options.
  name: Oracle Financials Ledger Options API
  slug: oracle-financials-ledger-options-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: Accounts Payable invoices.
  name: Oracle Financials Payables API
  slug: oracle-financials-payables-api
- baseURL: https://your-instance.fa.us2.oraclecloud.com/fscmRestApi/resources/11.13.18.05
  baseurl_source: declared
  description: Customer transactions.
  name: Oracle Financials Receivables API
  slug: oracle-financials-receivables-api
artifact_total: 49
collections:
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
- group: commercial
  href: https://artifacts.apis.io/oracle-financials/plans/oracle-financials-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/oracle-financials-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/oracle-financials/finops/oracle-financials-finops.yml
  title: ''
  type: FinOps
  url: finops/oracle-financials-finops.yml
- group: company
  title: ''
  type: Website
  url: https://oracle.com
- group: other
  href: https://artifacts.apis.io/oracle-financials/capabilities/oracle-financials-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-financials-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/oracle-financials/agentic-access/oracle-financials-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-financials-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/oracle-financials/security/oracle-financials-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oracle-financials-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/oracle-financials/authentication/oracle-financials-authentication.yml
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
- has_sources: true
  method: generated
  name: Oracle Financials Finops
  primary_unit: ''
  service_category: ERP / Financials
  slug: oracle-financials-finops
  template: false
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
overview: 'Oracle Financials publishes 28 API contracts indexed on the [APIs.io](https://apis.io/) network, including Budgetary Control API, Chart of Accounts API, Currency Rates API, and 25 more. Tagged areas include Accounting, Accounts Payable, Accounts Receivable, Cash Management, and ERP.


  The Oracle Financials catalog on APIs.io includes 1 Spectral governance ruleset.


  Oracle Financials'' developer surface includes authentication, getting-started guide, support, and 12 more developer resources.'
plans:
- name: Oracle Financials Plans Pricing
  plan_count: 2
  slug: oracle-financials-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Oracle Financials Rate Limits
  slug: oracle-financials-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Oracle Financials — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: oracle-financials-jsonschema-spectral-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 33.3
    catalog_earned_first_party: 0.0
    catalog_gap: 81.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 51.5
    developer_ergonomics: 52.4
    discoverability: 44.6
    operational_transparency: 42.1
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/oracle-financials/oracle-financials-2026-06-20T191131.png
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
