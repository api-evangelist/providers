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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 138
  human_in_the_loop: 4
  name: Beatra Ai Agentic Access
  operation_count: 208
  slug: beatra-ai-agentic-access
  summary_line: 208 operations · 138 acting · 4 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The account API from Beatra AI — 112 operation(s) for account.
  name: Beatra AI Account API
  slug: beatra-ai-account-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The account-feedback API from Beatra AI — 4 operation(s) for account-feedback.
  name: Beatra AI Account Feedback API
  slug: beatra-ai-account-feedback-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The audio API from Beatra AI — 2 operation(s) for audio.
  name: Beatra AI Audio API
  slug: beatra-ai-audio-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The catalog API from Beatra AI — 5 operation(s) for catalog.
  name: Beatra AI Catalog API
  slug: beatra-ai-catalog-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The health API from Beatra AI — 3 operation(s) for health.
  name: Beatra AI Health API
  slug: beatra-ai-health-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The images API from Beatra AI — 4 operation(s) for images.
  name: Beatra AI Images API
  slug: beatra-ai-images-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The mcp-device-authorization API from Beatra AI — 8 operation(s) for mcp-device-authorization.
  name: Beatra AI MCP Device Authorization API
  slug: beatra-ai-mcp-device-authorization-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The music API from Beatra AI — 2 operation(s) for music.
  name: Beatra AI Music API
  slug: beatra-ai-music-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The Payments API from Beatra AI — 1 operation(s) for payments.
  name: Beatra AI Payments API
  slug: beatra-ai-payments-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The tasks API from Beatra AI — 3 operation(s) for tasks.
  name: Beatra AI Tasks API
  slug: beatra-ai-tasks-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The uploads API from Beatra AI — 1 operation(s) for uploads.
  name: Beatra AI Uploads API
  slug: beatra-ai-uploads-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The videos API from Beatra AI — 9 operation(s) for videos.
  name: Beatra AI Videos API
  slug: beatra-ai-videos-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The voices API from Beatra AI — 3 operation(s) for voices.
  name: Beatra AI Voices API
  slug: beatra-ai-voices-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The webhooks API from Beatra AI — 1 operation(s) for webhooks.
  name: Beatra AI Webhooks API
  slug: beatra-ai-webhooks-api
- baseURL: https://api.beatra.ai
  baseurl_source: declared
  description: The Chat Completions API from Beatra AI — 1 operation(s) for chat completions.
  name: Beatra AI Chat Completions API
  slug: beatra-ai-chat-completions-api
artifact_total: 33
asyncapis:
- description: ''
  name: Beatra Ai Webhooks
  slug: beatra-ai-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/beatra-ai/agentic-access/beatra-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beatra-ai-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/beatra-ai/rate-limits/beatra-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/beatra-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/beatra-ai/plans/beatra-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beatra-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/beatra-ai/rules/beatra-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/beatra-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/beatra-ai/json-ld/beatra-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beatra-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/beatra-ai/vocabulary/beatra-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beatra-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/beatra-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/beatra-ai/asyncapi/beatra-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/beatra-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/beatra-ai/data-model/beatra-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beatra-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/beatra-ai/conventions/beatra-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/beatra-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/beatra-ai/conventions/beatra-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/beatra-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/beatra-ai/authentication/beatra-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beatra-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/beatra-ai/errors/beatra-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beatra-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/beatra-ai/conformance/beatra-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beatra-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beatra-ai/llms/beatra-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beatra-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/beatra-ai/well-known/beatra-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beatra-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/beatra-ai/hosts/beatra-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beatra-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/beatra-ai/vendors/beatra-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beatra-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beatra.ai/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beatra.ai/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://beatra.ai/en/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beatra-ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beatra.ai/en/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beatra.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.beatra.ai\
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beatra.ai/en/docs/api-reference
- group: auth
  href: https://artifacts.apis.io/beatra-ai/security/beatra-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beatra-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beatra.ai/
created: '2026-11-02'
description: Beatra AI provides a multimodal AI platform that enables developers to generate images, video, music, speech, and retrieve social data through simple API calls. The service offers a unified interface for creative content generation, supports various model capabilities, and includes detailed documentation, pricing, and authentication guides for seamless integration into applications.
image: https://beatra.ai/brand/og-default.png
json_schemas:
- name: ChatCompletionRequest
  property_count: 30
  slug: beatra-ai-chat-completion-request
- name: FramesToVideoRequest
  property_count: 19
  slug: beatra-ai-frames-to-video-request
- name: ImageEditRequest
  property_count: 13
  slug: beatra-ai-image-edit-request
- name: ImageToVideoRequest
  property_count: 18
  slug: beatra-ai-image-to-video-request
- name: VideoEditRequest
  property_count: 19
  slug: beatra-ai-video-edit-request
- name: VideoExtendRequest
  property_count: 19
  slug: beatra-ai-video-extend-request
jsonld:
- class_count: 120
  name: Beatra Ai Context
  property_count: 378
  slug: beatra-ai-context
layout: provider
modified: '2026-11-02'
name: Beatra AI
nav: Providers
network: true
overview: 'Beatra AI publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account Feedback API, Audio API, and 12 more. Tagged areas include Company, Artificial Intelligence, Multi-Modal, Generation, and Social Data.


  The Beatra AI catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Beatra AI''s developer surface includes authentication, pricing, getting-started guide, documentation, API reference, and 23 more developer resources.'
plans:
- name: Beatra Ai Plans Pricing
  plan_count: 4
  slug: beatra-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Beatra Ai Rate Limits
  slug: beatra-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Beatra AI API Rules
  rule_count: 44
  severity_counts:
    error: 28
    hint: 0
    info: 2
    warn: 14
  slug: beatra-ai-rules
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 62.8
    developer_ergonomics: 32.7
    discoverability: 66.1
    operational_transparency: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 64.3
      derived: 0
      marker_coverage: 0.0
      total: 15
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Beatra Ai Authentication
  slug: beatra-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Beatra Ai Domain Security
  slug: beatra-ai-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: beatra-ai-cancel-task
  slug: beatra-ai-cancel-task
- name: beatra-ai-clone-and-activate-voice
  slug: beatra-ai-clone-and-activate-voice
- name: beatra-ai-create-edit-images
  slug: beatra-ai-create-edit-images
- name: beatra-ai-update-profile
  slug: beatra-ai-update-profile
slug: beatra-ai
tags:
- Company
- Artificial Intelligence
- Multi-Modal
- Generation
- Social Data
website: https://beatra.ai/
---
