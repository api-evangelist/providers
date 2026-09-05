---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-04'
api_count: 5
apis:
- baseURL: https://api.vectorizer.ai/api/v1
  baseurl_source: declared
  description: Account status and API credit information.
  name: Vectorizer.AI Account API
  slug: vectorizer-ai-account-api
- baseURL: https://api.vectorizer.ai/api/v1
  baseurl_source: declared
  description: Vectorize images, download retained results, and delete retained images.
  name: Vectorizer.AI Vectorization API
  slug: vectorizer-ai-vectorization-api
artifact_total: 2
created: '2026-08-28'
description: 'Vectorizer.AI converts raster bitmap images into vector artwork through a production HTTP API, returning SVG, PDF, EPS, DXF and PNG. The API is small and single-purpose: four operations covering vectorization, download of a previously vectorized result, deletion, and an account endpoint for checking subscription and credit state. Authentication is HTTP Basic, using an API Id as the username and an API Secret as the password. The company publishes its own APIs.json discovery document at vectorizer.ai/apis.json and a first-party OpenAPI 3.0.3 description at vectorizer.ai/api/openapi.json, alongside official SDKs, a cross-platform CLI, a public Postman workspace, and separately documented error codes and rate limits. The service is operated by Cedar Lake Ventures, Inc.'
image: https://d1j8j7mb8gx2ao.cloudfront.net/p/assets/images/open-graph_7edfc602c1a14fb37dcd46e3fa5503f1.png
layout: provider
modified: '2026-08-28'
name: Vectorizer.AI
nav: Providers
network: true
overview: 'Vectorizer.AI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Account API and Vectorization API. Tagged areas include image vectorization, raster to vector, image conversion, SVG, and PDF.'
random_paper: 4
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 56.8
    developer_ergonomics: 52.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 34.2
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vectorizer-ai/refs/heads/main/screenshots/vectorizer-ai-2026-09-02T165542.png
slug: vectorizer-ai
tags:
- image vectorization
- raster to vector
- image conversion
- SVG
- PDF
- EPS
- dxf
---
