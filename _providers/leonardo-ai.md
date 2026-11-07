---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Leonardo Ai Agentic Access
  operation_count: 53
  slug: leonardo-ai-agentic-access
  summary_line: 53 operations · 32 acting
api_count: 17
apis:
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The 3D Model Assets API from Leonardo.AI — 3 operation(s) for 3d model assets.
  name: Leonardo.AI 3D Model Assets API
  slug: leonardo-ai-3d-model-assets-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Blueprints API from Leonardo.AI — 6 operation(s) for blueprints.
  name: Leonardo.AI Blueprints API
  slug: leonardo-ai-blueprints-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Dataset API from Leonardo.AI — 4 operation(s) for dataset.
  name: Leonardo.AI Dataset API
  slug: leonardo-ai-dataset-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Elements API from Leonardo.AI — 3 operation(s) for elements.
  name: Leonardo.AI Elements API
  slug: leonardo-ai-elements-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Image API from Leonardo.AI — 3 operation(s) for image.
  name: Leonardo.AI Image API
  slug: leonardo-ai-image-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Init Images API from Leonardo.AI — 3 operation(s) for init images.
  name: Leonardo.AI Init Images API
  slug: leonardo-ai-init-images-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Media API from Leonardo.AI — 2 operation(s) for media.
  name: Leonardo.AI Media API
  slug: leonardo-ai-media-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Models API from Leonardo.AI — 4 operation(s) for models.
  name: Leonardo.AI Models API
  slug: leonardo-ai-models-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Motion API from Leonardo.AI — 3 operation(s) for motion.
  name: Leonardo.AI Motion API
  slug: leonardo-ai-motion-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Pricing Calculator API from Leonardo.AI — 1 operation(s) for pricing calculator.
  name: Leonardo.AI Pricing Calculator API
  slug: leonardo-ai-pricing-calculator-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Prompt API from Leonardo.AI — 2 operation(s) for prompt.
  name: Leonardo.AI Prompt API
  slug: leonardo-ai-prompt-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Realtime Canvas API from Leonardo.AI — 4 operation(s) for realtime canvas.
  name: Leonardo.AI Realtime Canvas API
  slug: leonardo-ai-realtime-canvas-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The User API from Leonardo.AI — 1 operation(s) for user.
  name: Leonardo.AI User API
  slug: leonardo-ai-user-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Variation API from Leonardo.AI — 6 operation(s) for variation.
  name: Leonardo.AI Variation API
  slug: leonardo-ai-variation-api
- baseURL: https://cloud.leonardo.ai/api/rest/v1
  baseurl_source: declared
  description: The Generations API from Leonardo.AI — 1 operation(s) for generations.
  name: Leonardo.AI Generations API
  slug: leonardo-ai-generations-api
artifact_total: 107
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
  slug: open-leonardo-ai-3d-model-assets-api
- collection_type: open
  name: Leonardo.AI 3D Model Assets API
  slug: open-leonardo-ai-3d-model-assets
- collection_type: open
  name: Leonardo.AI 3D Model Assets Blueprints API
  slug: open-leonardo-ai-blueprints-api
- collection_type: open
  name: Leonardo.AI Blueprints API
  slug: open-leonardo-ai-blueprints
- collection_type: open
  name: Leonardo.AI 3D Model Assets Dataset API
  slug: open-leonardo-ai-dataset-api
- collection_type: open
  name: Leonardo.AI Datasets API
  slug: open-leonardo-ai-datasets
- collection_type: open
  name: Leonardo.AI 3D Model Assets Elements API
  slug: open-leonardo-ai-elements-api
- collection_type: open
  name: Leonardo.AI Elements API
  slug: open-leonardo-ai-elements
- collection_type: open
  name: Leonardo.AI 3D Model Assets Image API
  slug: open-leonardo-ai-image-api
- collection_type: open
  name: Leonardo.AI Image Generation API
  slug: open-leonardo-ai-image-generation
- collection_type: open
  name: Leonardo.AI 3D Model Assets Init Images API
  slug: open-leonardo-ai-init-images-api
- collection_type: open
  name: Leonardo.AI Init Images API
  slug: open-leonardo-ai-init-images
- collection_type: open
  name: Leonardo.AI 3D Model Assets Media API
  slug: open-leonardo-ai-media-api
- collection_type: open
  name: Leonardo.AI Media API
  slug: open-leonardo-ai-media
