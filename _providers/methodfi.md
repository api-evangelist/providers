---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.4
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 60
  human_in_the_loop: 0
  name: Methodfi Agentic Access
  operation_count: 146
  slug: methodfi-agentic-access
  summary_line: 146 operations · 60 acting
api_count: 2
apis:
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Attribute data for accounts
  name: MethodFi Account Attributes API
  phrasing_intents:
  - id: listAccountAttributes
    intent: List the attributes pulled for an account
    question: Which attribute requests have already been run on this account?
  - id: createAccountAttribute
    intent: Request fresh attributes for an account
    question: How do I kick off a new attribute request for a liability account?
  - id: retrieveAccountAttribute
    intent: Get one account attribute record
    question: Can I look up a single attribute result by its ID?
  phrasing_ops: 3
  slug: methodfi-account-attributes-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Balance data for accounts
  name: MethodFi Account Balances API
  phrasing_intents:
  - id: listAccountBalances
    intent: List balance records for an account
    question: Where can I see the history of balance syncs for an account?
  - id: createAccountBalance
    intent: Sync a fresh balance for an account
    question: How do I trigger a new balance sync on an account?
  - id: retrieveAccountBalance
    intent: Get one balance record
    question: What did a particular balance sync return?
  phrasing_ops: 3
  slug: methodfi-account-balances-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Card brand information for accounts
  name: MethodFi Account Card Brands API
  phrasing_intents:
  - id: listAccountCardBrands
    intent: List card brand lookups for an account
    question: Which card brand lookups have been run on this card account?
  - id: createAccountCardBrand
    intent: Look up the card brand for an account
    question: How do I find out which card brand a card account belongs to?
  - id: retrieveAccountCardBrand
    intent: Get one card brand result
    question: What did a specific card brand lookup return?
  phrasing_ops: 3
  slug: methodfi-account-card-brands-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Consent management for accounts
  name: MethodFi Account Consent API
  phrasing_intents:
  - id: updateAccountConsent
    intent: Grant or withdraw consent on an account
    question: Can I withdraw data-access consent for a single account?
  phrasing_ops: 1
  slug: methodfi-account-consent-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Payment instruments for accounts
  name: MethodFi Account Payment Instruments API
  phrasing_intents:
  - id: listAccountPaymentInstruments
    intent: List payment instruments on an account
    question: Which payment instruments are attached to this account?
  - id: createAccountPaymentInstrument
    intent: Create a payment instrument for an account
    question: How do I create a new payment instrument for an account?
  - id: retrieveAccountPaymentInstrument
    intent: Get one payment instrument
    question: Can I look up a payment instrument's details by its ID?
  - id: closeAccountPaymentInstrument
    intent: Close a payment instrument
    question: How do I close a payment instrument I no longer need?
  phrasing_ops: 4
  slug: methodfi-account-payment-instruments-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Payoff data for accounts
  name: MethodFi Account Payoffs API
  phrasing_intents:
  - id: listAccountPayoffs
    intent: List payoff records for an account
    question: Where can I see every payoff quote pulled for a loan account?
  - id: createAccountPayoff
    intent: Request a new payoff amount for an account
    question: How do I get an up-to-date payoff amount for a loan?
  - id: retrieveAccountPayoff
    intent: Get one payoff record
    question: What payoff amount did a specific payoff sync return?
  phrasing_ops: 3
  slug: methodfi-account-payoffs-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Products associated with accounts
  name: MethodFi Account Products API
  phrasing_intents:
  - id: listAccountProducts
    intent: List products available on an account
    question: Which Method products are enabled or available for this account?
  - id: retrieveAccountProduct
    intent: Get one product on an account
    question: Is a specific product available for this account?
  phrasing_ops: 2
  slug: methodfi-account-products-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Sensitive data for accounts
  name: MethodFi Account Sensitive API
  phrasing_intents:
  - id: listAccountSensitives
    intent: List sensitive data requests for an account
    question: Which sensitive data requests have been made for this account?
  - id: createAccountSensitive
    intent: Request sensitive data for an account
    question: How do I request sensitive data for an account?
  - id: retrieveAccountSensitive
    intent: Get one sensitive data record
    question: Can I fetch a sensitive data record I already requested?
  phrasing_ops: 3
  slug: methodfi-account-sensitive-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Subscriptions for accounts
  name: MethodFi Account Subscriptions API
  phrasing_intents:
  - id: listAccountSubscriptions
    intent: List subscriptions on an account
    question: Which recurring updates is this account subscribed to?
  - id: createAccountSubscription
    intent: Subscribe an account to a product
    question: How do I enroll an account in a recurring subscription?
  - id: retrieveAccountSubscription
    intent: Get one account subscription
    question: Is a specific account subscription still active?
  - id: deleteAccountSubscription
    intent: Cancel an account subscription
    question: How do I stop recurring updates on an account?
  phrasing_ops: 4
  slug: methodfi-account-subscriptions-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Transactions for accounts
  name: MethodFi Account Transactions API
  phrasing_intents:
  - id: listAccountTransactions
    intent: List transactions on an account
    question: Can I pull an account's transactions between two dates?
  - id: retrieveAccountTransaction
    intent: Get one account transaction
    question: Can I look up the details of one transaction by its ID?
  phrasing_ops: 2
  slug: methodfi-account-transactions-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Update records for accounts
  name: MethodFi Account Updates API
  phrasing_intents:
  - id: listAccountUpdates
    intent: List update records for an account
    question: Where can I see each time an account's details were refreshed?
  - id: createAccountUpdate
    intent: Request a refresh of account details
    question: How do I ask Method to refresh an account's details on demand?
  - id: retrieveAccountUpdate
    intent: Get one account update
    question: What did a specific account update return?
  phrasing_ops: 3
  slug: methodfi-account-updates-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Verification sessions for accounts
  name: MethodFi Account Verification Sessions API
  phrasing_intents:
  - id: listAccountVerificationSessions
    intent: List verification sessions for an account
    question: Which verification attempts have been made on this account?
  - id: createAccountVerificationSession
    intent: Start verifying an account
    question: How do I begin verifying ownership of a bank account?
  - id: retrieveAccountVerificationSession
    intent: Get one account verification session
    question: Has a particular account verification session succeeded?
  - id: updateAccountVerificationSession
    intent: Submit details to verify an account
    question: How do I submit micro-deposit amounts to finish verifying an account?
  - id: retrieveAccountVerificationSessionAmounts
    intent: Get micro-deposit amounts for a session
    question: Where can I see the micro-deposit amounts sent for a verification session?
  phrasing_ops: 5
  slug: methodfi-account-verification-sessions-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Financial accounts (ACH, liability, clearing, debit card)
  name: MethodFi Accounts API
  phrasing_intents:
  - id: listAccounts
    intent: List accounts
    question: Can I list only the accounts that belong to one holder?
  - id: createAccount
    intent: Create an account for an entity
    question: How do I add a bank, liability, clearing or debit card account to an entity?
  - id: retrieveAccount
    intent: Get an account with expanded details
    question: Can I fetch an account and expand related objects in the same call?
  - id: updateAccount
    intent: Update an account's metadata or number
    question: How do I change the metadata stored on an account?
  - id: getAccount
    intent: Get an account (legacy unversioned path)
    question: Is there an older account lookup that takes acc_id without a version header?
  - id: getAccountBalance
    intent: Get an account's real-time balance
    question: How do I read the live balance straight from the account's institution?
  - id: getAccountPayoff
    intent: Get the payoff for an account
    question: What is the current payoff on this loan account?
  - id: createAccountVerificationSession
    intent: Verify an account via deposits or aggregator
    question: Can I verify an account through micro-deposits or an instant network check?
  phrasing_ops: 8
  slug: methodfi-accounts-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Card product definitions
  name: MethodFi Card Products API
  phrasing_intents:
  - id: retrieveCardProduct
    intent: Get a card product
    question: Can I look up the details of a specific card program?
  phrasing_ops: 1
  slug: methodfi-card-products-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Client-side Element endpoints
  name: MethodFi Elements API
  phrasing_intents:
  - id: elementsCreateToken
    intent: Create an element token for the frontend
    question: How do I generate a client-side token to launch an element for an entity?
  - id: elementsRetrieveSessionResults
    intent: Get the results of a completed element
    question: How do I get the data a user entered during an element flow?
  - id: elementsRetrieveSession
    intent: Get an element session
    question: Can I look up an element session by its session ID?
  - id: elementsUpdateSession
    intent: Update an element session
    question: Is it possible to modify an element session after it has started?
  - id: elementsExchangeAccount
    intent: Exchange account details for an element flow
    question: How do I exchange account information server-side during an element flow?
  phrasing_ops: 5
  slug: methodfi-elements-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Individuals, corporations, and receive-only entities
  name: MethodFi Entities API
  phrasing_intents:
  - id: listEntities
    intent: List entities
    question: Can I search my entities by name?
  - id: createEntity
    intent: Create an entity
    question: How do I create a new individual or corporation in Method?
  - id: retrieveEntity
    intent: Get an entity with expanded details
    question: Can I fetch an entity and expand its related objects at the same time?
  - id: updateEntity
    intent: Update an entity (versioned)
    question: How do I change an entity's address on the current API version?
  - id: getEntity
    intent: Get an entity (legacy unversioned path)
    question: Is there an older entity lookup that takes ent_id without a version header?
  - id: putEntitiesByEntId
    intent: Update an entity (legacy, type required)
    question: Does the legacy entity update require me to send the entity type?
  - id: retrieveEntityCreditScores
    intent: Get an entity's credit scores (legacy)
    question: Can I read a person's credit scores from the legacy ent_id endpoint?
  - id: createEntityVerificationSession
    intent: Start an SMS, KBA, SNA or BYO verification
    question: How do I start an SMS or KBA identity verification for an entity?
  phrasing_ops: 9
  slug: methodfi-entities-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Attribute data for entities
  name: MethodFi Entity Attributes API
  phrasing_intents:
  - id: listEntityAttributes
    intent: List attribute records for an entity
    question: Which attribute retrievals have been run on this person?
  - id: createEntityAttributes
    intent: Retrieve new attributes for an entity
    question: How do I pull a fresh set of attributes for an entity?
  - id: retrieveEntityAttribute
    intent: Get one entity attribute record
    question: What did a specific entity attribute retrieval return?
  phrasing_ops: 3
  slug: methodfi-entity-attributes-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Account connection sessions for entities
  name: MethodFi Entity Connects API
  phrasing_intents:
  - id: listEntityConnects
    intent: List connect sessions for an entity
    question: Which connect sessions have been run for this entity?
  - id: createEntityConnect
    intent: Discover an entity's liability accounts
    question: How do I find all of a person's liability accounts automatically?
  - id: retrieveEntityConnect
    intent: Get one entity connect session
    question: What did a particular connect session find for an entity?
  - id: createEntityManualConnect
    intent: Connect an entity using supplied tradelines
    question: Can I connect an entity using tradelines I already have from a bureau?
  - id: retrieveEntityManualConnect
    intent: Get one manual connect session
    question: What happened with a manual connect session I submitted?
  phrasing_ops: 5
  slug: methodfi-entity-connects-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Consent management for entities
  name: MethodFi Entity Consent API
  phrasing_intents:
  - id: updateEntityConsent
    intent: Grant or withdraw consent for an entity
    question: What call withdraws a person's consent across Method?
  phrasing_ops: 1
  slug: methodfi-entity-consent-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Credit score data for entities
  name: MethodFi Entity Credit Scores API
  phrasing_intents:
  - id: listEntityCreditScores
    intent: List credit scores pulled for an entity
    question: Can I see every credit score pulled for one person?
  - id: createEntityCreditScore
    intent: Pull a new credit score for an entity
    question: How do I request a fresh credit score for a person?
  - id: retrieveEntityCreditScore
    intent: Get one credit score record
    question: What score did a specific credit score request return?
  phrasing_ops: 3
  slug: methodfi-entity-credit-scores-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Identity verification data for entities
  name: MethodFi Entity Identities API
  phrasing_intents:
  - id: listEntityIdentities
    intent: List identity records for an entity
    question: Which identity retrievals have been run on this person?
  - id: createEntityIdentity
    intent: Retrieve identity data for an entity
    question: How do I pull identity information for a person in Method?
  - id: retrieveEntityIdentity
    intent: Get one identity record
    question: What did a specific identity retrieval return?
  phrasing_ops: 3
  slug: methodfi-entity-identities-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Products associated with entities
  name: MethodFi Entity Products API
  phrasing_intents:
  - id: listEntityProducts
    intent: List products available to an entity
    question: Which Method products can this entity use?
  - id: retrieveEntityProduct
    intent: Get one product for an entity
    question: Is a specific product available to this entity?
  phrasing_ops: 2
  slug: methodfi-entity-products-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Subscriptions for entities
  name: MethodFi Entity Subscriptions API
  phrasing_intents:
  - id: listEntitySubscriptions
    intent: List subscriptions for an entity
    question: Which subscriptions is this entity enrolled in?
  - id: createEntitySubscription
    intent: Subscribe an entity to a product
    question: How do I enroll an entity in a recurring subscription?
  - id: retrieveEntitySubscription
    intent: Get one entity subscription
    question: Is a specific entity subscription still active?
  - id: deleteEntitySubscription
    intent: Cancel an entity subscription
    question: How do I stop an entity's subscription?
  phrasing_ops: 4
  slug: methodfi-entity-subscriptions-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Vehicle data for entities
  name: MethodFi Entity Vehicles API
  phrasing_intents:
  - id: listEntityVehicles
    intent: List vehicles for an entity
    question: Which vehicles are on file for this person?
  - id: searchEntityVehicles
    intent: Search for an entity's vehicles
    question: How do I find vehicles associated with a person?
  - id: retrieveEntityVehicle
    intent: Get one vehicle record
    question: Can I look up a single vehicle record by its ID?
  phrasing_ops: 3
  slug: methodfi-entity-vehicles-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Verification sessions for entities
  name: MethodFi Entity Verification Sessions API
  phrasing_intents:
  - id: listEntityVerificationSessions
    intent: List verification sessions for an entity
    question: Which identity verifications has this entity gone through?
  - id: createEntityVerificationSession
    intent: Start an identity verification for an entity
    question: How do I verify a person's phone number by SMS?
  - id: retrieveEntityVerificationSession
    intent: Get one entity verification session
    question: Has a particular identity verification session passed?
  - id: updateEntityVerificationSession
    intent: Submit an SMS code or KBA answers
    question: How do I submit the SMS code a person received to finish verification?
  phrasing_ops: 4
  slug: methodfi-entity-verification-sessions-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Webhook event log
  name: MethodFi Events API
  phrasing_intents:
  - id: listEvents
    intent: List webhook events
    question: Can I list only events of a certain type?
  - id: retrieveEvent
    intent: Get one event
    question: Can I look up a single webhook event by its ID?
  phrasing_ops: 2
  slug: methodfi-events-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Request forwarding with sensitive data injection
  name: MethodFi Forwarding Requests API
  phrasing_intents:
  - id: createForwardingRequest
    intent: Forward a request with sensitive data injected
    question: How do I send sensitive data to a third-party endpoint without handling it myself?
  - id: retrieveForwardingRequest
    intent: Get a forwarding request
    question: Can I check the result of a forwarding request I sent?
  phrasing_ops: 2
  slug: methodfi-forwarding-requests-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Method-managed accounts
  name: MethodFi Managed Accounts API
  phrasing_intents:
  - id: listManagedAccounts
    intent: List the team's managed accounts
    question: Which managed accounts does my team have?
  - id: retrieveManagedAccount
    intent: Get a managed account
    question: Can I look up one managed account by its ID?
  - id: listManagedAccountTransactions
    intent: List transactions on a managed account
    question: How do I see money moving in and out of a managed account?
  phrasing_ops: 3
  slug: methodfi-managed-accounts-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Merchant directory
  name: MethodFi Merchants API
  phrasing_intents:
  - id: listMerchants
    intent: Search the merchant directory
    question: Can I find a lender in Method's merchant directory by name?
  - id: retrieveMerchant
    intent: Get a merchant (versioned)
    question: Which versioned call returns one merchant by mchId?
  - id: getMerchant
    intent: Get a merchant (legacy unversioned path)
    question: Is there an older merchant lookup that takes mch_id without a version header?
  phrasing_ops: 3
  slug: methodfi-merchants-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Opal client-side session and token management
  name: MethodFi Opal API
  phrasing_intents:
  - id: retrieveOpalToken
    intent: Get the current Opal session
    question: What state is the Opal session behind my token in?
  - id: createOpalToken
    intent: Create an Opal token and session
    question: How do I launch Opal for an existing entity in a given mode?
  - id: deactivateOpalToken
    intent: Deactivate the current Opal token
    question: How do I stop an Opal token from being used again?
  phrasing_ops: 3
  slug: methodfi-opal-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Reversals for payments
  name: MethodFi Payment Reversals API
  phrasing_intents:
  - id: listPaymentReversals
    intent: List reversals for a payment
    question: Has this payment been reversed, and how many times?
  - id: retrievePaymentReversal
    intent: Get one payment reversal
    question: Can I look up a specific reversal on a payment?
  - id: updatePaymentReversal
    intent: Change a payment reversal's status
    question: How do I update the status of a reversal?
  phrasing_ops: 3
  slug: methodfi-payment-reversals-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: ACH and clearing payments
  name: MethodFi Payments API
  phrasing_intents:
  - id: listPayments
    intent: List payments
    question: Can I list only the payments that failed?
  - id: createPayment
    intent: Send a payment between accounts
    question: How do I move money from a source account to a destination account?
  - id: retrievePayment
    intent: Get a payment with expanded details
    question: Can I fetch a payment and expand its source and destination?
  - id: deletePayment
    intent: Cancel a pending payment (versioned)
    question: How do I cancel a payment that hasn't been processed yet?
  - id: getPayment
    intent: Get a payment (legacy unversioned path)
    question: Is there an older payment lookup that takes pmt_id without a version header?
  - id: deletePaymentsByPmtId
    intent: Cancel a pending payment (legacy path)
    question: Can I cancel a pending payment through the older pmt_id endpoint?
  - id: createPaymentReversal
    intent: Reverse funds for a failed payment
    question: How do I balance funds after a payment fails?
  - id: listPaymentReversals
    intent: List reversals for a payment (legacy)
    question: Can I list a payment's reversals from the payments endpoints using pmt_id?
  phrasing_ops: 8
  slug: methodfi-payments-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Health check endpoint
  name: MethodFi Ping API
  phrasing_intents:
  - id: ping
    intent: Check that the API is reachable
    question: Is my API key working against Method right now?
  phrasing_ops: 1
  slug: methodfi-ping-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Public key discovery endpoints for Message-Level Encryption.
  name: MethodFi Public Keys API
  phrasing_intents:
  - id: listPublicJwks
    intent: List Method's public encryption keys
    question: Where do I get the public keys for message-level encryption?
  - id: retrievePublicJwk
    intent: Get one Method public key
    question: Can I fetch a single public encryption key by its ID?
  phrasing_ops: 2
  slug: methodfi-public-keys-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Downloadable reports
  name: MethodFi Reports API
  phrasing_intents:
  - id: createReport
    intent: Generate a report
    question: How do I generate a report of a given type?
  - id: retrieveReport
    intent: Check a report's status
    question: Is my report finished and ready to download?
  - id: downloadReport
    intent: Download a completed report as CSV
    question: How do I download a finished report as a CSV file?
  phrasing_ops: 3
  slug: methodfi-reports-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Secure secret storage
  name: MethodFi Secrets API
  phrasing_intents:
  - id: listSecrets
    intent: List stored secrets
    question: Which secrets have I stored, without exposing their values?
  - id: createSecret
    intent: Store a secret
    question: How do I store a sensitive value securely in Method?
  - id: retrieveSecret
    intent: Get a secret's details
    question: Can I look up a secret by its ID?
  - id: deleteSecret
    intent: Delete a secret
    question: How do I remove a secret I no longer need?
  phrasing_ops: 4
  slug: methodfi-secrets-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Sandbox account simulation
  name: MethodFi Simulate Accounts API
  phrasing_intents:
  - id: simulateRetrieveVerificationAmounts
    intent: Get sandbox micro-deposit amounts
    question: Where do I get the test micro-deposit amounts in sandbox?
  - id: simulateCreateAccountTransaction
    intent: Simulate a transaction in sandbox
    question: Can I create a fake transaction on an account to test my flow?
  - id: simulateCreateAccountCardBrand
    intent: Simulate a card brand result in sandbox
    question: Can I fake a card brand result to test card brand retrieval?
  phrasing_ops: 3
  slug: methodfi-simulate-accounts-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Sandbox entity simulation
  name: MethodFi Simulate Entities API
  phrasing_intents:
  - id: simulateEntityCreditScore
    intent: Simulate a credit score in sandbox
    question: Can I set a specific credit score for a test entity?
  - id: simulateEntityConnect
    intent: Simulate entity connect in sandbox
    question: Where do I test account discovery for an entity in sandbox?
  - id: simulateEntityAttributes
    intent: Simulate entity attributes in sandbox
    question: Can I generate fake attribute data for a test entity?
  phrasing_ops: 3
  slug: methodfi-simulate-entities-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Sandbox event simulation
  name: MethodFi Simulate Events API
  phrasing_intents:
  - id: simulateCreateEvent
    intent: Simulate a webhook event in sandbox
    question: Can I trigger a test webhook event to check my handler?
  phrasing_ops: 1
  slug: methodfi-simulate-events-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Sandbox payment simulation
  name: MethodFi Simulate Payments API
  phrasing_intents:
  - id: simulateUpdatePaymentStatus
    intent: Simulate a payment status change in sandbox
    question: Can I move a sandbox payment to a new status to test my flow?
  - id: simulatePostPaymentViaPaymentInstrument
    intent: Simulate a payment through a payment instrument
    question: Can I post a test payment through a payment instrument in sandbox?
  phrasing_ops: 2
  slug: methodfi-simulate-payments-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Team and API key management
  name: MethodFi Teams API
  phrasing_intents:
  - id: retrieveTeam
    intent: Get the current team
    question: Which team is my API key tied to?
  - id: createTeam
    intent: Create a child team
    question: How do I create a sub-team under my team?
  - id: createTeamEncryptionKey
    intent: Set the team's default encryption key
    question: How do I set the key used to encrypt sensitive data in responses?
  - id: listTeamPublicKeys
    intent: List the team's MLE public keys
    question: Which message-level encryption keys has my team registered?
  - id: createTeamPublicKey
    intent: Register an MLE public key
    question: How do I register my public key for message-level encryption?
  - id: retrieveTeamPublicKey
    intent: Get one MLE public key
    question: Can I look up one of my registered MLE keys by its ID?
  - id: deleteTeamPublicKey
    intent: Delete an MLE public key
    question: How do I remove an MLE public key from my team?
  phrasing_ops: 7
  slug: methodfi-teams-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Webhook subscriptions
  name: MethodFi Webhooks API
  phrasing_intents:
  - id: listWebhooks
    intent: List webhooks
    question: Which webhooks are active or need attention on my team?
  - id: createWebhook
    intent: Subscribe a URL to an event type
    question: How do I get notified at my URL when a given event happens?
  - id: retrieveWebhook
    intent: Get a webhook (versioned)
    question: Which versioned call returns one webhook by webhookId?
  - id: updateWebhook
    intent: Change a webhook's status
    question: How do I re-enable a webhook that was disabled?
  - id: deleteWebhook
    intent: Delete a webhook (versioned)
    question: How do I stop receiving events at a webhook on the current API version?
  - id: getWebhook
    intent: Get a webhook (legacy unversioned path)
    question: Is there an older webhook lookup that takes whk_id without a version header?
  - id: deleteWebhooksByWhkId
    intent: Delete a webhook (legacy path)
    question: Can I delete a webhook through the older whk_id endpoint?
  phrasing_ops: 7
  slug: methodfi-webhooks-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Liability discovery across Method's institution network.
  name: MethodFi Connect API
  phrasing_intents:
  - id: retrieveEntityConnect
    intent: Get liabilities discovered for an entity
    question: Which liability accounts did Method find for this person?
  phrasing_ops: 1
  slug: methodfi-connect-api
