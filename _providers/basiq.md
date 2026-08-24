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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Basiq Agentic Access
  operation_count: 14
  slug: basiq-agentic-access
  summary_line: 14 operations · 5 acting
api_count: 6
apis:
- description: The Accounts API from Basiq — 2 operation(s) for accounts.
  name: Basiq Accounts API
  slug: basiq-accounts-api
- description: The Affordability API from Basiq — 2 operation(s) for affordability.
  name: Basiq Affordability API
  slug: basiq-affordability-api
- description: The Authentication API from Basiq — 1 operation(s) for authentication.
  name: Basiq Authentication API
  slug: basiq-authentication-api
- description: The Connections API from Basiq — 2 operation(s) for connections.
  name: Basiq Connections API
  slug: basiq-connections-api
- description: The Transactions API from Basiq — 2 operation(s) for transactions.
  name: Basiq Transactions API
  slug: basiq-transactions-api
- description: The Users API from Basiq — 2 operation(s) for users.
  name: Basiq Users API
  slug: basiq-users-api
artifact_total: 83
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Basiq Accounts API
  slug: open-basiq-accounts-api
- collection_type: open
  name: Basiq Accounts Affordability API
  slug: open-basiq-affordability-api
- collection_type: open
  name: Basiq API
  slug: open-basiq-api
- collection_type: open
  name: Basiq Accounts Authentication API
  slug: open-basiq-authentication-api
- collection_type: open
  name: Basiq Accounts Connections API
  slug: open-basiq-connections-api
- collection_type: open
  name: Basiq Accounts Transactions API
  slug: open-basiq-transactions-api
- collection_type: open
  name: Basiq Accounts Users API
  slug: open-basiq-users-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/basiq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/basiq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/basiq-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/basiq-i-o
- group: company
  title: ''
  type: Website
  url: https://basiq.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.basiq.io/reference
- group: company
  title: ''
  type: Website
  url: https://dashboard.basiq.io/
- group: company
  title: ''
  type: Website
  url: https://basiq.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://basiq.io/blog/
- group: company
  title: ''
  type: Website
  url: https://github.com/basiqio
- group: commercial
  title: ''
  type: TermsOfService
  url: https://basiq.io/legal/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://basiq.io/legal/privacy-policy/
- group: design
  title: ''
  type: SpectralRules
  url: rules/basiq-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/basiq-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/basiq-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://api.basiq.io/llms.txt
created: '2026-03-27'
description: Basiq is an Australian open banking and financial data API platform providing unified access to bank account data and enrichment services. It enables fintechs, lenders, and financial service providers to connect to 180+ Australian and New Zealand banks via CDR (Consumer Data Right) and third-party connectors. The Basiq API provides user management, bank connections, account balances, transaction history, income verification, and expense categorization. Uses JWT Bearer token authentication.
examples:
- key_count: 5
  name: Account
  slug: account
- key_count: 3
  name: Accountlistresponse
  slug: accountlistresponse
- key_count: 4
  name: Connection
  slug: connection
- key_count: 3
  name: Connectionlistresponse
  slug: connectionlistresponse
- key_count: 3
  name: Createconnectionrequest
  slug: createconnectionrequest
- key_count: 4
  name: Createuserrequest
  slug: createuserrequest
- key_count: 5
  name: Errorresponse
  slug: errorresponse
- key_count: 3
  name: Expensereport
  slug: expensereport
- key_count: 3
  name: Incomeverification
  slug: incomeverification
- key_count: 3
  name: Tokenresponse
  slug: tokenresponse
- key_count: 5
  name: Transaction
  slug: transaction
- key_count: 4
  name: Transactionlistresponse
  slug: transactionlistresponse
- key_count: 5
  name: User
  slug: user
features:
- description: Connect to 180+ Australian and New Zealand banks via CDR and third-party connectors.
  name: Bank Connections
- description: Retrieve real-time account balances, available funds, and account metadata.
  name: Account Data
- description: Access enriched transaction history with categorization and merchant data.
  name: Transaction History
- description: Automated income stream identification and regular/irregular income calculation.
  name: Income Verification
