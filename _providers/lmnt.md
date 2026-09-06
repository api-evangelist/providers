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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Lmnt Agentic Access
  operation_count: 14
  slug: lmnt-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- description: WebSocket-based real-time speech generation API for streaming LLM text output to synthesized audio with reset-latency support for conversational AI applications requiring interrupt handling.
  name: LMNT Speech Sessions API
  slug: lmnt-speech-sessions-api
- baseURL: https://api.lmnt.com
  baseurl_source: declared
  description: The Ai API from LMNT — 8 operation(s) for ai.
  name: LMNT Ai API
  slug: lmnt-ai-api
- baseURL: https://api.lmnt.com
  baseurl_source: declared
  description: The Health Check API from LMNT — 1 operation(s) for health check.
  name: LMNT Health Check API
  slug: lmnt-health-check-api
- baseURL: https://api.lmnt.com
  baseurl_source: declared
  description: The Speech API from LMNT — 2 operation(s) for speech.
  name: LMNT Speech API
  slug: lmnt-speech-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LMNT Speech Ai API
  slug: open-lmnt-ai-api
- collection_type: open
  name: LMNT Speech Ai Health Check API
  slug: open-lmnt-health-check-api
- collection_type: open
  name: LMNT Ai Speech API
  slug: open-lmnt-speech-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lmnt-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lmnt-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lmnt-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lmnt-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lmnt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lmnt.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lmnt-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lmnt
- group: other
  title: ''
  type: X
  url: https://x.com/lmnt_com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lmnt.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lmnt.com/changelog/overview
- group: commercial
  title: ''
  type: Plans
  url: plans/lmnt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lmnt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lmnt-finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/lmnt-speech-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lmnt-voice-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/lmnt-speech-synthesis-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/lmnt-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/lmnt-vocabulary.yml
created: 2026-06-12
description: LMNT is a text-to-speech API platform delivering ultra-low latency voice synthesis with streaming audio output designed for real-time conversational AI applications. The platform provides a Speech API for standard text-to-speech generation and a Speech Sessions API for WebSocket-based real-time streaming integrated with LLM pipelines, achieving latency under 300 milliseconds. LMNT supports 31 languages and offers voice cloning from as little as five seconds of audio, with its Blizzard 2 model optimized for accuracy, expressiveness, and pronunciation. Authentication uses API keys managed via the app dashboard, with SDKs available for Python, TypeScript, and Go.
examples:
- key_count: 7
  name: Lmnt Speech Synthesis Request
  slug: lmnt-speech-synthesis-request
- key_count: 1
  name: Lmnt Voice List Response
  slug: lmnt-voice-list-response
finops:
- name: Lmnt Finops
  service_category: ''
  slug: lmnt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lmnt.png
json_schemas:
- name: LMNT Speech Synthesis Request
  property_count: 11
  slug: lmnt-speech-synthesis
- name: LMNT Voice
  property_count: 10
  slug: lmnt-voice
jsonld:
- class_count: 0
  name: Lmnt Context
  property_count: 24
  slug: lmnt-context
layout: provider
modified: 2026-06-12
name: LMNT
nav: Providers
network: true
overview: 'LMNT publishes 3 APIs on the [APIs.io](https://apis.io/) network: Ai API, Health Check API, and Speech API. Tagged areas include Text-to-Speech, Voice Synthesis, Voice Cloning, Audio Streaming, and Conversational AI.


  The LMNT catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LMNT''s developer surface includes authentication, documentation, pricing, changelog, and 15 more developer resources.'
plans:
- name: Lmnt Plans Pricing
  plan_count: 5
  slug: lmnt-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Lmnt Rate Limits
  slug: lmnt-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: LMNT API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lmnt-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 76.3
    catalog_earned_first_party: 0.0
    catalog_gap: 38.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 25.0
    contract_quality: 58.6
    developer_ergonomics: 21.4
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 39.5
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lmnt/refs/heads/main/screenshots/lmnt-2026-06-20T184626.png
security:
- kind: authentication
  name: Lmnt Authentication
  slug: lmnt-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lmnt Domain Security
  slug: lmnt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Lmnt Trust Center
  slug: lmnt-trust-center
  summary_line: SOC 2
slug: lmnt
tags:
- Text-to-Speech
- Voice Synthesis
- Voice Cloning
- Audio Streaming
- Conversational AI
- Low Latency
- Real-Time Audio
website: https://www.lmnt.com/
---
