---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 1
  name: Pipecat Ai Agentic Access
  operation_count: 24
  slug: pipecat-ai-agentic-access
  summary_line: 24 operations · 11 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Open-source (BSD 2-Clause) Python framework whose interface is the pipecat-ai library, not a REST API. Applications wire FrameProcessors into a Pipeline, where Frames carry audio, text, images, and co
  name: Pipecat Framework (Python SDK)
  slug: pipecat-framework-python-sdk
- description: Realtime media transport layer of the framework. Bidirectional audio, video, and data flow over Daily WebRTC, SmallWebRTC, LiveKit, FastAPI WebSocket server, and telephony serializers (Twilio, Telnyx,
  name: Transports (WebRTC/WebSocket)
  slug: transports-webrtc-websocket
- baseURL: https://api.pipecat.daily.co/v1
  baseurl_source: declared
  description: Create, list, update, and delete deployed agents and inspect logs and sessions.
  name: Pipecat Agents API
  slug: pipecat-ai-agents-api
- baseURL: https://api.pipecat.daily.co/v1
  baseurl_source: declared
  description: Build container images for agent deployments.
  name: Pipecat Builds API
  slug: pipecat-ai-builds-api
- baseURL: https://api.pipecat.daily.co/v1
  baseurl_source: declared
  description: Organization properties and available regions.
  name: Pipecat Organization API
  slug: pipecat-ai-organization-api
- baseURL: https://api.pipecat.daily.co/v1
  baseurl_source: declared
  description: Manage secret sets and individual secrets used by agents.
  name: Pipecat Secrets API
  slug: pipecat-ai-secrets-api
- baseURL: https://api.pipecat.daily.co/v1
  baseurl_source: declared
  description: Start, stop, and proxy requests to running agent sessions.
  name: Pipecat Sessions API
  slug: pipecat-ai-sessions-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pipecat Cloud Agents API
  slug: open-pipecat-ai-agents-api
- collection_type: open
  name: Pipecat Cloud Agents Builds API
  slug: open-pipecat-ai-builds-api
- collection_type: open
  name: Pipecat Cloud Agents Organization API
  slug: open-pipecat-ai-organization-api
- collection_type: open
  name: Pipecat Cloud Agents Secrets API
  slug: open-pipecat-ai-secrets-api
- collection_type: open
  name: Pipecat Cloud Agents Sessions API
  slug: open-pipecat-ai-sessions-api
- collection_type: open
  name: Pipecat Cloud API
  slug: open-pipecat-ai
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/pipecat-ai-capability-edges.yml
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
overview: 'Pipecat publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Builds API, Organization API, and 2 more. Tagged areas include Artificial Intelligence, Voice, Multi-Modal, Agents, and Real-Time.


  Pipecat''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Pipecat Ai Plans Pricing
  plan_count: 3
  slug: pipecat-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Pipecat Ai Rate Limits
  slug: pipecat-ai-rate-limits
score:
  band: thin
  composite: 37.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pipecat-ai/refs/heads/main/screenshots/pipecat-ai-2026-09-02T151314.png
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
- Artificial Intelligence
- Voice
- Multi-Modal
- Agents
- Real-Time
- Framework
website: https://www.pipecat.ai
---
