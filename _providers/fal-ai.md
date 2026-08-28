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
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Fal Ai Agentic Access
  operation_count: 11
  slug: fal-ai-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 12
apis:
- description: WebSocket-based realtime inference for ultra-low latency interactive generative experiences such as LCM/SDXL sketch-to-image, live-portrait, and realtime upscaling. Bi-directional binary/JSON messagin
  name: fal Realtime API
  slug: fal-realtime-api
- description: HTTP streaming endpoint (`/{model-id}/stream`) that emits progressive partial outputs as a model runs — used for LLM/VLM token streams, incremental video frames, and step-by-step image diffusion previ
  name: fal Streaming API
  slug: fal-streaming-api
- description: Read-only discovery endpoints for browsing fal's 1,000+ production model catalog, including model metadata, capability tags, pricing per output, supported parameters, example inputs, and OpenAPI schem
  name: fal Models Catalog API
  slug: fal-models-catalog-api
- description: Provision and manage dedicated GPU instances (H100, H200, A100, B200) with full SSH access for training, fine-tuning, and persistent workloads. Hourly or per-second billing with no lock-in.
  name: fal Compute API
  slug: fal-compute-api
- description: 'Manage fal API keys — create, list, scope, and revoke keys used to authenticate against the Model, Storage, Serverless, and Compute APIs via the Authorization: Key $FAL_KEY header.'
  name: fal API Keys API
  slug: fal-keys-api
- description: Programmatic access to usage metrics, per-model spend, GPU-second consumption, and invoicing history. Surfaces the same data shown on the fal dashboard so platform teams can pipe inference cost into i
  name: fal Usage and Billing API
  slug: fal-usage-billing-api
- description: List and inspect deployed Serverless apps.
  name: fal Apps API
  slug: fal-ai-apps-api
- description: Manage files on persistent Serverless `/data` volumes.
  name: fal Files API
  slug: fal-ai-files-api
- description: Submit, inspect, and cancel model inference jobs.
  name: fal Queue API
  slug: fal-ai-queue-api
- description: Manage per-org secrets injected into Serverless runs.
  name: fal Secrets API
  slug: fal-ai-secrets-api
- description: Upload binary assets to the fal CDN.
  name: fal Storage API
  slug: fal-ai-storage-api
- description: Server-sent streaming of incremental model output.
  name: fal Streaming API
  slug: fal-ai-streaming-api
arazzos:
- description: Upload a reference image, submit an image-to-image job with a webhook, and confirm queue acceptance.
  name: fal Upload, Run Image-To-Image With Webhook
  slug: fal-ai-image-to-image-result-workflow
- description: Submit a model inference job, poll the queue until it completes, then fetch the result.
  name: fal Queue Inference
  slug: fal-ai-queue-inference-workflow
- description: List deployed Serverless apps, then fetch full metadata and scaling for the first one.
  name: fal Serverless App Discovery
  slug: fal-ai-serverless-app-discovery-workflow
- description: Confirm a Serverless app exists, then list files on its persistent /data volume.
  name: fal Serverless App Files Inspection
  slug: fal-ai-serverless-app-files-workflow
- description: Create or replace a Serverless secret, then list secret names to confirm it is present.
  name: fal Set And Verify Serverless Secret
  slug: fal-ai-set-and-verify-secret-workflow
- description: Run a model synchronously over the streaming endpoint to receive progressive output.
  name: fal Streaming Inference
  slug: fal-ai-stream-inference-workflow
- description: Submit an inference job, check its status once, and cancel it if it has not finished.
  name: fal Submit And Conditionally Cancel
  slug: fal-ai-submit-and-cancel-workflow
- description: Upload a binary reference asset to the fal CDN, then run an image-to-X model against it.
  name: fal Upload Asset Then Run Inference
  slug: fal-ai-upload-then-inference-workflow
- description: Submit an inference job with a webhook callback and confirm it was accepted into the queue.
  name: fal Webhook-Backed Submission
  slug: fal-ai-webhook-submission-workflow
artifact_total: 73
asyncapis:
- description: 'AsyncAPI description of fal''s event-driven inference surfaces. fal exposes two real-time channels in addition to its REST queue: (1) a Server-Sent Events stream that pushes incremental status updates '
  name: fal Event-Driven APIs
  slug: fal-ai-asyncapi
collections:
- collection_type: postman
  name: fal Model APIs
  slug: postman-fal-model-apis
