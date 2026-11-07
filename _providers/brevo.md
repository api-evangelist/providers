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
  - scopes
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
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 57.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 218
  human_in_the_loop: 4
  name: Brevo Agentic Access
  operation_count: 360
  slug: brevo-agentic-access
  summary_line: 360 operations · 218 acting · 4 human-in-the-loop
api_count: 21
apis:
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Manage agent online status for conversation availability.
  name: brevo Agent Status API
  phrasing_intents:
  - id: setAgentOnline
    intent: Mark a chat agent as online
    question: What keeps a chat agent showing as available for conversations?
  phrasing_ops: 1
  slug: brevo-agent-status-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create, manage, and retrieve automated messages pushed to visitors.
  name: brevo Automated Messages API
  phrasing_intents:
  - id: createAutomatedMessage
    intent: Send an automated message to a visitor
    question: How do I send a proactive welcome message to a website visitor?
  - id: getAutomatedMessage
    intent: Get an automated message
    question: What was in a particular automated message?
  - id: updateAutomatedMessage
    intent: Update an automated message
    question: Can I change the wording of an automated message already sent?
  - id: deleteAutomatedMessage
    intent: Delete an automated message
    question: How do I permanently delete an automated message?
  phrasing_ops: 4
  slug: brevo-automated-messages-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Manage product categories for organizing the catalog.
  name: brevo Categories API
  phrasing_intents:
  - id: listCategories
    intent: List product categories
    question: Which product categories exist in my Brevo eCommerce catalog?
  - id: createUpdateCategory
    intent: Create or update a product category
    question: How do I add a single product category to the catalog?
  - id: batchCreateUpdateCategories
    intent: Create or update categories in bulk
    question: Can I sync many product categories in one call?
  phrasing_ops: 3
  slug: brevo-categories-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create, retrieve, update, and delete individual contacts.
  name: brevo Contacts API
  phrasing_intents:
  - id: createAttribute
    intent: Create a new contact attribute
    question: How do I add a custom field like a birthday or loyalty tier to my Brevo contacts?
  - id: updateAttribute
    intent: Update a contact attribute
    question: Can I change the dropdown values of a category attribute that already exists on my contacts?
  - id: deleteAttribute
    intent: Delete a contact attribute
    question: Can I permanently remove a contact field I no longer use?
  - id: getAttributes
    intent: List all contact attributes
    question: What custom fields are defined on the contacts in my account?
  - id: deleteMultiAttributeOptions
    intent: Remove an option from a multiple-choice attribute
    question: Can I delete one choice from a multiple-choice contact field without deleting the whole field?
  - id: createList
    intent: Create a contact list
    question: How do I create a new mailing list inside one of my folders?
  - id: getLists
    intent: List all contact lists
    question: What contact lists do I have in my Brevo account?
  - id: getList
    intent: Get a contact list's details
    question: How many subscribers does a specific list have and when was it created?
  phrasing_ops: 29
  slug: brevo-contacts-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Track and retrieve transactional email activity including delivery status, opens, clicks, and bounces.
  name: brevo Email Activity API
  phrasing_intents:
  - id: getTransactionalEmailEvents
    intent: List individual transactional email events
    question: Did a specific customer open the transactional email we sent them?
  - id: getAggregatedEmailReport
    intent: Get transactional email totals for a period
    question: What are my total transactional deliveries, opens and clicks for last month?
  phrasing_ops: 2
  slug: brevo-email-activity-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create and manage reusable email templates for transactional messaging.
  name: brevo Email Templates API
  phrasing_intents:
  - id: listSmtpTemplates
    intent: List transactional email templates
    question: What transactional email templates do I have?
  - id: createSmtpTemplate
    intent: Create a transactional email template
    question: How do I create a reusable transactional email template?
  - id: getSmtpTemplate
    intent: Get an email template
    question: What is the subject and content of a specific email template?
  - id: updateSmtpTemplate
    intent: Update an email template
    question: Can I change the subject line of an existing template?
  - id: deleteSmtpTemplate
    intent: Delete an email template
    question: Can I permanently delete a transactional email template?
  phrasing_ops: 5
  slug: brevo-email-templates-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Send and manage chat messages as an agent or automated bot within conversations.
  name: brevo Messages API
  phrasing_intents:
  - id: sendMessageAsAgent
    intent: Send a chat message as an agent
    question: How do I reply to a website visitor in live chat from code?
  - id: getMessage
    intent: Get a chat message
    question: Who sent a particular chat message and when?
  - id: updateMessage
    intent: Edit an agent's chat message
    question: Can I fix a typo in a chat message I already sent?
  - id: deleteMessage
    intent: Delete a chat message
    question: Can I remove a message from a chat conversation?
  phrasing_ops: 4
  slug: brevo-messages-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create and manage eCommerce order data for revenue attribution and purchase tracking.
  name: brevo Orders API
  phrasing_intents:
  - id: createUpdateOrder
    intent: Create or update an order
    question: How do I send a store order to Brevo for revenue attribution?
  - id: batchCreateUpdateOrders
    intent: Create or update orders in bulk
    question: Can I import a large batch of historical orders in one call?
  - id: listOrders
    intent: List eCommerce orders
    question: Which orders has Brevo recorded from my store?
  phrasing_ops: 3
  slug: brevo-orders-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Import, manage, and retrieve eCommerce product data.
  name: brevo Products API
  phrasing_intents:
  - id: listProducts
    intent: List eCommerce products
    question: Which products from my store are synced to Brevo?
  - id: createUpdateProduct
    intent: Create or update a product
    question: How do I sync a single product from my store into Brevo?
  - id: batchCreateUpdateProducts
    intent: Create or update products in bulk
    question: Can I sync my whole product catalog in one request?
  - id: getProduct
    intent: Get a product
    question: What price and URL does Brevo have for one of my products?
  phrasing_ops: 4
  slug: brevo-products-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Manage sender identities used for transactional email sending.
  name: brevo Senders API
  phrasing_intents:
  - id: getSenders
    intent: List email senders
    question: Which sender addresses can I use for my Brevo campaigns?
  - id: createSender
    intent: Create an email sender
    question: How do I add a new From name and address for campaigns?
  - id: updateSender
    intent: Update an email sender
    question: Can I change the display name on an existing sender?
  - id: deleteSender
    intent: Delete an email sender
    question: How do I remove a duplicate sender address?
  - id: validateSenderByOTP
    intent: Verify a sender with a one-time code
    question: How do I verify a new sender with the code I got by email?
  - id: getIps
    intent: List the account's dedicated IPs
    question: Which dedicated sending IPs does my account have?
  - id: getIpsFromSender
    intent: List dedicated IPs for one sender
    question: Which dedicated IPs does a particular sender send from?
  phrasing_ops: 7
  slug: brevo-senders-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Retrieve delivery reports and activity statistics for transactional SMS messages.
  name: brevo SMS Statistics API
  phrasing_intents:
  - id: getSmsEvents
    intent: List transactional SMS events
    question: Was a transactional text to a specific phone number delivered?
  - id: getSmsReports
    intent: Get daily transactional SMS stats
    question: How many transactional texts were delivered each day this week?
  - id: getAggregatedSmsReport
    intent: Get total transactional SMS stats for a period
    question: What's my total number of transactional texts sent and bounced this month?
  phrasing_ops: 3
  slug: brevo-sms-statistics-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Send and manage transactional emails including order confirmations, password resets, and account notifications.
  name: brevo Transactional Emails API
  phrasing_intents:
  - id: sendTransactionalEmail
    intent: Send a transactional email
    question: How do I send a password reset email from my app?
  - id: batchSendTransactionalEmails
    intent: Send many transactional emails in one call
    question: Can I send different personalized emails to many recipients in one request?
  - id: getTransactionalEmailContent
    intent: Get the content of a sent email
    question: What exactly did a customer receive in a transactional email I sent?
  - id: getTransacEmailsList
    intent: List sent transactional emails
    question: Which transactional emails did we send to a particular address in the last 30 days?
  - id: getTransacEmailContent
    intent: Get the personalized content of a sent email
    question: Which version of an email, with their own merge values, did one recipient get, looked up by the uuid from the logs?
  - id: deleteScheduledEmailById
    intent: Cancel scheduled transactional emails
    question: How do I cancel a transactional email I scheduled but haven't sent yet?
  - id: getScheduledEmailById
    intent: Check the status of scheduled emails
    question: Has my scheduled batch of transactional emails been sent yet?
  - id: deleteHardbounces
    intent: Clear hard bounces
    question: Can I remove hard bounces caused by a temporary ISP outage?
  phrasing_ops: 24
  slug: brevo-transactional-emails-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Send transactional SMS messages for notifications, verifications, and alerts.
  name: brevo Transactional SMS API
  phrasing_intents:
  - id: sendTransactionalSms
    intent: Send a transactional SMS
    question: Can I send a one-time verification text to a phone number right away?
  - id: sendAsyncTransactionalSms
    intent: Send a transactional SMS asynchronously
    question: How do I send an order confirmation text to a customer's phone?
  - id: getTransacAggregatedSmsReport
    intent: Get total transactional SMS stats for a period
    question: How many transactional texts were delivered, bounced or replied to in total last month?
  - id: getTransacSmsReport
    intent: Get daily transactional SMS stats
    question: What did my SMS delivery numbers look like day by day this week?
  - id: getSmsEvents
    intent: List individual transactional SMS events
    question: Which texts to a specific phone number bounced, and why?
  phrasing_ops: 5
  slug: brevo-transactional-sms-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create, manage, and configure webhook subscriptions for receiving real-time event notifications.
  name: brevo Webhooks API
  phrasing_intents:
  - id: getWebhooks
    intent: List webhooks
    question: Which webhooks are configured on my Brevo account?
  - id: createWebhook
    intent: Create a webhook
    question: How do I get notified at my URL when an email is delivered or opened?
  - id: getWebhook
    intent: Get a webhook
    question: Which events is a particular webhook subscribed to?
  - id: updateWebhook
    intent: Update a webhook
    question: Can I change the URL or events of an existing webhook?
  - id: deleteWebhook
    intent: Delete a webhook
    question: Can I stop all notifications from a webhook for good?
  - id: exportWebhooksHistory
    intent: Export webhook event history
    question: Can I download the history of webhook events as a CSV?
  phrasing_ops: 6
  slug: brevo-webhooks-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create, manage, and send WhatsApp marketing campaigns.
  name: brevo WhatsApp Campaigns API
  phrasing_intents:
  - id: listWhatsAppCampaigns
    intent: List WhatsApp campaigns
    question: What WhatsApp campaigns exist in my account?
  - id: createWhatsAppCampaign
    intent: Create and send a WhatsApp campaign
    question: How do I send a WhatsApp marketing campaign with a template?
  - id: getWhatsAppCampaign
    intent: Get a WhatsApp campaign
    question: What are the delivery stats of one WhatsApp campaign?
  - id: updateWhatsAppCampaign
    intent: Update a draft WhatsApp campaign
    question: Can I change the template or schedule of a WhatsApp campaign?
  - id: deleteWhatsAppCampaign
    intent: Delete a WhatsApp campaign
    question: Can I permanently delete a WhatsApp campaign?
  - id: getWhatsAppTemplates
    intent: List WhatsApp templates
    question: Which WhatsApp templates have I created and are they approved yet?
  - id: getWhatsAppConfig
    intent: Get WhatsApp account configuration
    question: Is my WhatsApp Business account connected and what is its status?
  - id: createWhatsAppTemplate
    intent: Create a WhatsApp template
    question: How do I make a new WhatsApp message template for campaigns?
  phrasing_ops: 9
  slug: brevo-whatsapp-campaigns-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Send transactional WhatsApp messages to recipients using approved templates or plain text.
  name: brevo WhatsApp Messages API
  phrasing_intents:
  - id: sendWhatsAppMessage
    intent: Send a WhatsApp message
    question: What does it take to send a transactional WhatsApp message to a customer?
  phrasing_ops: 1
  slug: brevo-whatsapp-messages-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create and manage WhatsApp message templates that require Meta approval before use.
  name: brevo WhatsApp Templates API
  phrasing_intents:
  - id: createWhatsAppTemplate
    intent: Create a WhatsApp message template
    question: How do I create a WhatsApp template for marketing or utility messages?
  - id: listWhatsAppTemplates
    intent: List WhatsApp templates
    question: Which of my WhatsApp templates have been approved?
  - id: sendWhatsAppTemplateForApproval
    intent: Submit a WhatsApp template for approval
    question: How do I get a WhatsApp template approved by Meta?
  phrasing_ops: 3
  slug: brevo-whatsapp-templates-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The account API from Brevo — 2 operation(s) for account.
  name: Brevo Account API
  phrasing_intents:
  - id: getAccount
    intent: Get account and plan details
    question: How many email credits are left on my Brevo plan?
  - id: getAccountActivity
    intent: Get user activity logs
    question: Who logged in to our account recently and from where?
  phrasing_ops: 2
  slug: brevo-account-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The balance API from Brevo — 12 operation(s) for balance.
  name: Brevo Balance API
  phrasing_intents:
  - id: getBalanceDefinitionList
    intent: List balance definitions in a loyalty program
    question: Which point or credit balances are defined in my loyalty program?
  - id: createBalanceDefinition
    intent: Create a balance definition
    question: How do I set up a new points balance with its own unit in a loyalty program?
  - id: getBalanceDefinition
    intent: Get a balance definition
    question: What are the settings of one specific balance definition, like its unit and limits?
  - id: updateBalanceDefinition
    intent: Update a balance definition
    question: Can I change the name, unit or rounding rules of an existing balance definition?
  - id: deleteBalanceDefinition
    intent: Delete a balance definition
    question: Can I remove a balance definition from my loyalty program?
  - id: createBalanceLimit
    intent: Add a limit to a balance definition
    question: How do I cap how many points a member can earn per week?
  - id: getBalanceLimit
    intent: Get a balance limit
    question: What are the constraints of a specific limit on a balance definition?
  - id: deleteBalanceLimit
    intent: Delete a balance limit
    question: Can I remove an earning or spending cap from a balance?
  phrasing_ops: 18
  slug: brevo-balance-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The companies API from Brevo — 6 operation(s) for companies.
  name: Brevo Companies API
  phrasing_intents:
  - id: getAllCompanies
    intent: List CRM companies
    question: Which companies are in my Brevo CRM?
  - id: createACompany
    intent: Create a CRM company
    question: How do I add a new company to the CRM?
  - id: getACompany
    intent: Get a CRM company
    question: What contacts and deals are linked to a specific company?
  - id: deleteACompany
    intent: Delete a CRM company
    question: Who is allowed to delete a company from the CRM?
  - id: updateACompany
    intent: Update a CRM company
    question: How do I rename a company or change its attributes?
  - id: createACompanyDealAttribute
    intent: Create a custom company or deal attribute
    question: Can I add a custom field to companies or deals in the CRM?
  - id: getCompanyAttributes
    intent: List company attributes
    question: What fields are defined on companies, including my custom ones?
  - id: linkAndUnlinkCompanyWithContactAndDeal
    intent: Link or unlink contacts and deals on a company
    question: How do I attach a contact to a company without replacing its other contacts?
  phrasing_ops: 9
  slug: brevo-companies-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The conversations API from Brevo — 6 operation(s) for conversations.
  name: Brevo Conversations API
  phrasing_intents:
  - id: deleteAMessageSentByAnAgent
    intent: Delete a message an agent sent
    question: How do I delete a chat reply an agent posted by mistake?
  - id: updateAMessageSentByAnAgent
    intent: Edit a message an agent sent
    question: Can I fix a typo in a chat reply an agent already sent?
  - id: getAMessage
    intent: Get a conversation message
    question: What did a specific chat message in Brevo Conversations say?
  - id: sendAMessageAsAnAgent
    intent: Reply to a visitor as an agent
    question: How do I post a chat reply to a website visitor as one of my agents?
  - id: deleteAnAutomatedMessage
    intent: Delete an automated chat message
    question: How do I remove a pushed message from a visitor's chat?
  - id: updateAnAutomatedMessage
    intent: Edit an automated chat message
    question: Can I change the text of an automated message after it was pushed?
  - id: getAnAutomatedMessage
    intent: Get an automated chat message
    question: What did an automated pushed message to a visitor contain?
  - id: sendAnAutomatedMessageToAVisitor
    intent: Push an automated message to a visitor
    question: How do I push an order status update into a visitor's chat window?
  phrasing_ops: 10
  slug: brevo-conversations-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The coupons API from Brevo — 3 operation(s) for coupons.
  name: Brevo Coupons API
  phrasing_intents:
  - id: getCouponCollections
    intent: List coupon collections
    question: What coupon collections do I have and how many coupons remain?
  - id: createCouponCollection
    intent: Create a coupon collection
    question: How do I set up a new pool of discount coupons?
  - id: getCouponCollection
    intent: Get a coupon collection
    question: How many coupons are left in one collection?
  - id: updateCouponCollection
    intent: Update a coupon collection
    question: Can I change the expiration date of a coupon collection?
  - id: createCoupons
    intent: Add coupon codes to a collection
    question: How do I upload coupon codes into a collection?
  phrasing_ops: 5
  slug: brevo-coupons-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The deals API from Brevo — 8 operation(s) for deals.
  name: Brevo Deals API
  phrasing_intents:
  - id: getPipelineStages
    intent: Get pipeline stages (deprecated)
    question: Is there an older endpoint that returns the default pipeline's stages?
  - id: getAPipeline
    intent: Get a deal pipeline
    question: What stages and order does a specific sales pipeline have?
  - id: getAllPipelines
    intent: List all deal pipelines
    question: What sales pipelines are configured in my CRM?
  - id: getDealAttributes
    intent: List deal attributes
    question: Which fields can I set on a deal?
  - id: getAllDeals
    intent: List and filter deals
    question: Can I find deals owned by a specific person or in a given stage?
  - id: createADeal
    intent: Create a deal
    question: How do I add a new deal to my CRM pipeline?
  - id: getADeal
    intent: Get a deal
    question: What stage is a particular deal in?
  - id: deleteADeal
    intent: Delete a deal
    question: Who is allowed to delete a deal?
  phrasing_ops: 11
  slug: brevo-deals-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The domains API from Brevo — 3 operation(s) for domains.
  name: Brevo Domains API
  phrasing_intents:
  - id: getDomains
    intent: List sender domains
    question: Which sending domains have I added to Brevo?
  - id: createDomain
    intent: Add a sender domain
    question: How do I add my company domain for sending emails?
  - id: deleteDomain
    intent: Delete a sender domain
    question: How do I remove a test domain from my sending setup?
  - id: getDomainConfiguration
    intent: Check a sender domain's configuration
    question: Is my sending domain configured correctly?
  - id: authenticateDomain
    intent: Authenticate a sender domain
    question: I've added the DNS records, how do I get the domain authenticated?
  phrasing_ops: 5
  slug: brevo-domains-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The ecommerce API from Brevo — 15 operation(s) for ecommerce.
  name: Brevo Ecommerce API
  phrasing_intents:
  - id: createOrder
    intent: Record or update an order's status
    question: How do I send an order and its status from my store into Brevo?
  - id: createBatchOrder
    intent: Create orders in batch
    question: Can I upload many orders at once instead of one at a time?
  - id: getOrders
    intent: List orders
    question: What orders have been synced into my Brevo account?
  - id: createUpdateProduct
    intent: Create or update a product
    question: How do I add a single product with price and SKU to my catalog?
  - id: getProducts
    intent: List and filter products
    question: Which products are in my Brevo ecommerce catalog?
  - id: getProductInfo
    intent: Get a product's details
    question: What is the stock level and price of a specific product?
  - id: createUpdateBatchProducts
    intent: Create or update products in batch
    question: Can I upload many products in one request?
  - id: createProductAlert
    intent: Subscribe a contact to a product alert
    question: How do I notify a shopper when a product is back in stock?
  phrasing_ops: 18
  slug: brevo-ecommerce-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The event API from Brevo — 2 operation(s) for event.
  name: Brevo Event API
  phrasing_intents:
  - id: getEvents
    intent: List custom events
    question: Which custom events has a particular contact triggered?
  - id: createEvent
    intent: Track a contact event
    question: How do I record that a contact did something on my site, like viewing a page?
  - id: createBatchEvents
    intent: Track many contact events at once
    question: Can I send a bulk batch of tracked events in one request?
  phrasing_ops: 3
  slug: brevo-event-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The files API from Brevo — 3 operation(s) for files.
  name: Brevo Files API
  phrasing_intents:
  - id: getAllFiles
    intent: List CRM files
    question: Which files are attached to my CRM contacts, companies or deals?
  - id: uploadAFile
    intent: Upload a file to the CRM
    question: How do I attach a document to a deal or contact?
  - id: downloadAFile
    intent: Get a download link for a file
    question: How do I download a CRM file?
  - id: deleteAFile
    intent: Delete a CRM file
    question: Does deleting a file unlink it from contacts and deals?
  - id: getFileDetails
    intent: Get a file's metadata
    question: What is the size, type and linked records of a CRM file?
  phrasing_ops: 5
  slug: brevo-files-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The inboundParsing API from Brevo — 3 operation(s) for inboundparsing.
  name: Brevo Inbound Parsing API
  phrasing_intents:
  - id: getInboundEmailEvents
    intent: List inbound email events
    question: What emails have been received through inbound parsing lately?
  - id: getInboundEmailEventsByUuid
    intent: Get the event history of one received email
    question: What happened to one specific inbound email?
  - id: getInboundEmailAttachment
    intent: Download an inbound email attachment
    question: How do I download a file attached to a received email?
  phrasing_ops: 3
  slug: brevo-inboundparsing-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The notes API from Brevo — 2 operation(s) for notes.
  name: Brevo Notes API
  phrasing_intents:
  - id: getAllNotes
    intent: List CRM notes
    question: What notes have been logged against a company or deal in the CRM?
  - id: createANote
    intent: Create a CRM note
    question: How do I log a note after a call with a customer?
  - id: getANote
    intent: Get a CRM note
    question: Who wrote a given note and what does it say?
  - id: updateANote
    intent: Update a CRM note
    question: Can I edit the text of a note I already saved?
  - id: deleteANote
    intent: Delete a CRM note
    question: How do I delete a note logged by mistake?
  phrasing_ops: 5
  slug: brevo-notes-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The payments API from Brevo — 2 operation(s) for payments.
  name: Brevo Payments API
  phrasing_intents:
  - id: createPaymentRequest
    intent: Request a payment from a contact
    question: How do I send a contact a link to pay me?
  - id: getPaymentRequest
    intent: Get a payment request
    question: Has a contact paid the payment request I sent?
  - id: deletePaymentRequest
    intent: Delete a payment request
    question: Can I cancel a payment request so it can no longer be paid?
  phrasing_ops: 3
  slug: brevo-payments-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The process API from Brevo — 2 operation(s) for process.
  name: Brevo Process API
  phrasing_intents:
  - id: getProcesses
    intent: List background processes
    question: What imports or exports are running in the background?
  - id: getProcess
    intent: Get a background process
    question: Has my contact import finished yet?
  phrasing_ops: 2
  slug: brevo-process-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The program API from Brevo — 7 operation(s) for program.
  name: Brevo Program API
  phrasing_intents:
  - id: getLPList
    intent: List loyalty programs
    question: Which loyalty programs have I set up in Brevo?
  - id: createNewLP
    intent: Create a loyalty program
    question: How do I start a new customer loyalty program?
  - id: getLoyaltyProgramInfo
    intent: Get a loyalty program
    question: What are the settings of one of my loyalty programs?
  - id: updateLoyaltyProgram
    intent: Replace a loyalty program's details
    question: How do I overwrite a loyalty program's name and description together?
  - id: partiallyUpdateLoyaltyProgram
    intent: Partially update a loyalty program
    question: Can I change just the description of a loyalty program without resending its name?
  - id: deleteLoyaltyProgram
    intent: Delete a loyalty program
    question: Can I delete a loyalty program I no longer run?
  - id: publishLoyaltyProgram
    intent: Publish a loyalty program
    question: How do I make a draft loyalty program live?
  - id: subscribeToLoyaltyProgram
    intent: Enroll a contact in a loyalty program
    question: How do I sign a customer up for my loyalty program?
  phrasing_ops: 12
  slug: brevo-program-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The reward API from Brevo — 9 operation(s) for reward.
  name: Brevo Reward API
  phrasing_intents:
  - id: getCodeCount
    intent: Count codes in a reward code pool
    question: How many voucher codes are left in a code pool?
  - id: getVoucherForAContact
    intent: List a contact's vouchers
    question: Which vouchers has a specific contact been given?
  - id: getRewardPageApi
    intent: List rewards in a loyalty program
    question: What rewards are offered in my loyalty program?
  - id: createReward
    intent: Create a reward
    question: How do I add a new reward to my loyalty program?
  - id: getRewardInformation
    intent: Get a reward
    question: What are the details of one specific reward?
  - id: createVoucher
    intent: Issue a voucher to a member
    question: How do I give a loyalty member a voucher for a reward?
  - id: redeemVoucher
    intent: Request to redeem a voucher
    question: How do I start redeeming a member's voucher at checkout?
  - id: completeRedeemTransaction
    intent: Complete a voucher redemption
    question: How do I finalize a pending voucher redemption?
  phrasing_ops: 10
  slug: brevo-reward-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The tasks API from Brevo — 3 operation(s) for tasks.
  name: Brevo Tasks API
  phrasing_intents:
  - id: getAllTaskTypes
    intent: List task types
    question: What kinds of CRM tasks can I create, like calls or meetings?
  - id: getAllTasks
    intent: List and filter tasks
    question: Which CRM tasks are assigned to a specific person?
  - id: createATask
    intent: Create a task
    question: How do I create a follow-up task in the CRM?
  - id: getATask
    intent: Get a task
    question: What are the details and linked records of a specific task?
  - id: deleteATask
    intent: Delete a task
    question: Does deleting a task cancel its reminders?
  - id: updateATask
    intent: Update a task
    question: Can I mark a task as done?
  phrasing_ops: 6
  slug: brevo-tasks-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The tier API from Brevo — 6 operation(s) for tier.
  name: Brevo Tier API
  phrasing_intents:
  - id: createTierGroup
    intent: Create a tier group
    question: How do I set up a tier group like Silver, Gold and Platinum?
  - id: getListOfTierGroups
    intent: List tier groups
    question: What tier groups are set up in my loyalty program?
  - id: updateTierGroup
    intent: Update a tier group
    question: Can I change the downgrade strategy or tier order of an existing group?
  - id: deleteTierGroup
    intent: Delete a tier group
    question: Can I remove a whole tier group from my loyalty program?
  - id: getTierGroup
    intent: Get a tier group
    question: What are the upgrade and downgrade rules for one tier group?
  - id: getLoyaltyProgramTier
    intent: List tiers
    question: What tiers exist across my loyalty program?
  - id: createTierForTierGroup
    intent: Create a tier in a tier group
    question: How do I add a new level to a tier group with its entry conditions?
  - id: deleteTier
    intent: Delete a tier
    question: Can I delete a single tier from a tier group?
  phrasing_ops: 10
  slug: brevo-tier-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The transactionalWhatsApp API from Brevo — 2 operation(s) for transactionalwhatsapp.
  name: Brevo Transactional Whats App API
  phrasing_intents:
  - id: sendWhatsappMessage
    intent: Send a transactional WhatsApp message
    question: How do I send a WhatsApp message to a customer through Brevo?
  - id: getWhatsappEventReport
    intent: List WhatsApp message events
    question: Were my WhatsApp messages to a given number delivered and read?
  phrasing_ops: 2
  slug: brevo-transactionalwhatsapp-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The user API from Brevo — 6 operation(s) for user.
  name: Brevo User API
  phrasing_intents:
  - id: getInvitedUsersList
    intent: List users in the organization
    question: Who has access to my Brevo organization, including pending invites?
  - id: getUserPermission
    intent: Check a user's feature permissions
    question: What features can a specific teammate access in our organization?
  - id: putRevokeUserPermission
    intent: Revoke a user's access
    question: How do I remove a teammate's access to the organization?
  - id: putresendcancelinvitation
    intent: Resend or cancel a user invitation
    question: Can I resend an organization invite that expired?
  - id: inviteuser
    intent: Invite a user to the organization
    question: How do I invite a colleague to our Brevo organization?
  - id: EditUserPermission
    intent: Update an existing user's permissions
    question: How do I change what an existing teammate can do?
  phrasing_ops: 6
  slug: brevo-user-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The wallet API from Brevo — 1 operation(s) for wallet.
  name: Brevo Wallet API
  phrasing_intents:
  - id: getWalletPassInstallUrl
    intent: Get a wallet pass install link for a contact
    question: How do I give a customer a link to add their loyalty pass to their phone wallet?
  phrasing_ops: 1
  slug: brevo-wallet-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The Consent Groups API from Brevo — 2 operation(s) for consent groups.
  name: Brevo Consent Groups API
  phrasing_intents:
  - id: getConsentGroups
    intent: List consent groups
    question: Which consent groups have I set up for my contacts?
  - id: createConsentGroup
    intent: Create a consent group
    question: How do I create a consent group to track marketing opt-ins?
  - id: getConsentGroup
    intent: Get a consent group
    question: What signup mode and description does one consent group have?
  - id: updateConsentGroup
    intent: Update a consent group
    question: Can I rename a consent group or change its description?
  - id: deleteConsentGroup
    intent: Delete a consent group
    question: What happens to contacts when I delete their consent group?
  phrasing_ops: 5
  slug: brevo-consent-groups-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The Custom Objects API from Brevo — 3 operation(s) for custom objects.
  name: Brevo Custom Objects API
  phrasing_intents:
  - id: upsertrecords
    intent: Create or update custom object records in bulk
    question: How do I bulk load records into one of my custom objects?
  - id: getrecords
    intent: List custom object records
    question: What records exist for one of my custom objects and how many in total?
  - id: batchDeleteObjectRecords
    intent: Delete custom object records in bulk
    question: Can I delete up to a thousand custom object records at once?
  phrasing_ops: 3
  slug: brevo-custom-objects-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The Email Campaigns API from Brevo — 10 operation(s) for email campaigns.
  name: Brevo Email Campaigns API
  phrasing_intents:
  - id: getEmailCampaigns
    intent: List email campaigns
    question: Which email campaigns have I sent or scheduled in Brevo?
  - id: createEmailCampaign
    intent: Create an email campaign
    question: How do I set up a new newsletter campaign as a draft?
  - id: updateEmailCampaign
    intent: Update an email campaign
    question: Can I change the subject or send time of a campaign I already created?
  - id: deleteEmailCampaign
    intent: Delete an email campaign
    question: Why can't I delete an email campaign that's already scheduled?
  - id: getEmailCampaign
    intent: Get an email campaign's report
    question: How did a specific email campaign perform in opens and clicks?
  - id: sendEmailCampaignNow
    intent: Send an email campaign immediately
    question: Can I send an email campaign right now instead of scheduling it?
  - id: sendTestEmail
    intent: Send a test of an email campaign
    question: How do I preview a campaign in my own inbox before it goes out?
  - id: updateCampaignStatus
    intent: Suspend, archive or replicate an email campaign
    question: Can I pause an email campaign that's scheduled?
  phrasing_ops: 13
  slug: brevo-email-campaigns-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The External Feeds API from Brevo — 2 operation(s) for external feeds.
  name: Brevo External Feeds API
  phrasing_intents:
  - id: getAllExternalFeeds
    intent: List external feeds
    question: Which external data feeds are powering dynamic content in my emails?
  - id: createExternalFeed
    intent: Create an external feed
    question: How do I pull product data from my own URL into email campaigns?
  - id: getExternalFeedByUUID
    intent: Get an external feed
    question: What URL and authentication does one of my feeds use?
  - id: updateExternalFeed
    intent: Update an external feed
    question: How do I point an existing feed at a new data URL?
  - id: deleteExternalFeed
    intent: Delete an external feed
    question: How do I remove a data feed I don't use anymore?
  phrasing_ops: 5
  slug: brevo-external-feeds-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The Master Account API from Brevo — 21 operation(s) for master account.
  name: Brevo Master Account API
  phrasing_intents:
  - id: getTheListOfAllTheSubAccountsOfTheMasterAccount
    intent: List all sub-accounts under the master account
    question: Which sub-accounts sit under my Brevo corporate master account?
  - id: createANewSubAccountUnderAMasterAccount
    intent: Create a new sub-account
    question: How do I spin up a new sub-account for a client under my corporate account?
  - id: getSubAccountDetails
    intent: Get details of one sub-account
    question: What plan, credits and company info does a specific sub-account have?
  - id: deleteASubAccount
    intent: Permanently delete a sub-account
    question: Can I permanently remove a sub-account and all its data from my master account?
  - id: updateSubAccountPlan
    intent: Update one sub-account's plan and credits
    question: How do I give a single sub-account more email or SMS credits?
  - id: updateSubAccountsPlan
    intent: Update the plan for several sub-accounts at once
    question: Can I update credits for many sub-accounts in one request?
  - id: generateSsoTokenToAccessAdminAccount
    intent: Generate an SSO token for the admin account
    question: How can an admin user log into the corporate admin account with single sign-on?
  - id: generateSsoTokenToAccessSubAccount
    intent: Generate an SSO token to access a sub-account
    question: How do I log into a client's sub-account from the master account without a password?
  phrasing_ops: 26
  slug: brevo-master-account-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The SMS Campaigns API from Brevo — 7 operation(s) for sms campaigns.
  name: Brevo SMS Campaigns API
  phrasing_intents:
  - id: getSmsCampaigns
    intent: List SMS campaigns
    question: Which SMS campaigns have I created in Brevo?
  - id: createSmsCampaign
    intent: Create an SMS campaign
    question: How do I set up a bulk text message campaign?
  - id: getSmsCampaign
    intent: Get an SMS campaign
    question: How many texts in a specific SMS campaign were delivered?
  - id: updateSmsCampaign
    intent: Update an SMS campaign
    question: Can I change the text of an SMS campaign before it sends?
  - id: deleteSmsCampaign
    intent: Delete an SMS campaign
    question: Can I delete an SMS campaign that has already been scheduled?
  - id: sendSmsCampaignNow
    intent: Send an SMS campaign immediately
    question: How do I send an SMS campaign right away?
  - id: updateSmsCampaignStatus
    intent: Suspend, archive or replicate an SMS campaign
    question: Can I pause a scheduled SMS campaign?
  - id: sendTestSms
    intent: Send a test SMS of a campaign
    question: Can I text myself a preview of an SMS campaign first?
  phrasing_ops: 10
  slug: brevo-sms-campaigns-api
