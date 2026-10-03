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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 107
  human_in_the_loop: 1
  name: Gerencianet Agentic Access
  operation_count: 169
  slug: gerencianet-agentic-access
  summary_line: 169 operations · 107 acting · 1 human-in-the-loop
api_count: 6
apis:
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Account API from Efí Pay (Gerencianet) — 2 operation(s) for account.
  name: Efí Pay (Gerencianet) Account API
  phrasing_intents:
  - id: getAccountBalance
    intent: Check the account balance
    question: What is the current balance in my Efí Pay account?
  - id: listAccountConfig
    intent: View the account's Pix settings
    question: Where can I see the settings configured on my Pix account?
  - id: updateAccountConfig
    intent: Change the account's Pix settings
    question: Can I change the configuration of my Pix account through the API?
  phrasing_ops: 3
  slug: gerencianet-account-api
- baseURL: https://abrircontas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Accounts API from Efí Pay (Gerencianet) — 3 operation(s) for accounts.
  name: Efí Pay (Gerencianet) Accounts API
  phrasing_intents:
  - id: createAccount
    intent: Open a simplified account
    question: How do I open a simplified account for one of my customers?
  - id: getAccountCertificate
    intent: Generate a certificate for a simplified account
    question: Can I generate the API certificate for a simplified account I opened?
  - id: getAccountCredentials
    intent: Get a simplified account's API credentials
    question: Where do I get the client credentials for a simplified account?
  phrasing_ops: 3
  slug: gerencianet-accounts-api
- baseURL: https://cobrancas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Authorization API from Efí Pay (Gerencianet) — 2 operation(s) for authorization.
  name: Efí Pay (Gerencianet) Authorization API
  phrasing_intents:
  - id: authorize
    intent: Get an access token for the billing API
    question: How do I get an OAuth2 access token for the Cobranças billing API?
  - id: contasAuthorize
    intent: Get an access token for the accounts API
    question: Which endpoint issues the token for the Contas simplified accounts API?
  phrasing_ops: 2
  slug: gerencianet-authorization-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Automatic Charges API from Efí Pay (Gerencianet) — 3 operation(s) for automatic charges.
  name: Efí Pay (Gerencianet) Automatic Charges API
  phrasing_intents:
  - id: pixCreateAutomaticCharge
    intent: Create a Pix Automático charge
    question: Can I create an automatic Pix charge and let the system assign its txid?
  - id: pixListAutomaticCharge
    intent: List Pix Automático charges
    question: How do I see all the Pix Automático charges I've issued?
  - id: pixCreateAutomaticChargeTxid
    intent: Create a Pix Automático charge with my own txid
    question: Can I choose the txid myself when creating an automatic Pix charge?
  - id: pixUpdateAutomaticCharge
    intent: Update a Pix Automático charge
    question: Can I change an automatic Pix charge after it was created?
  - id: pixDetailAutomaticCharge
    intent: Get a Pix Automático charge
    question: Can I look up one automatic Pix charge by its txid?
  - id: pixRetryRequestAutomaticCharge
    intent: Retry a failed Pix Automático charge
    question: If an automatic Pix charge fails, can I schedule a retry for another date?
  phrasing_ops: 6
  slug: gerencianet-automatic-charges-api
- baseURL: https://openfinance.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Automatic Pix API from Efí Pay (Gerencianet) — 2 operation(s) for automatic pix.
  name: Efí Pay (Gerencianet) Automatic Pix API
  phrasing_intents:
  - id: ofCreateAutomaticEnrollment
    intent: Enroll a payer in Pix Automático via Open Finance
    question: Can I ask a payer to authorize Pix Automático through Open Finance?
  - id: ofListAutomaticEnrollment
    intent: List Open Finance Pix Automático enrollments
    question: How do I see the Pix Automático enrollments made through Open Finance?
  - id: ofUpdateAutomaticEnrollment
    intent: Update a Pix Automático enrollment
    question: Can I change an Open Finance Pix Automático enrollment after it was set up?
  - id: ofCreateAutomaticPixPayment
    intent: Initiate a Pix Automático payment
    question: Can I trigger a payment under an existing Pix Automático enrollment?
  - id: ofListAutomaticPixPayment
    intent: List Open Finance Pix Automático payments
    question: How can I see the payments collected under Pix Automático enrollments?
  - id: ofCancelAutomaticPixPayment
    intent: Cancel a Pix Automático payment
    question: Can I cancel an automatic Pix payment before it settles?
  phrasing_ops: 6
  slug: gerencianet-automatic-pix-api
- baseURL: https://pagarcontas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Bill Payments API from Efí Pay (Gerencianet) — 3 operation(s) for bill payments.
  name: Efí Pay (Gerencianet) Bill Payments API
  phrasing_intents:
  - id: payDetailBarCode
    intent: Look up a bill by its barcode
    question: Can I check what a boleto or bill is for before paying it?
  - id: payRequestBarCode
    intent: Pay a bill by barcode
    question: How do I pay a boleto from my account using its barcode?
  - id: payDetailPayment
    intent: Get a bill payment
    question: Can I check the status of a bill payment I already requested?
  - id: payListPayments
    intent: List bill payments
    question: Which bills have I paid from my Efí account?
  phrasing_ops: 4
  slug: gerencianet-bill-payments-api
- baseURL: https://openfinance.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Biometric Pix API from Efí Pay (Gerencianet) — 2 operation(s) for biometric pix.
  name: Efí Pay (Gerencianet) Biometric Pix API
  phrasing_intents:
  - id: ofCreateBiometricEnrollment
    intent: Create a biometric Pix enrollment
    question: Can I link a payer so they can pay Pix with biometrics?
  - id: ofListBiometricEnrollment
    intent: List biometric Pix enrollments
    question: How do I see the devices or payers linked for biometric Pix?
  - id: ofRevokeBiometricEnrollment
    intent: Revoke a biometric Pix enrollment
    question: Can I revoke a biometric enrollment so it can no longer authorize payments?
  - id: ofCreateBiometricPixPayment
    intent: Initiate a biometric Pix payment
    question: How do I start a Pix payment that the payer approves with biometrics?
  - id: ofListBiometricPixPayment
    intent: List biometric Pix payments
    question: Which Pix payments were authorized with biometrics?
  phrasing_ops: 5
  slug: gerencianet-biometric-pix-api
