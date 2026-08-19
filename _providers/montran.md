---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 31
  human_in_the_loop: 1
  name: Montran Agentic Access
  operation_count: 73
  slug: montran-agentic-access
  summary_line: 73 operations · 31 acting · 1 human-in-the-loop
api_count: 43
apis:
- description: A robust 24/7, high-capacity, retail-focused payment solution that processes individual payments in real-time with guaranteed end-to-end payment processing latency of a few seconds. Designed for centr
  name: Montran Instant Payments System
  slug: montran-instant-payments-system
- description: Provides secure, real-time settlement of high-value interbank payments. Holds a perfect security track record with no successful attacks on any Montran RTGS customer over the past decade.
  name: Montran Real-Time Gross Settlement
  slug: montran-real-time-gross-settlement
- description: An electronic clearing system that enables the full spectrum of payment instructions to be exchanged among financial institutions. Powers some of the largest clearing houses worldwide with support for
  name: Montran Automated Clearing House
  slug: montran-automated-clearing-house
- description: Handles very high volumes of both high-value and low-value payments such as credit transfers, direct debits, and cheques. Provides a unified clearing and settlement platform for diverse payment types.
  name: Montran Automated Transfer System
  slug: montran-automated-transfer-system
- description: A 24/7, ISO 20022 compliant platform that facilitates safekeeping of dematerialized financial instruments, settlement of trades free or against payment, and calculation and distribution of corporate a
  name: Montran Central Securities Depository
  slug: montran-central-securities-depository
- description: Provides a fast, secure, and innovative platform that facilitates the multi-currency trading of financial instruments including debt instruments and equities.
  name: Montran Trading System
  slug: montran-trading-system
- description: An enterprise-level system delivering real-time liquidity management with live monitoring, an intuitive user interface for granular insight into cash positions, and complete control over cash movement
  name: Montran Intraday Liquidity Management
  slug: montran-intraday-liquidity-management
- description: Provides multi-currency cash concentration and notional pooling, generating end-of-day or real-time sweeps from accounts held within the bank, its branches, or third-party banks. Supports ZBA, target,
  name: Montran Cash Pool Engine
  slug: montran-cash-pool-engine
- description: A multi-bank POBO/COBO platform using Virtual Account Management to allow corporations to centralize collection and payment-on-behalf-of operations regionally or globally. Available as SaaS or on-prem
  name: Montran Payments and Collections Factory
  slug: montran-payments-and-collections-factory
- description: Enables banks to offer in-house banking capability to global corporate customers, providing centralization of operations and controls, bank account rationalization, liquidity optimization, and automat
  name: Montran In-House Bank
  slug: montran-in-house-bank
- description: A 24/7, ISO 20022 based, paperless centralized platform for electronic mandates for direct debits and credit transfers. Stores and validates mandates to decrease risks associated with direct debit pay
  name: Montran Mandate Management
  slug: montran-mandate-management
- description: An online system for the automatic processing of all inquiries related to payments, both foreign and domestic. Provides investigation and compensation capabilities for payment exceptions and disputes.
  name: Montran Case Management
  slug: montran-case-management
- description: Provides comprehensive dispute resolution capabilities for payment transactions, enabling financial institutions to manage and resolve payment disputes efficiently.
  name: Montran Dispute Management
  slug: montran-dispute-management
- description: A backup real-time gross settlement solution providing business continuity for critical payment infrastructure, ensuring settlement operations continue even during primary system outages.
  name: Montran Backup RTGS
  slug: montran-backup-rtgs
- description: PSD2-compliant account information operations for AISP integration. Provides account details, balances, and transaction history.
  name: Montran Account Information API
  slug: montran-account-information-api
- description: Virtual account hierarchy and structure management
  name: Montran Account Structures API
  slug: montran-account-structures-api
- description: Multi-bank account visibility and management
  name: Montran Accounts API
  slug: montran-accounts-api
- description: Screening alert management and resolution
  name: Montran Alerts API
  slug: montran-alerts-api
