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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.7
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Leonardo Ai Agentic Access
  operation_count: 53
  slug: leonardo-ai-agentic-access
  summary_line: 53 operations · 32 acting
api_count: 14
apis:
- description: The 3D Model Assets API from Leonardo.AI — 3 operation(s) for 3d model assets.
  name: Leonardo.AI 3D Model Assets API
  slug: leonardo-ai-3d-model-assets-api
- description: The Blueprints API from Leonardo.AI — 6 operation(s) for blueprints.
  name: Leonardo.AI Blueprints API
  slug: leonardo-ai-blueprints-api
- description: The Dataset API from Leonardo.AI — 4 operation(s) for dataset.
  name: Leonardo.AI Dataset API
  slug: leonardo-ai-dataset-api
- description: The Elements API from Leonardo.AI — 3 operation(s) for elements.
  name: Leonardo.AI Elements API
  slug: leonardo-ai-elements-api
- description: The Image API from Leonardo.AI — 3 operation(s) for image.
  name: Leonardo.AI Image API
  slug: leonardo-ai-image-api
- description: The Init Images API from Leonardo.AI — 3 operation(s) for init images.
  name: Leonardo.AI Init Images API
  slug: leonardo-ai-init-images-api
- description: The Media API from Leonardo.AI — 2 operation(s) for media.
  name: Leonardo.AI Media API
  slug: leonardo-ai-media-api
- description: The Models API from Leonardo.AI — 4 operation(s) for models.
  name: Leonardo.AI Models API
  slug: leonardo-ai-models-api
- description: The Motion API from Leonardo.AI — 3 operation(s) for motion.
  name: Leonardo.AI Motion API
  slug: leonardo-ai-motion-api
- description: The Pricing Calculator API from Leonardo.AI — 1 operation(s) for pricing calculator.
  name: Leonardo.AI Pricing Calculator API
  slug: leonardo-ai-pricing-calculator-api
- description: The Prompt API from Leonardo.AI — 2 operation(s) for prompt.
  name: Leonardo.AI Prompt API
  slug: leonardo-ai-prompt-api
- description: The Realtime Canvas API from Leonardo.AI — 4 operation(s) for realtime canvas.
  name: Leonardo.AI Realtime Canvas API
  slug: leonardo-ai-realtime-canvas-api
- description: The User API from Leonardo.AI — 1 operation(s) for user.
  name: Leonardo.AI User API
  slug: leonardo-ai-user-api
- description: The Variation API from Leonardo.AI — 6 operation(s) for variation.
  name: Leonardo.AI Variation API
  slug: leonardo-ai-variation-api
artifact_total: 80
asyncapis:
- description: AsyncAPI description of Leonardo.AI's outbound webhook callback surface. Leonardo delivers asynchronous job-completion notifications to a customer- hosted HTTPS endpoint that is configured per Product
  name: Leonardo.AI Webhook Callbacks
  slug: leonardo-ai-webhooks-asyncapi
collections:
- collection_type: postman
  name: Leonardo.AI 3D Model Assets API
  slug: postman-leonardo-ai-3d-model-assets-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Blueprints API
  slug: postman-leonardo-ai-blueprints-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Dataset API
  slug: postman-leonardo-ai-dataset-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Elements API
  slug: postman-leonardo-ai-elements-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Image API
  slug: postman-leonardo-ai-image-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Init Images API
  slug: postman-leonardo-ai-init-images-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Media API
  slug: postman-leonardo-ai-media-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Models API
  slug: postman-leonardo-ai-models-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Motion API
  slug: postman-leonardo-ai-motion-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Pricing Calculator API
  slug: postman-leonardo-ai-pricing-calculator-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Prompt API
  slug: postman-leonardo-ai-prompt-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Realtime Canvas API
  slug: postman-leonardo-ai-realtime-canvas-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets User API
  slug: postman-leonardo-ai-user-api
- collection_type: postman
  name: Leonardo.AI 3D Model Assets Variation API
  slug: postman-leonardo-ai-variation-api
- collection_type: open
  name: Leonardo.AI 3D Model Assets API
  slug: open-leonardo-ai-3d-model-assets
- collection_type: open
  name: Leonardo.AI Blueprints API
  slug: open-leonardo-ai-blueprints
- collection_type: open
  name: Leonardo.AI Datasets API
  slug: open-leonardo-ai-datasets
- collection_type: open
  name: Leonardo.AI Elements API
  slug: open-leonardo-ai-elements
