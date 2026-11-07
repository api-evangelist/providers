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
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 64.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 136
  human_in_the_loop: 2
  name: Drippay Agentic Access
  operation_count: 245
  slug: drippay-agentic-access
  summary_line: 245 operations · 136 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Business-level settings and configuration.
  name: Drippay Business API
  phrasing_intents:
  - id: getBusinessSettings
    intent: Get business billing settings
    question: What default reporting currency is my business set to?
  - id: updateBusinessSettings
    intent: Change the default reporting currency
    question: How do I change the currency my business reports in by default?
  phrasing_ops: 2
  slug: drippay-business-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: View charge history and settlement status.
  name: Drippay Charges API
  phrasing_intents:
  - id: listCharges
    intent: List charges
    question: What charges have been made against a specific customer?
  - id: getCharge
    intent: Get a charge
    question: What are the details of one particular charge?
  - id: exportCharges
    intent: Export all charges as JSON or CSV
    question: How do I download all my charges into a spreadsheet?
  - id: refundCharge
    intent: Refund a charge to the customer
    question: How do I refund a charge that was made in error?
  - id: estimateCostsFromUsage
    intent: Estimate costs from existing usage
    question: What would last month's usage have cost under different pricing?
  - id: estimateCostsFromHypothetical
    intent: Estimate costs for hypothetical usage
    question: How much would a given quantity of API calls cost before they happen?
  phrasing_ops: 6
  slug: drippay-charges-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Per-customer commercial agreements with custom pricing, prepaid commits, and spend caps. All contract endpoints require a secret key (`sk_*`) with the `ADMIN` role.
  name: Drippay Contracts API
  phrasing_intents:
  - id: createContract
    intent: Create a per-customer contract
    question: How do I set up an enterprise deal with a prepaid commit for a customer?
  - id: listContracts
    intent: List customer contracts
    question: Which contracts does a particular customer have with us?
  - id: getContract
    intent: Get a contract with balance and overrides
    question: How much prepaid balance is left on a customer's contract?
  - id: amendContract
    intent: Amend an active contract's terms
    question: How do I extend the end date on an existing contract?
  - id: cancelContract
    intent: Cancel a contract permanently
    question: Can a cancelled contract ever be reactivated?
  - id: addContractPriceOverride
    intent: Add a negotiated price override to a contract
    question: How do I give one customer a lower per-unit rate than the default plan?
  - id: removeContractPriceOverride
    intent: Remove a price override from a contract
    question: How do I put a customer back on the default rate for one usage type?
  phrasing_ops: 7
  slug: drippay-contracts-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Coupons and promotion codes for discounts.
  name: Drippay Coupons API
  phrasing_intents:
  - id: createCoupon
    intent: Create a coupon
    question: How do I set up a new discount coupon?
  - id: listCoupons
    intent: List coupons
    question: Which discount coupons have I created?
  - id: getCoupon
    intent: Get a coupon
    question: What discount does a specific coupon give, and how often has it been redeemed?
  - id: deactivateCoupon
    intent: Deactivate a coupon
    question: How do I switch off a coupon so nobody can use it anymore?
  - id: createPromotionCode
    intent: Create a promotion code
    question: How do I give customers a code they can type in to get a coupon's discount?
  - id: listPromotionCodes
    intent: List promotion codes
    question: Which customer-facing promo codes exist right now?
  - id: redeemPromotionCode
    intent: Redeem a promotion code against an amount
    question: How do I apply a promo code to a charge and get the discounted net amount?
  phrasing_ops: 7
  slug: drippay-coupons-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Create, issue, and void credit notes.
  name: Drippay Credit Notes API
  phrasing_intents:
  - id: createCreditNote
    intent: Create a draft credit note on an invoice
    question: How do I correct an invoice that was already issued without voiding it?
  - id: listCreditNotes
    intent: List credit notes
    question: Which credit notes have been created against my invoices?
  - id: getCreditNote
    intent: Get a credit note
    question: What is the status of one specific credit note?
  - id: issueCreditNote
    intent: Issue a draft credit note to its invoice
    question: How do I apply a draft credit note to its invoice?
  - id: voidCreditNote
    intent: Void a credit note
    question: Can I reverse a credit note that was already issued?
  phrasing_ops: 5
  slug: drippay-credit-notes-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Self-service customer portal for profile, subscriptions, and address management.
  name: Drippay Customer Portal API
  phrasing_intents:
  - id: getPortalProfile
    intent: Get my customer profile in the portal
    question: What profile details does the customer portal have on file for me?
  - id: updatePortalProfileAddress
    intent: Update my billing address
    question: How do I change the billing address on my account?
  - id: listPortalSubscriptions
    intent: List my subscriptions in the portal
    question: Which subscriptions am I currently signed up for?
  - id: cancelPortalSubscription
    intent: Cancel one of my subscriptions
    question: How do I cancel my subscription myself?
  phrasing_ops: 4
  slug: drippay-customer-portal-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Create and manage billable customers.
  name: Drippay Customers API
  phrasing_intents:
  - id: createCustomer
    intent: Create a customer
    question: What's the minimum I need to send to register a new billing customer?
  - id: listCustomers
    intent: List customers
    question: How do I list all the customers on my Drip business account?
  - id: getCustomer
    intent: Get a customer
    question: Can I look up a single customer's record by their Drip ID?
  - id: updateCustomer
    intent: Update a customer
    question: Can I change the details on an existing customer?
  - id: getCustomerBillingHistory
    intent: View a customer's billing-field change history
    question: Can I see every past version of a customer's billing name and email?
  - id: getCustomerRevOpsSummary
    intent: Get a customer's RevOps summary
    question: What is a customer's lifetime revenue and gross margin?
  - id: syncCustomerBalance
    intent: Refresh a customer's on-chain balance
    question: A customer just deposited funds on-chain — how do I get the new balance picked up right away?
  - id: provisionSmartAccount
    intent: Provision a customer's smart account
    question: How do I deploy an ERC-4337 smart account for a customer?
  phrasing_ops: 17
  slug: drippay-customers-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: The Drift API from Drippay — 6 operation(s) for drift.
  name: Drippay Drift API
  phrasing_intents:
  - id: listStripeDriftFindings
    intent: List Stripe drift findings
    question: Where has my billing data drifted out of sync with Stripe?
  - id: listCustomerDriftFindings
    intent: List customer churn-risk findings
    question: Which customers are showing signs of churn risk?
  - id: listConfigDriftFindings
    intent: List configuration drift findings
    question: Has my billing configuration drifted from what it should be?
  - id: getDriftSummary
    intent: Summarize drift findings by kind
    question: How many drift findings do I have of each kind?
  - id: getDriftFinding
    intent: Get a single drift finding
    question: What are the details of one particular drift finding?
  - id: updateDriftFinding
    intent: Acknowledge, resolve or suppress a finding
    question: How do I mark a drift finding as resolved?
  - id: runDriftDetector
    intent: Run a drift detector on demand
    question: Can I trigger a drift check right now instead of waiting for the schedule?
  phrasing_ops: 7
  slug: drippay-drift-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Automatic retry + dunning email flow for failed payments. Configure a per-business retry schedule, list failed charges in collections, and manually re-trigger retries.
  name: Drippay Dunning API
  phrasing_intents:
  - id: getDunningSchedule
    intent: Get the dunning retry schedule
    question: How often are failed payments retried for my business?
  - id: upsertDunningSchedule
    intent: Set the dunning retry schedule
    question: Can I choose on which days after a failure payments are retried?
  - id: listCollections
    intent: List failed payments in collections
    question: Which failed payments are currently being retried?
  - id: getCollection
    intent: Get one failed payment's detail
    question: What's the retry history for one failed payment?
  - id: retryCollection
    intent: Manually retry a failed payment
    question: Can I retry a failed payment now instead of waiting for the schedule?
  phrasing_ops: 5
  slug: drippay-dunning-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Quota management and pre-request access checks.
  name: Drippay Entitlements API
  phrasing_intents:
  - id: listEntitlementPlans
    intent: List entitlement plans
    question: Which entitlement tiers have I set up for my product?
  - id: createEntitlementPlan
    intent: Create an entitlement plan
    question: How do I set up a new feature tier like Free or Pro?
  - id: getEntitlementPlan
    intent: Get an entitlement plan
    question: What does one particular entitlement tier contain?
  - id: updateEntitlementPlan
    intent: Update an entitlement plan
    question: Can I rename a feature tier or change its description?
  - id: deleteEntitlementPlan
    intent: Deactivate an entitlement plan
    question: How do I retire a feature tier I no longer offer?
  - id: listEntitlementPlanVersions
    intent: List versions of an entitlement plan
    question: Can I see how a feature tier's rules changed over time?
  - id: createEntitlementRule
    intent: Add a feature limit rule to a plan
    question: How do I cap how many times a feature can be used per month on a tier?
  - id: listEntitlementRules
    intent: List the feature rules on a plan
    question: What feature limits are configured on a tier?
  phrasing_ops: 14
  slug: drippay-entitlements-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Record execution events for observability.
  name: Drippay Events API
  phrasing_intents:
  - id: getCustomerEvents
    intent: Get a customer's execution events
    question: What has one customer's agent been doing — can I see their events?
  - id: createEvent
    intent: Record an execution event
    question: How do I log what my agent did as an execution event?
  - id: listEvents
    intent: List execution events across the business
    question: Which events happened inside a specific agent run?
  - id: getEvent
    intent: Get an event's full details
    question: What were the outcome, hashes and billing info for one event?
  - id: getEventPayload
    intent: Get the stored payloads for an event
    question: Can I retrieve the raw input and output my agent sent for one event?
  - id: traceEvent
    intent: Trace an event's causality chain
    question: What chain of events led to this one, and what did it cause?
  - id: traceByCorrelationId
    intent: Trace events across runs by correlation ID
    question: How do I follow one request across multiple agent runs and services?
  - id: listEventPayloads
    intent: List events with payloads in flat rows
    question: Can I export events with their inputs and outputs inlined as flat rows for SQL?
  phrasing_ops: 8
  slug: drippay-events-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Manage billing, CRM, and marketplace integrations (Stripe, Xero, Salesforce).
  name: Drippay Integrations API
  phrasing_intents:
  - id: salesforceWebhook
    intent: Receive Salesforce change events
    question: Where does Salesforce Change Data Capture send signed change events for my integration?
  - id: listIntegrations
    intent: List marketplace and CRM integrations
    question: Which marketplace and CRM integrations are connected to my billing account?
  - id: createIntegration
    intent: Create a marketplace or CRM integration
    question: How do I connect AWS Marketplace metering to my usage billing?
  - id: getIntegration
    intent: Get a marketplace integration
    question: What is the configuration and status of one specific integration?
  - id: updateIntegration
    intent: Rotate secrets or toggle an integration
    question: How do I rotate the secrets on an existing marketplace integration?
  - id: deleteIntegration
    intent: Delete a marketplace or CRM integration
    question: Can I remove a marketplace integration I no longer use?
  - id: testIntegration
    intent: Test a marketplace integration connection
    question: Is my marketplace integration actually able to reach the provider?
  - id: submitIntegrationUsage
    intent: Submit a metered usage record to a marketplace
    question: How do I forward a usage record to a connected cloud marketplace?
  phrasing_ops: 82
  slug: drippay-integrations-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: The Internal API from Drippay — 1 operation(s) for internal.
  name: Drippay Internal API
  phrasing_intents:
  - id: desktopFeatureFlags
    intent: Get desktop feature-flag entitlements
    question: Which desktop app features are enabled for my account?
  phrasing_ops: 1
  slug: drippay-internal-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Generate, issue, and manage invoices. Supports usage-based and subscription-based billing periods.
  name: Drippay Invoices API
  phrasing_intents:
  - id: generateInvoice
    intent: Generate a draft invoice from usage charges
    question: How do I turn a customer's usage charges for a period into an invoice?
  - id: generateInvoiceFromSubscription
    intent: Generate a draft invoice for a subscription period
    question: Can I invoice a subscription for a partial period with proration?
  - id: listInvoices
    intent: List invoices
    question: Which invoices are still unpaid?
  - id: getInvoice
    intent: Get an invoice
    question: What line items and totals are on a specific invoice?
  - id: updateInvoice
    intent: Edit terms and notes on a draft invoice
    question: Can I add a PO number or change NET terms on an invoice before it's issued?
  - id: addInvoiceLineItem
    intent: Add a one-off line item to a draft invoice
    question: How do I add a setup fee or manual adjustment to an invoice?
  - id: issueInvoice
    intent: Issue a draft invoice
    question: How do I finalize a draft invoice so it's pending payment?
  - id: markInvoicePaid
    intent: Mark an invoice as paid
    question: Can I record a partial payment against an invoice?
  phrasing_ops: 13
  slug: drippay-invoices-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Define per-unit pricing for usage types. Creating, updating, and deleting plans requires a secret key (`sk_*`) with the `ADMIN` role.
  name: Drippay Pricing Plans API
  phrasing_intents:
  - id: listPricingPlans
    intent: List pricing plans
    question: What per-unit pricing plans have I set up?
  - id: createPricingPlan
    intent: Create a pricing plan for a usage type
    question: How do I set a per-unit price for a usage type like API calls or tokens?
  - id: getPricingPlan
    intent: Get a pricing plan
    question: What price and pricing model does one plan use?
  - id: updatePricingPlan
    intent: Update a pricing plan's price or status
    question: Can I change my unit price and have it apply to new charges straight away?
  - id: deletePricingPlan
    intent: Deactivate a pricing plan
    question: How do I stop a pricing plan from applying to new usage?
  - id: listPricingPlanVersions
    intent: List a pricing plan's version history
    question: What did a pricing plan cost in its earlier versions?
  - id: getPricingPlanByType
    intent: Look up the active price for a unit type
    question: What am I currently charging per unit for a given usage type?
  - id: reprovisionPricingPlanStripe
    intent: Retry Stripe provisioning for a pricing plan
    question: My plan's Stripe product and price didn't get created — can I retry that?
  phrasing_ops: 8
  slug: drippay-pricing-plans-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Controlled taxonomy for strict-products governance. Groups pricing plans into service-line categories for ARR rollups and revenue reporting.
  name: Drippay Product Categories API
  phrasing_intents:
  - id: listProductCategories
    intent: List product categories
    question: Which product categories exist in my taxonomy?
  - id: createProductCategory
    intent: Create a product category
    question: How do I add a new product category for revenue reporting?
  - id: updateProductCategory
    intent: Update a product category
    question: Can I change a product category's GL code or revenue class?
  - id: archiveProductCategory
    intent: Archive a product category
    question: How do I stop a product category from being attached to new pricing plans?
  phrasing_ops: 4
  slug: drippay-product-categories-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Start, update, and inspect agent runs.
  name: Drippay Runs API
  phrasing_intents:
  - id: startRun
    intent: Start tracking a new agent run
    question: How do I begin tracking an agent run for a customer's workflow?
  - id: listRuns
    intent: List agent runs with filters
    question: Which agent runs has a given customer had this week?
  - id: updateRun
    intent: Update a run's status or end it
    question: How do I mark an agent run as completed or failed?
  - id: getRun
    intent: Get a run's metadata and summary totals
    question: What are the summary totals for one specific agent run?
  - id: getRunTimelineV2
    intent: Get a run's full event timeline for debugging
    question: What exactly happened step by step during an agent run?
  - id: emitRunEvent
    intent: Emit a single event to a run (legacy)
    question: How do I send one usage event to a run through the legacy run-events endpoint?
  - id: batchEmitRunEvents
    intent: Emit a batch of events to runs (legacy)
    question: Can I send many run events in one request with the legacy batch endpoint?
  - id: recordRun
    intent: Record a complete run in one call
    question: Is there a single call that starts a run, adds its events and ends it?
  phrasing_ops: 8
  slug: drippay-runs-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Recurring billing and subscription lifecycle management.
  name: Drippay Subscriptions API
  phrasing_intents:
  - id: createSubscription
    intent: Create a recurring subscription
    question: How do I start charging a customer a recurring monthly fee in USDC?
  - id: listSubscriptions
    intent: List subscriptions
    question: Which subscriptions does a customer have?
  - id: getSubscription
    intent: Get a subscription
    question: What price and billing period is a subscription on?
  - id: updateSubscription
    intent: Update a subscription
    question: When does a subscription price change take effect?
  - id: cancelSubscription
    intent: Cancel a subscription
    question: Does cancelling a subscription stop it immediately or at period end?
  - id: pauseSubscription
    intent: Pause a subscription
    question: Can I pause a subscription so no charges are made for a while?
  - id: resumeSubscription
    intent: Resume a paused subscription
    question: How do I restart billing on a paused subscription?
  phrasing_ops: 7
  slug: drippay-subscriptions-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: 'Sales tax configuration: customer tax addresses, exemptions, business registrations, and jurisdiction rates. Requires a secret key with ADMIN role and full mode (`SIMPLE_MODE=false`).'
  name: Drippay Tax API
  phrasing_intents:
  - id: setCustomerAddress
    intent: Set a customer's billing address
    question: How do I save or replace a customer's billing address for tax purposes?
  - id: getCustomerAddress
    intent: Get a customer's billing address
    question: What billing address do I have on file for a customer?
  - id: removeCustomerAddress
    intent: Remove a customer's address
    question: Can I delete the stored address from a customer?
  - id: createCustomerTaxExemption
    intent: Add a tax exemption for a customer
    question: How do I mark a customer as tax exempt?
  - id: listCustomerTaxExemptions
    intent: List a customer's active tax exemptions
    question: Which tax exemptions are currently active for a customer?
  - id: removeCustomerTaxExemption
    intent: Deactivate a customer tax exemption
    question: How do I revoke a customer's tax exemption once it expires?
  - id: previewCustomerTax
    intent: Preview tax on a hypothetical charge
    question: How much tax would a customer pay on a given charge amount?
  - id: createTaxRegistration
    intent: Add a tax registration for the business
    question: How do I register my business to collect tax in a new jurisdiction?
  phrasing_ops: 12
  slug: drippay-tax-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Record metered usage. Creates charges when a pricing plan matches.
  name: Drippay Usage API
  phrasing_intents:
  - id: recordUsage
    intent: Record usage and charge immediately
    question: How do I bill a customer for usage and wait until the charge is settled on-chain?
  - id: listUsageEvents
    intent: List recent usage events and charges
    question: What usage has been recorded recently, with the charges it created?
  - id: recordUsageAsync
    intent: Record usage and charge in the background
    question: Can I record billable usage without waiting for the charge to settle?
  - id: recordInternalUsage
    intent: Track usage without billing
    question: How do I track internal team usage without charging anyone?
  - id: recordInternalUsageBatch
    intent: Track unbilled usage at high throughput
    question: What should I use to send over a million unbilled usage events a day?
  - id: getUsageQuota
    intent: Check this month's event usage against plan quota
    question: Have I exceeded my monthly event quota on Drip?
  phrasing_ops: 6
  slug: drippay-usage-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Manage webhook endpoints for real-time event notifications.
  name: Drippay Webhooks API
  phrasing_intents:
  - id: listWebhookEventTypes
    intent: List available webhook event types
    question: Which event types can I subscribe a webhook to?
  - id: createWebhook
    intent: Create a webhook endpoint
    question: How do I get real-time notifications when a charge succeeds?
  - id: listWebhooks
    intent: List webhooks
    question: Which webhook endpoints have I registered, and how are their deliveries doing?
  - id: getWebhook
    intent: Get a webhook
    question: What URL and events is a specific webhook configured with?
  - id: updateWebhook
    intent: Update a webhook
    question: Can I change the URL of an existing webhook?
  - id: deleteWebhook
    intent: Delete a webhook
    question: How do I permanently remove a webhook endpoint?
  - id: rotateWebhookSecret
    intent: Rotate a webhook's signing secret
    question: My webhook secret leaked — how do I generate a new one?
  - id: listWebhookDeliveries
    intent: List a webhook's delivery attempts
    question: Which recent deliveries to my webhook failed?
  phrasing_ops: 11
  slug: drippay-webhooks-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Define workflow templates for agent execution.
  name: Drippay Workflows API
  phrasing_intents:
  - id: createWorkflow
    intent: Create a workflow definition
    question: How do I define a new workflow so I can track agent runs against it?
  - id: listWorkflows
    intent: List workflows for the business
    question: Which workflows have I defined for tracking agent runs?
  - id: getWorkflow
    intent: Get a workflow with usage statistics
    question: What are the usage statistics for one of my workflows?
  - id: updateWorkflow
    intent: Update a workflow
    question: Can I change the name or description of an existing workflow?
  phrasing_ops: 4
  slug: drippay-workflows-api
