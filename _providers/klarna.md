---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Klarna Agentic Access
  operation_count: 37
  slug: klarna-agentic-access
  summary_line: 37 operations · 19 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: Create and authorize Klarna payment sessions; create orders against authorizations.
  name: Klarna Payments API
  slug: klarna-payments-api-2
- description: 'Hosted Klarna Checkout (KCO), the checkout/v3 surface. Klarna divested the Klarna Checkout product and it now trades as Kustom; as of 2026-08-27 Klarna no longer publishes a dedicated Klarna Checkout '
  name: Klarna Checkout API
  slug: klarna-checkout-api-2
- description: Capture, refund, cancel and update orders post-authorization.
  name: Klarna Order Management API
  slug: klarna-order-management-api
- description: Persist a payment authorization as a customer token for repeat purchases.
  name: Klarna Customer Token API
  slug: klarna-customer-token-api-2
- description: Read merchant settlement reports and transactions.
  name: Klarna Settlements API
  slug: klarna-settlements-api
- baseURL: https://merchant.example.com
  baseurl_source: declared
  description: Outbound HTTP POST callbacks Klarna issues to merchant-hosted URLs for Payments authorization, HPP status updates, Checkout push, and pending-order risk decisions.
  name: Klarna Push Notifications
  slug: klarna-push-notifications
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Captures API from Klarna — 6 operation(s) for captures.
  name: Klarna Captures API
  phrasing_intents:
  - id: captureOrder
    intent: Capture an order's payment
    question: How do I capture payment on an order once I've shipped it?
  - id: getCaptures
    intent: List the captures on an order
    question: Which captures have already been taken against a Klarna order?
  - id: getCapture
    intent: Get the details of one capture
    question: What was included in a specific capture on an order?
  - id: extendDueDate
    intent: Extend a customer's payment due date
    question: Can I give a customer more days to pay for a captured purchase?
  - id: getOptionsForExtendDueDate
    intent: See due date extension options and fees
    question: What would it cost me as a merchant to extend a customer's due date?
  - id: appendShippingInfo
    intent: Add shipping details to a capture
    question: Can I add a tracking number to a capture I already made?
  - id: triggerSendOut
    intent: Resend a capture's customer communication
    question: A shopper lost their payment instructions, can I resend them for a capture?
  phrasing_ops: 7
  slug: klarna-captures-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Checkout API from Klarna — 3 operation(s) for checkout.
  name: Klarna Checkout API
  phrasing_intents:
  - id: createOrderMerchant
    intent: Create a checkout order
    question: How do I start a new Klarna Checkout order and get the checkout snippet to embed?
  - id: updateOrderMerchant
    intent: Update an in-progress checkout order
    question: Can I change the cart of a checkout order before the customer completes it?
  - id: readOrderMerchant
    intent: Get a checkout order
    question: How can I read back a checkout order while the customer is still checking out?
  - id: abortOrder
    intent: Abort a checkout order
    question: How do I abandon a checkout order the customer will never finish?
  phrasing_ops: 4
  slug: klarna-checkout-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Customer Token API from Klarna — 3 operation(s) for customer token.
  name: Klarna Customer Token API
  phrasing_intents:
  - id: readCustomerToken
    intent: Get a customer token's status and details
    question: Is a saved customer token still active, and what payment method is behind it?
  - id: createOrder
    intent: Charge a stored customer token with a new order
    question: How do I bill a returning subscriber using their saved Klarna token?
  - id: patchCustomerToken
    intent: Cancel a customer token
    question: How do I stop a saved customer token from being charged again?
  phrasing_ops: 3
  slug: klarna-customer-token-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Hpp API from Klarna — 3 operation(s) for hpp.
  name: Klarna Hpp API
  phrasing_intents:
  - id: createHppSession
    intent: Create a hosted payment page session
    question: How do I send shoppers to a Klarna-hosted payment page instead of embedding the widget?
  - id: getSessionById
    intent: Get a hosted payment page session
    question: Has the customer finished paying on the hosted payment page yet?
  - id: disableHppSession
    intent: Disable a hosted payment page session
    question: How do I shut down a hosted payment page link after the payment was cancelled?
  - id: distributeHppSession
    intent: Send a hosted payment page link to a customer
    question: Can I text or email the payment link to a customer instead of redirecting them?
  phrasing_ops: 4
  slug: klarna-hpp-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Merchant Urls.address Update API from Klarna — 1 operation(s) for merchant urls.address update.
  name: Klarna Merchant Urls.address Update API
  phrasing_intents:
  - id: updateAddress
    intent: Respond to a shopper's address change
    question: What does the address update callback send my store when a shopper edits their address?
  phrasing_ops: 1
  slug: klarna-merchant-urls-address-update-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Merchant Urls.country Change API from Klarna — 1 operation(s) for merchant urls.country change.
  name: Klarna Merchant Urls.country Change API
  phrasing_intents:
  - id: countryChange
    intent: Respond to a billing country change
    question: What happens in checkout when the customer switches their billing country?
  phrasing_ops: 1
  slug: klarna-merchant-urls-country-change-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Merchant Urls.shipping Option Update API from Klarna — 1 operation(s) for merchant urls.shipping option update.
  name: Klarna Merchant Urls.shipping Option Update API
  phrasing_intents:
  - id: updateShippingOption
    intent: Respond to a shipping option selection
    question: How do I add the shipping fee when a shopper picks a delivery option in checkout?
  phrasing_ops: 1
  slug: klarna-merchant-urls-shipping-option-update-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Merchant Urls.validation API from Klarna — 1 operation(s) for merchant urls.validation.
  name: Klarna Merchant Urls.validation API
  phrasing_intents:
  - id: validate
    intent: Validate an order before purchase completes
    question: Can my store reject a checkout order right before the customer completes it?
  phrasing_ops: 1
  slug: klarna-merchant-urls-validation-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Orders API from Klarna — 9 operation(s) for orders.
  name: Klarna Orders API
  phrasing_intents:
  - id: getOrder
    intent: Get an order's details
    question: How can I see the status, captures and remaining amount of a placed order?
  - id: acknowledgeOrder
    intent: Acknowledge a checkout order
    question: Do I need to confirm to Klarna that I received a new checkout order?
  - id: updateAuthorization
    intent: Change an order's amount and lines
    question: Can I raise or lower the authorized amount of an order before shipping?
  - id: updateConsumerDetails
    intent: Update an order's shipping address
    question: The customer moved, can I change the shipping address on their order?
  - id: extendAuthorizationTime
    intent: Extend an order's authorization time
    question: My order won't ship before the authorization expires, can I get more time?
  - id: updateMerchantReferences
    intent: Update an order's merchant references
    question: Can I change my internal order number stored on an order?
  - id: releaseRemainingAuthorization
    intent: Release an order's remaining authorization
    question: I shipped only part of an order, how can I free the rest of the authorized amount?
  - id: appendOrderShippingInfo
    intent: Add shipping details to an order
    question: Can I attach tracking info to the whole order rather than a single capture?
  phrasing_ops: 9
  slug: klarna-orders-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Payments API from Klarna — 5 operation(s) for payments.
  name: Klarna Payments API
  phrasing_intents:
  - id: createCreditSession
    intent: Start a payment session
    question: How do I start a Klarna Payments session and get a client token for the browser?
  - id: updateCreditSession
    intent: Update a payment session
    question: The shopper added an item to the cart, how do I update their payment session?
  - id: readCreditSession
    intent: Get a payment session
    question: What data has been collected so far in a payment session?
  - id: cancelAuthorization
    intent: Release an unused payment authorization
    question: What do I do with an authorization token I'm not going to turn into an order?
  - id: createOrder
    intent: Place an order from an authorization
    question: After a successful authorization, how do I turn it into an order?
  - id: purchaseToken
    intent: Save a customer token from an authorization
    question: How can I store a customer's payment method for future charges after they authorize?
  phrasing_ops: 6
  slug: klarna-payments-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Payouts API from Klarna — 3 operation(s) for payouts.
  name: Klarna Payouts API
  phrasing_intents:
  - id: getPayoutSummary
    intent: Summarize payouts per currency for a period
    question: How much has been paid out to me in each currency over a date range?
  - id: getPayout
    intent: Get a single payout
    question: What is in the payout with a given payment reference?
  - id: getPayouts
    intent: List payouts
    question: Which payouts have I received recently?
  phrasing_ops: 3
  slug: klarna-payouts-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Refunds API from Klarna — 2 operation(s) for refunds.
  name: Klarna Refunds API
  phrasing_intents:
  - id: refundOrder
    intent: Refund an order
    question: How do I refund a customer for a captured order?
  - id: get
    intent: Get a refund's details
    question: Can I check the amount and lines of a refund I already issued?
  phrasing_ops: 2
  slug: klarna-refunds-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Reports API from Klarna — 4 operation(s) for reports.
  name: Klarna Reports API
  phrasing_intents:
  - id: getPayoutReportWithTransactions
    intent: Download one payout's transactions as CSV
    question: Can I export every transaction in a single payout to a spreadsheet?
  - id: payout
    intent: Download one payout's summary as PDF
    question: Is there a printable PDF summary of a single settlement?
  - id: getPayoutsSummaryReportWithTransactions
    intent: Export all payout transactions for a period as CSV
    question: Can I export the transactions of all payouts between two dates as CSV?
  - id: payoutsSummary
    intent: Download a PDF summary of payouts for a period
    question: Can I get a PDF covering all payouts between two dates?
  phrasing_ops: 4
  slug: klarna-reports-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Transactions API from Klarna — 1 operation(s) for transactions.
  name: Klarna Transactions API
  phrasing_intents:
  - id: getTransactions
    intent: List settlement transactions
    question: Which transactions made up a particular payout?
  phrasing_ops: 1
  slug: klarna-transactions-api