- baseURL: https://cobrancas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Card Payments API from Efí Pay (Gerencianet) — 3 operation(s) for card payments.
  name: Efí Pay (Gerencianet) Card Payments API
  phrasing_intents:
  - id: cardPaymentRetry
    intent: Retry a declined card payment
    question: Can I retry a credit card charge that was declined?
  - id: refundCard
    intent: Refund a card charge
    question: How do I refund a credit card charge?
  - id: getInstallments
    intent: Get card installment options
    question: How many installments can a customer split a card payment into?
  phrasing_ops: 3
  slug: gerencianet-card-payments-api
- baseURL: https://cobrancas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Carnets API from Efí Pay (Gerencianet) — 12 operation(s) for carnets.
  name: Efí Pay (Gerencianet) Carnets API
  phrasing_intents:
  - id: createCarnet
    intent: Create a carnet of installment boletos
    question: How do I issue a carnê so a customer pays in monthly boletos?
  - id: detailCarnet
    intent: Get a carnet
    question: Can I look up a carnet and see its installments?
  - id: updateCarnetParcels
    intent: Update several carnet parcels at once
    question: Can I update several parcels of a carnet at once?
  - id: updateCarnetParcel
    intent: Update one carnet parcel
    question: Can I change just one installment of a carnet?
  - id: cancelCarnetParcel
    intent: Cancel one carnet parcel
    question: Can I cancel a single installment without cancelling the whole carnet?
  - id: settleCarnetParcel
    intent: Mark one carnet parcel as paid
    question: Can I mark a carnet installment as paid when the customer paid outside the system?
  - id: sendCarnetParcelEmail
    intent: Email one carnet parcel to the customer
    question: Can I resend just one installment's boleto by email?
  - id: cancelCarnet
    intent: Cancel a whole carnet
    question: Can I cancel an entire carnê and all its open installments?
  phrasing_ops: 12
  slug: gerencianet-carnets-api
- baseURL: https://cobrancas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Charges API from Efí Pay (Gerencianet) — 12 operation(s) for charges.
  name: Efí Pay (Gerencianet) Charges API
  phrasing_intents:
  - id: createCharge
    intent: Create a charge
    question: How do I create a charge before choosing how the customer pays?
  - id: createOneStepCharge
    intent: Create and pay a charge in one step
    question: Can I create a charge and set its boleto or card payment in a single call?
  - id: detailCharge
    intent: Get a charge
    question: Can I look up a single charge and see whether it's paid?
  - id: listCharges
    intent: List charges
    question: Which charges have I issued?
  - id: cancelCharge
    intent: Cancel a charge
    question: Can I cancel a charge the customer hasn't paid?
  - id: definePayMethod
    intent: Set the payment method on a charge
    question: How do I turn an existing charge into a boleto or card payment?
  - id: updateBillet
    intent: Update an issued boleto
    question: Can I modify a boleto I already issued?
  - id: sendBilletEmail
    intent: Email a boleto to the customer
    question: Can I resend a boleto to the customer by email?
  phrasing_ops: 12
  slug: gerencianet-charges-api
- baseURL: https://openfinance.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Configuration API from Efí Pay (Gerencianet) — 1 operation(s) for configuration.
  name: Efí Pay (Gerencianet) Configuration API
  phrasing_intents:
  - id: ofConfigDetail
    intent: View the Open Finance configuration
    question: Where can I see my Open Finance integration settings?
  - id: ofConfigUpdate
    intent: Update the Open Finance configuration
    question: Can I change my Open Finance integration settings?
  phrasing_ops: 2
  slug: gerencianet-configuration-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Devolutions API from Efí Pay (Gerencianet) — 1 operation(s) for devolutions.
  name: Efí Pay (Gerencianet) Devolutions API
  phrasing_intents:
  - id: pixDevolution
    intent: Refund a received Pix
    question: How do I send money back to someone who paid me by Pix?
  - id: pixDetailDevolution
    intent: Get a Pix refund
    question: Can I check the status of a refund I made on a received Pix?
  phrasing_ops: 2
  slug: gerencianet-devolutions-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Due Charge Batches API from Efí Pay (Gerencianet) — 2 operation(s) for due charge batches.
  name: Efí Pay (Gerencianet) Due Charge Batches API
  phrasing_intents:
  - id: pixListDueChargeBatch
    intent: List batches of Pix due charges
    question: Which batches of due-date Pix charges have I submitted?
  - id: pixCreateDueChargeBatch
    intent: Create a batch of Pix due charges
    question: How do I issue many Pix charges with due dates in one request?
  - id: pixUpdateDueChargeBatch
    intent: Update charges in a due charge batch
    question: Can I change charges inside a batch I already submitted?
  - id: pixDetailDueChargeBatch
    intent: Get a batch of Pix due charges
    question: Can I check how each charge in a batch was processed?
  phrasing_ops: 4
  slug: gerencianet-due-charge-batches-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Due Charges API from Efí Pay (Gerencianet) — 2 operation(s) for due charges.
  name: Efí Pay (Gerencianet) Due Charges API
  phrasing_intents:
  - id: pixListDueCharges
    intent: List Pix charges with due dates
    question: Which Pix charges with due dates have I issued?
  - id: pixCreateDueCharge
    intent: Create a Pix charge with a due date
    question: How do I issue a Pix charge that has a due date?
  - id: pixUpdateDueCharge
    intent: Update a Pix charge with a due date
    question: Can I change a cobv charge after issuing it?
  - id: pixDetailDueCharge
    intent: Get a Pix charge with a due date
    question: Can I look up a due-date Pix charge by txid?
  phrasing_ops: 4
  slug: gerencianet-due-charges-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Immediate Charges API from Efí Pay (Gerencianet) — 2 operation(s) for immediate charges.
  name: Efí Pay (Gerencianet) Immediate Charges API
  phrasing_intents:
  - id: pixCreateImmediateCharge
    intent: Create an immediate Pix charge
    question: How do I create a Pix charge and let the system generate the txid?
  - id: pixListCharges
    intent: List immediate Pix charges
    question: Which immediate Pix charges have I created?
  - id: pixCreateCharge
    intent: Create an immediate Pix charge with my own txid
    question: Can I choose the txid when creating an immediate Pix charge?
  - id: pixUpdateCharge
    intent: Update an immediate Pix charge
    question: Can I change an immediate Pix charge before it's paid?
  - id: pixDetailCharge
    intent: Get an immediate Pix charge
    question: Can I look up an immediate Pix charge by txid?
  phrasing_ops: 5
  slug: gerencianet-immediate-charges-api
