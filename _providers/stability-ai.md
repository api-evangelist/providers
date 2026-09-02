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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 18
  human_in_the_loop: 3
  name: Stability Ai Agentic Access
  operation_count: 20
  slug: stability-ai-agentic-access
  summary_line: 20 operations · 18 acting · 3 human-in-the-loop
api_count: 6
apis:
- description: Generate textured 3D mesh assets from single input images using the Stable Fast 3D model.
  name: Stability AI 3D Generation API
  slug: stability-ai-3d-generation-api
- description: Increase image resolution while closely preserving the original image details and composition with minimal creative additions.
  name: Stability AI Conservative Upscale API
  slug: stability-ai-conservative-upscale-api
- description: Increase image resolution while enhancing details and adding creative improvements guided by an optional text prompt. This is an asynchronous endpoint that returns a generation ID for polling.
  name: Stability AI Creative Upscale API
  slug: stability-ai-creative-upscale-api
- description: Remove objects from an image by masking the area to erase and letting the AI fill in the background naturally.
  name: Stability AI Erase API
  slug: stability-ai-erase-api
- description: Quickly increase image resolution with minimal processing time while maintaining image quality.
  name: Stability AI Fast Upscale API
  slug: stability-ai-fast-upscale-api
- description: Generate images using Stable Image Core, a fast and affordable model for high-quality image generation.
  name: Stability AI Generate Core API
  slug: stability-ai-generate-core-api
- description: Generate images using Stable Diffusion 3 and 3.5 models with advanced text-to-image and image-to-image capabilities.
  name: Stability AI Generate SD3 API
  slug: stability-ai-generate-sd3-api
- description: Generate images using Stable Image Ultra, the highest quality model for state-of-the-art photorealistic and artistic image generation.
  name: Stability AI Generate Ultra API
  slug: stability-ai-generate-ultra-api
- description: Generate short video clips from a single input image using the Stable Video Diffusion model. The API uses an asynchronous start-and-poll pattern.
  name: Stability AI Image to Video API
  slug: stability-ai-image-to-video-api
- description: Fill in masked regions of an image using AI-guided inpainting with text prompts to control what appears in the filled area.
  name: Stability AI Inpaint API
  slug: stability-ai-inpaint-api
- description: Extend the boundaries of an image by generating new content that seamlessly continues the existing scene in any direction.
  name: Stability AI Outpaint API
  slug: stability-ai-outpaint-api
- description: Automatically detect and remove the background from an image, isolating the foreground subject.
  name: Stability AI Remove Background API
  slug: stability-ai-remove-background-api
- description: Replace the background of an image and adjust lighting conditions using AI-powered scene understanding.
  name: Stability AI Replace Background and Relight API
  slug: stability-ai-replace-background-and-relight-api
- description: Find specific objects within an image and recolor them using text descriptions of the target object and desired color.
  name: Stability AI Search and Recolor API
  slug: stability-ai-search-and-recolor-api
- description: Find and replace specific objects within an image using text descriptions of what to search for and what to replace it with.
  name: Stability AI Search and Replace API
  slug: stability-ai-search-and-replace-api
- description: Generate images from hand-drawn sketches or line drawings, guided by a text prompt to fill in details, colors, and textures.
  name: Stability AI Sketch API
  slug: stability-ai-sketch-api
- description: Generate images guided by the structural composition of a reference image, preserving edges and layout while applying new content from a text prompt.
  name: Stability AI Structure API
  slug: stability-ai-structure-api
- description: Generate images that adopt the visual style of a reference image while following a text prompt for content direction.
  name: Stability AI Style API
  slug: stability-ai-style-api
artifact_total: 117
collections:
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation API
  slug: postman-stability-ai-3d-generation-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Conservative Upscale API
  slug: postman-stability-ai-conservative-upscale-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Creative Upscale API
  slug: postman-stability-ai-creative-upscale-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Erase API
  slug: postman-stability-ai-erase-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Fast Upscale API
  slug: postman-stability-ai-fast-upscale-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Generate Core API
  slug: postman-stability-ai-generate-core-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Generate SD3 API
  slug: postman-stability-ai-generate-sd3-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Generate Ultra API
  slug: postman-stability-ai-generate-ultra-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Image to Video API
  slug: postman-stability-ai-image-to-video-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Inpaint API
  slug: postman-stability-ai-inpaint-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Outpaint API
  slug: postman-stability-ai-outpaint-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Remove Background API
  slug: postman-stability-ai-remove-background-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Replace Background and Relight API
  slug: postman-stability-ai-replace-background-and-relight-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Search and Recolor API
  slug: postman-stability-ai-search-and-recolor-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Search and Replace API
  slug: postman-stability-ai-search-and-replace-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Sketch API
  slug: postman-stability-ai-sketch-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Structure API
  slug: postman-stability-ai-structure-api
