---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.w.ai/v1
  baseurl_source: declared
  description: Image generation and editing
  name: Wombo Images API
  slug: wombo-images-api
- baseURL: https://api.w.ai/v1
  baseurl_source: declared
  description: Model discovery
  name: Wombo Models API
  slug: wombo-models-api
- baseURL: https://api.w.ai/v1
  baseurl_source: declared
  description: Object detection and segmentation
  name: Wombo Predictions API
  slug: wombo-predictions-api
- baseURL: https://api.w.ai/v1
  baseurl_source: declared
  description: Text and vision-language chat completions
  name: Wombo Chat Completions API
  slug: wombo-chat-completions-api
artifact_total: 14
collections:
- collection_type: open
  name: w.ai Inference Chat API
  slug: open-wombo-chat-api
- collection_type: open
  name: w.ai Inference Chat Images API
  slug: open-wombo-images-api
- collection_type: open
  name: w.ai Inference Chat Models API
  slug: open-wombo-models-api
- collection_type: open
  name: w.ai Inference Chat Predictions API
  slug: open-wombo-predictions-api
common:
- group: company
  title: ''
  type: Website
  url: https://w.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.w.ai/dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://docs.w.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.w.ai/w.ai-api/api-features
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.w.ai/get-started/quick-start
- group: start
  title: ''
  type: SignUp
  url: https://app.w.ai/dashboard
- group: operate
  title: ''
  type: Support
  url: https://docs.w.ai/bugs-and-support/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://discord.gg/w-ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/womboai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.w.ai/compute/terms
- group: other
  title: ''
  type: Download
  url: https://download.w.ai
- group: auth
  href: https://artifacts.apis.io/wombo/authentication/wombo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wombo-authentication.yml
- group: design
  href: https://artifacts.apis.io/wombo/conventions/wombo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wombo-conventions.yml
- group: design
  href: https://artifacts.apis.io/wombo/errors/wombo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wombo-problem-types.yml
- group: build
  href: https://artifacts.apis.io/wombo/cli/wombo-cli.yml
  title: ''
  type: CLI
  url: cli/wombo-cli.yml
- group: build
  href: https://artifacts.apis.io/wombo/packages/wombo-packages.yml
  title: ''
  type: Packages
  url: packages/wombo-packages.yml
- group: agent
  href: https://artifacts.apis.io/wombo/mcp/wombo-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/wombo-mcp.yml
- group: agent
  href: https://artifacts.apis.io/wombo/llms/wombo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wombo-llms.txt
- group: design
  href: https://artifacts.apis.io/wombo/lifecycle/wombo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wombo-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wombo/conformance/wombo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wombo-conformance.yml
- group: design
  href: https://artifacts.apis.io/wombo/data-model/wombo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wombo-data-model.yml
- group: auth
  href: https://artifacts.apis.io/wombo/security/wombo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wombo-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/wombo/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/wombo/overlays/wombo-wai-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wombo-wai-overlay.yaml
created: '2026-07-17'
description: Wombo is the AI company behind Dream by WOMBO, a consumer AI art and video generator, and w.ai, a decentralized AI supercomputer that pools idle GPU compute worldwide to serve affordable on-demand inference. The w.ai developer platform exposes an OpenAI-compatible HTTP API at api.w.ai/v1 covering model discovery, text and vision-language chat completions with tool calling and streaming, text-to-image generation and editing (FLUX, SDXL), and object detection and segmentation (YOLO11n, SAM2) over images and video, plus a `wai` CLI and rentable Jupyter/SSH compute environments. Backed by 500 Global.
image: https://w.ai/wai-logo.png
layout: provider
modified: '2026-07-21'
name: Wombo
nav: Providers
network: true
overview: 'Wombo publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Images API, Models API, Predictions API, and 1 more. Tagged areas include Company, Artificial Intelligence, Machine Learning, Inference, and LLM.


  The Wombo catalog on APIs.io includes 1 Spectral governance ruleset.


  Wombo''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, CLI, and 17 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Wombo API Rules
  rule_count: 53
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 1
  slug: wombo-rules
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    contract_governance: 18.2
    contract_quality: 14.3
    developer_ergonomics: 63.7
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 30.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/wombo/wombo-2026-09-02T170908.png
security:
- kind: authentication
  name: Wombo Authentication
  slug: wombo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wombo Domain Security
  slug: wombo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Generate a chat completion on w.ai
  slug: wombo-chat-completion
- name: Detect and segment objects on w.ai
  slug: wombo-detect-and-segment
- name: Generate and edit images on w.ai
  slug: wombo-image-generation
slug: wombo
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Inference
- LLM
- Image Generation
- Generative AI
- Decentralized Compute
- GPU
- OpenAI-Compatible
website: https://w.ai/
---
