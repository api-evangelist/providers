---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Retell Agentic Access
  operation_count: 35
  slug: retell-agentic-access
  summary_line: 35 operations · 21 acting
api_count: 11
apis:
- description: The Agent API from Retell AI — 5 operation(s) for agent.
  name: Retell AI Agent API
  slug: retell-agent-api
- description: The Batch Call API from Retell AI — 1 operation(s) for batch call.
  name: Retell AI Batch Call API
  slug: retell-batch-call-api
- description: The Call API from Retell AI — 2 operation(s) for call.
  name: Retell AI Call API
  slug: retell-call-api
- description: The Concurrency API from Retell AI — 1 operation(s) for concurrency.
  name: Retell AI Concurrency API
  slug: retell-concurrency-api
- description: The Conversation Flow API from Retell AI — 5 operation(s) for conversation flow.
  name: Retell AI Conversation Flow API
  slug: retell-conversation-flow-api
- description: The Knowledge Base API from Retell AI — 6 operation(s) for knowledge base.
  name: Retell AI Knowledge Base API
  slug: retell-knowledge-base-api
- description: The Phone Call API from Retell AI — 1 operation(s) for phone call.
  name: Retell AI Phone Call API
  slug: retell-phone-call-api
- description: The Phone Number API from Retell AI — 6 operation(s) for phone number.
  name: Retell AI Phone Number API
  slug: retell-phone-number-api
- description: The Retell LLM API from Retell AI — 5 operation(s) for retell llm.
  name: Retell AI Retell LLM API
  slug: retell-retell-llm-api
- description: The Voice API from Retell AI — 2 operation(s) for voice.
  name: Retell AI Voice API
  slug: retell-voice-api
- description: The Web Call API from Retell AI — 1 operation(s) for web call.
  name: Retell AI Web Call API
  slug: retell-web-call-api
artifact_total: 20
asyncapis:
- description: AsyncAPI 2.6 description of Retell AI's real-time **Custom LLM WebSocket** surface, documented at https://docs.retellai.com/api-references/llm-websocket. Unlike a one-way HTTP stream, this is a true b
  name: Retell AI Custom LLM WebSocket
  slug: retell-asyncapi
collections:
- collection_type: open
  name: Retell AI API
  slug: open-retell
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/retell-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/retell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/retell-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RetellAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/retell-ai
- group: company
  title: ''
  type: Website
  url: https://www.retellai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.retellai.com
- group: commercial
  title: ''
  type: Plans
  url: plans/retell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/retell-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/retell-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.retellai.com/blog
created: '2026-07-01'
description: Retell AI is a platform to build, test, and deploy AI voice agents for phone calls. Its conversational voice API orchestrates LLM responses, telephony, speech, and call analysis so developers can place and receive natural-sounding automated calls, with a real-time WebSocket for bringing your own custom LLM and streaming call audio.
finops:
- name: Retell Finops
  service_category: AI and Machine Learning
  slug: retell-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/retell.png
layout: provider
modified: '2026-07-01'
name: Retell AI
nav: Providers
network: true
overview: 'Retell AI publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Agent API, Batch Call API, Call API, and 8 more. Tagged areas include AI, Voice, Voice Agents, Conversational AI, and Telephony.


  The Retell AI catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Retell AI''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Retell Plans Pricing
  plan_count: 3
  slug: retell-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Retell Rate Limits
  slug: retell-rate-limits
rules:
- name: Retell AI API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: retell-asyncapi-spectral-rules
score:
  band: thin
  composite: 41.2
  delta: -8.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Retell Authentication
  slug: retell-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Retell Domain Security
  slug: retell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: retell
tags:
- AI
- Voice
- Voice Agents
- Conversational AI
- Telephony
website: https://www.retellai.com/
---