- baseURL: https://production.methodfi.com
  baseurl_source: declared
  description: Transaction history for an account.
  name: MethodFi Transactions API
  phrasing_intents:
  - id: listAccountTransactions
    intent: List transactions on an account
    question: Can I page through all the transactions on an account?
  phrasing_ops: 1
  slug: methodfi-transactions-api
artifact_total: 140
asyncapis:
- description: ''
  name: Methodfi Webhooks
  slug: methodfi-webhooks
collections:
- collection_type: postman
  name: Method Account Attributes API
  slug: postman-methodfi-account-attributes-api
- collection_type: postman
  name: Method Account Attributes Account Balances API
  slug: postman-methodfi-account-balances-api
- collection_type: postman
  name: Method Account Attributes Account Card Brands API
  slug: postman-methodfi-account-card-brands-api
- collection_type: postman
  name: Method Account Attributes Account Consent API
  slug: postman-methodfi-account-consent-api
- collection_type: postman
  name: Method Account Attributes Account Payment Instruments API
  slug: postman-methodfi-account-payment-instruments-api
- collection_type: postman
  name: Method Account Attributes Account Payoffs API
  slug: postman-methodfi-account-payoffs-api
- collection_type: postman
  name: Method Account Attributes Account Products API
  slug: postman-methodfi-account-products-api
