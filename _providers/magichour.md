---
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
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.4
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: AI generation of video, image and audio — headshots, clothes changer, face editor, GIF generator, image editor and upscaler among 36 operations. Bearer auth, credit-priced.
  name: Magic Hour API
  slug: magichour-api
artifact_total: 1
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
overview: Magic Hour publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Media Generation, Video, Image, and Audio.
random_paper: 14
score:
  band: emerging
  composite: 22.6
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 53.8
    developer_ergonomics: 9.5
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
slug: magichour
tags:
- AI
- Media Generation
- Video
- Image
- Audio
- Generative AI
- Webhooks
website: https://magichour.ai
---
