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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
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
- description: The CHARGES API from Clover — 3 operation(s) for charges.
  name: Clover CHARGES API
  slug: clover-charges-api
- description: The CHECKOUT API from Clover — 1 operation(s) for checkout.
  name: Clover CHECKOUT API
  slug: clover-checkout-api
- description: The CUSTOMERS API from Clover — 2 operation(s) for customers.
  name: Clover CUSTOMERS API
  slug: clover-customers-api
- description: The EMPLOYEES API from Clover — 3 operation(s) for employees.
  name: Clover EMPLOYEES API
  slug: clover-employees-api
- description: The INVENTORY API from Clover — 5 operation(s) for inventory.
  name: Clover INVENTORY API
  slug: clover-inventory-api
- description: The ORDERS API from Clover — 4 operation(s) for orders.
  name: Clover ORDERS API
  slug: clover-orders-api
- description: The PAYMENTS API from Clover — 2 operation(s) for payments.
  name: Clover PAYMENTS API
  slug: clover-payments-api
- description: The REFUNDS API from Clover — 2 operation(s) for refunds.
  name: Clover REFUNDS API
  slug: clover-refunds-api
- description: The TOKENS API from Clover — 1 operation(s) for tokens.
  name: Clover TOKENS API
  slug: clover-tokens-api
artifact_total: 51
collections:
- collection_type: open
  name: Clover Ecommerce API
  slug: open-clover-ecommerce-api
- collection_type: open
  name: Clover Platform REST API
  slug: open-clover-platform-rest-api
common:
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
overview: 'Clover publishes 9 APIs on the [APIs.io](https://apis.io/) network, including CHARGES API, CHECKOUT API, CUSTOMERS API, and 6 more. Tagged areas include Restaurant, POS, Payments, Retail, and SMB.


  The Clover catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Clover''s developer surface includes authentication, engineering blog, and 15 more developer resources.'
plans:
- name: Clover Plans Pricing
  plan_count: 2
  slug: clover-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Clover Rate Limits
  slug: clover-rate-limits
rules:
- name: Clover API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: clover-jsonschema-spectral-rules
- name: Clover API Rules
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
  composite: 43.1
  delta: -8.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.5
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
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
- POS
- Payments
- Retail
- SMB
- Hardware
website: https://www.clover.com/
---