- collection_type: postman
  name: Method Account Attributes Account Sensitive API
  slug: postman-methodfi-account-sensitive-api
- collection_type: postman
  name: Method Account Attributes Account Subscriptions API
  slug: postman-methodfi-account-subscriptions-api
- collection_type: postman
  name: Method Account Attributes Account Transactions API
  slug: postman-methodfi-account-transactions-api
- collection_type: postman
  name: Method Account Attributes Account Updates API
  slug: postman-methodfi-account-updates-api
- collection_type: postman
  name: Method Account Attributes Account Verification Sessions API
  slug: postman-methodfi-account-verification-sessions-api
- collection_type: postman
  name: Method Account Attributes Accounts API
  slug: postman-methodfi-accounts-api
- collection_type: postman
  name: Method Account Attributes Card Products API
  slug: postman-methodfi-card-products-api
- collection_type: postman
  name: Method Account Attributes Elements API
  slug: postman-methodfi-elements-api
- collection_type: postman
  name: Method Account Attributes Entities API
  slug: postman-methodfi-entities-api
- collection_type: postman
  name: Method Account Attributes Entity Attributes API
  slug: postman-methodfi-entity-attributes-api
- collection_type: postman
  name: Method Account Attributes Entity Connects API
  slug: postman-methodfi-entity-connects-api