artifact_total: 347
asyncapis:
- description: Brevo delivers real-time event notifications via webhooks for transactional emails, marketing campaigns, transactional SMS, and conversations. When configured, Brevo sends HTTP POST requests to your s
  name: Brevo Webhook Events
  slug: brevo-webhooks-asyncapi
collections:
- collection_type: open
  name: Accounts and Settings
  slug: open-brevo-accounts-and-settings
- collection_type: open
  name: Brevo Contacts Agent Status API
  slug: open-brevo-agent-status-api
- collection_type: open
  name: Brevo Contacts Agent Status Automated Messages API
  slug: open-brevo-automated-messages-api
- collection_type: open
  name: Brevo Contacts Agent Status Campaign Statistics API
  slug: open-brevo-campaign-statistics-api
- collection_type: open
  name: Brevo Contacts Agent Status Categories API
  slug: open-brevo-categories-api
- collection_type: open
  name: Brevo Contacts Agent Status Contact Attributes API
  slug: open-brevo-contact-attributes-api
- collection_type: open
  name: Brevo Contacts Agent Status Contact Lists API
  slug: open-brevo-contact-lists-api
- collection_type: open
  name: Contact Management
  slug: open-brevo-contact-management
- collection_type: open
  name: Brevo Agent Status Contacts API
  slug: open-brevo-contacts-api
