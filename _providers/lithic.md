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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 97
  human_in_the_loop: 1
  name: Lithic Agentic Access
  operation_count: 194
  slug: lithic-agentic-access
  summary_line: 194 operations · 97 acting · 1 human-in-the-loop
api_count: 31
apis:
- description: Real-time HTTP endpoint customers expose for Lithic to call synchronously during authorization for custom approve/decline logic.
  name: Lithic Auth Stream Access (ASA)
  slug: auth-stream
- description: Outbound HTTP webhook delivery for transaction, card, account-holder, dispute, and payment events.
  name: Lithic Webhooks
  slug: webhooks
- description: The 3DS API from Lithic — 6 operation(s) for 3ds.
  name: Lithic 3DS API
  slug: lithic-3ds-api
- description: The Account API from Lithic — 4 operation(s) for account.
  name: Lithic Account API
  slug: lithic-account-api
- description: The Account Holder API from Lithic — 8 operation(s) for account holder.
  name: Lithic Account Holder API
  slug: lithic-account-holder-api
- description: The Auth Rules API from Lithic — 10 operation(s) for auth rules.
  name: Lithic Auth Rules API
  slug: lithic-auth-rules-api
- description: The Auth Stream Access (ASA) API from Lithic — 2 operation(s) for auth stream access (asa).
  name: Lithic Auth Stream Access (ASA) API
  slug: lithic-auth-stream-access-asa-api
- description: The Balance API from Lithic — 2 operation(s) for balance.
  name: Lithic Balance API
  slug: lithic-balance-api
- description: The Book Transfer API from Lithic — 5 operation(s) for book transfer.
  name: Lithic Book Transfer API
  slug: lithic-book-transfer-api
- description: The Card API from Lithic — 16 operation(s) for card.
  name: Lithic Card API
  slug: lithic-card-api
- description: The Card Bulk Orders API from Lithic — 2 operation(s) for card bulk orders.
  name: Lithic Card Bulk Orders API
  slug: lithic-card-bulk-orders-api
- description: The Chargeback API from Lithic — 4 operation(s) for chargeback.
  name: Lithic Chargeback API
  slug: lithic-chargeback-api
- description: The Credit Product API from Lithic — 2 operation(s) for credit product.
  name: Lithic Credit Product API
  slug: lithic-credit-product-api
- description: The Event API from Lithic — 12 operation(s) for event.
  name: Lithic Event API
  slug: lithic-event-api
- description: The External Bank Account API from Lithic — 7 operation(s) for external bank account.
  name: Lithic External Bank Account API
  slug: lithic-external-bank-account-api
- description: The External Payments API from Lithic — 6 operation(s) for external payments.
  name: Lithic External Payments API
  slug: lithic-external-payments-api
- description: The Financial Account API from Lithic — 9 operation(s) for financial account.
  name: Lithic Financial Account API
  slug: lithic-financial-account-api
- description: The Fraud Report API from Lithic — 1 operation(s) for fraud report.
  name: Lithic Fraud Report API
  slug: lithic-fraud-report-api
- description: The Funding Events API from Lithic — 3 operation(s) for funding events.
  name: Lithic Funding Events API
  slug: lithic-funding-events-api
- description: The Hold API from Lithic — 3 operation(s) for hold.
  name: Lithic Hold API
  slug: lithic-hold-api
- description: The Managed Disputes API from Lithic — 2 operation(s) for managed disputes.
  name: Lithic Managed Disputes API
  slug: lithic-managed-disputes-api
- description: The Management Operations API from Lithic — 3 operation(s) for management operations.
  name: Lithic Management Operations API
  slug: lithic-management-operations-api
- description: The Network Program API from Lithic — 2 operation(s) for network program.
  name: Lithic Network Program API
  slug: lithic-network-program-api
- description: The Payment API from Lithic — 8 operation(s) for payment.
  name: Lithic Payment API
  slug: lithic-payment-api
- description: The Responder Endpoints API from Lithic — 1 operation(s) for responder endpoints.
  name: Lithic Responder Endpoints API
  slug: lithic-responder-endpoints-api
- description: The Settlement Report API from Lithic — 4 operation(s) for settlement report.
  name: Lithic Settlement Report API
  slug: lithic-settlement-report-api
- description: The Statements API from Lithic — 8 operation(s) for statements.
  name: Lithic Statements API
  slug: lithic-statements-api
- description: The Status API from Lithic — 1 operation(s) for status.
  name: Lithic Status API
  slug: lithic-status-api
- description: The Tokenization API from Lithic — 13 operation(s) for tokenization.
  name: Lithic Tokenization API
  slug: lithic-tokenization-api
- description: The Transaction API from Lithic — 12 operation(s) for transaction.
  name: Lithic Transaction API
  slug: lithic-transaction-api
- description: The Transfer Limits API from Lithic — 1 operation(s) for transfer limits.
  name: Lithic Transfer Limits API
  slug: lithic-transfer-limits-api
artifact_total: 488
collections:
- collection_type: open
  name: Lithic Developer API
  slug: open-lithic
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lithic-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lithic-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lithic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lithic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lithic-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lithic-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lithic
- group: company
  title: ''
  type: Website
  url: https://lithic.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/lithic-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lithic-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lithic-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.lithic.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.lithic.com/blog
created: '2026-05-08'
description: Lithic is a modern card-issuing and program-management platform offering REST APIs for cards, accounts, transactions, authorization control, ACH/wire payments, external bank accounts, account-holder KYC/KYB, 3-D Secure, tokenization, disputes, and webhooks. OpenAPI spec is published via Stainless and powers official SDKs in Node, Python, Go, Java, Kotlin.
examples:
- key_count: 6
  name: Lithic Createeventsubscription Example
  slug: lithic-createeventsubscription-example
- key_count: 6
  name: Lithic Createexternalbankaccount Example
  slug: lithic-createexternalbankaccount-example
- key_count: 6
  name: Lithic Deleteaccountholderentity Example
  slug: lithic-deleteaccountholderentity-example
- key_count: 6
  name: Lithic Get V2Auth Rulesresults Example
  slug: lithic-get-v2auth-rulesresults-example
- key_count: 6
  name: Lithic Getaccountholder Example
  slug: lithic-getaccountholder-example
