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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: A GraphQL API providing access to Product Hunt's platform data including daily product launches, votes, comments, maker profiles, topics, and collections. Supports OAuth 2.0 authentication with public
  name: Product Hunt GraphQL API
  slug: product-hunt-graphql-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/producthunt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.producthunt.com/
- group: other
  title: ''
  type: Developer
  url: https://api.producthunt.com/v2/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/producthunt
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/producthunt/producthunt-api
- group: other
  title: ''
  type: Dashboard
  url: https://www.producthunt.com/v2/oauth/applications
- group: operate
  title: ''
  type: Support
  url: https://help.producthunt.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.producthunt.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.producthunt.com/legal/privacy
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/producthunt/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/producthunt/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/producthunt/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Product Hunt is a product discovery platform providing a GraphQL API for accessing product launches, votes, comments, maker profiles, and collection data from the Product Hunt community. Developers can query posts, users, topics, and collections, and with approval, perform write operations such as posting comments and managing goals.
finops:
- name: Finops
  service_category: ''
  slug: finops
graphqls:
- description: The Product Hunt GraphQL API (V2) provides access to the full Product Hunt platform, exposing product launches (Posts), voting data, comments, user profiles, topics, collections, maker groups, and mak
  name: Product Hunt GraphQL API
  slug: producthunt-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/producthunt.png
layout: provider
modified: '2026-06-13'
name: Product Hunt
nav: Providers
network: true
overview: 'Product Hunt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Product Discovery, GraphQL, Community, Products, and Startups.


  Product Hunt''s developer surface includes support and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 60
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 25.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/producthunt/refs/heads/main/screenshots/producthunt-2026-06-20T192141.png
security:
- kind: domain-security
  name: Producthunt Domain Security
  slug: producthunt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: producthunt
tags:
- Product Discovery
- GraphQL
- Community
- Products
- Startups
- Launches
- Voting
- Tech
website: https://www.producthunt.com/
---
