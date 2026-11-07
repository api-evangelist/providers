---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 86
  human_in_the_loop: 3
  name: Token Io Agentic Access
  operation_count: 215
  slug: token-io-agentic-access
  summary_line: 215 operations · 86 acting · 3 human-in-the-loop
api_count: 4
apis:
- description: Official Token.io JavaScript SDK for Node.js and browser environments interacting with the Token System and Open Banking API.
  name: Token.io JavaScript SDK
  slug: javascript-sdk
- description: Official Token.io PHP SDK for interacting with the Token System and Open Banking API.
  name: Token.io PHP SDK
  slug: php-sdk
- description: Official Token.io C# / .NET SDK for the Open Banking API.
  name: Token.io C# SDK
  slug: csharp-sdk
- description: Official Token.io Objective-C SDK for iOS.
  name: Token.io Objective-C SDK
  slug: objc-sdk
- description: iOS webview SDK for embedding Token.io Hosted Payments pages in native iOS apps.
  name: Token.io iOS Webview SDK
  slug: ios-webview-sdk
- description: Android webview SDK for embedding Token.io Hosted Payments pages in native Android apps.
  name: Token.io Android Webview SDK
  slug: android-webview-sdk
- description: Java merchant checkout sample illustrating Token.io payment initiation flows.
  name: Merchant Sample (Java)
  slug: merchant-sample-java
- description: Simple JavaScript merchant checkout example for Token.io.
  name: Merchant Sample (JavaScript)
  slug: merchant-sample-js
- description: Sample implementation of the Token Bank Integration API in Java.
  name: Bank Sample (Java)
  slug: bank-sample-java
- description: Simple personal finance app illustrating Token.io's Access Tokens for AIS use cases.
  name: Personal Finance Management Sample (Java)
  slug: pfm-sample-java
