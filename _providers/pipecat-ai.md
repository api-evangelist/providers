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
    asyncapi_events: false
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Pipecat Ai Agentic Access
  operation_count: 24
  slug: pipecat-ai-agentic-access
  summary_line: 24 operations · 11 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Open-source (BSD 2-Clause) Python framework whose interface is the pipecat-ai library, not a REST API. Applications wire FrameProcessors into a Pipeline, where Frames carry audio, text, images, and co
  name: Pipecat Framework (Python SDK)
  slug: pipecat-framework-python-sdk
- description: Realtime media transport layer of the framework. Bidirectional audio, video, and data flow over Daily WebRTC, SmallWebRTC, LiveKit, FastAPI WebSocket server, and telephony serializers (Twilio, Telnyx,
  name: Transports (WebRTC/WebSocket)
  slug: transports-webrtc-websocket
- description: Create, list, update, and delete deployed agents and inspect logs and sessions.
  name: Pipecat Agents API
  slug: pipecat-ai-agents-api
- description: Build container images for agent deployments.
  name: Pipecat Builds API
  slug: pipecat-ai-builds-api
- description: Organization properties and available regions.
  name: Pipecat Organization API
  slug: pipecat-ai-organization-api
- description: Manage secret sets and individual secrets used by agents.
  name: Pipecat Secrets API
  slug: pipecat-ai-secrets-api
- description: Start, stop, and proxy requests to running agent sessions.
  name: Pipecat Sessions API
  slug: pipecat-ai-sessions-api
artifact_total: 14
collections:
- collection_type: open
  name: Pipecat Cloud API
  slug: open-pipecat-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pipecat-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pipecat-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pipecat-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pipecat-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/daily-co
- group: company
  title: ''
  type: Website
  url: https://www.pipecat.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pipecat.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/pipecat-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pipecat-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pipecat-ai-finops.yml
created: '2026-06-21'
description: Pipecat is an open-source Python framework (created by Daily) for building realtime voice and multimodal AI agents. It orchestrates pipelines of frames through pluggable services (STT, LLM, TTS, vision) and transports (Daily WebRTC, WebSocket, SmallWebRTC, telephony). Pipecat Cloud adds a hosted platform with a REST control API for deploying agents and starting/stopping agent sessions at scale.
finops:
- name: Pipecat Ai Finops
  service_category: AI and Machine Learning
  slug: pipecat-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pipecat-ai.png
layout: provider
modified: '2026-06-21'
name: Pipecat
nav: Providers
network: true
overview: 'Pipecat publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Builds API, Organization API, and 2 more. Tagged areas include AI, Voice, Multimodal, Agents, and Realtime.


  Pipecat''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Pipecat Ai Plans Pricing
  plan_count: 3
  slug: pipecat-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Pipecat Ai Rate Limits
  slug: pipecat-ai-rate-limits
score:
  band: thin
  composite: 33.9
  delta: -5.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.7
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
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
  name: Pipecat Ai Authentication
  slug: pipecat-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Pipecat Ai Domain Security
  slug: pipecat-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pipecat-ai
tags:
- AI
- Voice
- Multimodal
- Agents
- Realtime
- Framework
website: https://www.pipecat.ai
---
