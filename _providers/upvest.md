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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Upvest Agentic Access
  operation_count: 70
  slug: upvest-agentic-access
  summary_line: 70 operations · 27 acting
api_count: 35
apis:
- description: Transfer accounts between entities.
  name: Upvest Account Transfers API
  slug: upvest-account-transfers-api
- description: Investment accounts that hold positions and track balances for users.
  name: Upvest Accounts API
  slug: upvest-accounts-api
- description: OAuth 2.0 token management for API access using client credentials flow.
  name: Upvest Authentication API
  slug: upvest-authentication-api
- description: View cash balance information for accounts.
  name: Upvest Cash Balances API
  slug: upvest-cash-balances-api
- description: View and manage corporate action events on held securities.
  name: Upvest Corporate Actions API
  slug: upvest-corporate-actions-api
- description: Manage direct debit funding operations.
  name: Upvest Direct Debits API
  slug: upvest-direct-debits-api
- description: Track order execution details and fills.
  name: Upvest Executions API
  slug: upvest-executions-api
- description: Configure fee structures and schedules.
  name: Upvest Fee Configurations API
  slug: upvest-fee-configurations-api
- description: Track and manage fee charges on accounts.
  name: Upvest Fees API
  slug: upvest-fees-api
- description: Access and download generated files such as reports and statements.
  name: Upvest Files API
  slug: upvest-files-api
- description: Retrieve real-time and historical price data for instruments.
  name: Upvest Instrument Prices API
  slug: upvest-instrument-prices-api
- description: Query available financial instruments and their metadata.
  name: Upvest Instruments API
  slug: upvest-instruments-api
- description: Manage full or partial account liquidations.
  name: Upvest Liquidations API
  slug: upvest-liquidations-api
- description: Manage direct debit mandates for accounts.
  name: Upvest Mandates API
  slug: upvest-mandates-api
- description: Cancel pending orders before execution.
  name: Upvest Order Cancellations API
  slug: upvest-order-cancellations-api
- description: Place, manage, and track buy and sell orders for instruments.
  name: Upvest Orders API
  slug: upvest-orders-api
- description: Define and update target allocations within portfolios.
  name: Upvest Portfolio Allocations API
  slug: upvest-portfolio-allocations-api
- description: Place orders against portfolio allocations.
  name: Upvest Portfolio Orders API
  slug: upvest-portfolio-orders-api
- description: Create and manage portfolios with custom asset allocations.
  name: Upvest Portfolios API
  slug: upvest-portfolios-api
- description: Trigger and track portfolio rebalancing operations.
  name: Upvest Portfolios Rebalancing API
  slug: upvest-portfolios-rebalancing-api
- description: View current holdings and position details for accounts.
  name: Upvest Positions API
  slug: upvest-positions-api
- description: Manage reference bank accounts linked to investment accounts.
  name: Upvest Reference Accounts API
  slug: upvest-reference-accounts-api
- description: Generate and retrieve user-facing investment reports and statements.
  name: Upvest Reports API
  slug: upvest-reports-api
- description: Calculate account-level investment returns.
  name: Upvest Returns API
  slug: upvest-returns-api
- description: Configure automated recurring investments into portfolios or instruments.
  name: Upvest Savings Plans API
  slug: upvest-savings-plans-api
- description: Transfer securities between accounts or providers.
  name: Upvest Securities Transfers API
  slug: upvest-securities-transfers-api
- description: Manage tax residency information for users.
  name: Upvest Tax Residencies API
  slug: upvest-tax-residencies-api
- description: View transaction history for accounts.
  name: Upvest Transactions API
  slug: upvest-transactions-api
- description: Access treasury-level reporting for institutional oversight.
  name: Upvest Treasury Reports API
  slug: upvest-treasury-reports-api
- description: Compliance and verification checks on users.
  name: Upvest User Checks API
  slug: upvest-user-checks-api
- description: Manage external identifiers associated with users.
  name: Upvest User Identifiers API
  slug: upvest-user-identifiers-api
