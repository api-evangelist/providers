---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://runwayml.com/'', ''status'': 308, ''note'': ''declared website redirects to https://runway.com/ — a different registrable domain (runwayml.com -> runway.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Runway Agentic Access
  operation_count: 17
  slug: runway-agentic-access
  summary_line: 17 operations · 15 acting
api_count: 3
apis:
- description: The Runway Python SDK provides a convenient Python library for interacting with the Runway API. Supports Python 3.8+ with type annotations compatible with MyPy. Includes automatic retries, best-practi
  name: Runway Python SDK
  slug: python-sdk
- description: The Runway Node.js SDK provides a JavaScript and TypeScript library for integrating with the Runway API. Supports Node.js 18+ with TypeScript bindings, automatic retries, and best-practice error handl
  name: Runway Node.js SDK
  slug: nodejs-sdk
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Create and manage persistent avatar personas with defined appearance, voice, and personality. Avatars can be created from a single reference image in any visual style.
  name: Runway Avatars API
  slug: runway-avatars-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Control a character's facial expressions and body movements using a reference performance video with the Act Two model.
  name: Runway Character Performance API
  slug: runway-character-performance-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Upload and manage domain-specific knowledge documents that avatars can reference during conversations to provide accurate, contextual responses. Each avatar supports up to 50,000 tokens of knowledge.
  name: Runway Documents API
  slug: runway-documents-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Interpolate between video frames to increase frame rate and smoothness.
  name: Runway Frame Interpolation API
  slug: runway-frame-interpolation-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Generate videos from input images with optional text prompts using Gen-4, Gen-4 Turbo, Gen-4.5, or Aleph models.
  name: Runway Image to Video API
  slug: runway-image-to-video-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Create generative videos where a selected face speaks lines from audio clips or AI-generated voices, supporting 28+ languages.
  name: Runway Lip Sync API
  slug: runway-lip-sync-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Create live WebRTC sessions connecting users to avatars for real-time conversational interactions. Each session has a maximum duration of 5 minutes.
  name: Runway Realtime Sessions API
  slug: runway-realtime-sessions-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Generate sound effects for videos using AI.
  name: Runway Sound Effects API
  slug: runway-sound-effects-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Retrieve status and output of asynchronous generation tasks.
  name: Runway Tasks API
  slug: runway-tasks-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Generate high-quality images from text prompts using the Gen-4 Image model.
  name: Runway Text to Image API
  slug: runway-text-to-image-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Generate videos from text prompts alone using Gen-4.5, Veo 3.1, or Veo 3.1 Fast models.
  name: Runway Text to Video API
  slug: runway-text-to-video-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Upload temporary media files that can be referenced in generation requests.
  name: Runway Uploads API
  slug: runway-uploads-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Generate new videos from existing video inputs using the Gen-4 Aleph model.
  name: Runway Video to Video API
  slug: runway-video-to-video-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Upscale video resolution and quality.
  name: Runway Video Upscale API
  slug: runway-video-upscale-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Generate video from an image and prompt (Gen-4 Turbo, Gen-4.5).
  name: Runway Image-to-Video API
  slug: runwayml-image-to-video-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Usage tier and credit balance for the API organization.
  name: Runway Organization API
  slug: runwayml-organization-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Generate images from a prompt (Gen-4 Image, Gen-4 Image Turbo).
  name: Runway Text-to-Image API
  slug: runwayml-text-to-image-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Synthesize speech audio from text.
  name: Runway Text-to-Speech API
  slug: runwayml-text-to-speech-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Upscale a video to higher resolution.
  name: Runway Upscale API
  slug: runwayml-upscale-api
- baseURL: https://api.dev.runwayml.com/v1
  baseurl_source: declared
  description: Edit / restyle an existing video (Aleph).
  name: Runway Video-to-Video API
  slug: runwayml-video-to-video-api
