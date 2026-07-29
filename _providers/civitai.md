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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Civitai Agentic Access
  operation_count: 29
  slug: civitai-agentic-access
  summary_line: 29 operations · 9 acting
api_count: 12
apis:
- description: OAuth 2.0 authorization-code with PKCE for third-party apps that act on behalf of a Civitai user. Supports scoped tokens, refresh flow, and per-app Buzz spend caps so a delegated app cannot drain a us
  name: Civitai OAuth API
  slug: civitai-oauth-api
- description: Upload and reference blobs for inputs and outputs.
  name: Civitai Blobs API
  slug: civitai-blobs-api
- description: Users who publish models.
  name: Civitai Creators API
  slug: civitai-creators-api
- description: Enumerations used throughout the API.
  name: Civitai Enums API
  slug: civitai-enums-api
- description: Community-shared generation outputs.
  name: Civitai Images API
  slug: civitai-images-api
- description: Catalog of model checkpoints, LoRAs, embeddings, and VAEs.
  name: Civitai Models API
  slug: civitai-models-api
- description: Specific versions of a model with files, hashes, and AIR identifiers.
  name: Civitai ModelVersions API
  slug: civitai-modelversions-api
- description: Permission checks for the current bearer.
  name: Civitai Permissions API
  slug: civitai-permissions-api
- description: Catalog tag taxonomy.
  name: Civitai Tags API
  slug: civitai-tags-api
- description: User accounts.
  name: Civitai Users API
  slug: civitai-users-api
- description: A user's saved-model vault (membership tiers).
  name: Civitai Vault API
  slug: civitai-vault-api
- description: Submit and manage generation workflows.
  name: Civitai Workflows API
  slug: civitai-workflows-api
arazzos:
- description: Resolve many file hashes to version ids in bulk, then enrich the first match with model detail.
  name: Civitai Batch Hash Reconciliation
  slug: civitai-batch-hash-reconcile-workflow
- description: Upload a source image blob, run an img2img workflow against it, poll, and read the result.
  name: Civitai Blob Upload and Image-to-Image Generation
  slug: civitai-blob-upload-img2img-workflow
- description: Find a creator, list the models they publish, and pull a gallery of images for one model.
  name: Civitai Creator Models and Image Gallery
  slug: civitai-creator-models-gallery-workflow
- description: Submit an image generation workflow, poll until it finishes, and collect the output blobs.
  name: Civitai Image Generation Submit and Poll
  slug: civitai-image-generation-poll-workflow
- description: Open a model, browse its community images, and resolve the version behind the top image.
  name: Civitai Model Images Explorer
  slug: civitai-model-images-explorer-workflow
- description: Resolve a local model file's hash to its model version, then load the parent model.
  name: Civitai Identify a Model From a File Hash
  slug: civitai-model-version-by-hash-workflow
- description: Resolve a catalog model version's AIR, generate an image with it, poll, and read the result.
  name: Civitai Generate From a Catalog Model Version
  slug: civitai-model-version-to-generation-workflow
- description: Resolve a model version, check the bearer's permissions, and branch on download rights.
  name: Civitai Permission-Gated Version Download
  slug: civitai-permission-gated-download-workflow
- description: Request a presigned blob upload URL, reference the blob in a workflow with webhook callbacks, and poll.
  name: Civitai Presigned Blob Upload Then Generate
  slug: civitai-presigned-blob-generate-workflow
- description: Search the model catalog, open the top matching model, and resolve one of its versions.
  name: Civitai Search Models and Drill Into a Version
  slug: civitai-search-models-detail-workflow
- description: Pick a tag from the taxonomy, list models carrying that tag, and open the top model.
  name: Civitai Tag-Driven Model Discovery
  slug: civitai-tag-models-discovery-workflow
- description: Confirm the user, check vault capacity, add a model version to the vault, and verify storage.
  name: Civitai Vault Add and Verify
  slug: civitai-vault-toggle-verify-workflow