- description: Payment approval workflow management
  name: Montran Approvals API
  slug: montran-approvals-api
- description: Balance inquiry and reconciliation operations
  name: Montran Balances API
  slug: montran-balances-api
- description: Beneficiary management for recurring payments
  name: Montran Beneficiaries API
  slug: montran-beneficiaries-api
- description: Communication channel management and monitoring
  name: Montran Channels API
  slug: montran-channels-api
- description: Clearing and settlement operations across multiple CSMs
  name: Montran Clearing API
  slug: montran-clearing-api
- description: Clearing and settlement system connectivity
  name: Montran Clearing Systems API
  slug: montran-clearing-systems-api
- description: Screening rules and channel configuration
  name: Montran Configuration API
  slug: montran-configuration-api
- description: PSD2 consent management for AISP and PISP access
  name: Montran Consent API
  slug: montran-consent-api
- description: Credit transfer payment operations including SEPA and cross-border
  name: Montran Credit Transfers API
  slug: montran-credit-transfers-api
- description: Direct debit payment operations
  name: Montran Direct Debits API
  slug: montran-direct-debits-api
- description: File upload and processing for batch payments
  name: Montran Files API
  slug: montran-files-api
- description: Real-time instant payment processing with guaranteed end-to-end latency of a few seconds
  name: Montran Instant Payments API
  slug: montran-instant-payments-api
- description: Sanctions and compliance list management
  name: Montran Lists API
  slug: montran-lists-api
- description: Message format conversion and validation
  name: Montran Message Formats API
  slug: montran-message-formats-api
- description: Message routing and transformation between systems
  name: Montran Message Routing API
  slug: montran-message-routing-api
- description: PSD2-compliant payment initiation operations for PISP integration. Supports instant credit transfers and request-to-pay flows.
  name: Montran Payment Initiation API
  slug: montran-payment-initiation-api
- description: Payment status inquiry and tracking operations
  name: Montran Payment Status API
  slug: montran-payment-status-api
- description: Corporate payment initiation and management
  name: Montran Payments API
  slug: montran-payments-api
- description: Request-to-pay initiation and management operations
  name: Montran Request to Pay API
  slug: montran-request-to-pay-api
- description: Transaction and entity screening operations
  name: Montran Screening API
  slug: montran-screening-api
- description: Account statement and reporting operations
  name: Montran Statements API
  slug: montran-statements-api
- description: SWIFT network connectivity and message management
  name: Montran SWIFT API
  slug: montran-swift-api
- description: Transaction processing and allocation
  name: Montran Transactions API
  slug: montran-transactions-api
- description: Virtual account creation, management, and lifecycle operations
  name: Montran Virtual Accounts API
  slug: montran-virtual-accounts-api
- description: Virtual IBAN issuance and management
  name: Montran Virtual IBANs API
  slug: montran-virtual-ibans-api
artifact_total: 185
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Montran Corporate Payments Portal Account Information API
  slug: open-montran-account-information-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Account Structures API
  slug: open-montran-account-structures-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Accounts API
  slug: open-montran-accounts-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Alerts API
  slug: open-montran-alerts-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Approvals API
  slug: open-montran-approvals-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Balances API
  slug: open-montran-balances-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Beneficiaries API
  slug: open-montran-beneficiaries-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Channels API
  slug: open-montran-channels-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Clearing API
  slug: open-montran-clearing-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Clearing Systems API
  slug: open-montran-clearing-systems-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Configuration API
  slug: open-montran-configuration-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Consent API
  slug: open-montran-consent-api
- collection_type: open
  name: Montran Corporate Payments Portal API
  slug: open-montran-corporate-payments-portal
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Credit Transfers API
  slug: open-montran-credit-transfers-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Direct Debits API
  slug: open-montran-direct-debits-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Files API
  slug: open-montran-files-api
- collection_type: open
  name: Montran Global Payments Hub API
  slug: open-montran-global-payments-hub
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Instant Payments API
  slug: open-montran-instant-payments-api
