---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Commonwealth Bank Agentic Access
  operation_count: 38
  slug: commonwealth-bank-agentic-access
  summary_line: 38 operations · 6 acting
api_count: 25
apis:
- description: 'Documented in CommBank''s business API catalogue as the Credit Transfer Initiation / Fast Payment API: a near real-time capability that lets a business send money to most Australian financial instituti'
  name: Commonwealth Bank Fast Payment (Credit Transfer Initiation) API
  slug: cba-fast-payment-credit-transfer-api
- description: 'Documented in CommBank''s business API catalogue: NameCheck is a security tool that helps organisations and their customers avoid false billing scams and mistaken payments by checking payee account nam'
  name: Commonwealth Bank NameCheck API
  slug: cba-namecheck-api
- description: 'Documented in CommBank''s business API catalogue: PayTo is a modern digital payment solution enabling near real-time, account-to-account payments from a customer''s bank account over the New Payments Pl'
  name: Commonwealth Bank PayTo API
  slug: cba-payto-api
- description: CommBank's merchant Payment Gateway exposes a hosted REST API for online card acceptance, authorisation, capture, refunds, tokenisation, and hosted checkout for eCommerce merchants. Integration guidel
  name: CommBank Payment Gateway API
  slug: cba-payment-gateway-api
- description: 'CommBank API Banking provides programmatic banking interfaces for business customers covering payments, account information, reconciliation, and direct integration with ERP and accounting systems for '
  name: CommBank API Banking for Business
  slug: commbank-app-api-banking
- description: CommBiz is CommBank's business and corporate online banking platform supporting multi-user payments, account management, bulk payments, foreign exchange, file-based banking, treasury management, and b
  name: CommBiz
  slug: commbiz
- description: CommBank International Payments provides foreign exchange, international money transfer, travel money cards, and overseas payment services for retail and business customers, including SWIFT integratio
  name: CommBank International Payments
  slug: commbank-international
- description: CommBank provides merchant payment acceptance through EFTPOS terminals, eCommerce gateways, BPAY merchant services, Smart mini and Smart Pos terminals, and online card acceptance. Includes integration
  name: CommBank Merchant Payments
  slug: commbank-merchant-payments
- description: The CommBank mobile app is the bank's primary digital channel for personal customers offering account management, transfers, bill payment via BPAY, mobile cheque deposit, PayID, NPP real-time transfer
  name: CommBank Mobile App
  slug: commbank-mobile-app
- description: NetBank is CommBank's web-based online banking platform giving personal customers access to account details, transactions, transfers, BPAY payments, statements, card services, and customer self-servic
  name: NetBank
  slug: netbank
- description: CommBank Yello is the bank's customer recognition and rewards program offering eligible customers exclusive cashback offers, partner discounts, fee waivers, and home loan benefits surfaced through the
  name: CommBank Yello
  slug: commbank-yello
- description: Obtain the list of accounts authorised to be shared by the customer. Account API is a consumer API. To access data you'll need the customer's consent.</p><h3 style="margin-top:30px;">Host URL</h3><p>C
  name: Commonwealth Bank Accounts API API
  slug: commonwealth-bank-accounts-api-api
- description: 'Obtain the balance for a single specified account. Balances API is a consumer API. To access data you''ll need the customer''s consent.</p><h3 style="margin-top:30px;">Host URL</h3><p>CommBank requests '
  name: Commonwealth Bank Balances API API
  slug: commonwealth-bank-balances-api-api
- description: Banking Account Balance endpoints
  name: Commonwealth Bank Banking Account Balances API
  slug: commonwealth-bank-banking-account-balances-api
- description: Banking Account Direct Debit endpoints
  name: Commonwealth Bank Banking Account Direct Debits API
  slug: commonwealth-bank-banking-account-direct-debits-api
- description: Banking Account Scheduled Payment endpoints
  name: Commonwealth Bank Banking Account Scheduled Payments API
  slug: commonwealth-bank-banking-account-scheduled-payments-api
- description: Banking Account Transaction endpoints
  name: Commonwealth Bank Banking Account Transactions API
  slug: commonwealth-bank-banking-account-transactions-api
- description: Banking Account endpoints
  name: Commonwealth Bank Banking Accounts API
  slug: commonwealth-bank-banking-accounts-api
- description: Banking Payee endpoints
  name: Commonwealth Bank Banking Payees API
  slug: commonwealth-bank-banking-payees-api
- description: Banking Product endpoints
  name: Commonwealth Bank Banking Products API
  slug: commonwealth-bank-banking-products-api
- description: Access a customer's basic contact details. The customer may choose to share their personal or organisation details. Customer API is a consumer API. To access data you'll need the customer's consent.</
  name: Commonwealth Bank Customer API API
  slug: commonwealth-bank-customer-api-api