- collection_type: open
  name: Brevo Contacts API
  slug: open-brevo-contacts
- collection_type: open
  name: Conversations
  slug: open-brevo-conversations
- collection_type: open
  name: Ecommerce
  slug: open-brevo-ecommerce
- collection_type: open
  name: Brevo Contacts Agent Status Email Activity API
  slug: open-brevo-email-activity-api
- collection_type: open
  name: Email API
  slug: open-brevo-email-api
- collection_type: open
  name: Brevo Contacts Agent Status Email Campaigns API
  slug: open-brevo-email-campaigns-api
- collection_type: open
  name: Brevo Email Campaigns API
  slug: open-brevo-email-campaigns
- collection_type: open
  name: Brevo Contacts Agent Status Email Templates API
  slug: open-brevo-email-templates-api
- collection_type: open
  name: Events
  slug: open-brevo-events
- collection_type: open
  name: Brevo Contacts Agent Status Folders API
  slug: open-brevo-folders-api
- collection_type: open
  name: Brevo Contacts Agent Status Import API
  slug: open-brevo-import-api
- collection_type: open
  name: Loyalty
  slug: open-brevo-loyalty
- collection_type: open
  name: Marketing Campaigns
  slug: open-brevo-marketing-campaigns
- collection_type: open
  name: Brevo Contacts Agent Status Messages API
  slug: open-brevo-messages-api
