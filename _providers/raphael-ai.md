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
  scored_at: '2026-09-15'
api_count: 1
apis:
- description: Consumer AI image and video generation product. No public API is offered yet (stated as coming in the near future); the only machine-readable surface is an llms.txt product/marketing discovery index.
  name: Raphael AI
  slug: raphael-ai
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://raphael.app
- group: commercial
  title: ''
  type: Pricing
  url: https://raphael.app/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://raphael.app/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://raphael.app/tos
coverage:
  checked: '2026-09-13'
  detail: Raphael AI is a consumer AI image/video web app; its own pricing FAQ states "we don't have a public API at the moment but will be offering one in the near future," and no API host exists (api.raphael.app is NXDOMAIN). The only machine-readable surface is a marketing llms.txt.
  evidence:
  - status: 200
    url: https://raphael.app/pricing
  - status: 404
    url: https://raphael.app/openapi.json
  - status: 404
    url: https://raphael.app/mcp
  - status: 404
    url: https://raphael.app/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: A free, no-signup AI image and video generator (text-to-image, image-to-image, image editing, outpaint, background removal, text-to-video, image-to-video) that aggregates multiple underlying models (Nano Banana, Seedream, GPT Image, Veo, Kling and more). Currently exposes an llms.txt product/marketing index but no public API, MCP server, or agent skills; the provider states a public API is planned for the near future.
layout: provider
modified: '2026-09-13'
name: Raphael AI
nav: Providers
network: true
overview: 'Raphael AI publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Image-Generation, Text-to-Image, Image to Image, and Image Editing.


  Raphael AI''s developer surface includes pricing and 3 more developer resources.'
plans:
- name: Raphael Ai Plans Pricing
  plan_count: 4
  slug: raphael-ai-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 3
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 72.2
    operational_transparency: 0.0
  previous_composite: 19.9
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: raphael-ai
tags:
- Artificial Intelligence
- Image-Generation
- Text-to-Image
- Image to Image
- Image Editing
- Video Generation
- Generative Media
- Model Aggregator
website: https://raphael.app
---