- key_count: 6
  name: Lithic Getaccountholders Example
  slug: lithic-getaccountholders-example
- key_count: 6
  name: Lithic Getaccounts Example
  slug: lithic-getaccounts-example
- key_count: 6
  name: Lithic Getembedcard Example
  slug: lithic-getembedcard-example
- key_count: 6
  name: Lithic Getenhancedtransactiondata Example
  slug: lithic-getenhancedtransactiondata-example
- key_count: 6
  name: Lithic Getevents Example
  slug: lithic-getevents-example
- key_count: 6
  name: Lithic Geteventsubscription Example
  slug: lithic-geteventsubscription-example
- key_count: 6
  name: Lithic Geteventsubscriptions Example
  slug: lithic-geteventsubscriptions-example
- key_count: 6
  name: Lithic Geteventsubscriptionsecret Example
  slug: lithic-geteventsubscriptionsecret-example
- key_count: 6
  name: Lithic Getnetworkprogram Example
  slug: lithic-getnetworkprogram-example
- key_count: 6
  name: Lithic Getsettlementdetails Example
  slug: lithic-getsettlementdetails-example
- key_count: 6
  name: Lithic Gettokenization Example
  slug: lithic-gettokenization-example
- key_count: 6
  name: Lithic Gettokenizations Example
  slug: lithic-gettokenizations-example
- key_count: 6
  name: Lithic Listenhancedtransactiondata Example
  slug: lithic-listenhancedtransactiondata-example
- key_count: 6
  name: Lithic Patchaccountbytoken Example
  slug: lithic-patchaccountbytoken-example
- key_count: 6
  name: Lithic Patchaccountholder Example
  slug: lithic-patchaccountholder-example
- key_count: 6
  name: Lithic Patchcardbulkorder Example
  slug: lithic-patchcardbulkorder-example
- key_count: 6
  name: Lithic Patchcardbytoken Example
  slug: lithic-patchcardbytoken-example
- key_count: 6
  name: Lithic Post V1Three Ds Decisioningsimulateenter Otp Example
  slug: lithic-post-v1three-ds-decisioningsimulateenter-otp-example
- key_count: 6
  name: Lithic Postaccountholderdocuments Example
  slug: lithic-postaccountholderdocuments-example
- key_count: 6
  name: Lithic Postaccountholderentities Example
  slug: lithic-postaccountholderentities-example
- key_count: 6
  name: Lithic Postaccountholders Example
  slug: lithic-postaccountholders-example
- key_count: 6
  name: Lithic Postcardbulkorder Example
  slug: lithic-postcardbulkorder-example
- key_count: 6
  name: Lithic Postcardprovision Example
  slug: lithic-postcardprovision-example
- key_count: 6
  name: Lithic Postcardreissue Example
  slug: lithic-postcardreissue-example
- key_count: 6
  name: Lithic Postcardrenew Example
  slug: lithic-postcardrenew-example
- key_count: 6
  name: Lithic Postcards Example
  slug: lithic-postcards-example
- key_count: 6
  name: Lithic Postcardwebprovision Example
  slug: lithic-postcardwebprovision-example
- key_count: 6
  name: Lithic Postconvertphysical Example
  slug: lithic-postconvertphysical-example
- key_count: 6
  name: Lithic Postdisputes Example
  slug: lithic-postdisputes-example
- key_count: 6
  name: Lithic Postsimulateauthentication Example
  slug: lithic-postsimulateauthentication-example
- key_count: 6
  name: Lithic Postsimulateauthorizationadvice Example
  slug: lithic-postsimulateauthorizationadvice-example
- key_count: 6
  name: Lithic Postsimulateauthorize Example
  slug: lithic-postsimulateauthorize-example
- key_count: 6
  name: Lithic Postsimulateclearing Example
  slug: lithic-postsimulateclearing-example
- key_count: 6
  name: Lithic Postsimulatecreditauthorizationadvice Example
  slug: lithic-postsimulatecreditauthorizationadvice-example
- key_count: 6
  name: Lithic Postsimulatereturn Example
  slug: lithic-postsimulatereturn-example
- key_count: 6
  name: Lithic Postsimulatereturnreversal Example
  slug: lithic-postsimulatereturnreversal-example
- key_count: 6
  name: Lithic Postsimulatetokenizations Example
  slug: lithic-postsimulatetokenizations-example
- key_count: 6
  name: Lithic Postsimulatevoid Example
  slug: lithic-postsimulatevoid-example
- key_count: 6
  name: Lithic Resendactivationcodefortokenization Example
  slug: lithic-resendactivationcodefortokenization-example
- key_count: 6
  name: Lithic Searchcardbypan Example
  slug: lithic-searchcardbypan-example
- key_count: 6
  name: Lithic Simulateaccountholderenrollmentdocumentreview Example
  slug: lithic-simulateaccountholderenrollmentdocumentreview-example
- key_count: 6
  name: Lithic Simulateaccountholderenrollmentreview Example
  slug: lithic-simulateaccountholderenrollmentreview-example
- key_count: 6
  name: Lithic Updatedigitalcardartfortokenization Example
  slug: lithic-updatedigitalcardartfortokenization-example
- key_count: 6
  name: Lithic Updateeventsubscription Example
  slug: lithic-updateeventsubscription-example
finops:
- name: Lithic Finops
  service_category: FinTech
  slug: lithic-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Lithic card-issuing and program-management platform. Lithic provides a REST API; this schema represents the same domain expressed as GraphQL
  name: Lithic GraphQL Schema
  slug: lithic-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lithic.png
json_schemas:
- name: Account Financial Account Type
  property_count: 0
  slug: lithic-account-financial-account-type
- name: Account Holder Created
  property_count: 6
  slug: lithic-account-holder-created
- name: Account Holder Document Updated
  property_count: 6
  slug: lithic-account-holder-document-updated
- name: Account Holder
  property_count: 20
  slug: lithic-account-holder-response
- name: Account Holder Updated
  property_count: 0
  slug: lithic-account-holder-updated
- name: Account Holder Verification
  property_count: 5
  slug: lithic-account-holder-verification
- name: Account Standing
  property_count: 8
  slug: lithic-account-standing
- name: Account State
  property_count: 0
  slug: lithic-account-state