- collection_type: open
  name: Object Management
  slug: open-brevo-object-management
- collection_type: open
  name: Brevo Contacts Agent Status Orders API
  slug: open-brevo-orders-api
- collection_type: open
  name: Brevo Contacts Agent Status Products API
  slug: open-brevo-products-api
- collection_type: open
  name: Sales CRM
  slug: open-brevo-sales-crm
- collection_type: open
  name: Brevo Contacts Agent Status Senders API
  slug: open-brevo-senders-api
- collection_type: open
  name: Brevo Contacts Agent Status SMS Statistics API
  slug: open-brevo-sms-statistics-api
- collection_type: open
  name: Brevo Transactional Email API
  slug: open-brevo-transactional-email
- collection_type: open
  name: Brevo Contacts Agent Status Transactional Emails API
  slug: open-brevo-transactional-emails-api
- collection_type: open
  name: Brevo Contacts Agent Status Transactional SMS API
  slug: open-brevo-transactional-sms-api
- collection_type: open
  name: Transactional SMS
  slug: open-brevo-transactional-sms
- collection_type: open
  name: Transactional WhatsApp
  slug: open-brevo-transactional-whatsapp
- collection_type: open
  name: Wallet
  slug: open-brevo-wallet
- collection_type: open
  name: Brevo Contacts Agent Status Webhooks API
  slug: open-brevo-webhooks-api
- collection_type: open
  name: Brevo Webhooks API
  slug: open-brevo-webhooks
