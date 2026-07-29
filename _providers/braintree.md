---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Braintree Agentic Access
  operation_count: 25
  slug: braintree-agentic-access
  summary_line: 25 operations · 16 acting
api_count: 14
apis:
- description: The Braintree GraphQL API provides a modern, flexible interface for interacting with the Braintree payment gateway. It exposes a single HTTP endpoint that handles all queries and mutations, allowing d
  name: Braintree GraphQL API
  slug: graphql-api
- description: 'The Braintree JavaScript Client SDK enables secure collection of payment information directly in the browser without sensitive card data touching your servers. It is organized into standalone modules '
  name: Braintree JavaScript Client SDK
  slug: javascript-client-sdk
- description: The Braintree iOS SDK is a native library for accepting card and alternative payments within iOS applications. It supports Swift and Objective-C and provides modules for credit and debit card processi
  name: Braintree iOS SDK
  slug: ios-sdk
- description: The Braintree Android SDK provides a native library for integrating payment acceptance into Android applications. It supports Java and Kotlin and includes modules for card payments, PayPal, Venmo, Goo
  name: Braintree Android SDK
  slug: android-sdk
- description: Braintree Webhooks deliver automated HTTP POST notifications to your server when specific events occur within the payment gateway. Supported event types include subscription status changes, transactio
  name: Braintree Webhooks
  slug: webhooks
- description: Operations for retrieving add-on definitions that can be applied to subscriptions to increase their price.
  name: braintree Add-Ons API
  slug: braintree-add-ons-api
- description: Operations for generating client tokens used to initialize Braintree client SDKs on web and mobile.
  name: braintree Client Tokens API
  slug: braintree-client-tokens-api
- description: Operations for creating, retrieving, updating, and deleting customer records in the Braintree Vault.
  name: braintree Customers API
  slug: braintree-customers-api
- description: Operations for retrieving discount definitions that can be applied to subscriptions to reduce their price.
  name: braintree Discounts API
  slug: braintree-discounts-api
- description: Operations for retrieving and managing payment disputes and chargebacks.
  name: braintree Disputes API
  slug: braintree-disputes-api
- description: Operations for creating, retrieving, updating, and deleting vaulted payment methods associated with customers.
  name: braintree Payment Methods API
  slug: braintree-payment-methods-api
- description: Operations for retrieving billing plan definitions configured in the Braintree Control Panel.
  name: braintree Plans API
  slug: braintree-plans-api
- description: Operations for creating, retrieving, updating, canceling, and retrying customer subscriptions to recurring billing plans.
  name: braintree Subscriptions API
  slug: braintree-subscriptions-api
- description: Operations for creating, capturing, voiding, refunding, and retrieving payment transactions.
  name: braintree Transactions API
  slug: braintree-transactions-api
artifact_total: 54
asyncapis:
- description: Braintree Webhooks deliver automated HTTP POST notifications to a merchant-configured destination URL when specific events occur within the payment gateway. Webhook notifications are triggered by tran
  name: Braintree Webhooks
  slug: braintree-webhooks-asyncapi
collections:
- collection_type: open
  name: Braintree Payments API
  slug: open-braintree-payments
- collection_type: open
  name: Braintree Subscriptions API
  slug: open-braintree-subscriptions
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/braintree-agentic-access.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/braintree-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/braintree-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/braintree-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/braintree-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/braintree-data-model.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/braintree-decline-codes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/braintree-trust-center.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/braintree-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/braintree-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/braintree-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/braintree-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/braintree
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/braintree
- group: design
  title: ''
  type: JSONLD
  url: json-ld/braintree-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/braintree-transaction-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/braintree-customer-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/braintree-subscription-schema.json
description: Our mission is to empower developers with the tools, resources, and simple-to-use SDKs and APIs to build on one platform, so they can serve merchants from around the world.
finops:
- name: Braintree Finops
  service_category: Payments
  slug: braintree-finops