- name: Auth Rule Account Tokens
  property_count: 0
  slug: lithic-account-tokens
- name: Account Type External
  property_count: 0
  slug: lithic-account-type-external
- name: Searchable Account Type
  property_count: 0
  slug: lithic-account-type
- name: AccountConfiguration
  property_count: 10
  slug: lithic-accountconfiguration
- name: AccountHolder
  property_count: 20
  slug: lithic-accountholder
- name: AccountHolderBusinessResponse
  property_count: 7
  slug: lithic-accountholderbusinessresponse
- name: AccountHolderIndividualResponse
  property_count: 7
  slug: lithic-accountholderindividualresponse
- name: AccountHolderVerificationApplication
  property_count: 4
  slug: lithic-accountholderverificationapplication
- name: AccountSpendLimits
  property_count: 3
  slug: lithic-accountspendlimits
- name: ACH Action
  property_count: 0
  slug: lithic-ach-action
- name: AchMethodAttributes
  property_count: 9
  slug: lithic-achmethodattributes
- name: action_explanation
  property_count: 1
  slug: lithic-action-explanation
- name: Address Match Result
  property_count: 0
  slug: lithic-address-match-result
- name: Address
  property_count: 6
  slug: lithic-address-patch
- name: Address
  property_count: 6
  slug: lithic-address
- name: Amount Due
  property_count: 2
  slug: lithic-amount-due
- name: Amount
  property_count: 2
  slug: lithic-amount
- name: AmountTotals
  property_count: 3
  slug: lithic-amount-totals
- name: AppleWebPushProvisioningResponse
  property_count: 2
  slug: lithic-applewebpushprovisioningresponse
- name: asa_network_specific_data_mastercard
  property_count: 3
  slug: lithic-asa-network-specific-data-mastercard
- name: Network Specific Data
  property_count: 2
  slug: lithic-asa-network-specific-data
- name: asa_network_specific_data_visa
  property_count: 1
  slug: lithic-asa-network-specific-data-visa
- name: Point of Sale Terminal
  property_count: 8
  slug: lithic-asa-pos-terminal
- name: asa_request_card
  property_count: 7
  slug: lithic-asa-request-card
- name: Fleet Info
  property_count: 4
  slug: lithic-asa-request-fleet-info
- name: asa_request_pos_entry_mode
  property_count: 4
  slug: lithic-asa-request-pos-entry-mode
- name: asa-request
  property_count: 30
  slug: lithic-asa-request
- name: asa_request_status
  property_count: 0
  slug: lithic-asa-request-status
- name: asa-response
  property_count: 6
  slug: lithic-asa-response
- name: Auth Rule Feature State
  property_count: 2
  slug: lithic-auth-rule-feature-state
- name: Auth Rule Name
  property_count: 0
  slug: lithic-auth-rule-name
- name: Auth Rule Parameters
  property_count: 0
  slug: lithic-auth-rule-parameters
- name: Auth Rule Result
  property_count: 7
  slug: lithic-auth-rule-result
- name: Auth Rule
  property_count: 15
  slug: lithic-auth-rule
- name: Auth Rule State
  property_count: 0
  slug: lithic-auth-rule-state
- name: Auth Rule Token
  property_count: 0
  slug: lithic-auth-rule-token
- name: Auth Rule Types
  property_count: 0
  slug: lithic-auth-rule-type
- name: Auth Rule Version
  property_count: 0
  slug: lithic-auth-rule-version-id
- name: Auth Rule Version
  property_count: 4
  slug: lithic-auth-rule-version
- name: Auth Rule Version State
  property_count: 0
  slug: lithic-auth-rule-version-state
- name: Authentication (3DS) Action
  property_count: 0
  slug: lithic-authentication-3ds-action
- name: 3DS Authentication object
  property_count: 20
  slug: lithic-authentication
- name: Authorization Action
  property_count: 0
  slug: lithic-authorization-action
- name: Auto Collection Configuration Request
  property_count: 1
  slug: lithic-auto-collection-configuration-request
- name: Auto Collection Configuration Response
  property_count: 1
  slug: lithic-auto-collection-configuration-response
- name: Address Verification Service
  property_count: 2
  slug: lithic-avs
- name: Backtest List Item
  property_count: 4
  slug: lithic-backtest-list-item
- name: Auth Rules Backtest Report
  property_count: 0
  slug: lithic-backtest-report
- name: Backtest Request Parameters
  property_count: 2
  slug: lithic-backtest-request
- name: Auth Rules Backtest Results
  property_count: 3
  slug: lithic-backtest-results
- name: Backtest Simulation Parameters
  property_count: 2
  slug: lithic-backtest-simulation-parameters
- name: Auth Rule Backtest Statistics
  property_count: 5
  slug: lithic-backtest-stats
- name: Backtest Status
  property_count: 0
  slug: lithic-backtest-status
- name: Auth Rule Backtest Token
  property_count: 0
  slug: lithic-backtest-token
- name: Balance Details
  property_count: 2
  slug: lithic-balance-details
- name: balance
  property_count: 10
  slug: lithic-balance
- name: Balance Updated
  property_count: 1
  slug: lithic-balance-updated
- name: Balances
  property_count: 4
  slug: lithic-balances
- name: Bank Account Api Response
  property_count: 22
  slug: lithic-bank-account-api-response
- name: Bank Account Api Response
  property_count: 22
  slug: lithic-bank-account-api-response-unlinked
- name: Bank Accounts Api Response
  property_count: 2
  slug: lithic-bank-accounts-api-response
- name: Bank Verified Create Bank Account Api Request
  property_count: 17
  slug: lithic-bank-verified-create-bank-account-api-request
- name: Bank Verified Verification Methods
  property_count: 0
  slug: lithic-bank-verified-verification-method
- name: Transaction Response
  property_count: 0
  slug: lithic-base-transaction-response
- name: base_transaction
  property_count: 4
  slug: lithic-base-transaction
- name: Activity Response
  property_count: 2
  slug: lithic-base-transactions-response
- name: Book Transfer Category
  property_count: 0
  slug: lithic-book-transfer-category
- name: Book Transfer Detailed Results
  property_count: 0
  slug: lithic-book-transfer-detailed-results