- collection_type: open
  name: Leonardo.AI 3D Model Assets Models API
  slug: open-leonardo-ai-models-api
- collection_type: open
  name: Leonardo.AI Models API
  slug: open-leonardo-ai-models
- collection_type: open
  name: Leonardo.AI 3D Model Assets Motion API
  slug: open-leonardo-ai-motion-api
- collection_type: open
  name: Leonardo.AI 3D Model Assets Pricing Calculator API
  slug: open-leonardo-ai-pricing-calculator-api
- collection_type: open
  name: Leonardo.AI Pricing Calculator API
  slug: open-leonardo-ai-pricing-calculator
- collection_type: open
  name: Leonardo.AI 3D Model Assets Prompt API
  slug: open-leonardo-ai-prompt-api
- collection_type: open
  name: Leonardo.AI Prompt API
  slug: open-leonardo-ai-prompt
- collection_type: open
  name: Leonardo.AI 3D Model Assets Realtime Canvas API
  slug: open-leonardo-ai-realtime-canvas-api
- collection_type: open
  name: Leonardo.AI Realtime Canvas API
  slug: open-leonardo-ai-realtime-canvas
- collection_type: open
  name: Leonardo.AI 3D Model Assets User API
  slug: open-leonardo-ai-user-api
- collection_type: open
  name: Leonardo.AI User API
  slug: open-leonardo-ai-user
- collection_type: open
  name: Leonardo.AI 3D Model Assets Variation API
  slug: open-leonardo-ai-variation-api
- collection_type: open
  name: Leonardo.AI Variation & Upscale API
  slug: open-leonardo-ai-variation
- collection_type: open
  name: Leonardo.AI Video Generation API
  slug: open-leonardo-ai-video-generation
common:
- group: design
  href: https://artifacts.apis.io/leonardo-ai/rules/leonardo-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/leonardo-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/leonardo-ai/rules/leonardo-ai-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/leonardo-ai-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/leonardo-ai/rules/leonardo-ai-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/leonardo-ai-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/leonardo-ai/vocabulary/leonardo-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/leonardo-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/leonardo-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/leonardo-ai/asyncapi/leonardo-ai-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/leonardo-ai-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/leonardo-ai/data-model/leonardo-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/leonardo-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/leonardo-ai/changelog/leonardo-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/leonardo-ai-changelog.yml
- group: design
  href: https://artifacts.apis.io/leonardo-ai/conventions/leonardo-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/leonardo-ai-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.leonardo.ai/docs/deprecations-changes
- group: design
  href: https://artifacts.apis.io/leonardo-ai/lifecycle/leonardo-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/leonardo-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/leonardo-ai/errors/leonardo-ai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/leonardo-ai-error-codes.yml
- group: design
  href: https://artifacts.apis.io/leonardo-ai/errors/leonardo-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/leonardo-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/leonardo-ai/conformance/leonardo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/leonardo-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/leonardo-ai/overlays/leonardo-ai-3d-model-assets-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/leonardo-ai-3d-model-assets-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/leonardo-ai/llms/leonardo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leonardo-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/leonardo-ai/mcp/leonardo-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/leonardo-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/leonardo-ai/mcp/leonardo-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/leonardo-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/leonardo-ai/well-known/leonardo-ai-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/leonardo-ai-www-security.txt
- group: auth
  href: https://artifacts.apis.io/leonardo-ai/well-known/leonardo-ai-intercom-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/leonardo-ai-intercom-security.txt
- group: auth
  href: https://artifacts.apis.io/leonardo-ai/well-known/leonardo-ai-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/leonardo-ai-api-security.txt
- group: agent
  href: https://artifacts.apis.io/leonardo-ai/well-known/leonardo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leonardo-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/leonardo-ai/hosts/leonardo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/leonardo-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/leonardo-ai/integrations/leonardo-ai-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/leonardo-ai-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/leonardo-ai/vendors/leonardo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/leonardo-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/leonardo-ai/packages/leonardo-ai-packages.yml
  title: ''
  type: Packages
  url: packages/leonardo-ai-packages.yml
- group: company
  title: ''
  type: Website
  url: https://leonardo.ai
- group: other
  href: https://artifacts.apis.io/leonardo-ai/capabilities/leonardo-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/leonardo-ai-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/leonardoai/overview
- group: agent
  href: https://artifacts.apis.io/leonardo-ai/agentic-access/leonardo-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/leonardo-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/leonardo-ai/security/leonardo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leonardo-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/leonardo-ai/authentication/leonardo-ai-authentication.yml
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
  url: https://docs.leonardo.ai/docs/guide-to-concurrency-queue-and-rate-limit
