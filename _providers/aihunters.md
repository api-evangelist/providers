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
  scored_at: '2026-09-21'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://aihunters.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AIHunters
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/aihunters
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aihunters/refs/heads/main/lifecycle/aihunters-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aihunters-lifecycle.yml
coverage:
  checked: '2026-09-14'
  detail: 'AIHunters no longer operates: it rebranded to GrayPaw, Linque acquired its Cognitive Vision AI IP on 2026-02-15, and both aihunters.com and cognitivemill.com now answer every path — including a negative-control path that cannot exist — with a blanket HTTP 301 to the acquirer''s site at linque.com, while the Cognitive Mill REST API host api.cognitivemill.com has no DNS record at all and the only archived capture of its Swagger UI never included the spec document it loaded.'
  evidence:
  - status: 301
    url: https://aihunters.com/.well-known/security.txt
  - status: 301
    url: https://cognitivemill.com/openapi.json
  - status: 301
    url: https://aihunters.com/.well-known/aihunters-negative-control-7f3ab91c.json
  - status: 0
    url: https://api.cognitivemill.com/swagger/index.html
  - status: 200
    url: https://github.com/AIHunters
  - status: 200
    url: https://www.linque.com/
  reason: defunct
  state: none
created: '2026-09-14'
description: 'AIHunters was an AI and computer-vision company that built Cognitive Mill, a cognitive computing cloud platform for Media and Entertainment automation. Cognitive Mill analyzed long-form video with human-like scene understanding and shipped as branded services: CognitiveReelz (automated sports highlights and movie summarization), CognitiveSkip (end-credits detection for EPG correction), CognitiveCrop (cropping to portrait/mobile aspect), CognitiveCast (celebrity face-recognition metadata), CognitiveNude (nudity filtering) and CognitiveShapes (broadcast graphics detection). It exposed a public REST API at api.cognitivemill.com behind a Swagger UI. The company later became GrayPaw and pivoted to industrial cognitive vision; in February 2026 Linque acquired the Cognitive Vision AI IP. Both aihunters.com and cognitivemill.com now redirect to linque.com and the Cognitive Mill API host no longer resolves.'
layout: provider
modified: '2026-09-14'
name: AIHunters
nav: Providers
network: true
overview: AIHunters is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Computer-Vision, Video, Media, and Entertainment.
random_paper: 11
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 2.6
  previous_composite: 5.0
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: aihunters
tags:
- Artificial Intelligence
- Computer-Vision
- Video
- Media
- Entertainment
- Machine-Learning
- Content Automation
- Video Analysis
website: https://aihunters.com/
---
