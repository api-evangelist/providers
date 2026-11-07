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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 78
  human_in_the_loop: 2
  name: Stax Agentic Access
  operation_count: 133
  slug: stax-agentic-access
  summary_line: 133 operations · 78 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Admin API from Stax — 1 operation(s) for admin.
  name: Stax Admin API
  phrasing_intents:
  - id: enroll-a-merchant
    intent: Enroll a merchant, registration and user at once
    question: Can I create a merchant, its registration and its first user login in a single Stax request?
  phrasing_ops: 1
  slug: stax-admin-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Charge API from Stax — 1 operation(s) for charge.
  name: Stax Charge API
  phrasing_intents:
  - id: charge-a-payment-method
    intent: Charge a saved payment method
    question: Can I charge a customer's stored card or bank account through Stax?
  phrasing_ops: 1
  slug: stax-charge-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Credit API from Stax — 1 operation(s) for credit.
  name: Stax Credit API
  phrasing_intents:
  - id: credit-a-payment-method
    intent: Send a credit to a saved payment method
    question: Can I push money back to a customer's stored card or bank account without an original sale?
  phrasing_ops: 1
  slug: stax-credit-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Customer API from Stax — 3 operation(s) for customer.
  name: Stax Customer API
  phrasing_intents:
  - id: create-customer
    intent: Create a customer record
    question: How do I add a new customer to my Stax merchant account?
  - id: find-all-customers
    intent: List and filter customers
    question: Can I look up customers on my merchant account by name, email or company?
  - id: delete-a-customer
    intent: Delete a customer
    question: Can I remove a customer from my merchant account?
  - id: get-a-customers-information
    intent: Get one customer's details
    question: What contact and address details do I have on file for a specific customer?
  - id: update-customer-info
    intent: Update an existing customer
    question: Can I change the email or phone number on a customer I already created?
  - id: get-all-payment-methods-for-a-customer
    intent: List a customer's payment methods
    question: Which cards and bank accounts does a particular customer have saved?
  phrasing_ops: 6
  slug: stax-customer-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Ephemeral API from Stax — 1 operation(s) for ephemeral.
  name: Stax Ephemeral API
  phrasing_intents:
  - id: ephemeral-authentication-tokens-1
    intent: Issue a short-lived authentication token
    question: Can I exchange my Stax API key for a temporary token that expires in 24 hours?
  phrasing_ops: 1
  slug: stax-ephemeral-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The File API from Stax — 5 operation(s) for file.
  name: Stax File API
  phrasing_intents:
  - id: post_file
    intent: Upload a file
    question: Can I upload a file like a product image and classify it with a tag?
  - id: get_file
    intent: List uploaded files
    question: Which files have I uploaded to my Stax account?
  - id: delete-evidence-for-dispute
    intent: Delete a dispute evidence file
    question: Can I remove an evidence file I attached to a chargeback dispute by mistake?
  - id: put_file{id}
    intent: Update an uploaded file
    question: Can I rename or retag a file I already uploaded?
  - id: get_file{id}
    intent: Get a file by ID
    question: Can I fetch the details of one uploaded file using its ID?
  - id: get_file{tag}
    intent: Get files by tag
    question: Can I pull up only the files classified with a certain tag, like thumbnail?
  - id: upload-evidence-for-dispute
    intent: Upload evidence for a dispute
    question: How do I attach evidence to a chargeback dispute?
  phrasing_ops: 7
  slug: stax-file-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The File{id} API from Stax — 1 operation(s) for file{id}.
  name: Stax File{id} API
  phrasing_intents:
  - id: delete_file{id}
    intent: Delete an uploaded file
    question: Can I permanently remove a file I uploaded to my Stax account?
  phrasing_ops: 1
  slug: stax-file-id-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Forgot API from Stax — 1 operation(s) for forgot.
  name: Stax Forgot API
  phrasing_intents:
  - id: initiate-password-reset
    intent: Start a password reset for a user
    question: What happens when a user forgets their Stax password?
  phrasing_ops: 1
  slug: stax-forgot-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Invoice API from Stax — 9 operation(s) for invoice.
  name: Stax Invoice API
  phrasing_intents:
  - id: createScheduledInvoice
    intent: Schedule a recurring or one-time invoice
    question: Can I set up an invoice that bills a customer automatically every month?
  - id: create-an-invoice
    intent: Create an invoice for a customer
    question: How do I bill a customer with a one-off invoice?
  - id: get-all-invoices
    intent: List and search invoices
    question: Which invoices have I sent to a particular customer email?
  - id: delete-an-invoice
    intent: Delete an invoice
    question: Can I delete an invoice that was created by mistake?
  - id: get-an-invoice
    intent: Get one invoice
    question: What is the status and balance of a specific invoice?
  - id: update-an-invoice
    intent: Update an existing invoice
    question: Can I change the invoice date on an invoice I already created?
  - id: delete-invoice-schedule
    intent: Delete a recurring invoice schedule
    question: Can I stop a recurring billing schedule for good?
  - id: editInvoiceSchedule
    intent: Edit an invoice schedule
    question: Can I pause a recurring invoice schedule without deleting it?
  phrasing_ops: 13
  slug: stax-invoice-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Item API from Stax — 5 operation(s) for item.
  name: Stax Item API
  phrasing_intents:
  - id: create-catalog-item
    intent: Add an item to the catalog
    question: How do I add a new product to my Stax catalog?
  - id: retrieve-all-catalog-items
    intent: List catalog items
    question: What products and services are in my merchant catalog?
  - id: decrement-items-stock
    intent: Decrease an item's stock
    question: Can I reduce the stock count of an item after selling some offline?
  - id: delete-a-catalog-item
    intent: Delete a catalog item
    question: Can I remove a product I no longer sell from my catalog?
  - id: retrieve-an-item-by-id
    intent: Get a catalog item
    question: What price and stock level does a specific catalog item have?
  - id: update-an-item
    intent: Update a catalog item
    question: Can I change the price of an existing product in my catalog?
  - id: increment-items-stock
    intent: Increase an item's stock
    question: Can I add units to an item's inventory when a new shipment arrives?
  - id: retrieve-all-item-codes
    intent: List item codes
    question: Which merchant-side item codes am I using across my catalog?
  phrasing_ops: 8
  slug: stax-item-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Merchant API from Stax — 7 operation(s) for merchant.
  name: Stax Merchant API
  phrasing_intents:
  - id: add-file-to-merchant-registration
    intent: Upload a file to a merchant's registration
    question: Can I attach a voided check or ID document to a merchant's onboarding registration?
  - id: create-a-merchant
    intent: Create a merchant
    question: How do I create a new merchant account on its own, without a user or registration?
  - id: get-all-merchants
    intent: List and filter merchants
    question: Which merchants do I manage, and what status is each in?
  - id: create-a-new-api-key-for-merchant
    intent: Create an API key for a merchant
    question: Can I generate a new API key on behalf of a merchant I manage?
  - id: list-api-keys-for-merchant
    intent: List a merchant's API keys
    question: Which API keys exist for one of my merchants?
  - id: delete-file-from-merchant-registration
    intent: Remove a file from a merchant's registration
    question: Can I delete a wrong document uploaded to a merchant's onboarding registration?
  - id: get-merchant-by-id
    intent: Get a merchant
    question: What details does Stax hold for one specific merchant account?
  - id: get-merchant-registration-data
    intent: Get a merchant's registration data
    question: What onboarding information has a merchant submitted for underwriting?
  phrasing_ops: 11
  slug: stax-merchant-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Payment Method API from Stax — 4 operation(s) for payment method.
  name: Stax Payment Method API
  phrasing_intents:
  - id: create-a-payment-method-copy
    intent: Save a bank account (ACH) payment method
    question: How do I tokenize a customer's bank account for ACH payments?
  - id: get-all-payment-methods-for-a-merchant
    intent: List all payment methods on the merchant
    question: Which saved cards and bank accounts exist across all of my customers?
  - id: create-a-payment-method
    intent: Save a credit or debit card payment method
    question: Can I tokenize a customer's credit card directly through the API?
  - id: delete-a-payment-method
    intent: Delete a customer's payment method
    question: Can I remove a card a customer no longer wants on file?
  - id: get-a-payment-method-by-id
    intent: Get a payment method
    question: What card brand and last four digits are on a specific saved payment method?
  - id: update-a-payment-method
    intent: Update a saved payment method
    question: Can I change the expiration date on a card that is already saved?
  - id: share-a-payment-method-with-a-third-party
    intent: Copy a payment method to an external gateway
    question: Can I copy a stored Stax card into another payment gateway's vault?
  phrasing_ops: 7
  slug: stax-payment-method-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Query API from Stax — 14 operation(s) for query.
  name: Stax Query API
  phrasing_intents:
  - id: ach-rejections
    intent: Report ACH rejections for a date range
    question: Which ACH payments were rejected or returned on my statement last month?
  - id: card-processing
    intent: Report card processing volume
    question: How much card processing volume did I run over a period?
  - id: create-a-payment-link
    intent: Create a payment link
    question: Can I generate a shareable link that customers use to pay me?
  - id: list-and-filter-all-payment-links
    intent: List payment links
    question: Which payment links have I created for my merchant account?
  - id: daily-sales
    intent: Report daily sales, fees and surcharges
    question: What were my total sales for each day of last week?
  - id: delete-a-payment-link
    intent: Delete a payment link
    question: Can I permanently remove a payment link from my account?
  - id: get-a-payment-links-information
    intent: Get a payment link's details
    question: What amount, name and metadata does a specific payment link have?
  - id: update-a-payment-link
    intent: Update or deactivate a payment link
    question: Can I turn off a payment link without deleting it?
  phrasing_ops: 17
  slug: stax-query-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Reset API from Stax — 1 operation(s) for reset.
  name: Stax Reset API
  phrasing_intents:
  - id: reset-password
    intent: Set a new password with a reset token
    question: Can a user choose a new password once they have a reset token?
  - id: verify-password-reset-token
    intent: Check a password reset token
    question: Is a password reset link's token still valid before I show the reset form?
  phrasing_ops: 2
  slug: stax-reset-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Self API from Stax — 4 operation(s) for self.
  name: Stax Self API
  phrasing_intents:
  - id: check-if-e-mail-exists
    intent: Check whether an email is already registered
    question: Is an email address already taken by an existing Stax user?
  - id: create-a-user-account-self-registration
    intent: Self-register a new user account
    question: How does someone sign up for their own user account?
  - id: get-self-and-teams-info
    intent: Get my user and team info
    question: Who am I logged in as, and which team am I on?
  - id: update-your-user-info
    intent: Update my own user profile
    question: Can I change my own name or details on my Stax login?
  - id: resend-verification-e-mail
    intent: Resend the verification email
    question: What if a new user never received their email verification message?
  - id: verify-e-mail-token
    intent: Verify an email confirmation token
    question: Is the token from a user's email verification link valid?
  phrasing_ops: 6
  slug: stax-self-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Surcharge API from Stax — 1 operation(s) for surcharge.
  name: Stax Surcharge API
  phrasing_intents:
  - id: review-a-transactions-surcharge-information
    intent: Preview the surcharge for a payment method
    question: What surcharge would a customer pay if I charged their saved card?
  phrasing_ops: 1
  slug: stax-surcharge-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Team API from Stax — 8 operation(s) for team.
  name: Stax Team API
  phrasing_intents:
  - id: addupdate-team-settings
    intent: Add or update team settings
    question: Can I change my merchant team's option settings?
  - id: post_teamoptionadvanced_customizations
    intent: Set an advanced customization field
    question: Can I add a custom field to my team's checkout or invoice forms?
  - id: create-a-new-team-member
    intent: Add a new user to my team
    question: How do I create a login for a new employee on my merchant team?
  - id: find-the-merchant-teams-users
    intent: List my team's users
    question: Who are the users on my merchant team?
  - id: create-a-team
    intent: Create a new merchant team
    question: Can I set up a brand-new merchant team?
  - id: edit-your-merchant-teams-info
    intent: Edit my team's company details
    question: Can I change the company name or contact email on my existing team?
  - id: get-team-members-information-copy
    intent: Update a team member
    question: As a team admin, can I change another team member's information?
  - id: get-team-members-information
    intent: Get a team member
    question: What role and details does a specific person on my team have?
  phrasing_ops: 12
  slug: stax-team-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Terminal API from Stax — 13 operation(s) for terminal.
  name: Stax Terminal API
  phrasing_intents:
  - id: charge-queue
    intent: Queue a card-present sale on a terminal
    question: Can I stage a terminal sale while the device is busy with another customer?
  - id: charge
    intent: Run a card-present sale on a terminal now
    question: How do I take an in-person card payment on a paired terminal?
  - id: credit
    intent: Give a standalone credit on a terminal
    question: Can I return money to a customer at the terminal without an original sale?
  - id: get-all-devices
    intent: List terminal devices
    question: Which Wi-Fi card terminals are connected to my merchant account?
  - id: get-transaction-status
    intent: Check a terminal transaction's status
    question: Did the customer finish paying on the terminal yet?
  - id: print
    intent: Print a custom message on a terminal
    question: Can I print a custom note or receipt add-on from the card terminal's printer?
  - id: get_terminalpromptChoice
    intent: Prompt a multiple-choice question on a terminal
    question: Can I show the customer a list of options to pick from on the terminal screen?
  - id: prompt-input
    intent: Prompt for free-text input on a terminal
    question: Can the terminal ask for a table number or PO reference typed in by the customer?
  phrasing_ops: 13
  slug: stax-terminal-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Transaction API from Stax — 11 operation(s) for transaction.
  name: Stax Transaction API
  phrasing_intents:
  - id: capture-a-pre-auth-transaction
    intent: Capture a pre-authorized transaction
    question: How do I finalize a card pre-authorization into a completed charge?
  - id: e-mail-transaction-receipt
    intent: Email a transaction receipt
    question: Can I email a customer the receipt for a payment they made?
  - id: get-a-related-transaction
    intent: Get a transaction's child transactions
    question: Which refunds or voids were made against an original payment?
  - id: get-a-transactions-funding-instructions
    intent: Get a transaction's split-funding instructions
    question: How was a split-funded payment divided between accounts?
  - id: get-a-transactions-information
    intent: Get a transaction's details
    question: What payment method and customer were used on a specific transaction?
  - id: list-and-filter-all-transactions
    intent: List and filter transactions
    question: Which payments did I take last week?
  - id: refund-transaction
    intent: Refund a batched transaction
    question: How do I refund a card-not-present payment that has already settled?
  - id: sms-transaction-receipt
    intent: Text a transaction receipt
    question: Can I text a receipt for a payment to the customer's phone?
  phrasing_ops: 11
  slug: stax-transaction-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Underwriting API from Stax — 5 operation(s) for underwriting.
  name: Stax Underwriting API
  phrasing_intents:
  - id: get-registration-documents
    intent: List a merchant's required registration documents
    question: Which documents does a merchant still need to supply for underwriting?
  - id: list-disputes-copy
    intent: List disputes for a specific merchant
    question: Which chargebacks has one of my sub-merchants received?
  - id: list-disputes
    intent: List my own disputes
    question: What chargebacks has my account received?
  - id: retrieve-terms-and-conditions
    intent: Get a merchant's terms and conditions
    question: What terms and conditions apply to a given merchant?
  - id: submit-dispute-evidence-files-for-review
    intent: Submit dispute evidence for review
    question: Once my evidence is uploaded, how do I send the dispute for review?
  phrasing_ops: 5
  slug: stax-underwriting-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Verify API from Stax — 1 operation(s) for verify.
  name: Stax Verify API
  phrasing_intents:
  - id: verify-a-payment-method
    intent: Verify a saved payment method
    question: Can I check that a customer's saved card is good before charging it for real?
  phrasing_ops: 1
  slug: stax-verify-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Webhook API from Stax — 2 operation(s) for webhook.
  name: Stax Webhook API
  phrasing_intents:
  - id: create-new-webhook-for-all-of-my-users-merchants
    intent: Create a webhook for all my merchants
    question: Can I get notified at my own URL when a transaction event happens on any of my merchants?
  - id: get-all-webhooks
    intent: List my webhooks
    question: Which webhooks have I set up for my merchants?
  - id: delete-a-webhook
    intent: Delete a webhook
    question: Can I stop a webhook from firing?
  phrasing_ops: 3
  slug: stax-webhook-api