- description: Klarna's agent-facing product protocol, exposing product and commerce data for AI agents to query. Registered 2026-09-04 from the same declined submission.
  name: Klarna Agentic Product Protocol (KAPP) API
  slug: klarna-agentic-product-protocol-kapp-api
- baseURL: https://api.klarna.com
  baseurl_source: declared
  description: The Merchant Card API from Klarna — 6 operation(s) for merchant card.
  name: Klarna Merchant Card API
  phrasing_intents:
  - id: createPromise
    intent: Create a virtual card promise for an order
    question: How do I request virtual credit cards to pay a supplier for an order?
  - id: readPromise
    intent: Get a virtual card promise
    question: Can I look up which cards were promised in a card promise?
  - id: settlePromise
    intent: Settle virtual cards for a completed order
    question: How do I get the actual virtual card numbers once an order is complete?
  - id: readSettlement
    intent: Get a virtual card settlement by id
    question: Can I retrieve an existing card settlement using its settlement id?
  - id: readSettlementByOrderId
    intent: Get the card settlement for an order
    question: If I only have the order id, can I find its virtual card settlement?
  - id: postcancelorder
    intent: Request cancellation of a virtual card order
    question: How do I cancel an order that has a virtual card settlement?
  - id: getcancelorder
    intent: Check a virtual card order cancellation
    question: Has my cancellation request for a virtual card order gone through yet?
  phrasing_ops: 7
  slug: klarna-merchant-card-api
