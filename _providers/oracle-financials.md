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
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Oracle Financials Agentic Access
  operation_count: 9
  slug: oracle-financials-agentic-access
  summary_line: 9 operations · 4 acting · 1 human-in-the-loop
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
artifact_total: 27
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/oracle-financials-capability-edges.yml
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


  Oracle Financials'' developer surface includes authentication, getting-started guide, support, and 9 more developer resources.'
plans:
- name: Oracle Financials Plans Pricing
  plan_count: 2
  slug: oracle-financials-plans-pricing
random_paper: 1
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
  composite: 39.3
  coverage:
    artifact_dirs: 15
    catalog_gap: 71.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 57.1
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
