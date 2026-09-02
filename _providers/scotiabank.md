---
access_model:
  confidence: high
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Scotiabank Agentic Access
  operation_count: 13
  slug: scotiabank-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 1
apis:
- description: Enables businesses to initiate secure, one-time wire transfers between accounts in the same currency (CAD or USD), domestically within Canada and the U.S., or internationally. Uses the SWIFT GPI-enabl
  name: Wire Payments API
  slug: wire-payments
- description: Provides fast payment capabilities for business transactions via INTERAC e-Transfer for business. Customers can send up to $25,000 per transaction in real time.
  name: Real-time Payments API
  slug: real-time-payments
- description: Supports creation and submission of Electronic Funds Transfers (EFTs), including inquiring on payment and file status, deleting, updating, and recalling or reversing payments.
  name: EFT Payment API
  slug: eft-payments
- description: Provides the ability to retrieve account balance for the current day or any prior day along with enriched transaction data for the two years prior, and view a list of eligible deposit accounts.
  name: Account Balance and Transactions API
  slug: account-balance-transactions
- description: Assists clients in determining the validity of an account number's format and indicates the likelihood of account ownership match for Scotiabank accounts.
  name: Account Validation API
  slug: account-validation
- description: Provides the capability to inquire on the status of wire payments using unique reference numbers, offering real-time payment tracking powered by SWIFT GPI.
  name: Payment Track and Trace API
  slug: payment-track-trace
- description: The Account Validation API from Scotiabank — 1 operation(s) for account validation.
  name: Scotiabank Account Validation API
  slug: scotiabank-account-validation-api
- description: The Accounts API from Scotiabank — 3 operation(s) for accounts.
  name: Scotiabank Accounts API
  slug: scotiabank-accounts-api
- description: The EFT Payments API from Scotiabank — 2 operation(s) for eft payments.
  name: Scotiabank EFT Payments API
  slug: scotiabank-eft-payments-api
- description: The Payment Tracking API from Scotiabank — 1 operation(s) for payment tracking.
  name: Scotiabank Payment Tracking API
  slug: scotiabank-payment-tracking-api
- description: The Real-Time Payments API from Scotiabank — 1 operation(s) for real-time payments.
  name: Scotiabank Real-Time Payments API
  slug: scotiabank-real-time-payments-api
- description: The Request for Payment API from Scotiabank — 1 operation(s) for request for payment.
  name: Scotiabank Request for Payment API
  slug: scotiabank-request-for-payment-api
- description: The Wire Payments API from Scotiabank — 2 operation(s) for wire payments.
  name: Scotiabank Wire Payments API
  slug: scotiabank-wire-payments-api
artifact_total: 51
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scotiabank Scotia TranXact APIs Account Validation API
  slug: open-scotiabank-account-validation-api
- collection_type: open
  name: Scotiabank Scotia TranXact APIs Account Validation Accounts API
  slug: open-scotiabank-accounts-api
- collection_type: open
  name: Scotiabank Scotia TranXact APIs Account Validation EFT Payments API
  slug: open-scotiabank-eft-payments-api
- collection_type: open
  name: Scotiabank Scotia TranXact APIs Account Validation Payment Tracking API
  slug: open-scotiabank-payment-tracking-api
- collection_type: open
  name: Scotiabank Scotia TranXact APIs Account Validation Real-Time Payments API
  slug: open-scotiabank-real-time-payments-api
- collection_type: open
  name: Scotiabank Scotia TranXact APIs Account Validation Request for Payment API
  slug: open-scotiabank-request-for-payment-api
- collection_type: open
  name: Scotiabank Scotia TranXact APIs
  slug: open-scotiabank-tranxact
- collection_type: open
  name: Scotiabank Scotia TranXact APIs Account Validation Wire Payments API
  slug: open-scotiabank-wire-payments-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/scotiabank-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scotiabank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scotiabank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scotiabank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/scotiabank-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scotiabank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scotiabank
