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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Vocode Agentic Access
  operation_count: 28
  slug: vocode-agentic-access
  summary_line: 28 operations · 14 acting
api_count: 1
apis:
- description: Real-time, bidirectional streaming conversation pipeline (StreamingConversation) in the open-source library that wires transcription, agent response, and synthesis together; the hosted platform consum
  name: Vocode Realtime Streaming Conversation
  slug: vocode-realtime-streaming
- description: 'vocode-core, the MIT-licensed Python library for building voice-based LLM agents with pluggable STT, LLM, and TTS providers and Twilio/Vonage telephony, self-hosted and free, distinct from the hosted '
  name: Vocode Open Source Library
  slug: vocode-oss-library
- baseURL: https://api.vocode.dev/v1
  baseurl_source: declared
  description: The Actions API from Vocode — 4 operation(s) for actions.
  name: Vocode Actions API
  slug: vocode-actions-api
- baseURL: https://api.vocode.dev/v1
  baseurl_source: declared
  description: The Agents API from Vocode — 4 operation(s) for agents.
  name: Vocode Agents API
  slug: vocode-agents-api
- baseURL: https://api.vocode.dev/v1
  baseurl_source: declared
  description: The Calls API from Vocode — 5 operation(s) for calls.
  name: Vocode Calls API
  slug: vocode-calls-api
- baseURL: https://api.vocode.dev/v1
  baseurl_source: declared
  description: The Numbers API from Vocode — 6 operation(s) for numbers.
  name: Vocode Numbers API
  slug: vocode-numbers-api
- baseURL: https://api.vocode.dev/v1
  baseurl_source: declared
  description: The Usage API from Vocode — 1 operation(s) for usage.
  name: Vocode Usage API
  slug: vocode-usage-api
- baseURL: https://api.vocode.dev/v1
  baseurl_source: declared
  description: The Voices API from Vocode — 4 operation(s) for voices.
  name: Vocode Voices API
  slug: vocode-voices-api
- baseURL: https://api.vocode.dev/v1
  baseurl_source: declared
  description: The Webhooks API from Vocode — 4 operation(s) for webhooks.
  name: Vocode Webhooks API
  slug: vocode-webhooks-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vocode Hosted Actions API
  slug: open-vocode-actions-api
- collection_type: open
  name: Vocode Hosted Actions Agents API
  slug: open-vocode-agents-api
- collection_type: open
  name: Vocode Hosted Actions Calls API
  slug: open-vocode-calls-api
- collection_type: open
  name: Vocode Hosted Actions Numbers API
  slug: open-vocode-numbers-api
- collection_type: open
  name: Vocode Hosted Actions Usage API
  slug: open-vocode-usage-api
- collection_type: open
  name: Vocode Hosted Actions Voices API
  slug: open-vocode-voices-api
- collection_type: open
  name: Vocode Hosted Actions Webhooks API
  slug: open-vocode-webhooks-api
- collection_type: open
  name: Vocode Hosted API
  slug: open-vocode
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vocode-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vocode-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vocode-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vocodedev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vocode
- group: company
  title: ''
  type: Website
  url: https://www.vocode.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vocode.dev
- group: commercial
  title: ''
  type: Plans
  url: plans/vocode-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vocode-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vocode-finops.yml
created: '2026-06-21'
description: Vocode is an open-source Python library (vocode-core, MIT licensed) for building real-time, streaming voice AI agents that run over phone calls, plus a hosted REST API at https://api.vocode.dev/v1 (Bearer API key) for placing and managing outbound and inbound phone calls, configuring agents, voices, prompts, actions, phone numbers, and webhooks without operating the streaming infrastructure yourself.
finops:
- name: Vocode Finops
  service_category: AI and Machine Learning
  slug: vocode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vocode.png
layout: provider
modified: '2026-06-21'
name: Vocode
nav: Providers
network: true
overview: 'Vocode publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Agents API, Calls API, and 4 more. Tagged areas include Voice AI, Voice Agents, Telephony, Conversational AI, and Phone Calls.


  Vocode''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Vocode Plans Pricing
  plan_count: 4
  slug: vocode-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Vocode Rate Limits
  slug: vocode-rate-limits
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 50.8
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 38.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vocode/refs/heads/main/screenshots/vocode-2026-09-02T170205.png
security:
- kind: authentication
  name: Vocode Authentication
  slug: vocode-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vocode Domain Security
  slug: vocode-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vocode
tags:
- Voice AI
- Voice Agents
- Telephony
- Conversational AI
- Phone Calls
website: https://www.vocode.dev
---