- collection_type: postman
  name: Method Account Attributes Entity Consent API
  slug: postman-methodfi-entity-consent-api
- collection_type: postman
  name: Method Account Attributes Entity Credit Scores API
  slug: postman-methodfi-entity-credit-scores-api
- collection_type: postman
  name: Method Account Attributes Entity Identities API
  slug: postman-methodfi-entity-identities-api
- collection_type: postman
  name: Method Account Attributes Entity Products API
  slug: postman-methodfi-entity-products-api
- collection_type: postman
  name: Method Account Attributes Entity Subscriptions API
  slug: postman-methodfi-entity-subscriptions-api
- collection_type: postman
  name: Method Account Attributes Entity Vehicles API
  slug: postman-methodfi-entity-vehicles-api
- collection_type: postman
  name: Method Account Attributes Entity Verification Sessions API
  slug: postman-methodfi-entity-verification-sessions-api
- collection_type: postman
  name: Method Account Attributes Events API
  slug: postman-methodfi-events-api
- collection_type: postman
  name: Method Account Attributes Forwarding Requests API
  slug: postman-methodfi-forwarding-requests-api
- collection_type: postman
  name: Method Account Attributes Managed Accounts API
  slug: postman-methodfi-managed-accounts-api
- collection_type: postman
  name: Method Account Attributes Merchants API
  slug: postman-methodfi-merchants-api
