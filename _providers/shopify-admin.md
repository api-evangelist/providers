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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Shopify Admin Agentic Access
  operation_count: 22
  slug: shopify-admin-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 10
apis:
- description: The Shopify Admin GraphQL API is the recommended API for building Shopify apps and integrations. It provides access to all Shopify admin resources including products, customers, orders, inventory, ful
  name: Shopify Admin GraphQL API
  slug: shopify-admin-graphql-api
- description: Shopify webhooks allow apps to subscribe to specific events that occur in a store. When an event occurs, Shopify sends an HTTP POST request with a JSON payload to the configured endpoint. Webhooks can
  name: Shopify Webhooks
  slug: shopify-webhooks
- description: The Collections API from Shopify Admin API — 2 operation(s) for collections.
  name: Shopify Admin API Collections API
  slug: shopify-admin-collections-api
- description: The Customers API from Shopify Admin API — 2 operation(s) for customers.
  name: Shopify Admin API Customers API
  slug: shopify-admin-customers-api
- description: The Inventory API from Shopify Admin API — 2 operation(s) for inventory.
  name: Shopify Admin API Inventory API
  slug: shopify-admin-inventory-api
- description: The Locations API from Shopify Admin API — 1 operation(s) for locations.
  name: Shopify Admin API Locations API
  slug: shopify-admin-locations-api
- description: The Orders API from Shopify Admin API — 3 operation(s) for orders.
  name: Shopify Admin API Orders API
  slug: shopify-admin-orders-api
- description: The Products API from Shopify Admin API — 2 operation(s) for products.
  name: Shopify Admin API Products API
  slug: shopify-admin-products-api
- description: The Shop API from Shopify Admin API — 1 operation(s) for shop.
  name: Shopify Admin API Shop API
  slug: shopify-admin-shop-api
- description: The Webhooks API from Shopify Admin API — 2 operation(s) for webhooks.
  name: Shopify Admin API Webhooks API
  slug: shopify-admin-webhooks-api
artifact_total: 29
asyncapis:
- description: AsyncAPI 2.6 specification modeling the Shopify Admin webhook event surface. Shopify webhooks allow apps to subscribe to events that occur in a Shopify store. When a subscribed event occurs, Shopify s
  name: Shopify Admin Webhooks
  slug: shopify-admin-webhooks-asyncapi
collections:
- collection_type: open
  name: Shopify Admin REST API
  slug: open-shopify-admin-rest
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shopify-admin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopify-admin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopify-admin-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopify
- group: company
  title: ''
  type: Website
  url: https://shopify.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://shopify.dev/docs/api
- group: auth
  title: ''
  type: Authentication
  url: https://shopify.dev/docs/apps/auth/get-access-tokens
- group: operate
  title: ''
  type: RateLimits
  url: https://shopify.dev/docs/api/usage/rate-limits
- group: design
  title: ''
  type: Versioning
  url: https://shopify.dev/docs/api/usage/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: https://shopify.dev/changelog
- group: company
  title: ''
  type: Blog
  url: https://shopify.dev/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Shopify
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/shopify-admin-product-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/shopify-admin-order-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/shopify-admin-customer-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/shopify-admin-product-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/shopify-admin-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/shopify-admin-list-products-example.json
- group: build
  title: ''
  type: Examples
  url: examples/shopify-admin-create-order-example.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/shopify-admin-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/shopify-admin-rules.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/store-management.yaml
- group: agent
  title: ''
  type: LlmsText
  url: https://shopify.dev/llms.txt
created: '2026-05-02'
description: The Shopify Admin API provides programmatic access to manage Shopify store administration. It enables app developers and merchants to manage products, customers, orders, inventory, shipping, fulfillment, collections, webhooks, and store settings. The Admin API is available in both REST and GraphQL formats. Shopify is transitioning from REST to GraphQL as the primary API, with GraphQL recommended for all new development.
examples:
- key_count: 4
  name: Shopify Admin Create Order Example
  slug: shopify-admin-create-order-example
- key_count: 4
  name: Shopify Admin List Products Example
  slug: shopify-admin-list-products-example
finops:
- name: Shopify Admin Finops
  service_category: Commerce
  slug: shopify-admin-finops
graphqls:
- description: The Shopify Admin GraphQL API is the recommended API for building Shopify apps and integrations. It provides access to all Shopify admin resources including products, customers, orders, inventory, ful
  name: Shopify Admin API GraphQL API
  slug: shopify-admin-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopify-admin.png
json_schemas:
- name: Shopify Admin Customer
  property_count: 17
  slug: shopify-admin-customer
- name: Shopify Admin Order
  property_count: 22
  slug: shopify-admin-order
- name: Shopify Admin Product
  property_count: 14
  slug: shopify-admin-product
json_structures:
- name: Shopify Admin Product Structure
  property_count: 0
  slug: shopify-admin-product-structure
jsonld:
- class_count: 41
  name: Shopify Admin Context
  property_count: 3
  slug: shopify-admin-context
layout: provider
modified: '2026-05-30'
name: Shopify Admin API
nav: Providers
network: true
overview: 'Shopify Admin API publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Shopify Webhooks, Collections API, Customers API, and 6 more. Tagged areas include Commerce, Ecommerce, Admin, Products, and Orders.


  The Shopify Admin API catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Shopify Admin API''s developer surface includes authentication, documentation, changelog, engineering blog, GitHub presence, code examples, and 17 more developer resources.'
plans:
- name: Shopify Admin Plans Pricing
  plan_count: 5
  slug: shopify-admin-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 13
  name: Shopify Admin Rate Limits
  slug: shopify-admin-rate-limits
rules:
- name: Shopify Admin API API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: shopify-admin-asyncapi-spectral-rules
- name: Shopify Admin API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: shopify-admin-jsonschema-spectral-rules
- name: Shopify Admin API API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: shopify-admin-rules
score:
  band: developing
  composite: 48.1
  delta: -3.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 75.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 31.3
    operational_transparency: 52.6
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shopify-admin/refs/heads/main/screenshots/shopify-admin-2026-06-20T193830.png
security:
- kind: authentication
  name: Shopify Admin Authentication
  slug: shopify-admin-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shopify Admin Domain Security
  slug: shopify-admin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shopify-admin
tags:
- Commerce
- Ecommerce
- Admin
- Products
- Orders
- Customers
website: https://shopify.dev/
---
