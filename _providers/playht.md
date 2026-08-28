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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Playht Agentic Access
  operation_count: 13
  slug: playht-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 8
apis:
- description: The PlayAI Text-to-Speech API converts text into natural, human-like speech using the PlayDialog 1.0, Dialog 1.0 Turbo, and Play 3.0 Mini models. It supports streaming, voice cloning, and a large cata
  name: PlayAI Text-to-Speech API
  slug: tts-api
- description: The PlayAI Voice Agents API lets developers create, configure, and run conversational AI agents that process voice input and respond with generated speech, with optional tool use and external integrat
  name: PlayAI Voice Agents API
  slug: agents-api
- description: Voice agent management.
  name: PlayHT Agents API
  slug: playht-agents-api
- description: Agent conversation retrieval.
  name: PlayHT Conversations API
  slug: playht-conversations-api
- description: Tool definitions for voice agents.
  name: PlayHT External Functions API
  slug: playht-external-functions-api
- description: Document-to-audio PlayNote jobs.
  name: PlayHT PlayNote API
  slug: playht-playnote-api
- description: Text-to-speech generation, streaming, and async jobs.
  name: PlayHT TTS API
  slug: playht-tts-api
- description: Prebuilt voice catalog.
  name: PlayHT Voices API
  slug: playht-voices-api
artifact_total: 24
asyncapis:
- description: AsyncAPI 2.6 description of the PlayAI (formerly PlayHT) realtime WebSocket APIs. Covers the Text-to-Speech (TTS) streaming WebSocket used to synthesize audio from text in real time, and the Voice Age
  name: PlayAI Realtime WebSocket APIs
  slug: playht-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PlayAI Agents API
  slug: open-playht-agents-api
- collection_type: open
  name: PlayAI Agents Conversations API
  slug: open-playht-conversations-api
- collection_type: open
  name: PlayAI Agents External Functions API
  slug: open-playht-external-functions-api
- collection_type: open
  name: PlayAI Agents PlayNote API
  slug: open-playht-playnote-api
- collection_type: open
  name: PlayAI Agents TTS API
  slug: open-playht-tts-api
- collection_type: open
  name: PlayAI Agents Voices API
  slug: open-playht-voices-api
- collection_type: open
  name: PlayAI API
  slug: open-playht
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/playht-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/playht-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/playht-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://play.ht
- group: docs
  title: ''
  type: Documentation
  url: https://docs.play.ai
- group: company
  title: ''
  type: Blog
  url: https://play.ht/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/playht
- group: commercial
  title: ''
  type: Pricing
  url: https://play.ht/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://play.ht/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://play.ht/privacy
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/VuP4nXVA9M
- group: other
  title: ''
  type: X
  url: https://x.com/play_ht
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/playht
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.play.ai/llms.txt
created: '2026-05-23'
description: PlayHT, now operating as PlayAI, is a generative voice platform offering realistic text-to-speech models, AI voice agents, and a podcast generation tool called PlayNote. The platform centers on the PlayDialog and Play 3.0 Mini models, providing more than 200 prebuilt voices across multiple languages and accents with sub-second latency suited to conversational applications. PlayAI exposes REST and streaming endpoints for text-to-speech, voice listing, voice cloning, and voice agent management. It ships Python and Node.js SDKs and a hosted playground, and integrates with the major voice agent infrastructure stacks. The product is widely used to build voice assistants, IVRs, narration pipelines, and content production workflows.
finops:
- name: Playht Finops
  service_category: API
  slug: playht-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/playht.png
layout: provider
modified: '2026-05-29'
name: PlayHT
nav: Providers
network: true
overview: 'PlayHT publishes 8 APIs on the [APIs.io](https://apis.io/) network, including PlayAI Text-to-Speech API, PlayAI Voice Agents API, Agents API, and 5 more. Tagged areas include Voice, TTS, Text-to-Speech, Voice Cloning, and Voice Agents.


  The PlayHT catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  PlayHT''s developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Playht Plans Pricing
  plan_count: 1
  slug: playht-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Playht Rate Limits
  slug: playht-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: PlayHT API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: playht-asyncapi-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: 7.1
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 13.6
    contract_quality: 48.8
    developer_ergonomics: 42.9
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
security:
- kind: authentication
  name: Playht Authentication
  slug: playht-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Playht Domain Security
  slug: playht-domain-security
  summary_line: TLSv1.3 · DMARC
slug: playht
tags:
- Voice
- TTS
- Text-to-Speech
- Voice Cloning
- Voice Agents
- Streaming
- PlayDialog
- Play 3.0
- PlayNote
- Multilingual
- Real-Time
website: https://play.ht
---
