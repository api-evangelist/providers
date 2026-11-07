---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
  band: agent-ready
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
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
artifact_total: 12
collections:
- collection_type: open
  name: OpenAPI Plant Store Plants API
  slug: open-rime-ai-plants-api
- collection_type: open
  name: OpenAPI Plant Store
  slug: open-rime-ai
common:
- group: agent
  href: https://artifacts.apis.io/rime-ai/agentic-access/rime-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rime-ai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/rime-ai/security/rime-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rime-ai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/rime-ai/authentication/rime-ai-authentication.yml
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
  href: https://artifacts.apis.io/rime-ai/plans/rime-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rime-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/rime-ai/rate-limits/rime-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rime-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rime-ai/finops/rime-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/rime-ai-finops.yml
created: '2026-05-08'
description: Rime is a realtime text-to-speech platform optimized for low-latency conversational agents. Models include Arcana v3, Arcana v2, Mist v3, and Mist v2. The TTS API supports streaming HTTP, WebSocket (binary and JSON), Server-Sent Events, and JSON envelopes for MP3, mu-law, OGG, and WAV audio.
finops:
- has_sources: true
  method: generated
  name: Rime Ai Finops
  primary_unit: ''
  service_category: AI
  slug: rime-ai-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rime-ai.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.rime.ai over HTTP; 6 tools listed.
  name: Rime MCP Server
  slug: rime-ai
modified: '2026-05-08'
name: Rime
nav: Providers
network: true
overview: 'Rime publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Plants API, and 1 more. Tagged areas include Artificial Intelligence, Voice, Text-to-Speech, Real-Time, and Conversational AI.


  The Rime catalog on APIs.io includes 1 Spectral governance ruleset.


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
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Rime API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: rime-ai-rules
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 13.6
    contract_quality: 12.4
    developer_ergonomics: 23.8
    discoverability: 75.0
    operational_transparency: 7.9
  previous_composite: 19.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rime-ai/rime-ai-2026-06-20T193201.png
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
- Text-to-Speech
- Real-Time
- Conversational AI
website: https://rime.ai/
---