- baseURL: https://api.drippay.dev
  baseurl_source: declared
  description: Evaluate and preview billable metrics.
  name: Drippay Billable Metrics API
  phrasing_intents:
  - id: listBillableMetrics
    intent: List billable metrics
    question: Which billable metrics have I defined?
  - id: createBillableMetric
    intent: Create a billable metric
    question: How do I define a metric that bills on several event types at once?
  - id: getBillableMetric
    intent: Get a billable metric
    question: What event types and aggregation does one metric use?
  - id: updateBillableMetric
    intent: Update a billable metric
    question: Can I change the definition of an existing billable metric?
  - id: deleteBillableMetric
    intent: Deactivate a billable metric
    question: What happens to historical charges if I delete a billable metric?
  - id: evaluateBillableMetric
    intent: Evaluate a saved metric over a period
    question: What value would a saved metric produce over a given billing period?
  - id: previewBillableMetricSql
    intent: Preview an unsaved metric SQL expression
    question: Can I test a SQL expression for a metric before I save it?
  phrasing_ops: 7
  slug: drippay-billable-metrics-api
artifact_total: 64
asyncapis:
- description: ''
  name: Drippay Webhooks
  slug: drippay-webhooks
collections:
- collection_type: open
  name: Drip BillableMetrics API
  slug: open-drippay-billablemetrics-api