- baseURL: https://apiprod.fattlabs.com
  baseurl_source: declared
  description: The Webhookadmin API from Stax — 2 operation(s) for webhookadmin.
  name: Stax Webhookadmin API
  phrasing_intents:
  - id: create-partner-level-webhook-for-your-brand
    intent: Create a partner-level brand webhook
    question: Can I create one webhook that triggers for every merchant under my partner brand?
  - id: get-all-partner-level-webhooks-for-your-brand
    intent: List partner-level brand webhooks
    question: Which partner-level webhooks are registered for my brand?
  - id: delete-a-partner-level-webhook-for-your-brand
    intent: Delete a partner-level brand webhook
    question: Can I remove a webhook that fires for my whole partner brand?
  - id: get-a-specific-partner-level-webhook-for-your-brand
    intent: Get a partner-level brand webhook
    question: What URL and event is a particular brand webhook set to?
  phrasing_ops: 4
  slug: stax-webhookadmin-api
artifact_total: 39
asyncapis:
- description: ''
  name: Stax Webhooks
  slug: stax-webhooks
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://staxpayments.com/feed/
- group: other
  href: https://artifacts.apis.io/stax/capabilities/stax-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/stax-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/stax/agentic-access/stax-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/stax-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://staxpayments.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.staxpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.staxpayments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.staxpayments.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.staxpayments.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.fattmerchant.com/
