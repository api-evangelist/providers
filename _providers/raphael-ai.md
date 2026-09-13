---
agent_readiness:
  band: human-only
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-12'
api_count: 1
apis:
- description: Consumer AI image and video generation product. No public API is offered yet (stated as coming in the near future); the only machine-readable surface is an llms.txt product/marketing discovery index.
  name: Raphael AI
  slug: raphael-ai
artifact_total: 1
created: '2026-09-12'
description: A free, no-signup AI image and video generator (text-to-image, image-to-image, image editing, outpaint, background removal, text-to-video, image-to-video) that aggregates multiple underlying models. Currently exposes an llms.txt but no public API, MCP server, or agent skills.
layout: provider
modified: '2026-09-12'
name: Raphael AI
nav: Providers
network: true
overview: Raphael AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, image generation, text-to-image, image-to-image, and image editing.
random_paper: 14
score:
  band: minimal
  composite: 8.6
  coverage:
    artifact_dirs: 0
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: raphael-ai
tags:
- AI
- image generation
- text-to-image
- image-to-image
- image editing
- video generation
- generative media
- model aggregator
---