- description: Manage end users including onboarding, identity verification, and profile management.
  name: Upvest Users API
  slug: upvest-users-api
- description: Retrieve account and position valuations.
  name: Upvest Valuations API
  slug: upvest-valuations-api
- description: Register, update, and manage webhook subscriptions for event notifications.
  name: Upvest Webhook Subscriptions API
  slug: upvest-webhook-subscriptions-api
- description: Process cash withdrawals from investment accounts.
  name: Upvest Withdrawals API
  slug: upvest-withdrawals-api
artifact_total: 277
asyncapis:
- description: The Upvest Investment API uses an asynchronous, event-driven architecture where events represent state changes within the system. Webhook subscriptions allow your application to receive real-time noti
  name: Upvest Investment Events
  slug: upvest-investment-events-asyncapi
collections:
- collection_type: postman
  name: Upvest Investment Account Transfers API
  slug: postman-upvest-account-transfers-api
- collection_type: postman
  name: Upvest Investment Account Transfers Accounts API
  slug: postman-upvest-accounts-api
- collection_type: postman
  name: Upvest Investment Account Transfers Authentication API
  slug: postman-upvest-authentication-api
- collection_type: postman
  name: Upvest Investment Account Transfers Cash Balances API
  slug: postman-upvest-cash-balances-api
- collection_type: postman
  name: Upvest Investment Account Transfers Corporate Actions API
  slug: postman-upvest-corporate-actions-api
- collection_type: postman
  name: Upvest Investment Account Transfers Direct Debits API
  slug: postman-upvest-direct-debits-api
- collection_type: postman
  name: Upvest Investment Account Transfers Executions API
  slug: postman-upvest-executions-api
- collection_type: postman
  name: Upvest Investment Account Transfers Fee Configurations API
  slug: postman-upvest-fee-configurations-api
- collection_type: postman
  name: Upvest Investment Account Transfers Fees API
  slug: postman-upvest-fees-api
- collection_type: postman
  name: Upvest Investment Account Transfers Files API
  slug: postman-upvest-files-api
- collection_type: postman
  name: Upvest Investment Account Transfers Instrument Prices API
  slug: postman-upvest-instrument-prices-api
- collection_type: postman
  name: Upvest Investment Account Transfers Instruments API
  slug: postman-upvest-instruments-api
- collection_type: postman
  name: Upvest Investment Account Transfers Liquidations API
  slug: postman-upvest-liquidations-api
- collection_type: postman
  name: Upvest Investment Account Transfers Mandates API
  slug: postman-upvest-mandates-api
- collection_type: postman
  name: Upvest Investment Account Transfers Order Cancellations API
  slug: postman-upvest-order-cancellations-api
- collection_type: postman
  name: Upvest Investment Account Transfers Orders API
  slug: postman-upvest-orders-api
- collection_type: postman
  name: Upvest Investment Account Transfers Portfolio Allocations API
  slug: postman-upvest-portfolio-allocations-api
- collection_type: postman
  name: Upvest Investment Account Transfers Portfolio Orders API
  slug: postman-upvest-portfolio-orders-api
- collection_type: postman
  name: Upvest Investment Account Transfers Portfolios API
  slug: postman-upvest-portfolios-api
- collection_type: postman
  name: Upvest Investment Account Transfers Portfolios Rebalancing API
  slug: postman-upvest-portfolios-rebalancing-api
- collection_type: postman
  name: Upvest Investment Account Transfers Positions API
  slug: postman-upvest-positions-api
- collection_type: postman
  name: Upvest Investment Account Transfers Reference Accounts API
  slug: postman-upvest-reference-accounts-api
- collection_type: postman
  name: Upvest Investment Account Transfers Reports API
  slug: postman-upvest-reports-api
- collection_type: postman
  name: Upvest Investment Account Transfers Returns API
  slug: postman-upvest-returns-api
- collection_type: postman
  name: Upvest Investment Account Transfers Savings Plans API
  slug: postman-upvest-savings-plans-api
- collection_type: postman
  name: Upvest Investment Account Transfers Securities Transfers API
  slug: postman-upvest-securities-transfers-api
