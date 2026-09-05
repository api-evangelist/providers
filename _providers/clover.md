---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Clover Agentic Access
  operation_count: 36
  slug: clover-agentic-access
  summary_line: 36 operations · 18 acting
api_count: 14
apis:
- description: Native SDK for Android apps running on Clover devices, with access to merchant data and device hardware.
  name: Clover Android SDK
  slug: android-sdk
- description: Payment-processing API for Android apps on Clover devices that abstracts device configuration.
  name: Clover Android Payments API
  slug: android-payments-api
- description: Semi-integrated POS API for merchant-facing Pay Display flows on Clover devices.
  name: Clover REST Pay Display API
  slug: rest-pay-display
- description: Remote Pay SDKs for Cloud, Windows, iOS, and Android integrations with Clover devices.
  name: Clover Remote Pay SDKs
  slug: remote-pay-sdks
- description: Mobile SDK (iOS, Android) for accepting card-present payments via Clover Go readers.
  name: Clover Go SDK
  slug: go-sdk
- baseURL: https://api.clover.com
  baseurl_source: declared
  description: The CHARGES API from Clover — 3 operation(s) for charges.
  name: Clover CHARGES API
  slug: clover-charges-api
- baseURL: https://api.clover.com
  baseurl_source: declared
  description: The CHECKOUT API from Clover — 1 operation(s) for checkout.
  name: Clover CHECKOUT API
  slug: clover-checkout-api
- baseURL: https://api.clover.com
  baseurl_source: declared
  description: The CUSTOMERS API from Clover — 2 operation(s) for customers.
  name: Clover CUSTOMERS API
  slug: clover-customers-api
- baseURL: https://api.clover.com
  baseurl_source: declared
  description: The EMPLOYEES API from Clover — 3 operation(s) for employees.
  name: Clover EMPLOYEES API
  slug: clover-employees-api
- baseURL: https://api.clover.com
  baseurl_source: declared
  description: The INVENTORY API from Clover — 5 operation(s) for inventory.
  name: Clover INVENTORY API
  slug: clover-inventory-api
- baseURL: https://api.clover.com
  baseurl_source: declared
  description: The ORDERS API from Clover — 4 operation(s) for orders.
  name: Clover ORDERS API
  slug: clover-orders-api
- baseURL: https://api.clover.com
  baseurl_source: declared
  description: The PAYMENTS API from Clover — 2 operation(s) for payments.
  name: Clover PAYMENTS API
  slug: clover-payments-api
- baseURL: https://api.clover.com
  baseurl_source: declared
  description: The REFUNDS API from Clover — 2 operation(s) for refunds.
  name: Clover REFUNDS API
  slug: clover-refunds-api
- baseURL: https://api.clover.com
  baseurl_source: declared
  description: The TOKENS API from Clover — 1 operation(s) for tokens.
  name: Clover TOKENS API
  slug: clover-tokens-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Clover Ecommerce CHARGES API
  slug: open-clover-charges-api
- collection_type: open
  name: Clover Ecommerce CHARGES CHECKOUT API
  slug: open-clover-checkout-api
- collection_type: open
  name: Clover Ecommerce CHARGES CUSTOMERS API
  slug: open-clover-customers-api
- collection_type: open
  name: Clover Ecommerce API
  slug: open-clover-ecommerce-api
- collection_type: open
  name: Clover Ecommerce CHARGES EMPLOYEES API
  slug: open-clover-employees-api
- collection_type: open
  name: Clover Ecommerce CHARGES INVENTORY API
  slug: open-clover-inventory-api
- collection_type: open
  name: Clover Ecommerce CHARGES ORDERS API
  slug: open-clover-orders-api
- collection_type: open
  name: Clover Ecommerce CHARGES PAYMENTS API
  slug: open-clover-payments-api
- collection_type: open
  name: Clover Platform REST API
  slug: open-clover-platform-rest-api
- collection_type: open
  name: Clover Ecommerce CHARGES REFUNDS API
  slug: open-clover-refunds-api
- collection_type: open
  name: Clover Ecommerce CHARGES TOKENS API
  slug: open-clover-tokens-api
common:
- group: operate
  title: ''
  type: Support
  url: https://www.clover.com/help
- group: design
  title: ''
  type: Webhooks
  url: https://docs.clover.com/dev/docs/webhooks
- group: operate
  title: ''
  type: DeprecationPolicy
  url: https://docs.clover.com/dev/docs/deprecated-apis
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.dev.clover.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://docs.clover.com/reference-link/api-reference-overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.clover.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.clover.com/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clover.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clover.com/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clover.com/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.clover.com/docs/get-started-with-sandbox-environment
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clover-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clover-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clover-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/clover-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clover
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clovernetwork
- group: company
  title: ''
  type: Website
  url: https://www.clover.com/
- group: other
  title: ''
  type: Developer
  url: https://docs.clover.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/clover-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clover-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clover-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/clover-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/clover-vocabulary.yaml
