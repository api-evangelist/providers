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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 183
  human_in_the_loop: 2
  name: Recurly Agentic Access
  operation_count: 355
  slug: recurly-agentic-access
  summary_line: 355 operations · 183 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: Public, OAuth-protected Model Context Protocol server (streamable HTTP) exposing Recurly Compass Knowledge Agent (docs_search) and Coding Agent (api_reference_search) to Claude, Cursor and other MCP c
  name: Recurly Compass MCP server
  slug: recurly-compass-mcp-server
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Recurly offers the ability to record marketing data on customer accounts to match this data with revenue and billing data events in Recurly.
  name: Recurly Account Acquisition Info API
  slug: recurly-account-acquisition-info-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: 'Accounts are core to managing your customers inside of Recurly. The account object stores the entire Recurly history of your customer and acts as the entry point for working with a customer''s billing '
  name: Recurly Account API
  slug: recurly-account-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Account notes allow your team to leave notes on an account to add context, e.g. the reason for a refund, customer requests, and/or complaints. These notes are internal and not exposed to your customer
  name: Recurly Account Note API
  slug: recurly-account-note-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The accounts API from Recurly — 5 operation(s) for accounts.
  name: Recurly Accounts API
  slug: recurly-accounts-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: An add-on is a charge billed each billing period in addition to a subscription’s base charge. Each plan may have one or more add-ons associated with it.
  name: Recurly Add On API
  slug: recurly-add-on-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The adjustments API from Recurly — 2 operation(s) for adjustments.
  name: Recurly Adjustments API
  slug: recurly-adjustments-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Automated exports of customer data.
  name: Recurly Automated Exports API
  slug: recurly-automated-exports-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The BaseOrderLineItems API API from Recurly — 1 operation(s) for baseorderlineitems api.
  name: Recurly BaseOrderLineItems API
  slug: recurly-baseorderlineitems-api-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The BaseOrders API API from Recurly — 1 operation(s) for baseorders api.
  name: Recurly BaseOrders API
  slug: recurly-baseorders-api-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The billing-info API from Recurly — 4 operation(s) for billing-info.
  name: Recurly Billing Info API
  slug: recurly-billing-info-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: If the premium Wallet feature is enabled, an account can have multiple payment methods stored. Examples include credit cards, PayPal, or bank accounts. Primary or backup billing infos can be designate
  name: Recurly Billing Infos API
  slug: recurly-billing-infos-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The BillingAttempts API API from Recurly — 1 operation(s) for billingattempts api.
  name: Recurly BillingAttempts API
  slug: recurly-billingattempts-api-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Describes the business address that will be used for invoices and taxes depending on settings and subscriber location.
  name: Recurly Business Entities API
  slug: recurly-business-entities-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The CancellationQuestions API API from Recurly — 1 operation(s) for cancellationquestions api.
  name: Recurly CancellationQuestions API
  slug: recurly-cancellationquestions-api-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The CancellationSurveyResults API API from Recurly — 1 operation(s) for cancellationsurveyresults api.
  name: Recurly CancellationSurveyResults API
  slug: recurly-cancellationsurveyresults-api-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Coupons can either be single codes that easily allow mass distribution by many customers or bulk coupons that can generate many unique coupons that can allow for individual delivery and tracking.
  name: Recurly Coupon API
  slug: recurly-coupon-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Coupon redemptions are created when a coupon is applied to an account or subscription. This allows you to track your promotions.
  name: Recurly Coupon Redemption API
  slug: recurly-coupon-redemption-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The coupon-redemptions API from Recurly — 3 operation(s) for coupon-redemptions.
  name: Recurly Coupon Redemptions API
  slug: recurly-coupon-redemptions-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The coupons API from Recurly — 2 operation(s) for coupons.
  name: Recurly Coupons API
  slug: recurly-coupons-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The Credit Payment API from Recurly — 3 operation(s) for credit payment.
  name: Recurly Credit Payment API
  slug: recurly-credit-payment-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Describes the fields that can be used as custom fields on accounts, items, line-items (one time charges), plans, or subscriptions.
  name: Recurly Custom Field Definition API
  slug: recurly-custom-field-definition-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Settings used when attempting to dun customers whose payments are declined.
  name: Recurly Dunning Campaigns API
  slug: recurly-dunning-campaigns-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: An account from an external resource that is not managed by the Recurly platform and instead is managed by third-party platforms like Apple App Store and Google Play Store.
  name: Recurly External Account API
  slug: recurly-external-account-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: An invoice from an external resource that is not managed by the Recurly platform and instead is managed by third-party platforms like Apple App Store and Google Play Store.
  name: Recurly External Invoice API
  slug: recurly-external-invoice-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Details of payments in the lifecycle of a subscription from an external resource that is not managed by the Recurly platform, e.g. App Store or Google Play Store.
  name: Recurly External Payment Phase API
  slug: recurly-external-payment-phase-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: A product from an external resource that is not managed by the Recurly platform and instead is managed by third-party platforms like Apple App Store and Google Play Store.
  name: Recurly External Product API
  slug: recurly-external-product-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Associates an external product to a corresponding resource on an external platform like the Apple App Store or Google Play Store.
  name: Recurly External Product Reference API
  slug: recurly-external-product-reference-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: A subscription from an external resource that is not managed by the Recurly platform and instead is managed by third-party platforms like Apple App Store and Google Play Store.
  name: Recurly External Subscription API
  slug: recurly-external-subscription-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: A general ledger account is an account of record used to sort, store and summarize a company's transactions. Recurly supports the balance sheet (Liability) account and income (Revenue) account to be a
  name: Recurly General Ledger Account API
  slug: recurly-general-ledger-account-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Add gift card purchases to your checkout and allow gift card recipients to redeem the gift card for credit towards any of your products.
  name: Recurly Gift Cards API
  slug: recurly-gift-cards-api