- name: Book Transfer Event
  property_count: 8
  slug: lithic-book-transfer-event
- name: Book Transfer Transaction Created
  property_count: 0
  slug: lithic-book-transfer-transaction-created
- name: Book Transfer Transaction
  property_count: 0
  slug: lithic-book-transfer-transaction
- name: Book Transfer Transaction Updated
  property_count: 0
  slug: lithic-book-transfer-transaction-updated
- name: Book Transfer Type
  property_count: 0
  slug: lithic-book-transfer-type
- name: Bulk Order Response
  property_count: 8
  slug: lithic-bulk-order-response
- name: Auth Rule Business Account Tokens
  property_count: 0
  slug: lithic-business-account-tokens
- name: BusinessEntity
  property_count: 6
  slug: lithic-businessentity
- name: Card Authorization Challenge Response
  property_count: 8
  slug: lithic-card-authorization-challenge-response
- name: Card Converted
  property_count: 1
  slug: lithic-card-converted
- name: Card Created
  property_count: 2
  slug: lithic-card-created
- name: Card Reissued
  property_count: 1
  slug: lithic-card-reissued
- name: Card Renewed
  property_count: 5
  slug: lithic-card-renewed
- name: Card Shipped
  property_count: 4
  slug: lithic-card-shipped
- name: Auth Rule Card Tokens
  property_count: 0
  slug: lithic-card-tokens
- name: Card Transaction Enhanced Data Created
  property_count: 0
  slug: lithic-card-transaction-enhanced-data-created
- name: Card Transaction Enhanced Data Updated
  property_count: 0
  slug: lithic-card-transaction-enhanced-data-updated
- name: Card Transaction
  property_count: 28
  slug: lithic-card-transaction
- name: Card Transaction Status Filter
  property_count: 0
  slug: lithic-card-transaction-status-filter
- name: Card Transaction Update Action
  property_count: 0
  slug: lithic-card-transaction-update-action
- name: card-type
  property_count: 0
  slug: lithic-card-type
- name: Card Updated
  property_count: 3
  slug: lithic-card-updated
- name: Cardholder Authentication
  property_count: 5
  slug: lithic-cardholder-authentication
- name: Cardholder Liability Event Data
  property_count: 4
  slug: lithic-cardholder-liability-event-data
- name: CardProgram
  property_count: 8
  slug: lithic-cardprogram
- name: CardSpendLimits
  property_count: 3
  slug: lithic-cardspendlimits
- name: Carrier
  property_count: 1
  slug: lithic-carrier
- name: Category Balances
  property_count: 3
  slug: lithic-category-balances
- name: Category Details
  property_count: 3
  slug: lithic-category-details
- name: Category Tier
  property_count: 2
  slug: lithic-category-tier
- name: 3DS Challenge webhook event
  property_count: 3
  slug: lithic-challenge-event
- name: Challenge Response object
  property_count: 2
  slug: lithic-challenge-response
- name: Challenge Response Unprocessable
  property_count: 1
  slug: lithic-challenge-response-unprocessable
- name: 3DS Challenge object
  property_count: 4
  slug: lithic-challenge
- name: CommonData
  property_count: 5
  slug: lithic-common-data
- name: Conditional Action (3DS) Parameters
  property_count: 2
  slug: lithic-conditional-3ds-action-parameters
- name: Conditional Action (ACH) Parameters
  property_count: 2
  slug: lithic-conditional-ach-action-parameters
- name: Conditional Action (Authorization) Parameters
  property_count: 2
  slug: lithic-conditional-authorization-action-parameters
- name: Conditional Block Parameters
  property_count: 1
  slug: lithic-conditional-block-parameters
- name: Conditional Action (Card Transaction Update) Parameters
  property_count: 2
  slug: lithic-conditional-card-transaction-update-action-parameters
- name: Conditional Operation
  property_count: 0
  slug: lithic-conditional-operation
- name: Conditional Action (Tokenization) Parameters
  property_count: 2
  slug: lithic-conditional-tokenization-action-parameters
- name: Conditional Value
  property_count: 0
  slug: lithic-conditional-value
- name: Converted Amount
  property_count: 3
  slug: lithic-converted-amount
- name: Auth Rule Parameters
  property_count: 0
  slug: lithic-create-auth-rule-request
- name: Create Book Transfer Request
  property_count: 11
  slug: lithic-create-book-transfer-request
- name: Create Bulk Order Request
  property_count: 3
  slug: lithic-create-bulk-order-request
- name: Account Holder Entity Create Request
  property_count: 0
  slug: lithic-create-entity-request
- name: Account Holder Entity Create Response
  property_count: 6
  slug: lithic-create-entity-response
- name: Create External Bank Account Api Response Context
  property_count: 1
  slug: lithic-create-external-bank-account-error-response-context
- name: Create External Bank Account Api Response
  property_count: 3
  slug: lithic-create-external-bank-account-error-response
- name: Create External Payment Request
  property_count: 9
  slug: lithic-create-external-payment-request
- name: Create Hold Request
  property_count: 5
  slug: lithic-create-hold-request
- name: Create Management Operation Request
  property_count: 11
  slug: lithic-create-management-operation-request
- name: CreateFinancialAccountRequest
  property_count: 4
  slug: lithic-createfinancialaccountrequest
- name: CreatePaymentRequest
  property_count: 10
  slug: lithic-createpaymentrequest
- name: Credit Details
  property_count: 0
  slug: lithic-credit-details
- name: Currency
  property_count: 0
  slug: lithic-currency
- name: Auth Rule Current Version
  property_count: 0
  slug: lithic-current-version
- name: customer-tokenization-decision
  property_count: 4
  slug: lithic-customer-tokenization-decision
- name: Debit Details
  property_count: 0
  slug: lithic-debit-details
- name: Result of the transaction
  property_count: 0
  slug: lithic-decline-result
- name: Detailed Result
  property_count: 0
  slug: lithic-detailed-result
- name: Detailed Results
  property_count: 0
  slug: lithic-detailed-results
- name: device
  property_count: 3
  slug: lithic-device
- name: digital-wallet-token-metadata
  property_count: 5
  slug: lithic-digital-wallet-token-metadata
