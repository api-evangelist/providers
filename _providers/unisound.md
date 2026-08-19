---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: 'Multi-modal MaaS API for Unisound U2 models: OpenAI-compatible chat completions and Anthropic-compatible messages for the U2 and U2-Med LLMs (streaming, function calling, structured output, context ca'
  name: Unisound Token Hub API
  slug: unisound-token-hub-api
- description: REST chat-completions WebAPI for the Shanhai (山海 / UniGPT) large language model on the Unisound AI Open Platform. POST rest/v1.1/chat/completions with signature-based authentication (SHA-256 over appk
  name: Unisound Shanhai (UniGPT) LLM WebAPI
  slug: unisound-shanhai-unigpt-llm-webapi
- description: 'WebSocket speech APIs on the Unisound AI Open Platform: one-sentence speech recognition (Mandarin, Cantonese, Sichuanese, English; domain models for medical, finance, law, and more), real-time transcr'
  name: Unisound AI Open Platform Speech WebAPI
  slug: unisound-ai-open-platform-speech-webapi
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unisound-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unisound.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ai.unisound.com
- group: docs
  title: ''
  type: Documentation
  url: https://maas.unisound.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://maas.unisound.com/docs/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://maas.unisound.com/docs/guide/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://maas.unisound.com/docs/price/overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://maas.unisound.com/docs/protocol/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://maas.unisound.com/docs/protocol/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://maas.unisound.com/docs/guide/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Unisound
- group: start
  title: ''
  type: SignUp
  url: https://maas.unisound.com/
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unisound-rate-limits.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://maas.unisound.com/docs/api/rate-limits
- group: operate
  title: ''
  type: ChangeLog
  url: https://maas.unisound.com/docs/release/notes
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/unisound-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/unisound-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unisound-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unisound-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/unisound-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unisound-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unisound-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/unisound-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/unisound-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unisound-conventions.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/unisound-plans.yml
created: '2026-07-17'
description: Unisound (云知声) is a Chinese AGI technology company delivering conversational AI across smart living and smart healthcare. Its Token Hub MaaS platform exposes OpenAI- and Anthropic-compatible APIs for the Unisound U2 agent-native large language model and U2-Med medical model, plus U2-ASR speech transcription, U2-TTS synthesis and voice cloning, voiceprint, and U1-OCR document parsing services, alongside the legacy AI Open Platform WebSocket speech APIs and the Shanhai (UniGPT) LLM WebAPI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unisound.png
layout: provider
modified: '2026-07-21'
name: Unisound
nav: Providers
network: true
overview: 'Unisound publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Speech Recognition, Text-to-Speech, and Voice Cloning.


  Unisound''s developer surface includes documentation, API reference, getting-started guide, pricing, support, signup flow, changelog, and 19 more developer resources.'
plans:
- name: Unisound Plans
  plan_count: 3
  slug: unisound-plans
random_paper: 140
rate_limits:
- limit_count: 9
  name: Unisound Rate Limits
  slug: unisound-rate-limits
score:
  band: developing
  composite: 48.9
  delta: 5.6
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 43.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/unisound/refs/heads/main/screenshots/unisound-2026-08-17T082618.png
security:
- kind: authentication
  name: Unisound Authentication
  slug: unisound-authentication
  summary_line: apiKey/signature · 3 schemes
- kind: domain-security
  name: Unisound Domain Security
  slug: unisound-domain-security
  summary_line: TLSv1.3 · HSTS
slug: unisound
tags:
- Company
- Artificial Intelligence
- Speech Recognition
- Text-to-Speech
- Voice Cloning
- Large Language Models
- OCR
- Healthcare
- Machine Learning
- Voice
website: https://www.unisound.com
---