- baseURL: https://openfinance.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Immediate Pix API from Efí Pay (Gerencianet) — 2 operation(s) for immediate pix.
  name: Efí Pay (Gerencianet) Immediate Pix API
  phrasing_intents:
  - id: ofStartPixPayment
    intent: Initiate a Pix payment via Open Finance
    question: How do I start a Pix payment from the payer's bank through Open Finance?
  - id: ofListPixPayment
    intent: List Open Finance Pix payments
    question: Which Pix payments have I initiated through Open Finance?
  - id: ofDevolutionPix
    intent: Refund an Open Finance Pix payment
    question: Can I refund a Pix payment that was initiated through Open Finance?
  phrasing_ops: 3
  slug: gerencianet-immediate-pix-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Locations API from Efí Pay (Gerencianet) — 3 operation(s) for locations.
  name: Efí Pay (Gerencianet) Locations API
  phrasing_intents:
  - id: pixCreateLocation
    intent: Create a Pix payload location
    question: How do I create a location to attach to a Pix charge?
  - id: pixLocationList
    intent: List Pix payload locations
    question: Which Pix locations have I created for QR codes?
  - id: pixDetailLocation
    intent: Get a Pix payload location
    question: Can I look up a Pix location and see which txid it's linked to?
  - id: pixUnlinkTxidLocation
    intent: Detach a charge from a Pix location
    question: Can I unlink a txid from a location so it can be reused?
  phrasing_ops: 4
  slug: gerencianet-locations-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The MED Infractions API from Efí Pay (Gerencianet) — 2 operation(s) for med infractions.
  name: Efí Pay (Gerencianet) MED Infractions API
  phrasing_intents:
  - id: medList
    intent: List MED infraction reports
    question: Which MED fraud reports have been opened against Pix I received?
  - id: medDefense
    intent: Submit a defense for a MED infraction
    question: How do I contest a MED infraction report?
  phrasing_ops: 2
  slug: gerencianet-med-infractions-api
- baseURL: https://cobrancas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Notifications API from Efí Pay (Gerencianet) — 1 operation(s) for notifications.
  name: Efí Pay (Gerencianet) Notifications API
  phrasing_intents:
  - id: getNotification
    intent: Read a charge notification
    question: When I receive a notification token, how do I see what changed?
  phrasing_ops: 1
  slug: gerencianet-notifications-api
- baseURL: https://openfinance.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Participants API from Efí Pay (Gerencianet) — 1 operation(s) for participants.
  name: Efí Pay (Gerencianet) Participants API
  phrasing_intents:
  - id: ofListParticipants
    intent: List Open Finance participant banks
    question: Which banks can my customers pay from through Open Finance?
  phrasing_ops: 1
  slug: gerencianet-participants-api
- baseURL: https://cobrancas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Payment Links API from Efí Pay (Gerencianet) — 3 operation(s) for payment links.
  name: Efí Pay (Gerencianet) Payment Links API
  phrasing_intents:
  - id: createOneStepLink
    intent: Create a payment link in one step
    question: Can I create a charge and its payment link in a single call?
  - id: linkCharge
    intent: Create a payment link for an existing charge
    question: How do I turn an existing charge into a payment link?
  - id: updateChargeLink
    intent: Update a charge's payment link
    question: Can I change a payment link after it was generated?
  - id: sendLinkEmail
    intent: Email a payment link to the customer
    question: Can I resend a payment link by email?
  phrasing_ops: 4
  slug: gerencianet-payment-links-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Pix Keys API from Efí Pay (Gerencianet) — 3 operation(s) for pix keys.
  name: Efí Pay (Gerencianet) Pix Keys API
  phrasing_intents:
  - id: pixCreateEvp
    intent: Create a random Pix key
    question: How do I create a new random Pix key?
  - id: pixListEvp
    intent: List random Pix keys
    question: Which random Pix keys are registered on my account?
  - id: pixDeleteEvp
    intent: Delete a random Pix key
    question: Can I remove a random Pix key I no longer use?
  - id: pixKeysBucket
    intent: Check the Pix keys bucket
    question: Where do I check the Pix keys bucket for my account?
  phrasing_ops: 4
  slug: gerencianet-pix-keys-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Pix Send API from Efí Pay (Gerencianet) — 6 operation(s) for pix send.
  name: Efí Pay (Gerencianet) Pix Send API
  phrasing_intents:
  - id: pixSend
    intent: Send a Pix payment
    question: How do I send money by Pix from my account to a key?
  - id: pixQrCodePay
    intent: Pay a Pix QR code
    question: Can I pay a Pix QR code from my account through the API?
  - id: pixSendSameOwnership
    intent: Send Pix to my own account elsewhere
    question: Can I move money by Pix to another account in my own name?
  - id: pixSendList
    intent: List Pix I sent
    question: Which Pix transfers have I sent?
  - id: pixSendDetail
    intent: Get a sent Pix by end-to-end id
    question: Can I look up a Pix I sent by its end-to-end id?
  - id: pixSendDetailId
    intent: Get a sent Pix by my send id
    question: Can I find an outgoing Pix using the send id I chose?
  phrasing_ops: 6
  slug: gerencianet-pix-send-api