- collection_type: open
  name: Drip BillableMetrics Business API
  slug: open-drippay-business-api
- collection_type: open
  name: Drip BillableMetrics Charges API
  slug: open-drippay-charges-api
- collection_type: open
  name: Drip BillableMetrics Contracts API
  slug: open-drippay-contracts-api
- collection_type: open
  name: Drip BillableMetrics Coupons API
  slug: open-drippay-coupons-api
- collection_type: open
  name: Drip BillableMetrics Credit Notes API
  slug: open-drippay-credit-notes-api
- collection_type: open
  name: Drip BillableMetrics Customer Portal API
  slug: open-drippay-customer-portal-api
- collection_type: open
  name: Drip BillableMetrics Customers API
  slug: open-drippay-customers-api
- collection_type: open
  name: Drip BillableMetrics Drift API
  slug: open-drippay-drift-api
- collection_type: open
  name: Drip BillableMetrics Dunning API
  slug: open-drippay-dunning-api
- collection_type: open
  name: Drip BillableMetrics Entitlements API
  slug: open-drippay-entitlements-api
- collection_type: open
  name: Drip BillableMetrics Events API
  slug: open-drippay-events-api
- collection_type: open
  name: Drip BillableMetrics Integrations API
  slug: open-drippay-integrations-api
