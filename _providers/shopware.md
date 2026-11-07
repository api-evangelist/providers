---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Shopware Agentic Access
  operation_count: 26
  slug: shopware-agentic-access
  summary_line: 26 operations · 15 acting
api_count: 2
apis:
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: Customer registration, login and profile management
  name: Shopware Account API
  slug: shopware-account-api
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: High-throughput bulk upsert and delete operations
  name: Shopware Bulk API
  slug: shopware-bulk-api
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: Manage the shopping cart and its line items
  name: Shopware Cart API
  slug: shopware-cart-api
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: Manage the product category tree
  name: Shopware Category API
  slug: shopware-category-api
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: Complete the purchase workflow
  name: Shopware Checkout API
  slug: shopware-checkout-api
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: Manage customer accounts and addresses
  name: Shopware Customer API
  slug: shopware-customer-api
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: Fetch storefront navigation menus
  name: Shopware Navigation API
  slug: shopware-navigation-api
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: Access and manage orders and their line items
  name: Shopware Order API
  slug: shopware-order-api
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: Create, read, update, and delete products and variants
  name: Shopware Product API
  slug: shopware-product-api
- baseURL: https://{your-shop-domain}/api
  baseurl_source: declared
  description: DAL-powered search with filter, sort, and aggregation
  name: Shopware Search API
  slug: shopware-search-api
artifact_total: 37
collections:
- collection_type: open
  name: Shopware Admin Account API
  slug: open-shopware-account-api
- collection_type: open
  name: Shopware Admin Account Bulk API
  slug: open-shopware-bulk-api
- collection_type: open
  name: Shopware Admin Account Cart API
  slug: open-shopware-cart-api
- collection_type: open
  name: Shopware Admin Account Category API
  slug: open-shopware-category-api
- collection_type: open
  name: Shopware Admin Account Checkout API
  slug: open-shopware-checkout-api
- collection_type: open
  name: Shopware Admin Account Customer API
  slug: open-shopware-customer-api
- collection_type: open
  name: Shopware Admin Account Navigation API
  slug: open-shopware-navigation-api
- collection_type: open
  name: Shopware Admin Account Order API
  slug: open-shopware-order-api
- collection_type: open
  name: Shopware Admin Account Product API
  slug: open-shopware-product-api
- collection_type: open
  name: Shopware Admin Account Search API
  slug: open-shopware-search-api
common:
- group: other
  href: https://artifacts.apis.io/shopware/capabilities/shopware-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/shopware-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/shopware/agentic-access/shopware-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shopware-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/shopware/security/shopware-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/shopware-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/shopware/security/shopware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shopware-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/shopware/authentication/shopware-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shopware-authentication.yml
- group: auth
  href: https://artifacts.apis.io/shopware/scopes/shopware-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/shopware-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.shopware.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shopware.com/docs/concepts/api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopware
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopware-ag/
- group: company
  title: ''
  type: Blog
  url: https://www.shopware.com/en/news/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shopware.com/en/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shopware.com/
- group: other
  title: ''
  type: X
  url: https://x.com/shopwaredevs
- group: commercial
  href: https://artifacts.apis.io/shopware/plans/shopware-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/shopware-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/shopware/rate-limits/shopware-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shopware-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/shopware/finops/shopware-finops.yml
  title: ''
  type: FinOps
  url: finops/shopware-finops.yml
- group: design
  href: https://artifacts.apis.io/shopware/vocabulary/shopware-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shopware-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/shopware/json-ld/shopware-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/shopware-context.jsonld
- group: docs
  href: https://artifacts.apis.io/shopware/json-schema/shopware-product-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/shopware-product-schema.json
- group: docs
  href: https://artifacts.apis.io/shopware/json-schema/shopware-cart-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/shopware-cart-schema.json
- group: docs
  href: https://artifacts.apis.io/shopware/json-schema/shopware-order-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/shopware-order-schema.json
created: '2026-06-12'
description: 'Shopware is an open-source, API-first e-commerce platform built on Symfony and Vue.js, serving mid-market and enterprise merchants across B2C, D2C, and B2B use cases. The platform exposes two primary HTTP APIs: an Admin API for back-office integrations and automation, and a Store API for building headless customer-facing storefronts. Both APIs publish machine-readable OpenAPI 3 specifications directly from each running instance. Shopware is available as a free Community Edition (MIT-licensed), and as paid SaaS and self-hosted tiers (Rise, Evolve, Beyond) unlocking additional commerce capabilities.'
examples:
- key_count: 3
  name: Shopware Add To Cart Example
  slug: shopware-add-to-cart-example
- key_count: 3
  name: Shopware Create Product Example
  slug: shopware-create-product-example
- key_count: 3
  name: Shopware Search Products Example
  slug: shopware-search-products-example
finops:
- has_sources: true
  method: unmarked
  name: Shopware Finops
  primary_unit: ''
  service_category: E-Commerce Platform
  slug: shopware-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopware.png
json_schemas:
- name: Shopware Cart
  property_count: 11
  slug: shopware-cart
- name: Shopware Order
  property_count: 29
  slug: shopware-order
- name: Shopware Product
  property_count: 29
  slug: shopware-product
jsonld:
- class_count: 9
  name: Shopware Context
  property_count: 54
  slug: shopware-context
layout: provider
modified: '2026-06-12'
name: Shopware
nav: Providers
network: true
overview: 'Shopware publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Bulk API, Cart API, and 7 more. Tagged areas include E-Commerce, Open Source, Headless Commerce, B2B, and Consumer.


  The Shopware catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Shopware''s developer surface includes authentication, documentation, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Shopware Plans Pricing
  plan_count: 5
  slug: shopware-plans-pricing
- name: Shopware Price Estimates
  plan_count: 0
  slug: shopware-price-estimates
random_paper: 9
rate_limits:
- limit_count: 5
  name: Shopware Rate Limits
  slug: shopware-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Shopware — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: shopware-jsonschema-spectral-rules
scopes:
- name: Shopware Scopes
  scope_count: 1
  slug: shopware-scopes
  summary_line: 1 scope · clientCredentials/password
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.4
    catalog_earned_first_party: 0.0
    catalog_gap: 37.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 38.9
    contract_governance: 23.5
    contract_quality: 54.3
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 49.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 46.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/shopware/shopware-2026-06-20T193839.png
security:
- kind: authentication
  name: Shopware Authentication
  slug: shopware-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Shopware Domain Security
  slug: shopware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Shopware Vulnerability Disclosure
  slug: shopware-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: shopware
tags:
- E-Commerce
- Open Source
- Headless Commerce
- B2B
- Consumer
- REST
- OAuth
- Authentication
website: https://www.shopware.com
---
