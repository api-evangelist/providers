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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: A GraphQL API providing access to Product Hunt's platform data including daily product launches, votes, comments, maker profiles, topics, and collections. Supports OAuth 2.0 authentication with public
  name: Product Hunt GraphQL API
  slug: product-hunt-graphql-api
artifact_total: 6
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/producthunt/producthunt-api/issues
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
overview: 'Product Hunt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Product Discovery, GraphQL, Community, Product, and Startups.


  Product Hunt''s developer surface includes support and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 19
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 8
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  open_source:
    applies: true
    score: 0.0
  previous_composite: 30.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- Product
- Startups
- Launches
- Voting
- Tech
website: https://www.producthunt.com/
---