- collection_type: postman
  name: Upvest Investment Account Transfers Tax Residencies API
  slug: postman-upvest-tax-residencies-api
- collection_type: postman
  name: Upvest Investment Account Transfers Transactions API
  slug: postman-upvest-transactions-api
- collection_type: postman
  name: Upvest Investment Account Transfers Treasury Reports API
  slug: postman-upvest-treasury-reports-api
- collection_type: postman
  name: Upvest Investment Account Transfers User Checks API
  slug: postman-upvest-user-checks-api
- collection_type: postman
  name: Upvest Investment Account Transfers User Identifiers API
  slug: postman-upvest-user-identifiers-api
- collection_type: postman
  name: Upvest Investment Account Transfers Users API
  slug: postman-upvest-users-api
- collection_type: postman
  name: Upvest Investment Account Transfers Valuations API
  slug: postman-upvest-valuations-api
- collection_type: postman
  name: Upvest Investment Account Transfers Webhook Subscriptions API
  slug: postman-upvest-webhook-subscriptions-api
- collection_type: postman
  name: Upvest Investment Account Transfers Withdrawals API
  slug: postman-upvest-withdrawals-api
- collection_type: open
  name: Upvest Investment API
  slug: open-upvest-investment-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/upvestco/httpsignature-proxy/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/upvest/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/upvest-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/upvest-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upvest-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upvest-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/upvest-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upvest
- group: company
  title: ''
  type: Website
  url: https://upvest.co/
- group: start
  title: ''
  type: Portal
  url: https://upvest.co/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.upvest.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.upvest.co/documentation/guides
- group: company
  title: ''
  type: Blog
  url: https://upvest.co/blog
- group: company
  title: Engineering Blog
  type: Blog
  url: https://engineering.upvest.co/
- group: start
  title: ''
  type: Signup
  url: https://upvest.co/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upvest.co/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upvestco
- group: build
  title: HTTP Signature Proxy CLI
  type: GitHubRepository
  url: https://github.com/upvestco/httpsignature-proxy
- group: build
  title: HTTP Signature Examples
  type: GitHubRepository
  url: https://github.com/upvestco/http-signature-examples
- group: build
  title: Documentation Assets
  type: GitHubRepository
  url: https://github.com/upvestco/documentation_assets
- group: design
  title: ''
  type: JSONLD
  url: json-ld/upvest-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/upvest-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/upvest-vocabulary.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.upvest.co/llms.txt
created: '2026-03-24'
description: Upvest is a Berlin-based API-first investment infrastructure provider that enables banks, brokers, and wealth managers to build and launch investment experiences through a single modular API. Founded in 2017, Upvest is a regulated securities institution in Europe and the UK, covering trading, custody, and back-office operations. The platform supports fractional investing, portfolios, savings plans, roundups, and direct debit, enabling clients like Bunq, DKB, N26, Revolut, and Raisin to offer investment products to their customers.
examples:
- key_count: 3
  name: Investment Api Account Create Example
  slug: investment-api-account-create-example
- key_count: 7
  name: Investment Api Account Example
  slug: investment-api-account-example
- key_count: 6
  name: Investment Api Account Return Example
  slug: investment-api-account-return-example
- key_count: 2
  name: Investment Api Account Transfer Create Example
  slug: investment-api-account-transfer-create-example
- key_count: 3
  name: Investment Api Account Transfer Example
  slug: investment-api-account-transfer-example
- key_count: 1
  name: Investment Api Account Update Example
  slug: investment-api-account-update-example
- key_count: 6
  name: Investment Api Address Example
  slug: investment-api-address-example
- key_count: 5
  name: Investment Api Cash Balance Example
  slug: investment-api-cash-balance-example
- key_count: 7
  name: Investment Api Corporate Action Example
  slug: investment-api-corporate-action-example
- key_count: 6
  name: Investment Api Direct Debit Create Example
  slug: investment-api-direct-debit-create-example
- key_count: 9
  name: Investment Api Direct Debit Example
  slug: investment-api-direct-debit-example