- group: company
  title: ''
  type: Blog
  url: https://staxpayments.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fattmerchantorg
- group: commercial
  title: ''
  type: Pricing
  url: https://staxpayments.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://staxpayments.com/request-sandbox/
- group: start
  title: ''
  type: Login
  url: https://app.staxpayments.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://staxpayments.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://staxpayments.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.staxpayments.com/
- group: operate
  href: https://artifacts.apis.io/stax/changelog/stax-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/stax-changelog.yml
- group: design
  href: https://artifacts.apis.io/stax/lifecycle/stax-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/stax-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/stax/authentication/stax-authentication.yml
  title: ''
  type: Authentication
  url: authentication/stax-authentication.yml
- group: design
  href: https://artifacts.apis.io/stax/conventions/stax-conventions.yml
  title: ''
  type: Conventions
  url: conventions/stax-conventions.yml
- group: design
  href: https://artifacts.apis.io/stax/conventions/stax-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/stax-conventions.yml
- group: operate
  href: https://artifacts.apis.io/stax/rate-limits/stax-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/stax-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/stax/plans/stax-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/stax-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/stax/errors/stax-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/stax-problem-types.yml
- group: build
  href: https://artifacts.apis.io/stax/errors/stax-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/stax-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/stax/asyncapi/stax-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/stax-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/stax/mcp/stax-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/stax-mcp.yml