- baseURL: https://cobrancas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Plans API from Efí Pay (Gerencianet) — 3 operation(s) for plans.
  name: Efí Pay (Gerencianet) Plans API
  phrasing_intents:
  - id: listPlans
    intent: List subscription plans
    question: Which subscription plans have I created?
  - id: createPlan
    intent: Create a subscription plan
    question: How do I set up a recurring billing plan?
  - id: updatePlan
    intent: Update a subscription plan
    question: Can I rename or edit a plan I already created?
  - id: deletePlan
    intent: Delete a subscription plan
    question: Can I delete a plan I no longer offer?
  phrasing_ops: 4
  slug: gerencianet-plans-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The QR Codes API from Efí Pay (Gerencianet) — 2 operation(s) for qr codes.
  name: Efí Pay (Gerencianet) QR Codes API
  phrasing_intents:
  - id: pixGenerateQRCode
    intent: Generate a QR code for a Pix location
    question: How do I get the QR code image for a Pix charge's location?
  - id: pixQrCodeDetail
    intent: Decode a Pix QR code
    question: Can I see what a Pix QR code is charging before I pay it?
  phrasing_ops: 2
  slug: gerencianet-qr-codes-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Receipts API from Efí Pay (Gerencianet) — 1 operation(s) for receipts.
  name: Efí Pay (Gerencianet) Receipts API
  phrasing_intents:
  - id: pixGetReceipt
    intent: Get a Pix receipt
    question: Can I download the receipt for a Pix transaction?
  phrasing_ops: 1
  slug: gerencianet-receipts-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Received Pix API from Efí Pay (Gerencianet) — 2 operation(s) for received pix.
  name: Efí Pay (Gerencianet) Received Pix API
  phrasing_intents:
  - id: pixReceivedList
    intent: List Pix I received
    question: Which Pix payments have I received?
  - id: pixDetailReceived
    intent: Get a received Pix
    question: Can I look up an incoming Pix by its end-to-end id?
  phrasing_ops: 2
  slug: gerencianet-received-pix-api
- baseURL: https://openfinance.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Recurring Pix API from Efí Pay (Gerencianet) — 11 operation(s) for recurring pix.
  name: Efí Pay (Gerencianet) Recurring Pix API
  phrasing_intents:
  - id: ofStartRecurrencyPixPayment
    intent: Start an Open Finance recurring Pix payment
    question: How do I set up a repeating Pix payment through Open Finance?
  - id: ofListRecurrencyPixPayment
    intent: List Open Finance recurring Pix payments
    question: Which recurring Pix payments have I set up through Open Finance?
  - id: ofCancelRecurrencyPix
    intent: Cancel an Open Finance recurring Pix payment
    question: Can I cancel a recurring Pix series I started through Open Finance?
  - id: ofDevolutionRecurrencyPix
    intent: Refund an Open Finance recurring Pix payment
    question: Can I refund a payment from an Open Finance recurring series?
  - id: ofReplaceRecurrencyPixParcel
    intent: Replace one installment of a recurring Pix
    question: Can I replace a single installment within an Open Finance recurring payment?
  - id: pixCreateRecurrenceAutomatic
    intent: Create a Pix Automático recurrence
    question: How do I register a new Pix Automático recurrence for a customer?
  - id: pixListRecurrenceAutomatic
    intent: List Pix Automático recurrences
    question: Which Pix Automático recurrences have I registered as a biller?
  - id: pixDetailRecurrenceAutomatic
    intent: Get a Pix Automático recurrence
    question: Can I check whether a payer has authorized a Pix Automático recurrence?
  phrasing_ops: 16
  slug: gerencianet-recurring-pix-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Reports API from Efí Pay (Gerencianet) — 2 operation(s) for reports.
  name: Efí Pay (Gerencianet) Reports API
  phrasing_intents:
  - id: createReport
    intent: Request a reconciliation report
    question: How do I generate a statement reconciliation report?
  - id: detailReport
    intent: Get a reconciliation report
    question: Is my reconciliation report ready to download?
  phrasing_ops: 2
  slug: gerencianet-reports-api
- baseURL: https://openfinance.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Scheduled Pix API from Efí Pay (Gerencianet) — 3 operation(s) for scheduled pix.
  name: Efí Pay (Gerencianet) Scheduled Pix API
  phrasing_intents:
  - id: ofStartSchedulePixPayment
    intent: Schedule a Pix payment via Open Finance
    question: How do I schedule a Pix payment for a later date through Open Finance?
  - id: ofListSchedulePixPayment
    intent: List scheduled Open Finance Pix payments
    question: Which future-dated Pix payments have I scheduled through Open Finance?
  - id: ofCancelSchedulePix
    intent: Cancel a scheduled Pix payment
    question: Can I cancel a scheduled Pix before its date arrives?
  - id: ofDevolutionSchedulePix
    intent: Refund a scheduled Pix payment
    question: Can I refund a scheduled Pix payment after it was paid?
  phrasing_ops: 4
  slug: gerencianet-scheduled-pix-api
- baseURL: https://extratos.api.efipay.com.br/v1
  baseurl_source: spec
  description: The SFTP API from Efí Pay (Gerencianet) — 1 operation(s) for sftp.
  name: Efí Pay (Gerencianet) SFTP API
  phrasing_intents:
  - id: createSftpKey
    intent: Generate an SFTP key pair for statements
    question: How do I get SFTP keys to pick up my CNAB statement files?
  phrasing_ops: 1
  slug: gerencianet-sftp-api