- collection_type: open
  name: Leonardo.AI Image Generation API
  slug: open-leonardo-ai-image-generation
- collection_type: open
  name: Leonardo.AI Init Images API
  slug: open-leonardo-ai-init-images
- collection_type: open
  name: Leonardo.AI Media API
  slug: open-leonardo-ai-media
- collection_type: open
  name: Leonardo.AI Models API
  slug: open-leonardo-ai-models
- collection_type: open
  name: Leonardo.AI Pricing Calculator API
  slug: open-leonardo-ai-pricing-calculator
- collection_type: open
  name: Leonardo.AI Prompt API
  slug: open-leonardo-ai-prompt
- collection_type: open
  name: Leonardo.AI Realtime Canvas API
  slug: open-leonardo-ai-realtime-canvas
- collection_type: open
  name: Leonardo.AI User API
  slug: open-leonardo-ai-user
- collection_type: open
  name: Leonardo.AI Variation & Upscale API
  slug: open-leonardo-ai-variation
- collection_type: open
  name: Leonardo.AI Video Generation API
  slug: open-leonardo-ai-video-generation
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/leonardoai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/leonardo-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leonardo-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/leonardo-ai-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://leonardo.ai
- group: start
  title: ''
  type: Portal
  url: https://leonardo.ai/api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leonardo.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.leonardo.ai/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leonardo.ai/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leonardo.ai/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leonardo.ai/docs/api-faq
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.leonardo.ai/docs/api-error-messages
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.leonardo.ai/docs/concurrency-rate-limits-and-queue
- group: design
  title: ''
  type: Webhooks
  url: https://docs.leonardo.ai/docs/webhook-callback-feature
- group: design
  title: ''
  type: Webhooks
  url: https://docs.leonardo.ai/docs/guide-to-the-webhook-callback-feature
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/leonardo-ai-webhooks-asyncapi.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.leonardo.ai/docs/payg-guide
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.leonardo.ai/docs/plan-with-the-pricing-calculator
- group: build
  title: ''
  type: SDKs
  url: https://docs.leonardo.ai/docs/leonardoai-official-sdks
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leonardo.ai/docs/mcp-server
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leonardo.ai/docs/nsfw-handling
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Leonardo-Interactive
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Leonardo-Interactive/leonardo-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Leonardo-Interactive/leonardo-ts-sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/Leonardo-Interactive/agent-browser
- group: build
  title: ''
  type: Tools
  url: https://github.com/Leonardo-Interactive/background-removal-js
- group: build
  title: ''
  type: Plugins
  url: https://github.com/Leonardo-Interactive/leonardo-texturing-blender-plugin
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/leonardoai/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@leonardo-ai/sdk
- group: start
  title: ''
  type: Signup
  url: https://app.leonardo.ai/api-access
- group: start
  title: ''
  type: Portal
  url: https://app.leonardo.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://leonardo.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://leonardo.ai/news/
- group: company
  title: ''
  type: Press
  url: https://leonardo.ai/news/supercharging-leonardo-with-canva/
- group: company
  title: ''
  type: Press
  url: https://www.canva.com/newsroom/news/leonardo-ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://leonardo.ai/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leonardo.ai/privacy-policy/
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://leonardo.ai/legal/acceptable-use-policy/
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/leonardo-ai/
- group: docs
  title: ''
  type: Documentation
  url: https://intercom.help/leonardo-ai/en/articles/8973587-api-reference-and-guides-for-developers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leonardo-ai/
- group: other
  title: ''
  type: X
  url: https://x.com/LeonardoAi_
- group: commercial
  title: ''
  type: Plans
  url: plans/leonardo-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/leonardo-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/leonardo-ai-finops.yml
created: '2026-05-25'
description: Leonardo.AI is an Australian generative-AI company (acquired by Canva in July 2024) offering a Production API for AI image generation, video generation, 3D model creation, custom model and element training, realtime canvas editing, upscaling and variations, and Blueprint workflow execution. The platform supports in-house Leonardo models (Phoenix, Lucid Origin, Lucid Realism) and third-party models (FLUX.1/FLUX.2, Ideogram 3.0, GPT Image, Nano Banana, Seedream, Kling, LTX, Veo, Seedance, Hailuo, Rodin) under a unified pay-as-you-go dollar-denominated API surface with webhook callbacks, MCP server integration, and official Python and TypeScript SDKs.
examples:
- key_count: 2
  name: Leonardo Ai Create Generation Example
  slug: leonardo-ai-create-generation-example