- collection_type: postman
  name: Method Account Attributes Opal API
  slug: postman-methodfi-opal-api
- collection_type: postman
  name: Method Account Attributes Payment Reversals API
  slug: postman-methodfi-payment-reversals-api
- collection_type: postman
  name: Method Account Attributes Payments API
  slug: postman-methodfi-payments-api
- collection_type: postman
  name: Method Account Attributes Ping API
  slug: postman-methodfi-ping-api
- collection_type: postman
  name: Method Account Attributes Public Keys API
  slug: postman-methodfi-public-keys-api
- collection_type: postman
  name: Method Account Attributes Reports API
  slug: postman-methodfi-reports-api
- collection_type: postman
  name: Method Account Attributes Secrets API
  slug: postman-methodfi-secrets-api
- collection_type: postman
  name: Method Account Attributes Simulate Accounts API
  slug: postman-methodfi-simulate-accounts-api
- collection_type: postman
  name: Method Account Attributes Simulate Entities API
  slug: postman-methodfi-simulate-entities-api
- collection_type: postman
  name: Method Account Attributes Simulate Events API
  slug: postman-methodfi-simulate-events-api
- collection_type: postman
  name: Method Account Attributes Simulate Payments API
  slug: postman-methodfi-simulate-payments-api
- collection_type: postman
  name: Method Account Attributes Teams API
  slug: postman-methodfi-teams-api
