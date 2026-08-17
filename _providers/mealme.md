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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Mealme Agentic Access
  operation_count: 36
  slug: mealme-agentic-access
  summary_line: 36 operations · 22 acting
api_count: 9
apis:
- description: Cart creation, retrieval, and item management.
  name: MealMe Carts API
  slug: mealme-carts-api
- description: MealMe Connect account linking and ordering.
  name: MealMe Connect Accounts API
  slug: mealme-connect-accounts-api
- description: Address geocoding and reverse geocoding.
  name: MealMe Geocoding API
  slug: mealme-geocoding-api
- description: Order creation, finalization, and history.
  name: MealMe Orders API
  slug: mealme-orders-api
- description: Payment method management and payment intents.
  name: MealMe Payments API
  slug: mealme-payments-api
- description: Store, product, and place search.
  name: MealMe Search API
  slug: mealme-search-api
- description: Store lookup, inventory, and product details.
  name: MealMe Stores API
  slug: mealme-stores-api
- description: Customer support chat.
  name: MealMe Support Chat API
  slug: mealme-support-chat-api
- description: Order tracking webhooks.
  name: MealMe Tracking API
  slug: mealme-tracking-api
artifact_total: 56
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MealMe Food Ordering Carts API
  slug: open-mealme-carts-api
- collection_type: open
  name: MealMe Food Ordering Carts Connect Accounts API
  slug: open-mealme-connect-accounts-api
- collection_type: open
  name: MealMe Food Ordering Carts Geocoding API
  slug: open-mealme-geocoding-api
- collection_type: open
  name: MealMe Food Ordering Carts Orders API
  slug: open-mealme-orders-api
- collection_type: open
  name: MealMe Food Ordering Carts Payments API
  slug: open-mealme-payments-api
- collection_type: open
  name: MealMe Food Ordering Carts Search API
  slug: open-mealme-search-api
- collection_type: open
  name: MealMe Food Ordering Carts Stores API
  slug: open-mealme-stores-api
- collection_type: open
  name: MealMe Food Ordering Carts Support Chat API
  slug: open-mealme-support-chat-api
- collection_type: open
  name: MealMe Food Ordering Carts Tracking API
  slug: open-mealme-tracking-api
- collection_type: open
  name: MealMe Food Ordering API
  slug: open-mealme
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mealme-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mealme-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mealme-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.mealme.ai/blog-feed.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MealMe-Ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mealme
- group: start
  title: ''
  type: Portal
  url: https://www.mealme.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mealme.ai/
- group: agent
  title: ''
  type: LlmsText
  url: https://api.mealme.ai/llms.txt
- group: design
  title: ''
  type: Spectral
  url: rules/mealme-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mealme-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mealme-api-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/mealme-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mealme-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mealme-finops.yml
created: '2025-03-01'
description: MealMe provides the largest food ordering API, enabling developers to get menus, inventory, and send orders to the point of sale at over 1 million restaurants and grocery stores for pickup or delivery. Includes a Food Search API, Menu API, and Grocery Ordering API.
examples:
- key_count: 4
  name: Mealme Api Cart Example
  slug: mealme-api-cart-example
- key_count: 5
  name: Mealme Api Cart Item Example
  slug: mealme-api-cart-item-example
- key_count: 21
  name: Mealme Api Cart Request Example
  slug: mealme-api-cart-request-example
- key_count: 4
  name: Mealme Api Order Example
  slug: mealme-api-order-example
- key_count: 29
  name: Mealme Api Order Request Example
  slug: mealme-api-order-request-example
- key_count: 3
  name: Mealme Api Payment Method Create Request Example
  slug: mealme-api-payment-method-create-request-example
- key_count: 3
  name: Mealme Api Payment Method Example
  slug: mealme-api-payment-method-example
- key_count: 6
  name: Mealme Api Product Example
  slug: mealme-api-product-example
- key_count: 10
  name: Mealme Api Store Example
  slug: mealme-api-store-example
finops:
- name: Mealme Finops
  service_category: API
  slug: mealme-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mealme.png
json_schemas:
- name: CartItem
  property_count: 5
  slug: mealme-api-cart-item
- name: CartRequest
  property_count: 21
  slug: mealme-api-cart-request
- name: Cart
  property_count: 4
  slug: mealme-api-cart
- name: OrderRequest
  property_count: 29
  slug: mealme-api-order-request
- name: Order
  property_count: 4
  slug: mealme-api-order
- name: PaymentMethodCreateRequest
  property_count: 3
  slug: mealme-api-payment-method-create-request
- name: PaymentMethod
  property_count: 3
  slug: mealme-api-payment-method
- name: Product
  property_count: 6
  slug: mealme-api-product
- name: Store
  property_count: 10
  slug: mealme-api-store
json_structures:
- name: Mealme Api Cart Item Structure
  property_count: 5
  slug: mealme-api-cart-item-structure
- name: Mealme Api Cart Request Structure
  property_count: 21
  slug: mealme-api-cart-request-structure
- name: Mealme Api Cart Structure
  property_count: 4
  slug: mealme-api-cart-structure
- name: Mealme Api Order Request Structure
  property_count: 29
  slug: mealme-api-order-request-structure
- name: Mealme Api Order Structure
  property_count: 4
  slug: mealme-api-order-structure
- name: Mealme Api Payment Method Create Request Structure
  property_count: 3
  slug: mealme-api-payment-method-create-request-structure
- name: Mealme Api Payment Method Structure
  property_count: 3
  slug: mealme-api-payment-method-structure
- name: Mealme Api Product Structure
  property_count: 6
  slug: mealme-api-product-structure
- name: Mealme Api Store Structure
  property_count: 10
  slug: mealme-api-store-structure
jsonld:
- class_count: 9
  name: Mealme Api Context
  property_count: 56
  slug: mealme-api-context
layout: provider
modified: '2026-06-02'
name: MealMe
nav: Providers
network: true
overview: 'MealMe publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Carts API, Connect Accounts API, Geocoding API, and 6 more. Tagged areas include Delivery, Food, Grocery, Ordering, and Restaurants.


  The MealMe catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  MealMe''s developer surface includes authentication, engineering blog, developer portal, documentation, and 11 more developer resources.'
plans:
- name: Mealme Plans Pricing
  plan_count: 3
  slug: mealme-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Mealme Rate Limits
  slug: mealme-rate-limits
rules:
- name: MealMe API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mealme-jsonschema-spectral-rules
- name: MealMe API Rules
  rule_count: 39
  severity_counts:
    error: 7
    hint: 0
    info: 9
    warn: 23
  slug: mealme-spectral-rules
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 73.7
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mealme/refs/heads/main/screenshots/mealme-2026-06-20T185111.png
security:
- kind: authentication
  name: Mealme Authentication
  slug: mealme-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mealme Domain Security
  slug: mealme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mealme
tags:
- Delivery
- Food
- Grocery
- Ordering
- Restaurants
website: https://www.mealme.ai/
---
