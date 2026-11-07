---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.modelrush.ai/v1
  baseurl_source: declared
  description: The Audio API from ModelRush — 2 operation(s) for audio.
  name: ModelRush Audio API
  slug: modelrush-audio-api
- baseURL: https://api.modelrush.ai/v1
  baseurl_source: declared
  description: The Discovery API from ModelRush — 2 operation(s) for discovery.
  name: ModelRush Discovery API
  slug: modelrush-discovery-api
- baseURL: https://api.modelrush.ai/v1
  baseurl_source: declared
  description: The Images API from ModelRush — 2 operation(s) for images.
  name: ModelRush Images API
  slug: modelrush-images-api
- baseURL: https://api.modelrush.ai/v1
  baseurl_source: declared
  description: The Predictions API from ModelRush — 1 operation(s) for predictions.
  name: ModelRush Predictions API
  slug: modelrush-predictions-api
- baseURL: https://api.modelrush.ai/v1
  baseurl_source: declared
  description: The Uploads API from ModelRush — 2 operation(s) for uploads.
  name: ModelRush Uploads API
  slug: modelrush-uploads-api
- baseURL: https://api.modelrush.ai/v1
  baseurl_source: declared
  description: The Video API from ModelRush — 2 operation(s) for video.
  name: ModelRush Video API
  slug: modelrush-video-api
- baseURL: https://api.modelrush.ai/v1
  baseurl_source: declared
  description: The Webhooks API from ModelRush — 1 operation(s) for webhooks.
  name: ModelRush Webhooks API
  slug: modelrush-webhooks-api
- baseURL: https://api.modelrush.ai/v1
  baseurl_source: declared
  description: The Chat Completions API from ModelRush — 1 operation(s) for chat completions.
  name: ModelRush Chat Completions API
  slug: modelrush-chat-completions-api
artifact_total: 21
asyncapis:
- description: ''
  name: Modelrush Webhooks
  slug: modelrush-webhooks
collections:
- collection_type: postman
  name: ModelRush Public API
  slug: postman-ModelRush-Public-API
common:
- group: other
  href: https://artifacts.apis.io/modelrush/capabilities/modelrush-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/modelrush-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/modelrush/plans/modelrush-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/modelrush-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/modelrush/rate-limits/modelrush-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/modelrush-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/modelrush/mcp/modelrush-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/modelrush-mcp.yml
- group: other
  href: https://artifacts.apis.io/modelrush/overlays/modelrush-public-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/modelrush-public-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/modelrush/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/modelrush/security/modelrush-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/modelrush-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/modelrush/security/modelrush-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/modelrush-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/modelrush/security/modelrush-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/modelrush-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/modelrush/authentication/modelrush-authentication.yml
  title: ''
  type: Authentication
  url: authentication/modelrush-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://modelrush.ai
- group: company
  title: ''
  type: Blog
  url: https://modelrush.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Moonveil-AI
- group: operate
  title: ''
  type: Support
  url: https://modelrush.ai/docs/faq
- group: start
  title: ''
  type: Login
  url: https://modelrush.ai/dashboard
- group: start
  title: ''
  type: SignUp
  url: https://modelrush.ai/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://modelrush.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://modelrush.ai/privacy
created: '2026-09-10'
description: A multilingual multimodal AI API platform (text, image, video, speech) serving a hosted model catalog -- open-weight families (DeepSeek, GLM, CosyVoice, Fun-ASR) alongside grok-family entries -- behind one bearer key with a public keyless model inventory and per-model regional pricing.
finops:
- has_sources: true
  method: derived
  name: Modelrush Finops
  primary_unit: 1m tokens
  service_category: ''
  slug: modelrush-finops
  template: false
layout: provider
mcp_servers:
- description: MCP server; 13 tools listed. A candidate, not confirmed as published by the provider.
  name: ModelRush MCP Server
  slug: modelrush-mcp-yml
modified: '2026-09-10'
name: ModelRush
nav: Providers
network: true
overview: 'ModelRush publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Discovery API, Images API, and 5 more. Tagged areas include Artificial Intelligence, LLM, Inference, Multi-Modal, and Model Hosting.


  The ModelRush catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ModelRush''s developer surface includes authentication, engineering blog, support, signup flow, and 14 more developer resources.'
plans:
- name: Modelrush Plans Pricing
  plan_count: 13
  slug: modelrush-plans-pricing
- name: Modelrush Price Estimates
  plan_count: 0
  slug: modelrush-price-estimates
random_paper: 19
rate_limits:
- limit_count: 0
  name: Modelrush Rate Limits
  slug: modelrush-rate-limits
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: ModelRush API Rules
  rule_count: 61
  severity_counts:
    error: 59
    hint: 0
    info: 1
    warn: 1
  slug: modelrush-rules
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 54.5
    catalog_earned_first_party: 12.0
    catalog_gap: 60.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 55.8
    developer_ergonomics: 53.7
    discoverability: 69.6
    operational_transparency: 36.8
  previous_composite: 56.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/modelrush/modelrush-2026-10-11T111159.png
security:
- kind: authentication
  name: Modelrush Authentication
  slug: modelrush-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Modelrush Domain Security
  slug: modelrush-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Modelrush Vulnerability Disclosure
  slug: modelrush-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 2
skills:
- name: modelrush-async-media-generation
  slug: modelrush-async-media-generation
- name: modelrush-chat-completion
  slug: modelrush-chat-completion
slug: modelrush
tags:
- Artificial Intelligence
- LLM
- Inference
- Multi-Modal
- Model Hosting
- Speech
- Image Generation
website: https://modelrush.ai
---