- collection_type: open
  name: Brevo Contacts Agent Status WhatsApp Campaigns API
  slug: open-brevo-whatsapp-campaigns-api
- collection_type: open
  name: Brevo Contacts Agent Status WhatsApp Messages API
  slug: open-brevo-whatsapp-messages-api
- collection_type: open
  name: Brevo Contacts Agent Status WhatsApp Templates API
  slug: open-brevo-whatsapp-templates-api
- collection_type: open
  name: Brevo WhatsApp API
  slug: open-brevo-whatsapp
common:
- group: design
  href: https://artifacts.apis.io/brevo/rules/brevo-rules.yml
  title: ''
  type: Spectral
  url: rules/brevo-rules.yml
- group: design
  href: https://artifacts.apis.io/brevo/rules/brevo-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/brevo-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/brevo/rules/brevo-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/brevo-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/brevo/asyncapi/brevo-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/brevo-webhooks-asyncapi.yml
- group: other
  href: https://artifacts.apis.io/brevo/hosts/brevo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brevo-hosts.yml
- group: build
  href: https://artifacts.apis.io/brevo/integrations/brevo-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/brevo-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/brevo/vendors/brevo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brevo-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.brevo.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.brevo.com/company/leadership/
- group: other
  href: https://artifacts.apis.io/brevo/capabilities/brevo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/brevo-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/brevo/agentic-access/brevo-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/brevo-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/brevo/security/brevo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brevo-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/brevo/authentication/brevo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/brevo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getbrevo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brevo
- group: design
  href: https://artifacts.apis.io/brevo/json-ld/brevo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brevo-context.jsonld
- group: docs
  href: https://artifacts.apis.io/brevo/json-schema/brevo-contact-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/brevo-contact-schema.json
- group: docs
  href: https://artifacts.apis.io/brevo/json-schema/brevo-email-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/brevo-email-event-schema.json
- group: docs
  href: https://artifacts.apis.io/brevo/json-schema/brevo-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/brevo-order-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.brevo.com/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: https://developers.brevo.com/.well-known/api-catalog
- group: agent
  href: https://artifacts.apis.io/brevo/well-known/brevo-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brevo-well-known.yml
- group: other
  href: https://artifacts.apis.io/brevo/well-known/brevo-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/brevo-api-catalog.json
- group: build
  href: https://artifacts.apis.io/brevo/packages/brevo-packages.yml
  title: ''
  type: Packages
  url: packages/brevo-packages.yml
- group: build
  href: https://artifacts.apis.io/brevo/packages/brevo-packages.yml
  title: ''
  type: SDKs
  url: packages/brevo-packages.yml
- group: build
  href: https://artifacts.apis.io/brevo/cli/brevo-cli.yml
  title: ''
  type: CLI
  url: cli/brevo-cli.yml
- group: agent
  href: https://artifacts.apis.io/brevo/mcp/brevo-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/brevo-mcp.yml
- group: build
  href: https://artifacts.apis.io/brevo/mcp/brevo-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/brevo-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/brevo/llms/brevo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/brevo-llms.txt
- group: design
  href: https://artifacts.apis.io/brevo/conventions/brevo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/brevo-conventions.yml
- group: design
  href: https://artifacts.apis.io/brevo/conventions/brevo-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/brevo-conventions.yml
- group: design
  href: https://artifacts.apis.io/brevo/errors/brevo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/brevo-problem-types.yml
- group: design
  href: https://artifacts.apis.io/brevo/lifecycle/brevo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/brevo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brevo.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.brevo.com/changelog/2026/5/12
- group: operate
  href: https://artifacts.apis.io/brevo/changelog/brevo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/brevo-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.brevo.com/changelog
- group: auth
  href: https://artifacts.apis.io/brevo/scopes/brevo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/brevo-scopes.yml
- group: design
  href: https://artifacts.apis.io/brevo/conformance/brevo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brevo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.brevo.com/features/data-security/
- group: auth
  href: https://artifacts.apis.io/brevo/security/brevo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/brevo-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/brevo/security/brevo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/brevo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.brevo.com/legal/responsible-disclosure/
- group: start
  href: https://artifacts.apis.io/brevo/sandbox/brevo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/brevo-sandbox.yml
- group: design
  href: https://artifacts.apis.io/brevo/components/brevo-components.yml
  title: ''
  type: Components
  url: components/brevo-components.yml
- group: design
  href: https://artifacts.apis.io/brevo/data-model/brevo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brevo-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/brevo/plans/brevo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brevo-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/brevo/rate-limits/brevo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/brevo-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/brevo/finops/brevo-finops.yml
  title: ''
  type: FinOps
  url: finops/brevo-finops.yml
- group: design
  href: https://artifacts.apis.io/brevo/vocabulary/brevo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brevo-vocabulary.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developers.brevo.com/docs/how-to-use-webhooks
- group: docs
  href: https://artifacts.apis.io/brevo/asyncapi/brevo-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/brevo-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/brevo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-email-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-email-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-transactional-sms-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-transactional-sms-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-transactional-whatsapp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-transactional-whatsapp-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-marketing-campaigns-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-marketing-campaigns-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-contact-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-contact-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-events-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-object-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-object-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-accounts-and-settings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-accounts-and-settings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-sales-crm-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-sales-crm-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-conversations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-conversations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-ecommerce-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-ecommerce-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-loyalty-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-loyalty-overlay.yaml
- group: other
  href: https://artifacts.apis.io/brevo/overlays/brevo-wallet-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/brevo-wallet-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.brevo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.brevo.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.brevo.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.brevo.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.brevo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.brevo.com/blog/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/sib-apiv3/workspace/sendinblue
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brevo.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://onboarding.brevo.com/account/register
- group: start
  title: ''
  type: Login
  url: https://app.brevo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brevo.com/legal/termsofuse/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brevo.com/legal/privacypolicy/
- group: company
  title: ''
  type: Website
  url: https://www.brevo.com/
created: '2026-05-04'
description: Brevo (formerly Sendinblue) is a French customer-relationship platform that combines email marketing, transactional email and SMTP relay, transactional and campaign SMS, WhatsApp messaging, web and mobile push, live chat, a sales CRM, an ecommerce attribution layer and a loyalty and rewards engine behind a single REST API at api.brevo.com/v3. Brevo publishes thirteen OpenAPI 3.1 definitions covering 285 operations, advertises them through an RFC 9727 API catalog at its developer portal, ships seven official SDKs and a first-party CLI for OAuth app management, and operates a hosted MCP server exposing 27 modules to AI agents.
finops:
- has_sources: true
  method: derived
  name: Brevo Finops
  primary_unit: subscription
  service_category: ''
  slug: brevo-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brevo.png
json_schemas:
- name: Account_getAccountActivity_Response_200
  property_count: 1
  slug: brevo-account-get-account-activity-response-200
- name: Account_getAccount_Response_200
  property_count: 12
  slug: brevo-account-get-account-response-200
- name: AggregatedEmailReport
  property_count: 13
  slug: brevo-aggregated-email-report
- name: AggregatedSmsReport
  property_count: 7
  slug: brevo-aggregated-sms-report
- name: AggregatedEmailReport
  property_count: 13
  slug: brevo-aggregatedemailreport
- name: AggregatedSmsReport
  property_count: 7
  slug: brevo-aggregatedsmsreport
- name: AutomatedMessageResponse
  property_count: 5
  slug: brevo-automated-message-response
- name: AutomatedMessageResponse
  property_count: 5
  slug: brevo-automatedmessageresponse
- name: Balance_createBalanceOrder_Response_200
  property_count: 12
  slug: brevo-balance-create-balance-order-response-200
- name: Balance_createSubscriptionBalances_Response_200
  property_count: 9
  slug: brevo-balance-create-subscription-balances-response-200
- name: balanceDefinition
  property_count: 20
  slug: brevo-balance-definition
- name: Balance_getTransactionHistoryApi_Response_200
  property_count: 5
  slug: brevo-balance-get-transaction-history-api-response-200
- name: balanceLimit
  property_count: 10
  slug: brevo-balance-limit
- name: batchAcceptedResponse
  property_count: 2
  slug: brevo-batch-accepted-response
- name: cart
  property_count: 2
  slug: brevo-cart
- name: CategoriesBatchPostRequestBodyContentApplicationJsonSchemaCategoriesItems
  property_count: 5
  slug: brevo-categories-batch-post-request-body-content-application-json-schema-categories-items
- name: CategoryList
  property_count: 2
  slug: brevo-category-list
- name: Category
  property_count: 5
  slug: brevo-category
- name: CategoryList
  property_count: 2
  slug: brevo-categorylist
- name: Companies_getAllCompanies_Response_200
  property_count: 1
  slug: brevo-companies-get-all-companies-response-200
- name: CompaniesImportPostRequestBodyContentMultipartFormDataSchemaMapping
  property_count: 0
  slug: brevo-companies-import-post-request-body-content-multipart-form-data-schema-mapping
- name: Company
  property_count: 4
  slug: brevo-company
- name: configuration
  property_count: 1
  slug: brevo-configuration
- name: ConsentGroup
  property_count: 8
  slug: brevo-consent-group
- name: ConsentGroupsListResponse
  property_count: 4
  slug: brevo-consent-groups-list-response
- name: Brevo Contact
  property_count: 10
  slug: brevo-contact
- name: ContactAttributeList
  property_count: 1
  slug: brevo-contactattributelist
- name: ContactList
  property_count: 2
  slug: brevo-contactlist
- name: ContactListCollection
  property_count: 2
  slug: brevo-contactlistcollection
- name: ContactListDetail
  property_count: 6
  slug: brevo-contactlistdetail
- name: ContactsAttributesAttributeCategoryAttributeNamePostRequestBodyContentApplicationJsonSchemaType
  property_count: 0
  slug: brevo-contacts-attributes-attribute-category-attribute-name-post-request-body-content-application-json-schema-type