- baseURL: https://pix.api.efipay.com.br
  baseurl_source: spec
  description: The Splits API from Efí Pay (Gerencianet) — 6 operation(s) for splits.
  name: Efí Pay (Gerencianet) Splits API
  phrasing_intents:
  - id: pixSplitDetailCharge
    intent: See the split on an immediate Pix charge
    question: Can I see how an immediate Pix charge's money is split?
  - id: pixSplitLinkCharge
    intent: Apply a split to an immediate Pix charge
    question: How do I split an immediate Pix charge between accounts?
  - id: pixSplitUnlinkCharge
    intent: Remove a split from an immediate Pix charge
    question: Can I remove a split from an immediate Pix charge?
  - id: pixSplitDetailDueCharge
    intent: See the split on a Pix due charge
    question: Can I see how a due-date Pix charge's money is split?
  - id: pixSplitLinkDueCharge
    intent: Apply a split to a Pix due charge
    question: How do I split a due-date Pix charge between accounts?
  - id: pixSplitUnlinkDueCharge
    intent: Remove a split from a Pix due charge
    question: Can I remove a split from a due-date Pix charge?
  - id: pixSplitConfig
    intent: Create a Pix split configuration
    question: How do I define how Pix payments are divided among accounts?
  - id: pixSplitConfigId
    intent: Create or update a split configuration by id
    question: Can I change an existing split configuration?
  phrasing_ops: 9
  slug: gerencianet-splits-api
- baseURL: https://extratos.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Statement Files API from Efí Pay (Gerencianet) — 2 operation(s) for statement files.
  name: Efí Pay (Gerencianet) Statement Files API
  phrasing_intents:
  - id: listStatementFiles
    intent: List CNAB statement files
    question: Which CNAB statement files are available for my account?
  - id: getStatementFile
    intent: Download a CNAB statement file
    question: How do I download a specific CNAB statement file?
  phrasing_ops: 2
  slug: gerencianet-statement-files-api
- baseURL: https://extratos.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Statement Schedules API from Efí Pay (Gerencianet) — 3 operation(s) for statement schedules.
  name: Efí Pay (Gerencianet) Statement Schedules API
  phrasing_intents:
  - id: listStatementRecurrences
    intent: List statement delivery schedules
    question: Which recurring CNAB statement deliveries have I scheduled?
  - id: createStatementRecurrency
    intent: Schedule recurring CNAB statements
    question: How do I schedule CNAB statements to be generated regularly?
  - id: updateStatementRecurrency
    intent: Update a statement delivery schedule
    question: Can I change a statement schedule I set up?
  phrasing_ops: 3
  slug: gerencianet-statement-schedules-api
- baseURL: https://cobrancas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Subscriptions API from Efí Pay (Gerencianet) — 9 operation(s) for subscriptions.
  name: Efí Pay (Gerencianet) Subscriptions API
  phrasing_intents:
  - id: createSubscription
    intent: Subscribe a customer to a plan
    question: How do I subscribe a customer to one of my plans?
  - id: createOneStepSubscription
    intent: Subscribe and set payment in one step
    question: Can I create a subscription with its card or boleto payment in a single call?
  - id: createOneStepSubscriptionLink
    intent: Create a subscription payment link
    question: Can I generate a link so customers subscribe to a plan themselves?
  - id: detailSubscription
    intent: Get a subscription
    question: Can I look up a subscription and its charges?
  - id: updateSubscription
    intent: Update a subscription
    question: Can I change a subscription after it started?
  - id: defineSubscriptionPayMethod
    intent: Set the payment method on a subscription
    question: How do I add the card or boleto payment to a subscription I created?
  - id: cancelSubscription
    intent: Cancel a subscription
    question: Can I cancel a customer's subscription?
  - id: updateSubscriptionMetadata
    intent: Update a subscription's metadata
    question: Can I change the custom metadata on a subscription?
  phrasing_ops: 10
  slug: gerencianet-subscriptions-api
- baseURL: https://abrircontas.api.efipay.com.br/v1
  baseurl_source: spec
  description: The Webhooks API from Efí Pay (Gerencianet) — 8 operation(s) for webhooks.
  name: Efí Pay (Gerencianet) Webhooks API
  phrasing_intents:
  - id: accountConfigWebhook
    intent: Register an account webhook
    question: How do I register a webhook for account events?
  - id: accountDetailWebhook
    intent: Get an account webhook
    question: Can I look up one account webhook by its identifier?
  - id: accountDeleteWebhook
    intent: Delete an account webhook
    question: Can I remove an account webhook I no longer need?
  - id: accountListWebhook
    intent: List account webhooks
    question: Which account webhooks have I registered?
  - id: pixConfigWebhook
    intent: Set the webhook for a Pix key
    question: How do I get notified when a Pix arrives on one of my keys?
  - id: pixDetailWebhook
    intent: Get the webhook for a Pix key
    question: Which webhook URL is set on a given Pix key?
  - id: pixDeleteWebhook
    intent: Remove the webhook from a Pix key
    question: Can I stop Pix notifications for a specific key?
  - id: pixListWebhook
    intent: List Pix key webhooks
    question: Which of my Pix keys have webhooks configured?
  phrasing_ops: 15
  slug: gerencianet-webhooks-api
arazzos:
- description: Open a simplified Efí account, issue its certificate, and fetch its API credentials.
  name: Efí Account Onboarding
  slug: gerencianet-account-onboarding-workflow
- description: Register an account-level webhook and verify it was stored.
  name: Efí Account Webhook Setup
  slug: gerencianet-account-webhook-setup-workflow
- description: Decode a boleto bar code, pay it from the account, and reconcile the status.
  name: Efí Bill Payment by Bar Code
  slug: gerencianet-bill-payment-workflow
- description: Create a Cobranças charge, set the boleto payment method, and read its status.
  name: Efí Boleto Charge Issue
  slug: gerencianet-boleto-charge-issue-workflow
- description: Detail a Cobranças card charge, branch on its status, and refund it when paid.
  name: Efí Card Charge Refund
  slug: gerencianet-card-charge-refund-workflow
