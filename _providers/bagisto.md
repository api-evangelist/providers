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
    auth_clarity: bearer
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
  score: 18.0
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'RESTful API for managing all Bagisto e-commerce operations including products, categories, customers, orders, inventory, cart, checkout, and administrative functions. Provides separate Shop and Admin '
  name: Bagisto REST API
  slug: bagisto-rest-api
- description: GraphQL API for Bagisto providing flexible query-based access to storefront and catalog data as an alternative to the REST API.
  name: Bagisto GraphQL API
  slug: bagisto-graphql-api
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bagisto/bagisto/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/bagisto/bagisto/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/bagisto/bagisto/blob/2.4/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/bagisto/bagisto/blob/2.4/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/bagisto/bagisto/blob/2.4/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/bagisto/bagisto/blob/2.4/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bagisto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bagisto.com/en/
- group: docs
  title: ''
  type: Documentation
  url: https://devdocs.bagisto.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/bagisto
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bagisto/bagisto
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bagisto/rest-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bagisto/
- group: company
  title: ''
  type: Blog
  url: https://bagisto.com/en/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://bagisto.com/en/cloud-hosting/
- group: other
  title: ''
  type: X
  url: https://x.com/BagistoShop
- group: operate
  title: ''
  type: Forums
  url: https://forums.bagisto.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/bagisto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bagisto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bagisto-finops.yml
created: '2026-06-13'
description: Bagisto is a free and open-source Laravel e-commerce platform that provides REST and GraphQL APIs for managing products, categories, customers, orders, inventory, carts, and multi-channel selling. Built on Laravel Sanctum, the API offers both a public Storefront API and a full-control Admin API, making it suitable for headless commerce, mobile apps, and third-party integrations.
finops:
- name: Bagisto Finops
  service_category: ''
  slug: bagisto-finops
graphqls:
- description: Bagisto provides a GraphQL API built on the [Lighthouse](https://lighthouse-php.com/) PHP GraphQL server library. The API covers both a **Shop API** (storefront, public and authenticated customer oper
  name: Bagisto GraphQL API
  slug: bagisto-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bagisto.png
layout: provider
modified: '2026-06-13'
name: Bagisto
nav: Providers
network: true
overview: 'Bagisto publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include E-Commerce, Laravel, Open-Source, Product, and Order.


  Bagisto''s developer surface includes documentation, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Bagisto Plans Pricing
  plan_count: 3
  slug: bagisto-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Bagisto Rate Limits
  slug: bagisto-rate-limits
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 63.2
  open_source:
    applies: true
    score: 100.0
  previous_composite: 46.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bagisto/refs/heads/main/screenshots/bagisto-2026-06-20T172936.png
security:
- kind: domain-security
  name: Bagisto Domain Security
  slug: bagisto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bagisto
tags:
- E-Commerce
- Laravel
- Open-Source
- Product
- Order
- Customers
- Inventory
- Multi-Channel
- Headless Commerce
website: https://bagisto.com/en/
---