- group: build
  href: https://artifacts.apis.io/stax/mcp/stax-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/stax-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/stax/llms/stax-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/stax-llms.txt
- group: build
  href: https://artifacts.apis.io/stax/packages/stax-packages.yml
  title: ''
  type: Packages
  url: packages/stax-packages.yml
- group: build
  href: https://artifacts.apis.io/stax/packages/stax-packages.yml
  title: ''
  type: SDKs
  url: packages/stax-packages.yml
- group: design
  href: https://artifacts.apis.io/stax/components/stax-components.yml
  title: ''
  type: Components
  url: components/stax-components.yml
- group: start
  href: https://artifacts.apis.io/stax/sandbox/stax-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/stax-sandbox.yml
- group: design
  href: https://artifacts.apis.io/stax/data-model/stax-data-model.yml
  title: ''
  type: DataModel
  url: data-model/stax-data-model.yml
- group: design
  href: https://artifacts.apis.io/stax/conformance/stax-conformance.yml
  title: ''
  type: Conformance
  url: conformance/stax-conformance.yml
- group: auth
  href: https://artifacts.apis.io/stax/conformance/stax-conformance.yml
  title: ''
  type: Compliance
  url: conformance/stax-conformance.yml
- group: auth
  href: https://artifacts.apis.io/stax/security/stax-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/stax-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/stax/well-known/stax-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/stax-security.txt
