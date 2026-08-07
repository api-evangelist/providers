---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bank Of America Agentic Access
  operation_count: 11
  slug: bank-of-america-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 6
apis:
- description: The Accounts API from Bank of America — 2 operation(s) for accounts.
  name: Bank of America Accounts API
  slug: bank-of-america-accounts-api
- description: The Balances API from Bank of America — 1 operation(s) for balances.
  name: Bank of America Balances API
  slug: bank-of-america-balances-api
- description: Banking operations
  name: Bank of America Banking API
  slug: bank-of-america-banking-api
- description: The Payments API from Bank of America — 2 operation(s) for payments.
  name: Bank of America Payments API
  slug: bank-of-america-payments-api
- description: The Statements API from Bank of America — 2 operation(s) for statements.
  name: Bank of America Statements API
  slug: bank-of-america-statements-api
- description: The Transactions API from Bank of America — 1 operation(s) for transactions.
  name: Bank of America Transactions API
  slug: bank-of-america-transactions-api
artifact_total: 80
collections:
- collection_type: open
  name: Bank of America API
  slug: open-bank-of-america-bofa-api
- collection_type: open
  name: Bank of America CashPro API
  slug: open-bank-of-america-cashpro-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-of-america-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-america-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-of-america-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bank-of-america-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bankofamerica
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-of-america
- group: company
  title: ''
  type: Website
  url: https://www.bankofamerica.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bankofamerica.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.bankofamerica.com/
- group: company
  title: ''
  type: Blog
  url: https://newsroom.bankofamerica.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bankofamerica.com/online-banking/digital-banking-agreement.go
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bankofamerica.com/security-center/overview.go
- group: design
  title: ''
  type: SpectralRules
  url: rules/bank-of-america-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bank-of-america-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bank-of-america-context.jsonld
created: '2024-01-01'
description: Bank of America is a multinational investment bank and financial services holding company providing consumer banking, wealth management, corporate banking, and investment banking services worldwide. The CashPro Developer Studio provides REST APIs for corporate treasury clients to automate account management, payments, balance reporting, and statement access, supporting over 350 payment types and integration with TMS and ERP platforms.
examples:
- key_count: 8
  name: Account Example
  slug: account-example
- key_count: 4
  name: Accountlistresponse Example
  slug: accountlistresponse-example
- key_count: 6
  name: Balance Example
  slug: balance-example
- key_count: 2
  name: Balanceresponse Example
  slug: balanceresponse-example
- key_count: 6
  name: Beneficiary Example
  slug: beneficiary-example
- key_count: 4
  name: Errorresponse Example
  slug: errorresponse-example
- key_count: 4
  name: Paymentlistresponse Example
  slug: paymentlistresponse-example
- key_count: 8
  name: Paymentrequest Example
  slug: paymentrequest-example
- key_count: 10
  name: Paymentresponse Example
  slug: paymentresponse-example
- key_count: 9
  name: Statement Example
  slug: statement-example
- key_count: 2
  name: Statementlistresponse Example
  slug: statementlistresponse-example
- key_count: 10
  name: Transaction Example
  slug: transaction-example
- key_count: 4
  name: Transactionlistresponse Example
  slug: transactionlistresponse-example
features:
- description: Programmatic access to CashPro account details and metadata.
  name: Account Management
- description: Real-time ledger, available, and collected balance queries.
  name: Balance Reporting
- description: Paginated transaction history with date range filtering.
  name: Transaction History
- description: Initiate payments across 350+ payment types including ACH, wire, SWIFT, and RTP.
  name: Payment Initiation
- description: Real-time payment status monitoring and cancellation support.
  name: Payment Status Tracking
- description: Programmatic retrieval of monthly account statements.
  name: Statement Access
- description: Client credentials OAuth2 flow for secure API access.
  name: OAuth2 Security
- description: Pre-built connectors for 28+ Treasury Management and ERP platforms.
  name: TMS/ERP Integration
- description: Developer sandbox for testing and accelerated onboarding.
  name: Sandbox Environment
finops:
- name: Bank Of America Finops
  service_category: Corporate Banking / Treasury Services
  slug: bank-of-america-finops
graphqls:
- description: 'This conceptual GraphQL schema models the Bank of America CashPro API platform and broader retail banking services. It covers the full surface area of consumer and corporate banking operations: accoun'
  name: Bank of America GraphQL Schema
  slug: bank-of-america-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-of-america.png
integrations:
- name: SAP
- name: Oracle
- name: Kyriba
- name: Sage Intacct
- name: Microsoft Dynamics
- name: Coupa
- name: Workday
json_schemas:
- name: Account
  property_count: 8
  slug: account
- name: AccountListResponse
  property_count: 4
  slug: accountlistresponse
- name: Balance
  property_count: 6
  slug: balance
- name: BalanceResponse
  property_count: 2
  slug: balanceresponse
- name: Beneficiary
  property_count: 6
  slug: beneficiary
- name: ErrorResponse
  property_count: 4
  slug: errorresponse
