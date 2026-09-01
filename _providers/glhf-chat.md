---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.7
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Glhf Chat Agentic Access
  operation_count: 2
  slug: glhf-chat-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: The Chat API from glhf — 1 operation(s) for chat.
  name: glhf Chat API
  slug: glhf-chat-chat-api
- description: The Models API from glhf — 1 operation(s) for models.
  name: glhf Models API
  slug: glhf-chat-models-api
artifact_total: 14
asyncapis:
- description: AsyncAPI 2.6 description of glhf's (glhf.chat) **chat completion streaming** surface. glhf does not publish a WebSocket API. Its OpenAI-compatible REST API exposes chat completions at `POST /chat/comp
  name: glhf Chat Completions Streaming (HTTP + SSE)
  slug: glhf-chat-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: AgenticAccess
  url: agentic-access/glhf-chat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glhf-chat-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/glhf-chat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/glhf-chat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/glhf-chat-finops.yml
created: '2026-06-21'
description: glhf (glhf.chat) runs almost any open-source large language model on demand through an auto-scaling GPU scheduler built on vLLM. Any Hugging Face repository can be served by passing its identifier as hf:org/model to an OpenAI-compatible REST API, giving access to models like Llama, Qwen, and Mixtral without self-hosting.
finops:
- name: Glhf Chat Finops
  service_category: AI and Machine Learning
  slug: glhf-chat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glhf-chat.png
layout: provider
modified: '2026-06-21'
name: glhf
nav: Providers
network: true
overview: 'glhf publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Models API. Tagged areas include Artificial Intelligence, LLM, Inference, Open Source Models, and Hugging Face.


  The glhf catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  glhf''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Glhf Chat Plans Pricing
  plan_count: 2
  slug: glhf-chat-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Glhf Chat Rate Limits
  slug: glhf-chat-rate-limits
rules:
- effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: glhf API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: glhf-chat-asyncapi-spectral-rules
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 66.3
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 31.6
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
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