artifact_total: 89
asyncapis:
- description: The Runway Characters realtime event interface describes the WebRTC-based communication protocol for live conversational avatar sessions powered by GWM-1. Once a realtime session is created via the RE
  name: Runway Characters Realtime Events
  slug: runway-characters-asyncapi
collections:
- collection_type: postman
  name: Runway Characters Avatars API
  slug: postman-runway-avatars-api
- collection_type: postman
  name: Runway Characters Avatars Character Performance API
  slug: postman-runway-character-performance-api
- collection_type: postman
  name: Runway Characters Avatars Documents API
  slug: postman-runway-documents-api
- collection_type: postman
  name: Runway Characters Avatars Frame Interpolation API
  slug: postman-runway-frame-interpolation-api
- collection_type: postman
  name: Runway Characters Avatars Image to Video API
  slug: postman-runway-image-to-video-api
- collection_type: postman
  name: Runway Characters Avatars Lip Sync API
  slug: postman-runway-lip-sync-api
- collection_type: postman
  name: Runway Characters Avatars Realtime Sessions API
  slug: postman-runway-realtime-sessions-api
- collection_type: postman
  name: Runway Characters Avatars Sound Effects API
  slug: postman-runway-sound-effects-api
- collection_type: postman
  name: Runway Characters Avatars Tasks API
  slug: postman-runway-tasks-api
- collection_type: postman
  name: Runway Characters Avatars Text to Image API
  slug: postman-runway-text-to-image-api
- collection_type: postman
  name: Runway Characters Avatars Text to Video API
  slug: postman-runway-text-to-video-api
- collection_type: postman
  name: Runway Characters Avatars Uploads API
  slug: postman-runway-uploads-api
- collection_type: postman
  name: Runway Characters Avatars Video to Video API
  slug: postman-runway-video-to-video-api
- collection_type: postman
  name: Runway Characters Avatars Video Upscale API
  slug: postman-runway-video-upscale-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Runway Characters Avatars API
  slug: open-runway-avatars-api
- collection_type: open
  name: Runway Characters Avatars Character Performance API
  slug: open-runway-character-performance-api
- collection_type: open
  name: Runway Characters API
  slug: open-runway-characters
- collection_type: open
  name: Runway Characters Avatars Documents API
  slug: open-runway-documents-api
- collection_type: open
  name: Runway Characters Avatars Frame Interpolation API
  slug: open-runway-frame-interpolation-api
- collection_type: open
  name: Runway Image Generation API
  slug: open-runway-image-generation
- collection_type: open
  name: Runway Characters Avatars Image to Video API
  slug: open-runway-image-to-video-api
- collection_type: open
  name: Runway Characters Avatars Lip Sync API
  slug: open-runway-lip-sync-api
- collection_type: open
  name: Runway Characters Avatars Realtime Sessions API
  slug: open-runway-realtime-sessions-api
- collection_type: open
  name: Runway Characters Avatars Sound Effects API
  slug: open-runway-sound-effects-api
- collection_type: open
  name: Runway Characters Avatars Tasks API
  slug: open-runway-tasks-api
- collection_type: open
  name: Runway Characters Avatars Text to Image API
  slug: open-runway-text-to-image-api
- collection_type: open
  name: Runway Characters Avatars Text to Video API
  slug: open-runway-text-to-video-api
- collection_type: open
  name: Runway Characters Avatars Uploads API
  slug: open-runway-uploads-api
- collection_type: open
  name: Runway Video Generation API
  slug: open-runway-video-generation
- collection_type: open
  name: Runway Characters Avatars Video to Video API
  slug: open-runway-video-to-video-api
- collection_type: open
  name: Runway Characters Avatars Video Upscale API
  slug: open-runway-video-upscale-api
- collection_type: open
  name: Runway API
  slug: open-runwayml
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/runwayml/sdk-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/runwayml/sdk-python/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/runwayml/sdk-python/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/runwayml/sdk-python/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/runwayml/sdk-python/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/runway/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/runway-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runway-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/runway-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/runwayml
- group: start
  title: ''
  type: Portal
  url: https://docs.dev.runwayml.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dev.runwayml.com/api/