- description: Hands-on workshop for integrating a merchant with Token Checkout.
  name: Merchant Integration Workshop
  slug: merchant-integration-workshop
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints allow you to create and manage an Account on File from bank account details. The Account on File can then be used in other API requests instead of sending the full account details.
  name: token-io Account on File API
  phrasing_intents:
  - id: CreateTokenizedAccount
    intent: Save bank account details as an Account on File
    question: Can I store a customer's bank details once and reference them later without resending?
  - id: GetTokenizedAccount
    intent: Retrieve a saved Account on File
    question: How can I look up the bank details behind a tokenizedAccountId?
  - id: DeleteTokenizedAccount
    intent: Delete a saved Account on File
    question: Can I remove a stored Account on File so it can no longer be used?
  phrasing_ops: 3
  slug: token-io-account-on-file-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints provide authorized access to an authenticated user's account information.
  name: token-io Accounts API
  phrasing_intents:
  - id: getAccountBalance
    intent: Return an account balance as the bank integration
    question: As a bank integrating with Token.io, what do I return when asked for an account balance?
  - id: getAccountTransactions
    intent: Return account transactions as the bank integration
    question: On the bank side, how are transactions for an account paged by limit and offset?
  - id: getAccountTransactionForId
    intent: Return one transaction as the bank integration
    question: As the bank, how do I answer a request for one transaction by its id?
  - id: getAccount
    intent: Return a bank account as the bank integration
    question: What does the bank integration return when a TPP retrieves one bank account?
  - id: deleteAccount
    intent: Unlink a bank account when the user disconnects
    question: What happens on the bank side when a user unlinks their account at a TPP?
  - id: GatewayService.GetAccounts
    intent: List all bank accounts shared under a consent
    question: Which bank accounts has a user shared with me through their account-information consent?
  - id: GatewayService.GetAccount
    intent: Get details for one consented bank account
    question: What details can I pull for a single bank account a user shared with me?
  - id: GatewayService.GetBalances
    intent: Get balances for several consented accounts
    question: Can I fetch balances for multiple linked bank accounts in a single request?
  phrasing_ops: 25
  slug: token-io-accounts-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints are for managing the public keys that are used for JWT authentication.
  name: token-io Authentication keys API
  phrasing_intents:
  - id: GatewayService.AddMemberKey
    intent: Register a public key for a member
    question: How do I upload a new public key so a member can authenticate API calls?
  - id: GatewayService.GetMemberKeys
    intent: List a member's public authentication keys
    question: Which public keys are registered for authenticating a member?
  - id: GatewayService.GetMemberKey
    intent: Get one of a member's public keys
    question: Can I fetch the details of one specific public key by its key id?
  - id: GatewayService.DeleteMemberKey
    intent: Delete a member's public key
    question: Can I remove a compromised public key from a member?
  phrasing_ops: 4
  slug: token-io-authentication-keys-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints filter and fetch the list of connected banks, get information on specific banks, and initiate authorization with user-selected banks using Payments v1.
  name: token-io Banks v1 API
  phrasing_intents:
  - id: GatewayService.GetBanks
    intent: Search connected banks (v1)
    question: Which banks can I connect to in a given country through Token.io?
  - id: GatewayService.GetBanksCountries
    intent: List countries that have connected banks (v1)
    question: Which countries have banks available through the v1 bank directory?
  phrasing_ops: 2
  slug: token-io-banks-v1-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: This endpoint filters and fetches the list of connected banks, gets information on specific banks, and initiates authorization with user-selected banks using Payments v2.
  name: token-io Banks v2 API
  phrasing_intents:
  - id: GetBanksv2
    intent: Search connected banks (v2)
    question: Which banks support single payments in the v2 bank directory?
  phrasing_ops: 1
  slug: token-io-banks-v2-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints allow you to create and manage payment links. Payment links are reusable or single-use payment URLs that can be shared with customers, supporting fixed or variable amounts, usage limit
  name: token-io Pay by Link API
  phrasing_intents:
  - id: CreatePaymentLink
    intent: Create a shareable payment link
    question: Can I create a payment URL to send to a customer instead of building a checkout?
  - id: ListPaymentLinks
    intent: List payment links with filters
    question: Which of my payment links are still active?
  - id: GetPaymentLink
    intent: Get a payment link and its usage
    question: How many times has a particular payment link been used?
  - id: DeactivatePaymentLink
    intent: Deactivate a payment link
    question: Can I stop a payment link from being used any more?
  phrasing_ops: 4
  slug: token-io-pay-by-link-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: Creates and initiates a single immediate payment or a future-dated payment. Also supports initiating a Variable Recurring Payment (VRP) using an existing VRP mandate that has been created and authoris
  name: token-io Payments v2 API
  phrasing_intents:
  - id: InitiatePayment
    intent: Initiate a payment with a bank
    question: How do I kick off a pay-by-bank payment for a customer?
  - id: GetPayments
    intent: List payments with filters
    question: Which of my payments were refunded or partially refunded?
  - id: GetPayment
    intent: Get a payment and check its next step
    question: What's the status of one payment and what should happen next?
  - id: ProvideEmbeddedFields
    intent: Provide embedded authentication fields for a payment
    question: A payment is in INITIATION_PENDING_EMBEDDED_AUTH; what do I send?
  - id: GetQrCode
    intent: Generate a QR code for data
    question: Can I generate a scannable QR code for a payment URL?
  phrasing_ops: 5
  slug: token-io-payments-v2-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints allow you to make payouts.
  name: token-io Payouts API
  phrasing_intents:
  - id: InitiatePayout
    intent: Send a payout
    question: How do I send money out to a customer or supplier?
  - id: GetPayouts
    intent: List payouts
    question: Which payouts have I sent in the last month?
  - id: GetPayout
    intent: Get a payout
    question: Has a specific payout been completed?
  phrasing_ops: 3
  slug: token-io-payouts-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints allow you to handle registration, posting, and retrieval of refunds associated with original transaction account information.
  name: token-io Refunds API
  phrasing_intents:
  - id: InitiateRefund
    intent: Refund a payment
    question: How do I refund a customer who paid by bank?
  - id: GetRefunds
    intent: List refunds
    question: Which refunds have I issued this month?
  - id: GetRefund
    intent: Get a refund
    question: What's the status of a specific refund?
  - id: GetTransferRefunds
    intent: List refunds for a transfer
    question: Which refunds were made against one original payment?
  - id: RefundRegister
    intent: Register a debtor account for refund processing
    question: Can I register the account refunds are paid from so I don't pass the debtor each time?
  - id: GetRefundRegistration
    intent: Get refund registration information
    question: What refund registration information do I have on file?
  - id: DeleteRefundRegistration
    intent: Delete refund registration information
    question: Can I delete a refund registration I set up?
  - id: GenerateRefundSigningPayload
    intent: Build the payload to sign for a refund
    question: Which payload do I need to sign before submitting a refund?
  phrasing_ops: 10
  slug: token-io-refunds-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints retrieve the current AIS and PIS status of connected banks.
  name: token-io Reports API
  phrasing_intents:
  - id: GatewayService.GetBanksStatus
    intent: Get service status for all banks
    question: Are any banks currently having AIS or PIS outages?
  - id: GatewayService.GetBankStatus
    intent: Get service status for one bank
    question: Is a particular bank's payment service up right now?
  phrasing_ops: 2
  slug: token-io-reports-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints allow you to initiate a Payments v1 request or an AIS request, and retrieve the status of the request.
  name: token-io Requests - for Payments v1 or AIS API
  phrasing_intents:
  - id: GatewayService.StoreTokenRequest
    intent: Initiate a token request for payments v1 or AIS
    question: How do I start an AIS or v1 payment request using Token.io Hosted Pages?
  - id: GatewayService.RetrieveTokenRequest
    intent: Get a token request
    question: Can I retrieve a token request by its id?
  - id: GatewayService.GetTokenRequestResultWithStatus
    intent: Get a token request result
    question: Has my token request moved from PENDING to PROCESSED?
  - id: GatewayService.InitiateBankAuthorization
    intent: Initiate bank authorization for a token request
    question: How do I start the bank authorization step for a token request?
  phrasing_ops: 4
  slug: token-io-requests-for-payments-v1-or-ais-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints provide authorized access to an authenticated user's settlement account information, enabling you to create settlement accounts, retrieve settlement account details, transactions and p
  name: token-io Settlement Accounts API
  phrasing_intents:
  - id: GatewayService.CreateVirtualAccount
    intent: Open a settlement account
    question: How do I open a new settlement account to collect payments?
  - id: GatewayService.GetVirtualAccounts
    intent: List settlement accounts
    question: Which settlement accounts do I hold, and in which currencies?
  - id: GatewayService.GetVirtualAccountById
    intent: Get a settlement account
    question: What are the details of one of my settlement accounts?
  - id: GatewayService.GetVirtualAccountTransactions
    intent: List settlement account transactions
    question: Which payments landed in my settlement account this week?
  - id: GatewayService.GetVirtualAccountTransaction
    intent: Get one settlement account transaction
    question: Can I pull a single transaction from my settlement account?
  - id: GatewayService.CreateVirtualAccountSettlementRule
    intent: Create an automatic settlement rule
    question: Can I automatically sweep funds from a settlement account to my bank account on a schedule?
  - id: GatewayService.GetVirtualAccountSettlementRules
    intent: List settlement rules on an account
    question: Which settlement rules are configured on my settlement account?
  - id: GatewayService.GetVirtualAccountSettlementRule
    intent: Get one settlement rule
    question: What does a specific settlement rule do?
  phrasing_ops: 10
  slug: token-io-settlement-accounts-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints are for resellers using Token.io's licence to create, retrieve and delete sub-TPPs.
  name: token-io Sub-TPPs API
  phrasing_intents:
  - id: GatewayService.CreateSubTpp
    intent: Create a sub-TPP
    question: How do I add a new merchant as a sub-TPP under my reseller account?
  - id: GatewayService.RetrieveSubTpps
    intent: List a reseller's sub-TPPs
    question: Which sub-TPPs have I onboarded as a reseller?
  - id: GatewayService.RetrieveSubTpp
    intent: Get a sub-TPP
    question: What details are stored for one of my sub-TPPs?
  - id: GatewayService.DeleteSubTpp
    intent: Delete a sub-TPP
    question: Can I remove a sub-TPP from my reseller account?
  - id: GatewayService.RetrieveSubTppChildren
    intent: List a sub-TPP's children
    question: Which child sub-TPPs sit under a given sub-TPP?
  - id: GatewayService.GetDocuments
    intent: List a sub-TPP's documents
    question: Which onboarding documents has a sub-TPP uploaded?
  - id: GatewayService.UploadDocument
    intent: Upload a document for a sub-TPP
    question: How do I upload a KYB document for a sub-TPP?
  - id: GatewayService.GetPreSignedUrl
    intent: Get a link to view a sub-TPP document
    question: How can I securely view or download a document a sub-TPP uploaded?
  phrasing_ops: 8
  slug: token-io-sub-tpps-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints retrieve all tokens, a filtered list of tokens, or a specific token, as well as allowing you to cancel an existing token.
  name: token-io Tokens API
  phrasing_intents:
  - id: GatewayService.GetTokens
    intent: List tokens for my member
    question: Which access or transfer tokens does my member have?
  - id: GatewayService.GetToken
    intent: Get a token
    question: What does a specific token grant access to?
  - id: GatewayService.CancelToken
    intent: Cancel a token
    question: Can I cancel a token so it can no longer be used?
  - id: GatewayService.ConfirmToken
    intent: Confirm a token on behalf of the user
    question: How do I record that the user confirmed a token?
  phrasing_ops: 4
  slug: token-io-tokens-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints relate to transfers, which are requests to move money between accounts.
  name: token-io Transfers - for Payments v1 API
  phrasing_intents:
  - id: GatewayService.CreateTransfer
    intent: Redeem a transfer token
    question: When do I need to redeem a transfer token myself?
  - id: GatewayService.GetTransfers
    intent: List transfers (payments v1)
    question: Which v1 payment transfers have gone through?
  - id: GatewayService.GetTransfer
    intent: Get a transfer (payments v1)
    question: What's the status of one v1 transfer?
  phrasing_ops: 3
  slug: token-io-transfers-for-payments-v1-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints enable you to initiate Variable Recurring Payments (VRP). Note, that VRP is also available in Payments v2 API.
  name: token-io Variable Recurring Payments API
  phrasing_intents:
  - id: CreateVrpConsent
    intent: Create a VRP consent
    question: How do I set up a variable recurring payment mandate with a customer?
  - id: GetVrpConsents
    intent: List VRP consents
    question: Which variable recurring payment consents have I created?
  - id: GetVrpConsent
    intent: Get a VRP consent
    question: What are the limits and status of a VRP consent?
  - id: RevokeVrpConsent
    intent: Revoke a VRP consent
    question: Can I revoke a VRP consent to stop future recurring payments?
  - id: GetVrpConsentPayments
    intent: List payments under a VRP consent
    question: Which payments have been taken under a VRP consent?
  - id: ConfirmFunds
    intent: Check funds before a VRP payment
    question: Does the payer have enough money before I take a VRP payment?
  phrasing_ops: 6
  slug: token-io-variable-recurring-payments-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Verification API from token-io — 1 operation(s) for verification.
  name: token-io Verification API
  phrasing_intents:
  - id: post-verification
    intent: Verify an account holder's name matches
    question: Can I check that a sort code and account number match the payee's name before paying?
  phrasing_ops: 1
  slug: token-io-verification-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: These endpoints configure, retrieve and remove webhooks. See <a href="https://developer.token.io/token_rest_api_doc/content/e-rest/api-basics.htm#Webhook" target="_blank">Webhooks</a> for more details
  name: token-io Webhooks API
  phrasing_intents:
  - id: GatewayService.SetWebhookConfig
    intent: Set my webhook configuration
    question: How do I register a webhook URL to receive payment status updates?
  - id: GatewayService.GetWebhookConfig
    intent: Get my webhook configuration
    question: Where are my webhook notifications being sent?
  - id: GatewayService.DeleteWebhookConfig
    intent: Delete my webhook configuration
    question: Can I stop receiving webhook notifications entirely?
  phrasing_ops: 3
  slug: token-io-webhooks-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Account Verifications API from Token.io — 1 operation(s) for account verifications.
  name: Token.io Account Verifications API
  phrasing_intents:
  - id: AccountVerificationService.PerformAccountVerification
    intent: Verify a bank account before paying it
    question: Can I check that a bank account's details match before sending money to it?
  phrasing_ops: 1
  slug: token-io-account-verifications-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The bankConfigs API from Token.io — 2 operation(s) for bankconfigs.
  name: Token.io Bank Configs API
  phrasing_intents:
  - id: GatewayService.GetBankConfigs
    intent: List a member's bank connection configs
    question: Which bank configurations have I stored for my member?
  - id: GatewayService.GetBankConfig
    intent: Get a member's config for one bank
    question: What configuration is stored for a specific bank on my member?
  - id: GatewayService.StoreBankConfig
    intent: Store a member's config for one bank
    question: Can I save my own open banking client credentials for a specific bank?
  - id: GatewayService.DeleteBankConfig
    intent: Delete a member's config for one bank
    question: Can I remove the stored configuration for a bank I no longer connect to?
  phrasing_ops: 4
  slug: token-io-bankconfigs-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The banks API from Token.io — 9 operation(s) for banks.
  name: Token.io Banks API
  phrasing_intents:
  - id: GatewayService.RetrieveConsentRequest
    intent: Get a consent request at a bank
    question: As a bank, how do I look up a consent request by its request id?
  - id: GatewayService.CreateConsent
    intent: Create a consent at a bank from a request
    question: How does a bank turn a consent request into an actual consent?
  - id: GatewayService.GetConsent
    intent: Get a consent at a bank
    question: Can a bank look up a consent it granted by consent id?
  - id: GatewayService.CancelConsent
    intent: Cancel a consent at a bank
    question: Can a bank cancel a consent it previously granted to a TPP?
  - id: GatewayService.GetAvailabilityReport
    intent: Get a bank's API availability report
    question: How available has a bank's open banking API been recently?
  - id: GatewayService.GetTppAccessReport
    intent: Get a bank's TPP access report
    question: Which third-party providers have been accessing a bank's APIs?
  - id: GatewayService.GetTppPerformanceReport
    intent: Get a bank's TPP performance report
    question: How is a bank's API performing for third-party providers?
  - id: GatewayService.CreateBankUser
    intent: Create a user in a bank's realm
    question: Can a bank create a user record in its Token.io realm?
  phrasing_ops: 11
  slug: token-io-banks-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Consents API from Token.io — 4 operation(s) for consents.
  name: Token.io Consents API
  phrasing_intents:
  - id: ConsentGatewayService.GetConsents
    intent: List account information consents
    question: Which of my v2 consents are about to expire?
  - id: ConsentGatewayService.RequestConsent
    intent: Request a new account information consent
    question: How can I ask a user for consent to read their bank account data?
  - id: ConsentGatewayService.GetConsent
    intent: Get one account information consent
    question: What's the current status of a specific consent?
  - id: ConsentGatewayService.RevokeConsent
    intent: Revoke an account information consent
    question: Can I revoke a user's consent so I stop accessing their account data?
  - id: ConsentGatewayService.ConfirmConsentAuthentication
    intent: Complete bank authentication for a consent
    question: After the bank redirects back, how do I finish authenticating a consent?
  - id: ConsentGatewayService.ConfirmConsent
    intent: Record that the user reconfirmed a consent
    question: Can I record that a user reconfirmed their consent to keep it active?
  phrasing_ops: 6
  slug: token-io-consents-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The eidas API from Token.io — 5 operation(s) for eidas.
  name: Token.io Eidas API
  phrasing_intents:
  - id: GatewayService.RecoverEidasMember
    intent: Recover an eIDAS-onboarded business member
    question: Can I recover a business member that was originally onboarded with an eIDAS certificate?
  - id: GatewayService.RegisterWithEidas
    intent: Create and register a business member with eIDAS
    question: How do I onboard a new business member using an eIDAS certificate?
  - id: GatewayService.getEidasCertificateStatus
    intent: Check the status of my eIDAS certificate
    question: Is the eIDAS certificate on file for my member still valid?
  - id: GatewayService.VerifyEidas
    intent: Submit an eIDAS certificate for verification
    question: Can I submit an eIDAS certificate to verify a business member under a bank realm?
  - id: GatewayService.GetEidasVerificationStatus
    intent: Check the outcome of an eIDAS verification
    question: Did my eIDAS verification succeed?
  phrasing_ops: 5
  slug: token-io-eidas-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: Health Check Endpoints.
  name: Token.io Health API
  phrasing_intents:
  - id: getHealthCheck
    intent: Check the health of a bank connection
    question: Is the connection to a specific bank currently up?
  phrasing_ops: 1
  slug: token-io-health-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The info API from Token.io — 5 operation(s) for info.
  name: Token.io Info API
  phrasing_intents:
  - id: GatewayService.GetBanksCountries
    intent: List countries with integrated banks
    question: In which countries does Token.io have integrated banks?
  - id: GatewayService.GetBanks
    intent: Find banks matching feature criteria
    question: Which banks in a country support standing orders?
  - id: GatewayService.GetBankInfo
    intent: Get information about one bank
    question: What does Token.io know about a specific supported bank?
  - id: GatewayService.GetBankAuthUrl
    intent: Generate a bank authorization URL for a token request
    question: How do I get the URL to send a user to their bank for a token request?
  - id: GatewayService.InitiateBankAuthorization
    intent: Start bank authorization for a token request
    question: Can I kick off the bank authorization process directly for a token request?
  phrasing_ops: 5
  slug: token-io-info-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Member API from Token.io — 6 operation(s) for member.
  name: Token.io Member API
  phrasing_intents:
  - id: GatewayService.GetRestrictions
    intent: List product restrictions on members
    question: Which product restrictions have I set on members?
  - id: GatewayService.CreateRestriction
    intent: Create a product restriction for a member
    question: Can I restrict what a member is allowed to do with a product?
  - id: GatewayService.GetCountries
    intent: List countries available for restrictions
    question: Which countries can I use when writing a restriction rule?
  - id: GatewayService.GetRegions
    intent: List regions of a country for restrictions
    question: What regions within a country can a restriction rule target?
  - id: GatewayService.UpdateRestriction
    intent: Update a product restriction
    question: Can I change an existing restriction without deleting it?
  - id: GatewayService.DeleteRestriction
    intent: Delete a product restriction
    question: Can I lift a restriction entirely by removing it?
  - id: GatewayService.CreateRule
    intent: Add a rule to a product restriction
    question: How do I add a new rule under an existing restriction?
  - id: GatewayService.UpdateRule
    intent: Update a rule in a product restriction
    question: Can I edit one rule inside a restriction?
  phrasing_ops: 9
  slug: token-io-member-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Members API from Token.io — 2 operation(s) for members.
  name: Token.io Members API
  phrasing_intents:
  - id: GatewayService.GetMemberKeys
    intent: List a member's public keys
    question: Which public keys are on file for a member?
  - id: GatewayService.AddMemberKey
    intent: Add a public key to a member
    question: How do I register a new public key for a member?
  - id: GatewayService.GetMemberKey
    intent: Get one member public key
    question: Can I fetch a single member key by its id?
  - id: GatewayService.DeleteMemberKey
    intent: Remove a member public key
    question: Can I delete a public key a member no longer uses?
  phrasing_ops: 4
  slug: token-io-members-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The partner API from Token.io — 3 operation(s) for partner.
  name: Token.io Partner API
  phrasing_intents:
  - id: GatewayService.GetMembersUnderPartner
    intent: List members under my partner realm
    question: Which members are registered under my partner realm?
  - id: GatewayService.DisableMember
    intent: Disable a member under my partner realm
    question: Can I suspend a member that sits under my partner realm?
  - id: GatewayService.EnableMember
    intent: Re-enable a member under my partner realm
    question: Can I turn a disabled member back on?
  phrasing_ops: 3
  slug: token-io-partner-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Payment Links API from Token.io — 2 operation(s) for payment links.
  name: Token.io Payment Links API
  phrasing_intents:
  - id: PaymentLinkService.ListPaymentLinks
    intent: List payment links
    question: Which payment links have I created?
  - id: PaymentLinkService.CreatePaymentLink
    intent: Create a payment link
    question: Can I generate a link a customer opens to pay me?
  - id: PaymentLinkService.GetPaymentLink
    intent: Get one payment link
    question: What's the status of a payment link I sent?
  - id: PaymentLinkService.CancelPaymentLink
    intent: Cancel a payment link
    question: Can I cancel a payment link I shared by mistake?
  phrasing_ops: 4
  slug: token-io-payment-links-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Payments API from Token.io — 4 operation(s) for payments.
  name: Token.io Payments API
  phrasing_intents:
  - id: GatewayService.GetPaymentsV2
    intent: List payments
    question: Which payments failed or are still pending?
  - id: GatewayService.CreatePaymentV2
    intent: Initiate a payment
    question: How do I start a bank payment from my app?
  - id: GatewayService.GetPaymentV2
    intent: Get a payment and its status
    question: What's the current status of a payment?
  - id: GatewayService.CancelPayment
    intent: Cancel a payment
    question: Can I cancel a payment before it completes?
  - id: GatewayService.ProvidePaymentEmbeddedAuthV2
    intent: Submit embedded authentication for a payment
    question: The bank asked for extra details during payment; where do I send them?
  - id: GatewayService.RedeemPaymentV2
    intent: Redeem an authorized payment
    question: Once a user authorizes a payment, how do I redeem it to execute it?
  phrasing_ops: 6
  slug: token-io-payments-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Provider API from Token.io — 2 operation(s) for provider.
  name: Token.io Provider API
  phrasing_intents:
  - id: GatewayService.GetProviderRegistrations
    intent: List my provider registrations
    question: Which bank provider registrations do I have on file?
  - id: GatewayService.RegisterProvider
    intent: Register with a bank provider for a product
    question: How do I register my credentials with a provider such as HSBC or BNP Paribas?
  - id: GatewayService.GetProviderRegistration
    intent: Get one provider registration
    question: What's stored in a particular provider registration?
  - id: GatewayService.DeleteProviderRegistration
    intent: Delete a provider registration
    question: Can I remove a provider registration I no longer need?
  phrasing_ops: 4
  slug: token-io-provider-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Qr Code API from Token.io — 1 operation(s) for qr code.
  name: Token.io Qr Code API
  phrasing_intents:
  - id: GatewayService.GetQrCode
    intent: Generate a QR code
    question: Can I turn a payment link into a QR code a customer scans?
  phrasing_ops: 1
  slug: token-io-qr-code-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Refund API from Token.io — 2 operation(s) for refund.
  name: Token.io Refund API
  phrasing_intents:
  - id: GatewayService.RegisterForRefund
    intent: Register a debtor account for refunds
    question: How do I register the account refunds will be paid from?
  - id: GatewayService.GetRefundRegistration
    intent: Get a refund registration
    question: What's recorded in my refund registration?
  - id: GatewayService.DeleteRefundRegistration
    intent: Delete a refund registration
    question: Can I delete a refund registration?
  phrasing_ops: 3
  slug: token-io-refund-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The requests API from Token.io — 4 operation(s) for requests.
  name: Token.io Requests API
  phrasing_intents:
  - id: GatewayService.StoreTokenRequest
    intent: Create a token request
    question: How do I set up a token request for the web app to complete a transaction?
  - id: GatewayService.RetrieveTokenRequest
    intent: Find a token request
    question: Can I look up a token request I created?
  - id: GatewayService.GetTokenRequestResultWithStatus
    intent: Check a token request result with status
    question: Is my token request still PENDING or has it been PROCESSED?
  - id: GatewayService.GetTokenRequestResult
    intent: Get a token request result
    question: Is a result available for a token request yet?
  phrasing_ops: 4
  slug: token-io-requests-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Secrets API from Token.io — 1 operation(s) for secrets.
  name: Token.io Secrets API
  phrasing_intents:
  - id: GatewayService.UploadKeyAndCertificate
    intent: Upload a private key and certificate
    question: Where do I upload my private key and certificate?
  phrasing_ops: 1
  slug: token-io-secrets-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The subTpp API from Token.io — 6 operation(s) for subtpp.
  name: Token.io Sub Tpp API
  phrasing_intents:
  - id: GatewayService.RetrieveSubTpps
    intent: List all sub-TPPs for the reseller
    question: Which sub-TPPs do I have, and what are their statuses?
  - id: GatewayService.CreateSubTpp
    intent: Create a new sub-TPP
    question: How do I create a sub-TPP with a name, domain and merchant category code?
  - id: GatewayService.RetrieveSubTpp
    intent: Get sub-TPP details
    question: What's on file for one of my sub-TPPs?
  - id: GatewayService.UpdateSubTpp
    intent: Update a sub-TPP
    question: Can I change a sub-TPP's details after creating it?
  - id: GatewayService.DeleteSubTpp
    intent: Delete a sub-TPP
    question: Can I delete a sub-TPP I no longer resell to?
  - id: GatewayService.RetrieveSubTppChildren
    intent: List a sub-TPP's children
    question: Which sub-TPPs are children of another sub-TPP?
  - id: GatewayService.GetDocuments
    intent: List a sub-TPP's documents
    question: Which documents are uploaded for a sub-TPP?
  - id: GatewayService.GetPreSignedUrl
    intent: Get a pre-signed URL for a sub-TPP document
    question: How do I view or download an uploaded sub-TPP document?
  phrasing_ops: 9
  slug: token-io-subtpp-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Tokenized Accounts API from Token.io — 2 operation(s) for tokenized accounts.
  name: Token.io Tokenized Accounts API
  phrasing_intents:
  - id: TokenizedAccountService.CreateTokenizedAccount
    intent: Tokenize a bank account for reuse
    question: Can I save a customer's bank account as a token to reuse in later payments?
  - id: TokenizedAccountService.GetTokenizedAccount
    intent: Get a tokenized account
    question: What bank account does a tokenized account id refer to?
  - id: TokenizedAccountService.DeleteTokenizedAccount
    intent: Delete a tokenized account
    question: Can I delete a tokenized account so it can't be used again?
  phrasing_ops: 3
  slug: token-io-tokenized-accounts-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: Transfers Service - Implemented by bank to support payment initiation.
  name: Token.io Transfers API
  phrasing_intents:
  - id: createTransfer
    intent: Create a transaction for a transfer as the bank
    question: As the bank integration, how do I create a transaction for a transfer request?
  - id: GatewayService.GetTransfers
    intent: List transfers
    question: Which transfers were made under a particular token?
  - id: getTransferStatusForId
    intent: Get a transfer's status as the bank
    question: What's the bank-side status of a transfer?
  - id: GatewayService.GetRefundsByPaymentId
    intent: List refunds for a payment
    question: Which refunds have been issued against a payment?
  - id: GatewayService.GetStandingOrderSubmissions
    intent: List standing order submissions
    question: Which standing order submissions have I made?
  - id: GatewayService.CreateStandingOrder
    intent: Submit a standing order
    question: How do I create a standing order using a token?
  - id: GatewayService.GetStandingOrderSubmission
    intent: Get a standing order submission
    question: Did my standing order submission go through?
  - id: GatewayService.GetTransfer
    intent: Get a transfer
    question: What are the details of one transfer?
  phrasing_ops: 8
  slug: token-io-transfers-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The tsp API from Token.io — 2 operation(s) for tsp.
  name: Token.io Tsp API
  phrasing_intents:
  - id: GatewayService.OnBankAuthCallback
    intent: Process a bank authorization callback
    question: Where do I forward the bank's authorization callback?
  - id: GatewayService.GetExternalMetadata
    intent: Get bank metadata for a token request
    question: What external metadata did the bank return for a token request?
  phrasing_ops: 2
  slug: token-io-tsp-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Virtual Accounts API from Token.io — 1 operation(s) for virtual accounts.
  name: Token.io Virtual Accounts API
  phrasing_intents:
  - id: GatewayService.CreditVirtualAccount
    intent: Credit a virtual account
    question: Can I add funds to a virtual account?
  phrasing_ops: 1
  slug: token-io-virtual-accounts-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The Vrps API from Token.io — 1 operation(s) for vrps.
  name: Token.io Vrps API
  phrasing_intents:
  - id: GatewayService.ConfirmFundsAvailability
    intent: Confirm funds for a VRP consent
    question: Is there enough money in the payer's account for my next VRP?
  phrasing_ops: 1
  slug: token-io-vrps-api
