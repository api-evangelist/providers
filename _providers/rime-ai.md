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
    error_semantics: verified
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
  score: 25.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Rime Ai Agentic Access
  operation_count: 3
  slug: rime-ai-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Realtime text-to-speech API supporting streaming HTTP, WebSocket, and SSE delivery for Arcana and Mist models. Authentication via API key. Audio formats include MP3, mu-law, OGG, and WAV. List voice a
  name: Rime TTS API
  slug: tts
- baseURL: https://users.rime.ai
  baseurl_source: declared
  description: The Plants API from Rime — 2 operation(s) for plants.
  name: Rime Plants API
  slug: rime-ai-plants-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenAPI Plant Store Plants API
  slug: open-rime-ai-plants-api
- collection_type: open
  name: OpenAPI Plant Store
  slug: open-rime-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rime-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rime-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rime-ai-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://rime.ai/resources/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rime-ai
- group: company
  title: ''
  type: Website
  url: https://rime.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rime.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/rime-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rime-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rime-ai-finops.yml
created: '2026-05-08'
description: Rime is a realtime text-to-speech platform optimized for low-latency conversational agents. Models include Arcana v3, Arcana v2, Mist v3, and Mist v2. The TTS API supports streaming HTTP, WebSocket (binary and JSON), Server-Sent Events, and JSON envelopes for MP3, mu-law, OGG, and WAV audio.
finops:
- name: Rime Ai Finops
  service_category: AI
  slug: rime-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rime-ai.png
layout: provider
modified: '2026-05-08'
name: Rime
nav: Providers
network: true
overview: 'Rime publishes 1 API on the [APIs.io](https://apis.io/) network: Plants API. Tagged areas include Artificial Intelligence, Voice, TTS, Real-Time, and Conversational.


  Rime''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Rime Ai Plans Pricing
  plan_count: 4
  slug: rime-ai-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Rime Ai Rate Limits
  slug: rime-ai-rate-limits
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 11
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 42.9
    developer_ergonomics: 23.8
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rime-ai/refs/heads/main/screenshots/rime-ai-2026-06-20T193201.png
security:
- kind: authentication
  name: Rime Ai Authentication
  slug: rime-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rime Ai Domain Security
  slug: rime-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rime-ai
tags:
- Artificial Intelligence
- Voice
- TTS
- Real-Time
- Conversational
website: https://rime.ai/
---
