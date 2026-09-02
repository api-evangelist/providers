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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-01'
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
  name: Listings API MCP Server
  slug: listings-api-mcp-server
modified: '2026-07-12'
name: Listings API
nav: Providers
network: true
overview: 'Listings API publishes 1 API on the [APIs.io](https://apis.io/) network: Listings API. Tagged areas include Business Listings, Local SEO, Locations, Reviews, and Google Business Profile.'
random_paper: 18
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 1
    catalog_gap: 81.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 9.5
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  previous_composite: 14.9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/listings-api/refs/heads/main/screenshots/listings-api-2026-07-25T225325.png
slug: listings-api
tags:
- Business Listings
- Local SEO
- Locations
- Reviews
- Google Business Profile
- Analytics
- citation-management
- Local Marketing
- social-publishing
- MCP
- agent-native
---
