---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.5
  scored_at: '2026-09-01'
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
  slug: klarna-payments-api
- description: 'Hosted Klarna Checkout (KCO), the checkout/v3 surface. Klarna divested the Klarna Checkout product and it now trades as Kustom; as of 2026-08-27 Klarna no longer publishes a dedicated Klarna Checkout '
  name: Klarna Checkout API
  slug: klarna-checkout-api
- description: Capture, refund, cancel and update orders post-authorization.
  name: Klarna Order Management API
  slug: klarna-order-management-api
- description: Persist a payment authorization as a customer token for repeat purchases.
  name: Klarna Customer Token API
  slug: klarna-customer-token-api
- description: Read merchant settlement reports and transactions.
  name: Klarna Settlements API
  slug: klarna-settlements-api
- description: Outbound HTTP POST callbacks Klarna issues to merchant-hosted URLs for Payments authorization, HPP status updates, Checkout push, and pending-order risk decisions.
  name: Klarna Push Notifications
  slug: klarna-push-notifications
- description: The Captures API from Klarna — 6 operation(s) for captures.
  name: Klarna Captures API
  slug: klarna-captures-api
- description: The Checkout API from Klarna — 3 operation(s) for checkout.
  name: Klarna Checkout API
  slug: klarna-checkout-api
- description: The Customer Token API from Klarna — 3 operation(s) for customer token.
  name: Klarna Customer Token API
  slug: klarna-customer-token-api
- description: The Hpp API from Klarna — 3 operation(s) for hpp.
  name: Klarna Hpp API
  slug: klarna-hpp-api
- description: The Merchant Urls.address Update API from Klarna — 1 operation(s) for merchant urls.address update.
  name: Klarna Merchant Urls.address Update API
  slug: klarna-merchant-urls-address-update-api
- description: The Merchant Urls.country Change API from Klarna — 1 operation(s) for merchant urls.country change.
  name: Klarna Merchant Urls.country Change API
  slug: klarna-merchant-urls-country-change-api
- description: The Merchant Urls.shipping Option Update API from Klarna — 1 operation(s) for merchant urls.shipping option update.
  name: Klarna Merchant Urls.shipping Option Update API
  slug: klarna-merchant-urls-shipping-option-update-api
- description: The Merchant Urls.validation API from Klarna — 1 operation(s) for merchant urls.validation.
  name: Klarna Merchant Urls.validation API
  slug: klarna-merchant-urls-validation-api
- description: The Merchantcard API from Klarna — 6 operation(s) for merchantcard.
  name: Klarna Merchantcard API
  slug: klarna-merchantcard-api
- description: The Orders API from Klarna — 9 operation(s) for orders.
  name: Klarna Orders API
  slug: klarna-orders-api
- description: The Payments API from Klarna — 5 operation(s) for payments.
  name: Klarna Payments API
  slug: klarna-payments-api
- description: The Payouts API from Klarna — 3 operation(s) for payouts.
  name: Klarna Payouts API
  slug: klarna-payouts-api
- description: The Refunds API from Klarna — 2 operation(s) for refunds.
  name: Klarna Refunds API
  slug: klarna-refunds-api
- description: The Reports API from Klarna — 4 operation(s) for reports.
  name: Klarna Reports API
  slug: klarna-reports-api
- description: The Transactions API from Klarna — 1 operation(s) for transactions.
  name: Klarna Transactions API
  slug: klarna-transactions-api
artifact_total: 115
asyncapis:
- description: AsyncAPI 2.6 description of Klarna's outbound HTTP push surface — the set of server-to-server callbacks that Klarna issues to merchant-hosted endpoints when payment, checkout, and order lifecycle even
  name: Klarna Push Notifications
  slug: klarna-push-notifications-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
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
  title: ''
  type: AgenticAccess
  url: agentic-access/klarna-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/klarna-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/klarna-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/klarna-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klarna-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/klarna-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/klarna-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klarna-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/klarna-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/klarna-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klarna-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/klarna-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/klarna-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/klarna-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/klarna-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klarna-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/klarna-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/klarna-push-notifications-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/klarna-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/klarna-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/klarna-finops.yml
