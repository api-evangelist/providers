---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 41
  human_in_the_loop: 3
  name: Ludo Ai Agentic Access
  operation_count: 60
  slug: ludo-ai-agentic-access
  summary_line: 60 operations · 41 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: The Ludo.ai MCP Server exposes the platform's asset generation tools via the Model Context Protocol, allowing AI assistants like Claude and Cursor to generate game assets through natural language conv
  name: Ludo.ai MCP Server
  slug: mcp-server
- description: 'The Ludo.ai Unity Plugin integrates AI-powered asset generation directly into the Unity game engine. It provides a native interface for Unity developers to access Ludo.ai''s image generation, 3D model '
  name: Ludo.ai Unity Plugin
  slug: unity-plugin
- baseURL: https://api.ludo.ai/api/
  baseurl_source: declared
  description: Generate sound effects, background music, character voices, and text-to-speech audio for games.
  name: Ludo.ai Audio API
  slug: ludo-ai-audio-api
- baseURL: https://api.ludo.ai/api/
  baseurl_source: declared
  description: Generate, edit, and manipulate game-ready images including sprites, icons, UI assets, textures, and backgrounds.
  name: Ludo.ai Images API
  slug: ludo-ai-images-api
- baseURL: https://api.ludo.ai/api/
  baseurl_source: declared
  description: Retrieve previously generated assets using request IDs or browse recent API-generated content.
  name: Ludo.ai Results API
  slug: ludo-ai-results-api
- baseURL: https://api.ludo.ai/api/
  baseurl_source: declared
  description: Generate short videos from images with motion prompts, suitable for cinematics, trailers, and dynamic backgrounds.
  name: Ludo.ai Video API
  slug: ludo-ai-video-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: The 3D Models API from Ludo.ai — 6 operation(s) for 3d models.
  name: Ludo.ai 3D Models API
  slug: ludo-ai-3d-models-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: The Account API from Ludo.ai — 3 operation(s) for account.
  name: Ludo.ai Account API
  slug: ludo-ai-account-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: Create animated spritesheets from static sprites, transfer motion from videos or presets, and list available animation presets.
  name: Ludo.ai Animation API
  slug: ludo-ai-animation-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: The Authentication API from Ludo.ai — 1 operation(s) for authentication.
  name: Ludo.ai Authentication API
  slug: ludo-ai-authentication-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: The Documentation API from Ludo.ai — 2 operation(s) for documentation.
  name: Ludo.ai Documentation API
  slug: ludo-ai-documentation-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: The Files API from Ludo.ai — 1 operation(s) for files.
  name: Ludo.ai Files API
  slug: ludo-ai-files-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: The Generations API from Ludo.ai — 1 operation(s) for generations.
  name: Ludo.ai Generations API
  slug: ludo-ai-generations-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: The Jobs API from Ludo.ai — 2 operation(s) for jobs.
  name: Ludo.ai Jobs API
  slug: ludo-ai-jobs-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: The Spritesheets API from Ludo.ai — 10 operation(s) for spritesheets.
  name: Ludo.ai Spritesheets API
  slug: ludo-ai-spritesheets-api
- baseURL: https://mcp.ludo.ai/mcp
  baseurl_source: declared
  description: The Videos API from Ludo.ai — 5 operation(s) for videos.
  name: Ludo.ai Videos API
  slug: ludo-ai-videos-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ludo.ai REST 3D Models API
  slug: open-ludo-ai-3d-models-api
- collection_type: open
  name: Ludo.ai REST 3D Models Animation API
  slug: open-ludo-ai-animation-api
- collection_type: open
  name: Ludo.ai REST 3D Models Audio API
  slug: open-ludo-ai-audio-api
- collection_type: open
  name: Ludo.ai REST 3D Models Images API
  slug: open-ludo-ai-images-api
- collection_type: open
  name: Ludo.ai REST API
  slug: open-ludo-ai-rest-api
- collection_type: open
  name: Ludo.ai REST 3D Models Results API
  slug: open-ludo-ai-results-api
- collection_type: open
  name: Ludo.ai REST 3D Models Video API
  slug: open-ludo-ai-video-api
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/security/ludo-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ludo-ai-vulnerability-disclosure.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/mcp/ludo-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ludo-ai-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/security/ludo-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ludo-ai-vulnerability-disclosure.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/finops/ludo-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/ludo-ai-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/rate-limits/ludo-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ludo-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/plans/ludo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ludo-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/rules/ludo-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/ludo-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/rules/ludo-ai-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/ludo-ai-jsonschema-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/vocabulary/ludo-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ludo-ai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/data-model/ludo-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ludo-ai-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/cli/ludo-ai-cli.yml
  title: ''
  type: CLI
  url: cli/ludo-ai-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/changelog/ludo-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ludo-ai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/errors/ludo-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ludo-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/conformance/ludo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ludo-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/llms/ludo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ludo-ai-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/well-known/ludo-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ludo-ai-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/well-known/ludo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ludo-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/hosts/ludo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ludo-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/vendors/ludo-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ludo-ai-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/packages/ludo-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/ludo-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/packages/ludo-ai-packages.yml
  title: ''
  type: Packages
  url: packages/ludo-ai-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ludo.ai/privacy-policies
- group: commercial
  title: ''
  type: Pricing
  url: https://ludo.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://ludo.ai/whats-new
