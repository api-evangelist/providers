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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 28
  human_in_the_loop: 1
  name: Hume Ai Agentic Access
  operation_count: 49
  slug: hume-ai-agentic-access
  summary_line: 49 operations · 28 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: The Ai Default API from Hume AI — 6 operation(s) for ai default.
  name: Hume AI Ai Default API
  slug: hume-ai-default-api
- description: The subpackage_batch API from Hume AI — 4 operation(s) for subpackage_batch.
  name: Hume AI subpackage_batch API
  slug: hume-ai-subpackage-batch-api
- description: The subpackage_chatGroups API from Hume AI — 4 operation(s) for subpackage_chatgroups.
  name: Hume AI subpackage_chatGroups API
  slug: hume-ai-subpackage-chatgroups-api
- description: The subpackage_chats API from Hume AI — 3 operation(s) for subpackage_chats.
  name: Hume AI subpackage_chats API
  slug: hume-ai-subpackage-chats-api
- description: The subpackage_configs API from Hume AI — 3 operation(s) for subpackage_configs.
  name: Hume AI subpackage_configs API
  slug: hume-ai-subpackage-configs-api
- description: The subpackage_controlPlane API from Hume AI — 1 operation(s) for subpackage_controlplane.
  name: Hume AI subpackage_controlPlane API
  slug: hume-ai-subpackage-controlplane-api
- description: The subpackage_prompts API from Hume AI — 3 operation(s) for subpackage_prompts.
  name: Hume AI subpackage_prompts API
  slug: hume-ai-subpackage-prompts-api
- description: The subpackage_tools API from Hume AI — 3 operation(s) for subpackage_tools.
  name: Hume AI subpackage_tools API
  slug: hume-ai-subpackage-tools-api
- description: The subpackage_voices API from Hume AI — 1 operation(s) for subpackage_voices.
  name: Hume AI subpackage_voices API
  slug: hume-ai-subpackage-voices-api
artifact_total: 31
asyncapis:
- description: 'Consolidated AsyncAPI definition for Hume AI''s two production WebSocket surfaces: - **Empathic Voice Interface (EVI)** — bidirectional speech-to-speech voice conversation at `wss://api.hume.ai/v0/evi/'
  name: Hume AI WebSocket APIs
  slug: hume-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Speech-to-speech (EVI)  API
  slug: open-hume-ai-default-api
- collection_type: open
  name: Speech-to-speech (EVI)
  slug: open-hume-ai-evi
- collection_type: open
  name: Expression Measurement API
  slug: open-hume-ai-expression
- collection_type: open
  name: Speech-to-speech (EVI) subpackage_batch API
  slug: open-hume-ai-subpackage-batch-api
- collection_type: open
  name: Speech-to-speech (EVI) subpackage_chatGroups API
  slug: open-hume-ai-subpackage-chatgroups-api
- collection_type: open
  name: Speech-to-speech (EVI) subpackage_chats API
  slug: open-hume-ai-subpackage-chats-api
- collection_type: open
  name: Speech-to-speech (EVI) subpackage_configs API
  slug: open-hume-ai-subpackage-configs-api
- collection_type: open
  name: Speech-to-speech (EVI) subpackage_controlPlane API
  slug: open-hume-ai-subpackage-controlplane-api
- collection_type: open
  name: Speech-to-speech (EVI) subpackage_prompts API
  slug: open-hume-ai-subpackage-prompts-api
- collection_type: open
  name: Speech-to-speech (EVI) subpackage_tools API
  slug: open-hume-ai-subpackage-tools-api
- collection_type: open
  name: Speech-to-speech (EVI) subpackage_voices API
  slug: open-hume-ai-subpackage-voices-api
- collection_type: open
  name: Text-to-Speech (TTS)
  slug: open-hume-ai-tts
- collection_type: open
  name: Voices
  slug: open-hume-ai-voices
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hume-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hume-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hume-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HumeAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hume-ai
- group: company
  title: ''
  type: Website
  url: https://www.hume.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.hume.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/hume-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hume-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hume-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hume.ai/blog
created: '2026-05-08'
description: 'Hume AI builds empathic voice and emotional AI models. The platform exposes four published APIs: Voices, Octave Text-to-Speech, Empathic Voice Interface (EVI / speech-to-speech), and Expression Measurement (multimodal emotion analysis). REST + WebSocket interfaces are documented with public OpenAPI and AsyncAPI specifications at https://dev.hume.ai/.'
finops:
- name: Hume Ai Finops
  service_category: AI
  slug: hume-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hume-ai.png
layout: provider
modified: '2026-05-29'
name: Hume AI
nav: Providers
network: true
overview: 'Hume AI publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Ai Default API, subpackage_batch API, subpackage_chatGroups API, and 6 more. Tagged areas include AI, Voice, Empathic, Emotion, and Multimodal.


  The Hume AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Hume AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Hume Ai Plans Pricing
  plan_count: 8
  slug: hume-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Hume Ai Rate Limits
  slug: hume-ai-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Hume AI API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: hume-ai-asyncapi-spectral-rules
score:
  band: thin
  composite: 34.2
  delta: -3.3
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 11.4
    contract_quality: 64.6
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 11.4
    operational_transparency: 10.5
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hume-ai/refs/heads/main/screenshots/hume-ai-2026-06-20T183040.png
security:
- kind: authentication
  name: Hume Ai Authentication
  slug: hume-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hume Ai Domain Security
  slug: hume-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hume-ai
tags:
- AI
- Voice
- Empathic
- Emotion
- Multimodal
website: https://www.hume.ai/
---