artifact_total: 145
asyncapis:
- description: AsyncAPI 2.6 description of Klarna's outbound HTTP push surface — the set of server-to-server callbacks that Klarna issues to merchant-hosted endpoints when payment, checkout, and order lifecycle even
  name: Klarna Push Notifications
  slug: klarna-push-notifications-asyncapi
collections:
- collection_type: open
  name: Klarna HPP
  slug: open-hosted-payment-page-api
- collection_type: open
  name: Klarna HPP Captures API
  slug: open-klarna-captures-api
- collection_type: open
  name: Klarna HPP Captures Checkout API
  slug: open-klarna-checkout-api
- collection_type: open
  name: Klarna HPP Captures Customer Token API
  slug: open-klarna-customer-token-api
- collection_type: open
  name: Klarna Captures Hpp API
  slug: open-klarna-hpp-api
- collection_type: open
  name: Klarna HPP Captures Merchant Urls.address Update API
  slug: open-klarna-merchant-urls-address-update-api
- collection_type: open
  name: Klarna HPP Captures Merchant Urls.country Change API
  slug: open-klarna-merchant-urls-country-change-api
- collection_type: open
  name: Klarna HPP Captures Merchant Urls.shipping Option Update API
  slug: open-klarna-merchant-urls-shipping-option-update-api
