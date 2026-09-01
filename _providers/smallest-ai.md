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
- acting_count: 4
  human_in_the_loop: 0
  name: Smallest Ai Agentic Access
  operation_count: 6
  slug: smallest-ai-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: The Atoms platform for building, testing, and deploying production voice agents - orchestrating Waves TTS and Pulse STT with LLM-driven conversation flows, exposed through a developer API and dashboar
  name: Smallest AI Atoms (Voice Agents)
  slug: atoms-voice-agents
- description: Realtime streaming speech synthesis.
  name: Smallest AI Streaming API
  slug: smallest-ai-streaming-api
- description: Synthesize speech from text.
  name: Smallest AI Text to Speech API
  slug: smallest-ai-text-to-speech-api
- description: List prebuilt voices and manage cloned voices.
  name: Smallest AI Voices API
  slug: smallest-ai-voices-api
artifact_total: 19
asyncapis:
- description: Realtime, bidirectional text-to-speech over WebSocket for the Smallest AI Waves Lightning v2 model. The client opens a WebSocket connection, sends one or more JSON text payloads, and the server stream
  name: Smallest AI Waves Realtime TTS (WebSocket)
  slug: smallest-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smallest AI Waves Streaming API
  slug: open-smallest-ai-streaming-api
- collection_type: open
  name: Smallest AI Waves Streaming Text to Speech API
  slug: open-smallest-ai-text-to-speech-api
- collection_type: open
  name: Smallest AI Waves Streaming Voices API
  slug: open-smallest-ai-voices-api
- collection_type: open
  name: Smallest AI Waves API
  slug: open-smallest-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smallest-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/smallest-ai-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smallest-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smallest-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smallest-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smallest-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smallest
- group: company
  title: ''
  type: Website
  url: https://smallest.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.smallest.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/smallest-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smallest-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smallest-ai-finops.yml
created: '2026-06-21'
description: Smallest AI builds ultra-low-latency voice infrastructure - the Waves text-to-speech engine (Lightning / Lightning v2 models) for realtime speech synthesis and instant voice cloning, plus the Atoms platform for building and deploying production voice agents. The Waves REST API at https://waves-api.smallest.ai/api/v1 generates speech with sub-100ms latency, supports SSE and WebSocket streaming, and exposes voice listing and cloning via a Bearer-authenticated interface.
finops:
- name: Smallest Ai Finops
  service_category: AI and Machine Learning
  slug: smallest-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smallest-ai.png
layout: provider
modified: '2026-06-21'
name: Smallest AI
nav: Providers
network: true
overview: 'Smallest AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Streaming API, Text to Speech API, and Voices API. Tagged areas include Artificial Intelligence, Text-to-Speech, Voice, Real-Time, and Voice Agents.


  The Smallest AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Smallest AI''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Smallest Ai Plans Pricing
  plan_count: 4
  slug: smallest-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 3
  name: Smallest Ai Rate Limits
  slug: smallest-ai-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Smallest AI API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: smallest-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 44.0
  coverage:
    artifact_dirs: 11
    catalog_gap: 47.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 11.4
    contract_quality: 64.6
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smallest-ai/refs/heads/main/screenshots/smallest-ai-2026-08-17T081930.png
security:
- kind: authentication
  name: Smallest Ai Authentication
  slug: smallest-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smallest Ai Domain Security
  slug: smallest-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Smallest Ai Vulnerability Disclosure
  slug: smallest-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Smallest Ai Trust Center
  slug: smallest-ai-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: smallest-ai
tags:
- Artificial Intelligence
- Text-to-Speech
- Voice
- Real-Time
- Voice Agents
website: https://smallest.ai/
---
