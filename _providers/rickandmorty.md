---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
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
api_count: 2
apis:
- description: RESTful API providing access to characters, locations, and episodes from the Rick and Morty animated series. Returns paginated JSON responses with up to 20 results per page.
  name: Rick and Morty REST API
  slug: rick-and-morty-rest-api
- description: GraphQL endpoint for querying Rick and Morty characters, locations, and episodes with flexible field selection and filtering.
  name: Rick and Morty GraphQL API
  slug: rick-and-morty-graphql-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rickandmorty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rickandmortyapi.com
- group: docs
  title: ''
  type: Documentation
  url: https://rickandmortyapi.com/documentation
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/afuh
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/afuh/rick-and-morty-api
- group: company
  title: ''
  type: Blog
  url: https://github.com/afuh/rick-and-morty-api/blob/master/CHANGELOG.md
- group: commercial
  title: ''
  type: Pricing
  url: https://rickandmortyapi.com/support-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rickandmortyapi.com
- group: commercial
  title: ''
  type: Plans
  url: plans/rickandmorty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rickandmorty-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rickandmorty-finops.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/afuh/rick-and-morty-api/blob/master/LICENSE
created: '2026-06-13'
description: Free REST and GraphQL API providing data about characters, locations, and episodes from the Rick and Morty animated series. No authentication required. Offers access to 826 characters, 126 locations, and 51 episodes with filtering, pagination, and character images.
finops:
- name: Rickandmorty Finops
  service_category: ''
  slug: rickandmorty-finops
graphqls:
- description: The Rick and Morty GraphQL API provides a flexible query interface for accessing data from the Rick and Morty animated series. It exposes three core data types — Character, Location, and Episode — and
  name: Rick and Morty GraphQL API
  slug: rickandmorty-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rickandmorty.png
layout: provider
modified: '2026-06-13'
name: Rick and Morty API
nav: Providers
network: true
overview: 'Rick and Morty API publishes 1 API on the [APIs.io](https://apis.io/) network: Rick and Morty REST API. Tagged areas include Rick and Morty, Characters, Episodes, Locations, and Entertainment.


  Rick and Morty API''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Rickandmorty Plans Pricing
  plan_count: 1
  slug: rickandmorty-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 2
  name: Rickandmorty Rate Limits
  slug: rickandmorty-rate-limits
score:
  band: thin
  composite: 31.7
  delta: -2.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 37.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 34.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rickandmorty/refs/heads/main/screenshots/rickandmorty-2026-06-20T193112.png
security:
- kind: domain-security
  name: Rickandmorty Domain Security
  slug: rickandmorty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rickandmorty
tags:
- Rick and Morty
- Characters
- Episodes
- Locations
- Entertainment
- GraphQL
- REST
- Free
- Open Source
website: https://rickandmortyapi.com
---