- collection_type: postman
  name: Stability AI Stable Fast 3D 3D Generation Style API
  slug: postman-stability-ai-style-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation API
  slug: open-stability-ai-3d-generation-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Conservative Upscale API
  slug: open-stability-ai-conservative-upscale-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Creative Upscale API
  slug: open-stability-ai-creative-upscale-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Erase API
  slug: open-stability-ai-erase-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Fast Upscale API
  slug: open-stability-ai-fast-upscale-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Generate Core API
  slug: open-stability-ai-generate-core-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Generate SD3 API
  slug: open-stability-ai-generate-sd3-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Generate Ultra API
  slug: open-stability-ai-generate-ultra-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Image to Video API
  slug: open-stability-ai-image-to-video-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Inpaint API
  slug: open-stability-ai-inpaint-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Outpaint API
  slug: open-stability-ai-outpaint-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Remove Background API
  slug: open-stability-ai-remove-background-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Replace Background and Relight API
  slug: open-stability-ai-replace-background-and-relight-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Search and Recolor API
  slug: open-stability-ai-search-and-recolor-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Search and Replace API
  slug: open-stability-ai-search-and-replace-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Sketch API
  slug: open-stability-ai-sketch-api
- collection_type: open
  name: Stability AI Stable Fast 3D API
  slug: open-stability-ai-stable-fast-3d
- collection_type: open
  name: Stability AI Stable Image Control API
  slug: open-stability-ai-stable-image-control
- collection_type: open
  name: Stability AI Stable Image Edit API
  slug: open-stability-ai-stable-image-edit
- collection_type: open
  name: Stability AI Stable Image Generate API
  slug: open-stability-ai-stable-image-generate
- collection_type: open
  name: Stability AI Stable Image Upscale API
  slug: open-stability-ai-stable-image-upscale
- collection_type: open
  name: Stability AI Stable Video Diffusion API
  slug: open-stability-ai-stable-video-diffusion
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Structure API
  slug: open-stability-ai-structure-api
- collection_type: open
  name: Stability AI Stable Fast 3D 3D Generation Style API
  slug: open-stability-ai-style-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/stability-ai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stability-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stability-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stability-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stability-ai
- group: company
  title: ''
  type: Website
  url: https://stability.ai
- group: docs
  title: ''
  type: Documentation
  url: https://platform.stability.ai/docs/getting-started
- group: start
  title: ''
  type: Portal
  url: https://platform.stability.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://stability.ai/api-pricing-update-25
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stability.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stability.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://stability.ai/news-updates
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/stability-ai
- group: design
  title: ''
  type: JSONLD
  url: json-ld/stability-ai-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/stability-ai-image-generation-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/stability-ai-image-generation-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/stability-ai-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/stability-ai-rules.yml
created: '2026-03-20'
description: Stability AI is an AI company that develops open-source generative AI models for image, audio, video, and language, including the Stable Diffusion family of image generation models. The Stability AI developer platform provides REST APIs for text-to-image generation, image editing, image upscaling, image structure control, video generation, and 3D asset creation. All APIs are accessible at api.stability.ai using bearer token authentication.
examples:
- key_count: 3
  name: Stability Ai Generate Image Core Example
  slug: stability-ai-generate-image-core-example
features:
- 'API Membership $20/mo: 6,000 credits ($60 worth) included'
- 1 credit = $0.01
- 'SD3 (Stable Diffusion 3): ~$0.035 per image (3.5 credits)'
- 'Stable Image Ultra: $0.08 per image (8 credits, SD3.5 Large)'
- 'Stable Image Core: lower-cost mid-quality option'
- Stable Diffusion XL (SDXL)
- Stable Video Diffusion
- Stable 3D for 3D model generation
- Stable Audio for music generation
- 'Enterprise: volume discounts, self-hosted/private models'
- REST API at api.stability.ai
- Default 150 req/10s per key
- 'Image generation: 10 concurrent jobs'
- 'Video generation: 5 concurrent jobs'
- Bearer token (API key) auth
- Open-weights models (research / community use)
finops:
- name: Stability Ai Finops
  service_category: AI Image/Video Generation
  slug: stability-ai-finops
