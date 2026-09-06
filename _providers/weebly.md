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
  scored_at: '2026-09-05'
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
random_paper: 18
rate_limits:
- limit_count: 1
  name: Weebly Rate Limits
  slug: weebly-rate-limits
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 68.0
    catalog_earned_first_party: 0.0
    catalog_gap: 47.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 37.3
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 32.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Product
- Order
- Customers
- Square
website: https://www.weebly.com
---