- collection_type: open
  name: Drip BillableMetrics Internal API
  slug: open-drippay-internal-api
- collection_type: open
  name: Drip BillableMetrics Invoices API
  slug: open-drippay-invoices-api
- collection_type: open
  name: Drip BillableMetrics Pricing Plans API
  slug: open-drippay-pricing-plans-api
- collection_type: open
  name: Drip BillableMetrics Product Categories API
  slug: open-drippay-product-categories-api
- collection_type: open
  name: Drip BillableMetrics Runs API
  slug: open-drippay-runs-api
- collection_type: open
  name: Drip BillableMetrics Subscriptions API
  slug: open-drippay-subscriptions-api
- collection_type: open
  name: Drip BillableMetrics Tax API
  slug: open-drippay-tax-api
- collection_type: open
  name: Drip BillableMetrics Usage API
  slug: open-drippay-usage-api
- collection_type: open
  name: Drip BillableMetrics Webhooks API
  slug: open-drippay-webhooks-api
- collection_type: open
  name: Drip BillableMetrics Workflows API
  slug: open-drippay-workflows-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/drippay/overview
- group: other
  href: https://artifacts.apis.io/drippay/capabilities/drippay-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/drippay-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.dreach.ai/
- group: other
  href: https://artifacts.apis.io/drippay/overlays/drippay-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/drippay-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/drippay/security/drippay-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/drippay-trust-center.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dreach.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.usedrip.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.usedrip.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.usedrip.ai/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://dreach.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://dreach.ai/register