- key_count: 3
  name: Investment Api Exchange Example
  slug: investment-api-exchange-example
- key_count: 6
  name: Investment Api Execution Example
  slug: investment-api-execution-example
- key_count: 5
  name: Investment Api Fee Configuration Example
  slug: investment-api-fee-configuration-example
- key_count: 6
  name: Investment Api Fee Example
  slug: investment-api-fee-example
- key_count: 9
  name: Investment Api Instrument Example
  slug: investment-api-instrument-example
- key_count: 5
  name: Investment Api Instrument Price Example
  slug: investment-api-instrument-price-example
- key_count: 1
  name: Investment Api Liquidation Create Example
  slug: investment-api-liquidation-create-example
- key_count: 5
  name: Investment Api Liquidation Example
  slug: investment-api-liquidation-example
- key_count: 5
  name: Investment Api Mandate Example
  slug: investment-api-mandate-example
- key_count: 4
  name: Investment Api Order Cancellation Example
  slug: investment-api-order-cancellation-example
- key_count: 9
  name: Investment Api Order Create Example
  slug: investment-api-order-create-example
- key_count: 14
  name: Investment Api Order Example
  slug: investment-api-order-example
- key_count: 2
  name: Investment Api Portfolio Allocation Create Example
  slug: investment-api-portfolio-allocation-create-example
- key_count: 2
  name: Investment Api Portfolio Allocation Example
  slug: investment-api-portfolio-allocation-example
- key_count: 3
  name: Investment Api Portfolio Create Example
  slug: investment-api-portfolio-create-example
- key_count: 6
  name: Investment Api Portfolio Example
  slug: investment-api-portfolio-example
- key_count: 2
  name: Investment Api Portfolio Order Create Example
  slug: investment-api-portfolio-order-create-example
- key_count: 6
  name: Investment Api Portfolio Order Example
  slug: investment-api-portfolio-order-example
- key_count: 1
  name: Investment Api Portfolio Update Example
  slug: investment-api-portfolio-update-example
- key_count: 8
  name: Investment Api Position Example
  slug: investment-api-position-example
- key_count: 4
  name: Investment Api Rebalancing Execution Example
  slug: investment-api-rebalancing-execution-example
- key_count: 5
  name: Investment Api Reference Account Example
  slug: investment-api-reference-account-example
- key_count: 5
  name: Investment Api Report Example
  slug: investment-api-report-example
- key_count: 6
  name: Investment Api Savings Plan Create Example
  slug: investment-api-savings-plan-create-example
- key_count: 11
  name: Investment Api Savings Plan Example
  slug: investment-api-savings-plan-example
- key_count: 3
  name: Investment Api Savings Plan Update Example
  slug: investment-api-savings-plan-update-example
- key_count: 1
  name: Investment Api Securities Transfer Create Example
  slug: investment-api-securities-transfer-create-example
- key_count: 4
  name: Investment Api Securities Transfer Example
  slug: investment-api-securities-transfer-example
- key_count: 2
  name: Investment Api Tax Residency Create Example
  slug: investment-api-tax-residency-create-example
- key_count: 4
  name: Investment Api Tax Residency Example
  slug: investment-api-tax-residency-example
- key_count: 6
  name: Investment Api Transaction Example
  slug: investment-api-transaction-example
- key_count: 4
  name: Investment Api Treasury Report Example
  slug: investment-api-treasury-report-example
- key_count: 5
  name: Investment Api User Check Example
  slug: investment-api-user-check-example
- key_count: 6
  name: Investment Api User Create Example
  slug: investment-api-user-create-example
- key_count: 10
  name: Investment Api User Example
  slug: investment-api-user-example
- key_count: 2
  name: Investment Api User Identifier Create Example
  slug: investment-api-user-identifier-create-example
- key_count: 4
  name: Investment Api User Identifier Example
  slug: investment-api-user-identifier-example
- key_count: 1
  name: Investment Api User Identifier Update Example
  slug: investment-api-user-identifier-update-example
- key_count: 4
  name: Investment Api User Update Example
  slug: investment-api-user-update-example