- name: ContactsExportPostRequestBodyContentApplicationJsonSchemaCustomContactFilter
  property_count: 7
  slug: brevo-contacts-export-post-request-body-content-application-json-schema-custom-contact-filter
- name: Contacts_getContactInfo_Response_200
  property_count: 12
  slug: brevo-contacts-get-contact-info-response-200
- name: Contacts_getContactStats_Response_200
  property_count: 9
  slug: brevo-contacts-get-contact-stats-response-200
- name: Contacts_getList_Response_200
  property_count: 9
  slug: brevo-contacts-get-list-response-200
- name: ConversationsMessage
  property_count: 31
  slug: brevo-conversations-message
- name: Conversations_setVisitorGroupAssignment_Response_200
  property_count: 2
  slug: brevo-conversations-set-visitor-group-assignment-response-200
- name: Conversations_setsAgentsStatusToOnlineFor23Minutes_Response_201
  property_count: 0
  slug: brevo-conversations-sets-agents-status-to-online-for23-minutes-response-201
- name: CorporateSubAccountIdPlanPutRequestBodyContentApplicationJsonSchemaCredits
  property_count: 5
  slug: brevo-corporate-sub-account-id-plan-put-request-body-content-application-json-schema-credits
- name: CorporateSubAccountSsoTokenPostRequestBodyContentApplicationJsonSchemaTarget
  property_count: 0
  slug: brevo-corporate-sub-account-sso-token-post-request-body-content-application-json-schema-target
- name: CorporateSubAccountsPlanPutRequestBodyContentApplicationJsonSchemaCredits
  property_count: 5
  slug: brevo-corporate-sub-accounts-plan-put-request-body-content-application-json-schema-credits
- name: Coupons_createCouponCollection_Response_201
  property_count: 1
  slug: brevo-coupons-create-coupon-collection-response-201
- name: Coupons_updateCouponCollection_Response_200
  property_count: 3
  slug: brevo-coupons-update-coupon-collection-response-200
- name: CreateAutomatedMessage
  property_count: 4
  slug: brevo-create-automated-message
- name: CreateConsentGroupRequest
  property_count: 4
  slug: brevo-create-consent-group-request
- name: CreateSmtpTemplate
  property_count: 6
  slug: brevo-create-smtp-template
- name: CreateTemplateResponse
  property_count: 1
  slug: brevo-create-template-response
- name: CreateUpdateCategory
  property_count: 3
  slug: brevo-create-update-category
- name: CreateUpdateOrder
  property_count: 8
  slug: brevo-create-update-order
- name: CreateUpdateProduct
  property_count: 8
  slug: brevo-create-update-product
- name: CreateWhatsAppCampaign
  property_count: 4
  slug: brevo-create-whats-app-campaign
- name: CreateWhatsAppTemplate
  property_count: 6
  slug: brevo-create-whats-app-template
- name: CreateAutomatedMessage
  property_count: 4
  slug: brevo-createautomatedmessage
- name: CreateContact
  property_count: 5
  slug: brevo-createcontact
- name: CreateContactAttribute
  property_count: 3
  slug: brevo-createcontactattribute
- name: CreateContactList
  property_count: 2
  slug: brevo-createcontactlist
- name: CreateEmailCampaign
  property_count: 9
  slug: brevo-createemailcampaign
- name: CreateSender
  property_count: 2
  slug: brevo-createsender
- name: CreateSenderResponse
  property_count: 1
  slug: brevo-createsenderresponse
- name: CreateSmtpTemplate
  property_count: 6
  slug: brevo-createsmtptemplate
- name: CreateTemplateResponse
  property_count: 1
  slug: brevo-createtemplateresponse
- name: CreateUpdateCategory
  property_count: 3
  slug: brevo-createupdatecategory
- name: CreateUpdateOrder
  property_count: 8
  slug: brevo-createupdateorder
- name: CreateUpdateProduct
  property_count: 8
  slug: brevo-createupdateproduct
- name: CreateWebhook
  property_count: 5
  slug: brevo-createwebhook
- name: CreateWhatsAppCampaign
  property_count: 4
  slug: brevo-createwhatsappcampaign
- name: CreateWhatsAppTemplate
  property_count: 6
  slug: brevo-createwhatsapptemplate
- name: CrmAttributesCompaniesGetResponsesContentApplicationJsonSchemaItems
  property_count: 6
  slug: brevo-crm-attributes-companies-get-responses-content-application-json-schema-items
- name: CrmAttributesDealsGetResponsesContentApplicationJsonSchemaItems
  property_count: 6
  slug: brevo-crm-attributes-deals-get-responses-content-application-json-schema-items
- name: CrmAttributesPostRequestBodyContentApplicationJsonSchemaAttributeType
  property_count: 0
  slug: brevo-crm-attributes-post-request-body-content-application-json-schema-attribute-type
- name: CrmAttributesPostRequestBodyContentApplicationJsonSchemaObjectType
  property_count: 0
  slug: brevo-crm-attributes-post-request-body-content-application-json-schema-object-type
- name: CrmDealsIdPatchRequestBodyContentApplicationJsonSchemaAttributes
  property_count: 0
  slug: brevo-crm-deals-id-patch-request-body-content-application-json-schema-attributes
- name: CrmDealsImportPostRequestBodyContentMultipartFormDataSchemaMapping
  property_count: 0
  slug: brevo-crm-deals-import-post-request-body-content-multipart-form-data-schema-mapping
- name: CrmDealsPostRequestBodyContentApplicationJsonSchemaAttributes
  property_count: 0
  slug: brevo-crm-deals-post-request-body-content-application-json-schema-attributes
- name: CrmTasktypesGetResponsesContentApplicationJsonSchemaItems
  property_count: 2
  slug: brevo-crm-tasktypes-get-responses-content-application-json-schema-items
- name: Custom Objects_batchDeleteObjectRecords_Response_202
  property_count: 2
  slug: brevo-custom-objects-batch-delete-object-records-response-202
- name: Custom Objects_getrecords_Response_200
  property_count: 2
  slug: brevo-custom-objects-getrecords-response-200
- name: Custom Objects_upsertrecords_Response_202
  property_count: 2
  slug: brevo-custom-objects-upsertrecords-response-202
- name: Deal
  property_count: 4
  slug: brevo-deal
- name: Domains_authenticateDomain_Response_200
  property_count: 2
  slug: brevo-domains-authenticate-domain-response-200
- name: Domains_createDomain_Response_200
  property_count: 5
  slug: brevo-domains-create-domain-response-200
- name: Domains_deleteDomain_Response_200
  property_count: 0
  slug: brevo-domains-delete-domain-response-200
- name: Domains_getDomainConfiguration_Response_200
  property_count: 4
  slug: brevo-domains-get-domain-configuration-response-200
- name: Domains_getDomains_Response_200
  property_count: 4
  slug: brevo-domains-get-domains-response-200
- name: Ecommerce_getDetailedAttributionMetricsForASingleBrevoCampaignOrWorkflow_Response_200
  property_count: 6
  slug: brevo-ecommerce-get-detailed-attribution-metrics-for-asingle-brevo-campaign-or-workflow-response-200
- name: EmailCampaignsCampaignIdPutRequestBodyContentApplicationJsonSchemaRecipients
  property_count: 4
  slug: brevo-email-campaigns-campaign-id-put-request-body-content-application-json-schema-recipients
- name: EmailCampaignsCampaignIdPutRequestBodyContentApplicationJsonSchemaSender
  property_count: 3
  slug: brevo-email-campaigns-campaign-id-put-request-body-content-application-json-schema-sender
- name: Email Campaigns_getAbTestCampaignResult_Response_200
  property_count: 8
  slug: brevo-email-campaigns-get-ab-test-campaign-result-response-200
- name: Email Campaigns_getEmailCampaign_Response_200
  property_count: 42
  slug: brevo-email-campaigns-get-email-campaign-response-200
- name: EmailCampaignsPostRequestBodyContentApplicationJsonSchemaRecipients
  property_count: 4
  slug: brevo-email-campaigns-post-request-body-content-application-json-schema-recipients
- name: EmailCampaignsPostRequestBodyContentApplicationJsonSchemaSender
  property_count: 3
  slug: brevo-email-campaigns-post-request-body-content-application-json-schema-sender
- name: EmailEventReport
  property_count: 1
  slug: brevo-email-event-report
- name: Brevo Email Event
  property_count: 14
  slug: brevo-email-event
- name: EmailCampaign
  property_count: 11
  slug: brevo-emailcampaign
- name: EmailCampaignList
  property_count: 2
  slug: brevo-emailcampaignlist
- name: EmailEventReport
  property_count: 1
  slug: brevo-emaileventreport
- name: ErrorResponse
  property_count: 2
  slug: brevo-errorresponse
- name: EventsBatchPostRequestBodyContentApplicationJsonSchemaEventsItems
  property_count: 6
  slug: brevo-events-batch-post-request-body-content-application-json-schema-events-items
- name: EventsPostRequestBodyContentApplicationJsonSchemaEventProperties
  property_count: 0
  slug: brevo-events-post-request-body-content-application-json-schema-event-properties
- name: EventsPostRequestBodyContentApplicationJsonSchemaIdentifiers
  property_count: 6
  slug: brevo-events-post-request-body-content-application-json-schema-identifiers
- name: EventsPostRequestBodyContentApplicationJsonSchemaObject
  property_count: 2
  slug: brevo-events-post-request-body-content-application-json-schema-object
- name: External Feeds_createExternalFeed_Response_201
  property_count: 1
  slug: brevo-external-feeds-create-external-feed-response-201
- name: External Feeds_getAllExternalFeeds_Response_200
  property_count: 2
  slug: brevo-external-feeds-get-all-external-feeds-response-200
