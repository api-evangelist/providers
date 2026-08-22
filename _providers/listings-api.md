---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API (OpenAPI 3.1) for managing locations, listings, connected accounts, reviews, posts, and analytics, with a hosted MCP server and llms.txt for agent-native access.
  name: Listings API
  slug: listings-api
artifact_total: 2
created: '2026-07-12'
description: REST API and agent-native platform for managing business listings, citations, reviews, Google Business Profile posts, and local analytics across major publisher directories (Google, Facebook, Bing, Yelp, TripAdvisor). A facade over Synup's federated GraphQL backend, with first-party Python and Node SDKs, a hosted MCP server, and llms.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/listings-api.png
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
modified: '2026-07-12'
name: Listings API
nav: Providers
network: true
overview: 'Listings API publishes 1 API on the [APIs.io](https://apis.io/) network: Listings API. Tagged areas include business-listings, local-seo, locations, reviews, and google-business-profile.'
random_paper: 18
score:
  band: emerging
  composite: 13.4
  delta: -1.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 0.0
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 14.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/listings-api/refs/heads/main/screenshots/listings-api-2026-07-25T225325.png
slug: listings-api
tags:
- business-listings
- local-seo
- locations
- reviews
- google-business-profile
- analytics
- citation-management
- local-marketing
- social-publishing
- mcp
- agent-native
---