- key_count: 5
  name: Investment Api Valuation Example
  slug: investment-api-valuation-example
- key_count: 2
  name: Investment Api Webhook Subscription Create Example
  slug: investment-api-webhook-subscription-create-example
- key_count: 5
  name: Investment Api Webhook Subscription Example
  slug: investment-api-webhook-subscription-example
- key_count: 3
  name: Investment Api Webhook Subscription Update Example
  slug: investment-api-webhook-subscription-update-example
- key_count: 3
  name: Investment Api Withdrawal Create Example
  slug: investment-api-withdrawal-create-example
- key_count: 6
  name: Investment Api Withdrawal Example
  slug: investment-api-withdrawal-example
- key_count: 9
  name: Upvest Order Example
  slug: upvest-order-example
- key_count: 1
  name: Upvest Webhook Event Example
  slug: upvest-webhook-event-example
features:
- description: Enable customers to invest in stocks and ETFs starting at 1 EUR with fractional share support.
  name: Fractional Investing
- description: Build customized portfolios of stocks, ETFs, and upcoming crypto assets with automated rebalancing.
  name: Portfolio Management
- description: Configure recurring automated investment plans with direct debit integration.
  name: Savings Plans
- description: Micro-investing through spending-based roundups that automatically invest spare change.
  name: Roundups
- description: Enable customers to open investment accounts in seconds through the API.
  name: Instant Account Creation
- description: Regulated custody services with digital reports and securities safeguarding.
  name: Custody Management
- description: Track and manage cash balances across multiple currencies with virtual bank accounts.
  name: Multi-Currency Cash Management
- description: Automated tax wrapper support including ISA, tax exemptions, and compliance reporting.
  name: Tax and Compliance
- description: Real-time asynchronous event notifications for orders, payments, accounts, and compliance events.
  name: Webhook Events
- description: Full-featured sandbox at sandbox.upvest.co for testing with simulated bank transactions.
  name: Sandbox Environment
finops:
- name: Upvest Finops
  service_category: API
  slug: upvest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upvest.png
integrations:
- description: Localhost proxy for handling HTTP request signing required by the Upvest Investment API.
  name: HTTP Signature Proxy
- description: Automated recurring payment integration for savings plans and top-ups.
  name: Direct Debit
- description: Event-driven integration pattern via Upvest webhook subscriptions for real-time processing.
  name: Webhook Integration
- description: Client credentials flow for API authentication and token management.
  name: OAuth 2.0
json_schemas:
- name: AccountCreate
  property_count: 3
  slug: investment-api-account-create
- name: AccountReturn
  property_count: 6
  slug: investment-api-account-return
- name: Account
  property_count: 7
  slug: investment-api-account
- name: AccountTransferCreate
  property_count: 2
  slug: investment-api-account-transfer-create
- name: AccountTransfer
  property_count: 3
  slug: investment-api-account-transfer
- name: AccountUpdate
  property_count: 1
  slug: investment-api-account-update
- name: Address
  property_count: 6
  slug: investment-api-address
- name: CashBalance
  property_count: 5
  slug: investment-api-cash-balance
- name: CorporateAction
  property_count: 7
  slug: investment-api-corporate-action
- name: DirectDebitCreate
  property_count: 6
  slug: investment-api-direct-debit-create
- name: DirectDebit
  property_count: 9
  slug: investment-api-direct-debit
- name: Exchange
  property_count: 3
  slug: investment-api-exchange
- name: Execution
  property_count: 6
  slug: investment-api-execution
- name: FeeConfiguration
  property_count: 5
  slug: investment-api-fee-configuration
- name: Fee
  property_count: 6
  slug: investment-api-fee
- name: InstrumentPrice
  property_count: 5
  slug: investment-api-instrument-price
- name: Instrument
  property_count: 9
  slug: investment-api-instrument
- name: LiquidationCreate
  property_count: 1
  slug: investment-api-liquidation-create
- name: Liquidation
  property_count: 5
  slug: investment-api-liquidation
