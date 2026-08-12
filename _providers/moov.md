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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 36
  human_in_the_loop: 4
  name: Moov Agentic Access
  operation_count: 68
  slug: moov-agentic-access
  summary_line: 68 operations · 36 acting · 4 human-in-the-loop
api_count: 16
apis:
- description: 'Moov.js is a client-side JavaScript SDK designed to streamline interactions with the Moov API while keeping personally identifiable information out of developer infrastructure. All PII is transmitted '
  name: Moov.js
  slug: moov-js
- description: Moov Drops are pre-built, drop-in web UI components for complicated payment and account management flows. These components securely collect payment and account information from users without developer
  name: Moov Drops
  slug: moov-drops
- description: 'Moov provides official server-side client libraries for interacting with the Moov API across multiple programming languages, including Go, TypeScript, Python, Java, PHP, Ruby, and C#/.NET. These SDKs '
  name: Moov Backend SDKs
  slug: moov-backend-sdks
- description: Create and manage Moov accounts representing individual or business legal entities. Accounts are the foundation for all money movement operations.
  name: Moov Accounts API
  slug: moov-accounts-api
- description: OAuth2 access token creation and revocation for API authentication.
  name: Moov Authentication API
  slug: moov-authentication-api
- description: Link and manage bank accounts as funding sources for ACH and RTP transfers. Includes micro-deposit and instant verification flows.
  name: Moov Bank Accounts API
  slug: moov-bank-accounts-api
- description: Request and manage capabilities that enable specific financial operations on an account, such as send-funds or collect-funds.
  name: Moov Capabilities API
  slug: moov-capabilities-api
- description: Link and manage debit and credit cards as payment sources on Moov accounts.
  name: Moov Cards API
  slug: moov-cards-api
- description: Manage card payment disputes including evidence submission, acceptance, and lifecycle tracking for chargeback resolution.
  name: Moov Disputes API
  slug: moov-disputes-api
- description: Create and manage shareable payment links that allow customers to pay via card or bank account without custom code.
  name: Moov Payment Links API
  slug: moov-payment-links-api
- description: Retrieve the available payment methods on an account, including bank accounts, cards, and wallets, which can be used as transfer sources or destinations.
  name: Moov Payment Methods API
  slug: moov-payment-methods-api
- description: Create and retrieve refunds for completed card transfers, including full and partial refund support.
  name: Moov Refunds API
  slug: moov-refunds-api
- description: Manage business representatives associated with a Moov account for KYB compliance and ownership verification.
  name: Moov Representatives API
  slug: moov-representatives-api
- description: Configure automatic daily transfers from a Moov wallet to an external bank account on a set schedule using ACH or RTP rails.
  name: Moov Sweeps API
  slug: moov-sweeps-api
- description: Initiate and manage money movement between Moov accounts. Supports ACH, RTP, and card rails with full lifecycle tracking.
  name: Moov Transfers API
  slug: moov-transfers-api
- description: Create and manage Moov digital wallets that hold funds within the platform. Supports wallet transactions and balance adjustments.
  name: Moov Wallets API
  slug: moov-wallets-api
artifact_total: 110
asyncapis:
- description: Moov delivers real-time event notifications to your application via webhooks when state changes occur on your platform. When an event occurs, Moov sends an HTTP POST request with a JSON payload to you
  name: Moov Webhooks
  slug: moov-webhooks-asyncapi
collections:
- collection_type: open
  name: Moov API
  slug: open-moov-api
- collection_type: open
  name: Moov API
  slug: open-moov-io
common:
- group: operate
  title: ''
  type: Roadmap
  url: https://moov.io/platform/roadmap
- group: operate
  title: ''
  type: Support
  url: https://support.moov.io
- group: design
  title: ''
  type: Webhooks
  url: https://docs.moov.io/guides/webhooks/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.moov.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.moov.io/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moov.io/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.moov.io/moovjs/drops/terms-of-service/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moov.io/guides/quick-start
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/moov-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/moov-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moov-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/moov-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moovfinancial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/moov-io
- group: start
  title: ''
  type: Portal
  url: https://docs.moov.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moov.io/
- group: company
  title: ''
  type: Website
  url: https://moov.io/