- group: design
  title: Platform REST API Context
  type: JSONLD
  url: json-ld/clover-platform-rest-api-context.jsonld
- group: design
  title: Ecommerce API Context
  type: JSONLD
  url: json-ld/clover-ecommerce-api-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.clover.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://blog.clover.com/feed/
created: '2026-05-08'
description: Clover is a Fiserv-owned point-of-sale platform for small and mid-size merchants. The Clover developer platform exposes the Clover REST API for inventory/orders/customers/transactions, the Ecommerce API for online payments, an Android Payments API and Clover Android SDK for native apps on Clover devices, the REST Pay Display API for semi-integrated POS, the Remote Pay SDKs (cloud, Windows, iOS, Android), and the Clover Go SDK.
examples:
- key_count: 46
  name: Ecommerce Api Charge Example
  slug: ecommerce-api-charge-example
- key_count: 4
  name: Ecommerce Api Refund Example
  slug: ecommerce-api-refund-example
- key_count: 8
  name: Platform Rest Api Category Example
  slug: platform-rest-api-category-example
- key_count: 12
  name: Platform Rest Api Customer Example
  slug: platform-rest-api-customer-example
- key_count: 18
  name: Platform Rest Api Employee Example
  slug: platform-rest-api-employee-example
- key_count: 28
  name: Platform Rest Api Item Example
  slug: platform-rest-api-item-example
- key_count: 36
  name: Platform Rest Api Order Example
  slug: platform-rest-api-order-example
- key_count: 44
  name: Platform Rest Api Payment Example
  slug: platform-rest-api-payment-example
finops:
- name: Clover Finops
  service_category: Payments
  slug: clover-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clover.png
json_schemas:
- name: Charge
  property_count: 46
  slug: ecommerce-api-charge
- name: Refund
  property_count: 4
  slug: ecommerce-api-refund
- name: Category
  property_count: 8
  slug: platform-rest-api-category
- name: Customer
  property_count: 12
  slug: platform-rest-api-customer
- name: Employee
  property_count: 18
  slug: platform-rest-api-employee
- name: Item
  property_count: 28
  slug: platform-rest-api-item
- name: Order
  property_count: 36
  slug: platform-rest-api-order
- name: Payment
  property_count: 44
  slug: platform-rest-api-payment
json_structures:
- name: Ecommerce Api Charge Structure
  property_count: 46
  slug: ecommerce-api-charge-structure
- name: Ecommerce Api Refund Structure
  property_count: 4
  slug: ecommerce-api-refund-structure
- name: Platform Rest Api Category Structure
  property_count: 8
  slug: platform-rest-api-category-structure
- name: Platform Rest Api Customer Structure
  property_count: 12
  slug: platform-rest-api-customer-structure
- name: Platform Rest Api Employee Structure
  property_count: 18
  slug: platform-rest-api-employee-structure
- name: Platform Rest Api Item Structure
  property_count: 28
  slug: platform-rest-api-item-structure
- name: Platform Rest Api Order Structure
  property_count: 36
  slug: platform-rest-api-order-structure
- name: Platform Rest Api Payment Structure
  property_count: 44
  slug: platform-rest-api-payment-structure
jsonld:
- class_count: 2
  name: Clover Ecommerce Api Context
  property_count: 47
  slug: clover-ecommerce-api-context
- class_count: 6
  name: Clover Platform Rest Api Context
  property_count: 118
  slug: clover-platform-rest-api-context
layout: provider
modified: '2026-06-02'
name: Clover
nav: Providers
network: true
overview: 'Clover publishes 9 APIs on the [APIs.io](https://apis.io/) network, including CHARGES API, CHECKOUT API, CUSTOMERS API, and 6 more. Tagged areas include Restaurant, Point-of-Sale, Payments, Retail, and SMB.


  The Clover catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Clover''s developer surface includes support, sandbox, API reference, changelog, pricing, getting-started guide, authentication, and 21 more developer resources.'
plans:
- name: Clover Plans Pricing
  plan_count: 2
  slug: clover-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Clover Rate Limits
  slug: clover-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Clover API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: clover-jsonschema-spectral-rules
- effective_rule_count: 77
  extends:
  - spectral:oas
  name: Clover API Rules
  rule_count: 36
  severity_counts:
    error: 10
    hint: 0
    info: 5
    warn: 21
  slug: clover-spectral-rules
scopes:
- name: Clover Scopes
  scope_count: 13
  slug: clover-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 28.8
    contract_quality: 21.5
    developer_ergonomics: 50.0
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clover/refs/heads/main/screenshots/clover-2026-06-20T174623.png
security:
- kind: authentication
  name: Clover Authentication
  slug: clover-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Clover Domain Security
  slug: clover-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: clover
tags:
- Restaurant
- Point-of-Sale
- Payments
- Retail
- SMB
- Hardware
website: https://www.clover.com/
---