- description: List active workflows, inspect the first one, cancel it, and confirm the canceled state.
  name: Civitai Query and Cancel a Running Workflow
  slug: civitai-workflow-query-cancel-workflow
artifact_total: 64
collections:
- collection_type: postman
  name: Civitai Orchestration API
  slug: postman-civitai-orchestration-api
- collection_type: postman
  name: Civitai Site API
  slug: postman-civitai-site-api
- collection_type: open
  name: Civitai Orchestration API
  slug: open-civitai-orchestration-api
- collection_type: open
  name: Civitai Site API
  slug: open-civitai-site-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/civitai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/civitai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/civitai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/civitai-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/civitai/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-batch-hash-reconcile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-blob-upload-img2img-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-creator-models-gallery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-image-generation-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-model-images-explorer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-model-version-by-hash-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-model-version-to-generation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-permission-gated-download-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-presigned-blob-generate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-search-models-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-tag-models-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-vault-toggle-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/civitai-workflow-query-cancel-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/civitai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/HelloCivitai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/civitai
- group: start
  title: ''
  type: Portal
  url: https://civitai.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.civitai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://education.civitai.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.civitai.com/orchestration/guide/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.civitai.com/orchestration/guide/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://developer.civitai.com/orchestration/guide/results-and-webhooks
- group: design
  title: ''
  type: ErrorCodes
  url: https://developer.civitai.com/orchestration/guide/errors-and-retries
- group: start
  title: ''
  type: Signup
  url: https://civitai.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://civitai.com/content/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://civitai.com/content/privacy
- group: other
  title: ''
  type: ContentPolicy
  url: https://civitai.com/content/content-policy
- group: operate
  title: ''
  type: Support
  url: https://education.civitai.com/
- group: company
  title: ''
  type: Blog
  url: https://civitai.com/articles
- group: operate
  title: ''
  type: Forums
  url: https://education.civitai.com/forums/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/civitai/civitai-client-javascript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/civitai/civitai-app-starters
- group: build
  title: ''
  type: Tools
  url: https://github.com/civitai/civitai-link-desktop
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/civitai/civitai
- group: build
  title: ''
  type: Tools
  url: https://github.com/civitai/ai-toolkit
- group: build
  title: ''
  type: Tools
  url: https://github.com/civitai/model-scanner
- group: build
  title: ''
  type: Tools
  url: https://github.com/civitai/ComfyUI
- group: build
  title: ''
  type: Plugins
  url: https://github.com/civitai/ComfyUI_smZNodes
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/civitai/bitdex
- group: docs
  title: ''
  type: Documentation
  url: https://developer.civitai.com/site/guide/air
- group: agent
  title: ''
  type: MCPServer
  url: https://developer.civitai.com/orchestration/mcp
- group: docs
  title: ''
  type: Documentation
  url: https://developer.civitai.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://developer.civitai.com/llms-full.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/civitai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/civitai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/civitai-finops.yml
created: '2026-05-25'
description: Civitai is the largest open community for Stable Diffusion, SDXL, Flux, and video AI models — hosting over a million model checkpoints, LoRAs, embeddings, and VAEs uploaded and rated by creators. Beyond hosting, Civitai operates a hosted AI image, video, audio, and language generation service through its Orchestration API, which races workflows across providers (Flux 1/2, SDXL, SD1, Z-Image, Qwen, Seedream, Grok, WAN 2.1-2.7, Kling, LTX2, Vidu, Veo 3, HunyuanVideo) and supports LoRA training jobs. The Site API exposes the public catalog plus user vault, permissions, and AIR identifier resolution. OAuth 2.0 with PKCE and per-app Buzz spend caps lets third parties build delegated experiences without owning a user's full credit balance. Generation is metered in Buzz, a virtual credit topped up via memberships or one-off packs.
examples:
- key_count: 3
  name: Civitai Image Generation Example
  slug: civitai-image-generation-example