- group: company
  title: ''
  type: Blog
  url: https://moov.io/blog/
- group: start
  title: ''
  type: Login
  url: https://dashboard.moov.io/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.moov.io/llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/moov-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/moov-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/moov-finops.yml
created: '2026-03-21'
description: Moov is a financial infrastructure platform that enables developers to embed money movement capabilities directly into their applications. Their developer platform provides a RESTful API, client-side JavaScript SDK, pre-built UI components, and official backend SDKs across multiple languages for building compliant, full-featured financial products.
features:
- 'Card Acceptance: IC+ + 0.60% + $0.15/transaction'
- 'Tap to Pay: IC+ + 0.50% + $0.15'
- 'Instant Payments (RTP): 0.95% (50¢ min, $5 cap)'
- 'ACH transfers: $0.25-$0.40 each'
- 'Moov Wallets: $0.50/active wallet/month'
- 'Virtual Cards: $0.15 per card creation'
- $500/month minimum across all products
- Apple Pay and Google Pay support
- 'International cards: +1.5% surcharge'
- 'REST API: 600 req/min default'
- Webhooks for facilitator/account/transfer events
- OAuth 2.0 + API tokens
- Embedded onboarding for sub-merchants
- KYC/KYB built in
- 1099-K reporting handled
- Custom pricing for high-volume
finops:
- name: Moov Finops
  service_category: Embedded Finance
  slug: moov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moov.png
json_schemas:
- name: AccessToken
  property_count: 4
  slug: moov-accesstoken
- name: Moov Account
  property_count: 10
  slug: moov-account
- name: AccountConnection
  property_count: 3
  slug: moov-accountconnection
- name: AccountConnectionRequest
  property_count: 1
  slug: moov-accountconnectionrequest
- name: AccountProfile
  property_count: 2
  slug: moov-accountprofile
- name: AccountVerification
  property_count: 1
  slug: moov-accountverification
- name: Address
  property_count: 6
  slug: moov-address
- name: Amount
  property_count: 2
  slug: moov-amount
- name: BankAccount
  property_count: 9
  slug: moov-bankaccount
- name: BankAccountVerification
  property_count: 2
  slug: moov-bankaccountverification
- name: BusinessProfile
  property_count: 9
  slug: moov-businessprofile
- name: Capability
  property_count: 7
  slug: moov-capability
- name: CapabilityRequirement
  property_count: 2
  slug: moov-capabilityrequirement
- name: Card
  property_count: 14
  slug: moov-card
- name: CardExpiration
  property_count: 2
  slug: moov-cardexpiration
- name: CardVerification
  property_count: 3
  slug: moov-cardverification
- name: CompleteVerificationRequest
  property_count: 1
  slug: moov-completeverificationrequest
- name: CreateAccountRequest
  property_count: 5
  slug: moov-createaccountrequest
- name: CreatePaymentLinkRequest
  property_count: 3
  slug: moov-createpaymentlinkrequest
- name: CreateRefundRequest
  property_count: 1
  slug: moov-createrefundrequest
- name: CreateRepresentativeRequest
  property_count: 7
  slug: moov-createrepresentativerequest
- name: CreateSweepConfigRequest
  property_count: 4
  slug: moov-createsweepconfigrequest
- name: CreateTransferRequest
  property_count: 6
  slug: moov-createtransferrequest
- name: Dispute
  property_count: 10
  slug: moov-dispute
- name: DisputeEvidence
  property_count: 5
  slug: moov-disputeevidence
- name: DisputeEvidenceText
  property_count: 2
  slug: moov-disputeevidencetext
- name: Error
  property_count: 2
  slug: moov-error
- name: GovernmentID
  property_count: 2
  slug: moov-governmentid
- name: IndividualProfile
  property_count: 6
  slug: moov-individualprofile
- name: IndustryCodes
  property_count: 3
  slug: moov-industrycodes
- name: LinkBankAccountRequest
  property_count: 3
  slug: moov-linkbankaccountrequest
- name: LinkCardRequest
  property_count: 5
  slug: moov-linkcardrequest
- name: MicroDepositConfirmation
  property_count: 1
  slug: moov-microdepositconfirmation
- name: Name
  property_count: 4
  slug: moov-name
