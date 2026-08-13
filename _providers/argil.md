---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Argil Agentic Access
  operation_count: 20
  slug: argil-agentic-access
  summary_line: 20 operations · 11 acting
api_count: 5
apis:
- description: Upload and manage B-roll and media assets.
  name: Argil Assets API
  slug: argil-assets-api
- description: Create and list avatars and digital twins.
  name: Argil Avatars API
  slug: argil-avatars-api
- description: Create, render, and manage avatar videos.
  name: Argil Videos API
  slug: argil-videos-api
- description: Clone, list, and sync voices.
  name: Argil Voices API
  slug: argil-voices-api
- description: Register and manage render-event webhooks.
  name: Argil Webhooks API
  slug: argil-webhooks-api
artifact_total: 12
collections:
- collection_type: open
  name: Argil API
  slug: open-argil
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/argil-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/argil-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/argil-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/argil-ai
- group: company
  title: ''
  type: Website
  url: https://www.argil.ai/
- group: company
  title: ''
  type: Blog
  url: https://www.argil.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.argil.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/argil-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/argil-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/argil-finops.yml
created: '2026-07-01'
description: Argil (Argil AI) is an AI avatar video generation platform for the creator economy. Its API programmatically produces talking-avatar videos from text or audio, clones custom avatars and voices, manages B-roll assets, and delivers render events via webhooks - turning a script into a finished, subtitled avatar video.
finops:
- name: Argil Finops
  service_category: AI and Machine Learning
  slug: argil-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/argil.png
layout: provider
modified: '2026-07-01'
name: Argil
nav: Providers
network: true
overview: 'Argil publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Avatars API, Videos API, and 2 more. Tagged areas include AI, Video Generation, Avatars, Voice Cloning, and Content Automation.


  Argil''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Argil Plans Pricing
  plan_count: 4
  slug: argil-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Argil Rate Limits
  slug: argil-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/argil/refs/heads/main/screenshots/argil-2026-07-25T201139.png
security:
- kind: authentication
  name: Argil Authentication
  slug: argil-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Argil Domain Security
  slug: argil-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: argil
tags:
- AI
- Video Generation
- Avatars
- Voice Cloning
- Content Automation
website: https://www.argil.ai/
---
