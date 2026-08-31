---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: B2B HTTP API for generating royalty-free AI music at scale, supporting per-end-user music creation with style, mood, genre, length, and instrument customization. Generated tracks are cleared for perpe
  name: SOUNDRAW API
  slug: music-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soundraw-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soundraw.io/
- group: other
  title: ''
  type: ProductPage
  url: https://soundraw.io/api
- group: start
  title: ''
  type: FreeTrial
  url: https://soundraw.io/generate_music
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soundraw.io/terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soundraw.io/privacy_policy
- group: operate
  title: ''
  type: Contact
  url: https://soundraw.io/contact
created: '2026-05-23'
description: SOUNDRAW is an AI music generation platform that produces royalty-free, copyright-cleared music customized by genre, mood, theme, length, and instrumentation. Beyond the soundraw.io consumer product, SOUNDRAW offers a B2B API for embedding music generation into video platforms, games, social tools, and ad tech, with Canva, Filmora, and Captions Mirage cited as integration partners.
finops:
- name: Soundraw Finops
  service_category: API
  slug: soundraw-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soundraw.png
integrations:
- description: SOUNDRAW music generation embedded within the Canva creative suite.
  name: Canva
- description: AI music generation inside the Wondershare Filmora video editor.
  name: Filmora
- description: AI music for Captions' Mirage AI video tooling.
  name: Captions Mirage
layout: provider
modified: '2026-05-23'
name: SOUNDRAW
nav: Providers
network: true
overview: SOUNDRAW publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Music, Generative, Royalty-Free, B2B, and Music Generation.
plans:
- name: Soundraw Plans Pricing
  plan_count: 1
  slug: soundraw-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Soundraw Rate Limits
  slug: soundraw-rate-limits
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 17.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soundraw/refs/heads/main/screenshots/soundraw-2026-06-20T194220.png
security:
- kind: domain-security
  name: Soundraw Domain Security
  slug: soundraw-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soundraw
tags:
- AI Music
- Generative
- Royalty-Free
- B2B
- Music Generation
- Customization
- Video
- Games
website: https://soundraw.io/
---
