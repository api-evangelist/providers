---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Runwayml Agentic Access
  operation_count: 9
  slug: runwayml-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
apis:
- description: Drive a character with a reference performance (Act-Two).
  name: Runway Character Performance API
  slug: runwayml-character-performance-api
- description: Generate video from an image and prompt (Gen-4 Turbo, Gen-4.5).
  name: Runway Image-to-Video API
  slug: runwayml-image-to-video-api
- description: Usage tier and credit balance for the API organization.
  name: Runway Organization API
  slug: runwayml-organization-api
- description: Poll and cancel asynchronous generation tasks.
  name: Runway Tasks API
  slug: runwayml-tasks-api
- description: Generate images from a prompt (Gen-4 Image, Gen-4 Image Turbo).
  name: Runway Text-to-Image API
  slug: runwayml-text-to-image-api
- description: Synthesize speech audio from text.
  name: Runway Text-to-Speech API
  slug: runwayml-text-to-speech-api
- description: Upscale a video to higher resolution.
  name: Runway Upscale API
  slug: runwayml-upscale-api
- description: Edit / restyle an existing video (Aleph).
  name: Runway Video-to-Video API
  slug: runwayml-video-to-video-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Runway ML API
  slug: open-runway-ml
- collection_type: open
  name: Runway Character Performance API
  slug: open-runwayml-character-performance-api
- collection_type: open
  name: Runway Character Performance Image-to-Video API
  slug: open-runwayml-image-to-video-api
- collection_type: open
  name: Runway Character Performance Organization API
  slug: open-runwayml-organization-api
- collection_type: open
  name: Runway Character Performance Tasks API
  slug: open-runwayml-tasks-api
- collection_type: open
  name: Runway Character Performance Text-to-Image API
  slug: open-runwayml-text-to-image-api
- collection_type: open
  name: Runway Character Performance Text-to-Speech API
  slug: open-runwayml-text-to-speech-api
- collection_type: open
  name: Runway Character Performance Upscale API
  slug: open-runwayml-upscale-api
- collection_type: open
  name: Runway Character Performance Video-to-Video API
  slug: open-runwayml-video-to-video-api
- collection_type: open
  name: Runway API
  slug: open-runwayml
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/runwayml-agentic-access.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/runwayml
- group: company
  title: ''
  type: Website
  url: https://runwayml.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dev.runwayml.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/runwayml-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/runwayml-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/runwayml-finops.yml
- group: start
  title: ''
  type: SignUp
  url: https://dev.runwayml.com/
- group: company
  title: ''
  type: Blog
  url: https://runwayml.com/research
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runwayml-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/runwayml-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runwayml
- group: commercial
  title: ''
  type: Pricing
  url: https://runwayml.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runwayml.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runwayml.com/privacy-policy
- group: other
  title: ''
  type: X
  url: https://x.com/runwayml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dev.runwayml.com/llms.txt
created: '2026-07-11'
description: Runway (RunwayML) is a generative AI media platform whose developer API turns text, images, and video into new video, images, speech, and character performances. The REST API at https://api.dev.runwayml.com/v1 exposes Runway's Gen-4 and Gen-4 Turbo video models, Gen-4 Image text-to-image, the Aleph video-to-video editing model, and Act character performance, all through an asynchronous create-task-then-poll pattern authenticated with a Bearer API secret and a dated X-Runway-Version header. Access is API-key based via a developer organization; usage is billed in credits at roughly $0.01 per credit.
finops:
- name: Runwayml Finops
  service_category: AI and Machine Learning
  slug: runwayml-finops
graphqls:
- description: Runway is a generative AI research company building creative tools for video, image, and audio production. Its Gen-4 family of models (and the legacy Gen-3 Alpha family) powers text-to-video, image-to
  name: Runway ML GraphQL Schema
  slug: runwayml-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runwayml.png
layout: provider
modified: '2026-08-08'
name: Runway
nav: Providers
network: true
overview: 'Runway publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Character Performance API, Image-to-Video API, Organization API, and 5 more. Tagged areas include Video Generation, AI Video, Generative AI, Text-to-Video, and Image-to-Video.


  Runway''s developer surface includes documentation, signup flow, engineering blog, authentication, pricing, and 12 more developer resources.'
plans:
- name: Runwayml Plans Pricing
  plan_count: 2
  slug: runwayml-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Runwayml Rate Limits
  slug: runwayml-rate-limits
score:
  band: developing
  composite: 46.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 0.0
    contract_quality: 60.8
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runwayml/refs/heads/main/screenshots/runwayml-2026-06-20T193258.png
security:
- kind: authentication
  name: Runwayml Authentication
  slug: runwayml-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Runwayml Domain Security
  slug: runwayml-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: runwayml
tags:
- Video Generation
- AI Video
- Generative AI
- Text-to-Video
- Image-to-Video
- Text-to-Image
- Video-to-Video
website: https://runwayml.com/
---