- group: start
  title: ''
  type: SignUp
  url: https://dreach.ai/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dreach.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dreach.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://dreach.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://dreach.ai/guides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DripYCx26
- group: operate
  title: ''
  type: StatusPage
  url: https://status.usedrip.ai/
- group: operate
  href: https://artifacts.apis.io/drippay/rate-limits/drippay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/drippay-rate-limits.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dreach.ai/security
- group: auth
  title: ''
  type: Security
  url: https://dreach.ai/security
- group: auth
  href: https://artifacts.apis.io/drippay/well-known/drippay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/drippay-security.txt
- group: agent
  href: https://artifacts.apis.io/drippay/well-known/drippay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drippay-well-known.yml
- group: auth
  href: https://artifacts.apis.io/drippay/security/drippay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/drippay-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/drippay/security/drippay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drippay-domain-security.yml
- group: build
  href: https://artifacts.apis.io/drippay/packages/drippay-packages.yml
  title: ''
  type: Packages
  url: packages/drippay-packages.yml
- group: build
  href: https://artifacts.apis.io/drippay/packages/drippay-packages.yml
  title: ''
  type: SDKs
  url: packages/drippay-packages.yml
- group: agent
  href: https://artifacts.apis.io/drippay/mcp/drippay-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/drippay-mcp.yml