- collection_type: postman
  name: Method Account Attributes Webhooks API
  slug: postman-methodfi-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Method Financial API
  slug: open-method-fi
- collection_type: open
  name: Method Account Attributes API
  slug: open-methodfi-account-attributes-api
- collection_type: open
  name: Method Account Attributes Account Balances API
  slug: open-methodfi-account-balances-api
- collection_type: open
  name: Method Account Attributes Account Card Brands API
  slug: open-methodfi-account-card-brands-api
- collection_type: open
  name: Method Account Attributes Account Consent API
  slug: open-methodfi-account-consent-api
- collection_type: open
  name: Method Account Attributes Account Payment Instruments API
  slug: open-methodfi-account-payment-instruments-api
- collection_type: open
  name: Method Account Attributes Account Payoffs API
  slug: open-methodfi-account-payoffs-api
- collection_type: open
  name: Method Account Attributes Account Products API
  slug: open-methodfi-account-products-api
- collection_type: open
  name: Method Account Attributes Account Sensitive API
  slug: open-methodfi-account-sensitive-api
- collection_type: open
  name: Method Account Attributes Account Subscriptions API
  slug: open-methodfi-account-subscriptions-api
- collection_type: open
  name: Method Account Attributes Account Transactions API
  slug: open-methodfi-account-transactions-api