graphqls:
- description: The Braintree GraphQL API provides a modern, flexible interface for interacting with the Braintree payment gateway. It exposes a single HTTP endpoint that handles all queries and mutations, allowing d
  name: braintree GraphQL API
  slug: braintree-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/braintree.png
json_schemas:
- name: Address
  property_count: 9
  slug: braintree-address
- name: AppliedModification
  property_count: 7
  slug: braintree-appliedmodification
- name: CreditCardDetails
  property_count: 7
  slug: braintree-creditcarddetails
- name: Braintree Customer
  property_count: 13
  slug: braintree-customer
- name: CustomerRequest
  property_count: 10
  slug: braintree-customerrequest
- name: Descriptor
  property_count: 3
  slug: braintree-descriptor
- name: Dispute
  property_count: 10
  slug: braintree-dispute
- name: Error
  property_count: 2
  slug: braintree-error
- name: LineItem
  property_count: 9
  slug: braintree-lineitem
- name: Modification
  property_count: 9
  slug: braintree-modification
- name: ModificationAdd
  property_count: 5
  slug: braintree-modificationadd
- name: ModificationCollection
  property_count: 3
  slug: braintree-modificationcollection
- name: ModificationUpdate
  property_count: 5
  slug: braintree-modificationupdate
- name: PaymentMethod
  property_count: 6
  slug: braintree-paymentmethod
- name: PaymentMethodRequest
  property_count: 5
  slug: braintree-paymentmethodrequest
- name: PaymentMethodUpdateRequest
  property_count: 3
  slug: braintree-paymentmethodupdaterequest
- name: Plan
  property_count: 14
  slug: braintree-plan
- name: Braintree Subscription
  property_count: 24
  slug: braintree-subscription
- name: SubscriptionRequest
  property_count: 17
  slug: braintree-subscriptionrequest
- name: SubscriptionUpdateRequest
  property_count: 10
  slug: braintree-subscriptionupdaterequest
- name: Braintree Transaction
  property_count: 28
  slug: braintree-transaction
- name: TransactionOptions
  property_count: 6
  slug: braintree-transactionoptions
- name: TransactionRequest
  property_count: 16
  slug: braintree-transactionrequest
json_structures:
- name: Braintree Structure
  property_count: 0
  slug: braintree-structure
jsonld:
- class_count: 0
  name: Braintree Context
  property_count: 8
  slug: braintree-context
layout: provider
modified: '2026-05-19'
name: braintree
nav: Providers
network: true
overview: 'braintree publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Add-Ons API, Client Tokens API, and 7 more.


  The braintree catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  braintree''s developer surface includes sandbox, changelog, authentication, and 15 more developer resources.'
plans:
- name: Braintree Plans Pricing
  plan_count: 6
  slug: braintree-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 3
  name: Braintree Rate Limits
  slug: braintree-rate-limits
rules:
- name: braintree API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: braintree-asyncapi-spectral-rules
- name: braintree API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: braintree-jsonschema-spectral-rules
scopes:
- name: Braintree Scopes
  scope_count: 40
  slug: braintree-scopes
  summary_line: 40 scopes
score:
  band: developing
  composite: 48.5
  delta: -3.2
  facets:
    commercial_clarity: 47.4
    contract_quality: 74.6
    developer_ergonomics: 17.4
    discoverability: 50.0
    governance: 41.7
    operational_transparency: 52.6
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/braintree/refs/heads/main/screenshots/braintree-2026-06-20T173632.png
security:
- kind: authentication
  name: Braintree Authentication
  slug: braintree-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Braintree Domain Security
  slug: braintree-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Braintree Vulnerability Disclosure
  slug: braintree-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Braintree Trust Center
  slug: braintree-trust-center
  summary_line: PCI DSS, Visa Global Registry of Service Providers, Mastercard SDP, SOC 2 Type 2
slug: braintree
---