- collection_type: open
  name: Montran Instant Payments Gateway API
  slug: open-montran-instant-payments-gateway
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Lists API
  slug: open-montran-lists-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Message Formats API
  slug: open-montran-message-formats-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Message Routing API
  slug: open-montran-message-routing-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Payment Initiation API
  slug: open-montran-payment-initiation-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Payment Status API
  slug: open-montran-payment-status-api
- collection_type: open
  name: Montran Corporate Portal Account Information Payments API
  slug: open-montran-payments-api
- collection_type: open
  name: Montran Payments Connectivity API
  slug: open-montran-payments-connectivity
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Request to Pay API
  slug: open-montran-request-to-pay-api
- collection_type: open
  name: Montran Sanctions Screening API
  slug: open-montran-sanctions-screening
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Screening API
  slug: open-montran-screening-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Statements API
  slug: open-montran-statements-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information SWIFT API
  slug: open-montran-swift-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Transactions API
  slug: open-montran-transactions-api
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Virtual Accounts API
  slug: open-montran-virtual-accounts-api
- collection_type: open
  name: Montran Virtual Accounts API
  slug: open-montran-virtual-accounts
- collection_type: open
  name: Montran Corporate Payments Portal Account Information Virtual IBANs API
  slug: open-montran-virtual-ibans-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/montran-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/montran-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/montran-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/montran-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.montran.com/solutions/
- group: docs
  title: ''
  type: Documentation
  url: https://www.montran.com/solutions/
- group: company
  title: ''
  type: Blog
  url: https://www.montran.com/news-and-insights/
- group: operate
  title: ''
  type: Support
  url: https://www.montran.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.montran.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.montran.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.montran.com/contact-us/
- group: company
  title: ''
  type: Website
  url: https://www.montran.com/
- group: company
  title: ''
  type: About
  url: https://www.montran.com/company/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/montran
- group: other
  title: ''
  type: X
  url: https://x.com/montrancorp
created: '2025'
description: Montran Corporation provides technologically advanced critical payments, cash management, and securities solutions to commercial banks, corporates, central banks, and clearing institutions in over 90 countries. With more than 45 years of innovation, Montran offers market infrastructure solutions including RTGS, ACH, instant payments, and central securities depository systems.
finops:
- name: Montran Finops
  service_category: Payments / Capital Markets Software
  slug: montran-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/montran.png
json_schemas:
- name: Montran Account
  property_count: 13
  slug: montran-account
- name: AccountBalance
  property_count: 3
  slug: montran-accountbalance
- name: AccountBalances
  property_count: 2
  slug: montran-accountbalances
- name: AccountDetail
  property_count: 7
  slug: montran-accountdetail
- name: AccountIdentification
  property_count: 3
  slug: montran-accountidentification
- name: AccountList
  property_count: 1
  slug: montran-accountlist
- name: AccountStatementList
  property_count: 2
  slug: montran-accountstatementlist
- name: AccountStructure
  property_count: 6
  slug: montran-accountstructure
- name: AccountStructureCreate
  property_count: 4
  slug: montran-accountstructurecreate
- name: AccountStructureList
  property_count: 1
  slug: montran-accountstructurelist
- name: AlertDetail
  property_count: 10
  slug: montran-alertdetail
- name: AlertList
  property_count: 2
  slug: montran-alertlist
- name: AlertResolution
  property_count: 3
  slug: montran-alertresolution
- name: BalanceVerificationRequest
  property_count: 2
  slug: montran-balanceverificationrequest
- name: BalanceVerificationResponse
  property_count: 2
  slug: montran-balanceverificationresponse
- name: BankAccount
  property_count: 11
  slug: montran-bankaccount
- name: BankAccountList
  property_count: 1
  slug: montran-bankaccountlist
- name: BatchScreeningRequest
  property_count: 2
  slug: montran-batchscreeningrequest
- name: BatchScreeningResult
  property_count: 6
  slug: montran-batchscreeningresult
- name: Beneficiary
  property_count: 9
  slug: montran-beneficiary
