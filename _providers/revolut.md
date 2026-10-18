---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 130
  human_in_the_loop: 1
  name: Revolut Agentic Access
  operation_count: 259
  slug: revolut-agentic-access
  summary_line: 259 operations · 130 acting · 1 human-in-the-loop
api_count: 8
apis:
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: Manage [accounting settings](https://business.revolut.com/settings/accounting) for your business that can be assigned to your financial records such as [expenses](https://developer.revolut.com/docs/gu
  name: Revolut Accounting API
  slug: revolut-accounting-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: Manage accounting categories for your business. You can create, retrieve, and delete accounting categories that can be assigned to your financial records such as [expenses](https://developer.revolut.c
  name: Revolut Accounting categories API
  slug: revolut-accounting-categories-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: 'Get the balances, full banking details, and other details of your business accounts. For more information, see the guides: [Get your account details](https://developer.revolut.com/docs/guides/manage-a'
  name: Revolut Accounts API
  slug: revolut-accounts-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: 'Operations for managing a merchant''s domain registration and configuration with Apple for integration of Apple Pay via Revolut. This includes initiating domain validation with Apple, a necessary step '
  name: Revolut Apple Pay merchant registration API
  slug: revolut-apple-pay-merchant-registration-api
- baseURL: https://oba-auth.revolut.com
  baseurl_source: declared
  description: 'These endpoints let you manage your applications. Applications can also be created in the [Developer Portal](https://developer.revolut.com/portal/). For more information, see: - [Register your applica'
  name: Revolut Applications API
  slug: revolut-applications-api
- baseURL: https://revx.revolut.com/api/1.0
  baseurl_source: declared
  description: Get your Revolut X crypto exchange balances, including both crypto and fiat.
  name: Revolut Balance API
  slug: revolut-balance-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: Use card invitations to pre-create cards for [team members](https://developer.revolut.com/docs/guides/manage-accounts/teams/manage-team-members) who have not yet onboarded. Once the team member comple
  name: Revolut Card invitations API
  slug: revolut-card-invitations-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: Manage cards issued for your business, freeze, unfreeze, lock, unlock, terminate and update card settings, such as spending limits and merchant controls. :::note - This feature is not available in San
  name: Revolut Cards API
  slug: revolut-cards-api
- baseURL: https://revx.revolut.com/api/1.0
  baseurl_source: declared
  description: Get Revolut X configuration for traded assets and pairs.
  name: Revolut Configuration API
  slug: revolut-configuration-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: Manage counterparties that you intend to transact with. Request and response examples can vary based on the account provider's location and type of the counterparty. For more information, see the guid
  name: Revolut Counterparties API
  slug: revolut-counterparties-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: The Customers resource in the Merchant API is a pivotal tool for tracking and managing customer-related transactions within your e-commerce or retail platform. This resource provides a structured appr
  name: Revolut Customers API
  slug: revolut-customers-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: Endpoints that allow merchants to view customer payment disputes. It provides a robust framework with high-level states (e.g., `won`, `lost`, `needs_response`, `under_review`) and detailed substates (
  name: Revolut Disputes API
  slug: revolut-disputes-api
- baseURL: https://oba-auth.revolut.com
  baseurl_source: declared
  description: '*Domestic payments*, which you can use for local payments in the local currency of the user. :::note Revolut supports only GBP as local in the UK and EUR in Single Euro Payments Area (SEPA) countries.'
  name: Revolut Domestic payment API
  slug: revolut-domestic-payment-api
- baseURL: https://oba-auth.revolut.com
  baseurl_source: declared
  description: '*Domestic scheduled payments*, which you can use for local payments in the local currency of the user. :::note Revolut supports only GBP as local in the UK and EUR in Single Euro Payments Area (SEPA) '
  name: Revolut Domestic scheduled payment API
  slug: revolut-domestic-scheduled-payment-api
- baseURL: https://oba-auth.revolut.com
  baseurl_source: declared
  description: '*Domestic standing orders*, which you can use for local payments in the local currency of the user. :::note Revolut supports only GBP as local in the UK and EUR in Single Euro Payments Area (SEPA) cou'
  name: Revolut Domestic standing order API
  slug: revolut-domestic-standing-order-api
- baseURL: https://oba-auth.revolut.com
  baseurl_source: declared
  description: 'You can create a draft payment to initiate a payment on behalf of a user, and request the approval for the draft payment in the user account. Then, you can retrieve or delete a draft payment. :::note '
  name: Revolut Draft payment API
  slug: revolut-draft-payment-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: 'Get the list of all the expenses, or use the filters to narrow down the results. You can also get a specific expense, or get a receipt related to an expense by providing their respective IDs. :::note '
  name: Revolut Expenses API
  slug: revolut-expenses-api
- baseURL: https://oba-auth.revolut.com
  baseurl_source: declared
  description: The File Payment API from Revolut — 6 operation(s) for file payment.
  name: Revolut File Payment API
  slug: revolut-file-payment-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: 'Retrieve information on exchange rates between currencies, buy and sell currencies. For more information, see the guides: [Exchange money](https://developer.revolut.com/docs/guides/manage-accounts/exc'
  name: Revolut Foreign exchange API
  slug: revolut-foreign-exchange-api
- baseURL: https://oba-auth.revolut.com
  baseurl_source: declared
  description: '*International payments*, which you can use for international SWIFT payments in all currencies that Revolut supports. As a regulated third party provider, you can use the provided endpoints to initiat'
  name: Revolut International payment API
  slug: revolut-international-payment-api
- baseURL: https://oba-auth.revolut.com
  baseurl_source: declared
  description: '*International scheduled payments*, which you can use for international SWIFT payments in all currencies that Revolut supports. As a regulated third party provider, you can use the provided endpoints '
  name: Revolut International scheduled payment API
  slug: revolut-international-scheduled-payment-api
- baseURL: https://oba-auth.revolut.com
  baseurl_source: declared
  description: '*International standing orders*, which you can use for international SWIFT payments in all currencies that Revolut supports. As a regulated third party provider, you can use the provided endpoints to '
  name: Revolut International standing order API
  slug: revolut-international-standing-order-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: Manage accounting labels and label groups for your business. Create, retrieve, update, and delete label groups and labels that can be added to your financial records such as [expenses](https://develop
  name: Revolut Labels API
  slug: revolut-labels-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: The Locations API is designed to help merchants manage multiple points of sale, including both **online storefronts** and **physical stores**. Registering locations lets you differentiate and group yo
  name: Revolut Locations API
  slug: revolut-locations-api
- baseURL: https://revx.revolut.com/api/1.0
  baseurl_source: declared
  description: Retrieve real-time and historical market data for Revolut X.
  name: Revolut Market Data API
  slug: revolut-market-data-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: The Orders resource in the Merchant API offers a comprehensive solution for managing the lifecycle of orders within your e-commerce or retail platform. Designed to streamline order processing, this re
  name: Revolut Orders API
  slug: revolut-orders-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: Other operations that can be done with the Merchant API.
  name: Revolut Other API
  slug: revolut-other-api
- baseURL: https://ramp-partners.revolut.com/partners/api/2.0
  baseurl_source: declared
  description: 'The **Partners** endpoints let you poll different exchange rates, display them on your website and compare them with other providers. For more details, see the guides: [Leverage the Crypto Ramp API](h'
  name: Revolut Partners API
  slug: revolut-partners-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: 'Payment drafts let you prepare payments for future processing, prepare payments that require an approval, or prepare bulk or scheduled payments. Simply create a draft, and when you''re ready, [send it '
  name: Revolut Payment drafts API
  slug: revolut-payment-drafts-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: Operations for managing payment intents in the push payments to Revolut Terminal flow. A **payment intent** represents the intention to complete payment for a specific order on a specific Revolut Term
  name: Revolut Payment intents API
  slug: revolut-payment-intents-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: Payment operations enable you to initiate payments, or track payment status transitions. You can use the ID of the payment to retrieve information about a specific payment. :::info For more informatio
  name: Revolut Payments API
  slug: revolut-payments-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: Use payout links to send money without having to request full banking details of the recipient. The recipient must claim the money before the link expires. :::note This feature is available in the UK,
  name: Revolut Payout links API
  slug: revolut-payout-links-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: 'Endpoints for retrieving information about payouts, allowing merchants to access details of funds withdrawn from their Merchant account to external bank accounts. Merchants can use these endpoints to '
  name: Revolut Payouts API
  slug: revolut-payouts-api
- baseURL: https://revx.revolut.com/api/1.0
  baseurl_source: declared
  description: Get Revolut X real time public market data.
  name: Revolut Public Market Data API
  slug: revolut-public-market-data-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: 'Use **Report runs** operations to generate CSV reports of your Merchant account transactions. Choose from the following report types based on your use case: | Report type | Description | | -----------'
  name: Revolut Report runs API
  slug: revolut-report-runs-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: 'The Simulations API is only available in the Sandbox environment. It lets you simulate certain events that are otherwise only possible in the production environment, such as your account''s top-up and '
  name: Revolut Simulations API
  slug: revolut-simulations-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: The Subscriptions API provides a complete solution for creating and managing recurring billing for your customers. You can automatically charge customers on flexible billing cycles, manage sophisticat
  name: Revolut Subscriptions API
  slug: revolut-subscriptions-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: Manage tax rates for your business. Create, retrieve, update, and delete tax rates that can be assigned to your financial records such as [expenses](https://developer.revolut.com/docs/guides/manage-ac
  name: Revolut Tax rates API
  slug: revolut-tax-rates-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: 'Retrieve information on existing team members of your organisation, delete team members, and invite new members. For more information, see the guides: [Manage team members](https://developer.revolut.c'
  name: Revolut Team members API
  slug: revolut-team-members-api
- baseURL: https://merchant.revolut.com
  baseurl_source: declared
  description: Operations for managing Revolut Terminal devices and push payment integrations with Point of Sale (POS) systems. The Terminals API enables POS software providers to integrate with Revolut Terminal dev
  name: Revolut Terminals API
  slug: revolut-terminals-api
- baseURL: https://revx.revolut.com/api/1.0
  baseurl_source: declared
  description: 'Retrieve Revolut X trade history and execution details: view public market trades or your specific private trade executions (fills).'
  name: Revolut Trades API
  slug: revolut-trades-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: 'Get the details of your transactions. :::note An incoming or outgoing payment is represented as a transaction. ::: For more information, see the guides: [Retrieve transactions](https://developer.revol'
  name: Revolut Transactions API
  slug: revolut-transactions-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: 'Move funds in the same currency between accounts of your business, or make payments to your counterparties. For more details, see the guides: [Send money](https://developer.revolut.com/docs/guides/man'
  name: Revolut Transfers API
  slug: revolut-transfers-api
- baseURL: https://ramp-partners.revolut.com/partners/api/2.0
  baseurl_source: declared
  description: A webhook (also called a web callback) allows your system to receive an event from Ramp immediately after it happens. With the **Webhooks** endpoints, you can create, update, delete, and retrieve webh
  name: Revolut Webhooks API
  slug: revolut-webhooks-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: ':::warning This is the v1 of the Webhooks API. This version is deprecated. For the latest version of the API, see [Webhooks (v2)](https://developer.revolut.com/docs/api/business#tag-webhooks-v2). ::: '
  name: Revolut Webhooks (v1) (deprecated) API
  slug: revolut-webhooks-v1-deprecated-api
- baseURL: https://b2b.revolut.com/api/1.0
  baseurl_source: declared
  description: :::note This is the latest version of the Webhooks API, v2. For the previous version of the API, see [Webhooks (v1) (deprecated)](https://developer.revolut.com/docs/api/business#tag-webhooks-v1-deprec
  name: Revolut Webhooks (v2) API
  slug: revolut-webhooks-v2-api
- baseURL: https://partner.wallet.revolut.com
  baseurl_source: declared
  description: Pre-release preview (2026-07-01) of the Revolut Wallet Partner API, which lets onboarded partners create and manage passes in Revolut Wallet. Published by Revolut in the revolut-engineering/revolut-op
  name: Revolut Wallet Partner API
  slug: revolut-wallet-partner-api
artifact_total: 271
asyncapis:
- description: ''
  name: Revolut Webhooks
  slug: revolut-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Business Accounting API
  slug: open-revolut-accounting-api
- collection_type: open
  name: Business Accounting Accounting categories API
  slug: open-revolut-accounting-categories-api
- collection_type: open
  name: Business Accounting Accounts API
  slug: open-revolut-accounts-api
- collection_type: open
  name: Business Accounting Apple Pay merchant registration API
  slug: open-revolut-apple-pay-merchant-registration-api
- collection_type: open
  name: Business Accounting Applications API
  slug: open-revolut-applications-api
- collection_type: open
  name: Business Accounting Balance API
  slug: open-revolut-balance-api
- collection_type: open
  name: Business Accounting Card invitations API
  slug: open-revolut-card-invitations-api
- collection_type: open
  name: Business Accounting Cards API
  slug: open-revolut-cards-api
- collection_type: open
  name: Business Accounting Configuration API
  slug: open-revolut-configuration-api
- collection_type: open
  name: Business Accounting Counterparties API
  slug: open-revolut-counterparties-api
- collection_type: open
  name: Business Accounting Customers API
  slug: open-revolut-customers-api
- collection_type: open
  name: Business Accounting Disputes API
  slug: open-revolut-disputes-api
- collection_type: open
  name: Business Accounting Domestic payment API
  slug: open-revolut-domestic-payment-api
- collection_type: open
  name: Business Accounting Domestic scheduled payment API
  slug: open-revolut-domestic-scheduled-payment-api
- collection_type: open
  name: Business Accounting Domestic standing order API
  slug: open-revolut-domestic-standing-order-api
- collection_type: open
  name: Business Accounting Draft payment API
  slug: open-revolut-draft-payment-api
- collection_type: open
  name: Business Accounting Expenses API
  slug: open-revolut-expenses-api
- collection_type: open
  name: Business Accounting File Payment API
  slug: open-revolut-file-payment-api
- collection_type: open
  name: Business Accounting Foreign exchange API
  slug: open-revolut-foreign-exchange-api
- collection_type: open
  name: Business Accounting International payment API
  slug: open-revolut-international-payment-api
- collection_type: open
  name: Business Accounting International scheduled payment API
  slug: open-revolut-international-scheduled-payment-api
- collection_type: open
  name: Business Accounting International standing order API
  slug: open-revolut-international-standing-order-api
- collection_type: open
  name: Business Accounting Labels API
  slug: open-revolut-labels-api
- collection_type: open
  name: Business Accounting Locations API
  slug: open-revolut-locations-api
- collection_type: open
  name: Business Accounting Market Data API
  slug: open-revolut-market-data-api
- collection_type: open
  name: Business Accounting Orders API
  slug: open-revolut-orders-api
- collection_type: open
  name: Business Accounting Other API
  slug: open-revolut-other-api
- collection_type: open
  name: Business Accounting Partners API
  slug: open-revolut-partners-api
- collection_type: open
  name: Business Accounting Payment drafts API
  slug: open-revolut-payment-drafts-api
- collection_type: open
  name: Business Accounting Payment intents API
  slug: open-revolut-payment-intents-api
- collection_type: open
  name: Business Accounting Payments API
  slug: open-revolut-payments-api
- collection_type: open
  name: Business Accounting Payout links API
  slug: open-revolut-payout-links-api
- collection_type: open
  name: Business Accounting Payouts API
  slug: open-revolut-payouts-api
- collection_type: open
  name: Business Accounting Public Market Data API
  slug: open-revolut-public-market-data-api
- collection_type: open
  name: Business Accounting Report runs API
  slug: open-revolut-report-runs-api
- collection_type: open
  name: Business Accounting Simulations API
  slug: open-revolut-simulations-api
- collection_type: open
  name: Business Accounting Subscriptions API
  slug: open-revolut-subscriptions-api
- collection_type: open
  name: Business Accounting Tax rates API
  slug: open-revolut-tax-rates-api
- collection_type: open
  name: Business Accounting Team members API
  slug: open-revolut-team-members-api
- collection_type: open
  name: Business Accounting Terminals API
  slug: open-revolut-terminals-api
- collection_type: open
  name: Business Accounting Trades API
  slug: open-revolut-trades-api
- collection_type: open
  name: Business Accounting Transactions API
  slug: open-revolut-transactions-api
- collection_type: open
  name: Business Accounting Transfers API
  slug: open-revolut-transfers-api
- collection_type: open
  name: Business Accounting Webhooks API
  slug: open-revolut-webhooks-api
- collection_type: open
  name: Business Accounting Webhooks (v1) (deprecated) API
  slug: open-revolut-webhooks-v1-deprecated-api
- collection_type: open
  name: Business Accounting Webhooks (v2) API
  slug: open-revolut-webhooks-v2-api
common:
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/integrations/revolut-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/revolut-integration-edges.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/rules/revolut-rules.yml
  title: ''
  type: Spectral
  url: rules/revolut-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/json-ld/revolut-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/revolut-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/vocabulary/revolut-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/revolut-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/hosts/revolut-hosts.yml
  title: ''
  type: Hosts
  url: hosts/revolut-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/vendors/revolut-vendors.yml
  title: ''
  type: Vendors
  url: vendors/revolut-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.revolut.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revolut.com/privacy-policy/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/scopes/revolut-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/revolut-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.revolut.com/blog/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/rate-limits/revolut-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/revolut-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.revolut.com/en-US/business/business-account-plans/
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/plans/revolut-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/revolut-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/capabilities/revolut-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/revolut-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/revolut-engineering/revolut-openapi/issues
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/overlays/revolut-business-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/revolut-business-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.revolut.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.revolut.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.revolut.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.revolut.com/docs/guides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revolut-engineering
- group: company
  title: ''
  type: Website
  url: https://www.revolut.com/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/revolut-engineering/revolut-openapi
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/authentication/revolut-authentication.yml
  title: ''
  type: Authentication
  url: authentication/revolut-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/conventions/revolut-conventions.yml
  title: ''
  type: Conventions
  url: conventions/revolut-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/conventions/revolut-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/revolut-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/errors/revolut-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/revolut-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/lifecycle/revolut-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/revolut-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/lifecycle/revolut-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/revolut-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/changelog/revolut-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/revolut-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/conformance/revolut-conformance.yml
  title: ''
  type: Conformance
  url: conformance/revolut-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/conformance/revolut-conformance.yml
  title: ''
  type: Compliance
  url: conformance/revolut-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/data-model/revolut-data-model.yml
  title: ''
  type: DataModel
  url: data-model/revolut-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/sandbox/revolut-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/revolut-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/asyncapi/revolut-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/revolut-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/packages/revolut-packages.yml
  title: ''
  type: Packages
  url: packages/revolut-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/packages/revolut-packages.yml
  title: ''
  type: SDKs
  url: packages/revolut-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/mcp/revolut-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/revolut-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/well-known/revolut-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/revolut-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/well-known/revolut-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/revolut-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.revolut.com/responsible-disclosure-program
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/security/revolut-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/revolut-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/security/revolut-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/revolut-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/agentic-access/revolut-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/revolut-agentic-access.yml
created: '2026-07-17'
description: 'Revolut is a global financial technology company providing banking, payments, cards, foreign exchange, savings, and crypto services to retail and business customers. Its developer platform publishes several distinct REST APIs: the Business API (accounts, transfers, payments, counterparties, cards, webhooks), the Merchant API (online card acquiring, orders, captures, refunds, subscriptions), the Open Banking API (UK Open Banking / PSD2 account information and payment initiation, FAPI-secured with detached JWS), the Crypto Ramp API (fiat-to-crypto on/off ramp for partners), and the Revolut X crypto exchange API (balances, orders, trades, market data). Revolut publishes official OpenAPI specifications and Agent Skills on GitHub.'
image: https://assets.revolut.com/assets/revolut-app-icons/Developer.png
json_schemas:
- name: AccountBalance
  property_count: 0
  slug: revolut-account-balance
- name: Account
  property_count: 8
  slug: revolut-account
- name: AccountingCategoryResponse
  property_count: 6
  slug: revolut-accounting-category-response
- name: AllTradesPaginatedResponse
  property_count: 2
  slug: revolut-all-trades-paginated-response
- name: Candle
  property_count: 6
  slug: revolut-candle
- name: CardCreatedResponse
  property_count: 19
  slug: revolut-card-created-response
- name: CardInvitationCreatedResponse
  property_count: 14
  slug: revolut-card-invitation-created-response
- name: CardInvitationResponse
  property_count: 16
  slug: revolut-card-invitation-response
- name: CardInvitationUpdatedResponse
  property_count: 15
  slug: revolut-card-invitation-updated-response
- name: CardReferences
  property_count: 0
  slug: revolut-card-references
- name: CardResponse
  property_count: 20
  slug: revolut-card-response
- name: ClientTrade
  property_count: 16
  slug: revolut-client-trade
- name: Config
  property_count: 6
  slug: revolut-config
- name: CounterpartyCountriesResponse
  property_count: 1
  slug: revolut-counterparty-countries-response
- name: CounterpartyRequirementsResponse
  property_count: 1
  slug: revolut-counterparty-requirements-response
- name: Counterparty
  property_count: 10
  slug: revolut-counterparty
- name: CreateAccountingCategoryRequest
  property_count: 3
  slug: revolut-create-accounting-category-request
- name: CreateCounterpartyRequest
  property_count: 24
  slug: revolut-create-counterparty-request
- name: CreateLabelGroupRequest
  property_count: 2
  slug: revolut-create-label-group-request
- name: CreatePassResult
  property_count: 2
  slug: revolut-create-pass-result
- name: CreatePaymentDraftRequest
  property_count: 3
  slug: revolut-create-payment-draft-request
- name: CreateTaxRateRequest
  property_count: 0
  slug: revolut-create-tax-rate-request
- name: CreateWebhookRequest
  property_count: 2
  slug: revolut-create-webhook-request
- name: CurrenciesResponse
  property_count: 0
  slug: revolut-currencies-response
- name: CurrencyPairsResponse
  property_count: 0
  slug: revolut-currency-pairs-response
- name: Currency
  property_count: 0
  slug: revolut-currency
- name: Customer
  property_count: 6
  slug: revolut-customer-created
- name: Customer-Payment-Methods-v2
  property_count: 1
  slug: revolut-customer-payment-methods-v2
- name: Customer update
  property_count: 4
  slug: revolut-customer-update-v2
- name: Customer
  property_count: 7
  slug: revolut-customer-v3
- name: Dispute-Challenge
  property_count: 3
  slug: revolut-dispute-challenge
- name: Dispute-Evidence-Creation
  property_count: 1
  slug: revolut-dispute-evidence-creation
- name: Dispute-Evidence
  property_count: 1
  slug: revolut-dispute-evidence
- name: Dispute
  property_count: 11
  slug: revolut-dispute
- name: Disputes
  property_count: 0
  slug: revolut-disputes
- name: DraftPaymentListResponse
  property_count: 2
  slug: revolut-draft-payment-list-response
- name: DraftPaymentResponse
  property_count: 4
  slug: revolut-draft-payment-response
- name: EmptyBody
  property_count: 0
  slug: revolut-empty-body
- name: ExchangeRateResponse
  property_count: 5
  slug: revolut-exchange-rate-response
- name: ExchangeReasons
  property_count: 0
  slug: revolut-exchange-reasons
- name: ExchangeRequest
  property_count: 5
  slug: revolut-exchange-request
- name: ExchangeResponse
  property_count: 6
  slug: revolut-exchange-response
- name: Expense
  property_count: 14
  slug: revolut-expense
- name: GetApplicationResponse
  property_count: 9
  slug: revolut-get-application-response
- name: IndicativeQuoteRequest
  property_count: 7
  slug: revolut-indicative-quote-request
- name: IndicativeQuoteResponse
  property_count: 7
  slug: revolut-indicative-quote-response
- name: LabelGroupResponse
  property_count: 4
  slug: revolut-label-group-response
- name: LabelResponse
  property_count: 4
  slug: revolut-label-response
- name: LastTrades
  property_count: 2
  slug: revolut-last-trades
- name: Location-Creation
  property_count: 0
  slug: revolut-location-creation
- name: Location
  property_count: 0
  slug: revolut-location
- name: Location-Update
  property_count: 0
  slug: revolut-location-update
- name: MerchantControlsSchema
  property_count: 2
  slug: revolut-merchant-controls-schema
- name: OBReadAccount3
  property_count: 3
  slug: revolut-obread-account3
- name: OBReadBalance1
  property_count: 3
  slug: revolut-obread-balance1
- name: OBReadBeneficiary3
  property_count: 3
  slug: revolut-obread-beneficiary3
- name: OBReadConsentResponse1
  property_count: 4
  slug: revolut-obread-consent-response1
- name: OBReadConsent1
  property_count: 2
  slug: revolut-obread-consent1
- name: OBReadDirectDebit1
  property_count: 3
  slug: revolut-obread-direct-debit1
- name: OBReadStandingOrder4
  property_count: 3
  slug: revolut-obread-standing-order4
- name: OBReadTransaction4
  property_count: 3
  slug: revolut-obread-transaction4
- name: OBReportFileResponse
  property_count: 1
  slug: revolut-obreport-file-response
- name: OBWriteDomesticConsentResponse2
  property_count: 4
  slug: revolut-obwrite-domestic-consent-response2
- name: OBWriteDomesticConsent2
  property_count: 2
  slug: revolut-obwrite-domestic-consent2
- name: OBWriteDomesticResponse2
  property_count: 3
  slug: revolut-obwrite-domestic-response2
- name: OBWriteDomesticScheduledConsentResponse2
  property_count: 4
  slug: revolut-obwrite-domestic-scheduled-consent-response2
- name: OBWriteDomesticScheduledConsent2
  property_count: 2
  slug: revolut-obwrite-domestic-scheduled-consent2
- name: OBWriteDomesticScheduledResponse2
  property_count: 3
  slug: revolut-obwrite-domestic-scheduled-response2
- name: OBWriteDomesticScheduled2
  property_count: 2
  slug: revolut-obwrite-domestic-scheduled2
- name: OBWriteDomesticStandingOrderConsentResponse2
  property_count: 4
  slug: revolut-obwrite-domestic-standing-order-consent-response2
- name: OBWriteDomesticStandingOrderConsent2
  property_count: 2
  slug: revolut-obwrite-domestic-standing-order-consent2
- name: OBWriteDomesticStandingOrderResponse2
  property_count: 3
  slug: revolut-obwrite-domestic-standing-order-response2
- name: OBWriteDomesticStandingOrder2
  property_count: 2
  slug: revolut-obwrite-domestic-standing-order2
- name: OBWriteDomestic2
  property_count: 2
  slug: revolut-obwrite-domestic2
- name: OBWriteFileConsentResponse2
  property_count: 3
  slug: revolut-obwrite-file-consent-response2
- name: OBWriteFileConsent2
  property_count: 1
  slug: revolut-obwrite-file-consent2
- name: OBWriteFileResponse2
  property_count: 3
  slug: revolut-obwrite-file-response2
- name: OBWriteFile2
  property_count: 1
  slug: revolut-obwrite-file2
- name: OBWriteFundsConfirmationResponse1
  property_count: 3
  slug: revolut-obwrite-funds-confirmation-response1
- name: OBWriteInternationalConsentResponse2
  property_count: 4
  slug: revolut-obwrite-international-consent-response2
- name: OBWriteInternationalConsent2
  property_count: 2
  slug: revolut-obwrite-international-consent2
- name: OBWriteInternationalResponse2
  property_count: 3
  slug: revolut-obwrite-international-response2
- name: OBWriteInternationalScheduledConsentResponse2
  property_count: 4
  slug: revolut-obwrite-international-scheduled-consent-response2
- name: OBWriteInternationalScheduledConsent2
  property_count: 2
  slug: revolut-obwrite-international-scheduled-consent2
- name: OBWriteInternationalScheduledResponse2
  property_count: 3
  slug: revolut-obwrite-international-scheduled-response2
- name: OBWriteInternationalScheduled2
  property_count: 2
  slug: revolut-obwrite-international-scheduled2
- name: OBWriteInternationalStandingOrderConsentResponse2
  property_count: 4
  slug: revolut-obwrite-international-standing-order-consent-response2
- name: OBWriteInternationalStandingOrderConsent2
  property_count: 2
  slug: revolut-obwrite-international-standing-order-consent2
- name: OBWriteInternationalStandingOrderResponse2
  property_count: 3
  slug: revolut-obwrite-international-standing-order-response2
- name: OBWriteInternationalStandingOrder2
  property_count: 2
  slug: revolut-obwrite-international-standing-order2
- name: OBWriteInternational2
  property_count: 2
  slug: revolut-obwrite-international2
- name: OrderBookPublic
  property_count: 2
  slug: revolut-order-book-public
- name: OrderBook
  property_count: 2
  slug: revolut-order-book
- name: Order-Creation-v7
  property_count: 19
  slug: revolut-order-creation-v7
- name: OrderDetails
  property_count: 26
  slug: revolut-order-details
- name: OrderReplacementRequest
  property_count: 6
  slug: revolut-order-replacement-request
- name: Order
  property_count: 14
  slug: revolut-order
- name: Order-Update-v7
  property_count: 17
  slug: revolut-order-update-v7
- name: Order v7
  property_count: 31
  slug: revolut-order-v7
- name: Orders
  property_count: 0
  slug: revolut-orders
- name: PageToken
  property_count: 0
  slug: revolut-page-token
- name: PassCreateEnvelope
  property_count: 0
  slug: revolut-pass-create-envelope
- name: PassUpdateEnvelope
  property_count: 0
  slug: revolut-pass-update-envelope
- name: PaymentDraftResponse
  property_count: 4
  slug: revolut-payment-draft-response
- name: PaymentDraftsResponse
  property_count: 1
  slug: revolut-payment-drafts-response
- name: Payment Intent creation
  property_count: 2
  slug: revolut-payment-intent-creation
- name: Payment Intent
  property_count: 9
  slug: revolut-payment-intent
- name: Payment method update
  property_count: 1
  slug: revolut-payment-method-update
- name: Payment method
  property_count: 0
  slug: revolut-payment-method-v4
- name: PaymentRequest
  property_count: 7
  slug: revolut-payment-request
- name: Payment-Retrieval
  property_count: 9
  slug: revolut-payment-retrieval
- name: Payment-Retrieval-v3
  property_count: 19
  slug: revolut-payment-retrieval-v3
- name: PayoutLinkInitialProps
  property_count: 15
  slug: revolut-payout-link-initial-props
- name: Payout
  property_count: 6
  slug: revolut-payout
- name: PrivateTradesPaginatedResponse
  property_count: 2
  slug: revolut-private-trades-paginated-response
- name: Quote
  property_count: 4
  slug: revolut-quote
- name: RampRedirectUrl
  property_count: 1
  slug: revolut-ramp-redirect-url
- name: RegisterApplicationResponse
  property_count: 14
  slug: revolut-register-application-response
- name: Custom report CSV
  property_count: 64
  slug: revolut-report-run-csv-custom
- name: IC++ fee breakdown report CSV
  property_count: 19
  slug: revolut-report-run-csv-icpp
- name: Payments report CSV
  property_count: 26
  slug: revolut-report-run-csv-payments
- name: Payout statement report CSV
  property_count: 31
  slug: revolut-report-run-csv-payout
- name: Settlement report CSV
  property_count: 24
  slug: revolut-report-run-csv-settlement
- name: ReportRunDetails
  property_count: 3
  slug: revolut-report-run
- name: Role
  property_count: 4
  slug: revolut-role
- name: Saved-Payment-Method
  property_count: 1
  slug: revolut-saved-payment-method
- name: SpendingLimitsSchema
  property_count: 7
  slug: revolut-spending-limits-schema
- name: SpendingPeriodSchema
  property_count: 3
  slug: revolut-spending-period-schema
- name: Subscription-Change-Plan
  property_count: 4
  slug: revolut-subscription-change-plan
- name: Subscription-Cycle
  property_count: 13
  slug: revolut-subscription-cycle
- name: Subscription-Plan
  property_count: 7
  slug: revolut-subscription-plan
- name: Subscription
  property_count: 16
  slug: revolut-subscription
- name: Subscription-Usage-Creation
  property_count: 5
  slug: revolut-subscription-usage-creation
- name: Subscription-Usage
  property_count: 9
  slug: revolut-subscription-usage
- name: SynchronousWebhookCreation
  property_count: 3
  slug: revolut-synchronous-webhook-creation
- name: SynchronousWebhook
  property_count: 5
  slug: revolut-synchronous-webhook
- name: TaxRateResponse
  property_count: 5
  slug: revolut-tax-rate-response
- name: TeamMember
  property_count: 8
  slug: revolut-team-member
- name: TemplateCreate
  property_count: 11
  slug: revolut-template-create
- name: Template
  property_count: 16
  slug: revolut-template
- name: TemplateUpdate
  property_count: 11
  slug: revolut-template-update
- name: Terminals response
  property_count: 1
  slug: revolut-terminals-response
- name: TickersResponse
  property_count: 2
  slug: revolut-tickers-response
- name: TransactionPaymentRequest
  property_count: 10
  slug: revolut-transaction-payment-request
- name: Transaction
  property_count: 14
  slug: revolut-transaction
- name: Transactions
  property_count: 0
  slug: revolut-transactions
- name: TransferRequest
  property_count: 6
  slug: revolut-transfer-request
- name: TransferResponse
  property_count: 4
  slug: revolut-transfer-response
- name: UpdateAccountingCategoryRequest
  property_count: 3
  slug: revolut-update-accounting-category-request
- name: UpdateDraftPaymentRequest
  property_count: 6
  slug: revolut-update-draft-payment-request
- name: UpdateLabelGroupRequest
  property_count: 1
  slug: revolut-update-label-group-request
- name: UpdateLabelRequest
  property_count: 1
  slug: revolut-update-label-request
- name: UpdatePaymentDraftRequest
  property_count: 2
  slug: revolut-update-payment-draft-request
- name: UpdateTaxRateRequest
  property_count: 1
  slug: revolut-update-tax-rate-request
- name: UpdateWebhookRequest
  property_count: 2
  slug: revolut-update-webhook-request
- name: ValidateAccountNameRequest
  property_count: 0
  slug: revolut-validate-account-name-request
- name: ValidateAccountNameResponse
  property_count: 0
  slug: revolut-validate-account-name-response
- name: WebhookCreateRequest
  property_count: 2
  slug: revolut-webhook-create-request
- name: Webhook
  property_count: 4
  slug: revolut-webhook
- name: WebhookSigningSecretRotateRequest
  property_count: 1
  slug: revolut-webhook-signing-secret-rotate-request
- name: WebhookUpdateRequest
  property_count: 2
  slug: revolut-webhook-update-request
- name: Webhook update
  property_count: 2
  slug: revolut-webhook-update
- name: Webhook-v1
  property_count: 1
  slug: revolut-webhook-v1
- name: Webhook-v2-basic
  property_count: 3
  slug: revolut-webhook-v2-basic
- name: Webhook
  property_count: 4
  slug: revolut-webhook-v2
- name: Webhooks
  property_count: 0
  slug: revolut-webhooks
jsonld:
- class_count: 120
  name: Revolut Context
  property_count: 201
  slug: revolut-context
layout: provider
modified: '2026-10-06'
name: Revolut
nav: Providers
network: true
overview: 'Revolut publishes 47 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounting API, Accounting categories API, Accounts API, and 44 more. Tagged areas include Company, Fintech, Payments, Banking, and Open Banking.


  The Revolut catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Revolut''s developer surface includes support, engineering blog, pricing, documentation, API reference, getting-started guide, authentication, and 38 more developer resources.'
plans:
- name: Revolut Plans Pricing
  plan_count: 4
  slug: revolut-plans-pricing
- name: Revolut Price Estimates
  plan_count: 1
  slug: revolut-price-estimates
random_paper: 15
rate_limits:
- limit_count: 0
  name: Revolut Rate Limits
  slug: revolut-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Revolut API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 3
  slug: revolut-rules
scopes:
- name: Revolut Scopes
  scope_count: 3
  slug: revolut-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: exemplar
  composite: 70.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.7
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 77.9
    developer_ergonomics: 75.0
    discoverability: 71.4
    operational_transparency: 44.7
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 47
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 59.1
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/revolut/refs/heads/main/screenshots/revolut-2026-08-17T081548.png
security:
- kind: authentication
  name: Revolut Authentication
  slug: revolut-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Revolut Domain Security
  slug: revolut-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Revolut Vulnerability Disclosure
  slug: revolut-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: revolut
tags:
- Company
- Fintech
- Payments
- Banking
- Open Banking
- Merchant Acquiring
- Cryptocurrency
- Cards
- Consumer Banking
website: https://www.revolut.com/
---
