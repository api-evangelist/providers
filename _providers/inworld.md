---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Inworld Agentic Access
  operation_count: 19
  slug: inworld-agentic-access
  summary_line: 19 operations · 13 acting
api_count: 4
apis:
- description: TTS-2 and TTS-1.5 (Max/Mini) models for character voice synthesis. Priced per 1M characters with plan-tier discounts.
  name: Inworld Text-to-Speech API
  slug: tts
- description: Multi-provider transcription API priced at $0.35/hour standard rate.
  name: Inworld Speech-to-Text API
  slug: stt
- description: Low-latency speech-to-speech voice API for natural conversation experiences. Included with all plans.
  name: Inworld Realtime API
  slug: realtime
- description: Routing layer over 220+ LLM models, billed at provider cost via Inworld's unified API.
  name: Inworld LLM Router API
  slug: llm-router
artifact_total: 12
collections:
- collection_type: open
  name: Inworld AI API
  slug: open-inworld
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/inworld-a2a.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inworld-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/inworld-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inworld-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inworld-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inworld-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inworld-ai
- group: company
  title: ''
  type: Website
  url: https://inworld.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inworld.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/inworld-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inworld-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/inworld-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.inworld.ai/llms.txt
created: '2026-05-08'
description: Inworld AI provides voice and conversational AI building blocks for games and interactive media. Public APIs cover Text-to-Speech, Speech-to-Text, a Realtime speech-to-speech API, and an LLM Router that fronts 220+ third-party models with unified billing.
finops:
- name: Inworld Finops
  service_category: AI
  slug: inworld-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-05-08'
name: Inworld AI
nav: Providers
network: true
overview: 'Inworld AI publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Voice, Characters, Games, and Conversational.


  Inworld AI''s developer surface includes authentication, documentation, and 11 more developer resources.'
plans:
- name: Inworld Plans Pricing
  plan_count: 5
  slug: inworld-plans-pricing
random_paper: 56
rate_limits:
- limit_count: 4
  name: Inworld Rate Limits
  slug: inworld-rate-limits
score:
  band: emerging
  composite: 27.0
  delta: -14.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 8.1
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/inworld/refs/heads/main/screenshots/inworld-2026-06-20T183534.png
security:
- kind: authentication
  name: Inworld Authentication
  slug: inworld-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inworld Domain Security
  slug: inworld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Inworld Trust Center
  slug: inworld-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: inworld
tags:
- AI
- Voice
- Characters
- Games
- Conversational
website: https://inworld.ai/
---
