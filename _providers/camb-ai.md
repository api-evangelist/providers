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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Camb Ai Agentic Access
  operation_count: 17
  slug: camb-ai-agentic-access
  summary_line: 17 operations · 8 acting
api_count: 1
apis:
- description: End-to-end video and audio dubbing across languages.
  name: Camb.AI Dubbing API
  slug: camb-ai-dubbing-api
- description: Supported source and target languages.
  name: Camb.AI Languages API
  slug: camb-ai-languages-api
- description: Convert text to speech with the MARS voice models.
  name: Camb.AI Text-to-Speech API
  slug: camb-ai-text-to-speech-api
- description: Speech-to-text transcription with timestamps.
  name: Camb.AI Transcription API
  slug: camb-ai-transcription-api
- description: Neural text translation via the BOLI model.
  name: Camb.AI Translation API
  slug: camb-ai-translation-api
- description: Discover, clone, design, and manage voices.
  name: Camb.AI Voices API
  slug: camb-ai-voices-api
artifact_total: 22
asyncapis:
- description: 'Camb.AI exposes public WebSocket channels for real-time voice AI in addition to its REST API. Three streaming surfaces are documented: live text-to-speech (stream text in, receive synthesized audio an'
  name: Camb.AI Realtime WebSocket API
  slug: camb-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Camb.AI Dubbing API
  slug: open-camb-ai-dubbing-api
- collection_type: open
  name: Camb.AI Dubbing Languages API
  slug: open-camb-ai-languages-api
- collection_type: open
  name: Camb.AI Dubbing Text-to-Speech API
  slug: open-camb-ai-text-to-speech-api
- collection_type: open
  name: Camb.AI Dubbing Transcription API
  slug: open-camb-ai-transcription-api
- collection_type: open
  name: Camb.AI Dubbing Translation API
  slug: open-camb-ai-translation-api
- collection_type: open
  name: Camb.AI Dubbing Voices API
  slug: open-camb-ai-voices-api
- collection_type: open
  name: Camb.AI API
  slug: open-camb-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/camb-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/camb-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/camb-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/camb-ai
- group: company
  title: ''
  type: Website
  url: https://www.camb.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.camb.ai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Camb-ai
- group: commercial
  title: ''
  type: Plans
  url: plans/camb-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/camb-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/camb-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.camb.ai/blog
created: '2026-07-11'
description: Camb.AI is a generative voice AI platform for translation, dubbing, and speech. Its research models - MARS (text-to-speech and voice cloning) and BOLI (neural translation) - power an API covering text-to-speech, end-to-end video and audio dubbing, text translation across 140+ languages, voice discovery and custom voice cloning, and speech-to-text transcription. The REST API lives at https://client.camb.ai/apis, is authenticated with an x-api-key header, and follows an asynchronous create-and-poll pattern (POST to start a task, GET the task by id until it succeeds, then fetch the result). Camb.AI also exposes public WebSocket surfaces for real-time streaming TTS, live transcription, and realtime speech-to-speech translation.
finops:
- name: Camb Ai Finops
  service_category: AI and Machine Learning
  slug: camb-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/camb-ai.png
layout: provider
modified: '2026-07-11'
name: Camb.AI
nav: Providers
network: true
overview: 'Camb.AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Dubbing API, Languages API, Text-to-Speech API, and 3 more. Tagged areas include Artificial Intelligence, Text to Speech, Dubbing, Translation, and Transcription.


  The Camb.AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Camb.AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Camb Ai Plans Pricing
  plan_count: 6
  slug: camb-ai-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Camb Ai Rate Limits
  slug: camb-ai-rate-limits
rules:
- effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: Camb.AI API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 9
  slug: camb-ai-asyncapi-spectral-rules
score:
  band: thin
  composite: 33.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 47.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 11.4
    contract_quality: 22.3
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 36.8
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/camb-ai/refs/heads/main/screenshots/camb-ai-2026-07-25T204253.png
security:
- kind: authentication
  name: Camb Ai Authentication
  slug: camb-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Camb Ai Domain Security
  slug: camb-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: camb-ai
tags:
- Artificial Intelligence
- Text to Speech
- Dubbing
- Translation
- Transcription
- Voice Cloning
- Speech
website: https://www.camb.ai
---