- collection_type: open
  name: Method Account Attributes Account Updates API
  slug: open-methodfi-account-updates-api
- collection_type: open
  name: Method Account Attributes Account Verification Sessions API
  slug: open-methodfi-account-verification-sessions-api
- collection_type: open
  name: Method Account Attributes Accounts API
  slug: open-methodfi-accounts-api
- collection_type: open
  name: Method Account Attributes Card Products API
  slug: open-methodfi-card-products-api
- collection_type: open
  name: Method Financial Accounts Connect API
  slug: open-methodfi-connect-api
- collection_type: open
  name: Method Account Attributes Elements API
  slug: open-methodfi-elements-api
- collection_type: open
  name: Method Account Attributes Entities API
  slug: open-methodfi-entities-api
- collection_type: open
  name: Method Account Attributes Entity Attributes API
  slug: open-methodfi-entity-attributes-api
- collection_type: open
  name: Method Account Attributes Entity Connects API
  slug: open-methodfi-entity-connects-api
- collection_type: open
  name: Method Account Attributes Entity Consent API
  slug: open-methodfi-entity-consent-api
- collection_type: open
  name: Method Account Attributes Entity Credit Scores API
  slug: open-methodfi-entity-credit-scores-api
- collection_type: open
  name: Method Account Attributes Entity Identities API
  slug: open-methodfi-entity-identities-api
- collection_type: open
  name: Method Account Attributes Entity Products API
  slug: open-methodfi-entity-products-api
- collection_type: open
  name: Method Account Attributes Entity Subscriptions API
  slug: open-methodfi-entity-subscriptions-api
- collection_type: open
  name: Method Account Attributes Entity Vehicles API
  slug: open-methodfi-entity-vehicles-api
- collection_type: open
  name: Method Account Attributes Entity Verification Sessions API
  slug: open-methodfi-entity-verification-sessions-api
- collection_type: open
  name: Method Account Attributes Events API
  slug: open-methodfi-events-api
- collection_type: open
  name: Method Account Attributes Forwarding Requests API
  slug: open-methodfi-forwarding-requests-api
- collection_type: open
  name: Method Account Attributes Managed Accounts API
  slug: open-methodfi-managed-accounts-api
- collection_type: open
  name: Method Account Attributes Merchants API
  slug: open-methodfi-merchants-api
- collection_type: open
  name: Method Account Attributes Opal API
  slug: open-methodfi-opal-api
- collection_type: open
  name: Method Account Attributes Payment Reversals API
  slug: open-methodfi-payment-reversals-api
- collection_type: open
  name: Method Account Attributes Payments API
  slug: open-methodfi-payments-api
- collection_type: open
  name: Method Account Attributes Ping API
  slug: open-methodfi-ping-api
- collection_type: open
  name: Method Account Attributes Public Keys API
  slug: open-methodfi-public-keys-api
