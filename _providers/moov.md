---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 82
  human_in_the_loop: 8
  name: Moov Agentic Access
  operation_count: 189
  slug: moov-agentic-access
  summary_line: 189 operations · 82 acting · 8 human-in-the-loop
api_count: 4
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
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Create and manage Moov accounts representing individual or business legal entities. Accounts are the foundation for all money movement operations.
  name: Moov Accounts API
  slug: moov-accounts-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: OAuth2 access token creation and revocation for API authentication.
  name: Moov Authentication API
  slug: moov-authentication-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Link and manage bank accounts as funding sources for ACH and RTP transfers. Includes micro-deposit and instant verification flows.
  name: Moov Bank Accounts API
  slug: moov-bank-accounts-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Request and manage capabilities that enable specific financial operations on an account, such as send-funds or collect-funds.
  name: Moov Capabilities API
  slug: moov-capabilities-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Link and manage debit and credit cards as payment sources on Moov accounts.
  name: Moov Cards API
  slug: moov-cards-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Manage card payment disputes including evidence submission, acceptance, and lifecycle tracking for chargeback resolution.
  name: Moov Disputes API
  slug: moov-disputes-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Create and manage shareable payment links that allow customers to pay via card or bank account without custom code.
  name: Moov Payment Links API
  slug: moov-payment-links-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Retrieve the available payment methods on an account, including bank accounts, cards, and wallets, which can be used as transfer sources or destinations.
  name: Moov Payment Methods API
  slug: moov-payment-methods-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Create and retrieve refunds for completed card transfers, including full and partial refund support.
  name: Moov Refunds API
  slug: moov-refunds-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Manage business representatives associated with a Moov account for KYB compliance and ownership verification.
  name: Moov Representatives API
  slug: moov-representatives-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Configure automatic daily transfers from a Moov wallet to an external bank account on a set schedule using ACH or RTP rails.
  name: Moov Sweeps API
  slug: moov-sweeps-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Initiate and manage money movement between Moov accounts. Supports ACH, RTP, and card rails with full lifecycle tracking.
  name: Moov Transfers API
  slug: moov-transfers-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Create and manage Moov digital wallets that hold funds within the platform. Supports wallet transactions and balance adjustments.
  name: Moov Wallets API
  slug: moov-wallets-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Virtual spending cards, authorizations, and card transactions.
  name: Moov Card Issuing API
  slug: moov-card-issuing-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Financial institution lookup by routing number.
  name: Moov Institutions API
  slug: moov-institutions-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: Underwriting details used to enable card acquiring and higher-risk activity.
  name: Moov Underwriting API
  slug: moov-underwriting-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Account Terminal Applications API from Moov — 3 operation(s) for account terminal applications.
  name: Moov Account Terminal Applications API
  slug: moov-account-terminal-applications-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Adjustments API from Moov — 2 operation(s) for adjustments.
  name: Moov Adjustments API
  slug: moov-adjustments-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Apple pay API from Moov — 3 operation(s) for apple pay.
  name: Moov Apple pay API
  slug: moov-apple-pay-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Avatars API from Moov — 1 operation(s) for avatars.
  name: Moov Avatars API
  slug: moov-avatars-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Branding API from Moov — 1 operation(s) for branding.
  name: Moov Branding API
  slug: moov-branding-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The End to End Encryption API from Moov — 2 operation(s) for end to end encryption.
  name: Moov End to End Encryption API
  slug: moov-end-to-end-encryption-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Enriched address API from Moov — 1 operation(s) for enriched address.
  name: Moov Enriched address API
  slug: moov-enriched-address-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Enriched profile API from Moov — 1 operation(s) for enriched profile.
  name: Moov Enriched profile API
  slug: moov-enriched-profile-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Fee plans API from Moov — 9 operation(s) for fee plans.
  name: Moov Fee plans API
  slug: moov-fee-plans-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Files API from Moov — 2 operation(s) for files.
  name: Moov Files API
  slug: moov-files-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Images API from Moov — 4 operation(s) for images.
  name: Moov Images API
  slug: moov-images-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Industries API from Moov — 1 operation(s) for industries.
  name: Moov Industries API
  slug: moov-industries-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Issuing transactions API from Moov — 5 operation(s) for issuing transactions.
  name: Moov Issuing transactions API
  slug: moov-issuing-transactions-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Onboarding API from Moov — 2 operation(s) for onboarding.
  name: Moov Onboarding API
  slug: moov-onboarding-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Ping API from Moov — 1 operation(s) for ping.
  name: Moov Ping API
  slug: moov-ping-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Products API from Moov — 2 operation(s) for products.
  name: Moov Products API
  slug: moov-products-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Receipts API from Moov — 1 operation(s) for receipts.
  name: Moov Receipts API
  slug: moov-receipts-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Scheduling API from Moov — 3 operation(s) for scheduling.
  name: Moov Scheduling API
  slug: moov-scheduling-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Statements API from Moov — 2 operation(s) for statements.
  name: Moov Statements API
  slug: moov-statements-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Support API from Moov — 3 operation(s) for support.
  name: Moov Support API
  slug: moov-support-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Terminal Applications API from Moov — 3 operation(s) for terminal applications.
  name: Moov Terminal Applications API
  slug: moov-terminal-applications-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Wallet transactions API from Moov — 2 operation(s) for wallet transactions.
  name: Moov Wallet transactions API
  slug: moov-wallet-transactions-api