- baseURL: https://revrec.recurly.com
  baseurl_source: declared
  description: The Inbound APIs API from Recurly — 6 operation(s) for inbound apis.
  name: Recurly Inbound APIs API
  slug: recurly-inbound-apis-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: An invoice relates charges, credits, and payments together. When a subscription is created or renewed or a charge is created on the account, Recurly will sum the charges, discount or tax as appropriat
  name: Recurly Invoice API
  slug: recurly-invoice-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The Invoice Templates API from Recurly — 2 operation(s) for invoice templates.
  name: Recurly Invoice Templates API
  slug: recurly-invoice-templates-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The invoices API from Recurly — 8 operation(s) for invoices.
  name: Recurly Invoices API
  slug: recurly-invoices-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: For merchants who sell the same things to many customers, documenting those offerings in a catalog allows for faster charge creation, easier management of offerings, and analytics about your offerings
  name: Recurly Item API
  slug: recurly-item-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Line items are the charges and credits on your customer's invoices.
  name: Recurly Line Item API
  slug: recurly-line-item-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: A measured unit describes a usage-based add-on's usage. If different usage-based add-ons share the same measured unit, you can report on customer usage for those add-ons at the aggregated measured uni
  name: Recurly Measured Unit API
  slug: recurly-measured-unit-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The Memberships API API from Recurly — 2 operation(s) for memberships api.
  name: Recurly Memberships API
  slug: recurly-memberships-api-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The OneTimeAddOns API API from Recurly — 2 operation(s) for onetimeaddons api.
  name: Recurly OneTimeAddOns API
  slug: recurly-onetimeaddons-api-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The OrderLineItems API API from Recurly — 1 operation(s) for orderlineitems api.
  name: Recurly OrderLineItems API
  slug: recurly-orderlineitems-api-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The Orders API API from Recurly — 2 operation(s) for orders api.
  name: Recurly Orders API
  slug: recurly-orders-api-api
- baseURL: https://revrec.recurly.com
  baseurl_source: declared
  description: The Outbound Report APIs API from Recurly — 6 operation(s) for outbound report apis.
  name: Recurly Outbound Report APIs API
  slug: recurly-outbound-report-apis-api
- baseURL: https://conduit.redfast.com
  baseurl_source: declared
  description: The Paths API from Recurly — 5 operation(s) for paths.
  name: Recurly Paths API
  slug: recurly-paths-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: A performance obligation is a promise to provide a distinct good or service or a series of distinct goods or services as defined by the revenue standard. Performance obligations are completed and reve
  name: Recurly Performance Obligations API
  slug: recurly-performance-obligations-api