- group: design
  title: ''
  type: Webhooks
  url: https://docs.leonardo.ai/docs/guide-to-the-webhook-callback-feature
- group: docs
  href: https://artifacts.apis.io/leonardo-ai/asyncapi/leonardo-ai-webhooks-asyncapi.yml
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
  url: https://docs.leonardo.ai/docs/connect-to-leonardoai-mcp
- group: docs
  title: ''
  type: Documentation
  url: https://docs.leonardo.ai/docs/guide-to-handling-not-safe-for-work-image-generation-nsfw
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
  url: https://x.com/LeonardoAi
- group: commercial
  href: https://artifacts.apis.io/leonardo-ai/plans/leonardo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leonardo-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/leonardo-ai/rate-limits/leonardo-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/leonardo-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/leonardo-ai/finops/leonardo-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/leonardo-ai-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://docs.leonardo.ai/docs/need-more-support
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.leonardo.ai/docs/pricing-and-plans-faq
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
- has_sources: true
  method: derived
  name: Leonardo Ai Finops
  primary_unit: ''
  service_category: ''
  slug: leonardo-ai-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leonardo-ai.png
json_schemas:
- name: Anime
  property_count: 3
  slug: leonardo-ai-anime-xl-generation-request
- name: Leonardo.AI Generation
  property_count: 0
  slug: leonardo-ai-generation
- name: Illustrative Albedo
  property_count: 3
  slug: leonardo-ai-illustrative-albedo-generation-request
- name: Cinematic Kino
  property_count: 3
  slug: leonardo-ai-kino-xl-generation-request
- name: Lifelike Vision
  property_count: 3
  slug: leonardo-ai-lifelike-vision-generation-request
- name: Leonardo Lightning
  property_count: 3
  slug: leonardo-ai-lightning-xl-generation-request
- name: Leonardo.AI Model
  property_count: 0
  slug: leonardo-ai-model
- name: Portrait Perfect
  property_count: 3
  slug: leonardo-ai-portrait-perfect-generation-request
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
mcp_servers:
- description: Official hosted MCP server ("Leonardo.Ai Connector") that lets an AI assistant use Leonardo.Ai image generation over the Model Context Protocol. Requires a Leonardo.Ai API plan and API key.
  name: Leonardo.Ai Connector (MCP Server)
  slug: leonardo-ai-connector-mcp-server
modified: '2026-10-21'
name: Leonardo.AI
nav: Providers
network: true
overview: 'Leonardo.AI publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including 3D Model Assets API, Blueprints API, Dataset API, and 12 more. Tagged areas include Artificial Intelligence, Image Generation, Video Generation, Generative AI, and Creative.


  The Leonardo.AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Leonardo.AI''s developer surface includes changelog, authentication, developer portal, documentation, getting-started guide, pricing, tooling, and 67 more developer resources.'
plans:
- name: Leonardo Ai Plans Pricing
  plan_count: 2
  slug: leonardo-ai-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Leonardo Ai Rate Limits
  slug: leonardo-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Leonardo.AI — asyncapi rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: leonardo-ai-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Leonardo.AI — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: leonardo-ai-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Leonardo.AI API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 1
    info: 0
    warn: 4
  slug: leonardo-ai-rules
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 38
    catalog_earned: 79.0
    catalog_earned_first_party: 16.0
    catalog_gap: 36.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 66.1
    developer_ergonomics: 67.3
    discoverability: 81.7
    operational_transparency: 64.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 62.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/leonardo-ai/leonardo-ai-2026-06-20T184426.png
security:
- kind: authentication
  name: Leonardo Ai Authentication
  slug: leonardo-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Leonardo Ai Domain Security
  slug: leonardo-ai-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: animate-an-image
  slug: leonardo-ai-animate-an-image
- name: generate-images
  slug: leonardo-ai-generate-images
- name: remove-background-and-upscale
  slug: leonardo-ai-remove-background-and-upscale
- name: run-a-blueprint
  slug: leonardo-ai-run-a-blueprint
- name: train-a-custom-model
  slug: leonardo-ai-train-a-custom-model
slug: leonardo-ai
tags:
- Artificial Intelligence
- Image Generation
- Video Generation
- Generative AI
- Creative
- 3D
- Diffusion Models
- Canva
website: https://leonardo.ai
---
