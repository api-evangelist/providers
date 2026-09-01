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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: API related to audio projects
  name: Magic Hour Audio Projects API
  slug: magichour-audio-projects-api
- description: API related to uploading assets used for video generation
  name: Magic Hour Files API
  slug: magichour-files-api
- description: API related to image projects
  name: Magic Hour Image Projects API
  slug: magichour-image-projects-api
- description: API related to video projects
  name: Magic Hour Video Projects API
  slug: magichour-video-projects-api
artifact_total: 4
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/magichour-llms.txt
- group: company
  title: ''
  type: Website
  url: https://magichour.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.magichour.ai
created: '2026-08-22'
description: Magic Hour is an AI media generation platform for video, image and audio, exposed as a public REST API. The contract is an OpenAPI 3.0 document of 33 paths and 36 operations served from api.magichour.ai with bearer authentication, covering generators for headshots, clothes changing, face editing, GIFs, image editing and upscaling, plus video and audio synthesis. Operations are priced in credits and the documentation states the credit cost per call. Magic Hour publishes two llms.txt files — one on the marketing site and a different one on the docs host — plus a 653KB llms-full.txt, and documents an HMAC-SHA256 signed webhook surface with a full event-type reference.
layout: provider
modified: '2026-08-22'
name: Magic Hour
nav: Providers
network: true
overview: Magic Hour publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Audio Projects API, Files API, Image Projects API, and 1 more. Tagged areas include AI Video, Image-Generation, Audio, and Generative AI.
random_paper: 14
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 2
    catalog_gap: 85.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 50.0
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 31.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
slug: magichour
tags:
- AI Video
- Image-Generation
- Audio
- Generative AI
website: https://magichour.ai
---