- baseURL: https://api.token.io
  baseurl_source: declared
  description: The webhook API from Token.io — 1 operation(s) for webhook.
  name: Token.io Webhook API
  phrasing_intents:
  - id: GatewayService.GetWebhookConfig
    intent: Get my webhook configuration
    question: Where are my webhook notifications being sent?
  - id: GatewayService.SetWebhookConfig
    intent: Set my webhook configuration
    question: How do I register a webhook URL to receive payment status updates?
  - id: GatewayService.DeleteWebhookConfig
    intent: Delete my webhook configuration
    question: Can I stop receiving webhook notifications entirely?
  phrasing_ops: 3
  slug: token-io-webhook-api
artifact_total: 231
asyncapis:
- description: ''
  name: Token Io Webhooks
  slug: token-io-webhooks
collections:
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File API
  slug: postman-token-io-account-on-file-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Accounts API
  slug: postman-token-io-accounts-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Authentication keys API
  slug: postman-token-io-authentication-keys-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Banks v1 API
  slug: postman-token-io-banks-v1-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Banks v2 API
  slug: postman-token-io-banks-v2-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Pay by Link API
  slug: postman-token-io-pay-by-link-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Payments v2 API
  slug: postman-token-io-payments-v2-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Payouts API
  slug: postman-token-io-payouts-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Refunds API
  slug: postman-token-io-refunds-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Reports API
  slug: postman-token-io-reports-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Requests - for Payments v1 or AIS API
  slug: postman-token-io-requests-for-payments-v1-or-ais-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Settlement Accounts API
  slug: postman-token-io-settlement-accounts-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Sub-TPPs API
  slug: postman-token-io-sub-tpps-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Tokens API
  slug: postman-token-io-tokens-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Transfers - for Payments v1 API
  slug: postman-token-io-transfers-for-payments-v1-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Variable Recurring Payments API
  slug: postman-token-io-variable-recurring-payments-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Verification API
  slug: postman-token-io-verification-api