- key_count: 2
  name: Leonardo Ai Get Generation Example
  slug: leonardo-ai-get-generation-example
- key_count: 2
  name: Leonardo Ai Image To Video Example
  slug: leonardo-ai-image-to-video-example
- key_count: 2
  name: Leonardo Ai Me Example
  slug: leonardo-ai-me-example
- key_count: 2
  name: Leonardo Ai Pricing Calculator Example
  slug: leonardo-ai-pricing-calculator-example
features:
- Production API for image, video, 3D, and workflow generation under a unified dollar-denominated PAYG model
- In-house Leonardo models — Phoenix, Lucid Origin, Lucid Realism — alongside third-party FLUX.1/FLUX.2, Ideogram 3.0, GPT Image 2, Nano Banana, Seedream
- Video generation through Kling 2.x/3.x, LTX 2.x, Veo 3.x, Seedance, Hailuo, and Stable Video Diffusion motion models
- 3D model generation via Rodin V2 and 3D model asset management
- Realtime Canvas powered by LCM (Latent Consistency Models) for sub-second iterative editing
- Custom Models and Custom Elements — LoRA-style fine-tuning on user-uploaded datasets
- Blueprints — pre-packaged multi-step generation workflows that can be executed via the API
- PhotoReal, Alchemy, image prompts, image guidance (ControlNet), enhanced prompts, transparency
- Universal Upscaler, unzoom (outpainting), creative upscale, and background-removal variations
- Webhook callbacks for asynchronous job completion (no polling required)
- Pricing Calculator endpoint for pre-flight cost estimation
- Pay-As-You-Go billing in USD with manual and auto top-up, no monthly commitment, free starter credits
- Concurrency, queue, and rate-limit controls scoped per API key
- Production API key system (replaces deprecated User API key) — up to 10 keys per account
- Official Python and TypeScript SDKs generated from the OpenAPI spec via Speakeasy
- MCP Server integration for AI-agent workflows
- Browser-side background-removal JS library and Blender texturing plugin available as open source
- NSFW handling controls and per-model safety guardrails
- Acquired by Canva July 2024; tech being integrated into Canva Magic Studio while the API remains independent
finops:
- name: Leonardo Ai Finops
  service_category: AI and Machine Learning
  slug: leonardo-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leonardo-ai.png
json_schemas:
- name: Leonardo.AI Generation
  property_count: 0
  slug: leonardo-ai-generation
- name: Leonardo.AI Model
  property_count: 0
  slug: leonardo-ai-model
json_structures:
- name: Leonardo Ai Generation Structure
  property_count: 0
  slug: leonardo-ai-generation-structure
jsonld:
- class_count: 0
  name: Leonardo Ai Context
  property_count: 7
  slug: leonardo-ai-context
layout: provider
modified: '2026-05-30'
name: Leonardo.AI
nav: Providers
network: true
overview: 'Leonardo.AI publishes 14 APIs on the [APIs.io](https://apis.io/) network, including 3D Model Assets API, Blueprints API, Dataset API, and 11 more. Tagged areas include AI, Artificial Intelligence, Image Generation, Video Generation, and Generative AI.


  The Leonardo.AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Leonardo.AI''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, tooling, signup flow, and 38 more developer resources.'
plans:
- name: Leonardo Ai Plans Pricing
  plan_count: 5
  slug: leonardo-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Leonardo Ai Rate Limits
  slug: leonardo-ai-rate-limits
rules:
- name: Leonardo.AI API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: leonardo-ai-asyncapi-spectral-rules
- name: Leonardo.AI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: leonardo-ai-jsonschema-spectral-rules
- name: Leonardo.AI API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 4
  slug: leonardo-ai-rules
score:
  band: strong
  composite: 65.9
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 79.5
    developer_ergonomics: 65.2
    discoverability: 59.3
    governance: 47.9
    operational_transparency: 34.2
  previous_composite: 65.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leonardo-ai/refs/heads/main/screenshots/leonardo-ai-2026-06-20T184426.png
security:
- kind: authentication
  name: Leonardo Ai Authentication
  slug: leonardo-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Leonardo Ai Domain Security
  slug: leonardo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leonardo-ai
tags:
- AI
- Artificial Intelligence
- Image Generation
- Video Generation
- Generative AI
- Creative
- 3D
- Diffusion
- Canva
website: https://leonardo.ai
---
