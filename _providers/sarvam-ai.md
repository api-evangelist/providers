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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sarvam Ai Agentic Access
  operation_count: 7
  slug: sarvam-ai-agentic-access
  summary_line: 7 operations · 7 acting
api_count: 1
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
artifact_total: 22
asyncapis:
- description: AsyncAPI 2.6 description of Sarvam AI's **chat completion streaming** surface. Sarvam's chat completions endpoint streams partial results as **HTTP Server-Sent Events (SSE)** over the same REST endpoi
  name: Sarvam AI Chat Completions Streaming (HTTP + SSE)
  slug: sarvam-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sarvam AI Chat API
  slug: open-sarvam-ai-chat-api
- collection_type: open
  name: Sarvam AI Chat Language Identification API
  slug: open-sarvam-ai-language-identification-api
- collection_type: open
  name: Sarvam AI Chat Speech to Text API
  slug: open-sarvam-ai-speech-to-text-api
- collection_type: open
  name: Sarvam AI Chat Text to Speech API
  slug: open-sarvam-ai-text-to-speech-api
- collection_type: open
  name: Sarvam AI Chat Translate API
  slug: open-sarvam-ai-translate-api
- collection_type: open
  name: Sarvam AI Chat Transliterate API
  slug: open-sarvam-ai-transliterate-api
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
overview: 'Sarvam AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Language Identification API, Speech to Text API, and 3 more. Tagged areas include Artificial Intelligence, LLM, Speech-to-Text, Text-to-Speech, and Translation.


  The Sarvam AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Sarvam AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Sarvam Ai Plans Pricing
  plan_count: 3
  slug: sarvam-ai-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Sarvam Ai Rate Limits
  slug: sarvam-ai-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Sarvam AI API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: sarvam-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 47.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 63.1
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sarvam-ai/refs/heads/main/screenshots/sarvam-ai-2026-08-17T081724.png
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
- Artificial Intelligence
- LLM
- Speech-to-Text
- Text-to-Speech
- Translation
- Indian Languages
website: https://www.sarvam.ai
---