- collection_type: postman
  name: fal Serverless Platform API
  slug: postman-fal-serverless-platform-api
- collection_type: postman
  name: fal Storage API
  slug: postman-fal-storage-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: fal Model APIs Apps API
  slug: open-fal-ai-apps-api
- collection_type: open
  name: fal Model APIs Apps Files API
  slug: open-fal-ai-files-api
- collection_type: open
  name: fal Model APIs Apps Queue API
  slug: open-fal-ai-queue-api
- collection_type: open
  name: fal Model APIs Apps Secrets API
  slug: open-fal-ai-secrets-api
- collection_type: open
  name: fal Model APIs Apps Storage API
  slug: open-fal-ai-storage-api
- collection_type: open
  name: fal Model APIs Apps Streaming API
  slug: open-fal-ai-streaming-api
- collection_type: open
  name: fal Model APIs
  slug: open-fal-model-apis
- collection_type: open
  name: fal Serverless Platform API
  slug: open-fal-serverless-platform-api
- collection_type: open
  name: fal Storage API
  slug: open-fal-storage-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/fal-ai-model-apis-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fal-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fal-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fal-ai-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/fal-ai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fal-ai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fal-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fal-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fal-ai-llms-full.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/fal-ai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fal-ai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fal-ai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fal-ai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fal-ai-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fal-ai-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/fal-ai-cli.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fal/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fal-ai-image-to-image-result-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fal-ai-queue-inference-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fal-ai-serverless-app-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fal-ai-serverless-app-files-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fal-ai-set-and-verify-secret-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fal-ai-stream-inference-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fal-ai-submit-and-cancel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fal-ai-upload-then-inference-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/fal-ai-webhook-submission-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://fal.ai
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs/model-apis/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/models
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs/authentication
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs/model-apis/webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs/model-apis/real-time
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs/model-apis/streaming
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs/model-apis/file-uploads
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs/private-serverless-models
- group: start
  title: ''
  type: GettingStarted
  url: https://fal.ai/docs/model-apis/quickstart
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fal.ai
- group: company
  title: ''
  type: Blog
  url: https://blog.fal.ai
- group: start
  title: ''
  type: Signup
  url: https://fal.ai/login
- group: commercial
  title: ''
  type: Pricing
  url: https://fal.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/fal-ai
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/fal-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fal.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fal.ai/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.fal.ai
- group: auth
  title: ''
  type: TrustCenter
  url: security/fal-ai-trust-center.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/featuresandlabels
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/fal
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fal-ai
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fal-ai/fal-client-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fal-ai/fal-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fal-ai/fal-swift
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fal-ai/fal-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fal-ai/fal-dart
- group: build
  title: ''
  type: SDKs
  url: https://github.com/fal-ai/fal
- group: build
  title: ''
  type: Tools
  url: https://github.com/fal-ai/terraform-provider-fal
- group: build
  title: ''
  type: Tools
  url: https://github.com/fal-ai/fal-blender-extension
- group: build
  title: ''
  type: Tools
  url: https://github.com/fal-ai/serverless-vscode
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fal-ai/awesome
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fal-ai/real-time-demo-app
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/fal-ai/fal-nextjs-template
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs/mcp-server
- group: docs
  title: ''
  type: Documentation
  url: https://fal.ai/docs/comfyui
- group: commercial
  title: ''
  type: Plans
  url: plans/fal-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fal-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fal-ai-finops.yml
created: '2026-05-25'
description: fal (Features and Labels, Inc.) is a generative media platform providing the world's fastest API for running image, video, audio, and multimodal generative AI models. Through a unified queue-based REST API at https://queue.fal.run, plus realtime WebSocket and SSE streaming surfaces, fal serves 1,000+ production models — including FLUX, Veo 3, Kling, Wan, Seedream, Nano Banana, and Stable Diffusion — on autoscaling GPU infrastructure. fal Serverless lets developers ship custom models with `@fal.function` / `fal.App` / BYO containers, while fal Compute provides dedicated H100/H200/A100/B200 instances. Trusted by Canva, Perplexity, Poe, and 1.5M+ developers; Series D funded ($140M, Sequoia-led, December 2025); SOC 2 with 99.99% uptime.
examples:
- key_count: 3
  name: Fal Flux Schnell Example
  slug: fal-flux-schnell-example
- key_count: 4
  name: Fal Storage Upload Example
  slug: fal-storage-upload-example
