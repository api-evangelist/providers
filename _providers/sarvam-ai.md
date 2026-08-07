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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sarvam Ai Agentic Access
  operation_count: 7
  slug: sarvam-ai-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 6
apis:
- description: The Chat API from Sarvam AI — 1 operation(s) for chat.
  name: Sarvam AI Chat API
  slug: sarvam-ai-chat-api
- description: The Language Identification API from Sarvam AI — 1 operation(s) for language identification.
  name: Sarvam AI Language Identification API
  slug: sarvam-ai-language-identification-api
- description: The Speech to Text API from Sarvam AI — 2 operation(s) for speech to text.
  name: Sarvam AI Speech to Text API
  slug: sarvam-ai-speech-to-text-api
- description: The Text to Speech API from Sarvam AI — 1 operation(s) for text to speech.
  name: Sarvam AI Text to Speech API
  slug: sarvam-ai-text-to-speech-api
- description: The Translate API from Sarvam AI — 1 operation(s) for translate.
  name: Sarvam AI Translate API
  slug: sarvam-ai-translate-api
- description: The Transliterate API from Sarvam AI — 1 operation(s) for transliterate.
  name: Sarvam AI Transliterate API
  slug: sarvam-ai-transliterate-api
artifact_total: 15
asyncapis:
- description: AsyncAPI 2.6 description of Sarvam AI's **chat completion streaming** surface. Sarvam's chat completions endpoint streams partial results as **HTTP Server-Sent Events (SSE)** over the same REST endpoi
  name: Sarvam AI Chat Completions Streaming (HTTP + SSE)
  slug: sarvam-ai-asyncapi
collections:
- collection_type: open
  name: Sarvam AI API
  slug: open-sarvam-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sarvam-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sarvam-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sarvam-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sarvamai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sarvam-ai
- group: company
  title: ''
  type: Website
  url: https://www.sarvam.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sarvam.ai/api-reference-docs/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/sarvam-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sarvam-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sarvam-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sarvam.ai/blogs
created: '2026-06-21'
description: Sarvam AI is India's full-stack sovereign AI platform building large language models, speech, and translation systems for Indian languages. The Sarvam API serves chat completions (Sarvam-M / Sarvam-30B / Sarvam-105B), speech-to-text (Saaras / Saarika), text-to-speech (Bulbul), translation (Mayura / Sarvam-Translate), transliteration, and language identification across 10-22 Indic languages via a REST interface using an api-subscription-key header.
finops:
- name: Sarvam Ai Finops
  service_category: AI and Machine Learning
  slug: sarvam-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sarvam-ai.png
layout: provider
modified: '2026-06-21'
name: Sarvam AI
nav: Providers
network: true
overview: 'Sarvam AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Language Identification API, Speech to Text API, and 3 more. Tagged areas include AI, LLM, Speech to Text, Text to Speech, and Translation.


  The Sarvam AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Sarvam AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sarvam Ai Plans Pricing
  plan_count: 3
  slug: sarvam-ai-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 4
  name: Sarvam Ai Rate Limits
  slug: sarvam-ai-rate-limits
rules:
- name: Sarvam AI API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: sarvam-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 47.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Sarvam Ai Authentication
  slug: sarvam-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sarvam Ai Domain Security
  slug: sarvam-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sarvam-ai
tags:
- AI
- LLM
- Speech to Text
- Text to Speech
- Translation
- Indian Languages
website: https://www.sarvam.ai
---