- name: Mandate
  property_count: 5
  slug: investment-api-mandate
- name: OrderCancellation
  property_count: 4
  slug: investment-api-order-cancellation
- name: OrderCreate
  property_count: 9
  slug: investment-api-order-create
- name: Order
  property_count: 14
  slug: investment-api-order
- name: PortfolioAllocationCreate
  property_count: 2
  slug: investment-api-portfolio-allocation-create
- name: PortfolioAllocation
  property_count: 2
  slug: investment-api-portfolio-allocation
- name: PortfolioCreate
  property_count: 3
  slug: investment-api-portfolio-create
- name: PortfolioOrderCreate
  property_count: 2
  slug: investment-api-portfolio-order-create
- name: PortfolioOrder
  property_count: 6
  slug: investment-api-portfolio-order
- name: Portfolio
  property_count: 6
  slug: investment-api-portfolio
- name: PortfolioUpdate
  property_count: 1
  slug: investment-api-portfolio-update
- name: Position
  property_count: 8
  slug: investment-api-position
- name: RebalancingExecution
  property_count: 4
  slug: investment-api-rebalancing-execution
- name: ReferenceAccount
  property_count: 5
  slug: investment-api-reference-account
- name: Report
  property_count: 5
  slug: investment-api-report
- name: SavingsPlanCreate
  property_count: 6
  slug: investment-api-savings-plan-create
- name: SavingsPlan
  property_count: 11
  slug: investment-api-savings-plan
- name: SavingsPlanUpdate
  property_count: 3
  slug: investment-api-savings-plan-update
- name: SecuritiesTransferCreate
  property_count: 1
  slug: investment-api-securities-transfer-create
- name: SecuritiesTransfer
  property_count: 4
  slug: investment-api-securities-transfer
- name: TaxResidencyCreate
  property_count: 2
  slug: investment-api-tax-residency-create
- name: TaxResidency
  property_count: 4
  slug: investment-api-tax-residency
- name: Transaction
  property_count: 6
  slug: investment-api-transaction
- name: TreasuryReport
  property_count: 4
  slug: investment-api-treasury-report
- name: UserCheck
  property_count: 5
  slug: investment-api-user-check
- name: UserCreate
  property_count: 6
  slug: investment-api-user-create
- name: UserIdentifierCreate
  property_count: 2
  slug: investment-api-user-identifier-create
- name: UserIdentifier
  property_count: 4
  slug: investment-api-user-identifier
- name: UserIdentifierUpdate
  property_count: 1
  slug: investment-api-user-identifier-update
- name: User
  property_count: 10
  slug: investment-api-user
- name: UserUpdate
  property_count: 4
  slug: investment-api-user-update
- name: Valuation
  property_count: 5
  slug: investment-api-valuation
- name: WebhookSubscriptionCreate
  property_count: 2
  slug: investment-api-webhook-subscription-create
- name: WebhookSubscription
  property_count: 5
  slug: investment-api-webhook-subscription
- name: WebhookSubscriptionUpdate
  property_count: 3
  slug: investment-api-webhook-subscription-update
- name: WithdrawalCreate
  property_count: 3
  slug: investment-api-withdrawal-create
- name: Withdrawal
  property_count: 6
  slug: investment-api-withdrawal
- name: Upvest Order
  property_count: 9
  slug: upvest-order
- name: Upvest Webhook Event
  property_count: 1
  slug: upvest-webhook-event
json_structures:
- name: Investment Api Account Create Structure
  property_count: 3
  slug: investment-api-account-create-structure
- name: Investment Api Account Return Structure
  property_count: 6
  slug: investment-api-account-return-structure
- name: Investment Api Account Structure
  property_count: 7
  slug: investment-api-account-structure
- name: Investment Api Account Transfer Create Structure
  property_count: 2
  slug: investment-api-account-transfer-create-structure
- name: Investment Api Account Transfer Structure
  property_count: 3
  slug: investment-api-account-transfer-structure
- name: Investment Api Account Update Structure
  property_count: 1
  slug: investment-api-account-update-structure