graphqls:
- description: This conceptual GraphQL schema represents the Stability AI developer platform, which provides generative AI APIs for image generation, image editing, image upscaling, video generation, audio generatio
  name: Stability AI GraphQL Schema
  slug: stability-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stability-ai.png
json_schemas:
- name: AsyncGenerationResponse
  property_count: 2
  slug: stability-ai-asyncgenerationresponse
- name: ConservativeUpscaleRequest
  property_count: 5
  slug: stability-ai-conservativeupscalerequest
- name: ControlImageResponse
  property_count: 3
  slug: stability-ai-controlimageresponse
- name: CreativeUpscaleRequest
  property_count: 5
  slug: stability-ai-creativeupscalerequest
- name: EditImageResponse
  property_count: 3
  slug: stability-ai-editimageresponse
- name: EraseRequest
  property_count: 4
  slug: stability-ai-eraserequest
- name: ErrorResponse
  property_count: 3
  slug: stability-ai-errorresponse
- name: FastUpscaleRequest
  property_count: 2
  slug: stability-ai-fastupscalerequest
- name: Generate3DResponse
  property_count: 2
  slug: stability-ai-generate3dresponse
- name: GenerateCoreRequest
  property_count: 6
  slug: stability-ai-generatecorerequest
- name: GenerateImageResponse
  property_count: 3
  slug: stability-ai-generateimageresponse
- name: GenerateSD3Request
  property_count: 9
  slug: stability-ai-generatesd3request
- name: GenerateUltraRequest
  property_count: 5
  slug: stability-ai-generateultrarequest
- name: Stability AI Image Generation
  property_count: 9
  slug: stability-ai-image-generation
- name: ImageToVideoRequest
  property_count: 4
  slug: stability-ai-imagetovideorequest
- name: InpaintRequest
  property_count: 6
  slug: stability-ai-inpaintrequest
- name: OutpaintRequest
  property_count: 8
  slug: stability-ai-outpaintrequest
- name: RemoveBackgroundRequest
  property_count: 2
  slug: stability-ai-removebackgroundrequest
- name: ReplaceBackgroundAndRelightRequest
  property_count: 6
  slug: stability-ai-replacebackgroundandrelightrequest
- name: SearchAndRecolorRequest
  property_count: 6
  slug: stability-ai-searchandrecolorrequest
- name: SearchAndReplaceRequest
  property_count: 6
  slug: stability-ai-searchandreplacerequest
- name: SketchControlRequest
  property_count: 6
  slug: stability-ai-sketchcontrolrequest
- name: StableFast3DRequest
  property_count: 4
  slug: stability-ai-stablefast3drequest
- name: StructureControlRequest
  property_count: 6
  slug: stability-ai-structurecontrolrequest
- name: StyleControlRequest
  property_count: 6
  slug: stability-ai-stylecontrolrequest
- name: UpscaleImageResponse
  property_count: 3
  slug: stability-ai-upscaleimageresponse
- name: VideoGenerationResponse
  property_count: 3
  slug: stability-ai-videogenerationresponse
json_structures:
- name: Stability Ai Image Generation Structure
  property_count: 2
  slug: stability-ai-image-generation-structure
- name: Stability Ai Structure
  property_count: 0
  slug: stability-ai-structure
jsonld:
- class_count: 0
  name: Stability Ai Context
  property_count: 8
  slug: stability-ai-context
layout: provider
modified: '2026-05-19'
name: Stability AI
nav: Providers
network: true
overview: 'Stability AI publishes 18 APIs on the [APIs.io](https://apis.io/) network, including 3D Generation API, Conservative Upscale API, Creative Upscale API, and 15 more. Tagged areas include 3D Generation, Artificial Intelligence, Generative AI, Image-Generation, and Image Editing.


  The Stability AI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Stability AI''s developer surface includes authentication, documentation, developer portal, pricing, engineering blog, and 13 more developer resources.'
plans:
- name: Stability Ai Plans Pricing
  plan_count: 4
  slug: stability-ai-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Stability Ai Rate Limits
  slug: stability-ai-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Stability AI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: stability-ai-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Stability AI API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 7
  slug: stability-ai-rules
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 18
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 65.1
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 13.2
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stability-ai/refs/heads/main/screenshots/stability-ai-2026-06-20T194438.png
security:
- kind: authentication
  name: Stability Ai Authentication
  slug: stability-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Stability Ai Domain Security
  slug: stability-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: stability-ai
tags:
- 3D Generation
- Artificial Intelligence
- Generative AI
- Image-Generation
- Image Editing
- Machine-Learning
- Stable Diffusion
- Text-to-Image
- Video Generation
website: https://stability.ai
---