created: '2026-05-02'
description: Scotiabank is one of Canada's leading financial institutions and a major international bank. Through its Scotia TranXact developer portal, Scotiabank provides APIs for corporate and commercial customers to integrate banking capabilities into their treasury management, ERP, and CRM systems. APIs cover wire payments, real-time payments via INTERAC e-Transfer, EFT payments, account balance and transaction data, account validation, and payment track and trace.
examples:
- key_count: 2
  name: Scotiabank Initiate Wire Payment Example
  slug: scotiabank-initiate-wire-payment-example
finops:
- name: Scotiabank Finops
  service_category: Banking
  slug: scotiabank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scotiabank.png
json_schemas:
- name: Account
  property_count: 5
  slug: scotiabank-account
- name: AccountBalanceResponse
  property_count: 6
  slug: scotiabank-accountbalanceresponse
- name: AccountsListResponse
  property_count: 1
  slug: scotiabank-accountslistresponse
- name: AccountValidationRequest
  property_count: 4
  slug: scotiabank-accountvalidationrequest
- name: AccountValidationResponse
  property_count: 2
  slug: scotiabank-accountvalidationresponse
- name: EFTPaymentRequest
  property_count: 6
  slug: scotiabank-eftpaymentrequest
- name: EFTPaymentResponse
  property_count: 4
  slug: scotiabank-eftpaymentresponse
- name: PaymentTrackingResponse
  property_count: 4
  slug: scotiabank-paymenttrackingresponse
- name: RealtimePaymentRequest
  property_count: 4
  slug: scotiabank-realtimepaymentrequest
- name: RealtimePaymentResponse
  property_count: 3
  slug: scotiabank-realtimepaymentresponse
- name: RequestForPaymentRequest
  property_count: 4
  slug: scotiabank-requestforpaymentrequest
- name: RequestForPaymentResponse
  property_count: 3
  slug: scotiabank-requestforpaymentresponse
- name: Scotiabank Transaction
  property_count: 15
  slug: scotiabank-transaction
- name: TransactionsListResponse
  property_count: 4
  slug: scotiabank-transactionslistresponse
- name: WirePaymentRequest
  property_count: 6
  slug: scotiabank-wirepaymentrequest
- name: WirePaymentResponse
  property_count: 6
  slug: scotiabank-wirepaymentresponse
json_structures:
- name: Scotiabank Structure
  property_count: 0
  slug: scotiabank-structure
- name: Scotiabank Wire Payment Structure
  property_count: 0
  slug: scotiabank-wire-payment-structure
jsonld:
- class_count: 0
  name: Scotiabank Context
  property_count: 16
  slug: scotiabank-context
layout: provider
modified: '2026-05-19'
name: Scotiabank
nav: Providers
network: true
overview: 'Scotiabank publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account Validation API, Accounts API, EFT Payments API, and 4 more. Tagged areas include Banking, Finance, Payments, Canada, and Open Banking.


  The Scotiabank catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Scotiabank''s developer surface includes authentication and 6 more developer resources.'
plans:
- name: Scotiabank Plans Pricing
  plan_count: 1
  slug: scotiabank-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Scotiabank Rate Limits
  slug: scotiabank-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Scotiabank API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: scotiabank-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Scotiabank API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: scotiabank-rules
scopes:
- name: Scotiabank Scopes
  scope_count: 3
  slug: scotiabank-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 41.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 52.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 28.8
    contract_quality: 69.9
    developer_ergonomics: 42.9
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 41.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scotiabank/refs/heads/main/screenshots/scotiabank-2026-06-20T193550.png
security:
- kind: authentication
  name: Scotiabank Authentication
  slug: scotiabank-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Scotiabank Domain Security
  slug: scotiabank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: scotiabank
tags:
- Banking
- Finance
- Payments
- Canada
- Open Banking
---