- collection_type: open
  name: Klarna HPP Captures Merchant Urls.validation API
  slug: open-klarna-merchant-urls-validation-api
- collection_type: open
  name: Klarna HPP Captures Merchantcard API
  slug: open-klarna-merchantcard-api
- collection_type: open
  name: Klarna HPP Captures Orders API
  slug: open-klarna-orders-api
- collection_type: open
  name: Klarna HPP Captures Payments API
  slug: open-klarna-payments-api
- collection_type: open
  name: Klarna HPP Captures Payouts API
  slug: open-klarna-payouts-api
- collection_type: open
  name: Klarna HPP Captures Refunds API
  slug: open-klarna-refunds-api
- collection_type: open
  name: Klarna HPP Captures Reports API
  slug: open-klarna-reports-api
- collection_type: open
  name: Klarna Settlements API
  slug: open-klarna-settlements-api
- collection_type: open
  name: Klarna HPP Captures Transactions API
  slug: open-klarna-transactions-api
- collection_type: open
  name: Klarna Merchant Card Service API
  slug: open-merchant-card-service-api
- collection_type: open
  name: Klarna Order Management API
  slug: open-order-management-api
common:
- group: design
  href: https://artifacts.apis.io/klarna/rules/klarna-rules.yml
  title: ''
  type: Spectral
  url: rules/klarna-rules.yml
- group: design
  href: https://artifacts.apis.io/klarna/rules/klarna-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/klarna-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/klarna/rules/klarna-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/klarna-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/klarna/json-ld/klarna-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/klarna-context.jsonld
- group: design
  href: https://artifacts.apis.io/klarna/vocabulary/klarna-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/klarna-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/klarna/llms/klarna-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/klarna-llms.txt
- group: other
  href: https://artifacts.apis.io/klarna/hosts/klarna-hosts.yml
  title: ''
  type: Hosts
  url: hosts/klarna-hosts.yml
- group: build
  href: https://artifacts.apis.io/klarna/integrations/klarna-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/klarna-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/klarna/vendors/klarna-vendors.yml
  title: ''
  type: Vendors
  url: vendors/klarna-vendors.yml
- group: other
  href: https://artifacts.apis.io/klarna/overlays/klarna-merchantcard-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/klarna-merchantcard-overlay.yaml
- group: other
  href: https://artifacts.apis.io/klarna/capabilities/klarna-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/klarna-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.klarna.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.klarna.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.klarna.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.klarna.com/api/kn/introduction/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.klarna.com/acquirer/klarna/resources/developer-tools/testing-payments/before-you-test/
- group: operate
  title: ''
  type: Support
  url: https://www.klarna.com/us/help/
- group: company
  title: ''
  type: Blog
  url: https://www.klarna.com/international/press/category/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/klarna
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/klarna
- group: commercial
  title: ''
  type: Pricing
  url: https://x.klarnacdn.net/mepo/onboarding/pricing-annexes/pricing-annex-kp-CA-US-en-20230905.pdf
- group: start
  title: ''
  type: SignUp
  url: https://portal.playground.klarna.com/
- group: start
  title: ''
  type: Login
  url: https://portal.klarna.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klarna.com/us/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klarna.com/us/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.klarna.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.klarna.com/acquirer/klarna/resources/legal-and-compliance/policies-and-term-of-service/deprecation-policy/
- group: auth
  title: ''
  type: Security
  url: https://www.klarna.com/international/responsible-disclosure/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.klarna.com/llms.txt
- group: agent
  href: https://artifacts.apis.io/klarna/agentic-access/klarna-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/klarna-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/klarna/authentication/klarna-authentication.yml
  title: ''
  type: Authentication
  url: authentication/klarna-authentication.yml
- group: auth
  href: https://artifacts.apis.io/klarna/scopes/klarna-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/klarna-scopes.yml
- group: auth
  href: https://artifacts.apis.io/klarna/security/klarna-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/klarna-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/klarna/security/klarna-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/klarna-domain-security.yml
- group: build
  href: https://artifacts.apis.io/klarna/packages/klarna-packages.yml
  title: ''
  type: Packages
  url: packages/klarna-packages.yml