- group: auth
  href: https://artifacts.apis.io/stax/security/stax-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/stax-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stax/security/stax-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/stax-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/stax/security/stax-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stax-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/stax/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/stax/examples/stax-api-examples.yml
  title: ''
  type: Examples
  url: examples/stax-api-examples.yml
- group: other
  href: https://artifacts.apis.io/stax/overlays/stax-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/stax-api-overlay.yaml
- group: docs
  href: https://artifacts.apis.io/stax/openapi/_original/stax-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/stax-api-openapi.json
created: '2026-08-29'
description: Stax (formerly Fattmerchant) is an Orlando, Florida payments technology company that sells subscription-priced payment processing to small and large merchants (Stax Pay), embedded payments and merchant onboarding to SaaS platforms and ISVs (Stax Connect), compliant credit-card surcharging (CardX by Stax), automated subscription billing (Stax Bill), and full-stack processing for partners and ISOs (Stax Processing). Its public REST API at apiprod.fattlabs.com covers charges, credits, refunds and voids, stored payment methods and tokenization, customers, invoices and invoice schedules, payment links, catalog items, terminals and card-present devices, merchant enrollment and underwriting, disputes, statements and deposit reporting, teams, users and API keys, and merchant- and partner-level webhooks. Stax.js handles browser tokenization; iOS and Android SDKs cover card-present and Tap to Pay. Stax Payments, Inc. is a registered ISO/MSP of Fifth Third Bank and Synovus Bank and a registered
  partner/ISO of Elavon, Inc.
