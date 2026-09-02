---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 6
apis:
- description: Read-optimized GraphQL API for fetching structured product data, shapes, topics, price variants, stock, and rich content for storefronts. Queries are scoped to a tenant identifier and return path-base
  name: Crystallize Catalogue API
  slug: catalogue-api
- description: Semantic GraphQL API combining browse, search, and autocomplete in a single endpoint. Supports filtering, faceting, ranking, and rich product discovery experiences for storefronts.
  name: Crystallize Discovery / Search API
  slug: discovery-search-api
- description: Edge-distributed GraphQL API for cart, promotions, and checkout flows. Optimized for low-latency storefront writes during the buying journey.
  name: Crystallize Shop API
  slug: shop-api
- description: GraphQL API for creating, reading, and managing orders linked to a Crystallize tenant. Used by storefronts and back-office tooling to persist completed transactions.
  name: Crystallize Order API
  slug: order-api
- description: GraphQL API for managing recurring orders, subscription contracts, and renewal events for Crystallize-powered commerce experiences.
  name: Crystallize Subscription API
  slug: subscription-api
- description: 'Read/write GraphQL API for managing the product information model: shapes, items, topics, language, price variants, stock locations, and tenant configuration. Powers PIM tooling and back-office automa'
  name: Crystallize Core / PIM API
  slug: core-pim-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crystallize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crystallize.com
- group: start
  title: ''
  type: Portal
  url: https://crystallize.com/learn
- group: docs
  title: ''
  type: Documentation
  url: https://crystallize.com/learn
- group: start
  title: ''
  type: Signup
  url: https://crystallize.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.crystallize.com
- group: commercial
  title: ''
  type: Pricing
  url: https://crystallize.com/plans
- group: company
  title: ''
  type: Blog
  url: https://crystallize.com/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/CrystallizeAPI
- group: build
  title: ''
  type: SDKs
  url: https://crystallize.com/learn/open-source/sdks-and-libraries/js-api-client
- group: build
  title: ''
  type: CLI
  url: https://crystallize.com/learn/open-source/cli
- group: other
  title: ''
  type: Playground
  url: https://crystallize.com/learn/developer-guides/query-explorer/graphql-playground
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crystallize.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crystallize.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crystallize.com
- group: agent
  title: ''
  type: LlmsText
  url: https://crystallize.com/llms.txt
created: '2026-05-23'
description: Crystallize is a headless product information management (PIM) and commerce platform built around a set of GraphQL APIs. It separates product storytelling from the commerce engine, exposing a Catalogue API for reading structured product data, a Discovery (Search) API for browse and search, a Shop API for cart and checkout, an Order/Subscription API, and a Core/PIM API for managing shapes, items, and tenants.
finops:
- name: Crystallize Finops
  service_category: API
  slug: crystallize-finops
graphqls:
- description: Read-optimized GraphQL API for fetching structured product data, shapes, topics, price variants, stock, and rich content for storefronts. Queries are scoped to a tenant identifier and return path-base
  name: Crystallize GraphQL API
  slug: crystallize-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crystallize.png
layout: provider
modified: '2026-05-23'
name: Crystallize
nav: Providers
network: true
overview: 'Crystallize publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Commerce, Headless Commerce, Product Information Management, PIM, and GraphQL.


  Crystallize''s developer surface includes developer portal, documentation, signup flow, pricing, engineering blog, GitHub presence, CLI, and 9 more developer resources.'
plans:
- name: Crystallize Plans Pricing
  plan_count: 1
  slug: crystallize-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Crystallize Rate Limits
  slug: crystallize-rate-limits
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 27.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crystallize/refs/heads/main/screenshots/crystallize-2026-06-20T175316.png
security:
- kind: domain-security
  name: Crystallize Domain Security
  slug: crystallize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crystallize
tags:
- Commerce
- Headless Commerce
- Product Information Management
- PIM
- GraphQL
- Catalog
- Search
- Order
- Subscription
website: https://crystallize.com
---
