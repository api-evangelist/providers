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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Shopify Storefront Agentic Access
  operation_count: 1
  slug: shopify-storefront-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 3
apis:
- description: Hydrogen is Shopify's opinionated React-based framework for building headless storefronts powered by the Storefront API. Hydrogen provides components, hooks, and utilities optimized for commerce inclu
  name: Shopify Hydrogen
  slug: shopify-hydrogen
- description: The Shopify JavaScript Buy SDK is a lightweight library that enables developers to integrate Shopify's storefront capabilities into any website or application. The SDK wraps the Storefront API and pro
  name: Shopify Buy SDK
  slug: shopify-buy-sdk
- description: The GraphQL API from Shopify Storefront API — 1 operation(s) for graphql.
  name: Shopify Storefront API GraphQL API
  slug: shopify-storefront-graphql-api
artifact_total: 19
collections:
- collection_type: open
  name: Shopify Storefront API
  slug: open-shopify-storefront
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shopify-storefront-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopify-storefront-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopify-storefront-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shopify
- group: agent
  title: ''
  type: LlmsText
  url: https://shopify.dev/llms.txt
created: '2026-05-02'
description: The Shopify Storefront API is a GraphQL API that enables developers to build custom headless storefronts, purchasing flows, and commerce experiences using Shopify as a backend. The API provides programmatic access to products, collections, carts, checkout, customer accounts, and contextual pricing. It is designed for headless commerce architectures and powers the Shopify Hydrogen framework.
examples:
- key_count: 4
  name: Shopify Storefront Create Cart Example
  slug: shopify-storefront-create-cart-example
- key_count: 4
  name: Shopify Storefront Query Products Example
  slug: shopify-storefront-query-products-example
finops:
- name: Shopify Storefront Finops
  service_category: Commerce
  slug: shopify-storefront-finops
graphqls:
- description: The Shopify Storefront API is a GraphQL API for building headless commerce experiences. It provides access to products, collections, cart, checkout, customer accounts, and contextual pricing. All requ
  name: Shopify Storefront API GraphQL API
  slug: shopify-storefront-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shopify-storefront.png
json_schemas:
- name: Shopify Storefront Cart
  property_count: 10
  slug: shopify-storefront-cart
- name: Shopify Storefront Product
  property_count: 16
  slug: shopify-storefront-product
json_structures:
- name: Shopify Storefront Cart Structure
  property_count: 0
  slug: shopify-storefront-cart-structure
jsonld:
- class_count: 43
  name: Shopify Storefront Context
  property_count: 1
  slug: shopify-storefront-context
layout: provider
modified: '2026-05-19'
name: Shopify Storefront API
nav: Providers
network: true
overview: 'Shopify Storefront API publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Commerce, Ecommerce, Headless, GraphQL, and Storefront.


  The Shopify Storefront API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Shopify Storefront API''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Shopify Storefront Plans Pricing
  plan_count: 5
  slug: shopify-storefront-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 3
  name: Shopify Storefront Rate Limits
  slug: shopify-storefront-rate-limits
rules:
- name: Shopify Storefront API API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: shopify-storefront-jsonschema-spectral-rules
- name: Shopify Storefront API API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 2
  slug: shopify-storefront-rules
score:
  band: developing
  composite: 43.2
  delta: -4.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 73.7
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 48.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shopify-storefront/refs/heads/main/screenshots/shopify-storefront-2026-06-20T193831.png
security:
- kind: authentication
  name: Shopify Storefront Authentication
  slug: shopify-storefront-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shopify Storefront Domain Security
  slug: shopify-storefront-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shopify-storefront
tags:
- Commerce
- Ecommerce
- Headless
- GraphQL
- Storefront
- Products
- Cart
- Checkout
---
