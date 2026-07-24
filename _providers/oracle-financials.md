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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Oracle Financials Agentic Access
  operation_count: 9
  slug: oracle-financials-agentic-access
  summary_line: 9 operations · 4 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: Manage budget transactions and view budgetary control validation results
  name: Oracle Financials Budgetary Control API
  slug: oracle-financials-budgetary-control-api
- description: Create and manage chart of accounts filters and filter criteria
  name: Oracle Financials Chart of Accounts API
  slug: oracle-financials-chart-of-accounts-api
- description: Retrieve currency conversion rates used for multi-currency accounting
  name: Oracle Financials Currency Rates API
  slug: oracle-financials-currency-rates-api
- description: Manage journal batches including headers, lines, action logs, and attachments
  name: Oracle Financials Journal Batches API
  slug: oracle-financials-journal-batches-api
- description: View balance amounts for account combinations or accounts defined as part of an account group
  name: Oracle Financials Ledger Balances API
  slug: oracle-financials-ledger-balances-api
artifact_total: 21
collections:
- collection_type: open
  name: Oracle Financials General Ledger API
  slug: open-oracle-financials-general-ledger
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-financials-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-financials-domain-security.yml
- group: auth
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
modified: '2026-05-19'
name: Oracle Financials
nav: Providers
network: true
overview: 'Oracle Financials publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Budgetary Control API, Chart of Accounts API, Currency Rates API, and 2 more. Tagged areas include Accounting, Accounts Payable, Accounts Receivable, Cash Management, and ERP.


  The Oracle Financials catalog on APIs.io includes 1 Spectral governance ruleset.


  Oracle Financials'' developer surface includes authentication, getting-started guide, support, and 8 more developer resources.'
plans:
- name: Oracle Financials Plans Pricing
  plan_count: 2
  slug: oracle-financials-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 3
  name: Oracle Financials Rate Limits
  slug: oracle-financials-rate-limits
rules:
- name: Oracle Financials API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: oracle-financials-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 26.1
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 51.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
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
---