- group: docs
  title: ''
  type: APIReference
  url: https://api.ludo.ai/api-documentation/openapi.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/agentic-access/ludo-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ludo-ai-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/security/ludo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ludo-ai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/authentication/ludo-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ludo-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ludoai
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/json-ld/ludo-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ludo-ai-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/json-schema/ludo-ai-game-asset-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/ludo-ai-game-asset-schema.json
- group: company
  title: ''
  type: Website
  url: https://ludo.ai/
- group: start
  title: ''
  type: Portal
  url: https://ludo.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://ludo.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://ludo.ai/blog/introducing-ludo-ai-api-mcp-integration
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ludo-AI
- group: start
  title: ''
  type: Login
  url: https://ludo.ai/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Ludo-AI/ludo-mcp
created: '2026-03-24'
description: Ludo.ai is a game design hub that uses artificial intelligence to help developers generate production-ready game assets including images, 3D models, audio, and animations. The platform entered beta for its Model Context Protocol (MCP) integration, exposing its asset generation suite as a headless API that enables vibe coding where developers can trigger asset creation directly from AI assistants like Claude or Cursor.
finops:
- name: Ludo Ai Finops
  service_category: AI Infrastructure
  slug: ludo-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ludo-ai.png
json_schemas:
- name: AnimateSpriteKeyframesPayload
  property_count: 21
  slug: ludo-ai-animate-sprite-keyframes-payload
- name: AnimateSpritePayload
  property_count: 20
  slug: ludo-ai-animate-sprite-payload
- name: AudioResponse
  property_count: 2
  slug: ludo-ai-audio-response
- name: AudioResultsResponse
  property_count: 1
  slug: ludo-ai-audio-results-response
- name: CreateImageRequest
  property_count: 7
  slug: ludo-ai-create-image-request
- name: CreateMusicRequest
  property_count: 3
  slug: ludo-ai-create-music-request
- name: CreateSoundEffectRequest
  property_count: 3
  slug: ludo-ai-create-sound-effect-request
- name: CreateSpeechPresetRequest
  property_count: 5
  slug: ludo-ai-create-speech-preset-request
- name: CreateSpeechRequest
  property_count: 3
  slug: ludo-ai-create-speech-request
- name: CreateVideoRequest
  property_count: 6
  slug: ludo-ai-create-video-request
- name: CreateVoiceRequest
  property_count: 4
  slug: ludo-ai-create-voice-request
- name: EditImageRequest
  property_count: 5
  slug: ludo-ai-edit-image-request
- name: EditSpritesheetPayloadPublic
  property_count: 15
  slug: ludo-ai-edit-spritesheet-payload-public
- name: Ludo.ai Game Asset
  property_count: 10
  slug: ludo-ai-game-asset
- name: GenerateImagePayload
  property_count: 9
  slug: ludo-ai-generate-image-payload
- name: GeneratePoseRequest
  property_count: 5
  slug: ludo-ai-generate-pose-request
- name: GenerateVideoPayloadPublic
  property_count: 8
  slug: ludo-ai-generate-video-payload-public
- name: GenerateWithStyleRequest
  property_count: 5
  slug: ludo-ai-generate-with-style-request
- name: ImageResponse
  property_count: 2
  slug: ludo-ai-image-response
- name: ImageResultsResponse
  property_count: 1
  slug: ludo-ai-image-results-response
- name: Model3DResultsResponse
  property_count: 1
  slug: ludo-ai-model3-dresults-response
- name: PoseResponse
  property_count: 2
  slug: ludo-ai-pose-response
- name: SpriteResultsResponse
  property_count: 1
  slug: ludo-ai-sprite-results-response
- name: TransferMotionPayload
  property_count: 21
  slug: ludo-ai-transfer-motion-payload
- name: VideoResponse
  property_count: 2
  slug: ludo-ai-video-response
- name: VideoResultsResponse
  property_count: 1
  slug: ludo-ai-video-results-response
jsonld:
- class_count: 0
  name: Ludo Ai Context
  property_count: 7
  slug: ludo-ai-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Ludo.ai
nav: Providers
network: true
overview: 'Ludo.ai publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Audio API, Images API, Results API, and 13 more. Tagged areas include Artificial Intelligence, Asset Generation, Game Design, Game Development, and Game Asset Generation.


  The Ludo.ai catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ludo.ai''s developer surface includes CLI, changelog, pricing, API reference, authentication, developer portal, documentation, and 32 more developer resources.'
plans:
- name: Ludo Ai Plans Pricing
  plan_count: 2
  slug: ludo-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 7
  name: Ludo Ai Rate Limits
  slug: ludo-ai-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Ludo.ai API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ludo-ai-jsonschema-spectral-rules
- effective_rule_count: 56
  extends:
  - spectral:oas
  name: Ludo.ai API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: ludo-ai-rules
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.1
  facets:
    access_clarity: 56.6
    contract_governance: 22.0
    contract_quality: 57.2
    developer_ergonomics: 56.5
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 42.9
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/ludo-ai/refs/heads/main/screenshots/ludo-ai-2026-06-20T184746.png
security:
- kind: authentication
  name: Ludo Ai Authentication
  slug: ludo-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ludo Ai Domain Security
  slug: ludo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ludo Ai Vulnerability Disclosure
  slug: ludo-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ludo-ai
tags:
- Artificial Intelligence
- Asset Generation
- Game Design
- Game Development
- Game Asset Generation
- AI Art
- Sprite Sheets
website: https://ludo.ai/
---
