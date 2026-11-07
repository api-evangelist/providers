---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Glhf Chat Agentic Access
  operation_count: 2
  slug: glhf-chat-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://glhf.chat/api/openai/v1
  baseurl_source: declared
  description: The Models API from glhf — 1 operation(s) for models.
  name: glhf Models API
  slug: glhf-chat-models-api
- baseURL: https://glhf.chat/api/openai/v1
  baseurl_source: declared
  description: The Chat Completions API from glhf — 1 operation(s) for chat completions.
  name: glhf Chat Completions API
  slug: glhf-chat-chat-completions-api
artifact_total: 13
asyncapis:
- description: AsyncAPI 2.6 description of glhf's (glhf.chat) **chat completion streaming** surface. glhf does not publish a WebSocket API. Its OpenAI-compatible REST API exposes chat completions at `POST /chat/comp
  name: glhf Chat Completions Streaming (HTTP + SSE)
  slug: glhf-chat-asyncapi
collections:
- collection_type: open
  name: glhf Chat API
  slug: open-glhf-chat-chat-api
- collection_type: open
  name: glhf Chat Models API
  slug: open-glhf-chat-models-api
- collection_type: open
  name: glhf API
  slug: open-glhf-chat
common:
- group: agent
  href: https://artifacts.apis.io/glhf-chat/agentic-access/glhf-chat-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/glhf-chat-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/glhf-chat/security/glhf-chat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/glhf-chat-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/glhf-chat/authentication/glhf-chat-authentication.yml
  title: ''
  type: Authentication
  url: authentication/glhf-chat-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glhf-chat
- group: company
  title: ''
  type: Website
  url: https://glhf.chat
- group: docs
  title: ''
  type: Documentation
  url: https://glhf.chat/users/settings/api
- group: commercial
  href: https://artifacts.apis.io/glhf-chat/plans/glhf-chat-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/glhf-chat-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/glhf-chat/rate-limits/glhf-chat-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/glhf-chat-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/glhf-chat/finops/glhf-chat-finops.yml
  title: ''
  type: FinOps
  url: finops/glhf-chat-finops.yml
created: '2026-06-21'
description: glhf (glhf.chat) runs almost any open-source large language model on demand through an auto-scaling GPU scheduler built on vLLM. Any Hugging Face repository can be served by passing its identifier as hf:org/model to an OpenAI-compatible REST API, giving access to models like Llama, Qwen, and Mixtral without self-hosting.
finops:
- has_sources: true
  method: generated
  name: Glhf Chat Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: glhf-chat-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glhf-chat.png
layout: provider
modified: '2026-06-21'
name: glhf
nav: Providers
network: true
overview: 'glhf publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Models API and Chat Completions API. Tagged areas include Artificial Intelligence, LLM, Inference, Open Source Models, and Hugging Face.


  The glhf catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  glhf''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Glhf Chat Plans Pricing
  plan_count: 2
  slug: glhf-chat-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Glhf Chat Rate Limits
  slug: glhf-chat-rate-limits
rules:
- authorship: generated
  effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: glhf — asyncapi rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: glhf-chat-asyncapi-spectral-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.8
    catalog_earned_first_party: 0.0
    catalog_gap: 69.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 11.4
    contract_quality: 59.7
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 27.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/glhf-chat/glhf-chat-2026-10-11T185810.png
security:
- kind: authentication
  name: Glhf Chat Authentication
  slug: glhf-chat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Glhf Chat Domain Security
  slug: glhf-chat-domain-security
  summary_line: TLSv1.3
slug: glhf-chat
tags:
- Artificial Intelligence
- LLM
- Inference
- Open Source Models
- Hugging Face
website: https://glhf.chat
---