- name: BeneficiaryCreate
  property_count: 7
  slug: montran-beneficiarycreate
- name: BeneficiaryList
  property_count: 2
  slug: montran-beneficiarylist
- name: BulkPaymentRequest
  property_count: 4
  slug: montran-bulkpaymentrequest
- name: BulkPaymentResponse
  property_count: 6
  slug: montran-bulkpaymentresponse
- name: ChannelDetail
  property_count: 7
  slug: montran-channeldetail
- name: ChannelHealth
  property_count: 7
  slug: montran-channelhealth
- name: ChannelList
  property_count: 1
  slug: montran-channellist
- name: ClearingBatch
  property_count: 10
  slug: montran-clearingbatch
- name: ClearingBatchList
  property_count: 2
  slug: montran-clearingbatchlist
- name: ClearingSystemDetail
  property_count: 8
  slug: montran-clearingsystemdetail
- name: ClearingSystemList
  property_count: 1
  slug: montran-clearingsystemlist
- name: ComplianceListDetail
  property_count: 7
  slug: montran-compliancelistdetail
- name: ComplianceListSummary
  property_count: 1
  slug: montran-compliancelistsummary
- name: ConsentRequest
  property_count: 6
  slug: montran-consentrequest
- name: ConsentResponse
  property_count: 6
  slug: montran-consentresponse
- name: CorporatePayment
  property_count: 14
  slug: montran-corporatepayment
- name: CorporatePaymentCreate
  property_count: 12
  slug: montran-corporatepaymentcreate
- name: CorporatePaymentList
  property_count: 2
  slug: montran-corporatepaymentlist
- name: CreditTransferInitiation
  property_count: 18
  slug: montran-credittransferinitiation
- name: CreditTransferRequest
  property_count: 9
  slug: montran-credittransferrequest
- name: DirectDebitInitiation
  property_count: 16
  slug: montran-directdebitinitiation
- name: EntityScreeningRequest
  property_count: 8
  slug: montran-entityscreeningrequest
- name: EntityScreeningResult
  property_count: 5
  slug: montran-entityscreeningresult
- name: Error
  property_count: 3
  slug: montran-error
- name: FileStatus
  property_count: 10
  slug: montran-filestatus
- name: FileUploadResponse
  property_count: 4
  slug: montran-fileuploadresponse
- name: Montran Financial Institution
  property_count: 9
  slug: montran-financial-institution
- name: FinancialInstitution
  property_count: 3
  slug: montran-financialinstitution
- name: InstantPaymentDetail
  property_count: 18
  slug: montran-instantpaymentdetail
- name: InstantPaymentRequest
  property_count: 14
  slug: montran-instantpaymentrequest
- name: InstantPaymentResponse
  property_count: 8
  slug: montran-instantpaymentresponse
- name: InternalTransfer
  property_count: 5
  slug: montran-internaltransfer
- name: InternalTransferResponse
  property_count: 7
  slug: montran-internaltransferresponse
- name: MessageDetail
  property_count: 13
  slug: montran-messagedetail
- name: MessageList
  property_count: 2
  slug: montran-messagelist
- name: MessageResponse
  property_count: 5
  slug: montran-messageresponse
- name: MessageSubmission
  property_count: 7
  slug: montran-messagesubmission
- name: Pagination
  property_count: 4
  slug: montran-pagination
- name: Montran Payment
  property_count: 25
  slug: montran-payment
- name: PaymentCancellationRequest
  property_count: 2
  slug: montran-paymentcancellationrequest
- name: PaymentCancellationResponse
  property_count: 4
  slug: montran-paymentcancellationresponse
- name: PaymentDetail
  property_count: 18
  slug: montran-paymentdetail
- name: PaymentInitiation
  property_count: 15
  slug: montran-paymentinitiation
- name: PaymentInitiationResponse
  property_count: 4
  slug: montran-paymentinitiationresponse
- name: PaymentList
  property_count: 2
  slug: montran-paymentlist
