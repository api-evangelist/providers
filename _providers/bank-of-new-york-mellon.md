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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bank Of New York Mellon Agentic Access
  operation_count: 9
  slug: bank-of-new-york-mellon-agentic-access
  summary_line: 9 operations · 2 acting
api_count: 5
apis:
- description: The Accounts API from BNY Mellon — 2 operation(s) for accounts.
  name: BNY Mellon Accounts API
  slug: bank-of-new-york-mellon-accounts-api
- description: The Balances API from BNY Mellon — 1 operation(s) for balances.
  name: BNY Mellon Balances API
  slug: bank-of-new-york-mellon-balances-api
- description: The Funds Transfers API from BNY Mellon — 2 operation(s) for funds transfers.
  name: BNY Mellon Funds Transfers API
  slug: bank-of-new-york-mellon-funds-transfers-api
- description: The Payments API from BNY Mellon — 2 operation(s) for payments.
  name: BNY Mellon Payments API
  slug: bank-of-new-york-mellon-payments-api
- description: The Transactions API from BNY Mellon — 1 operation(s) for transactions.
  name: BNY Mellon Transactions API
  slug: bank-of-new-york-mellon-transactions-api
artifact_total: 74
collections:
- collection_type: open
  name: BNY Mellon Treasury Services API
  slug: open-bny-mellon-treasury-services-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bank-of-new-york-mellon-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-of-new-york-mellon-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bank-of-new-york-mellon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bank-of-new-york-mellon-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.bny.com/corporate/global/en/insights.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BNYMellon
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bny-mellon
- group: company
  title: ''
  type: Website
  url: https://www.bnymellon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://marketplace.bnymellon.com/treasury/api-central/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bny.com/app/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bnymellon.com/us/en/disclaimers/privacy-notice.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/bny-mellon-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/bny-mellon-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/bny-mellon-context.jsonld
created: '2024-01-01'
description: BNY Mellon is a global investments company providing asset servicing, asset management, wealth management, treasury services, and clearance and collateral management for institutions and individuals. The BNY Mellon Marketplace (marketplace.bnymellon.com) and developer portal (developer.bny.com) provide Treasury Services APIs for corporate clients to automate payments, account management, balance reporting, and funds transfers.
examples:
- key_count: 7
  name: Account Example
  slug: account-example
- key_count: 2
  name: Accountlistresponse Example
  slug: accountlistresponse-example
- key_count: 7
  name: Balance Example
  slug: balance-example
- key_count: 2
  name: Balanceresponse Example
  slug: balanceresponse-example
- key_count: 4
  name: Errorresponse Example
  slug: errorresponse-example
- key_count: 7
  name: Fundstransferrequest Example
  slug: fundstransferrequest-example
- key_count: 9
  name: Fundstransferresponse Example
  slug: fundstransferresponse-example
- key_count: 2
  name: Paymentlistresponse Example
  slug: paymentlistresponse-example
- key_count: 11
  name: Paymentrequest Example
  slug: paymentrequest-example
- key_count: 9
  name: Paymentresponse Example
  slug: paymentresponse-example
- key_count: 10
  name: Transaction Example
  slug: transaction-example
- key_count: 3
  name: Transactionlistresponse Example
  slug: transactionlistresponse-example
features:
- description: Access institutional account details and metadata.
  name: Account Management
- description: Real-time and intraday account balance queries.
  name: Balance Reporting
- description: Detailed transaction history with date range filtering.
  name: Transaction History
- description: Initiate wire, ACH, SWIFT, and CHIPS payments globally.
  name: Payment Initiation
- description: Internal account-to-account funds transfer management.
  name: Funds Transfers
- description: Client credentials OAuth2 flow for secure API access.
  name: OAuth2 Security
- description: UAT sandbox for developer testing and integration validation.
  name: Sandbox Environment
- description: Support for payments and balances across multiple currencies.
  name: Multi-Currency
finops:
- name: Bank Of New York Mellon Finops
  service_category: API
  slug: bank-of-new-york-mellon-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bank-of-new-york-mellon.png
integrations:
- name: SAP
- name: Oracle
- name: Kyriba
- name: FIS Quantum
- name: ION Treasury
- name: Workday
- name: Reval
json_schemas:
- name: Account
  property_count: 7
  slug: account
- name: AccountListResponse
  property_count: 2
  slug: accountlistresponse
- name: Balance
  property_count: 7
  slug: balance
- name: BalanceResponse
  property_count: 2
  slug: balanceresponse
- name: ErrorResponse
  property_count: 4
  slug: errorresponse
- name: FundsTransferRequest
  property_count: 7
  slug: fundstransferrequest
- name: FundsTransferResponse
  property_count: 9
  slug: fundstransferresponse