- name: digital-wallet-tokenization-approval-request
  property_count: 0
  slug: lithic-digital-wallet-tokenization-approval-request
- name: Digital Wallet Tokenization Result
  property_count: 5
  slug: lithic-digital-wallet-tokenization-result
- name: Digital Wallet Tokenization Two Factor Authentication Code Sent
  property_count: 5
  slug: lithic-digital-wallet-tokenization-two-factor-authentication-code-s
- name: Digital Wallet Tokenization Two Factor Authentication Code
  property_count: 6
  slug: lithic-digital-wallet-tokenization-two-factor-authentication-code
- name: Digital Wallet Tokenization Updated
  property_count: 4
  slug: lithic-digital-wallet-tokenization-updated
- name: DigitalCardArt
  property_count: 7
  slug: lithic-digitalcardart
- name: Directional Limits
  property_count: 2
  slug: lithic-directional-limits
- name: Dispute Evidence
  property_count: 7
  slug: lithic-dispute-evidence
- name: Dispute Evidence Upload Failed
  property_count: 0
  slug: lithic-dispute-evidence-upload-failed
- name: Dispute
  property_count: 14
  slug: lithic-dispute
- name: Dispute Updated
  property_count: 0
  slug: lithic-dispute-updated
- name: Dispute
  property_count: 18
  slug: lithic-dispute-v1
- name: Disputes Response
  property_count: 2
  slug: lithic-disputes-response
- name: Account Holder KYC Document
  property_count: 5
  slug: lithic-document
- name: Account Holder document types
  property_count: 0
  slug: lithic-document-type
- name: Account holder document upload status reasons
  property_count: 0
  slug: lithic-document-upload-status-reasons
- name: Account holder document upload status
  property_count: 0
  slug: lithic-document-upload-status
- name: Auth Rule Draft Version
  property_count: 0
  slug: lithic-draft-version
- name: EnhancedData
  property_count: 5
  slug: lithic-enhanced-data
- name: EnhancedDataListResponse
  property_count: 1
  slug: lithic-enhanceddatalistresponse
- name: Account Holder Entity
  property_count: 10
  slug: lithic-entity-response
- name: Account Holder Entity Status
  property_count: 0
  slug: lithic-entity-status
- name: Account Holder Entity Type
  property_count: 0
  slug: lithic-entity-type
- name: error
  property_count: 2
  slug: lithic-error
- name: Event
  property_count: 4
  slug: lithic-event
- name: Event Stream Types
  property_count: 0
  slug: lithic-event-stream
- name: event_type
  property_count: 0
  slug: lithic-event-type
- name: EventSubscription
  property_count: 5
  slug: lithic-eventsubscription
- name: Auth Rule Excluded Account Tokens
  property_count: 0
  slug: lithic-excluded-account-tokens
- name: Auth Rule Excluded Business Account Tokens
  property_count: 0
  slug: lithic-excluded-business-account-tokens
- name: Auth Rule Excluded Card Tokens
  property_count: 0
  slug: lithic-excluded-card-tokens
- name: Extended Credit
  property_count: 1
  slug: lithic-extended-credit
- name: External Bank Account Address
  property_count: 6
  slug: lithic-external-bank-account-address
- name: External Payment Action Request
  property_count: 2
  slug: lithic-external-payment-action-request
- name: External Payment Action with Progress to Request
  property_count: 3
  slug: lithic-external-payment-action-with-progress-to-request
- name: External Payment Category
  property_count: 0
  slug: lithic-external-payment-category
- name: External Payment Direction
  property_count: 0
  slug: lithic-external-payment-direction
- name: External Payment Event
  property_count: 8
  slug: lithic-external-payment-event
- name: External Payment Event Type
  property_count: 0
  slug: lithic-external-payment-event-type
- name: External Payment Progress To
  property_count: 0
  slug: lithic-external-payment-progress-to
- name: External Payment Response
  property_count: 0
  slug: lithic-external-payment-response
- name: External Payments Response
  property_count: 2
  slug: lithic-external-payments-response
- name: ExternalResource
  property_count: 3
  slug: lithic-external-resource
- name: ExternalResourceType
  property_count: 0
  slug: lithic-external-resource-type
- name: Externally Verified Create Bank Account Api Request
  property_count: 15
  slug: lithic-externally-verified-create-bank-account-api-request
- name: Externally Verified Verification Methods
  property_count: 0
  slug: lithic-externally-verified-verification-method
- name: Financial Account Balance
  property_count: 10
  slug: lithic-financial-account-balance
- name: Financial Account Credit Configuration Request
  property_count: 5
  slug: lithic-financial-account-credit-config-request
- name: Financial Account Credit Configuration Response
  property_count: 6
  slug: lithic-financial-account-credit-config-response
- name: Financial Account Credit Config
  property_count: 5
  slug: lithic-financial-account-credit-config
- name: Financial Account Response
  property_count: 13
  slug: lithic-financial-account-response
- name: Financial Account State
  property_count: 2
  slug: lithic-financial-account-state
- name: Financial Account Status
  property_count: 0
  slug: lithic-financial-account-status
- name: Financial Account Substatus
  property_count: 0
  slug: lithic-financial-account-substatus
- name: financial-account-transaction
  property_count: 11
  slug: lithic-financial-account-transaction
- name: Financial Accounts Response
  property_count: 2
  slug: lithic-financial-accounts-response
- name: Financial Event Data
  property_count: 4
  slug: lithic-financial-event-data
- name: Financial Event
  property_count: 5
  slug: lithic-financial-event
- name: Financial Event Type
  property_count: 0
  slug: lithic-financial-event-type
- name: Financial Transaction
  property_count: 0
  slug: lithic-financial-transaction
- name: Fleet
  property_count: 6
  slug: lithic-fleet
- name: Fraud Report Parameters
  property_count: 3
  slug: lithic-fraud-report-request
- name: Fraud Report Response
  property_count: 6
  slug: lithic-fraud-report-response
- name: FuelData
  property_count: 4
  slug: lithic-fuel-data
- name: FuelType
  property_count: 0
  slug: lithic-fuel-type
- name: FuelUnitOfMeasure
  property_count: 0
  slug: lithic-fuel-unit-of-measure
- name: funding_account
  property_count: 7
  slug: lithic-funding-account