- collection_type: postman
  name: Token.io's Open Banking API for TPPs Account on File Webhooks API
  slug: postman-token-io-webhooks-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File API
  slug: open-token-io-account-on-file-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Accounts API
  slug: open-token-io-accounts-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Authentication keys API
  slug: open-token-io-authentication-keys-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Banks v1 API
  slug: open-token-io-banks-v1-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Banks v2 API
  slug: open-token-io-banks-v2-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Pay by Link API
  slug: open-token-io-pay-by-link-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Payments v2 API
  slug: open-token-io-payments-v2-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Payouts API
  slug: open-token-io-payouts-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Refunds API
  slug: open-token-io-refunds-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Reports API
  slug: open-token-io-reports-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Requests - for Payments v1 or AIS API
  slug: open-token-io-requests-for-payments-v1-or-ais-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Settlement Accounts API
  slug: open-token-io-settlement-accounts-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Sub-TPPs API
  slug: open-token-io-sub-tpps-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Tokens API
  slug: open-token-io-tokens-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Transfers - for Payments v1 API
  slug: open-token-io-transfers-for-payments-v1-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Variable Recurring Payments API
  slug: open-token-io-variable-recurring-payments-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Verification API
  slug: open-token-io-verification-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs Account on File Webhooks API
  slug: open-token-io-webhooks-api