- key_count: 3
  name: Fal Veo3 Video Example
  slug: fal-veo3-video-example
features:
- Unified queue-based REST API at https://queue.fal.run/{model-id} for 1,000+ generative models
- Image generation models — FLUX (Schnell, Dev, Pro, Kontext Pro), Seedream V4, Nano Banana, Qwen, SDXL, SD3, Ideogram, Recraft
- Video generation models — Veo 3, Kling 2.5 Turbo Pro, Wan 2.5, Seedance 2.0, Ovi, Hunyuan, Sora-class
- Audio and voice models — Inworld TTS-1.5, ElevenLabs, MMAudio, MusicGen, Stable Audio
- 3D and multimodal models — TripoSR, Hunyuan3D, LivePortrait, FaceChain
- Synchronous, asynchronous queue, server-sent streaming, and WebSocket realtime invocation modes
- Webhook callbacks for queue completion with HMAC signature verification
- File uploads / CDN storage at https://v3.fal.media with signed upload URLs
- fal Serverless — `@fal.function`, `fal.App`, BYO container deployment with autoscaling from 0 to thousands of GPUs
- fal Compute — dedicated H100/H200/A100/B200 instances with SSH and per-second billing
- Per-output billing (image, video second, audio minute) plus per-second GPU billing for custom deployments
- 99.99% uptime SLA, SOC 2 compliance, private endpoints, and enterprise support
- Proprietary Inference Engine — up to 10x faster than reference implementations
- Official SDKs for Python (fal-client), JavaScript/TypeScript (@fal-ai/client), Swift, Java/Kotlin, Dart
- fal CLI for serverless deploy / run / apps / secrets / auth
- fal MCP Server exposing all 1,000+ models to AI assistants via the Model Context Protocol
- ComfyUI and Blender extensions, plus Terraform provider for infra-as-code
- Day-zero launch partner for major model releases (FLUX, Veo, Kling, Seedance, Wan, etc.)
finops:
- name: Fal Ai Finops
  service_category: AI and Machine Learning
  slug: fal-ai-finops
graphqls:
- description: fal is a fast serverless inference platform for AI models including image generation (Stable Diffusion, FLUX, Kling), video generation, speech, and custom models. The API covers model invocation, queu
  name: fal GraphQL API
  slug: fal-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fal-ai.png
json_schemas:
- name: fal Image Model Result
  property_count: 5
  slug: fal-image-result
- name: fal Queue Inference Request
  property_count: 10
  slug: fal-queue-request
- name: fal Queue Status Response
  property_count: 6
  slug: fal-queue-status
json_structures:
- name: Fal Ai Structure
  property_count: 0
  slug: fal-ai-structure
jsonld:
- class_count: 0
  name: Fal Ai Context
  property_count: 9
  slug: fal-ai-context
layout: provider
mcp_servers:
- description: ''
  name: fal MCP Server
  slug: fal-mcp-server
modified: '2026-06-20'
name: fal
nav: Providers
network: true
overview: 'fal publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Realtime API, Streaming API, Apps API, and 5 more. Tagged areas include Artificial Intelligence, Generative AI, Generative Media, Image-Generation, and Video Generation.


  The fal catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  fal''s developer surface includes authentication, changelog, CLI, developer portal, documentation, getting-started guide, engineering blog, and 60 more developer resources.'
plans:
- name: Fal Ai Plans Pricing
  plan_count: 2
  slug: fal-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Fal Ai Rate Limits
  slug: fal-ai-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: fal API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: fal-ai-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: fal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: fal-ai-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: fal API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 5
  slug: fal-ai-rules
score:
  band: exemplar
  composite: 69.7
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 30.3
    contract_quality: 77.5
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 30.3
    operational_transparency: 50.0
  previous_composite: 69.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fal-ai/refs/heads/main/screenshots/fal-ai-2026-06-20T181030.png
security:
- kind: authentication
  name: Fal Ai Authentication
  slug: fal-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fal Ai Domain Security
  slug: fal-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Fal Ai Trust Center
  slug: fal-ai-trust-center
  summary_line: SOC 2 Type II
slug: fal-ai
tags:
- Artificial Intelligence
- Generative AI
- Generative Media
- Image-Generation
- Video Generation
- Audio Generation
- Inference
- Serverless
- GPU
- MCP
website: https://fal.ai
---
