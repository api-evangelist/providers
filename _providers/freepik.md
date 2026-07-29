---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Freepik Agentic Access
  operation_count: 22
  slug: freepik-agentic-access
  summary_line: 22 operations · 19 acting
api_count: 6
apis:
- description: Generate music and sound effects.
  name: Freepik Audio API
  slug: freepik-audio-api
- description: Upscale, relight, restyle, or edit images.
  name: Freepik Image Editing API
  slug: freepik-image-editing-api
- description: Generate images from text or reference inputs.
  name: Freepik Image Generation API
  slug: freepik-image-generation-api
- description: Search Freepik's stock library.
  name: Freepik Resources API
  slug: freepik-resources-api
- description: Poll asynchronous task status.
  name: Freepik Tasks API
  slug: freepik-tasks-api
- description: Generate video from images or text.
  name: Freepik Video Generation API
  slug: freepik-video-generation-api
artifact_total: 13
collections:
- collection_type: open
  name: Freepik / Magnific API
  slug: open-freepik
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freepik-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freepik-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/freepik-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/freepik-company
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/freepik-company
- group: company
  title: ''
  type: Website
  url: https://www.freepik.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.freepik.com/
- group: start
  title: ''
  type: Signup
  url: https://www.freepik.com/profile/signup
created: '2025-01-07'
description: Freepik is a leading platform that provides high-quality graphic resources for designers, marketers, and creative professionals. Its developer platform (operated through Magnific) offers AI image, video, audio generation, image editing, and access to the Freepik stock library.
finops:
- name: Freepik Finops
  service_category: API
  slug: freepik-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freepik.png
layout: provider
modified: '2026-05-19'
name: Freepik
nav: Providers
network: true
overview: 'Freepik publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Image Editing API, Image Generation API, and 3 more. Tagged areas include AI, Graphics, Illustrations, Image Generation, and Photos.


  Freepik''s developer surface includes authentication, documentation, signup flow, and 5 more developer resources.'
plans:
- name: Freepik Plans Pricing
  plan_count: 3
  slug: freepik-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Freepik Rate Limits
  slug: freepik-rate-limits
score:
  band: thin
  composite: 37.6
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freepik/refs/heads/main/screenshots/freepik-2026-06-20T181529.png
security:
- kind: authentication
  name: Freepik Authentication
  slug: freepik-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Freepik Domain Security
  slug: freepik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: freepik
tags:
- AI
- Graphics
- Illustrations
- Image Generation
- Photos
- Video Generation
website: https://www.freepik.com/
---