- baseURL: https://conduit.redfast.com
  baseurl_source: declared
  description: The Ping API from Recurly — 2 operation(s) for ping.
  name: Recurly Ping API
  slug: recurly-ping-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The plan-add-ons API from Recurly — 3 operation(s) for plan-add-ons.
  name: Recurly Plan Add Ons API
  slug: recurly-plan-add-ons-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: A plan tells Recurly how often and how much to charge your customers. Plans can be created with free trials, optional products (called add-ons), setup fees, and more.
  name: Recurly Plan API
  slug: recurly-plan-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The plans API from Recurly — 2 operation(s) for plans.
  name: Recurly Plans API
  slug: recurly-plans-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The Price Segment API from Recurly — 2 operation(s) for price segment.
  name: Recurly Price Segment API
  slug: recurly-price-segment-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The Products API API from Recurly — 1 operation(s) for products api.
  name: Recurly Products API
  slug: recurly-products-api-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: A purchase is a checkout containing at least one or more subscriptions or one-time charges (line items) and supports both coupon and gift card redemptions. All items purchased will be on one invoice a
  name: Recurly Purchase API
  slug: recurly-purchase-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Revenue recovery
  name: Recurly Revenue Recovery API
  slug: recurly-revenue-recovery-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Shipping addresses are tied to a customer's account. Each account can have up to 20 different shipping addresses, and if you have enabled multiple subscriptions per account, you can associate differen
  name: Recurly Shipping Address API
  slug: recurly-shipping-address-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Shipping methods offered to send products to customers.
  name: Recurly Shipping Method API
  slug: recurly-shipping-method-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The Site API from Recurly — 2 operation(s) for site.
  name: Recurly Site API
  slug: recurly-site-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The Subscribers API API from Recurly — 5 operation(s) for subscribers api.
  name: Recurly Subscribers API
  slug: recurly-subscribers-api-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Subscriptions are created when your customers subscribe to one of your plans. The customer's subscription tells Recurly when and how much to bill the customer.
  name: Recurly Subscription API
  slug: recurly-subscription-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Subscription changes alter subscription in a way that might affect the invoiced amount, such as changing the plan, add-ons, quantities, or shipping address. Changes can be made immediately in the curr
  name: Recurly Subscription Change API
  slug: recurly-subscription-change-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The Subscription Offers API API from Recurly — 2 operation(s) for subscription offers api.
  name: Recurly Subscription Offers API
  slug: recurly-subscription-offers-api-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The SubscriptionActivities API API from Recurly — 1 operation(s) for subscriptionactivities api.
  name: Recurly SubscriptionActivities API
  slug: recurly-subscriptionactivities-api-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The SubscriptionDiscountCodes API API from Recurly — 1 operation(s) for subscriptiondiscountcodes api.
  name: Recurly SubscriptionDiscountCodes API
  slug: recurly-subscriptiondiscountcodes-api-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The SubscriptionLines API API from Recurly — 7 operation(s) for subscriptionlines api.
  name: Recurly SubscriptionLines API
  slug: recurly-subscriptionlines-api-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The Subscriptions API API from Recurly — 17 operation(s) for subscriptions api.
  name: Recurly Subscriptions API
  slug: recurly-subscriptions-api-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The subscriptions API from Recurly — 10 operation(s) for subscriptions.
  name: Recurly Subscriptions API
  slug: recurly-subscriptions-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The SwapAndAddOnOptions API API from Recurly — 1 operation(s) for swapandaddonoptions api.
  name: Recurly SwapAndAddOnOptions API
  slug: recurly-swapandaddonoptions-api-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Purchasing information is sent to your payment gateway in an action called a transaction. This includes the customer's billing information and the amount of money to be charged, voided, or refunded.
  name: Recurly Transaction API
  slug: recurly-transaction-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: The transactions API from Recurly — 3 operation(s) for transactions.
  name: Recurly Transactions API
  slug: recurly-transactions-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Unique coupon codes are generated from bulk coupons.
  name: Recurly Unique Coupon Code API
  slug: recurly-unique-coupon-code-api