- baseURL: https://api.moov.io
  baseurl_source: declared
  description: The Webhooks API from Moov — 5 operation(s) for webhooks.
  name: Moov Webhooks API
  slug: moov-webhooks-api
artifact_total: 161
asyncapis:
- description: Moov delivers real-time event notifications to your application via webhooks when state changes occur on your platform. When an event occurs, Moov sends an HTTP POST request with a JSON payload to you
  name: Moov Webhooks
  slug: moov-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Moov Accounts API
  slug: open-moov-accounts-api
- collection_type: open
  name: Moov API
  slug: open-moov-api
- collection_type: open
  name: Moov Accounts Authentication API
  slug: open-moov-authentication-api
- collection_type: open
  name: Moov Accounts Bank Accounts API
  slug: open-moov-bank-accounts-api
- collection_type: open
  name: Moov Accounts Capabilities API
  slug: open-moov-capabilities-api
- collection_type: open
  name: Moov Accounts Card Issuing API
  slug: open-moov-card-issuing-api
- collection_type: open
  name: Moov Accounts Cards API
  slug: open-moov-cards-api
- collection_type: open
  name: Moov Accounts Disputes API
  slug: open-moov-disputes-api
- collection_type: open
  name: Moov Accounts Institutions API
  slug: open-moov-institutions-api
- collection_type: open
  name: Moov API
  slug: open-moov-io
- collection_type: open
  name: Moov Accounts Payment Links API
  slug: open-moov-payment-links-api
- collection_type: open
  name: Moov Accounts Payment Methods API
  slug: open-moov-payment-methods-api
- collection_type: open
  name: Moov Accounts Refunds API
  slug: open-moov-refunds-api
- collection_type: open
  name: Moov Accounts Representatives API
  slug: open-moov-representatives-api
- collection_type: open
  name: Moov Accounts Sweeps API
  slug: open-moov-sweeps-api
- collection_type: open
  name: Moov Accounts Transfers API
  slug: open-moov-transfers-api
- collection_type: open
  name: Moov Accounts Underwriting API
  slug: open-moov-underwriting-api
