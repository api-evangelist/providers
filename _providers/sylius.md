---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Sylius REST API is built on API Platform and provides endpoints for all core eCommerce operations including product catalog management, order processing, customer management, payment handling, shi
  name: Sylius REST API
  slug: sylius-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sylius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sylius.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sylius.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Sylius
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sylius/
- group: company
  title: ''
  type: Blog
  url: https://sylius.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://sylius.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Sylius
- group: commercial
  title: ''
  type: Plans
  url: plans/sylius-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sylius-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sylius-finops.yml
created: 2026-06-13
description: Sylius is an open-source headless eCommerce platform built on PHP, Symfony, and API Platform. It provides a comprehensive REST API for managing products, product variants, orders, carts, customers, payments, shipments, promotions, and customizable shop configuration. The API uses JWT authentication and generates OpenAPI documentation automatically, making it well-suited for headless commerce architectures and custom storefront implementations.
finops:
- name: Sylius Finops
  service_category: ''
  slug: sylius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sylius.png
jsonld:
- class_count: 0
  name: Sylius Context
  property_count: 8
  slug: sylius-context
layout: provider
modified: 2026-06-13
name: Sylius
nav: Providers
network: true
overview: 'Sylius publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include E-Commerce, Open-Source, Headless Commerce, REST API, and Symfony.


  The Sylius catalog on APIs.io includes 1 JSON-LD context.


  Sylius'' developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Sylius Plans Pricing
  plan_count: 4
  slug: sylius-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Sylius Rate Limits
  slug: sylius-rate-limits
score:
  band: emerging
  composite: 25.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 33.3
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sylius/refs/heads/main/screenshots/sylius-2026-06-20T194814.png
security:
- kind: domain-security
  name: Sylius Domain Security
  slug: sylius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sylius
tags:
- E-Commerce
- Open-Source
- Headless Commerce
- REST API
- Symfony
- PHP
- Product
- Order
- Payments
- Shipments
- Customers
website: https://sylius.com/
---