- baseURL: https://v3.recurly.com
  baseurl_source: declared
  description: Send Recurly your customer usage and we will automatically bill them in arrears at the end of the billing cycle. For more info on usage-based billing, [click here](https://docs.recurly.com/docs/usage-
  name: Recurly Usage API
  slug: recurly-usage-api
- baseURL: https://subs.api.recurlycommerce.com
  baseurl_source: declared
  description: The Webhooks API API from Recurly — 3 operation(s) for webhooks api.
  name: Recurly Webhooks API
  slug: recurly-webhooks-api-api
artifact_total: 104
asyncapis:
- description: ''
  name: Recurly Webhooks
  slug: recurly-webhooks
common:
- group: other
  href: https://artifacts.apis.io/recurly/capabilities/recurly-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/recurly-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/recurly/asyncapi/recurly-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/recurly-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/recurly/agentic-access/recurly-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/recurly-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/recurly/rate-limits/recurly-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/recurly-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/recurly/plans/recurly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/recurly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/recurly/rules/recurly-rules.yml
  title: ''
  type: Spectral
  url: rules/recurly-rules.yml
- group: design
  href: https://artifacts.apis.io/recurly/json-ld/recurly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/recurly-context.jsonld
- group: design
  href: https://artifacts.apis.io/recurly/vocabulary/recurly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/recurly-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/recurly/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/recurly/data-model/recurly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/recurly-data-model.yml
- group: design
  href: https://artifacts.apis.io/recurly/components/recurly-components.yml
  title: ''
  type: Components
  url: components/recurly-components.yml
- group: operate
  href: https://artifacts.apis.io/recurly/changelog/recurly-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/recurly-changelog.yml
- group: design
  href: https://artifacts.apis.io/recurly/conventions/recurly-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/recurly-conventions.yml
- group: design
  href: https://artifacts.apis.io/recurly/conventions/recurly-conventions.yml
  title: ''
  type: Conventions
  url: conventions/recurly-conventions.yml
- group: start
  href: https://artifacts.apis.io/recurly/sandbox/recurly-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/recurly-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.recurly.com/
- group: auth
  href: https://artifacts.apis.io/recurly/scopes/recurly-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/recurly-scopes.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://recurly.com/developers/api/changelog.html
- group: design
  href: https://artifacts.apis.io/recurly/lifecycle/recurly-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/recurly-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/recurly/errors/recurly-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/recurly-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/recurly/errors/recurly-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/recurly-problem-types.yml
- group: design
  href: https://artifacts.apis.io/recurly/conformance/recurly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/recurly-conformance.yml
- group: agent
  href: https://artifacts.apis.io/recurly/llms/recurly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/recurly-llms.txt
- group: agent
  href: https://artifacts.apis.io/recurly/llms/recurly-docs-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/recurly-docs-llms.txt
- group: build
  href: https://artifacts.apis.io/recurly/mcp/recurly-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/recurly-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/recurly/mcp/recurly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/recurly-mcp.yml
- group: agent
  href: https://artifacts.apis.io/recurly/well-known/recurly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/recurly-well-known.yml
- group: other
  href: https://artifacts.apis.io/recurly/hosts/recurly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/recurly-hosts.yml
- group: build
  href: https://artifacts.apis.io/recurly/integrations/recurly-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/recurly-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/recurly/vendors/recurly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/recurly-vendors.yml
- group: build
  href: https://artifacts.apis.io/recurly/packages/recurly-packages.yml
  title: ''
  type: Packages
  url: packages/recurly-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://docs.recurly.com/recurly-subscriptions/docs/webhooks
- group: build
  title: ''
  type: SDKs
  url: https://recurly.com/developers/
- group: auth
  href: https://artifacts.apis.io/recurly/authentication/recurly-authentication.yml
  title: ''
  type: Authentication
  url: authentication/recurly-authentication.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://recurly.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://recurly.com/legal/terms
- group: auth
  href: https://artifacts.apis.io/recurly/security/recurly-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/recurly-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/recurly/security/recurly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/recurly-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recurly
- group: company
  title: ''
  type: Website
  url: https://recurly.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.recurly.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://recurly.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://recurly.com/developers/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://recurly.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/recurly
- group: operate
  title: ''
  type: Support
  url: https://recurly.zendesk.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.recurly.com
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.recurly.com/llms.txt
- group: company
  title: ''
  type: BlogRSS
  url: https://recurly.com/blog/rss.xml
- group: start
  title: ''
  type: SignUp
  url: https://info.recurly.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.recurly.com/login
- group: company
  title: ''
  type: Newsroom
  url: https://recurly.com/newsroom/
- group: auth
  title: ''
  type: Security
  url: https://recurly.com/legal/security/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.recurly.com/recurly-subscriptions/docs/quick-start-guide
- group: company
  title: ''
  type: Blog
  url: https://recurly.com/blog/
- group: start
  title: ''
  type: Sandbox
  url: https://docs.recurly.com/recurly-subscriptions/docs/sandbox-features-to-discover
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.recurly.com/recurly-subscriptions/changelog
- group: other
  title: ''
  type: Subprocessors
  url: https://recurly.com/legal/privacy/subprocessors/
created: '2026-05-11'
description: Recurly is a subscription management and recurring billing platform (Recurly Subscriptions, Recurly Commerce for Shopify, Recurly Engage, Recurly RevRec and the Recurly Compass AI layer) that handles signups, plans, add-ons, coupons, dunning, invoicing, tax, revenue recognition and analytics for subscription businesses. The Recurly v3 REST API (v3.recurly.com, date-versioned through the Accept header, HTTP Basic with a site API key, Idempotency-Key replay protection) covers accounts, subscriptions, invoices, transactions, plans, purchases and external (app store) subscriptions; the legacy XML API v2, the Commerce, Recover and RevRec APIs, Recurly.js Elements, webhooks and a public Compass MCP server complete the surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recurly.png
json_schemas:
- name: Add-on
  property_count: 28
  slug: recurly-add-on-create
- name: BillingAttemptDto
  property_count: 20
  slug: recurly-billing-attempt-dto
- name: DunningCampaignList
  property_count: 4
  slug: recurly-dunning-campaign-list
- name: DunningCampaign
  property_count: 10
  slug: recurly-dunning-campaign
- name: Invoice collection
  property_count: 4
  slug: recurly-invoice-collection
- name: Invoice
  property_count: 47
  slug: recurly-invoice
- name: Line item
  property_count: 61
  slug: recurly-line-item
- name: PurchaseCreate
  property_count: 23
  slug: recurly-purchase-create
- name: RecoveryInvoiceCreate
  property_count: 7
  slug: recurly-recovery-invoice-create
- name: SubscriberDto
  property_count: 10
  slug: recurly-subscriber-dto
- name: SubscriptionCreateRequestDTO
  property_count: 22
  slug: recurly-subscription-create-request-dto
- name: SubscriptionCreate
  property_count: 38
  slug: recurly-subscription-create
- name: SubscriptionDto
  property_count: 57
  slug: recurly-subscription-dto
- name: SubscriptionLineDto
  property_count: 15
  slug: recurly-subscription-line-dto
- name: SubscriptionOfferDto
  property_count: 12
  slug: recurly-subscription-offer-dto
- name: Subscription
  property_count: 57
  slug: recurly-subscription
- name: Transaction
  property_count: 46
  slug: recurly-transaction
jsonld:
- class_count: 120
  name: Recurly Context
  property_count: 312
  slug: recurly-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.recurly.com over HTTP requiring OAuth; 2 tools listed.
  name: Recurly Compass MCP
  slug: recurly
modified: '2026-11-05'
name: Recurly
nav: Providers
network: true
overview: 'Recurly publishes 71 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Acquisition Info API, Account API, Account Note API, and 68 more. Tagged areas include Subscription, Billing, Payments, Recurring Revenue, and Invoicing.


  The Recurly catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Recurly''s developer surface includes changelog, sandbox, authentication, documentation, API reference, pricing, support, and 51 more developer resources.'
plans:
- name: Recurly Plans Pricing
  plan_count: 5
  slug: recurly-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Recurly Rate Limits
  slug: recurly-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Recurly API Rules
  rule_count: 52
  severity_counts:
    error: 28
    hint: 0
    info: 3
    warn: 21
  slug: recurly-rules
scopes:
- name: Recurly Scopes
  scope_count: 1
  slug: recurly-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 78.8
  coverage:
    artifact_dirs: 35
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 43.1
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 70.2
    developer_ergonomics: 73.2
    discoverability: 81.7
    operational_transparency: 84.2
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 70
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2-sca
    - jurisdiction: US
      standard: ccpa
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/recurly/recurly-2026-06-20T192713.png
security:
- kind: authentication
  name: Recurly Authentication
  slug: recurly-authentication
  summary_line: http/apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Recurly Domain Security
  slug: recurly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Recurly Trust Center
  slug: recurly-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
skill_count: 5
skills:
- name: recurly-cancel-or-reactivate-subscription
  slug: recurly-cancel-or-reactivate-subscription
- name: recurly-change-subscription-plan
  slug: recurly-change-subscription-plan
- name: recurly-create-purchase
  slug: recurly-create-purchase
- name: recurly-paginate-and-export
  slug: recurly-paginate-and-export
- name: recurly-refund-invoice
  slug: recurly-refund-invoice
slug: recurly
tags:
- Subscription
- Billing
- Payments
- Recurring Revenue
- Invoicing
- Dunning
- Revenue Recognition
- Churn
- MCP
- Shopify
- Webhook
website: https://recurly.com
---