- name: Investment Api Address Structure
  property_count: 6
  slug: investment-api-address-structure
- name: Investment Api Cash Balance Structure
  property_count: 5
  slug: investment-api-cash-balance-structure
- name: Investment Api Corporate Action Structure
  property_count: 7
  slug: investment-api-corporate-action-structure
- name: Investment Api Direct Debit Create Structure
  property_count: 6
  slug: investment-api-direct-debit-create-structure
- name: Investment Api Direct Debit Structure
  property_count: 9
  slug: investment-api-direct-debit-structure
- name: Investment Api Exchange Structure
  property_count: 3
  slug: investment-api-exchange-structure
- name: Investment Api Execution Structure
  property_count: 6
  slug: investment-api-execution-structure
- name: Investment Api Fee Configuration Structure
  property_count: 5
  slug: investment-api-fee-configuration-structure
- name: Investment Api Fee Structure
  property_count: 6
  slug: investment-api-fee-structure
- name: Investment Api Instrument Price Structure
  property_count: 5
  slug: investment-api-instrument-price-structure
- name: Investment Api Instrument Structure
  property_count: 9
  slug: investment-api-instrument-structure
- name: Investment Api Liquidation Create Structure
  property_count: 1
  slug: investment-api-liquidation-create-structure
- name: Investment Api Liquidation Structure
  property_count: 5
  slug: investment-api-liquidation-structure
- name: Investment Api Mandate Structure
  property_count: 5
  slug: investment-api-mandate-structure
- name: Investment Api Order Cancellation Structure
  property_count: 4
  slug: investment-api-order-cancellation-structure
- name: Investment Api Order Create Structure
  property_count: 9
  slug: investment-api-order-create-structure
- name: Investment Api Order Structure
  property_count: 14
  slug: investment-api-order-structure
- name: Investment Api Portfolio Allocation Create Structure
  property_count: 2
  slug: investment-api-portfolio-allocation-create-structure
- name: Investment Api Portfolio Allocation Structure
  property_count: 2
  slug: investment-api-portfolio-allocation-structure
- name: Investment Api Portfolio Create Structure
  property_count: 3
  slug: investment-api-portfolio-create-structure
- name: Investment Api Portfolio Order Create Structure
  property_count: 2
  slug: investment-api-portfolio-order-create-structure
- name: Investment Api Portfolio Order Structure
  property_count: 6
  slug: investment-api-portfolio-order-structure
- name: Investment Api Portfolio Structure
  property_count: 6
  slug: investment-api-portfolio-structure
- name: Investment Api Portfolio Update Structure
  property_count: 1
  slug: investment-api-portfolio-update-structure
- name: Investment Api Position Structure
  property_count: 8
  slug: investment-api-position-structure
- name: Investment Api Rebalancing Execution Structure
  property_count: 4
  slug: investment-api-rebalancing-execution-structure
- name: Investment Api Reference Account Structure
  property_count: 5
  slug: investment-api-reference-account-structure
- name: Investment Api Report Structure
  property_count: 5
  slug: investment-api-report-structure
- name: Investment Api Savings Plan Create Structure
  property_count: 6
  slug: investment-api-savings-plan-create-structure
- name: Investment Api Savings Plan Structure
  property_count: 11
  slug: investment-api-savings-plan-structure
- name: Investment Api Savings Plan Update Structure
  property_count: 3
  slug: investment-api-savings-plan-update-structure
- name: Investment Api Securities Transfer Create Structure
  property_count: 1
  slug: investment-api-securities-transfer-create-structure
- name: Investment Api Securities Transfer Structure
  property_count: 4
  slug: investment-api-securities-transfer-structure
- name: Investment Api Tax Residency Create Structure
  property_count: 2
  slug: investment-api-tax-residency-create-structure
- name: Investment Api Tax Residency Structure
  property_count: 4
  slug: investment-api-tax-residency-structure
- name: Investment Api Transaction Structure
  property_count: 6
  slug: investment-api-transaction-structure
- name: Investment Api Treasury Report Structure
  property_count: 4
  slug: investment-api-treasury-report-structure
