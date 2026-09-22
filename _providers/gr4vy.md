---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 148
  human_in_the_loop: 4
  name: Gr4Vy Agentic Access
  operation_count: 263
  slug: gr4vy-agentic-access
  summary_line: 263 operations · 148 acting · 4 human-in-the-loop
api_count: 4
apis:
- description: 'Hosted, unauthenticated Model Context Protocol server over the Gr4vy documentation: search, read-only docs filesystem queries and a docs-feedback tool. It does not execute payment operations.'
  name: Gr4vy Docs MCP Server
  slug: gr4vy-docs-mcp
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage and create 3DS scenarios in sandbox.
  name: Gr4vy 3DS scenarios API
  slug: gr4vy-3ds-scenarios-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: An Account Updater is a service provided by credit card issuers (such as banks and financial institutions) to merchants who accept recurring payments from customers. Its primary purpose is to help mer
  name: Gr4vy Account Updater API
  slug: gr4vy-account-updater-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Anti fraud service definitions describe the fields required for a anti fraud service to be configured.
  name: Gr4vy Anti Fraud Service Definitions API
  slug: gr4vy-anti-fraud-service-definitions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, an anti-fraud service represents a configured anti-fraud service provider (`Sift`, `CyberSource`, etc). This third-party services will be used to screen transactions to determine the risk an
  name: Gr4vy Anti-Fraud Services API
  slug: gr4vy-anti-fraud-services-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, an API key pair is used to sign and validate JSON Web Tokens (JWT). JWTs are used as a HTTP `bearer` token to authenticate to the API. For more information please visit our [in-depth authent
  name: Gr4vy API Key Pairs API
  slug: gr4vy-api-key-pairs-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: API Logs provide an historic of 4XX and 5XX errors that happened in the API in the last 24 hours with a 250 result limit.
  name: Gr4vy API Logs API
  slug: gr4vy-api-logs-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Apple Pay payment processing certificates are used by Apple to encrypt Apple Pay tokens. You must register and upload an Apple Pay payment processing certificate if you wish to use Apple Pay with Gr4v
  name: Gr4vy Apple Pay Certificates API
  slug: gr4vy-apple-pay-certificates-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Audit Logs provide an historic record of changes made to your Gr4vy instance.
  name: Gr4vy Audit Logs API
  slug: gr4vy-audit-logs-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: 'In Gr4vy, a buyer represents your customer, the shopper who''s performing a checkout and making a purchase. A buyer can be used by you to: * Display a human readable name (`display_name`) for a buyer i'
  name: Gr4vy Buyers API
  slug: gr4vy-buyers-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Query gift cards for buyers.
  name: Gr4vy Buyers - Gift cards API
  slug: gr4vy-buyers-gift-cards-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Query payment methods for buyers.
  name: Gr4vy Buyers - Payment methods API
  slug: gr4vy-buyers-payment-methods-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage shipping details for buyers.
  name: Gr4vy Buyers - Shipping details API
  slug: gr4vy-buyers-shipping-details-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Endpoints to retrieve details of a card by utilising a BIN lookup table.
  name: Gr4vy Card Details API
  slug: gr4vy-card-details-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Card Scheme definitions provide display information to a card scheme.
  name: Gr4vy Card Scheme Definitions API
  slug: gr4vy-card-scheme-definitions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: A Checkout Session represents the session of a user as they progress through an online checkout.
  name: Gr4vy Checkout Sessions API
  slug: gr4vy-checkout-sessions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Endpoints to retrieve details of various connections such as payment services, digital wallets, and anti-fraud services.
  name: Gr4vy Connection Definitions API
  slug: gr4vy-connection-definitions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Endpoints to retrieve details of configured connections such as payment services, digital wallets, and anti-fraud services.
  name: Gr4vy Connections API
  slug: gr4vy-connections-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, a digital wallet represents a way for a buyer to pay using card details already stored on their device via a digital wallet service such as Apple Pay or Google Pay. The buyer will not have t
  name: Gr4vy Digital Wallets API
  slug: gr4vy-digital-wallets-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Create sessions for digital wallets like Apple Pay and Google Pay.
  name: Gr4vy Digital wallets - Sessions API
  slug: gr4vy-digital-wallets-sessions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage digital wallets like Apple Pay and Google Pay.
  name: Gr4vy Digital wallets - Setup API
  slug: gr4vy-digital-wallets-setup-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, a rule can be created that triggers actions anywhere in the payment flow.
  name: Gr4vy Flow API
  slug: gr4vy-flow-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Gift card service definitions describe the fields required for a gift card service to be configured.
  name: Gr4vy Gift Card Service Definitions API
  slug: gr4vy-gift-card-service-definitions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, a gift card service represents a configured provider for processing gift cards.
  name: Gr4vy Gift Card Services API
  slug: gr4vy-gift-card-services-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, a gift card represents a stored value card that can be used to pay for a transaction.
  name: Gr4vy Gift Cards API
  slug: gr4vy-gift-cards-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Endpoints to retrieve the data used for the Health Dashboard.
  name: Gr4vy Health Dashboard API
  slug: gr4vy-health-dashboard-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Retrieve Insights data.
  name: Gr4vy Insights API
  slug: gr4vy-insights-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage presets for Insights.
  name: Gr4vy Insights - Presets API
  slug: gr4vy-insights-presets-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage 3DS profiles for merchant accounts.
  name: Gr4vy Merchant accounts - 3DS configuration API
  slug: gr4vy-merchant-accounts-3ds-configuration-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, a merchant account represents an individual merchant in an instance. Each instance has one or more merchant accounts, and each merchant account has its own connections, Flow rules, transacti
  name: Gr4vy Merchant Accounts API
  slug: gr4vy-merchant-accounts-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Endpoints to retrieve the data used for the Metrics Explorer.
  name: Gr4vy Metrics Explorer API
  slug: gr4vy-metrics-explorer-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage monitoring and alerting.
  name: Gr4vy Monitoring API
  slug: gr4vy-monitoring-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, payment links allow a merchant to generate a link, send it to a customer via email, SMS, etc, and then have the customer pay without the need for the merchant hosting their own checkout.
  name: Gr4vy Payment Links API
  slug: gr4vy-payment-links-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Payment Method definitions provide display information to a payment method.
  name: Gr4vy Payment Method Definitions API
  slug: gr4vy-payment-method-definitions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: 'In Gr4vy, a payment method represents a way in which a payment can be processed, for example a card, a PayPal account, or a bank account. The payment method API can be used to: * List all the availabl'
  name: Gr4vy Payment Methods API
  slug: gr4vy-payment-methods-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage payment method definitions.
  name: Gr4vy Payment methods - Definitions API
  slug: gr4vy-payment-methods-definitions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage network tokens for stored payment methods.
  name: Gr4vy Payment methods - Network tokens API
  slug: gr4vy-payment-methods-network-tokens-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage payment service tokens for stored payment methods.
  name: Gr4vy Payment methods - Payment service tokens API
  slug: gr4vy-payment-methods-payment-service-tokens-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: 'In Gr4vy, a payment option represents a list of methods (card, PayPal, etc) that are available for a given locale. The payment options API can be used to: * Determine what types of payments can be pro'
  name: Gr4vy Payment Options API
  slug: gr4vy-payment-options-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Payment service definitions describe the fields required for a payment service to be configured.
  name: Gr4vy Payment Service Definitions API
  slug: gr4vy-payment-service-definitions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: 'In Gr4vy, a payment service represents a configured payment provider (Stripe, PayPal, Adyen, etc) for a specific payment type (card, bitcoin, etc) The payment services API can be used to: * Provide Gr'
  name: Gr4vy Payment Services API
  slug: gr4vy-payment-services-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Payouts allow a merchant to send money from one of their own accounts to a third party.
  name: Gr4vy Payouts API
  slug: gr4vy-payouts-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage transaction refunds.
  name: Gr4vy Refunds API
  slug: gr4vy-refunds-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, a report represents the configuration details to extract or dump a set of data into a downloadable CSV file. The data extracted by a report is configured via the reports API where you can sp
  name: Gr4vy Reports API
  slug: gr4vy-reports-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage executions of reports.
  name: Gr4vy Reports - Executions API
  slug: gr4vy-reports-executions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, users can be granted access to specific types of resources and permissions to perform certain actions by being assigned one or more roles.
  name: Gr4vy Roles API
  slug: gr4vy-roles-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: The sessions APIs are used to facilitate user authentication for the Gr4vy dashboard.
  name: Gr4vy Sessions API
  slug: gr4vy-sessions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Endpoints related to the Gr4vy tokenization service.
  name: Gr4vy Tokens API
  slug: gr4vy-tokens-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Read Flow actions triggered for a transaction.
  name: Gr4vy Transactions - Actions API
  slug: gr4vy-transactions-actions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: 'In Gr4vy, a transaction represents a payment in any state, either before it is authorized, once it is captured, or after it has been refunded. The transactions API can be used to: - Authorize, capture'
  name: Gr4vy Transactions API
  slug: gr4vy-transactions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Read transaction capture data.
  name: Gr4vy Transactions - Captures API
  slug: gr4vy-transactions-captures-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Read transaction chargeback reversal data.
  name: Gr4vy Transactions - Chargeback reversals API
  slug: gr4vy-transactions-chargeback-reversals-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Read transaction chargeback data.
  name: Gr4vy Transactions - Chargebacks API
  slug: gr4vy-transactions-chargebacks-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Read transaction refund settlement data.
  name: Gr4vy Transactions - Refund settlements API
  slug: gr4vy-transactions-refund-settlements-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Manage transaction session data.
  name: Gr4vy Transactions - Sessions API
  slug: gr4vy-transactions-sessions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Read transaction settlement data.
  name: Gr4vy Transactions - Settlements API
  slug: gr4vy-transactions-settlements-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: In Gr4vy, a user represents an employee of the merchant with access to the dashboard.
  name: Gr4vy Users API
  slug: gr4vy-users-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Vault Forwarding is a way to perform requests where, provided a template, Gr4vy will evaluate it to inject PCI data and forward it to third party services that have been vetted to receive such data.
  name: Gr4vy Vault Forward API
  slug: gr4vy-vault-forward-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: A Vault Forward Configuration represents a third party service that is currently enabled to send requests containing PCI data.
  name: Gr4vy Vault Forward Configurations API
  slug: gr4vy-vault-forward-configurations-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Vault Forward definitions describe a third party service that has been vetted to receive requests containing PCI data.
  name: Gr4vy Vault Forward Definitions API
  slug: gr4vy-vault-forward-definitions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Endpoints related to the management of subscriptions for endpoints to receive webhooks.
  name: Gr4vy Webhook subscriptions API
  slug: gr4vy-webhook-subscriptions-api
- baseURL: https://api.{id}.gr4vy.app
  baseurl_source: declared
  description: Endpoints related to webhooks to integrate Gr4vy with payment services webhooks functionality.
  name: Gr4vy Webhooks API
  slug: gr4vy-webhooks-api
artifact_total: 70
asyncapis:
- description: ''
  name: Gr4Vy Webhooks
  slug: gr4vy-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/agentic-access/gr4vy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gr4vy-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/llms/gr4vy-website-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gr4vy-website-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/overlays/gr4vy-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gr4vy-openapi-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/security/gr4vy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gr4vy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gr4vy.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gr4vy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gr4vy.com/guides/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gr4vy.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.gr4vy.com/guides/get-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/authentication/gr4vy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gr4vy-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/scopes/gr4vy-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/gr4vy-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/packages/gr4vy-packages.yml
  title: ''
  type: Packages
  url: packages/gr4vy-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/packages/gr4vy-packages.yml
  title: ''
  type: SDKs
  url: packages/gr4vy-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/cli/gr4vy-cli.yml
  title: ''
  type: CLI
  url: cli/gr4vy-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/components/gr4vy-components.yml
  title: ''
  type: Components
  url: components/gr4vy-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/well-known/gr4vy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gr4vy-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/a2a/gr4vy-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gr4vy-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/llms/gr4vy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gr4vy-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.gr4vy.com/llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/conformance/gr4vy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gr4vy-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://gr4vy.com/regulation-and-compliance/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/lifecycle/gr4vy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gr4vy-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/lifecycle/gr4vy-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/gr4vy-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gr4vy.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/changelog/gr4vy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gr4vy-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.gr4vy.com/updates
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/plans/gr4vy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gr4vy-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gr4vy/refs/heads/main/rate-limits/gr4vy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gr4vy-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://gr4vy.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://gr4vy.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gr4vy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gr4vy.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gr4vy.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gr4vy
created: '2026-09-20'
description: Gr4vy is a cloud-native payment orchestration platform delivered as dedicated, per-merchant infrastructure. A single REST API and a PCI DSS Level 1 vault connect merchants and platforms to hundreds of payment services, payment methods, anti-fraud providers, digital wallets and gift-card services, with no-code Flow routing rules, network tokens, 3-D Secure, payouts, payment links, reporting and webhooks. Gr4vy publishes an OpenAPI 3.1 contract, Speakeasy-generated server SDKs in six languages, mobile and web checkout components (Embed, Secure Fields), a native CLI, a Postman collection, a docs MCP server, an A2A agent card and an Agent Skill.
image: https://avatars.githubusercontent.com/u/17150969
layout: provider
mcp_servers:
- description: Gr4vy serves a hosted, unauthenticated documentation MCP server (Mintlify-hosted) on its docs host. It exposes search and read-only filesystem retrieval over the published docs plus a feedback tool; i
  name: Gr4vy
  slug: gr4vy
modified: '2026-09-20'
name: Gr4vy
nav: Providers
network: true
overview: 'Gr4vy publishes 61 APIs on the [APIs.io](https://apis.io/) network, including 3DS scenarios API, Account Updater API, Anti Fraud Service Definitions API, and 58 more. Tagged areas include Payments, Payment Orchestration, Fintech, Checkout, and Tokenization.


  The Gr4vy catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Gr4vy''s developer surface includes documentation, API reference, getting-started guide, authentication, CLI, changelog, engineering blog, and 28 more developer resources.'
plans:
- name: Gr4Vy Plans Pricing
  plan_count: 0
  slug: gr4vy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Gr4Vy Rate Limits
  slug: gr4vy-rate-limits
scopes:
- name: Gr4Vy Scopes
  scope_count: 86
  slug: gr4vy-scopes
  summary_line: 86 scopes · password
score:
  band: exemplar
  composite: 66.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.8
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 66.1
    developer_ergonomics: 90.5
    discoverability: 75.9
    operational_transparency: 73.7
  previous_composite: 65.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 63.9
      derived: 0
      marker_coverage: 0.0
      total: 61
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2-sca
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 84.4
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Gr4Vy Authentication
  slug: gr4vy-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Gr4Vy Domain Security
  slug: gr4vy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gr4vy
tags:
- Payments
- Payment Orchestration
- Fintech
- Checkout
- Tokenization
- Vault
- Fraud
- 3D Secure
- Webhook
- Commerce
website: https://gr4vy.com/
---
