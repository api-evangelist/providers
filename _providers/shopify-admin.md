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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Shopify Admin Agentic Access
  operation_count: 22
  slug: shopify-admin-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 1
apis:
- description: The Shopify Admin GraphQL API is the recommended API for building Shopify apps and integrations. It provides access to all Shopify admin resources including products, customers, orders, inventory, ful
  name: Shopify Admin GraphQL API
  slug: shopify-admin-graphql-api
- description: Shopify webhooks allow apps to subscribe to specific events that occur in a store. When an event occurs, Shopify sends an HTTP POST request with a JSON payload to the configured endpoint. Webhooks can
  name: Shopify Webhooks
  slug: shopify-webhooks
- baseURL: https://{store_name}.myshopify.com/admin/api/2024-10
  baseurl_source: declared
  description: The Collections API from Shopify Admin API — 2 operation(s) for collections.
  name: Shopify Admin API Collections API
  slug: shopify-admin-collections-api
- baseURL: https://{store_name}.myshopify.com/admin/api/2024-10
  baseurl_source: declared
  description: The Customers API from Shopify Admin API — 2 operation(s) for customers.
  name: Shopify Admin API Customers API
  slug: shopify-admin-customers-api
- baseURL: https://{store_name}.myshopify.com/admin/api/2024-10
  baseurl_source: declared
  description: The Inventory API from Shopify Admin API — 2 operation(s) for inventory.
  name: Shopify Admin API Inventory API
  slug: shopify-admin-inventory-api
- baseURL: https://{store_name}.myshopify.com/admin/api/2024-10
  baseurl_source: declared
  description: The Locations API from Shopify Admin API — 1 operation(s) for locations.
  name: Shopify Admin API Locations API
  slug: shopify-admin-locations-api
- baseURL: https://{store_name}.myshopify.com/admin/api/2024-10
  baseurl_source: declared
  description: The Orders API from Shopify Admin API — 3 operation(s) for orders.
  name: Shopify Admin API Orders API
  slug: shopify-admin-orders-api
- baseURL: https://{store_name}.myshopify.com/admin/api/2024-10
  baseurl_source: declared
  description: The Products API from Shopify Admin API — 2 operation(s) for products.
  name: Shopify Admin API Products API
  slug: shopify-admin-products-api
- baseURL: https://{store_name}.myshopify.com/admin/api/2024-10
  baseurl_source: declared
  description: The Shop API from Shopify Admin API — 1 operation(s) for shop.
  name: Shopify Admin API Shop API
  slug: shopify-admin-shop-api
- baseURL: https://{store_name}.myshopify.com/admin/api/2024-10
  baseurl_source: declared
  description: The Webhooks API from Shopify Admin API — 2 operation(s) for webhooks.
  name: Shopify Admin API Webhooks API
  slug: shopify-admin-webhooks-api
artifact_total: 38
asyncapis:
- description: AsyncAPI 2.6 specification modeling the Shopify Admin webhook event surface. Shopify webhooks allow apps to subscribe to events that occur in a Shopify store. When a subscribed event occurs, Shopify s
  name: Shopify Admin Webhooks
  slug: shopify-admin-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shopify Admin REST Collections API
  slug: open-shopify-admin-collections-api
- collection_type: open
  name: Shopify Admin REST Collections Customers API
  slug: open-shopify-admin-customers-api
- collection_type: open
  name: Shopify Admin REST Collections Inventory API
  slug: open-shopify-admin-inventory-api
- collection_type: open
  name: Shopify Admin REST Collections Locations API
  slug: open-shopify-admin-locations-api
- collection_type: open
  name: Shopify Admin REST Collections Orders API
  slug: open-shopify-admin-orders-api
- collection_type: open
  name: Shopify Admin REST Collections Products API
  slug: open-shopify-admin-products-api
- collection_type: open
  name: Shopify Admin REST API
  slug: open-shopify-admin-rest
- collection_type: open
  name: Shopify Admin REST Collections Shop API
  slug: open-shopify-admin-shop-api
- collection_type: open
  name: Shopify Admin REST Collections Webhooks API
  slug: open-shopify-admin-webhooks-api
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
overview: 'Shopify Admin API publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Shopify Webhooks, Collections API, Customers API, and 6 more. Tagged areas include Commerce, E-Commerce, Admin, Product, and Order.


  The Shopify Admin API catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Shopify Admin API''s developer surface includes authentication, documentation, changelog, engineering blog, GitHub presence, code examples, and 16 more developer resources.'
plans:
- name: Shopify Admin Plans Pricing
  plan_count: 5
  slug: shopify-admin-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 13
  name: Shopify Admin Rate Limits
  slug: shopify-admin-rate-limits
rules:
- effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: Shopify Admin API API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: shopify-admin-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Shopify Admin API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: shopify-admin-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Shopify Admin API API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 5
  slug: shopify-admin-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 46.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 78.8
    developer_ergonomics: 16.7
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 28.9
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- E-Commerce
- Admin
- Product
- Order
- Customers
website: https://shopify.dev/
---