- name: Funding Event Details Response
  property_count: 3
  slug: lithic-funding-event-details-response
- name: Funding Event Response
  property_count: 8
  slug: lithic-funding-event-response
- name: Funding Event Responses
  property_count: 2
  slug: lithic-funding-event-responses
- name: Funding Event Settlement
  property_count: 2
  slug: lithic-funding-event-settlement
- name: Funding Event Webhook
  property_count: 1
  slug: lithic-funding-events-created-webhook
- name: GoogleWebPushProvisioningResponse
  property_count: 2
  slug: lithic-googlewebpushprovisioningresponse
- name: Hold Event
  property_count: 8
  slug: lithic-hold-event
- name: Hold Event Type
  property_count: 0
  slug: lithic-hold-event-type
- name: Hold Status
  property_count: 0
  slug: lithic-hold-status
- name: Hold Transaction
  property_count: 0
  slug: lithic-hold-transaction
- name: Holds Response
  property_count: 2
  slug: lithic-holds-response
- name: Individual
  property_count: 8
  slug: lithic-individual-patch
- name: Individual
  property_count: 7
  slug: lithic-individual
- name: Instance Financial Account Type
  property_count: 0
  slug: lithic-instance-financial-account-type
- name: Interest Calculation method
  property_count: 0
  slug: lithic-interest-calculation-method
- name: Interest Details
  property_count: 7
  slug: lithic-interest-details
- name: Interest Rate
  property_count: 2
  slug: lithic-interest-rate
- name: Internal Adjustment Event
  property_count: 5
  slug: lithic-internal-adjustment-event
- name: Internal Adjustment Transaction
  property_count: 11
  slug: lithic-internal-adjustment-transaction
- name: KYB Business Entity
  property_count: 7
  slug: lithic-kyb-business-entity-patch
- name: KYB Business Entity
  property_count: 6
  slug: lithic-kyb-business-entity
- name: KYB Individual
  property_count: 0
  slug: lithic-kyb-individual-patch
- name: Business/Individual Patch Response
  property_count: 20
  slug: lithic-kyb-kyc-patch-response
- name: Business Patch Request
  property_count: 7
  slug: lithic-kyb-patch-request
- name: Kyb
  property_count: 10
  slug: lithic-kyb
- name: KybDelegated
  property_count: 9
  slug: lithic-kybdelegated
- name: KybDelegatedBusinessEntity
  property_count: 6
  slug: lithic-kybdelegatedbusinessentity
- name: KybDelegatedIndividual
  property_count: 0
  slug: lithic-kybdelegatedindividual
- name: KybIndividual
  property_count: 0
  slug: lithic-kybindividual
- name: Individuals associated with a KYC application.
  property_count: 0
  slug: lithic-kyc-individual-patch
- name: Individual Patch Request
  property_count: 2
  slug: lithic-kyc-patch-request
- name: Kyc
  property_count: 5
  slug: lithic-kyc
- name: KycExempt
  property_count: 9
  slug: lithic-kycexempt
- name: KycIndividual
  property_count: 0
  slug: lithic-kycindividual
- name: Liability Allocation
  property_count: 5
  slug: lithic-liability-allocation
- name: Limit With Progress
  property_count: 2
  slug: lithic-limit-with-progress
- name: LineItem
  property_count: 4
  slug: lithic-line-item
- name: List Transactions Response
  property_count: 2
  slug: lithic-list-transactions-response
- name: Loan Tape Configuration
  property_count: 7
  slug: lithic-loan-tape-configuration
- name: Loan Tape Rebuild Configuration
  property_count: 3
  slug: lithic-loan-tape-rebuild-configuration
- name: Loan Tape Response
  property_count: 22
  slug: lithic-loan-tape-response
- name: Loan Tapes Response
  property_count: 2
  slug: lithic-loan-tapes-response
- name: Management Operation Action Request
  property_count: 2
  slug: lithic-management-operation-action-request
- name: Management Operation Category
  property_count: 0
  slug: lithic-management-operation-category
- name: Management Operation Direction
  property_count: 0
  slug: lithic-management-operation-direction
- name: Management Operation Event
  property_count: 9
  slug: lithic-management-operation-event
- name: Management Operation Event Type
  property_count: 0
  slug: lithic-management-operation-event-type
- name: Management Operation Transaction
  property_count: 0
  slug: lithic-management-operation-transaction
- name: Management Operation Transactions Response
  property_count: 2
  slug: lithic-management-operation-transactions-response
- name: Mastercard Network Specific Data
  property_count: 3
  slug: lithic-mastercard-network-specific-data
- name: Merchant Currency
  property_count: 0
  slug: lithic-merchant-currency
- name: Merchant Lock Inputs
  property_count: 1
  slug: lithic-merchant-lock-parameters
- name: Merchant
  property_count: 7
  slug: lithic-merchant
- name: MessageAttempt
  property_count: 8
  slug: lithic-messageattempt
- name: Micro Deposit Verification Request
  property_count: 1
  slug: lithic-micro-deposit-verification-request
- name: Network Information
  property_count: 4
  slug: lithic-network-info
- name: Network Risk Score
  property_count: 0
  slug: lithic-network-risk-score
- name: Network Specific Data
  property_count: 2
  slug: lithic-network-specific-data
- name: Network Total
  property_count: 12
  slug: lithic-network-total
- name: Network Totals Response
  property_count: 2
  slug: lithic-network-totals-list
- name: NetworkProgram
  property_count: 4
  slug: lithic-networkprogram
- name: non_pci_card_response
  property_count: 25
  slug: lithic-non-pci-card-response
- name: On Closed Account
  property_count: 0
  slug: lithic-on-closed-account
- name: Owner Type
  property_count: 0
  slug: lithic-owner-type
- name: Auth Rule Patch Request
  property_count: 2
  slug: lithic-patch-auth-rule-request
- name: Legacy Patch Request
  property_count: 7
  slug: lithic-patch-request
- name: Legacy Patch Response
  property_count: 8
  slug: lithic-patch-response
- name: Payment Allocation
  property_count: 6
  slug: lithic-payment-allocation
- name: Payment Details
  property_count: 0
  slug: lithic-payment-details
- name: Payment Event
  property_count: 7
  slug: lithic-payment-event
