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
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Public capability and contract discovery.
  name: MediaRuntime Discovery API
  slug: mediaruntime-discovery-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Redeem completed job output bundles.
  name: MediaRuntime Job Results API
  slug: mediaruntime-job-results-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Create, list, and inspect asynchronous media jobs.
  name: MediaRuntime Jobs API
  slug: mediaruntime-jobs-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Read analysis reports produced by requested presets.
  name: MediaRuntime Media Analysis API
  slug: mediaruntime-media-analysis-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: The MediaRuntime API API from MediaRuntime — 0 operation(s) for mediaruntime api.
  name: MediaRuntime MediaRuntime API
  slug: mediaruntime-mediaruntime-api-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Read a job's requested moderation verdict.
  name: MediaRuntime Moderation API
  slug: mediaruntime-moderation-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Manage immutable, account-scoped processing recipes.
  name: MediaRuntime Recipes API
  slug: mediaruntime-recipes-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Create a bounded public-sandbox session.
  name: MediaRuntime Sandbox API
  slug: mediaruntime-sandbox-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Optional upload targets for local media bytes.
  name: MediaRuntime Uploads API
  slug: mediaruntime-uploads-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Configure the account watermark logo.
  name: MediaRuntime Watermarks API
  slug: mediaruntime-watermarks-api
- baseURL: https://mediaruntime.com
  baseurl_source: declared
  description: Retry delivery of signed terminal events.
  name: MediaRuntime Webhooks API
  slug: mediaruntime-webhooks-api
- description: Versioned REST API (under /v1) for media-processing jobs, reports/analysis, reusable recipes, uploads/watermarking, and runtime capability discovery. Auth via X-API-Key (production) or X-Sandbox-Token
  name: MediaRuntime API
  slug: mediaruntime-api
artifact_total: 12
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
overview: MediaRuntime publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Job Results API, Jobs API, and 9 more. Tagged areas include Media Processing, Video, Audio, and Runtime.
random_paper: 3
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 52.2
    developer_ergonomics: 26.2
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mediaruntime/refs/heads/main/screenshots/mediaruntime-2026-09-02T150453.png
slug: mediaruntime
tags:
- Media Processing
- Video
- Audio
- Runtime
website: https://mediaruntime.com
---