created: '2026-05-08'
description: Klarna Bank AB is a Swedish licensed bank and payments network serving 150M+ consumers and 600k+ merchants with buy-now-pay-later, financing, cards, banking and a shopping app. For developers Klarna publishes a merchant API estate covering payment sessions and authorization (Klarna Payments), hosted checkout (Klarna Checkout and the Hosted Payment Page), post-purchase order management (capture, refund, cancel, extend due date), customer tokens for recurring purchases, settlement payouts and transaction reporting, the Merchant Card Service, and a PSD2 XS2A open-banking API for licensed TPPs. Authentication is HTTP Basic with a Klarna-issued API key; Sign in with Klarna adds a full OAuth 2.0 / OpenID Connect consumer-identity surface. Klarna publishes rate limits, a six-month deprecation policy, public service-level objectives, a self-serve playground with market-specific sample data, and an llms.txt — but no fetchable OpenAPI, no server-side SDK in any language, and no MCP server.
finops:
- name: Klarna Finops
  service_category: Fintech
  slug: klarna-finops
graphqls:
- description: '> **NOT PUBLISHED BY KLARNA.** Verified 2026-08-27: Klarna ships no GraphQL API. There is no'
  name: Klarna GraphQL Schema
  slug: klarna-graphql
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
- name: customer
  property_count: 2
  slug: klarna-customer
- name: CustomerV1
  property_count: 5
  slug: klarna-customerv1
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
- name: Pagination
  property_count: 5
  slug: klarna-pagination
- name: Payout
  property_count: 8
  slug: klarna-payout
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
- name: Refund
  property_count: 7
  slug: klarna-refund
- name: RefundObject
  property_count: 4
  slug: klarna-refundobject
- name: SelectedShippingOptionDto
  property_count: 14
  slug: klarna-selectedshippingoptiondto
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
- name: subscription
  property_count: 3
  slug: klarna-subscription
- name: Timeslot
  property_count: 5
  slug: klarna-timeslot
- name: Totals
  property_count: 18
  slug: klarna-totals
- name: Transaction
  property_count: 27
  slug: klarna-transaction
- name: TransactionCollection
  property_count: 2
  slug: klarna-transactioncollection
- name: Update authorization
  property_count: 3
  slug: klarna-update-authorization
- name: Update merchant references
  property_count: 2
  slug: klarna-update-merchant-references
- name: UpdateConsumer
  property_count: 1
  slug: klarna-updateconsumer
- name: UpdateShippingInfo
  property_count: 1
  slug: klarna-updateshippinginfo
layout: provider
modified: '2026-08-27'
name: Klarna
nav: Providers
network: true
overview: 'Klarna publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Payments API, Checkout API, Customer Token API, and 16 more. Tagged areas include Fintech, BNPL, Payments, Cards, and Shopping.


  The Klarna catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Klarna''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 34 more developer resources.'
plans:
- name: Klarna Plans Pricing
  plan_count: 1
  slug: klarna-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 14
  name: Klarna Rate Limits
  slug: klarna-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Klarna API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: klarna-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Klarna API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: klarna-jsonschema-spectral-rules
scopes:
- name: Klarna Scopes
  scope_count: 34
  slug: klarna-scopes
  summary_line: 34 scopes · authorizationCode
score:
  band: exemplar
  composite: 74.3
  coverage:
    artifact_dirs: 31
    catalog_gap: 47.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 5.0
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 31.8
    contract_quality: 60.6
    developer_ergonomics: 73.2
    discoverability: 81.5
    governance: 31.8
    operational_transparency: 92.1
  previous_composite: 69.3
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
    score: 78.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
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
slug: klarna
tags:
- Fintech
- BNPL
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
website: https://www.klarna.com/
---