- name: Payment Event Type
  property_count: 0
  slug: lithic-payment-event-type
- name: Payment Return Request
  property_count: 5
  slug: lithic-payment-return-request
- name: Payment Transaction Created
  property_count: 0
  slug: lithic-payment-transaction-created
- name: Payment Transaction
  property_count: 0
  slug: lithic-payment-transaction
- name: Payment Transaction Updated
  property_count: 0
  slug: lithic-payment-transaction-updated
- name: PaymentMethodRequestAttributes
  property_count: 4
  slug: lithic-paymentmethodrequestattributes
- name: Payoff Details
  property_count: 5
  slug: lithic-payoff-details
- name: pci_card_response
  property_count: 0
  slug: lithic-pci-card-response
- name: Auth Rule Performance Report V2
  property_count: 4
  slug: lithic-performance-report-v2
- name: Period State
  property_count: 0
  slug: lithic-period-state
- name: Point of Sale Entry Mode
  property_count: 4
  slug: lithic-pos-entry-mode
- name: Point of Sale
  property_count: 2
  slug: lithic-pos
- name: Point of Sale Terminal
  property_count: 8
  slug: lithic-pos-terminal
- name: PostPaymentResponse
  property_count: 0
  slug: lithic-postpaymentresponse
- name: Prime Rates Response
  property_count: 2
  slug: lithic-prime-rates-response
- name: Auth Rule Program Level Parameter
  property_count: 0
  slug: lithic-program-level
- name: Register Account Number Request
  property_count: 1
  slug: lithic-register-account-number-request
- name: Related Account Tokens
  property_count: 2
  slug: lithic-related-account-tokens
- name: Auth Rule Version Report Statistics
  property_count: 4
  slug: lithic-report-stats-v2
- name: Account Holder Required Document
  property_count: 3
  slug: lithic-required-document
- name: Authentication (3DS) Action (Result)
  property_count: 1
  slug: lithic-result-authentication-3ds-action
- name: Authorization Action (Result)
  property_count: 0
  slug: lithic-result-authorization-action
- name: Result
  property_count: 0
  slug: lithic-result
- name: Retry Book Transfer Request
  property_count: 1
  slug: lithic-retry-book-transfer-request
- name: Retry Micro Deposit Verification Request
  property_count: 1
  slug: lithic-retry-micro-deposit-verification-request
- name: Retry Prenote Verification Request
  property_count: 1
  slug: lithic-retry-prenote-verification-request
- name: Rule Feature
  property_count: 0
  slug: lithic-rule-feature
- name: Detailed Rule Result
  property_count: 4
  slug: lithic-rule-result
- name: Service Location
  property_count: 5
  slug: lithic-service-location
- name: FuelServiceType
  property_count: 0
  slug: lithic-service-type
- name: Set Verification Method Allowed Verification Methods
  property_count: 0
  slug: lithic-set-verification-method-allowed-verification-methods
- name: Set Verification Method Request
  property_count: 2
  slug: lithic-set-verification-method-request
- name: Settlement Report
  property_count: 11
  slug: lithic-settlement-report
- name: settlement Summary Details
  property_count: 8
  slug: lithic-settlement-summary-details
- name: SettlementDetail
  property_count: 21
  slug: lithic-settlementdetail
- name: ShippingAddress
  property_count: 11
  slug: lithic-shippingaddress
- name: Signals Response
  property_count: 31
  slug: lithic-signals-response
- name: Simulate Action Request
  property_count: 5
  slug: lithic-simulate-action-request
- name: 3DS Simulation Request object
  property_count: 4
  slug: lithic-simulate-authentication-request
- name: Simulate account holder enrollment document review request body
  property_count: 4
  slug: lithic-simulate-enrollment-document-review-request
- name: Simulate account holder enrollment review request body
  property_count: 3
  slug: lithic-simulate-enrollment-review-request
- name: Simulate Origination Release Request
  property_count: 1
  slug: lithic-simulate-origination-release-request
- name: Simulate Origination Return Request
  property_count: 2
  slug: lithic-simulate-origination-return-request
- name: Simulate Payment Response
  property_count: 3
  slug: lithic-simulate-payment-response
- name: Simulate Receipt Request
  property_count: 5
  slug: lithic-simulate-receipt-request
- name: Spend Feature State
  property_count: 4
  slug: lithic-spend-feature-state
- name: spend_limit_duration
  property_count: 0
  slug: lithic-spend-limit-duration
- name: Spend Velocity Filters
  property_count: 0
  slug: lithic-spend-velocity-filters
- name: Statement Line Item Response
  property_count: 14
  slug: lithic-statement-line-item-response
- name: Statement Line Items Response
  property_count: 2
  slug: lithic-statement-line-items-response
- name: Statement Response
  property_count: 23
  slug: lithic-statement-response
- name: Statement Totals
  property_count: 11
  slug: lithic-statement-totals
- name: Statement Type
  property_count: 0
  slug: lithic-statement-type
- name: Statement Webhook
  property_count: 1
  slug: lithic-statements-created-webhook
- name: Statements Response
  property_count: 2
  slug: lithic-statements-response
- name: KYC/KYB Status Reasons
  property_count: 0
  slug: lithic-status-reasons
- name: KYC/KYB Status
  property_count: 0
  slug: lithic-status
- name: Supported Simulation Decline Reasons
  property_count: 0
  slug: lithic-supported-simulation-decline-reasons
- name: Supported Simulation Types
  property_count: 0
  slug: lithic-supported-simulation-types
- name: Tags
  property_count: 0
  slug: lithic-tags
- name: TaxData
  property_count: 3
  slug: lithic-tax-data
- name: TaxExemptIndicator
  property_count: 0
  slug: lithic-tax-exempt-indicator
- name: 3DS Decision Response object
  property_count: 2
  slug: lithic-three-ds-decisioning
- name: Tier Schedule Entry
  property_count: 5
  slug: lithic-tier-schedule-entry
- name: Tier Schedule Response
  property_count: 2
  slug: lithic-tier-schedule-response
- name: Token Info
  property_count: 1
  slug: lithic-token-info
- name: Tokenization Action
  property_count: 0
  slug: lithic-tokenization-action
- name: tokenization-approval-request
  property_count: 0
  slug: lithic-tokenization-approval-request