- collection_type: open
  name: Method Account Attributes Reports API
  slug: open-methodfi-reports-api
- collection_type: open
  name: Method Account Attributes Secrets API
  slug: open-methodfi-secrets-api
- collection_type: open
  name: Method Account Attributes Simulate Accounts API
  slug: open-methodfi-simulate-accounts-api
- collection_type: open
  name: Method Account Attributes Simulate Entities API
  slug: open-methodfi-simulate-entities-api
- collection_type: open
  name: Method Account Attributes Simulate Events API
  slug: open-methodfi-simulate-events-api
- collection_type: open
  name: Method Account Attributes Simulate Payments API
  slug: open-methodfi-simulate-payments-api
- collection_type: open
  name: Method Account Attributes Teams API
  slug: open-methodfi-teams-api
- collection_type: open
  name: Method Financial Accounts Transactions API
  slug: open-methodfi-transactions-api
- collection_type: open
  name: Method Account Attributes Webhooks API
  slug: open-methodfi-webhooks-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/capabilities/methodfi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/methodfi-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/overlays/methodfi-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/methodfi-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/methodfi/overview
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/security/methodfi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/methodfi-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/agentic-access/methodfi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/methodfi-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/authentication/methodfi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/methodfi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/conventions/methodfi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/methodfi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/conventions/methodfi-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/methodfi-conventions.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/packages/methodfi-packages.yml
  title: ''
  type: Packages
  url: packages/methodfi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/packages/methodfi-packages.yml
  title: ''
  type: SDKs
  url: packages/methodfi-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/components/methodfi-components.yml
  title: ''
  type: Components
  url: components/methodfi-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/sandbox/methodfi-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/methodfi-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/lifecycle/methodfi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/methodfi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://methodfi.statuspage.io
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/lifecycle/methodfi-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/methodfi-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/conformance/methodfi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/methodfi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://methodfi.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/errors/methodfi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/methodfi-problem-types.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/errors/methodfi-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/methodfi-decline-codes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/changelog/methodfi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/methodfi-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/data-model/methodfi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/methodfi-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/asyncapi/methodfi-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/methodfi-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/rate-limits/methodfi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/methodfi-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/mcp/methodfi-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/methodfi-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/llms/methodfi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/methodfi-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://methodfi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.methodfi.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.methodfi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.methodfi.com/reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.methodfi.com/guides/quickstart
- group: operate
  title: ''
  type: Support
  url: https://methodfi.com/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MethodFi
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/methodfi/method-api
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.methodfi.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://methodfi.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://methodfi.com/privacy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/security/methodfi-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/methodfi-trust-center.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/methodfi
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/plans/methodfi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/methodfi-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/finops/methodfi-finops.yml
  title: ''
  type: FinOps
  url: finops/methodfi-finops.yml
created: '2026-07-17'
description: Method (Method Financial) is the infrastructure layer for consumer liability data and payments. Its API lets developers create entities, verify identity, and use Connect to discover a user's complete liability picture across 15,000+ institutions (credit cards, auto loans, student loans, mortgages, personal loans) without credential sharing, then normalize that data and move money via ACH to pay down those liabilities. Additional products include credit scores, card-brand enrichment, financial attributes, transactions, updates/subscriptions for monitoring, reports, and embeddable UI (Opal/Elements). Method powers lending, personal finance management, and commerce/card-linking use cases.
finops:
- name: Methodfi Finops
  service_category: Financial Services
  slug: methodfi-finops
image: https://framerusercontent.com/assets/ZHgWyxIoZ4u3muxNTrEuOhP9o.jpg
layout: provider
modified: '2026-08-08'
name: Method Financial
nav: Providers
network: true
overview: 'Method Financial publishes 44 APIs on the [APIs.io](https://apis.io/) network, including MethodFi Account Attributes API, MethodFi Account Balances API, MethodFi Account Card Brands API, and 41 more. Tagged areas include Company, Fintech, Liability Data, Payments, and Lending.


  The Method Financial catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Method Financial''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 34 more developer resources.'
plans:
- name: Methodfi Plans Pricing
  plan_count: 2
  slug: methodfi-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Methodfi Rate Limits
  slug: methodfi-rate-limits
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 27
    catalog_earned: 59.2
    catalog_earned_first_party: 12.0
    catalog_gap: 55.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.7
    contract_governance: 18.2
    contract_quality: 62.5
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 81.6
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/methodfi/refs/heads/main/screenshots/methodfi-2026-08-07T172708.png
security:
- kind: authentication
  name: Methodfi Authentication
  slug: methodfi-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Methodfi Domain Security
  slug: methodfi-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Methodfi Trust Center
  slug: methodfi-trust-center
  summary_line: SOC 2, PCI DSS
slug: methodfi
tags:
- Company
- Fintech
- Liability Data
- Payments
- Lending
- Personal Finance
- Credit
- ACH
- Debt
- Identity Verification
website: https://methodfi.com
---