- description: Obtain a list of pre-registered payees authorised to be shared by the customer. Payees API is a consumer API. To access data you'll need the customer's consent.</p><h3 style="margin-top:30px;">Host UR
  name: Commonwealth Bank Payees API API
  slug: commonwealth-bank-payees-api-api
- description: Get details on available CommBank products including deposit and transaction accounts, credit cards, home loans, personal loans, and offset accounts. Information available through the API includes eli
  name: Commonwealth Bank Products API API
  slug: commonwealth-bank-products-api-api
- description: Obtain the Regular Payment details authorised to be shared by the customer. Regular Payments API is a consumer API. To access data you'll need the customer's consent.</p><h3 style="margin-top:30px;">H
  name: Commonwealth Bank Regular Payments API API
  slug: commonwealth-bank-regular-payments-api-api
- description: Obtain the list of transactions for a CommBank account and details for each transaction. Transaction API is a consumer API. To access data you'll need the customer's consent. Seven years’ worth of tra
  name: Commonwealth Bank Transaction API API
  slug: commonwealth-bank-transaction-api-api
artifact_total: 66
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CommBank Accounts Accounts API API
  slug: open-commonwealth-bank-accounts-api-api
- collection_type: open
  name: CommBank Accounts Accounts API Balances API API
  slug: open-commonwealth-bank-balances-api-api
- collection_type: open
  name: CommBank Accounts Accounts API Banking Account Balances API
  slug: open-commonwealth-bank-banking-account-balances-api
- collection_type: open
  name: CommBank Accounts Accounts API Banking Account Direct Debits API
  slug: open-commonwealth-bank-banking-account-direct-debits-api
- collection_type: open
  name: CommBank Accounts Accounts API Banking Account Scheduled Payments API
  slug: open-commonwealth-bank-banking-account-scheduled-payments-api
- collection_type: open
  name: CommBank Accounts Accounts API Banking Account Transactions API
  slug: open-commonwealth-bank-banking-account-transactions-api
- collection_type: open
  name: CommBank Accounts Accounts API Banking Accounts API
  slug: open-commonwealth-bank-banking-accounts-api
- collection_type: open
  name: CommBank Accounts Accounts API Banking Payees API
  slug: open-commonwealth-bank-banking-payees-api
- collection_type: open
  name: CommBank Accounts Accounts API Banking Products API
  slug: open-commonwealth-bank-banking-products-api
- collection_type: open
  name: CommBank Accounts Accounts API Customer API API
  slug: open-commonwealth-bank-customer-api-api
- collection_type: open
  name: CommBank Accounts Accounts API Payees API API
  slug: open-commonwealth-bank-payees-api-api
- collection_type: open
  name: CommBank Accounts Accounts API Products API API
  slug: open-commonwealth-bank-products-api-api
- collection_type: open
  name: CommBank Accounts Accounts API Regular Payments API API
  slug: open-commonwealth-bank-regular-payments-api-api
- collection_type: open
  name: CommBank Accounts Accounts API Transaction API API
  slug: open-commonwealth-bank-transaction-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/commonwealth-bank-cdr-accounts-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/commonwealth-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/commonwealth-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/commonwealth-bank-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/commonwealth-bank-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/commonwealth-bank-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/commonwealth-bank-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/commonwealth-bank-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.commbank.com.au/developer/Documentation/specification/Discovery
- group: operate
  title: ''
  type: Deprecation
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: design
  title: ''
  type: Conformance
  url: conformance/commonwealth-bank-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.commbank.com.au/banking/open-banking.html
- group: design
  title: ''
  type: DataModel
  url: data-model/commonwealth-bank-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/commonwealth-bank-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/commonwealth-bank-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.commbank.com.au/developer
- group: start
  title: ''
  type: Portal
  url: https://developer.api.commbank.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.commbank.com.au/developer/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://consumerdatastandardsaustralia.github.io/standards/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.commbank.com.au/developer
- group: other
  title: ''
  type: OpenBanking
  url: https://www.commbank.com.au/banking/open-banking.html
- group: other
  title: ''
  type: DataSharing
  url: https://www.commbank.com.au/banking/open-banking/data-sharing-from-cba.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.api.commbank.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commbank.com.au/support/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://www.commbank.com.au/support.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/commbank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/commonwealthbank
- group: company
  title: ''
  type: Website
  url: https://www.commbank.com.au/
- group: start
  title: ''
  type: Login
  url: https://www.my.commbank.com.au/netbank/Logon/Logon.aspx
- group: other
  title: ''
  type: Business
  url: https://www.commbank.com.au/business.html
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.commbank.com.au/about-us/shareholders.html
- group: auth
  title: ''
  type: Security
  url: https://www.commbank.com.au/support/security.html