- description: Create an immediate Pix charge, confirm it, and render its payable QR Code.
  name: Efí Pix Immediate Charge to QR Code
  slug: gerencianet-pix-charge-qrcode-workflow
- description: Create a Pix charge under a fixed txid, check its status, and revise it while still active.
  name: Efí Pix Charge Revise
  slug: gerencianet-pix-charge-revise-workflow
- description: Detail a Pix charge, branch on its status, and refund the received Pix when paid.
  name: Efí Pix Charge Status and Refund
  slug: gerencianet-pix-charge-status-refund-workflow
- description: Create a Pix due charge with a due date, confirm it, and render its QR Code.
  name: Efí Pix Due Charge to QR Code
  slug: gerencianet-pix-due-charge-qrcode-workflow
- description: Send a Pix payout to a key and confirm the outbound transfer status.
  name: Efí Pix Cash-Out Send
  slug: gerencianet-pix-send-cashout-workflow
- description: Register a Pix webhook for a Pix key and verify it was stored.
  name: Efí Pix Webhook Setup
  slug: gerencianet-pix-webhook-setup-workflow
- description: Schedule a recurring CNAB statement job and confirm it is registered.
  name: Efí CNAB Statement Schedule
  slug: gerencianet-statement-schedule-workflow
artifact_total: 146
collections:
- collection_type: postman
  name: Efí Pay Cobranças API
  slug: postman-efi-cobrancas
- collection_type: postman
  name: Efí Pay Contas (Account Opening) API
  slug: postman-efi-contas
- collection_type: postman
  name: Efí Pay Extratos (Statements) API
  slug: postman-efi-extratos
- collection_type: postman
  name: Efí Pay Open Finance API
  slug: postman-efi-openfinance
- collection_type: postman
  name: Efí Pay Pagamentos (Bill Payment) API
  slug: postman-efi-pagamentos
- collection_type: postman
  name: Efí Pay Pix API
  slug: postman-efi-pix
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Efí Pay Cobranças API
  slug: open-efi-cobrancas
- collection_type: open
  name: Efí Pay Contas (Account Opening) API
  slug: open-efi-contas
- collection_type: open
  name: Efí Pay Extratos (Statements) API
  slug: open-efi-extratos
- collection_type: open
  name: Efí Pay Open Finance API
  slug: open-efi-openfinance
- collection_type: open
  name: Efí Pay Pagamentos (Bill Payment) API
  slug: open-efi-pagamentos
- collection_type: open
  name: Efí Pay Pix API
  slug: open-efi-pix
- collection_type: open
  name: Efí Pay Cobranças Account API
  slug: open-gerencianet-account-api
- collection_type: open
  name: Efí Pay Cobranças Account Accounts API
  slug: open-gerencianet-accounts-api
- collection_type: open
  name: Efí Pay Cobranças Account Authorization API
  slug: open-gerencianet-authorization-api
- collection_type: open
  name: Efí Pay Cobranças Account Automatic Charges API
  slug: open-gerencianet-automatic-charges-api
- collection_type: open
  name: Efí Pay Cobranças Account Automatic Pix API
  slug: open-gerencianet-automatic-pix-api
- collection_type: open
  name: Efí Pay Cobranças Account Bill Payments API
  slug: open-gerencianet-bill-payments-api
- collection_type: open
  name: Efí Pay Cobranças Account Biometric Pix API
  slug: open-gerencianet-biometric-pix-api
- collection_type: open
  name: Efí Pay Cobranças Account Card Payments API
  slug: open-gerencianet-card-payments-api
- collection_type: open
  name: Efí Pay Cobranças Account Carnets API
  slug: open-gerencianet-carnets-api
- collection_type: open
  name: Efí Pay Cobranças Account Charges API
  slug: open-gerencianet-charges-api
- collection_type: open
  name: Efí Pay Cobranças Account Configuration API
  slug: open-gerencianet-configuration-api
- collection_type: open
  name: Efí Pay Cobranças Account Devolutions API
  slug: open-gerencianet-devolutions-api
- collection_type: open
  name: Efí Pay Cobranças Account Due Charge Batches API
  slug: open-gerencianet-due-charge-batches-api
- collection_type: open
  name: Efí Pay Cobranças Account Due Charges API
  slug: open-gerencianet-due-charges-api
- collection_type: open
  name: Efí Pay Cobranças Account Immediate Charges API
  slug: open-gerencianet-immediate-charges-api
- collection_type: open
  name: Efí Pay Cobranças Account Immediate Pix API
  slug: open-gerencianet-immediate-pix-api
- collection_type: open
  name: Efí Pay Cobranças Account Locations API
  slug: open-gerencianet-locations-api
- collection_type: open
  name: Efí Pay Cobranças Account MED Infractions API
  slug: open-gerencianet-med-infractions-api
- collection_type: open
  name: Efí Pay Cobranças Account Notifications API
  slug: open-gerencianet-notifications-api
- collection_type: open
  name: Efí Pay Cobranças Account Participants API
  slug: open-gerencianet-participants-api
- collection_type: open
  name: Efí Pay Cobranças Account Payment Links API
  slug: open-gerencianet-payment-links-api
- collection_type: open
  name: Efí Pay Cobranças Account Pix Keys API
  slug: open-gerencianet-pix-keys-api
- collection_type: open
  name: Efí Pay Cobranças Account Pix Send API
  slug: open-gerencianet-pix-send-api
- collection_type: open
  name: Efí Pay Cobranças Account Plans API
  slug: open-gerencianet-plans-api
- collection_type: open
  name: Efí Pay Cobranças Account QR Codes API
  slug: open-gerencianet-qr-codes-api
- collection_type: open
  name: Efí Pay Cobranças Account Receipts API
  slug: open-gerencianet-receipts-api
- collection_type: open
  name: Efí Pay Cobranças Account Received Pix API
  slug: open-gerencianet-received-pix-api