- name: External Feeds_getExternalFeedByUUID_Response_200
  property_count: 12
  slug: brevo-external-feeds-get-external-feed-by-uuid-response-200
- name: FeedsPostRequestBodyContentApplicationJsonSchemaAuthType
  property_count: 0
  slug: brevo-feeds-post-request-body-content-application-json-schema-auth-type
- name: FeedsPostRequestBodyContentApplicationJsonSchemaHeadersItems
  property_count: 2
  slug: brevo-feeds-post-request-body-content-application-json-schema-headers-items
- name: FeedsUuidPutRequestBodyContentApplicationJsonSchemaHeadersItems
  property_count: 2
  slug: brevo-feeds-uuid-put-request-body-content-application-json-schema-headers-items
- name: FileData
  property_count: 8
  slug: brevo-file-data
- name: Files_downloadAFile_Response_200
  property_count: 1
  slug: brevo-files-download-afile-response-200
- name: FolderList
  property_count: 2
  slug: brevo-folderlist
- name: getCategoryDetails
  property_count: 6
  slug: brevo-get-category-details
- name: getCouponCollection
  property_count: 9
  slug: brevo-get-coupon-collection
- name: getEventsList
  property_count: 2
  slug: brevo-get-events-list
- name: getFolder
  property_count: 5
  slug: brevo-get-folder
- name: getProductDetails
  property_count: 19
  slug: brevo-get-product-details
- name: getSmtpTemplateOverview
  property_count: 14
  slug: brevo-get-smtp-template-overview
- name: getWebhook
  property_count: 11
  slug: brevo-get-webhook
- name: ImportContacts
  property_count: 9
  slug: brevo-importcontacts
- name: Inbound Parsing_getInboundEmailEventsByUuid_Response_200
  property_count: 8
  slug: brevo-inbound-parsing-get-inbound-email-events-by-uuid-response-200
- name: Inbound Parsing_getInboundEmailEvents_Response_200
  property_count: 1
  slug: brevo-inbound-parsing-get-inbound-email-events-response-200
- name: inviteuser
  property_count: 3
  slug: brevo-inviteuser
- name: LoyaltyOfferProgramsPidRewardsRedeemPostRequestBodyContentApplicationJsonSchemaOrder
  property_count: 12
  slug: brevo-loyalty-offer-programs-pid-rewards-redeem-post-request-body-content-application-json-schema-order
- name: loyaltyProgram
  property_count: 13
  slug: brevo-loyalty-program
- name: LoyaltyTierProgramsPidTierGroupsGidPutRequestBodyContentApplicationJsonSchemaDowngradeStrategy
  property_count: 0
  slug: brevo-loyalty-tier-programs-pid-tier-groups-gid-put-request-body-content-application-json-schema-downgrade-strategy
- name: LoyaltyTierProgramsPidTierGroupsPostRequestBodyContentApplicationJsonSchemaDowngradeSchedule
  property_count: 4
  slug: brevo-loyalty-tier-programs-pid-tier-groups-post-request-body-content-application-json-schema-downgrade-schedule
- name: LoyaltyTierProgramsPidTierGroupsPostRequestBodyContentApplicationJsonSchemaUpgradeSchedule
  property_count: 4
  slug: brevo-loyalty-tier-programs-pid-tier-groups-post-request-body-content-application-json-schema-upgrade-schedule
- name: Master account_getCorporateUserPermission_Response_200
  property_count: 4
  slug: brevo-master-account-get-corporate-user-permission-response-200
- name: Master account_getSubAccountDetails_Response_200
  property_count: 5
  slug: brevo-master-account-get-sub-account-details-response-200
- name: Master account_getTheDetailsOfRequestedMasterAccount_Response_200
  property_count: 7
  slug: brevo-master-account-get-the-details-of-requested-master-account-response-200
- name: MessageResponse
  property_count: 7
  slug: brevo-message-response
- name: MessageResponse
  property_count: 7
  slug: brevo-messageresponse
- name: NoteData
  property_count: 4
  slug: brevo-note-data
- name: Note
  property_count: 8
  slug: brevo-note
- name: Notes_createANote_Response_200
  property_count: 1
  slug: brevo-notes-create-anote-response-200
- name: notification
  property_count: 2
  slug: brevo-notification
- name: ObjectsObjectTypeBatchDeletePostRequestBodyContentApplicationJsonSchemaIdentifiers
  property_count: 0
  slug: brevo-objects-object-type-batch-delete-post-request-body-content-application-json-schema-identifiers
- name: ObjectsObjectTypeBatchUpsertPostRequestBodyContentApplicationJsonSchemaRecordsItems
  property_count: 0
  slug: brevo-objects-object-type-batch-upsert-post-request-body-content-application-json-schema-records-items
- name: OrderList
  property_count: 1
  slug: brevo-order-list
- name: Brevo eCommerce Order
  property_count: 8
  slug: brevo-order
- name: OrderList
  property_count: 1
  slug: brevo-orderlist
- name: OrderProduct
  property_count: 4
  slug: brevo-orderproduct
- name: Payments_createPaymentRequest_Response_201
  property_count: 2
  slug: brevo-payments-create-payment-request-response-201
- name: Payments_getPaymentRequest_Response_200
  property_count: 7
  slug: brevo-payments-get-payment-request-response-200
- name: Pipeline
  property_count: 3
  slug: brevo-pipeline
- name: Process_getProcess_Response_200
  property_count: 5
  slug: brevo-process-get-process-response-200
- name: Process_getProcesses_Response_200
  property_count: 2
  slug: brevo-process-get-processes-response-200
- name: ProductList
  property_count: 2
  slug: brevo-product-list
- name: Product
  property_count: 10
  slug: brevo-product
- name: ProductList
  property_count: 2
  slug: brevo-productlist
- name: ProductsBatchPostRequestBodyContentApplicationJsonSchemaProductsItems
  property_count: 15
  slug: brevo-products-batch-post-request-body-content-application-json-schema-products-items
- name: redeem
  property_count: 14
  slug: brevo-redeem
- name: Reward_createReward_Response_200
  property_count: 8
  slug: brevo-reward-create-reward-response-200
- name: Reward_createVoucher_Response_200
  property_count: 12
  slug: brevo-reward-create-voucher-response-200
- name: Reward_getRewardInformation_Response_200
  property_count: 40
  slug: brevo-reward-get-reward-information-response-200
- name: Reward_getVoucherForAContact_Response_200
  property_count: 5
  slug: brevo-reward-get-voucher-for-acontact-response-200
- name: SendMessage
  property_count: 4
  slug: brevo-send-message
- name: sendReport
  property_count: 2
  slug: brevo-send-report
- name: SendSmsResponse
  property_count: 5
  slug: brevo-send-sms-response
- name: sendTransacSms
  property_count: 10
  slug: brevo-send-transac-sms
- name: SendTransactionalEmail
  property_count: 14
  slug: brevo-send-transactional-email
- name: SendTransactionalSms
  property_count: 6
  slug: brevo-send-transactional-sms
- name: SendWhatsAppMessage
  property_count: 3
  slug: brevo-send-whats-app-message
- name: SendWhatsAppResponse
  property_count: 1
  slug: brevo-send-whats-app-response
- name: SendEmailResponse
  property_count: 1
  slug: brevo-sendemailresponse
- name: SenderList
  property_count: 1
  slug: brevo-senderlist
- name: Senders_createSender_Response_201
  property_count: 3
  slug: brevo-senders-create-sender-response-201
- name: Senders_getIpsFromSender_Response_200
  property_count: 1
  slug: brevo-senders-get-ips-from-sender-response-200
- name: Senders_getIps_Response_200
  property_count: 1
  slug: brevo-senders-get-ips-response-200
- name: Senders_getSenders_Response_200
  property_count: 1
  slug: brevo-senders-get-senders-response-200
- name: SendersPostRequestBodyContentApplicationJsonSchemaIpsItems
  property_count: 3
  slug: brevo-senders-post-request-body-content-application-json-schema-ips-items
- name: SendersSenderIdPutRequestBodyContentApplicationJsonSchemaIpsItems
  property_count: 3
  slug: brevo-senders-sender-id-put-request-body-content-application-json-schema-ips-items
- name: SendMessage
  property_count: 4
  slug: brevo-sendmessage
- name: SendSmsResponse
  property_count: 5
  slug: brevo-sendsmsresponse
- name: SendTransactionalEmail
  property_count: 14
  slug: brevo-sendtransactionalemail
- name: SendTransactionalSms
  property_count: 6
  slug: brevo-sendtransactionalsms
- name: SendWhatsAppMessage
  property_count: 3
  slug: brevo-sendwhatsappmessage
- name: SendWhatsAppResponse
  property_count: 1
  slug: brevo-sendwhatsappresponse
- name: SmsCampaignsCampaignIdExportRecipientsPostRequestBodyContentApplicationJsonSchemaRecipientsType
  property_count: 0
  slug: brevo-sms-campaigns-campaign-id-export-recipients-post-request-body-content-application-json-schema-recipients-type
- name: SmsCampaignsCampaignIdPutRequestBodyContentApplicationJsonSchemaRecipients
  property_count: 2
  slug: brevo-sms-campaigns-campaign-id-put-request-body-content-application-json-schema-recipients
- name: SMS Campaigns_getSmsCampaign_Response_200
  property_count: 14
  slug: brevo-sms-campaigns-get-sms-campaign-response-200
- name: SMS Campaigns_getSmsCampaigns_Response_200
  property_count: 2
  slug: brevo-sms-campaigns-get-sms-campaigns-response-200
- name: SmsCampaignsPostRequestBodyContentApplicationJsonSchemaRecipients
  property_count: 2
  slug: brevo-sms-campaigns-post-request-body-content-application-json-schema-recipients
- name: SmsEventReport
  property_count: 1
  slug: brevo-sms-event-report