- collection_type: open
  name: Token.io's Open Banking API for TPPs
  slug: open-token-io
common:
- group: design
  href: https://artifacts.apis.io/token-io/rules/token-io-rules.yml
  title: ''
  type: Spectral
  url: rules/token-io-rules.yml
- group: design
  href: https://artifacts.apis.io/token-io/rules/token-io-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/token-io-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/token-io/vocabulary/token-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/token-io-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-transferinstructions.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-transferinstructions.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-transfer.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-transfer.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-transaction.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-transaction.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-subscriber.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-subscriber.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-submission.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-submission.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-security.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-security.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-providerspecific.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-providerspecific.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-pricing.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-pricing.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-notification.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-notification.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-money.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-money.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-member.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-member.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-eidas.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-eidas.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-consent.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-consent.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-blob.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-blob.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-banklink.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-banklink.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-bankinfo.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-bankinfo.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-alias.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-alias.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-address.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-address.proto
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-account.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-account.proto
- group: agent
  href: https://artifacts.apis.io/token-io/well-known/token-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/token-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/token-io/hosts/token-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/token-io-hosts.yml
- group: build
  href: https://artifacts.apis.io/token-io/integrations/token-io-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/token-io-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/token-io/vendors/token-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/token-io-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://token.io/press
- group: other
  href: https://artifacts.apis.io/token-io/capabilities/token-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/token-io-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://token.io
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/token-io/overview
- group: agent
  href: https://artifacts.apis.io/token-io/agentic-access/token-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/token-io-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/token-io/security/token-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/token-io-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/token-io/authentication/token-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/token-io-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://token.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.token.io
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.token.io/products/tpp
- group: docs
  title: ''
  type: Reference
  url: https://reference.token.io/
