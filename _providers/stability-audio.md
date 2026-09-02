---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: REST API for generating music and SFX clips with Stable Audio 2.5. Hosted on the Stability Developer Platform at https://api.stability.ai. Authentication via API key; credit-based billing.
  name: Stable Audio API
  slug: stable-audio
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stability-audio-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Stability-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stability-ai
- group: company
  title: ''
  type: Website
  url: https://stability.ai/stable-audio
- group: docs
  title: ''
  type: Documentation
  url: https://platform.stability.ai/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/stability-audio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stability-audio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stability-audio-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://stability.ai/news-updates
created: '2026-05-08'
description: Stable Audio (by Stability AI) is a generative audio model for music and sound-effect generation. The Stability Developer Platform exposes Stable Audio 2.5 endpoints alongside image, video, and 3D generation. Pricing is credit-based at 1 credit = $0.01; Stable Audio 2.5 generations are reported at $0.20 per generation regardless of duration.
finops:
- name: Stability Audio Finops
  service_category: AI
  slug: stability-audio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stability-audio.png
layout: provider
modified: '2026-05-08'
name: Stability Audio
nav: Providers
network: true
overview: 'Stability Audio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Audio, Music Generation, SFX, and Stability.


  Stability Audio''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Stability Audio Plans Pricing
  plan_count: 3
  slug: stability-audio-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Stability Audio Rate Limits
  slug: stability-audio-rate-limits
score:
  band: emerging
  composite: 14.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 14.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stability-audio/refs/heads/main/screenshots/stability-audio-2026-06-20T194441.png
security:
- kind: domain-security
  name: Stability Audio Domain Security
  slug: stability-audio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: stability-audio
tags:
- Artificial Intelligence
- Audio
- Music Generation
- SFX
- Stability
website: https://stability.ai/stable-audio
---
