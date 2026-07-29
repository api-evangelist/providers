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
- acting_count: 4
  human_in_the_loop: 0
  name: Pika Agentic Access
  operation_count: 8
  slug: pika-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: The Fal Ai API from Pika — 8 operation(s) for fal ai.
  name: Pika Fal Ai API
  slug: pika-fal-ai-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pika-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pika-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pika-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://pika.art
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/models/fal-ai/pika/v2.2/text-to-video
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pika-Labs
- group: company
  title: ''
  type: Blog
  url: https://pika.art/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pika.art/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pika-labs
- group: other
  title: ''
  type: X
  url: https://x.com/pika_labs
- group: commercial
  title: ''
  type: Plans
  url: plans/pika-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pika-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pika-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/pika-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/pika-context.jsonld
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-12'
description: Pika is an AI-powered video generation platform that allows users and developers to create, edit, and transform video content using natural language prompts, images, and existing video clips. The platform employs advanced diffusion models to produce short-form videos with realistic motion, smooth camera transitions, and detailed scene composition. Pika offers a suite of AI video tools including text-to-video, image-to-video, scene building (Pikascenes), keyframe interpolation (Pikaframes), and specialized transformation features such as Pikaffects, Pikaswaps, and Pikadditions. Developer API access is provided through a partnership with fal.ai, enabling programmatic integration of Pika's Pika 2.2 video models into applications and workflows.
examples:
- key_count: 5
  name: Pika Image To Video Example
  slug: pika-image-to-video-example
- key_count: 5
  name: Pika Text To Video Example
  slug: pika-text-to-video-example
finops:
- name: Pika Finops
  service_category: ''
  slug: pika-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pika.png
json_schemas:
- name: PikaVideoRequest
  property_count: 7
  slug: pika-video-request
- name: PikaVideoResponse
  property_count: 1
  slug: pika-video-response
jsonld:
- class_count: 5
  name: Pika Context
  property_count: 23
  slug: pika-context
layout: provider
modified: '2026-06-12'
name: Pika
nav: Providers
network: true
overview: 'Pika publishes 1 API on the [APIs.io](https://apis.io/) network: Fal Ai API. Tagged areas include AI, Video Generation, Text-to-Video, Image-to-Video, and Diffusion Models.


  The Pika catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pika''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Pika Plans Pricing
  plan_count: 5
  slug: pika-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Pika Rate Limits
  slug: pika-rate-limits
rules:
- name: Pika API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pika-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.7
  delta: -5.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.2
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 55.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/pika/refs/heads/main/screenshots/pika-2026-06-20T191705.png
security:
- kind: authentication
  name: Pika Authentication
  slug: pika-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pika Domain Security
  slug: pika-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pika
tags:
- AI
- Video Generation
- Text-to-Video
- Image-to-Video
- Diffusion Models
- Generative AI
- Media
- Creative Tools
website: https://pika.art
---
