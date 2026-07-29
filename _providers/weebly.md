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
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful API for managing Weebly sites, pages, blog posts, e-commerce products, orders, customers, coupons, categories, and form submissions. Supports OAuth 2.0 authentication and JSON data exchange. R
  name: Weebly REST API
  slug: weebly-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weebly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.weebly.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.weebly.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/weebly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/weebly
- group: company
  title: ''
  type: Blog
  url: https://www.weebly.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.weebly.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://weebly.statuspage.io
- group: other
  title: ''
  type: X
  url: https://x.com/weebly
- group: commercial
  title: ''
  type: Plans
  url: plans/weebly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/weebly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/weebly-finops.yml
created: '2026-06-13'
description: Weebly (a Square company) is a website and e-commerce builder providing REST APIs for managing sites, pages, products, orders, customers, blog posts, and custom form submissions. The platform serves over 50 million websites and offers OAuth 2.0-authenticated REST endpoints for building apps and integrations on top of Weebly-powered storefronts and sites.
finops:
- name: Weebly Finops
  service_category: ''
  slug: weebly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weebly.png
jsonld:
- class_count: 0
  name: Weebly Context
  property_count: 43
  slug: weebly-context
layout: provider
modified: '2026-06-13'
name: Weebly
nav: Providers
network: true
overview: 'Weebly publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Website Builder, E-Commerce, Blogging, Sites, and Pages.


  The Weebly catalog on APIs.io includes 1 JSON-LD context.


  Weebly''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Weebly Plans Pricing
  plan_count: 4
  slug: weebly-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Weebly Rate Limits
  slug: weebly-rate-limits
score:
  band: thin
  composite: 33.1
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weebly/refs/heads/main/screenshots/weebly-2026-06-20T201342.png
security:
- kind: domain-security
  name: Weebly Domain Security
  slug: weebly-domain-security
  summary_line: TLSv1.3 · DMARC
slug: weebly
tags:
- Website Builder
- E-Commerce
- Blogging
- Sites
- Pages
- Products
- Orders
- Customers
- Square
website: https://www.weebly.com
---