- group: build
  href: https://artifacts.apis.io/klarna/packages/klarna-packages.yml
  title: ''
  type: SDKs
  url: packages/klarna-packages.yml
- group: design
  href: https://artifacts.apis.io/klarna/conventions/klarna-conventions.yml
  title: ''
  type: Conventions
  url: conventions/klarna-conventions.yml
- group: design
  href: https://artifacts.apis.io/klarna/conventions/klarna-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/klarna-conventions.yml
- group: design
  href: https://artifacts.apis.io/klarna/errors/klarna-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/klarna-problem-types.yml
- group: design
  href: https://artifacts.apis.io/klarna/lifecycle/klarna-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/klarna-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/klarna/changelog/klarna-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/klarna-changelog.yml
- group: start
  href: https://artifacts.apis.io/klarna/sandbox/klarna-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/klarna-sandbox.yml
- group: design
  href: https://artifacts.apis.io/klarna/components/klarna-components.yml
  title: ''
  type: Components
  url: components/klarna-components.yml
- group: design
  href: https://artifacts.apis.io/klarna/data-model/klarna-data-model.yml
  title: ''
  type: DataModel
  url: data-model/klarna-data-model.yml
- group: design
  href: https://artifacts.apis.io/klarna/conformance/klarna-conformance.yml
  title: ''
  type: Conformance
  url: conformance/klarna-conformance.yml
- group: agent
  href: https://artifacts.apis.io/klarna/well-known/klarna-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/klarna-well-known.yml
- group: design
  href: https://artifacts.apis.io/klarna/asyncapi/klarna-push-notifications-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/klarna-push-notifications-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/klarna/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/klarna/plans/klarna-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/klarna-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/klarna/rate-limits/klarna-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/klarna-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/klarna/finops/klarna-finops.yml
  title: ''
  type: FinOps
  url: finops/klarna-finops.yml
created: '2026-05-08'
description: Klarna Bank AB is a Swedish licensed bank and payments network serving 150M+ consumers and 600k+ merchants with buy-now-pay-later, financing, cards, banking and a shopping app. For developers Klarna publishes a merchant API estate covering payment sessions and authorization (Klarna Payments), hosted checkout (Klarna Checkout and the Hosted Payment Page), post-purchase order management (capture, refund, cancel, extend due date), customer tokens for recurring purchases, settlement payouts and transaction reporting, the Merchant Card Service, and a PSD2 XS2A open-banking API for licensed TPPs. Authentication is HTTP Basic with a Klarna-issued API key; Sign in with Klarna adds a full OAuth 2.0 / OpenID Connect consumer-identity surface. Klarna publishes rate limits, a six-month deprecation policy, public service-level objectives, a self-serve playground with market-specific sample data, and an llms.txt — but no fetchable OpenAPI, no server-side SDK in any language, and no MCP server.
finops:
- has_sources: true
  method: derived
  name: Klarna Finops
  primary_unit: ''
  service_category: ''
  slug: klarna-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/klarna.png
json_schemas:
- name: Addon
  property_count: 4
  slug: klarna-addon
- name: Address
  property_count: 6
  slug: klarna-address
- name: BackgroundImageV1
  property_count: 2
  slug: klarna-backgroundimagev1
- name: Cancel not allowed error message
  property_count: 3
  slug: klarna-cancel-not-allowed-error-message
- name: cancel_order_request_status_cancelled
  property_count: 1
  slug: klarna-cancel-order-request-status-cancelled
- name: cancel_order_request_status_no_request_found
  property_count: 3
  slug: klarna-cancel-order-request-status-no-request-found
- name: cancel_order_request_status_pending
  property_count: 2
  slug: klarna-cancel-order-request-status-pending
- name: cancel_order_request_status
  property_count: 4
  slug: klarna-cancel-order-request-status
- name: Capture not allowed error message
  property_count: 3
  slug: klarna-capture-not-allowed-error-message
- name: CaptureObject
  property_count: 6
  slug: klarna-capture-object
- name: Capture
  property_count: 11
  slug: klarna-capture
- name: CaptureObject
  property_count: 6
  slug: klarna-captureobject
- name: card
  property_count: 9
  slug: klarna-card
