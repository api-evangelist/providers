---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Pika's official developer access is not hosted by Pika. Pika partnered with fal to serve its Pika 2.2 video models on fal's inference infrastructure, so the pika.art/api page hands developers off to f
  name: Pika Video Generation API (via fal)
  slug: pika-art-video-generation-api
artifact_total: 3
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pika-labs
- group: company
  title: ''
  type: Website
  url: https://pika.art
- group: docs
  title: ''
  type: Documentation
  url: https://pika.art/api
- group: commercial
  title: ''
  type: Plans
  url: plans/pika-art-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pika-art-finops.yml
created: '2026-07-11'
description: Pika (Pika Labs) is a generative AI video platform that turns text prompts and images into short, high-quality videos. Pika is primarily a consumer and creator product delivered through its web app at pika.art (and historically a Discord bot), with features such as text-to-video, image-to-video, Pikascenes, Pikaframes keyframe interpolation, lip sync, and AI sound effects. Pika does NOT publish a first-party developer API on its own domain. Its pika.art/api page is a landing page that directs developers to fal.ai, Pika's official inference partner, which hosts Pika's 2.x video models as callable API endpoints (for example fal-ai/pika/v2.2/text-to-video and fal-ai/pika/v2.2/image-to-video). Consumer access is sold as credit-based monthly subscriptions; programmatic access is billed per generation on fal. Various unofficial third-party wrappers (PiAPI, useapi.net, Pollo, and others) also resell Pika access but are not operated or endorsed by Pika.
finops:
- name: Pika Art Finops
  service_category: AI and Machine Learning
  slug: pika-art-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pika-art.png
layout: provider
modified: '2026-07-11'
name: Pika
nav: Providers
network: true
overview: 'Pika publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video Generation, AI Video, Generative AI, Text-to-Video, and Image-to-Video.


  Pika''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Pika Art Plans Pricing
  plan_count: 4
  slug: pika-art-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 16.7
  delta: 0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
slug: pika-art
tags:
- Video Generation
- AI Video
- Generative AI
- Text-to-Video
- Image-to-Video
- Creative
website: https://pika.art
---