- group: agent
  href: https://artifacts.apis.io/drippay/llms/drippay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drippay-llms.txt
- group: design
  href: https://artifacts.apis.io/drippay/lifecycle/drippay-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/drippay-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/drippay/changelog/drippay-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/drippay-changelog.yml
- group: start
  href: https://artifacts.apis.io/drippay/sandbox/drippay-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/drippay-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/drippay/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/drippay/skills/drippay-drip-published.md
  title: ''
  type: AgentSkill
  url: skills/drippay-drip-published.md
- group: other
  href: https://artifacts.apis.io/drippay/a2a/drippay-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/drippay-a2a.yml
- group: auth
  href: https://artifacts.apis.io/drippay/scopes/drippay-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/drippay-scopes.yml
- group: build
  href: https://artifacts.apis.io/drippay/cli/drippay-cli.yml
  title: ''
  type: CLI
  url: cli/drippay-cli.yml
- group: commercial
  href: https://artifacts.apis.io/drippay/plans/drippay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/drippay-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/drippay/mcp/drippay-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/drippay-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/drippay/authentication/drippay-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drippay-authentication.yml
- group: design
  href: https://artifacts.apis.io/drippay/conventions/drippay-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/drippay-conventions.yml
- group: design
  href: https://artifacts.apis.io/drippay/conventions/drippay-conventions.yml
  title: ''
  type: Conventions
  url: conventions/drippay-conventions.yml