- name: PaymentResponse
  property_count: 6
  slug: montran-paymentresponse
- name: PaymentReturnRequest
  property_count: 2
  slug: montran-paymentreturnrequest
- name: PaymentReturnResponse
  property_count: 4
  slug: montran-paymentreturnresponse
- name: PaymentStatus
  property_count: 7
  slug: montran-paymentstatus
- name: PaymentStatusResponse
  property_count: 6
  slug: montran-paymentstatusresponse
- name: RequestToPayDetail
  property_count: 13
  slug: montran-requesttopaydetail
- name: RequestToPayRequest
  property_count: 10
  slug: montran-requesttopayrequest
- name: RequestToPayResponse
  property_count: 3
  slug: montran-requesttopayresponse
- name: Montran Screening Result
  property_count: 10
  slug: montran-screening-result
- name: ScreeningChannelList
  property_count: 1
  slug: montran-screeningchannellist
- name: ScreeningMatch
  property_count: 9
  slug: montran-screeningmatch
- name: ScreeningRequest
  property_count: 5
  slug: montran-screeningrequest
- name: ScreeningResult
  property_count: 6
  slug: montran-screeningresult
- name: StatusHistoryEntry
  property_count: 4
  slug: montran-statushistoryentry
- name: SwiftMessageList
  property_count: 2
  slug: montran-swiftmessagelist
- name: Montran Transaction
  property_count: 16
  slug: montran-transaction
- name: TransactionData
  property_count: 14
  slug: montran-transactiondata
- name: TransactionList
  property_count: 2
  slug: montran-transactionlist
- name: TransformRequest
  property_count: 5
  slug: montran-transformrequest
- name: TransformResponse
  property_count: 6
  slug: montran-transformresponse
- name: ValidateRequest
  property_count: 3
  slug: montran-validaterequest
- name: ValidationResult
  property_count: 2
  slug: montran-validationresult
- name: VirtualAccount
  property_count: 14
  slug: montran-virtualaccount
- name: VirtualAccountBalance
  property_count: 7
  slug: montran-virtualaccountbalance
- name: VirtualAccountCreate
  property_count: 9
  slug: montran-virtualaccountcreate
- name: VirtualAccountList
  property_count: 2
  slug: montran-virtualaccountlist
- name: VirtualAccountUpdate
  property_count: 4
  slug: montran-virtualaccountupdate
- name: VirtualIban
  property_count: 6
  slug: montran-virtualiban
- name: VirtualIbanCreate
  property_count: 3
  slug: montran-virtualibancreate
- name: VirtualIbanList
  property_count: 2
  slug: montran-virtualibanlist
- name: VirtualTransactionList
  property_count: 2
  slug: montran-virtualtransactionlist
json_structures:
- name: Montran Structure
  property_count: 0
  slug: montran-structure
jsonld:
- class_count: 1
  name: Montran Context
  property_count: 8
  slug: montran-context
layout: provider
modified: '2026-05-19'
name: Montran
nav: Providers
network: true
overview: 'Montran publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Account Information API, Account Structures API, Accounts API, and 26 more. Tagged areas include Banking, Central Banking, Financial Services, ISO 20022, and Market Infrastructure.


  The Montran catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Montran''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 10 more developer resources.'
plans:
- name: Montran Plans Pricing
  plan_count: 1
  slug: montran-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Montran Rate Limits
  slug: montran-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Montran API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: montran-jsonschema-spectral-rules
scopes:
- name: Montran Scopes
  scope_count: 2
  slug: montran-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 44.7
  delta: -3.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 70.6
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 5.3
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 58.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/montran/refs/heads/main/screenshots/montran-2026-06-20T185750.png
security:
- kind: authentication
  name: Montran Authentication
  slug: montran-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Montran Domain Security
  slug: montran-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: montran
tags:
- Banking
- Central Banking
- Financial Services
- ISO 20022
- Market Infrastructure
- Messaging
- Payments
- Real-Time Payments
- SWIFT
website: https://www.montran.com/
---