finops:
- has_sources: true
  method: derived
  name: Stax Finops
  primary_unit: transaction
  service_category: ''
  slug: stax-finops
  template: false
image: https://staxpayments.com/wp-content/uploads/2024/04/stax-logo-full.png
layout: provider
mcp_servers:
- description: 'Stax hosts a remote MCP server at https://docs.staxpayments.com/mcp. It answered an anonymous initialize + tools/list on 2026-08-29 (protocolVersion 2025-06-18, serverInfo {name: ''Stax Docs'', version:'
  name: Stax Docs MCP Server
  slug: stax-docs-mcp-server
modified: '2026-10-06'
name: Stax
nav: Providers
network: true
overview: 'Stax publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Charge API, Credit API, and 20 more. Tagged areas include Payments, Payment Processing, Merchant Services, Embedded Payments, and ACH.


  The Stax catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Stax''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
plans:
- name: Stax Plans Pricing
  plan_count: 8
  slug: stax-plans-pricing
- name: Stax Price Estimates
  plan_count: 0
  slug: stax-price-estimates
random_paper: 16
rate_limits:
- limit_count: 4
  name: Stax Rate Limits
  slug: stax-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Stax API Rules
  rule_count: 48
  severity_counts:
    error: 32
    hint: 0
    info: 4
    warn: 12
  slug: stax-rules
score:
  band: exemplar
  composite: 75.7
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 61.6
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 84.2
  previous_composite: 75.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/stax/stax-2026-09-02T160822.png
security:
- kind: authentication
  name: Stax Authentication
  slug: stax-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Stax Domain Security
  slug: stax-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Stax Vulnerability Disclosure
  slug: stax-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Stax Trust Center
  slug: stax-trust-center
  summary_line: trust center published
skill_count: 4
skills:
- name: stax-charge-and-reverse
  slug: stax-charge-and-reverse
- name: stax-invoice-and-collect
  slug: stax-invoice-and-collect
- name: stax-onboard-a-merchant
  slug: stax-onboard-a-merchant
- name: stax-reconcile-deposits
  slug: stax-reconcile-deposits
slug: stax
tags:
- Payments
- Payment Processing
- Merchant Services
- Embedded Payments
- ACH
- Invoicing
- Subscription Billing
- Surcharging
- Point-of-Sale
- Tokenization
- Financial Services
- Fintech
- Card Present
- Merchant Onboarding
website: https://staxpayments.com/
---