- key_count: 3
  name: Civitai Video Generation Example
  slug: civitai-video-generation-example
features:
- Largest community catalog of Stable Diffusion, SDXL, and Flux checkpoints, LoRAs, embeddings, and VAEs
- Image, video, audio, and language generation through a single Orchestration API
- Multi-provider workflow racing across Flux 1/2, SDXL, SD1, Z-Image, Qwen, Seedream, Grok, WAN, Kling, LTX2, Vidu, Veo 3, HunyuanVideo
- LoRA training jobs for SDXL, Flux, WAN, and LTX2 ecosystems
- AI Resource Identifier (AIR) URN scheme for unambiguously referencing models, versions, and weights
- Bearer-token authentication via per-user API keys, plus OAuth 2.0 + PKCE for third-party apps
- In-order, serialized webhooks for workflow, step, and job lifecycle events
- HTTPS-only webhook endpoints with retry on non-2xx; idempotency keyed on `(workflowId, status, timestamp)`
- Blob upload API with built-in NSFW moderation and presigned upload URLs
- Buzz credit system for metering generation, with per-app spend caps on delegated OAuth tokens
- Civitai Vault for membership-tier model storage and retrieval via API
- Hash-based model-version lookup for client tools (ComfyUI, A1111, Civitai Link)
- Public MCP server exposing Civitai as tools for Claude, Cursor, and other MCP-aware agents
- Open-source Civitai platform repo (TypeScript) on GitHub
- Official JavaScript SDK (`civitai-client-javascript`) and OAuth SDK (`civitai-app-starters`)
- Civitai Link Desktop for syncing models into local Stable Diffusion installs
- AI Toolkit for diffusion model finetuning; Model Scanner for safety/security checks
- Education portal and community articles, posts, comics, challenges, and bounties
finops:
- name: Civitai Finops
  service_category: AI and Machine Learning
  slug: civitai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/civitai.png
json_schemas:
- name: Civitai Image
  property_count: 12
  slug: civitai-image
- name: Civitai Model
  property_count: 14
  slug: civitai-model
- name: Civitai Orchestration Workflow
  property_count: 10
  slug: civitai-workflow
json_structures:
- name: Civitai Model Structure
  property_count: 0
  slug: civitai-model-structure
jsonld:
- class_count: 53
  name: Civitai Context
  property_count: 20
  slug: civitai-context
layout: provider
mcp_servers:
- description: ''
  name: Civitai MCP Server
  slug: civitai-mcp-server
modified: '2026-05-25'
name: Civitai
nav: Providers
network: true
overview: 'Civitai publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Blobs API, Creators API, Enums API, and 8 more. Tagged areas include AI, Artificial Intelligence, Image Generation, Video Generation, and Stable Diffusion.


  The Civitai catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Civitai''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, support, engineering blog, and 44 more developer resources.'
plans:
- name: Civitai Plans Pricing
  plan_count: 7
  slug: civitai-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 4
  name: Civitai Rate Limits
  slug: civitai-rate-limits
rules:
- name: Civitai API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: civitai-jsonschema-spectral-rules
- name: Civitai API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 7
  slug: civitai-rules
score:
  band: strong
  composite: 61.8
  delta: -3.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 71.8
    developer_ergonomics: 65.2
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 44.7
  previous_composite: 65.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/civitai/refs/heads/main/screenshots/civitai-2026-06-20T174434.png
security:
- kind: authentication
  name: Civitai Authentication
  slug: civitai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Civitai Domain Security
  slug: civitai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Civitai Vulnerability Disclosure
  slug: civitai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: civitai
tags:
- AI
- Artificial Intelligence
- Image Generation
- Video Generation
- Stable Diffusion
- SDXL
- Flux
- LoRA
- Model Hosting
- Community
- Generative AI
website: https://civitai.com
---
