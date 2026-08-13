---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 70.7
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 119
  human_in_the_loop: 1
  name: Revolut Agentic Access
  operation_count: 237
  slug: revolut-agentic-access
  summary_line: 237 operations · 119 acting · 1 human-in-the-loop
api_count: 46
apis:
- description: Manage [accounting settings](https://business.revolut.com/settings/accounting) for your business that can be assigned to your financial records such as [expenses](https://developer.revolut.com/docs/gu
  name: Revolut Accounting API
  slug: revolut-accounting-api
- description: Manage accounting categories for your business. You can create, retrieve, and delete accounting categories that can be assigned to your financial records such as [expenses](https://developer.revolut.c
  name: Revolut Accounting categories API
  slug: revolut-accounting-categories-api
- description: 'Get the balances, full banking details, and other details of your business accounts. For more information, see the guides: [Get your account details](https://developer.revolut.com/docs/guides/manage-a'
  name: Revolut Accounts API
  slug: revolut-accounts-api
- description: 'Operations for managing a merchant''s domain registration and configuration with Apple for integration of Apple Pay via Revolut. This includes initiating domain validation with Apple, a necessary step '
  name: Revolut Apple Pay merchant registration API
  slug: revolut-apple-pay-merchant-registration-api
- description: 'These endpoints let you manage your applications. Applications can also be created in the [Developer Portal](https://developer.revolut.com/portal/). For more information, see: - [Register your applica'
  name: Revolut Applications API
  slug: revolut-applications-api
- description: Get your Revolut X crypto exchange balances, including both crypto and fiat.
  name: Revolut Balance API
  slug: revolut-balance-api
- description: Use card invitations to pre-create cards for [team members](https://developer.revolut.com/docs/guides/manage-accounts/teams/manage-team-members) who have not yet onboarded. Once the team member comple
  name: Revolut Card invitations API
  slug: revolut-card-invitations-api
- description: Manage cards issued for your business, freeze, unfreeze, lock, unlock, terminate and update card settings, such as spending limits and merchant controls. :::note - This feature is not available in San
  name: Revolut Cards API
  slug: revolut-cards-api
- description: Get Revolut X configuration for traded assets and pairs.
  name: Revolut Configuration API
  slug: revolut-configuration-api
- description: Manage counterparties that you intend to transact with. Request and response examples can vary based on the account provider's location and type of the counterparty. For more information, see the guid
  name: Revolut Counterparties API
  slug: revolut-counterparties-api
- description: The Customers resource in the Merchant API is a pivotal tool for tracking and managing customer-related transactions within your e-commerce or retail platform. This resource provides a structured appr
  name: Revolut Customers API
  slug: revolut-customers-api
- description: Endpoints that allow merchants to view customer payment disputes. It provides a robust framework with high-level states (e.g., `won`, `lost`, `needs_response`, `under_review`) and detailed substates (
  name: Revolut Disputes API
  slug: revolut-disputes-api
- description: '*Domestic payments*, which you can use for local payments in the local currency of the user. :::note Revolut supports only GBP as local in the UK and EUR in Single Euro Payments Area (SEPA) countries.'
  name: Revolut Domestic payment API
  slug: revolut-domestic-payment-api
- description: '*Domestic scheduled payments*, which you can use for local payments in the local currency of the user. :::note Revolut supports only GBP as local in the UK and EUR in Single Euro Payments Area (SEPA) '
  name: Revolut Domestic scheduled payment API
  slug: revolut-domestic-scheduled-payment-api
- description: '*Domestic standing orders*, which you can use for local payments in the local currency of the user. :::note Revolut supports only GBP as local in the UK and EUR in Single Euro Payments Area (SEPA) cou'
  name: Revolut Domestic standing order API
  slug: revolut-domestic-standing-order-api
- description: 'You can create a draft payment to initiate a payment on behalf of a user, and request the approval for the draft payment in the user account. Then, you can retrieve or delete a draft payment. :::note '
  name: Revolut Draft payment API
  slug: revolut-draft-payment-api
- description: 'Get the list of all the expenses, or use the filters to narrow down the results. You can also get a specific expense, or get a receipt related to an expense by providing their respective IDs. :::note '
  name: Revolut Expenses API
  slug: revolut-expenses-api
- description: The File Payment API from Revolut — 6 operation(s) for file payment.
  name: Revolut File Payment API
  slug: revolut-file-payment-api
- description: 'Retrieve information on exchange rates between currencies, buy and sell currencies. For more information, see the guides: [Exchange money](https://developer.revolut.com/docs/guides/manage-accounts/exc'
  name: Revolut Foreign exchange API
  slug: revolut-foreign-exchange-api
- description: '*International payments*, which you can use for international SWIFT payments in all currencies that Revolut supports. As a regulated third party provider, you can use the provided endpoints to initiat'
  name: Revolut International payment API
  slug: revolut-international-payment-api
- description: '*International scheduled payments*, which you can use for international SWIFT payments in all currencies that Revolut supports. As a regulated third party provider, you can use the provided endpoints '
  name: Revolut International scheduled payment API
  slug: revolut-international-scheduled-payment-api
- description: '*International standing orders*, which you can use for international SWIFT payments in all currencies that Revolut supports. As a regulated third party provider, you can use the provided endpoints to '
  name: Revolut International standing order API
  slug: revolut-international-standing-order-api
- description: Manage accounting labels and label groups for your business. Create, retrieve, update, and delete label groups and labels that can be added to your financial records such as [expenses](https://develop
  name: Revolut Labels API
  slug: revolut-labels-api
- description: The Locations API is designed to help merchants manage multiple points of sale, including both **online storefronts** and **physical stores**. Registering locations lets you differentiate and group yo
  name: Revolut Locations API
  slug: revolut-locations-api
- description: Retrieve real-time and historical market data for Revolut X.
  name: Revolut Market Data API
  slug: revolut-market-data-api
- description: The Orders resource in the Merchant API offers a comprehensive solution for managing the lifecycle of orders within your e-commerce or retail platform. Designed to streamline order processing, this re
  name: Revolut Orders API
  slug: revolut-orders-api
- description: Other operations that can be done with the Merchant API.
  name: Revolut Other API
  slug: revolut-other-api
- description: 'The **Partners** endpoints let you poll different exchange rates, display them on your website and compare them with other providers. For more details, see the guides: [Leverage the Crypto Ramp API](h'
  name: Revolut Partners API
  slug: revolut-partners-api
- description: 'Payment drafts let you prepare payments for future processing, prepare payments that require an approval, or prepare bulk or scheduled payments. Simply create a draft, and when you''re ready, [send it '
  name: Revolut Payment drafts API
  slug: revolut-payment-drafts-api
- description: Operations for managing payment intents in the push payments to Revolut Terminal flow. A **payment intent** represents the intention to complete payment for a specific order on a specific Revolut Term
  name: Revolut Payment intents API
  slug: revolut-payment-intents-api
- description: Payment operations enable you to initiate payments, or track payment status transitions. You can use the ID of the payment to retrieve information about a specific payment. :::info For more informatio
  name: Revolut Payments API
  slug: revolut-payments-api
- description: Use payout links to send money without having to request full banking details of the recipient. The recipient must claim the money before the link expires. :::note This feature is available in the UK,
  name: Revolut Payout links API
  slug: revolut-payout-links-api
- description: 'Endpoints for retrieving information about payouts, allowing merchants to access details of funds withdrawn from their Merchant account to external bank accounts. Merchants can use these endpoints to '
  name: Revolut Payouts API
  slug: revolut-payouts-api
- description: Get Revolut X real time public market data.
  name: Revolut Public Market Data API
  slug: revolut-public-market-data-api
- description: 'Use **Report runs** operations to generate CSV reports of your Merchant account transactions. Choose from the following report types based on your use case: | Report type | Description | | -----------'
  name: Revolut Report runs API
  slug: revolut-report-runs-api
- description: 'The Simulations API is only available in the Sandbox environment. It lets you simulate certain events that are otherwise only possible in the production environment, such as your account''s top-up and '
  name: Revolut Simulations API
  slug: revolut-simulations-api
- description: The Subscriptions API provides a complete solution for creating and managing recurring billing for your customers. You can automatically charge customers on flexible billing cycles, manage sophisticat
  name: Revolut Subscriptions API
  slug: revolut-subscriptions-api
- description: Manage tax rates for your business. Create, retrieve, update, and delete tax rates that can be assigned to your financial records such as [expenses](https://developer.revolut.com/docs/guides/manage-ac
  name: Revolut Tax rates API
  slug: revolut-tax-rates-api
- description: 'Retrieve information on existing team members of your organisation, delete team members, and invite new members. For more information, see the guides: [Manage team members](https://developer.revolut.c'
  name: Revolut Team members API
  slug: revolut-team-members-api
- description: Operations for managing Revolut Terminal devices and push payment integrations with Point of Sale (POS) systems. The Terminals API enables POS software providers to integrate with Revolut Terminal dev
  name: Revolut Terminals API
  slug: revolut-terminals-api
- description: 'Retrieve Revolut X trade history and execution details: view public market trades or your specific private trade executions (fills).'
  name: Revolut Trades API
  slug: revolut-trades-api
- description: 'Get the details of your transactions. :::note An incoming or outgoing payment is represented as a transaction. ::: For more information, see the guides: [Retrieve transactions](https://developer.revol'
  name: Revolut Transactions API
  slug: revolut-transactions-api
- description: 'Move funds in the same currency between accounts of your business, or make payments to your counterparties. For more details, see the guides: [Send money](https://developer.revolut.com/docs/guides/man'
  name: Revolut Transfers API
  slug: revolut-transfers-api
- description: A webhook (also called a web callback) allows your system to receive an event from Ramp immediately after it happens. With the **Webhooks** endpoints, you can create, update, delete, and retrieve webh
  name: Revolut Webhooks API
  slug: revolut-webhooks-api
- description: ':::warning This is the v1 of the Webhooks API. This version is deprecated. For the latest version of the API, see [Webhooks (v2)](https://developer.revolut.com/docs/api/business#tag-webhooks-v2). ::: '
  name: Revolut Webhooks (v1) (deprecated) API
  slug: revolut-webhooks-v1-deprecated-api
- description: :::note This is the latest version of the Webhooks API, v2. For the previous version of the API, see [Webhooks (v1) (deprecated)](https://developer.revolut.com/docs/api/business#tag-webhooks-v1-deprec
  name: Revolut Webhooks (v2) API
  slug: revolut-webhooks-v2-api
artifact_total: 52
asyncapis:
- description: ''
  name: Revolut Webhooks
  slug: revolut-webhooks
common:
- group: other
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
  title: ''
  type: Authentication
  url: authentication/revolut-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/revolut-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/revolut-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/revolut-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revolut-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/revolut-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/revolut-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/revolut-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/revolut-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/revolut-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/revolut-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/revolut-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/revolut-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/revolut-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/revolut-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revolut-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/revolut-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/revolut-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.revolut.com/responsible-disclosure-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/revolut-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revolut-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revolut-agentic-access.yml
created: '2026-07-17'
description: 'Revolut is a global financial technology company providing banking, payments, cards, foreign exchange, savings, and crypto services to retail and business customers. Its developer platform publishes several distinct REST APIs: the Business API (accounts, transfers, payments, counterparties, cards, webhooks), the Merchant API (online card acquiring, orders, captures, refunds, subscriptions), the Open Banking API (UK Open Banking / PSD2 account information and payment initiation, FAPI-secured with detached JWS), the Crypto Ramp API (fiat-to-crypto on/off ramp for partners), and the Revolut X crypto exchange API (balances, orders, trades, market data). Revolut publishes official OpenAPI specifications and Agent Skills on GitHub.'
image: https://assets.revolut.com/assets/revolut-app-icons/Developer.png
layout: provider
mcp_servers:
- description: ''
  name: revolut-mcp.yml
  slug: revolut-mcpyml
modified: '2026-07-21'
name: Revolut
nav: Providers
network: true
overview: 'Revolut publishes 46 APIs on the [APIs.io](https://apis.io/) network, including Accounting API, Accounting categories API, Accounts API, and 43 more. Tagged areas include Company, Fintech, Payments, Banking, and Open Banking.


  The Revolut catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Revolut''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, and 25 more developer resources.'
random_paper: 65
score:
  band: developing
  composite: 48.6
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 73.4
    developer_ergonomics: 67.4
    discoverability: 74.1
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 48.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 46
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
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
website: https://www.revolut.com/
---
