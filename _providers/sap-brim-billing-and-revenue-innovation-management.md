---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Sap Brim Billing And Revenue Innovation Management Agentic Access
  operation_count: 43
  slug: sap-brim-billing-and-revenue-innovation-management-agentic-access
  summary_line: 43 operations · 29 acting
api_count: 11
apis:
- description: API for managing subscription-based orders within the SAP BRIM suite, supporting complex offerings that combine physical products, services, and usage-based fees with full lifecycle management.
  name: SAP Subscription Order Management API
  slug: sap-subscription-order-management-api
- description: Account balance inquiries and adjustments
  name: SAP BRIM (Billing and Revenue Innovation Management) Balances API
  slug: sap-brim-billing-and-revenue-innovation-management-balances-api
- description: Billing cycle and invoice generation operations
  name: SAP BRIM (Billing and Revenue Innovation Management) Billing API
  slug: sap-brim-billing-and-revenue-innovation-management-billing-api
- description: Real-time charging operations for prepaid and postpaid accounts
  name: SAP BRIM (Billing and Revenue Innovation Management) Charging API
  slug: sap-brim-billing-and-revenue-innovation-management-charging-api
- description: Customer account management for subscriptions
  name: SAP BRIM (Billing and Revenue Innovation Management) Customers API
  slug: sap-brim-billing-and-revenue-innovation-management-customers-api
- description: Subscription plan and offer catalog management
  name: SAP BRIM (Billing and Revenue Innovation Management) Plans API
  slug: sap-brim-billing-and-revenue-innovation-management-plans-api
- description: Management of pricing plans, rate cards, and pricing structures
  name: SAP BRIM (Billing and Revenue Innovation Management) Pricing API
  slug: sap-brim-billing-and-revenue-innovation-management-pricing-api
- description: Operations for rating usage events against pricing plans
  name: SAP BRIM (Billing and Revenue Innovation Management) Rating API
  slug: sap-brim-billing-and-revenue-innovation-management-rating-api
- description: Management of individual items within a subscription
  name: SAP BRIM (Billing and Revenue Innovation Management) Subscription Items API
  slug: sap-brim-billing-and-revenue-innovation-management-subscription-items-api
- description: Subscription lifecycle management operations
  name: SAP BRIM (Billing and Revenue Innovation Management) Subscriptions API
  slug: sap-brim-billing-and-revenue-innovation-management-subscriptions-api
- description: Submission and management of usage event records
  name: SAP BRIM (Billing and Revenue Innovation Management) Usage Events API
  slug: sap-brim-billing-and-revenue-innovation-management-usage-events-api
arazzos:
- description: Add a line item to a subscription, read it back, and generate an on-demand invoice.
  name: SAP BRIM Add a Subscription Item and Invoice It
  slug: sap-brim-billing-and-revenue-innovation-management-add-item-and-invoice-workflow
- description: Reserve an amount against a prepaid balance, confirm it into a final charge, and read the balance.
  name: SAP BRIM Authorize and Confirm a Charge Reservation
  slug: sap-brim-billing-and-revenue-innovation-management-authorize-confirm-charge-workflow
- description: Check the balance, reserve an amount, and release the reservation when it is not needed.
  name: SAP BRIM Authorize a Charge or Release on Insufficient Balance
  slug: sap-brim-billing-and-revenue-innovation-management-authorize-or-release-workflow
- description: Rate a batch of usage events in one call, then charge the account for the aggregate total.
  name: SAP BRIM Batch Rate Usage and Charge the Total
  slug: sap-brim-billing-and-revenue-innovation-management-batch-rate-and-charge-workflow
- description: Cancel a subscription, verify the cancelled state, then optionally delete it.
  name: SAP BRIM Cancel and Clean Up a Subscription
  slug: sap-brim-billing-and-revenue-innovation-management-cancel-and-cleanup-workflow
- description: Execute a charge against an account, refund that charge, and confirm the balance.
  name: SAP BRIM Charge an Account and Refund It
  slug: sap-brim-billing-and-revenue-innovation-management-charge-and-refund-workflow
