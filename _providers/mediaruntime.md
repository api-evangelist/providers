---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: Public capability and contract discovery.
  name: MediaRuntime Discovery API
  slug: mediaruntime-discovery-api
- description: Redeem completed job output bundles.
  name: MediaRuntime Job Results API
  slug: mediaruntime-job-results-api
- description: Create, list, and inspect asynchronous media jobs.
  name: MediaRuntime Jobs API
  slug: mediaruntime-jobs-api
- description: Read analysis reports produced by requested presets.
  name: MediaRuntime Media Analysis API
  slug: mediaruntime-media-analysis-api
- description: The MediaRuntime API API from MediaRuntime — 0 operation(s) for mediaruntime api.
  name: MediaRuntime MediaRuntime API
  slug: mediaruntime-mediaruntime-api-api
- description: Read a job's requested moderation verdict.
  name: MediaRuntime Moderation API
  slug: mediaruntime-moderation-api
- description: Manage immutable, account-scoped processing recipes.
  name: MediaRuntime Recipes API
  slug: mediaruntime-recipes-api
- description: Create a bounded public-sandbox session.
  name: MediaRuntime Sandbox API
  slug: mediaruntime-sandbox-api
- description: Optional upload targets for local media bytes.
  name: MediaRuntime Uploads API
  slug: mediaruntime-uploads-api
- description: Configure the account watermark logo.
  name: MediaRuntime Watermarks API
  slug: mediaruntime-watermarks-api
- description: Retry delivery of signed terminal events.
  name: MediaRuntime Webhooks API
  slug: mediaruntime-webhooks-api
artifact_total: 11
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/mediaruntime-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://mediaruntime.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mediaruntime.com/docs
created: '2026-08-26'
description: MediaRuntime is a media-processing API. The published contract is an OpenAPI 3.1 document of 17 paths, 20 operations and 72 schemas served from mediaruntime.com, with two credential types — a production API key and a separate sandbox token, so callers can exercise the surface without touching production.
layout: provider
modified: '2026-08-26'
name: MediaRuntime
nav: Providers
network: true
overview: MediaRuntime publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Job Results API, Jobs API, and 8 more. Tagged areas include Media Processing, Video, Audio, and runtime.
random_paper: 3
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 2
    catalog_gap: 85.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 52.2
    developer_ergonomics: 26.2
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 25.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: mediaruntime
tags:
- Media Processing
- Video
- Audio
- runtime
website: https://mediaruntime.com
---
