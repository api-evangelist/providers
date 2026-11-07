---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
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
    error_semantics: false
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
  score: 23.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Sutra Ai Agentic Access
  operation_count: 2
  slug: sutra-ai-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.two.ai/v2
  baseurl_source: declared
  description: List available SUTRA models.
  name: SUTRA (Two AI) Models API
  slug: sutra-ai-models-api
- baseURL: https://api.two.ai/v2
  baseurl_source: declared
  description: OpenAI-compatible chat completions across SUTRA models.
  name: SUTRA (Two AI) Chat Completions API
  slug: sutra-ai-chat-completions-api
artifact_total: 13
asyncapis:
- description: AsyncAPI 2.6 description of SUTRA's **chat completion streaming** surface. Two AI (Numeric) does not publish a WebSocket API for SUTRA. The only asynchronous / event-style transport documented at http
  name: SUTRA Chat Completions Streaming (HTTP + SSE)
  slug: sutra-ai-asyncapi
collections:
- collection_type: open
  name: SUTRA Chat API
  slug: open-sutra-ai-chat-api
- collection_type: open
  name: SUTRA Chat Models API
  slug: open-sutra-ai-models-api
- collection_type: open
  name: SUTRA API
  slug: open-sutra-ai
common:
- group: company
  title: ''
  type: Blog
  url: https://www.two.ai/blog
- group: agent
  href: https://artifacts.apis.io/sutra-ai/agentic-access/sutra-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sutra-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/sutra-ai/security/sutra-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sutra-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sutra-ai/authentication/sutra-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sutra-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sutra-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/two-ai
- group: company
  title: ''
  type: Website
  url: https://www.two.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.two.ai/docs
- group: commercial
  href: https://artifacts.apis.io/sutra-ai/plans/sutra-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sutra-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/sutra-ai/rate-limits/sutra-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sutra-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/sutra-ai/finops/sutra-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/sutra-ai-finops.yml
created: '2026-06-21'
description: SUTRA is a family of multilingual large language models from Two AI (Numeric), fluent in 50+ languages including Hindi, Gujarati, Tamil, Bengali, Korean, Arabic, and Japanese. The SUTRA API is OpenAI-compatible and serves the SUTRA-V2 instruction/conversation model and the SUTRA-R0 reasoning model through a single Bearer-authenticated REST interface.
finops:
- has_sources: true
  method: generated
  name: Sutra Ai Finops
  primary_unit: ''
  service_category: AI and Machine Learning
  slug: sutra-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sutra-ai.png
layout: provider
modified: '2026-10-06'
name: SUTRA (Two AI)
nav: Providers
network: true
overview: 'SUTRA (Two AI) publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Models API and Chat Completions API. Tagged areas include Artificial Intelligence, LLM, Multilingual, Inference, and Reasoning.


  The SUTRA (Two AI) catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SUTRA (Two AI)''s developer surface includes engineering blog, authentication, documentation, and 8 more developer resources.'
plans:
- name: Sutra Ai Plans Pricing
  plan_count: 3
  slug: sutra-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 3
  name: Sutra Ai Rate Limits
  slug: sutra-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: SUTRA (Two AI) — asyncapi rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: sutra-ai-asyncapi-spectral-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 11.4
    contract_quality: 56.7
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 29.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sutra-ai/sutra-ai-2026-08-17T082207.png
security:
- kind: authentication
  name: Sutra Ai Authentication
  slug: sutra-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sutra Ai Domain Security
  slug: sutra-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sutra-ai
tags:
- Artificial Intelligence
- LLM
- Multilingual
- Inference
- Reasoning
- Real-Time
- Foundation Models
website: https://www.two.ai
---