- group: design
  href: https://artifacts.apis.io/drippay/errors/drippay-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drippay-problem-types.yml
- group: design
  href: https://artifacts.apis.io/drippay/data-model/drippay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/drippay-data-model.yml
- group: design
  href: https://artifacts.apis.io/drippay/asyncapi/drippay-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/drippay-webhooks.yml
- group: design
  href: https://artifacts.apis.io/drippay/conformance/drippay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drippay-conformance.yml
- group: agent
  href: https://artifacts.apis.io/drippay/agentic-access/drippay-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drippay-agentic-access.yml
created: '2026-07-17'
description: 'Drippay, Inc. is a Y Combinator company (YC P26) that operates two connected products. dreach — renamed from drip in 2026, with usedrip.ai now redirecting to dreach.ai — is a local-first Mac app for staffing, recruiting and executive search firms: an Opportunity Radar that watches hiring demand and leadership changes, drafts outreach in the user''s voice, follows up, and books meetings, with a hosted MCP server at mcp.drippay.dev exposing seven outbound tools to any HTTP MCP client over OAuth. The Drip API is a separate usage-based billing and execution-ledger platform for AI agents — a Stripe-like metering and monetization backend covering customers, subscriptions, pricing plans, billable metrics, usage events, invoices, credit notes, coupons, entitlements, charges, dunning, tax, contracts, drift detection and webhooks across 245 REST operations at api.drippay.dev. It ships official Node, Python and C++ SDKs and a drip-cli binary, an idempotencyKey contract, cursor pagination,
  role-scoped secret keys, an x402 payment-required flow for agent self-settlement, and a SOC 2 Type I posture monitored with Vanta.'