- collection_type: open
  name: Efí Pay Cobranças Account Recurring Pix API
  slug: open-gerencianet-recurring-pix-api
- collection_type: open
  name: Efí Pay Cobranças Account Reports API
  slug: open-gerencianet-reports-api
- collection_type: open
  name: Efí Pay Cobranças Account Scheduled Pix API
  slug: open-gerencianet-scheduled-pix-api
- collection_type: open
  name: Efí Pay Cobranças Account SFTP API
  slug: open-gerencianet-sftp-api
- collection_type: open
  name: Efí Pay Cobranças Account Splits API
  slug: open-gerencianet-splits-api
- collection_type: open
  name: Efí Pay Cobranças Account Statement Files API
  slug: open-gerencianet-statement-files-api
- collection_type: open
  name: Efí Pay Cobranças Account Statement Schedules API
  slug: open-gerencianet-statement-schedules-api
- collection_type: open
  name: Efí Pay Cobranças Account Subscriptions API
  slug: open-gerencianet-subscriptions-api
- collection_type: open
  name: Efí Pay Cobranças Account Webhooks API
  slug: open-gerencianet-webhooks-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/capabilities/gerencianet-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gerencianet-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/agentic-access/gerencianet-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gerencianet-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/security/gerencianet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gerencianet-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/authentication/gerencianet-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gerencianet-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/scopes/gerencianet-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gerencianet-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ef-pay-gerencianet/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-account-onboarding-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-account-onboarding-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-account-webhook-setup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-account-webhook-setup-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-bill-payment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-bill-payment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-boleto-charge-issue-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-boleto-charge-issue-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-card-charge-refund-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-card-charge-refund-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-pix-charge-qrcode-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-pix-charge-qrcode-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-pix-charge-revise-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-pix-charge-revise-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-pix-charge-status-refund-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-pix-charge-status-refund-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-pix-due-charge-qrcode-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-pix-due-charge-qrcode-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-pix-send-cashout-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-pix-send-cashout-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-pix-webhook-setup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-pix-webhook-setup-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/arazzo/gerencianet-statement-schedule-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/gerencianet-statement-schedule-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://sejaefi.com.br
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.efipay.com.br
- group: start
  title: ''
  type: Console
  url: https://app.efipay.com.br
- group: start
  title: ''
  type: Signup
  url: https://sejaefi.com.br/cadastro
- group: commercial
  title: ''
  type: Pricing
  url: https://sejaefi.com.br/tarifas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sejaefi.com.br/termos-e-contratos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sejaefi.com.br/termos-e-contratos/politica-de-privacidade
- group: company
  title: ''
  type: Blog
  url: https://sejaefi.com.br/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sejaefi.com.br
- group: operate
  title: ''
  type: Support
  url: https://sejaefi.com.br/central-de-ajuda
- group: operate
  title: ''
  type: FAQ
  url: https://sejaefi.com.br/central-de-ajuda
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/efipay
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/efipay
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-php-apis-efi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-node-apis-efi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-python-apis-efi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-java-apis-efi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-go-apis-efi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-ruby-apis-efi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-dotnet-apis-efi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-typescript-apis-efi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-dart-apis-efi
- group: build
  title: ''
  type: SDKs
  url: https://github.com/efipay/sdk-delphi-apis-efi
- group: build
  title: ''
  type: Plugin
  url: https://github.com/efipay/Plugin-Wordpress-Efi
- group: build
  title: ''
  type: Plugin
  url: https://github.com/efipay/Plugin-Magento2-Efi
- group: build
  title: ''
  type: Plugin
  url: https://github.com/efipay/prestashop-efi-module
- group: build
  title: ''
  type: Plugin
  url: https://github.com/efipay/opencart-efi-module
- group: build
  title: ''
  type: Plugin
  url: https://github.com/efipay/whmcs-efi-module
- group: build
  title: ''
  type: Tools
  url: https://github.com/efipay/n8n-nodes-efibank
- group: build
  title: ''
  type: Tools
  url: https://github.com/efipay/mcp-server-efi-bank
- group: build
  title: ''
  type: Tools
  url: https://github.com/efipay/js-payment-token-efi
- group: build
  title: ''
  type: Tools
  url: https://github.com/efipay/conversor-p12-efi
- group: build
  title: ''
  type: Tools
  url: https://github.com/efipay/mtls-webhook
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/plans/gerencianet-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gerencianet-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/rate-limits/gerencianet-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gerencianet-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/finops/gerencianet-finops.yml
  title: ''
  type: FinOps
  url: finops/gerencianet-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/rules/efi-rules.yml
  title: ''
  type: SpectralRules
  url: rules/efi-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/vocabulary/gerencianet-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gerencianet-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/json-ld/gerencianet-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gerencianet-context.jsonld
created: '2026-05-24'
description: Efí Pay (formerly Gerencianet) is a Brazilian fintech and Banco Central-licensed payment institution headquartered in Belo Horizonte, Brazil. It provides a developer-first payments stack covering Pix (instant payments), Boleto / Bolix / Carnê (Brazilian bank slips), credit-card processing, recurring billing (assinaturas + carnês), marketplace splits, programmatic account opening (BaaS), Open Finance payment initiation, bill-payment automation, and CNAB statement extraction. The company rebranded from Gerencianet to Efí Pay / Efí Bank in 2022 and is rated at the top tier by Banco Central for its Pix API. The technical surface is exposed as five distinct REST APIs (Cobranças, Pix, Open Finance, Pagamentos, Contas) with twelve official SDKs plus e-commerce plugins.
examples:
- key_count: 2
  name: Efi Cobrancas Onestep Example
  slug: efi-cobrancas-onestep-example
- key_count: 2
  name: Efi Pix Create Cob Example
  slug: efi-pix-create-cob-example
- key_count: 2
  name: Efi Pix Send Example
  slug: efi-pix-send-example
