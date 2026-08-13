---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cj Affiliate Agentic Access
  operation_count: 4
  slug: cj-affiliate-agentic-access
  summary_line: 4 operations
api_count: 6
apis:
- description: Modern GraphQL API serving near-real-time commission and transaction data. The publisherCommissions and advertiserCommissions queries return commission records filtered by posting date range, action s
  name: CJ Commission Detail API
  slug: cj-affiliate-commission-detail-api
- description: Modern GraphQL API for product discovery across advertiser product feeds. The products and shoppingProducts queries search products you can promote by keyword, price range, currency, country / service
  name: CJ Product Search API
  slug: cj-affiliate-product-search-api
- description: The Advertiser Lookup API from CJ Affiliate — 1 operation(s) for advertiser lookup.
  name: CJ Affiliate Advertiser Lookup API
  slug: cj-affiliate-advertiser-lookup-api
- description: The Link Search API from CJ Affiliate — 1 operation(s) for link search.
  name: CJ Affiliate Link Search API
  slug: cj-affiliate-link-search-api
- description: The Product Search (Legacy) API from CJ Affiliate — 1 operation(s) for product search (legacy).
  name: CJ Affiliate Product Search (Legacy) API
  slug: cj-affiliate-product-search-legacy-api
- description: The Publisher Lookup API from CJ Affiliate — 1 operation(s) for publisher lookup.
  name: CJ Affiliate Publisher Lookup API
  slug: cj-affiliate-publisher-lookup-api
artifact_total: 14
collections:
- collection_type: open
  name: CJ Affiliate APIs
  slug: open-cj-affiliate
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cj-affiliate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cj-affiliate-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cj-affiliate-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cj.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cj-affiliate-by-conversant
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cj.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.cj.com/account/personal-access-tokens
- group: commercial
  title: ''
  type: Plans
  url: plans/cj-affiliate-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cj-affiliate-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cj-affiliate-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://junction.cj.com/
created: '2026-07-05'
description: CJ Affiliate (formerly Commission Junction) is one of the largest affiliate marketing networks, connecting publishers with thousands of advertiser programs. Its developer platform is primarily a modern GraphQL API - the Commission Detail API at commissions.api.cj.com and the Product Search / ads GraphQL API at ads.api.cj.com - covering commission and transaction data, product feeds, and advertiser discovery. A set of legacy REST APIs (Link Search, Advertiser Lookup, Publisher Lookup, and the legacy Product Search) remains documented for finding links, advertisers, publishers, and products. All APIs authenticate with a personal access token (Bearer) created in the CJ developer portal.
finops:
- name: Cj Affiliate Finops
  service_category: Marketing and Advertising
  slug: cj-affiliate-finops
graphqls:
- description: CJ Affiliate's modern developer surface is **GraphQL**. There are two documented
  name: CJ Affiliate GraphQL APIs
  slug: cj-affiliate-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cj-affiliate.png
layout: provider
modified: '2026-07-05'
name: CJ Affiliate
nav: Providers
network: true
overview: 'CJ Affiliate publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CJ Commission Detail API, Advertiser Lookup API, Link Search API, and 2 more. Tagged areas include Affiliate Marketing, Affiliate Network, Commission, Product Search, and Publisher.


  CJ Affiliate''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Cj Affiliate Plans Pricing
  plan_count: 2
  slug: cj-affiliate-plans-pricing
random_paper: 103
rate_limits:
- limit_count: 4
  name: Cj Affiliate Rate Limits
  slug: cj-affiliate-rate-limits
score:
  band: thin
  composite: 37.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cj-affiliate/refs/heads/main/screenshots/cj-affiliate-2026-07-25T205448.png
security:
- kind: authentication
  name: Cj Affiliate Authentication
  slug: cj-affiliate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cj Affiliate Domain Security
  slug: cj-affiliate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cj-affiliate
tags:
- Affiliate Marketing
- Affiliate Network
- Commission
- Product Search
- Publisher
- Advertiser
- GraphQL
- Ecommerce
website: https://www.cj.com/
---