finops:
- has_sources: true
  method: derived
  name: Drippay Finops
  primary_unit: account
  service_category: ''
  slug: drippay-finops
  template: false
image: https://dreach.ai/favicon.ico
layout: provider
mcp_servers:
- description: Hosted MCP server that connects AI agents to drip's outbound sales automation — lead sourcing, contact enrichment, and personalized message drafting. Research and drafting run server-side; message sen
  name: Drippay MCP Server
  slug: dripos-cloud
modified: '2026-08-13'
name: Drippay
nav: Providers
network: true
overview: 'Drippay publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Business API, Charges API, Contracts API, and 20 more. Tagged areas include Company, Billing, Usage-Based Billing, Metering, and Monetization.


  The Drippay catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Drippay''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 40 more developer resources.'
plans:
- name: Drippay Plans Pricing
  plan_count: 4
  slug: drippay-plans-pricing
- name: Drippay Price Estimates
  plan_count: 0
  slug: drippay-price-estimates
random_paper: 17
rate_limits:
- limit_count: 0
  name: Drippay Rate Limits
  slug: drippay-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Drippay API Rules
  rule_count: 53
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 6
  slug: drippay-rules
scopes:
- name: Drippay Scopes
  scope_count: 2
  slug: drippay-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 76.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 61.6
    developer_ergonomics: 86.9
    discoverability: 75.0
    operational_transparency: 52.6
  previous_composite: 75.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 23
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 41.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/drippay/drippay-2026-07-25T212410.png
security:
- kind: authentication
  name: Drippay Authentication
  slug: drippay-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Drippay Domain Security
  slug: drippay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Drippay Vulnerability Disclosure
  slug: drippay-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Drippay Trust Center
  slug: drippay-trust-center
  summary_line: SOC 2
skill_count: 5
skills:
- name: Drip
  slug: drippay-drip-published
- name: Assign and check entitlements
  slug: drippay-entitlements
- name: Meter usage and bill a customer
  slug: drippay-meter-and-bill
- name: Create a plan and manage a subscription
  slug: drippay-subscription-lifecycle
- name: Register and verify webhooks
  slug: drippay-webhooks-setup
slug: drippay
tags:
- Company
- Billing
- Usage-Based Billing
- Metering
- Monetization
- Payments
- AI Agents
- Developer Tools
- Webhook
- MCP
- CRM
- Sales Automation
- Agentic Payments
- x402
- Staffing
- Recruiting
- Outbound Sales
- A2A
website: https://www.dreach.ai/
---