- name: PaymentLink
  property_count: 10
  slug: moov-paymentlink
- name: PaymentMethod
  property_count: 5
  slug: moov-paymentmethod
- name: PaymentMethodOption
  property_count: 3
  slug: moov-paymentmethodoption
- name: Phone
  property_count: 2
  slug: moov-phone
- name: Refund
  property_count: 5
  slug: moov-refund
- name: Representative
  property_count: 11
  slug: moov-representative
- name: RepresentativeResponsibilities
  property_count: 4
  slug: moov-representativeresponsibilities
- name: RequestCapabilitiesRequest
  property_count: 1
  slug: moov-requestcapabilitiesrequest
- name: RevokeTokenRequest
  property_count: 1
  slug: moov-revoketokenrequest
- name: SsnOrItin
  property_count: 2
  slug: moov-ssnoritin
- name: Sweep
  property_count: 7
  slug: moov-sweep
- name: SweepConfig
  property_count: 8
  slug: moov-sweepconfig
- name: TaxID
  property_count: 1
  slug: moov-taxid
- name: TokenRequest
  property_count: 4
  slug: moov-tokenrequest
- name: TosToken
  property_count: 2
  slug: moov-tostoken
- name: Moov Transfer
  property_count: 13
  slug: moov-transfer
- name: TransferAccountRef
  property_count: 3
  slug: moov-transferaccountref
- name: TransferCancellation
  property_count: 3
  slug: moov-transfercancellation
- name: TransferOptions
  property_count: 2
  slug: moov-transferoptions
- name: TransferOptionsRequest
  property_count: 3
  slug: moov-transferoptionsrequest
- name: TransferParticipant
  property_count: 6
  slug: moov-transferparticipant
- name: UpdateAccountRequest
  property_count: 3
  slug: moov-updateaccountrequest
- name: UpdateCardRequest
  property_count: 3
  slug: moov-updatecardrequest
- name: UpdatePaymentLinkRequest
  property_count: 4
  slug: moov-updatepaymentlinkrequest
- name: UpdateRepresentativeRequest
  property_count: 7
  slug: moov-updaterepresentativerequest
- name: UpdateSweepConfigRequest
  property_count: 3
  slug: moov-updatesweepconfigrequest
- name: UpdateTransferRequest
  property_count: 1
  slug: moov-updatetransferrequest
- name: UpdateWalletRequest
  property_count: 1
  slug: moov-updatewalletrequest
- name: Wallet
  property_count: 4
  slug: moov-wallet
- name: WalletTransaction
  property_count: 9
  slug: moov-wallettransaction
json_structures:
- name: Moov Structure
  property_count: 0
  slug: moov-structure
jsonld:
- class_count: 0
  name: Moov Context
  property_count: 16
  slug: moov-context
layout: provider
modified: '2026-08-08'
name: Moov
nav: Providers
network: true
overview: 'Moov publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Bank Accounts API, and 10 more. Tagged areas include Banking, Embedded Finance, Financial Infrastructure, Money Movement, and Payments.


  The Moov catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Moov''s developer surface includes support, changelog, getting-started guide, authentication, developer portal, documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Moov Plans Pricing
  plan_count: 7
  slug: moov-plans-pricing
random_paper: 101
rate_limits:
- limit_count: 2
  name: Moov Rate Limits
  slug: moov-rate-limits
rules:
- name: Moov API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: moov-asyncapi-spectral-rules
- name: Moov API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: moov-jsonschema-spectral-rules
score:
  band: strong
  composite: 58.4
  delta: 7.3
  facets:
    commercial_clarity: 57.9
    contract_quality: 87.3
    developer_ergonomics: 45.7
    discoverability: 72.2
    governance: 41.7
    operational_transparency: 55.3
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/screenshots/moov-2026-08-07T184251.png
security:
- kind: authentication
  name: Moov Authentication
  slug: moov-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Moov Domain Security
  slug: moov-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Moov Trust Center
  slug: moov-trust-center
  summary_line: SOC 2
slug: moov
tags:
- Banking
- Embedded Finance
- Financial Infrastructure
- Money Movement
- Payments
- Transfers
website: https://moov.io/
---