- description: List a customer's subscriptions, read their billing summary, and pull billing history.
  name: SAP BRIM Customer Billing Overview
  slug: sap-brim-billing-and-revenue-innovation-management-customer-billing-overview-workflow
- description: Manually renew a subscription, invoice the renewed term, and read the billing history.
  name: SAP BRIM Renew a Subscription and Invoice the New Term
  slug: sap-brim-billing-and-revenue-innovation-management-manual-renewal-invoice-workflow
- description: Read a prepaid balance, top it up, execute a charge, and confirm the new balance.
  name: SAP BRIM Top Up and Charge a Prepaid Account
  slug: sap-brim-billing-and-revenue-innovation-management-prepaid-topup-and-charge-workflow
- description: Create a pricing plan, attach a rate card, list its rate cards, and read the plan back.
  name: SAP BRIM Build a Pricing Plan with a Rate Card
  slug: sap-brim-billing-and-revenue-innovation-management-pricing-plan-with-rate-card-workflow
- description: Create a subscription plan, subscribe a customer, activate the subscription, and confirm its state.
  name: SAP BRIM Provision a New Subscription
  slug: sap-brim-billing-and-revenue-innovation-management-provision-subscription-workflow
- description: Simulate the price of a usage event, commit the rating, then charge the rated amount.
  name: SAP BRIM Simulate, Rate, and Charge Usage
  slug: sap-brim-billing-and-revenue-innovation-management-simulate-rate-and-charge-workflow
- description: Read a subscription, switch it to a new plan with proration, and confirm the change.
  name: SAP BRIM Upgrade or Downgrade a Subscription Plan
  slug: sap-brim-billing-and-revenue-innovation-management-subscription-upgrade-workflow
- description: Suspend an active subscription, confirm the paused state, then reactivate it.
  name: SAP BRIM Suspend and Resume a Subscription
  slug: sap-brim-billing-and-revenue-innovation-management-suspend-and-resume-workflow
- description: List a subscription's items, update the quantity of one, confirm it, and generate an invoice.
  name: SAP BRIM Update a Subscription Item Quantity and Re-invoice
  slug: sap-brim-billing-and-revenue-innovation-management-update-item-quantity-and-invoice-workflow
- description: Submit a usage event for processing, then poll its status until it has been rated.
  name: SAP BRIM Submit a Usage Event and Poll for Rating
  slug: sap-brim-billing-and-revenue-innovation-management-usage-event-rating-poll-workflow
artifact_total: 75
collections:
- collection_type: postman
  name: SAP BRIM (Billing and Revenue Innovation Management) SAP BRIM Convergent Charging API
  slug: postman-sap-brim-convergent-charging
- collection_type: postman
  name: SAP BRIM (Billing and Revenue Innovation Management) SAP BRIM Subscription Billing API
  slug: postman-sap-brim-subscription-billing
- collection_type: open
  name: SAP BRIM (Billing and Revenue Innovation Management) SAP BRIM Convergent Charging API
  slug: open-sap-brim-convergent-charging
- collection_type: open
  name: SAP BRIM (Billing and Revenue Innovation Management) SAP BRIM Subscription Billing API
  slug: open-sap-brim-subscription-billing
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-brim-billing-and-revenue-innovation-management-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-brim-billing-and-revenue-innovation-management-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-brim-billing-and-revenue-innovation-management-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-brim-billing-and-revenue-innovation-management-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-brim-billing-and-revenue-innovation-management-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sap-brim-billing-and-revenue-innovation-management/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-add-item-and-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-authorize-confirm-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-authorize-or-release-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-batch-rate-and-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-cancel-and-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-charge-and-refund-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-customer-billing-overview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-manual-renewal-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-prepaid-topup-and-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-pricing-plan-with-rate-card-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-provision-subscription-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-simulate-rate-and-charge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-subscription-upgrade-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-suspend-and-resume-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-update-item-quantity-and-invoice-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-brim-billing-and-revenue-innovation-management-usage-event-rating-poll-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://api.sap.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/sap-brim-convergent-charging-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/sap-brim-subscription-billing-openapi.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sap-brim-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sap-brim-subscription-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sap-brim-subscription-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sap-brim-rating-request-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/sap-brim-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sap-brim-vocabulary.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/SAP_BRIM/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://help.sap.com/docs/SAP_BRIM/authentication
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: operate
  title: ''
  type: Community
  url: https://community.sap.com