- name: tokenization-decisioning-response
  property_count: 4
  slug: lithic-tokenization-decisioning-response
- name: Tokenization Decline Reason
  property_count: 0
  slug: lithic-tokenization-decline-reason
- name: Tokenization Event Outcome
  property_count: 0
  slug: lithic-tokenization-event-outcome
- name: Tokenization Event
  property_count: 7
  slug: lithic-tokenization-event
- name: tokenization-request-base
  property_count: 9
  slug: lithic-tokenization-request-base
- name: Tokenization Result
  property_count: 5
  slug: lithic-tokenization-result
- name: Tokenization Rule Result
  property_count: 4
  slug: lithic-tokenization-rule-result
- name: Tokenization
  property_count: 14
  slug: lithic-tokenization
- name: Tokenization TFA Reason
  property_count: 0
  slug: lithic-tokenization-tfa-reason
- name: Tokenization Two Factor Authentication Code
  property_count: 6
  slug: lithic-tokenization-two-factor-authentication-code
- name: Tokenization Two Factor Authentication Code Sent
  property_count: 5
  slug: lithic-tokenization-two-factor-authentication-code-sent
- name: Tokenization Updated
  property_count: 4
  slug: lithic-tokenization-updated
- name: Transaction Amounts
  property_count: 4
  slug: lithic-transaction-amounts
- name: Transaction Category
  property_count: 0
  slug: lithic-transaction-category
- name: Transaction Event Amounts
  property_count: 3
  slug: lithic-transaction-event-amounts
- name: Transaction Event
  property_count: 12
  slug: lithic-transaction-event
- name: Transaction Merchant
  property_count: 0
  slug: lithic-transaction-merchant
- name: Transaction Result
  property_count: 0
  slug: lithic-transaction-result
- name: Transaction Series
  property_count: 3
  slug: lithic-transaction-series
- name: Transaction Status
  property_count: 0
  slug: lithic-transaction-status
- name: Transfer Limit Item
  property_count: 6
  slug: lithic-transfer-limit-item
- name: Transfer Limits Response
  property_count: 2
  slug: lithic-transfer-limits-response
- name: Transfer
  property_count: 13
  slug: lithic-transfer
- name: Transfer Type
  property_count: 0
  slug: lithic-transfer-type
- name: TypeScript Code Parameters
  property_count: 2
  slug: lithic-typescript-code-parameters
- name: Unverified Create Bank Account Api Request
  property_count: 15
  slug: lithic-unverified-create-bank-account-api-request
- name: Unverified Verification Methods
  property_count: 0
  slug: lithic-unverified-verification-method
- name: Update Bank Account Api Request
  property_count: 9
  slug: lithic-update-bank-account-api-request
- name: Update Bulk Order Request
  property_count: 1
  slug: lithic-update-bulk-order-request
- name: Update financial account status request
  property_count: 3
  slug: lithic-update-financial-account-status-request
- name: Update Financial Account Substatus
  property_count: 0
  slug: lithic-update-financial-account-substatus
- name: Update Tier Schedule Entry Request
  property_count: 3
  slug: lithic-update-tier-schedule-entry-request
- name: UpdateFinancialAccountRequest
  property_count: 1
  slug: lithic-updatefinancialaccountrequest
- name: Velocity Limits Filters
  property_count: 5
  slug: lithic-velocity-limit-filters
- name: Velocity Limit Parameters
  property_count: 5
  slug: lithic-velocity-limit-parameters
- name: Velocity Limit Period
  property_count: 0
  slug: lithic-velocity-limit-period
- name: Velocity Limits Scope
  property_count: 0
  slug: lithic-velocity-scope
- name: Verification Application
  property_count: 5
  slug: lithic-verification-application
- name: Verification Method
  property_count: 0
  slug: lithic-verification-method
- name: Verification State
  property_count: 0
  slug: lithic-verification-state
- name: Visa Network Specific Data
  property_count: 1
  slug: lithic-visa-network-specific-data
- name: Void Hold Request
  property_count: 1
  slug: lithic-void-hold-request
- name: wallet-decisioning-info
  property_count: 4
  slug: lithic-wallet-decisioning-info
- name: WebPushProvisioningResponse
  property_count: 0
  slug: lithic-webpushprovisioningresponse
- name: WebPushProvisioningResponseHeader
  property_count: 1
  slug: lithic-webpushprovisioningresponseheader
- name: WebPushProvisioningResponseJws
  property_count: 4
  slug: lithic-webpushprovisioningresponsejws
- name: Wire Party Details
  property_count: 4
  slug: lithic-wire-party-details
- name: WireMethodAttributes
  property_count: 6
  slug: lithic-wiremethodattributes
- name: Workflow Event Data
  property_count: 6
  slug: lithic-workflow-event-data
json_structures:
- name: Lithic Structure
  property_count: 0
  slug: lithic-structure
layout: provider
modified: '2026-05-08'
name: Lithic
nav: Providers
network: true
overview: 'Lithic publishes 29 APIs on the [APIs.io](https://apis.io/) network, including 3DS API, Account API, Account Holder API, and 26 more. Tagged areas include FinTech, BaaS, Card Issuing, Payments, and Embedded Finance.


  The Lithic catalog on APIs.io includes 1 Spectral governance ruleset.


  Lithic''s developer surface includes authentication, engineering blog, and 11 more developer resources.'
plans:
- name: Lithic Plans Pricing
  plan_count: 3
  slug: lithic-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 2
  name: Lithic Rate Limits
  slug: lithic-rate-limits
rules:
- name: Lithic API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: lithic-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: -4.7
  facets:
    commercial_clarity: 47.4
    contract_quality: 65.9
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 49.5
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
    regime: Payments
    regime_id: payments
    score: 35.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lithic/refs/heads/main/screenshots/lithic-2026-06-20T184605.png
security:
- kind: authentication
  name: Lithic Authentication
  slug: lithic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lithic Domain Security
  slug: lithic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lithic Vulnerability Disclosure
  slug: lithic-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Lithic Trust Center
  slug: lithic-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: lithic
tags:
- FinTech
- BaaS
- Card Issuing
- Payments
- Embedded Finance
website: https://lithic.com/
---