features:
- description: Cash-in / cash-out / immediate (cob) / due (cobv) / automatic (cobr) / recurring (rec) Pix flows.
  name: Pix API (Banco Central rated tier-1)
- description: Brazilian bank slips with optional next-business-day settlement (Bolix).
  name: Boleto and Bolix
- description: Installment booklets — a single charge that emits a series of dated boletos.
  name: Carnê
- description: Card transactions with installments up to 12x and antecipação.
  name: Credit-Card Processing
- description: Recurring billing via the Cobranças API.
  name: Subscriptions and Plans
- description: Shareable payment URLs requiring no merchant site.
  name: Payment Links
- description: Automatic distribution of received funds across multiple Efí accounts.
  name: Marketplace Splits
- description: Initiate Pix payments from any participating Brazilian bank/fintech.
  name: Open Finance Payment Initiation
- description: Conta-simplificada accounts opened via API with auto-generated certificates and credentials.
  name: Programmatic Account Opening
- description: Decode boleto barcodes and pay them from the account balance.
  name: Bill Payment Automation
- description: Scheduled CNAB statement files retrievable via API or SFTP.
  name: CNAB Statement Extraction
- description: Submit defenses for Pix infraction notices via /v2/gn/infracoes.
  name: MED Infraction Defense
- description: Configurable Pix, recurring, and automatic-charge webhook delivery with replay endpoint.
  name: Webhooks With Optional mTLS Skip
finops:
- name: Gerencianet Finops
  service_category: Payments
  slug: gerencianet-finops
image: https://efipay.com.br/efi-logo.png
integrations:
- description: Official plugin for WooCommerce checkout.
  name: WordPress / WooCommerce
- description: Official Magento 2 plugin.
  name: Magento 2
- description: Official PrestaShop module.
  name: PrestaShop
- description: Official OpenCart module.
  name: OpenCart
- description: Official WHMCS billing plugin.
  name: WHMCS
- description: Community/official n8n custom node (efipay/n8n-nodes-efibank).
  name: n8n
- description: Official MCP server exposing Efí Pay APIs to LLM agents.
  name: Model Context Protocol
- description: Pix and Open Finance flows implement the BCB normative specifications.
  name: Banco Central do Brasil
json_schemas:
- name: Efí Pay Charge
  property_count: 6
  slug: efi-cobrancas-charge
- name: Pix Immediate Charge (Cob)
  property_count: 9
  slug: efi-pix-cob
- name: Received Pix
  property_count: 7
  slug: efi-pix-pix-received
json_structures:
- name: Efi Cobrancas Charge Structure
  property_count: 0
  slug: efi-cobrancas-charge-structure
- name: Efi Pix Cob Structure
  property_count: 0
  slug: efi-pix-cob-structure
jsonld:
- class_count: 12
  name: Gerencianet Context
  property_count: 15
  slug: gerencianet-context
layout: provider
modified: '2026-05-24'
name: Efí Pay (Gerencianet)
nav: Providers
network: true
overview: 'Efí Pay (Gerencianet) publishes 36 APIs on the [APIs.io](https://apis.io/) network, including Account API, Accounts API, Authorization API, and 33 more. Tagged areas include Payments, Pix, Boleto, Subscription, and Recurring Billing.


  The Efí Pay (Gerencianet) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Efí Pay (Gerencianet)''s developer surface includes authentication, developer portal, getting-started guide, developer console, signup flow, pricing, engineering blog, and 50 more developer resources.'
plans:
- name: Gerencianet Plans Pricing
  plan_count: 5
  slug: gerencianet-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Gerencianet Rate Limits
  slug: gerencianet-rate-limits
rules:
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Efí Pay (Gerencianet) API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: efi-rules
- effective_rule_count: 5
  extends: []
  name: Efí Pay (Gerencianet) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: gerencianet-jsonschema-spectral-rules
scopes:
- name: Gerencianet Scopes
  scope_count: 12
  slug: gerencianet-scopes
  summary_line: 12 scopes · clientCredentials
score:
  band: exemplar
  composite: 67.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 95.3
    catalog_earned_first_party: 0.0
    catalog_gap: 19.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.1
    contract_governance: 62.7
    contract_quality: 59.9
    developer_ergonomics: 75.0
    discoverability: 53.6
    operational_transparency: 49.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 67.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 36.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/gerencianet/refs/heads/main/screenshots/gerencianet-2026-06-20T181803.png
security:
- kind: authentication
  name: Gerencianet Authentication
  slug: gerencianet-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Gerencianet Domain Security
  slug: gerencianet-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: gerencianet
solutions:
- description: Account for self-employed individuals (no CNPJ required).
  name: Efí Pro
- description: Digital business account for registered companies.
  name: Efí Empresas
- description: Banco-rated institution providing Visa Platinum credit card and prepaid card issuance.
  name: Efí Bank
tags:
- Payments
- Pix
- Boleto
- Subscription
- Recurring Billing
- Marketplace
- Split Payments
- Open Finance
- Banking as a Service
- Account Opening
- Bill Payments
- CNAB
- Brazil
- Fintech
use_cases:
- description: Accept boleto, Pix QR Code, and credit card via a single transparent checkout.
  name: Brazilian E-Commerce Checkout
- description: Charge recurring fees via plan + subscription on boleto or card.
  name: SaaS Subscription Billing
- description: Split incoming Pix and boleto payments across multiple sellers.
  name: Marketplace Disbursement
- description: Open conta-simplificada accounts for partners and issue per-account credentials.
  name: White-Label BaaS / Sub-Account Onboarding
- description: Pay supplier boletos via /codBarras and Pix Cash-Out via /v3/gn/pix.
  name: AP Automation
- description: Pull daily CNAB statements + Pix reconciliation reports.
  name: Treasury Reconciliation
- description: Use the official MCP server (efipay/mcp-server-efi-bank) to expose Pix/billing as LLM tools.
  name: AI Agent Payments
website: https://sejaefi.com.br
---