- name: Investment Api User Check Structure
  property_count: 5
  slug: investment-api-user-check-structure
- name: Investment Api User Create Structure
  property_count: 6
  slug: investment-api-user-create-structure
- name: Investment Api User Identifier Create Structure
  property_count: 2
  slug: investment-api-user-identifier-create-structure
- name: Investment Api User Identifier Structure
  property_count: 4
  slug: investment-api-user-identifier-structure
- name: Investment Api User Identifier Update Structure
  property_count: 1
  slug: investment-api-user-identifier-update-structure
- name: Investment Api User Structure
  property_count: 10
  slug: investment-api-user-structure
- name: Investment Api User Update Structure
  property_count: 4
  slug: investment-api-user-update-structure
- name: Investment Api Valuation Structure
  property_count: 5
  slug: investment-api-valuation-structure
- name: Investment Api Webhook Subscription Create Structure
  property_count: 2
  slug: investment-api-webhook-subscription-create-structure
- name: Investment Api Webhook Subscription Structure
  property_count: 5
  slug: investment-api-webhook-subscription-structure
- name: Investment Api Webhook Subscription Update Structure
  property_count: 3
  slug: investment-api-webhook-subscription-update-structure
- name: Investment Api Withdrawal Create Structure
  property_count: 3
  slug: investment-api-withdrawal-create-structure
- name: Investment Api Withdrawal Structure
  property_count: 6
  slug: investment-api-withdrawal-structure
- name: Upvest Order Structure
  property_count: 9
  slug: upvest-order-structure
- name: Upvest Webhook Event Structure
  property_count: 1
  slug: upvest-webhook-event-structure
jsonld:
- class_count: 63
  name: Upvest Context
  property_count: 68
  slug: upvest-context
layout: provider
modified: '2026-05-19'
name: Upvest
nav: Providers
network: true
overview: 'Upvest publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Account Transfers API, Accounts API, Authentication API, and 32 more. Tagged areas include Banking Infrastructure, Fintech, Investments, Securities, and Fractional Investing.


  The Upvest catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Upvest''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Upvest Plans Pricing
  plan_count: 3
  slug: upvest-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 5
  name: Upvest Rate Limits
  slug: upvest-rate-limits
rules:
- name: Upvest API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: upvest-asyncapi-spectral-rules
- name: Upvest API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: upvest-jsonschema-spectral-rules
- name: Upvest API Rules
  rule_count: 45
  severity_counts:
    error: 17
    hint: 0
    info: 3
    warn: 25
  slug: upvest-spectral-rules
scopes:
- name: Upvest Scopes
  scope_count: 18
  slug: upvest-scopes
  summary_line: 18 scopes · clientCredentials
score:
  band: strong
  composite: 58.7
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 90.3
    developer_ergonomics: 45.7
    discoverability: 75.9
    governance: 52.1
    operational_transparency: 13.2
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 70.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/upvest/refs/heads/main/screenshots/upvest-2026-06-20T200511.png
security:
- kind: authentication
  name: Upvest Authentication
  slug: upvest-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Upvest Domain Security
  slug: upvest-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Upvest Trust Center
  slug: upvest-trust-center
  summary_line: ISO 27001, ISO 27017, PCI DSS, GDPR, FIPS 140
slug: upvest
tags:
- Banking Infrastructure
- Fintech
- Investments
- Securities
- Fractional Investing
- Custody
- Wealth Management
use_cases:
- description: Banks and fintechs embedding fractional stock and ETF trading into existing financial products.
  name: Embedded Brokerage
- description: Wealth managers building automated portfolio and savings plan products for retail clients.
  name: Digital Wealth Management
- description: Neobanks adding investment capabilities to checking and savings account offerings.
  name: Neobank Investment Features
- description: Third-party platforms building fully branded investment experiences using Upvest infrastructure.
  name: White-Label Investment Platform
- description: Platforms enabling micro-investing by rounding up purchases and investing the difference.
  name: Roundup Investing
website: https://upvest.co/
---