- name: PaymentListResponse
  property_count: 2
  slug: paymentlistresponse
- name: PaymentRequest
  property_count: 11
  slug: paymentrequest
- name: PaymentResponse
  property_count: 9
  slug: paymentresponse
- name: Transaction
  property_count: 10
  slug: transaction
- name: TransactionListResponse
  property_count: 3
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
- name: Errorresponse Structure
  property_count: 0
  slug: errorresponse-structure
- name: Fundstransferrequest Structure
  property_count: 0
  slug: fundstransferrequest-structure
- name: Fundstransferresponse Structure
  property_count: 0
  slug: fundstransferresponse-structure
- name: Paymentlistresponse Structure
  property_count: 0
  slug: paymentlistresponse-structure
- name: Paymentrequest Structure
  property_count: 0
  slug: paymentrequest-structure
- name: Paymentresponse Structure
  property_count: 0
  slug: paymentresponse-structure
- name: Transaction Structure
  property_count: 0
  slug: transaction-structure
- name: Transactionlistresponse Structure
  property_count: 0
  slug: transactionlistresponse-structure
jsonld:
- class_count: 0
  name: Bny Mellon Context
  property_count: 54
  slug: bny-mellon-context
layout: provider
modified: '2026-05-19'
name: BNY Mellon
nav: Providers
network: true
overview: 'BNY Mellon publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Balances API, Funds Transfers API, and 2 more. Tagged areas include Asset Servicing, Banking, Institutional Banking, Payments, and Treasury.


  The BNY Mellon catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  BNY Mellon''s developer surface includes authentication, engineering blog, documentation, and 11 more developer resources.'
plans:
- name: Bank Of New York Mellon Plans Pricing
  plan_count: 3
  slug: bank-of-new-york-mellon-plans-pricing
press:
- date: '2026-05-25'
  title: BNY, America's Oldest Bank, Signs Multiyear Deal With ...
  url: https://www.wsj.com/articles/bny-americas-oldest-bank-signs-multiyear-deal-with-openai-74987d1d
- date: '2026-05-25'
  title: BNY signs multiyear deal with OpenAI for AI tools
  url: https://www.linkedin.com/posts/isabelle-bousquette_my-latest-in-todays-print-edition-of-the-activity-7301076608004640768-Jybu
- date: '2026-05-25'
  title: BNY Mellon is all-in on digital
  url: https://www.americanbanker.com/news/bny-mellon-is-all-in-on-digital
- date: '2026-05-25'
  title: BNY embraces role on small lenders' AI journey
  url: https://www.bankingdive.com/news/bny-ai-community-banks-initiative-razzaque/811224/
- date: '2026-05-25'
  title: BNY Shares Jump 65% As AI Hiring Push Accelerates
  url: https://finance.yahoo.com/sectors/technology/articles/bny-shares-jump-65-ai-115004909.html
random_paper: 23
rate_limits:
- limit_count: 5
  name: Bank Of New York Mellon Rate Limits
  slug: bank-of-new-york-mellon-rate-limits
rules:
- name: BNY Mellon API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bank-of-new-york-mellon-jsonschema-spectral-rules
- name: BNY Mellon API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 9
  slug: bank-of-new-york-mellon-spectral-rules
- name: BNY Mellon API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 0
    warn: 6
  slug: bny-mellon-spectral-rules
scopes:
- name: Bank Of New York Mellon Scopes
  scope_count: 5
  slug: bank-of-new-york-mellon-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: developing
  composite: 51.8
  delta: -5.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 57.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/bank-of-new-york-mellon/refs/heads/main/screenshots/bank-of-new-york-mellon-2026-06-20T172950.png
security:
- kind: authentication
  name: Bank Of New York Mellon Authentication
  slug: bank-of-new-york-mellon-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Bank Of New York Mellon Domain Security
  slug: bank-of-new-york-mellon-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bank-of-new-york-mellon
tags:
- Asset Servicing
- Banking
- Institutional Banking
- Payments
- Treasury
- Wire Transfers
- Fortune 500
use_cases:
- description: Automate daily cash positioning, balance queries, and payment workflows.
  name: Treasury Automation
- description: Initiate global wire, ACH, and SWIFT payments programmatically.
  name: Payment Processing
- description: Real-time account balance visibility for institutional liquidity decisions.
  name: Liquidity Management
- description: Automated transaction downloads for reconciliation and reporting.
  name: Reconciliation
- description: Connect SAP, Oracle, and other ERP/TMS systems to BNY Mellon treasury APIs.
  name: ERP Integration
- description: Integrate treasury APIs into asset servicing and custody workflows.
  name: Custody Operations
website: https://www.bnymellon.com/
---