- name: SmsStatisticsReport
  property_count: 1
  slug: brevo-sms-statistics-report
- name: SmsEventReport
  property_count: 1
  slug: brevo-smseventreport
- name: SmsStatisticsReport
  property_count: 1
  slug: brevo-smsstatisticsreport
- name: SmtpTemplate
  property_count: 9
  slug: brevo-smtp-template
- name: SmtpTemplatesPostRequestBodyContentApplicationJsonSchemaSender
  property_count: 3
  slug: brevo-smtp-templates-post-request-body-content-application-json-schema-sender
- name: SmtpTemplatesTemplateIdPutRequestBodyContentApplicationJsonSchemaSender
  property_count: 3
  slug: brevo-smtp-templates-template-id-put-request-body-content-application-json-schema-sender
- name: SmtpTemplate
  property_count: 9
  slug: brevo-smtptemplate
- name: TaskReminder
  property_count: 3
  slug: brevo-task-reminder
- name: Task
  property_count: 12
  slug: brevo-task
- name: Tasks_createATask_Response_201
  property_count: 1
  slug: brevo-tasks-create-atask-response-201
- name: Tasks_getAllTasks_Response_200
  property_count: 1
  slug: brevo-tasks-get-all-tasks-response-200
- name: TemplateList
  property_count: 2
  slug: brevo-template-list
- name: TemplateList
  property_count: 2
  slug: brevo-templatelist
- name: Tier_addSubscriptionToTier_Response_200
  property_count: 7
  slug: brevo-tier-add-subscription-to-tier-response-200
- name: tierGroup
  property_count: 10
  slug: brevo-tier-group
- name: tier
  property_count: 9
  slug: brevo-tier
- name: transaction
  property_count: 16
  slug: brevo-transaction
- name: Transactional emails_getAggregatedSmtpReport_Response_200
  property_count: 13
  slug: brevo-transactional-emails-get-aggregated-smtp-report-response-200
- name: Transactional emails_getTransacEmailContent_Response_200
  property_count: 7
  slug: brevo-transactional-emails-get-transac-email-content-response-200
- name: Transactional SMS_getSmsEvents_Response_200
  property_count: 1
  slug: brevo-transactional-sms-get-sms-events-response-200
- name: Transactional SMS_getTransacAggregatedSmsReport_Response_200
  property_count: 11
  slug: brevo-transactional-sms-get-transac-aggregated-sms-report-response-200
- name: Transactional SMS_getTransacSmsReport_Response_200
  property_count: 1
  slug: brevo-transactional-sms-get-transac-sms-report-response-200
- name: Transactional WhatsApp_getWhatsappEventReport_Response_200
  property_count: 1
  slug: brevo-transactional-whats-app-get-whatsapp-event-report-response-200
- name: Transactional WhatsApp_sendWhatsappMessage_Request
  property_count: 0
  slug: brevo-transactional-whats-app-send-whatsapp-message-request
- name: Transactional WhatsApp_sendWhatsappMessage_Response_201
  property_count: 1
  slug: brevo-transactional-whats-app-send-whatsapp-message-response-201
- name: TransactionalEmailContent
  property_count: 5
  slug: brevo-transactionalemailcontent
- name: UpdateAutomatedMessage
  property_count: 1
  slug: brevo-update-automated-message
- name: UpdateConsentGroupRequest
  property_count: 3
  slug: brevo-update-consent-group-request
- name: UpdateSmtpTemplate
  property_count: 6
  slug: brevo-update-smtp-template
- name: UpdateWhatsAppCampaign
  property_count: 4
  slug: brevo-update-whats-app-campaign
- name: UpdateAutomatedMessage
  property_count: 1
  slug: brevo-updateautomatedmessage
- name: UpdateContact
  property_count: 5
  slug: brevo-updatecontact
- name: UpdateContactList
  property_count: 2
  slug: brevo-updatecontactlist
- name: UpdateEmailCampaign
  property_count: 6
  slug: brevo-updateemailcampaign
- name: UpdateSmtpTemplate
  property_count: 6
  slug: brevo-updatesmtptemplate
- name: UpdateWebhook
  property_count: 4
  slug: brevo-updatewebhook
- name: UpdateWhatsAppCampaign
  property_count: 4
  slug: brevo-updatewhatsappcampaign
- name: User_EditUserPermission_Response_200
  property_count: 3
  slug: brevo-user-edit-user-permission-response-200
- name: User_getInvitedUsersList_Response_200
  property_count: 1
  slug: brevo-user-get-invited-users-list-response-200
- name: User_getUserPermission_Response_200
  property_count: 3
  slug: brevo-user-get-user-permission-response-200
- name: User_putRevokeUserPermission_Response_200
  property_count: 2
  slug: brevo-user-put-revoke-user-permission-response-200
- name: User_putresendcancelinvitation_Response_200
  property_count: 2
  slug: brevo-user-putresendcancelinvitation-response-200
- name: walletPassInstallUrl
  property_count: 1
  slug: brevo-wallet-pass-install-url
- name: Webhook
  property_count: 8
  slug: brevo-webhook
- name: WebhookList
  property_count: 1
  slug: brevo-webhooklist
- name: WebhooksPostRequestBodyContentApplicationJsonSchemaAuth
  property_count: 2
  slug: brevo-webhooks-post-request-body-content-application-json-schema-auth
- name: WebhooksPostRequestBodyContentApplicationJsonSchemaEventsItems
  property_count: 0
  slug: brevo-webhooks-post-request-body-content-application-json-schema-events-items
- name: WebhooksWebhookIdPutRequestBodyContentApplicationJsonSchemaAuth
  property_count: 2
  slug: brevo-webhooks-webhook-id-put-request-body-content-application-json-schema-auth
- name: WebhooksWebhookIdPutRequestBodyContentApplicationJsonSchemaEventsItems
  property_count: 0
  slug: brevo-webhooks-webhook-id-put-request-body-content-application-json-schema-events-items
- name: WebhooksWebhookIdPutRequestBodyContentApplicationJsonSchemaHeadersItems
  property_count: 2
  slug: brevo-webhooks-webhook-id-put-request-body-content-application-json-schema-headers-items
- name: WhatsAppCampaignList
  property_count: 2
  slug: brevo-whats-app-campaign-list
- name: WhatsAppCampaign
  property_count: 9
  slug: brevo-whats-app-campaign
- name: WhatsApp Campaigns_getWhatsAppConfig_Response_200
  property_count: 6
  slug: brevo-whats-app-campaigns-get-whats-app-config-response-200
- name: WhatsApp Campaigns_getWhatsAppTemplates_Response_200
  property_count: 2
  slug: brevo-whats-app-campaigns-get-whats-app-templates-response-200
- name: WhatsAppTemplateList
  property_count: 2
  slug: brevo-whats-app-template-list
- name: WhatsAppCampaign
  property_count: 9
  slug: brevo-whatsappcampaign
- name: WhatsAppCampaignList
  property_count: 2
  slug: brevo-whatsappcampaignlist
- name: WhatsAppTemplateList
  property_count: 2
  slug: brevo-whatsapptemplatelist
json_structures:
- name: Brevo Structure
  property_count: 0
  slug: brevo-structure
jsonld:
- class_count: 0
  name: Brevo Context
  property_count: 10
  slug: brevo-context
layout: provider
mcp_servers:
- description: Brevo ships a hosted, remote MCP server at https://mcp.brevo.com. An agent POSTs directly to the endpoint with a Bearer MCP token minted in the Brevo dashboard (Account > SMTP & API > API Keys, with t
  name: Brevo MCP Server
  slug: brevo
modified: '2026-08-13'
name: Brevo
nav: Providers
network: true
overview: 'Brevo publishes 44 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Status API, Automated Messages API, Categories API, and 41 more. Tagged areas include Marketing, Marketing Automation, Email Marketing, Transactional Email, and SMS Marketing.


  The Brevo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Brevo''s developer surface includes authentication, CLI, changelog, sandbox, documentation, API reference, getting-started guide, and 72 more developer resources.'
plans:
- name: Brevo Plans Pricing
  plan_count: 5
  slug: brevo-plans-pricing
- name: Brevo Price Estimates
  plan_count: 0
  slug: brevo-price-estimates
random_paper: 14
rate_limits:
- limit_count: 30
  name: Brevo Rate Limits
  slug: brevo-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Brevo — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: brevo-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Brevo — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: brevo-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Brevo API Rules
  rule_count: 15
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 5
  slug: brevo-rules
scopes:
- name: Brevo Scopes
  scope_count: 37
  slug: brevo-scopes
  summary_line: 37 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 82.2
  coverage:
    artifact_dirs: 42
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 93.4
    contract_governance: 22.0
    contract_quality: 72.0
    developer_ergonomics: 82.7
    discoverability: 81.7
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 82.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/brevo/brevo-2026-06-20T173653.png
security:
- kind: authentication
  name: Brevo Authentication
  slug: brevo-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Brevo Domain Security
  slug: brevo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brevo Vulnerability Disclosure
  slug: brevo-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Brevo Trust Center
  slug: brevo-trust-center
  summary_line: ISO/IEC 27001:2022
skill_count: 4
skills:
- name: brevo-create-and-send-email-campaign
  slug: brevo-create-and-send-email-campaign
- name: brevo-run-a-loyalty-program
  slug: brevo-run-a-loyalty-program
- name: brevo-send-transactional-email
  slug: brevo-send-transactional-email
- name: brevo-sync-contacts-and-lists
  slug: brevo-sync-contacts-and-lists
slug: brevo
tags:
- Marketing
- Marketing Automation
- Email Marketing
- Transactional Email
- SMS Marketing
- WhatsApp
- Campaigns
- CRM
- Sales
- E-Commerce
- Loyalty
- Event
- Live Chat
- Email
- SMS
- Automation
- Messaging
- Contacts
website: https://www.brevo.com/
---