- group: operate
  title: ''
  type: Support
  url: https://support.token.io
- group: start
  title: ''
  type: Sandbox
  url: https://dashboard.sandbox.token.io/signin
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tokenio
- group: commercial
  title: ''
  type: Pricing
  url: https://token.io/contact/pricing
- group: company
  title: ''
  type: Blog
  url: https://token.io/blog
- group: operate
  title: ''
  type: FAQ
  url: https://token.io/faq
- group: commercial
  title: ''
  type: License
  url: https://www.openbanking.org.uk/regulated-providers/token/
- group: commercial
  href: https://artifacts.apis.io/token-io/plans/token-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/token-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/token-io/rate-limits/token-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/token-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/token-io/finops/token-io-finops.yml
  title: ''
  type: FinOps
  url: finops/token-io-finops.yml
- group: build
  href: https://artifacts.apis.io/token-io/packages/token-io-packages.yml
  title: ''
  type: Packages
  url: packages/token-io-packages.yml
- group: build
  href: https://artifacts.apis.io/token-io/packages/token-io-packages.yml
  title: ''
  type: SDKs
  url: packages/token-io-packages.yml
- group: agent
  href: https://artifacts.apis.io/token-io/mcp/token-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/token-io-mcp.yml
- group: build
  href: https://artifacts.apis.io/token-io/mcp/token-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/token-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/token-io/llms/token-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/token-io-llms.txt
- group: other
  href: https://artifacts.apis.io/token-io/overlays/token-io-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/token-io-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/token-io/grpc/token-io-token.proto
  title: ''
  type: Protobuf
  url: grpc/token-io-token.proto
- group: design
  href: https://artifacts.apis.io/token-io/conformance/token-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/token-io-conformance.yml
- group: auth
  href: https://artifacts.apis.io/token-io/conformance/token-io-conformance.yml
  title: ''
  type: Compliance
  url: conformance/token-io-conformance.yml
- group: design
  href: https://artifacts.apis.io/token-io/errors/token-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/token-io-problem-types.yml
- group: build
  href: https://artifacts.apis.io/token-io/errors/token-io-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/token-io-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/token-io/lifecycle/token-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/token-io-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/token-io/lifecycle/token-io-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/token-io-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/token-io/changelog/token-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/token-io-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.token.io/products/tpp/tech-bulletins/tb-1638
- group: design
  href: https://artifacts.apis.io/token-io/conventions/token-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/token-io-conventions.yml
- group: start
  href: https://artifacts.apis.io/token-io/sandbox/token-io-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/token-io-sandbox.yml
- group: design
  href: https://artifacts.apis.io/token-io/components/token-io-components.yml
  title: ''
  type: Components
  url: components/token-io-components.yml
- group: design
  href: https://artifacts.apis.io/token-io/data-model/token-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/token-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/token-io/asyncapi/token-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/token-io-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/token-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://token.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://token.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://dashboard.token.io
created: '2026-05-25T00:00:00.000Z'
description: Token.io is an Open Banking infrastructure provider offering A2A (Account-to-Account) payments and account information services across Europe. Founded in 2016 and FCA-authorised since 2018, Token.io was the first payment initiation service provider to conduct an end-to-end PSD2-compliant Open Banking transaction. The Token.io platform connects developers and TPPs to over 4,000 banks via a single standardised API supporting Payment Initiation Services (PIS), Account Information Services (AIS), Variable Recurring Payments (VRP), refunds, payouts, settlement accounts, account verification, and Pay-by-Link checkout. Used by merchants, PSPs, fintechs, PFM apps, and platform businesses to replace card-rail payments and aggregate multibank data.
features:
- Single Immediate Payments (SIP) via Payments v2
- Future-Dated Payments
- Variable Recurring Payments (VRP) — sweeping and commercial / non-sweeping
- VRP Consents with fund availability checks
- Account Information Services (AIS) — balances, transactions, standing orders, account details
- Pay by Link — reusable payment URLs with usage and amount limits
- Account on File — tokenized bank account references for repeat payments
- Refunds tied to original payment transactions
- Payouts — outbound transfer execution and monitoring
- Settlement Accounts — virtual accounts, transaction lists, and settlement rules
- Account Verification — name and account-holder confirmation checks
- Banks v1 and Banks v2 — discovery of 4,000+ connected banks across Europe
- Sub-TPP management for reseller and platform models
- Authentication Keys API for managing JWT public keys
- Webhooks for event notifications across payments and AIS lifecycle
- Reports API for monitoring AIS/PIS bank status
- JWT Bearer Token authentication (production and sandbox)
- Basic Auth for sandbox testing
- Hosted Payment Pages via iOS and Android webview SDKs
- PSD2-compliant Payment Initiation Service (PIS) and Account Information Service (AIS)
- FCA-authorised UK PISP / AISP since 2018
- Coverage across UK and EU SEPA payment rails
- Official SDKs for JavaScript, PHP, C#, and Objective-C
- Sandbox environment at dashboard.sandbox.token.io
finops:
- has_sources: true
  method: derived
  name: Token Io Finops
  primary_unit: ''
  service_category: ''
  slug: token-io-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/token-io.png
