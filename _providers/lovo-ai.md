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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lovo Ai Agentic Access
  operation_count: 5
  slug: lovo-ai-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: Retrieve the catalog of speakers/voices and their styles.
  name: LOVO AI Speakers API
  slug: lovo-ai-speakers-api
- description: Read team billing and usage information for the API key's account.
  name: LOVO AI Teams API
  slug: lovo-ai-teams-api
- description: Convert text to speech synchronously or asynchronously and retrieve job results.
  name: LOVO AI Text-to-Speech API
  slug: lovo-ai-text-to-speech-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LOVO AI Genny Speakers API
  slug: open-lovo-ai-speakers-api
- collection_type: open
  name: LOVO AI Genny Speakers Teams API
  slug: open-lovo-ai-teams-api
- collection_type: open
  name: LOVO AI Genny Speakers Text-to-Speech API
  slug: open-lovo-ai-text-to-speech-api
- collection_type: open
  name: LOVO AI Genny API
  slug: open-lovo-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lovo-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lovo-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lovo-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lovo-ai
- group: company
  title: ''
  type: Website
  url: https://lovo.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.genny.lovo.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/lovo-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/lovo-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/lovo-ai-finops.yml
created: '2026-07-11'
description: LOVO AI is an AI text-to-speech and voice generation platform whose flagship product, Genny, turns text into natural-sounding speech across a large library of speakers, locales, and speaker styles, plus AI voice cloning and voiceover tooling. The Genny API is a REST API (base https://api.genny.lovo.ai) authenticated with an X-API-KEY header. It exposes synchronous and asynchronous text-to-speech conversions, a speakers/voices catalog with styles, per-conversion pronunciation, pause, and emphasis controls, and a team billing/usage endpoint. TTS credits are deducted from the account tied to the API key, and generated audio URLs are valid for 24 hours.
finops:
- name: Lovo Ai Finops
  service_category: AI and Machine Learning
  slug: lovo-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lovo-ai.png
layout: provider
modified: '2026-07-11'
name: LOVO AI
nav: Providers
network: true
overview: 'LOVO AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Speakers API, Teams API, and Text-to-Speech API. Tagged areas include Artificial Intelligence, Text to Speech, TTS, Voice Generation, and Voice Cloning.


  LOVO AI''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Lovo Ai Plans Pricing
  plan_count: 5
  slug: lovo-ai-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Lovo Ai Rate Limits
  slug: lovo-ai-rate-limits
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 25.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lovo-ai/refs/heads/main/screenshots/lovo-ai-2026-07-25T225613.png
security:
- kind: authentication
  name: Lovo Ai Authentication
  slug: lovo-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lovo Ai Domain Security
  slug: lovo-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lovo-ai
tags:
- Artificial Intelligence
- Text to Speech
- TTS
- Voice Generation
- Voice Cloning
- Speech Synthesis
- Voiceover
website: https://lovo.ai
---