- name: card_specification
  property_count: 4
  slug: klarna-card-specification
- name: CarrierProduct
  property_count: 2
  slug: klarna-carrierproduct
- name: create_order_request
  property_count: 18
  slug: klarna-create-order-request
- name: customer
  property_count: 2
  slug: klarna-customer
- name: customer_token_creation_response
  property_count: 5
  slug: klarna-customer-token-creation-response
- name: customer_token_order
  property_count: 12
  slug: klarna-customer-token-order
- name: customer_token
  property_count: 4
  slug: klarna-customer-token
- name: customer_token_status_update_request
  property_count: 1
  slug: klarna-customer-token-status-update-request
- name: CustomerV1
  property_count: 5
  slug: klarna-customerv1
- name: DistributionRequestV1
  property_count: 3
  slug: klarna-distribution-request-v1
- name: DistributionContactV1
  property_count: 4
  slug: klarna-distributioncontactv1
- name: DistributionModuleV1
  property_count: 3
  slug: klarna-distributionmodulev1
- name: DistributionRequestV1
  property_count: 3
  slug: klarna-distributionrequestv1
- name: ErrorMessageDto
  property_count: 3
  slug: klarna-errormessagedto
- name: ErrorResponse
  property_count: 3
  slug: klarna-errorresponse
- name: ExtendDueDateOptions
  property_count: 2
  slug: klarna-extend-due-date-options
- name: ExtendDueDateRequest
  property_count: 1
  slug: klarna-extend-due-date-request
- name: ExtendDueDateOptions
  property_count: 2
  slug: klarna-extendduedateoptions
- name: ExtendDueDateRequest
  property_count: 1
  slug: klarna-extendduedaterequest
- name: InitialPaymentMethodDto
  property_count: 3
  slug: klarna-initialpaymentmethoddto
- name: Location
  property_count: 4
  slug: klarna-location
- name: MerchantOrderDto
  property_count: 26
  slug: klarna-merchant-order-dto
- name: MerchantManualIdentificationV1
  property_count: 4
  slug: klarna-merchantmanualidentificationv1
- name: MerchantOrderDto
  property_count: 26
  slug: klarna-merchantorderdto
- name: MerchantUrlsV1
  property_count: 6
  slug: klarna-merchanturlsv1
- name: No such capture error message
  property_count: 3
  slug: klarna-no-such-capture-error-message
- name: No such order error message
  property_count: 3
  slug: klarna-no-such-order-error-message
- name: Not allowed error message
  property_count: 3
  slug: klarna-not-allowed-error-message
- name: Not found error message
  property_count: 3
  slug: klarna-not-found-error-message
- name: OptionDto
  property_count: 2
  slug: klarna-optiondto
- name: OptionsV1
  property_count: 8
  slug: klarna-optionsv1
- name: order_line
  property_count: 15
  slug: klarna-order-line
- name: order
  property_count: 35
  slug: klarna-order
- name: Pagination
  property_count: 5
  slug: klarna-pagination
- name: PayoutCollection
  property_count: 2
  slug: klarna-payout-collection
- name: Payout
  property_count: 8
  slug: klarna-payout
- name: PayoutSummary
  property_count: 14
  slug: klarna-payout-summary
- name: PayoutCollection
  property_count: 2
  slug: klarna-payoutcollection
- name: PayoutSummary
  property_count: 14
  slug: klarna-payoutsummary
- name: ProductIdentifiers
  property_count: 6
  slug: klarna-productidentifiers
- name: promise_created_response
  property_count: 2
  slug: klarna-promise-created-response
- name: promise_request
  property_count: 2
  slug: klarna-promise-request
- name: promise_response
  property_count: 5
  slug: klarna-promise-response
- name: Refund not allowed error message
  property_count: 3
  slug: klarna-refund-not-allowed-error-message
- name: RefundObject
  property_count: 4
  slug: klarna-refund-object
- name: Refund
  property_count: 7
  slug: klarna-refund
- name: RefundObject
  property_count: 4
  slug: klarna-refundobject
- name: SelectedShippingOptionDto
  property_count: 14
  slug: klarna-selectedshippingoptiondto
- name: session_create
  property_count: 24
  slug: klarna-session-create
