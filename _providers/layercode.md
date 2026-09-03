---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Layercode Agentic Access
  operation_count: 8
  slug: layercode-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- baseURL: wss://api.layercode.com/v1/agents/web/websocket
  baseurl_source: declared
  description: Bidirectional realtime WebSocket transport that streams base64 PCM microphone audio from the browser to Layercode and streams synthesized speech, transcripts, and structured data back, authorized with
  name: Layercode Realtime Voice API
  slug: layercode-realtime-voice-api
- baseURL: https://docs.layercode.com/api-reference/webhook-sse-api
  baseurl_source: declared
  description: 'HMAC-signed webhook Layercode POSTs to your backend with session and transcript events (session.start, message, data, session.update, session.end); your backend streams response.tts / response.data / '
  name: Layercode Webhooks API
  slug: layercode-webhooks-api
- baseURL: https://api.layercode.com/v1
  baseurl_source: declared
  description: The Agents API from Layercode — 2 operation(s) for agents.
  name: Layercode Agents API
  slug: layercode-agents-api
- baseURL: https://api.layercode.com/v1
  baseurl_source: declared
  description: The Calls API from Layercode — 1 operation(s) for calls.
  name: Layercode Calls API
  slug: layercode-calls-api
- baseURL: https://api.layercode.com/v1
  baseurl_source: declared
  description: The Sessions API from Layercode — 3 operation(s) for sessions.
  name: Layercode Sessions API
  slug: layercode-sessions-api
artifact_total: 18
asyncapis:
- description: AsyncAPI 2.6 description of Layercode's **realtime voice transport**, a genuine bidirectional WebSocket documented at https://docs.layercode.com/api-reference/frontend-ws-api. Unlike one-way HTTP SSE,
  name: Layercode Realtime Voice WebSocket API
  slug: layercode-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Layercode REST Agents API
  slug: open-layercode-agents-api
- collection_type: open
  name: Layercode REST Agents Calls API
  slug: open-layercode-calls-api
- collection_type: open
  name: Layercode REST Agents Sessions API
  slug: open-layercode-sessions-api
- collection_type: open
  name: Layercode REST API
  slug: open-layercode
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/layercode-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/layercode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/layercode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/layercodedev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/layercode
- group: company
  title: ''
  type: Website
  url: https://layercode.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.layercode.com
- group: commercial
  title: ''
  type: Plans
  url: plans/layercode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/layercode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/layercode-finops.yml
created: '2026-06-21'
description: Layercode provides voice-AI agent infrastructure - low-latency voice pipelines that turn any LLM or text-based agent into a conversational voice agent for web, mobile, and phone. A REST API manages agents, sessions, and outbound calls, while a realtime WebSocket transport streams audio to the browser and a signed webhook delivers transcripts to your backend, which streams text-to-speech responses back over Server-Sent Events.
finops:
- name: Layercode Finops
  service_category: AI and Machine Learning
  slug: layercode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/layercode.png
layout: provider
modified: '2026-06-21'
name: Layercode
nav: Providers
network: true
overview: 'Layercode publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Realtime Voice API, Webhooks API, Agents API, and 2 more. Tagged areas include Artificial Intelligence, Voice, Voice Agents, Real-Time, and Low Latency.


  The Layercode catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Layercode''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Layercode Plans Pricing
  plan_count: 1
  slug: layercode-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Layercode Rate Limits
  slug: layercode-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Layercode API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: layercode-asyncapi-spectral-rules
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 11.4
    contract_quality: 54.8
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 11.4
    operational_transparency: 34.2
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/layercode/refs/heads/main/screenshots/layercode-2026-07-25T224657.png
security:
- kind: authentication
  name: Layercode Authentication
  slug: layercode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Layercode Domain Security
  slug: layercode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: layercode
tags:
- Artificial Intelligence
- Voice
- Voice Agents
- Real-Time
- Low Latency
website: https://layercode.com
---