json_schemas:
- name: Token.io Account
  property_count: 0
  slug: token-io-account
- name: google.protobuf.Empty
  property_count: 0
  slug: token-io-google-protobuf-empty
- name: io.token.proto.gateway.accountverification.AccountVerificationResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-accountverification-account-verification-response
- name: io.token.proto.gateway.accountverification.PerformAccountVerificationRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-accountverification-perform-account-verification-request
- name: io.token.proto.gateway.AddMemberKeyRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-add-member-key-request
- name: io.token.proto.gateway.AddMemberKeyResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-add-member-key-response
- name: io.token.proto.gateway.CancelPaymentResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-cancel-payment-response
- name: io.token.proto.gateway.ConfirmFundsAvailabilityResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-confirm-funds-availability-response
- name: io.token.proto.gateway.consent.ConfirmConsentAuthenticationRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-consent-confirm-consent-authentication-request
- name: io.token.proto.gateway.consent.ConfirmConsentRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-consent-confirm-consent-request
- name: io.token.proto.gateway.consent.ConsentRequest
  property_count: 10
  slug: token-io-io-token-proto-gateway-consent-consent-request
- name: io.token.proto.gateway.consent.ConsentResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-consent-consent-response
- name: io.token.proto.gateway.consent.GetConsentsResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-consent-get-consents-response
- name: io.token.proto.gateway.CreatePaymentV2Request
  property_count: 3
  slug: token-io-io-token-proto-gateway-create-payment-v2-request
- name: io.token.proto.gateway.CreateRestrictionRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-create-restriction-request
- name: io.token.proto.gateway.CreateStandingOrderResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-create-standing-order-response
- name: io.token.proto.gateway.CreateSubTppRequest
  property_count: 8
  slug: token-io-io-token-proto-gateway-create-sub-tpp-request
- name: io.token.proto.gateway.CreditVirtualAccountRequest
  property_count: 4
  slug: token-io-io-token-proto-gateway-credit-virtual-account-request
- name: io.token.proto.gateway.CreditVirtualAccountResponse
  property_count: 0
  slug: token-io-io-token-proto-gateway-credit-virtual-account-response
- name: io.token.proto.gateway.DeleteBankConfigResponse
  property_count: 0
  slug: token-io-io-token-proto-gateway-delete-bank-config-response
- name: io.token.proto.gateway.DeleteMemberKeyResponse
  property_count: 0
  slug: token-io-io-token-proto-gateway-delete-member-key-response
- name: io.token.proto.gateway.DeleteRestrictionResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-delete-restriction-response
- name: io.token.proto.gateway.DeleteWebhookConfigResponse
  property_count: 0
  slug: token-io-io-token-proto-gateway-delete-webhook-config-response
- name: io.token.proto.gateway.DisableMemberResponse
  property_count: 0
  slug: token-io-io-token-proto-gateway-disable-member-response
- name: io.token.proto.gateway.EmptyResponse
  property_count: 0
  slug: token-io-io-token-proto-gateway-empty-response
- name: io.token.proto.gateway.EnableMemberResponse
  property_count: 0
  slug: token-io-io-token-proto-gateway-enable-member-response
- name: io.token.proto.gateway.GetAccessConsentsResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-access-consents-response
- name: io.token.proto.gateway.GetActiveAccessConsentsResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-active-access-consents-response
- name: io.token.proto.gateway.GetAvailabilityReportResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-availability-report-response
- name: io.token.proto.gateway.GetBankAuthUrlRequest
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-bank-auth-url-request
- name: io.token.proto.gateway.GetBankConfigResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-bank-config-response
- name: io.token.proto.gateway.GetBankConfigsResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-bank-configs-response
- name: io.token.proto.gateway.GetBankInfoResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-bank-info-response
- name: io.token.proto.gateway.GetBanksCountriesResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-banks-countries-response
- name: io.token.proto.gateway.GetBanksResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-banks-response
- name: io.token.proto.gateway.GetCountriesResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-countries-response
- name: io.token.proto.gateway.GetDocumentsResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-documents-response
- name: io.token.proto.gateway.GetEidasCertificateStatusResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-eidas-certificate-status-response
- name: io.token.proto.gateway.GetEidasVerificationStatusResponse
  property_count: 4
  slug: token-io-io-token-proto-gateway-get-eidas-verification-status-response
- name: io.token.proto.gateway.GetExternalMetadataResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-external-metadata-response
- name: io.token.proto.gateway.GetMemberKeyResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-member-key-response
- name: io.token.proto.gateway.GetMemberKeysResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-member-keys-response
- name: io.token.proto.gateway.GetMembersUnderPartnerResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-members-under-partner-response
- name: io.token.proto.gateway.GetPaymentsV2Response
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-payments-v2-response
- name: io.token.proto.gateway.GetPayoutRegistrationResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-payout-registration-response
- name: io.token.proto.gateway.GetProviderRegistrationsResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-provider-registrations-response
- name: io.token.proto.gateway.GetQrCodeResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-qr-code-response
- name: io.token.proto.gateway.GetRefundsByPaymentIdResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-refunds-by-payment-id-response
- name: io.token.proto.gateway.GetRegionsResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-regions-response
- name: io.token.proto.gateway.GetRestrictionsResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-restrictions-response
- name: io.token.proto.gateway.GetStandingOrderSubmissionsResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-get-standing-order-submissions-response
- name: io.token.proto.gateway.GetTokenRequestResultWithStatusResponse
  property_count: 7
  slug: token-io-io-token-proto-gateway-get-token-request-result-with-status-response
- name: io.token.proto.gateway.GetTppAccessReportResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-tpp-access-report-response
- name: io.token.proto.gateway.GetTppPerformanceReportResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-tpp-performance-report-response
- name: io.token.proto.gateway.GetWebhookConfigResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-get-webhook-config-response
- name: io.token.proto.gateway.InitiateBankAuthorizationRequest
  property_count: 4
  slug: token-io-io-token-proto-gateway-initiate-bank-authorization-request
- name: io.token.proto.gateway.InitiateBankAuthorizationResponse
  property_count: 4
  slug: token-io-io-token-proto-gateway-initiate-bank-authorization-response
- name: io.token.proto.gateway.OnBankAuthCallbackRequest
  property_count: 1
  slug: token-io-io-token-proto-gateway-on-bank-auth-callback-request