- group: company
  title: ''
  type: Website
  url: https://runwayml.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.runwayml.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runwayml.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runwayml.com/terms-of-use
- group: company
  title: ''
  type: Blog
  url: https://runwayml.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.runwayml.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runwayml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dev.runwayml.com/api-details/api_changelog/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/runway-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/runway-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/runwayml/runway-api-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/runwayml/runway-characters-meeting-skill
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.dev.runwayml.com/llms.txt
created: '2025-03-01'
description: Runway is an applied AI research company that builds generative AI tools for creative professionals. Their developer platform provides APIs for video generation, image generation, real-time conversational avatar experiences, media uploads, and audio synthesis powered by advanced generative models including Gen-4, Gen-4 Turbo, Gen-4.5, Gen-4 Aleph, Veo 3.1, Act Two, and GWM-1 (General World Model). The API uses asynchronous task processing with Bearer token authentication.
examples:
- key_count: 3
  name: Runway Create Avatar Example
  slug: runway-create-avatar-example
- key_count: 3
  name: Runway Create Video Example
  slug: runway-create-video-example
features:
- 'Free: 125 one-time credits with Gen-4 Turbo image'
- 'Standard at $12/mo annual: 625 credits, all video models'
- 'Pro at $28/mo: 2,250 credits, custom voices'
- 'Unlimited at $76/mo: 2,250 credits + unlimited Explore Mode'
- 'Enterprise: SSO, custom org spaces, Workspace Analytics'
- Gen-4.5, Gen-4, Gen-4 Turbo video generation
- Image generation (Gen-4, Gemini 3 Pro/2.5)
- Text-to-Speech with custom voices
- Lip Sync
- Upscaling and watermark removal
- REST API for video/image generation
- Webhooks for completion notification
- OAuth 2.0 + API tokens
- Asset storage (5 GB Free, 100/500 GB paid)
- Video editor with unlimited projects on paid
- Enterprise integrations with internal tools
finops:
- name: Runway Finops
  service_category: Video Generation AI
  slug: runway-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/runway.png
json_schemas:
- name: Runway Avatar
  property_count: 8
  slug: runway-avatar
- name: Runway Generation Task
  property_count: 5
  slug: runway-task
json_structures:
- name: Runway Task Structure
  property_count: 0
  slug: runway-task-structure
jsonld:
- class_count: 0
  name: Runway Context
  property_count: 7
  slug: runway-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Runway
nav: Providers
network: true
overview: 'Runway publishes 20 APIs on the [APIs.io](https://apis.io/) network, including Avatars API, Character Performance API, Documents API, and 17 more. Tagged areas include Video Generation, Image-Generation, Artificial Intelligence, Machine-Learning, and Generative AI.


  The Runway catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Runway''s developer surface includes authentication, developer portal, documentation, engineering blog, changelog, and 20 more developer resources.'
plans:
- name: Runway Plans Pricing
  plan_count: 5
  slug: runway-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Runway Rate Limits
  slug: runway-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Runway API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 8
  slug: runway-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Runway API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: runway-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Runway API Rules
  rule_count: 17
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 11
  slug: runway-rules
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.5
    catalog_earned_first_party: 0.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 28.8
    contract_quality: 67.9
    developer_ergonomics: 39.3
    discoverability: 72.2
    governance: 28.8
    operational_transparency: 34.2
  open_source:
    applies: true
    score: 85.0
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runway/refs/heads/main/screenshots/runway-2026-06-20T193255.png
security:
- kind: authentication
  name: Runway Authentication
  slug: runway-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Runway Domain Security
  slug: runway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: runway-characters-meeting
  slug: runway-characters-meeting
slug: runway
tags:
- Video Generation
- Image-Generation
- Artificial Intelligence
- Machine-Learning
- Generative AI
- Avatars
- Characters
- WebRTC
- Creative Tools
website: https://runwayml.com/
---