- name: SessionCreationRequestV1
  property_count: 4
  slug: klarna-session-creation-request-v1
- name: SessionCreationResponseV1
  property_count: 8
  slug: klarna-session-creation-response-v1
- name: session_read
  property_count: 24
  slug: klarna-session-read
- name: SessionResponseV1
  property_count: 9
  slug: klarna-session-response-v1
- name: session
  property_count: 24
  slug: klarna-session
- name: SessionCreationRequestV1
  property_count: 4
  slug: klarna-sessioncreationrequestv1
- name: SessionCreationResponseV1
  property_count: 8
  slug: klarna-sessioncreationresponsev1
- name: SessionResponseV1
  property_count: 9
  slug: klarna-sessionresponsev1
- name: settlement_request
  property_count: 3
  slug: klarna-settlement-request
- name: settlement_response
  property_count: 6
  slug: klarna-settlement-response
- name: shipping_info
  property_count: 7
  slug: klarna-shipping-info
- name: shipping_service_response
  property_count: 10
  slug: klarna-shipping-service-response
- name: subscription
  property_count: 3
  slug: klarna-subscription
- name: Timeslot
  property_count: 5
  slug: klarna-timeslot
- name: Totals
  property_count: 18
  slug: klarna-totals
- name: TransactionCollection
  property_count: 2
  slug: klarna-transaction-collection
- name: Transaction
  property_count: 27
  slug: klarna-transaction
- name: TransactionCollection
  property_count: 2
  slug: klarna-transactioncollection
- name: Update authorization
  property_count: 3
  slug: klarna-update-authorization
- name: UpdateConsumer
  property_count: 1
  slug: klarna-update-consumer
- name: Update merchant references
  property_count: 2
  slug: klarna-update-merchant-references
- name: UpdateShippingInfo
  property_count: 1
  slug: klarna-update-shipping-info
- name: UpdateConsumer
  property_count: 1
  slug: klarna-updateconsumer
- name: UpdateShippingInfo
  property_count: 1
  slug: klarna-updateshippinginfo
jsonld:
- class_count: 94
  name: Klarna Context
  property_count: 262
  slug: klarna-context
layout: provider
modified: '2026-08-27'
name: Klarna
nav: Providers
network: true
overview: 'Klarna publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Push Notifications, Captures API, Checkout API, and 19 more. Tagged areas include Fintech, Buy Now Pay Later, Payments, Cards, and Shopping.


  The Klarna catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Klarna''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 44 more developer resources.'
plans:
- name: Klarna Plans Pricing
  plan_count: 1
  slug: klarna-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 14
  name: Klarna Rate Limits
  slug: klarna-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Klarna — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: klarna-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Klarna — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: klarna-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Klarna API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: klarna-rules
scopes:
- name: Klarna Scopes
  scope_count: 34
  slug: klarna-scopes
  summary_line: 34 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.6
  coverage:
    artifact_dirs: 38
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 59.2
    contract_governance: 35.6
    contract_quality: 66.9
    developer_ergonomics: 73.2
    discoverability: 78.6
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 73.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/klarna/klarna-2026-10-11T110137.png
security:
- kind: authentication
  name: Klarna Authentication
  slug: klarna-authentication
  summary_line: http/openIdConnect · 4 schemes
- kind: domain-security
  name: Klarna Domain Security
  slug: klarna-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Klarna Vulnerability Disclosure
  slug: klarna-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 5
skills:
- name: klarna-authorize-and-create-order
  slug: klarna-authorize-and-create-order
- name: klarna-capture-and-fulfil
  slug: klarna-capture-and-fulfil
- name: klarna-hosted-payment-page
  slug: klarna-hosted-payment-page
- name: klarna-recurring-with-customer-token
  slug: klarna-recurring-with-customer-token
- name: klarna-refund-and-reconcile
  slug: klarna-refund-and-reconcile
slug: klarna
tags:
- Fintech
- Buy Now Pay Later
- Payments
- Cards
- Shopping
- Banking
- Checkout
- Order Management
- Settlement
- Open Banking
- PSD2
- Consumer Credit
- Sweden
- Agentic Commerce
- Consumer Finance
website: https://www.klarna.com/
---
