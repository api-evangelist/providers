---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.6
  scored_at: '2026-08-10'
api_count: 5
apis:
- description: List, inspect, and manage custom and base AI models available to a Scenario account. Returns training status, training progress, model type (image, video, audio, 3D), and metadata for the 500+ base mo
  name: Scenario Models API
  slug: scenario-models-api
- description: Generate game-ready images, video, audio, and 3D assets from text prompts, reference images, or ControlNet guides. Supports text-to-image, image-to-image, ControlNet (txt2img and img2img), text-to-3D,
  name: Scenario Generation API
  slug: scenario-generation-api
- description: Inspect the status, progress, metadata, and output assets of an asynchronous generation or training job. Generation and training requests return a jobId immediately; clients poll the Jobs API (or rece
  name: Scenario Jobs API
  slug: scenario-jobs-api
- description: List, retrieve, upload, and manage the images, video, audio, and 3D assets stored in a team's Scenario workspace. Includes endpoints for project-private assets, public asset retrieval, and asset uploa
  name: Scenario Assets API
  slug: scenario-assets-api
- description: Retrieve unified compute-unit consumption for an account, filtered by date range, project, or model. Compute units match the metering used by the Scenario web application and are consumed by both gene
  name: Scenario Usage API
  slug: scenario-usage-api
artifact_total: 23
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/scenario-gg-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scenario-gg-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.scenario.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scenario.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.scenario.com/docs/welcome-to-scenario-api
- group: auth
  title: ''
  type: Authentication
  url: https://docs.scenario.com/docs/api-key-and-authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.scenario.com/docs/step-1-obtain-your-api-key
- group: docs
  title: ''
  type: Documentation
  url: https://help.scenario.com/en/articles/overviewing-the-api/
- group: docs
  title: ''
  type: Documentation
  url: https://help.scenario.com/en/articles/creating-an-api-key/
- group: docs
  title: ''
  type: Documentation
  url: https://www.scenario.com/features/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.scenario.com/features/train
- group: docs
  title: ''
  type: OpenAPI
  url: https://cdn.cloud.scenario.com/static/api/swagger.yaml
- group: start
  title: ''
  type: Portal
  url: https://app.scenario.com
- group: start
  title: ''
  type: Signup
  url: https://app.scenario.com/signup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scenario-com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scenario-labs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/scenario-labs/Scenario-Unity
- group: build
  title: ''
  type: SDKs
  url: https://github.com/scenario-labs/LTX-2
- group: build
  title: ''
  type: SDKs
  url: https://github.com/scenario-labs/diffusers
- group: build
  title: ''
  type: SDKs
  url: https://github.com/scenario-labs/PowerPaint
- group: build
  title: ''
  type: SDKs
  url: https://github.com/scenario-labs/FastSAM
- group: build
  title: ''
  type: SDKs
  url: https://github.com/scenario-labs/ai-toolkit
- group: build
  title: ''
  type: Tools
  url: https://github.com/scenario-labs/model-police
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/scenario-labs/awesome-blender-script
- group: commercial
  title: ''
  type: Plans
  url: https://www.scenario.com/pricing
created: '2026-05-25T00:00:00.000Z'
description: Scenario is a Paris- and San Francisco-headquartered AI platform for game asset generation founded in 2021 by Emmanuel de Maistre and Hervé Nivon. The Scenario REST API lets game studios and creative teams generate consistent, on-brand images, video, audio, and 3D assets, train custom LoRA models on their own reference art, automate batch asset pipelines, and integrate AI-generated visuals into production tools like Unity. Scenario aggregates 500+ AI models from 50+ providers behind a single workspace and API, with full commercial licensing for generated assets and enterprise SSO, SOC 2 Type II, and governance controls.
features:
- 500+ AI models across image, video, audio, and 3D from 50+ providers in a single workspace
- Custom LoRA model training on a team's reference art (10-50+ reference images, 30 min - 1 hr training)
- Text-to-image, image-to-image, ControlNet (txt2img and img2img), text-to-3D, image-to-3D generation
- Video and audio generation including the in-house LTX-2 audio-video model
- Asset editing: background removal, upscaling, vectorization, inpainting (PowerPaint), segmentation (FastSAM)
- Visual workflow builder for batch generation and asset-pipeline automation
- Pre-built apps for common creative tasks (character art, environments, UI, marketing creatives)
- REST API with Basic Auth (Base64-encoded API key:secret) for programmatic generation, training, and asset management
- Asynchronous job model with polling via /jobs and webhook callbacks
- dryRun parameter for cost estimation before executing generation jobs
- Unified compute-unit metering matching the web app pricing
- Official Unity plugin for in-engine generation
- Open-source companion projects: diffusers, LTX-2, PowerPaint, FastSAM, ai-toolkit, model-police
- Full commercial licensing for generated assets on all paid plans
- Enterprise SSO, SOC 2 Type II, governance, audit trail, custom integrations
- Studio customers including Ubisoft, Unity, Scopely, and many mobile game developers
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scenario-gg.png
layout: provider
modified: '2026-05-25'
name: Scenario
nav: Providers
network: true
overview: 'Scenario publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Artificial Intelligence, Game Assets, Game Development, and Generative AI.


  Scenario''s developer surface includes developer portal, documentation, getting-started guide, authentication, signup flow, tooling, code examples, and 18 more developer resources.'
random_paper: 59
score:
  band: emerging
  composite: 20.5
  delta: 0.0
  facets:
    commercial_clarity: 7.9
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scenario-gg/refs/heads/main/screenshots/scenario-gg-2026-06-20T193511.png
security:
- kind: domain-security
  name: Scenario Gg Domain Security
  slug: scenario-gg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Scenario Gg Trust Center
  slug: scenario-gg-trust-center
  summary_line: SOC 2
slug: scenario-gg
tags:
- AI
- Artificial Intelligence
- Game Assets
- Game Development
- Generative AI
- Image Generation
- Video Generation
- Audio Generation
- 3D Assets
- Custom Model Training
- LoRA
- ControlNet
- Creative AI
- Asset Pipeline
website: https://www.scenario.com
---