- group: company
  title: ''
  type: Blog
  url: https://blogs.sap.com
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/financial-management/billing-revenue-innovation-management.html
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/BRIM
- group: build
  title: ''
  type: SDKs
  url: https://developers.sap.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/sap
- group: start
  title: ''
  type: Signup
  url: https://developers.sap.com/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@sapdevs
- group: learn
  title: ''
  type: Learning
  url: https://learning.sap.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://support.sap.com/en/product/onboarding-resource-center/brim.html
created: '2024-01-15'
description: SAP BRIM (Billing and Revenue Innovation Management) is a comprehensive solution for order-to-cash processes, subscription management, usage-based pricing, and revenue management. It enables businesses to manage complex billing scenarios, subscription lifecycle, and revenue recognition.
examples:
- key_count: 4
  name: Sap Brim List Subscriptions Example
  slug: sap-brim-list-subscriptions-example
- key_count: 2
  name: Sap Brim Rate Usage Event Example
  slug: sap-brim-rate-usage-event-example
finops:
- name: Sap Brim Billing And Revenue Innovation Management Finops
  service_category: Billing / Revenue Management
  slug: sap-brim-billing-and-revenue-innovation-management-finops
image: https://www.sap.com/dam/application/shared/logos/sap-logo-svg.svg
json_schemas:
- name: AccountBalance
  property_count: 7
  slug: sap-brim-billing-and-revenue-innovation-management-accountbalance
- name: AuthorizationRequest
  property_count: 5
  slug: sap-brim-billing-and-revenue-innovation-management-authorizationrequest
- name: AuthorizationResponse
  property_count: 6
  slug: sap-brim-billing-and-revenue-innovation-management-authorizationresponse
- name: BillingRecord
  property_count: 13
  slug: sap-brim-billing-and-revenue-innovation-management-billingrecord
- name: ChargingRequest
  property_count: 7
  slug: sap-brim-billing-and-revenue-innovation-management-chargingrequest
- name: ChargingResponse
  property_count: 7
  slug: sap-brim-billing-and-revenue-innovation-management-chargingresponse
- name: CustomerBillingSummary
  property_count: 9
  slug: sap-brim-billing-and-revenue-innovation-management-customerbillingsummary
- name: ErrorResponse
  property_count: 1
  slug: sap-brim-billing-and-revenue-innovation-management-errorresponse
- name: MonetaryAmount
  property_count: 2
  slug: sap-brim-billing-and-revenue-innovation-management-monetaryamount
- name: Plan
  property_count: 14
  slug: sap-brim-billing-and-revenue-innovation-management-plan
- name: PlanCreate
  property_count: 9
  slug: sap-brim-billing-and-revenue-innovation-management-plancreate
- name: PricingPlan
  property_count: 12
  slug: sap-brim-billing-and-revenue-innovation-management-pricingplan
- name: PricingPlanCreate
  property_count: 7
  slug: sap-brim-billing-and-revenue-innovation-management-pricingplancreate
- name: PricingTier
  property_count: 5
  slug: sap-brim-billing-and-revenue-innovation-management-pricingtier
- name: RateCard
  property_count: 7
  slug: sap-brim-billing-and-revenue-innovation-management-ratecard
- name: RateCardCreate
  property_count: 6
  slug: sap-brim-billing-and-revenue-innovation-management-ratecardcreate
- name: RatingRequest
  property_count: 7
  slug: sap-brim-billing-and-revenue-innovation-management-ratingrequest
- name: RatingResponse
  property_count: 11
  slug: sap-brim-billing-and-revenue-innovation-management-ratingresponse
- name: RefundRequest
  property_count: 3
  slug: sap-brim-billing-and-revenue-innovation-management-refundrequest
- name: RefundResponse
  property_count: 5
  slug: sap-brim-billing-and-revenue-innovation-management-refundresponse