- description: Transaction-based expense categorization for affordability and budgeting analysis.
  name: Expense Categorization
- description: Consumer Data Right (CDR) compliant data access for Australian open banking.
  name: CDR Compliance
- description: Transaction enrichment with merchant names, categories, and subcategories.
  name: Data Enrichment
finops:
- name: Basiq Finops
  service_category: API
  slug: basiq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/basiq.png
integrations:
- name: Xero
- name: MYOB
- name: Salesforce
- name: Zapier
- name: Commonwealth Bank
- name: ANZ
- name: Westpac
- name: NAB
json_schemas:
- name: Account
  property_count: 8
  slug: account
- name: AccountListResponse
  property_count: 3
  slug: accountlistresponse
- name: Connection
  property_count: 4
  slug: connection
- name: ConnectionListResponse
  property_count: 3
  slug: connectionlistresponse
- name: CreateConnectionRequest
  property_count: 3
  slug: createconnectionrequest
- name: CreateUserRequest
  property_count: 4
  slug: createuserrequest
- name: ErrorResponse
  property_count: 5
  slug: errorresponse
- name: ExpenseReport
  property_count: 3
  slug: expensereport
- name: IncomeVerification
  property_count: 3
  slug: incomeverification
- name: TokenResponse
  property_count: 3
  slug: tokenresponse
- name: Transaction
  property_count: 10
  slug: transaction
- name: TransactionListResponse
  property_count: 4
  slug: transactionlistresponse
- name: User
  property_count: 6
  slug: user
json_structures:
- name: Account
  property_count: 0
  slug: account
- name: Accountlistresponse
  property_count: 0
  slug: accountlistresponse
- name: Connection
  property_count: 0
  slug: connection
- name: Connectionlistresponse
  property_count: 0
  slug: connectionlistresponse
- name: Createconnectionrequest
  property_count: 0
  slug: createconnectionrequest
- name: Createuserrequest
  property_count: 0
  slug: createuserrequest
- name: Errorresponse
  property_count: 0
  slug: errorresponse
- name: Expensereport
  property_count: 0
  slug: expensereport
- name: Incomeverification
  property_count: 0
  slug: incomeverification
- name: Tokenresponse
  property_count: 0
  slug: tokenresponse
- name: Transaction
  property_count: 0
  slug: transaction
- name: Transactionlistresponse
  property_count: 0
  slug: transactionlistresponse
- name: User
  property_count: 0
  slug: user
jsonld:
- class_count: 8
  name: Basiq Context
  property_count: 32
  slug: basiq-context
layout: provider
modified: '2026-05-19'
name: Basiq
nav: Providers
network: true
overview: 'Basiq publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Affordability API, Authentication API, and 3 more. Tagged areas include Australia, Banking, CDR, Financial Data, and Fintech.


  The Basiq catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Basiq''s developer surface includes authentication, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Basiq Plans Pricing
  plan_count: 3
  slug: basiq-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Basiq Rate Limits
  slug: basiq-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Basiq API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: basiq-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Basiq API Rules
  rule_count: 22
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 15
  slug: basiq-spectral-rules
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 65.0
    developer_ergonomics: 19.0
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 34.4
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
    score: 21.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/basiq/refs/heads/main/screenshots/basiq-2026-06-20T173039.png
security:
- kind: authentication
  name: Basiq Authentication
  slug: basiq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Basiq Domain Security
  slug: basiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: basiq
tags:
- Australia
- Banking
- CDR
- Financial Data
- Fintech
- Open Banking
- Transaction
use_cases:
- description: Use income verification and expense data to assess creditworthiness and affordability.
  name: Lending and Credit Assessment
- description: Aggregate bank accounts and transactions for budgeting and financial planning tools.
  name: Personal Finance Apps
- description: Automate bank statement verification and income confirmation for home loan applications.
  name: Mortgage Applications
- description: Assess buy-now-pay-later affordability using real-time transaction and income data.
  name: BNPL Affordability
- description: Provide financial planners with complete client financial pictures across institutions.
  name: Financial Advisory
- description: Verify bank account ownership for payment and identity verification workflows.
  name: Account Verification
website: https://basiq.io/
---
