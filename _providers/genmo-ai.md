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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: The first-party access surface is the open-source model itself. The Mochi repo (Apache-2.0) ships a "simple composable API" in Python - MochiSingleGPUPipeline built from T5ModelFactory, DitModelFactor
  name: Genmo Mochi Pipeline (Self-Hosted OSS)
  slug: genmo-ai-mochi-pipeline-api
- description: 'Third-party hosted access to Genmo''s Mochi 1 via Replicate''s predictions API (model identifier genmoai/mochi-1). Runs on Nvidia H100 hardware, ~$0.42 per run, typically completing within 5 minutes at '
  name: Mochi 1 on Replicate (Third-Party Hosted)
  slug: genmo-ai-mochi-replicate-api
- description: Third-party hosted access to Mochi via fal.ai (model identifier fal-ai/mochi-v1), using fal's queue API - submit with prompt, negative_prompt, seed, enable_prompt_expansion, and num_frames, then check
  name: Mochi v1 on fal.ai (Third-Party Hosted)
  slug: genmo-ai-mochi-fal-api
artifact_total: 4
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genmoai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genmoai
- group: company
  title: ''
  type: Website
  url: https://www.genmo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/genmoai/mochi
- group: other
  title: ''
  type: Playground
  url: https://www.genmo.ai/play
- group: commercial
  title: ''
  type: Plans
  url: plans/genmo-ai-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.genmo.ai/blog
created: '2026-07-11'
description: 'Genmo is a San Francisco research lab building open-source video generation models. Its flagship release, Mochi 1, is an Apache-2.0 licensed 10B-parameter text-to-video diffusion model (AsymmDiT architecture) with strong prompt adherence and high-fidelity motion. Genmo does NOT publish a first-party hosted developer REST API. Programmatic access to Mochi comes in three honest forms: (1) the open-source model itself, self-hosted via the repo''s Python pipeline ("simple composable API"), CLI, Gradio UI, or ComfyUI; (2) third-party hosted inference APIs from partners such as Replicate and fal.ai; and (3) a credit-based consumer web app and Playground at genmo.ai/play. The endpoints documented here for hosted access are modeled from partner documentation and are not operated by Genmo.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/genmo-ai.png
layout: provider
modified: '2026-07-11'
name: Genmo
nav: Providers
network: true
overview: 'Genmo publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Video Generation, AI Video, Generative AI, Text-to-Video, and Open Source.


  Genmo''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Genmo Ai Plans Pricing
  plan_count: 5
  slug: genmo-ai-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 19.2
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 19.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
slug: genmo-ai
tags:
- Video Generation
- AI Video
- Generative AI
- Text-to-Video
- Open Source
- Mochi
- Diffusion Model
website: https://www.genmo.ai
---