- name: PaymentListResponse
  property_count: 4
  slug: paymentlistresponse
- name: PaymentRequest
  property_count: 8
  slug: paymentrequest
- name: PaymentResponse
  property_count: 10
  slug: paymentresponse
- name: Statement
  property_count: 9
  slug: statement
- name: StatementListResponse
  property_count: 2
  slug: statementlistresponse
- name: Transaction
  property_count: 10
  slug: transaction
- name: TransactionListResponse
  property_count: 4
  slug: transactionlistresponse
json_structures:
- name: Account Structure
  property_count: 0
  slug: account-structure
- name: Accountlistresponse Structure
  property_count: 0
  slug: accountlistresponse-structure
- name: Balance Structure
  property_count: 0
  slug: balance-structure
- name: Balanceresponse Structure
  property_count: 0
  slug: balanceresponse-structure
- name: Beneficiary Structure
  property_count: 0
  slug: beneficiary-structure
- name: Errorresponse Structure
  property_count: 0
  slug: errorresponse-structure
- name: Paymentlistresponse Structure
  property_count: 0
  slug: paymentlistresponse-structure
- name: Paymentrequest Structure
  property_count: 0
  slug: paymentrequest-structure
- name: Paymentresponse Structure
  property_count: 0
  slug: paymentresponse-structure
- name: Statement Structure
  property_count: 0
  slug: statement-structure
- name: Statementlistresponse Structure
  property_count: 0
  slug: statementlistresponse-structure
- name: Transaction Structure
  property_count: 0
  slug: transaction-structure
- name: Transactionlistresponse Structure
  property_count: 0
  slug: transactionlistresponse-structure
jsonld:
- class_count: 0
  name: Bank Of America Context
  property_count: 65
  slug: bank-of-america-context
layout: provider
modified: '2026-05-19'
name: Bank of America
nav: Providers
network: true
overview: 'Bank of America publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Balances API, Banking API, and 3 more. Tagged areas include Banking, Corporate Banking, Finance, Payments, and Treasury.


  The Bank of America catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bank of America''s developer surface includes authentication, documentation, signup flow, engineering blog, and 11 more developer resources.'
plans:
- name: Bank Of America Plans Pricing
  plan_count: 1
  slug: bank-of-america-plans-pricing
press:
- date: '2026-05-25'
  title: Bank of America reports AI-driven workforce boost as ...
  url: https://www.bizjournals.com/charlotte/news/2026/01/14/bank-of-america-bac-jobs-ai-technology-labor-work.html
- date: '2026-05-25'
  title: 'Broadcom''s bold AI opportunity: Bank of America resets'
  url: https://www.facebook.com/sacramentobee/posts/broadcoms-bold-ai-opportunity-bank-of-america-resets-expectations/1386850996819716/
- date: '2026-05-25'
  title: Bank Of America Bets Big On AI With $4 Billion Investment ...
  url: https://www.benzinga.com/tech/25/04/44878856/bank-of-america-bets-big-on-ai-with-4-billion-investment-and-its-already-paying-off
- date: '2026-05-25'
  title: Bank of America AI CashPro Forecasting saves ...
  url: https://www.stocktitan.net/news/BAC/bof-a-s-ai-solution-cash-pro-forecasting-tm-helps-clients-navigate-xglvcv7x13mx.html
- date: '2026-05-25'
  title: Bank of America's Moynihan Says AI's Economic Benefit Is ' ...
  url: https://www.bloomberg.com/news/articles/2025-12-22/bofa-s-moynihan-says-ai-s-economic-benefit-is-kicking-in-more
random_paper: 81
rate_limits:
- limit_count: 1
  name: Bank Of America Rate Limits
  slug: bank-of-america-rate-limits
rules:
- name: Bank of America API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bank-of-america-jsonschema-spectral-rules
- name: Bank of America API Rules
  rule_count: 24
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 13
  slug: bank-of-america-spectral-rules
scopes:
- name: Bank Of America Scopes
  scope_count: 4
  slug: bank-of-america-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 52.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 52.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 58.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-america/refs/heads/main/screenshots/bank-of-america-2026-06-20T172951.png
security:
- kind: authentication
  name: Bank Of America Authentication
  slug: bank-of-america-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Bank Of America Domain Security
  slug: bank-of-america-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bank-of-america
tags:
- Banking
- Corporate Banking
- Finance
- Payments
- Treasury
- CashPro
- Fortune 100
use_cases:
- description: Automate daily cash positioning, balance reporting, and payment workflows.
  name: Treasury Automation
- description: Connect SAP, Oracle, or other ERP systems to Bank of America CashPro.
  name: ERP Integration
- description: Centralize payment initiation across ACH, wire, SWIFT, and real-time payment rails.
  name: Payments Hub
- description: Real-time visibility into global account balances for liquidity decisions.
  name: Liquidity Management
- description: Automated transaction download for account reconciliation workflows.
  name: Reconciliation
- description: Sweep and concentration account management via API.
  name: Cash Concentration
website: https://www.bankofamerica.com/
---