- name: io.token.proto.gateway.OnBankAuthCallbackResponse
  property_count: 5
  slug: token-io-io-token-proto-gateway-on-bank-auth-callback-response
- name: io.token.proto.gateway.PaymentV2Response
  property_count: 1
  slug: token-io-io-token-proto-gateway-payment-v2-response
- name: io.token.proto.gateway.paymentlinks.CreatePaymentLinkRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-paymentlinks-create-payment-link-request
- name: io.token.proto.gateway.paymentlinks.PaymentLinkResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-paymentlinks-payment-link-response
- name: io.token.proto.gateway.paymentlinks.PaymentLinksResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-paymentlinks-payment-links-response
- name: io.token.proto.gateway.PayoutRegisterRequest
  property_count: 4
  slug: token-io-io-token-proto-gateway-payout-register-request
- name: io.token.proto.gateway.PayoutRegisterResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-payout-register-response
- name: io.token.proto.gateway.ProvidePaymentEmbeddedAuthV2Request
  property_count: 1
  slug: token-io-io-token-proto-gateway-provide-payment-embedded-auth-v2-request
- name: io.token.proto.gateway.ProviderRegistrationResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-provider-registration-response
- name: io.token.proto.gateway.RecoverEidasRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-recover-eidas-request
- name: io.token.proto.gateway.RegisterProviderRequest
  property_count: 5
  slug: token-io-io-token-proto-gateway-register-provider-request
- name: io.token.proto.gateway.RegisterWithEidasRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-register-with-eidas-request
- name: io.token.proto.gateway.RetrieveConsentRequestResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-retrieve-consent-request-response
- name: io.token.proto.gateway.RetrieveSubTppChildrenResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-retrieve-sub-tpp-children-response
- name: io.token.proto.gateway.RetrieveSubTppResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-retrieve-sub-tpp-response
- name: io.token.proto.gateway.RetrieveSubTppsResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-retrieve-sub-tpps-response
- name: io.token.proto.gateway.SetWebhookConfigRequest
  property_count: 1
  slug: token-io-io-token-proto-gateway-set-webhook-config-request
- name: io.token.proto.gateway.SetWebhookConfigResponse
  property_count: 0
  slug: token-io-io-token-proto-gateway-set-webhook-config-response
- name: io.token.proto.gateway.StoreBankConfigResponse
  property_count: 0
  slug: token-io-io-token-proto-gateway-store-bank-config-response
- name: io.token.proto.gateway.tokenizedaccount.CreateTokenizedAccountRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-tokenizedaccount-create-tokenized-account-request
- name: io.token.proto.gateway.tokenizedaccount.CreateTokenizedAccountResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-tokenizedaccount-create-tokenized-account-response
- name: io.token.proto.gateway.tokenizedaccount.GetTokenizedAccountResponse
  property_count: 2
  slug: token-io-io-token-proto-gateway-tokenizedaccount-get-tokenized-account-response
- name: io.token.proto.gateway.UpdateRestrictionRequest
  property_count: 1
  slug: token-io-io-token-proto-gateway-update-restriction-request
- name: io.token.proto.gateway.UploadDocumentRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-upload-document-request
- name: io.token.proto.gateway.UploadKeyAndCertificateRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-upload-key-and-certificate-request
- name: io.token.proto.gateway.UploadKeyAndCertificateResponse
  property_count: 1
  slug: token-io-io-token-proto-gateway-upload-key-and-certificate-response
- name: io.token.proto.gateway.VerifyEidasRequest
  property_count: 2
  slug: token-io-io-token-proto-gateway-verify-eidas-request
- name: io.token.proto.gateway.VerifyEidasResponse
  property_count: 3
  slug: token-io-io-token-proto-gateway-verify-eidas-response
- name: Token.io Payment
  property_count: 0
  slug: token-io-payment
- name: TransactionStatus
  property_count: 0
  slug: token-io-transaction-status
- name: TransferRequest
  property_count: 9
  slug: token-io-transfer-request
- name: TransferResponse
  property_count: 4
  slug: token-io-transfer-response
- name: Token.io VRP Consent
  property_count: 11
  slug: token-io-vrp-consent
jsonld:
- class_count: 0
  name: Token Io Context
  property_count: 6
  slug: token-io-context
layout: provider
mcp_servers:
- description: 'Token.io serves a live, anonymous, remote MCP server on its own documentation host. It is a DOCUMENTATION server, not a payments server: the six tools read the API descriptions Token.io publishes (lis'
  name: Token.io Documentation MCP Server (https://docs.token.io/mcp)
  slug: token-io-documentation-mcp-server-https-docs-token-io-mcp
modified: '2026-09-17'
name: Token.io
nav: Providers
network: true
overview: 'Token.io publishes 53 API contracts indexed on the [APIs.io](https://apis.io/) network, including token-io Account on File API, token-io Accounts API, token-io Authentication keys API, and 50 more. Tagged areas include Payments, Open Banking, Banking, Financial Services, and Account-to-Account.


  The Token.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Token.io''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, sandbox, pricing, and 64 more developer resources.'
plans:
- name: Token Io Plans Pricing
  plan_count: 4
  slug: token-io-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Token Io Rate Limits
  slug: token-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Token.io — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: token-io-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Token.io API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 3
  slug: token-io-rules
score:
  band: exemplar
  composite: 70.5
  coverage:
    artifact_dirs: 38
    catalog_earned: 78.8
    catalog_earned_first_party: 24.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 84.2
    contract_governance: 35.6
    contract_quality: 64.9
    developer_ergonomics: 83.9
    discoverability: 72.5
    operational_transparency: 68.4
  previous_composite: 70.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 97.6
      derived: 0
      marker_coverage: 47.6
      total: 42
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 26.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/token-io/token-io-2026-06-20T195438.png
security:
- kind: authentication
  name: Token Io Authentication
  slug: token-io-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Token Io Domain Security
  slug: token-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: token-io-fetch-account-data
  slug: token-io-fetch-account-data
- name: token-io-initiate-single-payment
  slug: token-io-initiate-single-payment
- name: token-io-refund-a-payment
  slug: token-io-refund-a-payment
- name: token-io-set-up-vrp-consent
  slug: token-io-set-up-vrp-consent
slug: token-io
tags:
- Payments
- Open Banking
- Banking
- Financial Services
- Account-to-Account
- PSD2
- Variable Recurring Payments
- Account Information Services
- Payment Initiation
- Fintech
use_cases:
- E-commerce Pay-by-Bank checkout (Account-to-Account payments)
- Subscription billing via VRP commercial mandates
- Utility bill recurring payments via VRP
- Account top-ups (investment, gaming, mobile, savings)
- Charity donations (zero-fee for charitable organisations)
- Personal Finance Management (PFM) multibanking via AIS
- Peer-to-peer (P2P) and Business-to-Business (B2B) payments
- Lending and credit risk assessment via account data
- Account verification for KYC and anti-fraud workflows
- Payouts and settlements for marketplaces and platforms
- Reseller / Sub-TPP platform integrations
website: https://token.io
---