- group: company
  title: ''
  type: Blog
  url: https://www.commbank.com.au/newsroom.html
created: '2026-05-05'
description: Commonwealth Bank of Australia (CBA) is Australia's largest bank by market capitalization, a "Big Four" authorised deposit-taking institution (ADI) regulated by APRA and listed on the ASX (CBA), providing retail, business, and institutional banking. CBA serves millions of customers through NetBank online banking, the CommBank mobile app, CommBiz for business, and CommBank Yello loyalty. As a designated data holder under Australia's Consumer Data Right (CDR / Open Banking) regime, CommBank exposes a PUBLIC, unauthenticated Product Reference Data (PRD) API and a full set of consumer-AUTHORIZED CDR Banking endpoints (accounts, balances, transactions, direct debits, scheduled payments, payees, customer) conforming to the DSB Consumer Data Standards CDR Banking API v1.36.0. The bank publishes its own first-party Swagger 2.0 specifications for each of these families on its developer portal, and additionally documents a business API catalogue (Fast Payment / NPP credit transfer initiation,
  NameCheck, PayTo) and a hosted merchant Payment Gateway.
features:
- description: Everyday accounts, savings, home loans, credit cards, and personal loans.
  name: Personal Banking
- description: Business accounts, lending, merchant services, and CommBiz integration.
  name: Business Banking
- description: Data holder under Australia's Consumer Data Right with public PRD and consent-driven data sharing.
  name: Open Banking (CDR)
- description: CommBank app with Money Plan budgeting, card controls, and Yello rewards.
  name: Mobile Banking
- description: CommBank Yello customer recognition with cashback offers and fee waivers.
  name: Loyalty Recognition
- description: EFTPOS, eCommerce, and integrated payment acceptance for businesses.
  name: Merchant Payments
- description: FX, SWIFT, and travel money card services for personal and business customers.
  name: International Payments
- description: Programmatic banking interfaces (Fast Payment, NameCheck, PayTo) for business integration.
  name: API Banking
- description: NPP and PayID instant transfer support across personal and business channels.
  name: Real-Time Payments
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/commonwealth-bank.png
integrations:
- description: New Payments Platform real-time clearing and settlement integration.
  name: NPP Australia
- description: BPAY scheme for bill payment and merchant collections.
  name: BPAY
- description: PayID alias-based addressing for NPP real-time payments.
  name: PayID
- description: SWIFT messaging for cross-border payments and correspondent banking.
  name: SWIFT
- description: Consumer Data Right data sharing with Accredited Data Recipients.
  name: CDR Ecosystem
- description: Major card scheme acquiring and issuing partnerships.
  name: Mastercard and Visa
layout: provider
mcp_servers:
- description: ''
  name: commonwealth-bank-mcp.yml
  slug: commonwealth-bank-mcpyml
modified: '2026-07-21'
name: Commonwealth Bank
nav: Providers
network: true
overview: 'Commonwealth Bank publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API API, Balances API API, Banking Account Balances API, and 11 more. Tagged areas include Financial, Banks, Consumer Banking, Business Banking, and Open Banking.


  Commonwealth Bank''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
random_paper: 8
scopes:
- name: Commonwealth Bank Scopes
  scope_count: 10
  slug: commonwealth-bank-scopes
  summary_line: 10 scopes
score:
  band: developing
  composite: 44.1
  delta: 3.5
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 30.3
    contract_quality: 12.9
    developer_ergonomics: 58.9
    discoverability: 66.7
    governance: 30.3
    operational_transparency: 36.8
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 14
      marker_coverage: 100.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 77.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/commonwealth-bank/refs/heads/main/screenshots/commonwealth-bank-2026-07-21T114720.png
security:
- kind: authentication
  name: Commonwealth Bank Authentication
  slug: commonwealth-bank-authentication
  summary_line: oauth2/openIdConnect/mutualTLS/none · 4 schemes
- kind: domain-security
  name: Commonwealth Bank Domain Security
  slug: commonwealth-bank-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: commonwealth-bank
tags:
- Financial
- Banks
- Consumer Banking
- Business Banking
- Open Banking
- CDR
- Product Reference Data
- ADI
- Australia
use_cases:
- description: Authorized third parties access consumer banking data via CDR with consumer consent.
  name: Open Banking Data Sharing
- description: Automated reconciliation of accounts and payments via API Banking integrations.
  name: Business Reconciliation
- description: SME and enterprise card acceptance through CommBank merchant solutions.
  name: Merchant Acceptance
- description: Daily banking, transfers, and budgeting through the CommBank app.
  name: Consumer Mobile Banking
- description: Send and receive international payments for retail and business customers.
  name: Cross-Border Payments
- description: Corporate treasury automation using CommBiz and API Banking.
  name: Treasury Operations
website: https://www.commbank.com.au/
---