- collection_type: open
  name: Moov Accounts Wallets API
  slug: open-moov-wallets-api
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/rules/moov-rules.yml
  title: ''
  type: Spectral
  url: rules/moov-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/rules/moov-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/moov-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/rules/moov-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/moov-asyncapi-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/vocabulary/moov-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/moov-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/asyncapi/moov-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/moov-webhooks-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/data-model/moov-data-model.yml
  title: ''
  type: DataModel
  url: data-model/moov-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/changelog/moov-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/moov-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/conventions/moov-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/moov-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/conventions/moov-conventions.yml
  title: ''
  type: Conventions
  url: conventions/moov-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/sandbox/moov-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/moov-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.moov.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/scopes/moov-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/moov-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/lifecycle/moov-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/moov-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/errors/moov-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/moov-decline-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/errors/moov-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/moov-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/conformance/moov-conformance.yml
  title: ''
  type: Conformance
  url: conformance/moov-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/overlays/moov-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/moov-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/llms/moov-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/moov-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/mcp/moov-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/moov-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/well-known/moov-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/moov-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/hosts/moov-hosts.yml
  title: ''
  type: Hosts
  url: hosts/moov-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/integrations/moov-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/moov-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/vendors/moov-vendors.yml
  title: ''
  type: Vendors
  url: vendors/moov-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/packages/moov-packages.yml
  title: ''
  type: SDKs
  url: packages/moov-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/packages/moov-packages.yml
  title: ''
  type: Packages
  url: packages/moov-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://moov.io/news
- group: commercial
  title: ''
  type: Pricing
  url: https://moov.io/pricing/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/capabilities/moov-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/moov-capability-edges.yml
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
  url: https://moov.io/legal/website-terms-of-use
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moov.io/guides/quick-start
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/agentic-access/moov-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/moov-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/security/moov-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/moov-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/security/moov-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/moov-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/authentication/moov-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/plans/moov-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/moov-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/rate-limits/moov-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/moov-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/finops/moov-finops.yml
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
- has_sources: true
  method: generated
  name: Moov Finops
  primary_unit: ''
  service_category: Embedded Finance
  slug: moov-finops
  template: false
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
- name: CreatedTransfer
  property_count: 28
  slug: moov-created-transfer
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
- name: OnboardingInvite
  property_count: 14
  slug: moov-onboarding-invite
- name: PaymentLink
  property_count: 23
  slug: moov-payment-link
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
  property_count: 20
  slug: moov-wallet-transaction
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
mcp_servers:
- description: Remote MCP server at docs.moov.io over HTTP requiring an API key; 6 tools listed.
  name: Moov MCP Server
  slug: moov
modified: '2026-10-12'
name: Moov
nav: Providers
network: true
overview: 'Moov publishes 42 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Bank Accounts API, and 39 more. Tagged areas include Banking, Embedded Finance, Financial Infrastructure, Money Movement, and Payments.


  The Moov catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Moov''s developer surface includes changelog, sandbox, pricing, support, getting-started guide, authentication, developer portal, and 45 more developer resources.'
plans:
- name: Moov Plans Pricing
  plan_count: 29
  slug: moov-plans-pricing
- name: Moov Price Estimates
  plan_count: 0
  slug: moov-price-estimates
random_paper: 9
rate_limits:
- limit_count: 2
  name: Moov Rate Limits
  slug: moov-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Moov — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: moov-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Moov — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: moov-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Moov API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 3
    warn: 3
  slug: moov-rules
scopes:
- name: Moov Scopes
  scope_count: 27
  slug: moov-scopes
  summary_line: 27 scopes
score:
  band: exemplar
  composite: 74.4
  coverage:
    artifact_dirs: 36
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.8
  facets:
    access_clarity: 85.5
    contract_governance: 22.0
    contract_quality: 74.9
    developer_ergonomics: 73.2
    discoverability: 73.3
    operational_transparency: 68.4
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 37.0
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/moov/refs/heads/main/screenshots/moov-2026-08-07T184251.png
security:
- kind: authentication
  name: Moov Authentication
  slug: moov-authentication
  summary_line: http · 2 schemes
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
