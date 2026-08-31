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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Speechify Agentic Access
  operation_count: 5
  slug: speechify-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- description: The Audio API from Speechify — 2 operation(s) for audio.
  name: Speechify Audio API
  slug: speechify-audio-api
- description: The Voices API from Speechify — 2 operation(s) for voices.
  name: Speechify Voices API
  slug: speechify-voices-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Speechify Voice Audio API
  slug: open-speechify-audio-api
- collection_type: open
  name: Speechify Voice Audio Voices API
  slug: open-speechify-voices-api
- collection_type: open
  name: Speechify Voice API
  slug: open-speechify
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/speechify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speechify-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/speechify-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpeechifyInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/speechify
- group: company
  title: ''
  type: Website
  url: https://speechify.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sws.speechify.com
- group: commercial
  title: ''
  type: Plans
  url: plans/speechify-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/speechify-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/speechify-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://speechify.com/blog
created: '2026-06-21'
description: Speechify is a text-to-speech platform whose Speechify Voice API (also surfaced through Speechify Studio) synthesizes lifelike speech in 30+ languages from plain text or SSML. The REST API at https://api.sws.speechify.com offers non-streaming and streaming text-to-speech, a voice catalog, and instant voice cloning, authenticated with a Bearer API key.
finops:
- name: Speechify Finops
  service_category: AI and Machine Learning
  slug: speechify-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/speechify.png
layout: provider
modified: '2026-06-21'
name: Speechify
nav: Providers
network: true
overview: 'Speechify publishes 2 APIs on the [APIs.io](https://apis.io/) network: Audio API and Voices API. Tagged areas include Artificial Intelligence, Text to Speech, Voice, Speech Synthesis, and Voice Cloning.


  Speechify''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Speechify Plans Pricing
  plan_count: 3
  slug: speechify-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 4
  name: Speechify Rate Limits
  slug: speechify-rate-limits
score:
  band: thin
  composite: 39.1
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
    contract_quality: 56.8
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Speechify Authentication
  slug: speechify-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Speechify Domain Security
  slug: speechify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: speechify
tags:
- Artificial Intelligence
- Text to Speech
- Voice
- Speech Synthesis
- Voice Cloning
website: https://speechify.com
---
