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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Braintree Agentic Access
  operation_count: 25
  slug: braintree-agentic-access
  summary_line: 25 operations · 16 acting
api_count: 2
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
- baseURL: https://api.example.com
  baseurl_source: declared
  description: Braintree Webhooks deliver automated HTTP POST notifications to your server when specific events occur within the payment gateway. Supported event types include subscription status changes, transactio
  name: Braintree Webhooks
  slug: webhooks
- baseURL: https://api.braintreegateway.com
  baseurl_source: declared
  description: Operations for retrieving add-on definitions that can be applied to subscriptions to increase their price.
  name: braintree Add-Ons API
  slug: braintree-add-ons-api
- baseURL: https://api.braintreegateway.com
  baseurl_source: declared
  description: Operations for generating client tokens used to initialize Braintree client SDKs on web and mobile.
  name: braintree Client Tokens API
  slug: braintree-client-tokens-api
- baseURL: https://api.braintreegateway.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting customer records in the Braintree Vault.
  name: braintree Customers API
  slug: braintree-customers-api
- baseURL: https://api.braintreegateway.com
  baseurl_source: declared
  description: Operations for retrieving discount definitions that can be applied to subscriptions to reduce their price.
  name: braintree Discounts API
  slug: braintree-discounts-api
- baseURL: https://api.braintreegateway.com
  baseurl_source: declared
  description: Operations for retrieving and managing payment disputes and chargebacks.
  name: braintree Disputes API
  slug: braintree-disputes-api
- baseURL: https://api.braintreegateway.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, and deleting vaulted payment methods associated with customers.
  name: braintree Payment Methods API
  slug: braintree-payment-methods-api
- baseURL: https://api.braintreegateway.com
  baseurl_source: declared
  description: Operations for retrieving billing plan definitions configured in the Braintree Control Panel.
  name: braintree Plans API
  slug: braintree-plans-api
- baseURL: https://api.braintreegateway.com
  baseurl_source: declared
  description: Operations for creating, retrieving, updating, canceling, and retrying customer subscriptions to recurring billing plans.
  name: braintree Subscriptions API
  slug: braintree-subscriptions-api
- baseURL: https://api.braintreegateway.com
  baseurl_source: declared
  description: Operations for creating, capturing, voiding, refunding, and retrieving payment transactions.
  name: braintree Transactions API
  slug: braintree-transactions-api
artifact_total: 64
asyncapis:
- description: Braintree Webhooks deliver automated HTTP POST notifications to a merchant-configured destination URL when specific events occur within the payment gateway. Webhook notifications are triggered by tran
  name: Braintree Webhooks
  slug: braintree-webhooks-asyncapi
collections:
- collection_type: open
  name: Braintree Payments Add-Ons API
  slug: open-braintree-add-ons-api
- collection_type: open
  name: Braintree Payments Add-Ons Client Tokens API
  slug: open-braintree-client-tokens-api
- collection_type: open
  name: Braintree Payments Add-Ons Customers API
  slug: open-braintree-customers-api
- collection_type: open
  name: Braintree Payments Add-Ons Discounts API
  slug: open-braintree-discounts-api
- collection_type: open
  name: Braintree Payments Add-Ons Disputes API
  slug: open-braintree-disputes-api
- collection_type: open
  name: Braintree Payments Add-Ons Payment Methods API
  slug: open-braintree-payment-methods-api
- collection_type: open
  name: Braintree Payments API
  slug: open-braintree-payments
- collection_type: open
  name: Braintree Payments Add-Ons Plans API
  slug: open-braintree-plans-api
- collection_type: open
  name: Braintree Payments Add-Ons Subscriptions API
  slug: open-braintree-subscriptions-api
- collection_type: open
  name: Braintree Subscriptions API
  slug: open-braintree-subscriptions
- collection_type: open
  name: Braintree Payments Add-Ons Transactions API
  slug: open-braintree-transactions-api
common:
- group: commercial
  href: https://artifacts.apis.io/braintree/plans/braintree-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/braintree-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/braintree/rate-limits/braintree-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/braintree-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/braintree/finops/braintree-finops.yml
  title: ''
  type: FinOps
  url: finops/braintree-finops.yml
- group: other
  href: https://artifacts.apis.io/braintree/capabilities/braintree-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/braintree-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/braintree/agentic-access/braintree-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/braintree-agentic-access.yml
- group: start
  href: https://artifacts.apis.io/braintree/sandbox/braintree-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/braintree-sandbox.yml
- group: design
  href: https://artifacts.apis.io/braintree/conventions/braintree-conventions.yml
  title: ''
  type: Conventions
  url: conventions/braintree-conventions.yml
- group: operate
  href: https://artifacts.apis.io/braintree/changelog/braintree-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/braintree-changelog.yml
- group: design
  href: https://artifacts.apis.io/braintree/components/braintree-components.yml
  title: ''
  type: Components
  url: components/braintree-components.yml
- group: design
  href: https://artifacts.apis.io/braintree/data-model/braintree-data-model.yml
  title: ''
  type: DataModel
  url: data-model/braintree-data-model.yml
- group: build
  href: https://artifacts.apis.io/braintree/errors/braintree-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/braintree-decline-codes.yml
- group: auth
  href: https://artifacts.apis.io/braintree/security/braintree-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/braintree-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/braintree/scopes/braintree-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/braintree-scopes.yml
- group: auth
  href: https://artifacts.apis.io/braintree/security/braintree-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/braintree-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/braintree/security/braintree-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/braintree-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/braintree/authentication/braintree-authentication.yml
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
  href: https://artifacts.apis.io/braintree/json-ld/braintree-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/braintree-context.jsonld
- group: docs
  href: https://artifacts.apis.io/braintree/json-schema/braintree-transaction-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/braintree-transaction-schema.json
- group: docs
  href: https://artifacts.apis.io/braintree/json-schema/braintree-customer-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/braintree-customer-schema.json
- group: docs
  href: https://artifacts.apis.io/braintree/json-schema/braintree-subscription-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/braintree-subscription-schema.json
description: Our mission is to empower developers with the tools, resources, and simple-to-use SDKs and APIs to build on one platform, so they can serve merchants from around the world.
finops:
- has_sources: true
  method: generated
  name: Braintree Finops
  primary_unit: transaction
  service_category: Payments
  slug: braintree-finops
  template: false
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
mcp_servers:
- description: Remote MCP server at mcp.paypal.com over HTTP.
  name: Braintree MCP Server
  slug: braintree
modified: '2026-09-16'
name: Braintree
nav: Providers
network: true
overview: 'Braintree publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks, Add-Ons API, Client Tokens API, and 11 more. Tagged areas include Payments, Transaction, Mobile, Subscription, and Payment Processing.


  The Braintree catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Braintree''s developer surface includes sandbox, changelog, authentication, and 19 more developer resources.'
plans:
- name: Braintree Plans Pricing
  plan_count: 6
  slug: braintree-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Braintree Rate Limits
  slug: braintree-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Braintree — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: braintree-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Braintree — jsonschema rules
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
  composite: 40.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 23.7
    contract_governance: 13.6
    contract_quality: 63.1
    developer_ergonomics: 28.6
    discoverability: 51.8
    operational_transparency: 39.5
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/braintree/braintree-2026-06-20T173632.png
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
tags:
- Payments
- Transaction
- Mobile
- Subscription
- Payment Processing
---