- name: Subscription
  property_count: 22
  slug: sap-brim-billing-and-revenue-innovation-management-subscription
- name: SubscriptionCreate
  property_count: 11
  slug: sap-brim-billing-and-revenue-innovation-management-subscriptioncreate
- name: SubscriptionItem
  property_count: 11
  slug: sap-brim-billing-and-revenue-innovation-management-subscriptionitem
- name: SubscriptionItemCreate
  property_count: 4
  slug: sap-brim-billing-and-revenue-innovation-management-subscriptionitemcreate
- name: SubscriptionUpdate
  property_count: 4
  slug: sap-brim-billing-and-revenue-innovation-management-subscriptionupdate
- name: UsageEvent
  property_count: 7
  slug: sap-brim-billing-and-revenue-innovation-management-usageevent
- name: UsageEventDetail
  property_count: 11
  slug: sap-brim-billing-and-revenue-innovation-management-usageeventdetail
- name: SAP BRIM Subscription
  property_count: 29
  slug: sap-brim-subscription
json_structures:
- name: Sap Brim Billing And Revenue Innovation Management Structure
  property_count: 0
  slug: sap-brim-billing-and-revenue-innovation-management-structure
- name: Sap Brim Rating Request Structure
  property_count: 0
  slug: sap-brim-rating-request-structure
- name: Sap Brim Subscription Structure
  property_count: 0
  slug: sap-brim-subscription-structure
jsonld:
- class_count: 0
  name: Sap Brim Context
  property_count: 26
  slug: sap-brim-context
layout: provider
modified: '2026-05-19'
name: SAP BRIM (Billing and Revenue Innovation Management)
nav: Providers
network: true
overview: 'SAP BRIM (Billing and Revenue Innovation Management) publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Balances API, Billing API, Charging API, and 7 more. Tagged areas include Billing, Enterprise, Order to Cash, Revenue Management, and SAP.


  The SAP BRIM (Billing and Revenue Innovation Management) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SAP BRIM (Billing and Revenue Innovation Management)''s developer surface includes authentication, developer portal, getting-started guide, support, engineering blog, documentation, Stack Overflow tag, and 41 more developer resources.'
plans:
- name: Sap Brim Billing And Revenue Innovation Management Plans Pricing
  plan_count: 1
  slug: sap-brim-billing-and-revenue-innovation-management-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Sap Brim Billing And Revenue Innovation Management Rate Limits
  slug: sap-brim-billing-and-revenue-innovation-management-rate-limits
rules:
- name: SAP BRIM (Billing and Revenue Innovation Management) API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: sap-brim-billing-and-revenue-innovation-management-jsonschema-spectral-rules
- name: SAP BRIM (Billing and Revenue Innovation Management) API Rules
  rule_count: 10
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 8
  slug: sap-brim-rules
scopes:
- name: Sap Brim Billing And Revenue Innovation Management Scopes
  scope_count: 2
  slug: sap-brim-billing-and-revenue-innovation-management-scopes
  summary_line: 2 scopes · clientCredentials
score:
  band: strong
  composite: 64.9
  delta: 4.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 70.8
    developer_ergonomics: 56.5
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 42.1
  previous_composite: 60.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-brim-billing-and-revenue-innovation-management/refs/heads/main/screenshots/sap-brim-billing-and-revenue-innovation-management-2026-06-20T193418.png
security:
- kind: authentication
  name: Sap Brim Billing And Revenue Innovation Management Authentication
  slug: sap-brim-billing-and-revenue-innovation-management-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Sap Brim Billing And Revenue Innovation Management Domain Security
  slug: sap-brim-billing-and-revenue-innovation-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Brim Billing And Revenue Innovation Management Vulnerability Disclosure
  slug: sap-brim-billing-and-revenue-innovation-management-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-brim-billing-and-revenue-innovation-management
tags:
- Billing
- Enterprise
- Order to Cash
- Revenue Management
- SAP
- Subscription Management
- Usage-Based Pricing
website: https://www.sap.com/products/financial-management/billing-revenue-innovation-management.html
---
