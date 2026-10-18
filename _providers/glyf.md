---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.styleframe.ai/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/glyf/refs/heads/main/plans/glyf-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/glyf-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://www.styleframe.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.styleframe.ai/blog/rss.xml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/glyf/refs/heads/main/security/glyf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/glyf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.styleframe.ai/
- group: start
  title: ''
  type: SignUp
  url: https://www.styleframe.ai/signin
- group: operate
  title: ''
  type: Support
  url: https://www.styleframe.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.styleframe.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.styleframe.ai/terms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/glyfspace
created: '2026-07-17'
description: Glyf is an AI-powered creative tool for motion designers, studios, and creative teams, backed by Andreessen Horowitz (a16z Speedrun). It transforms 2D animations into stylized 3D with custom textures and effects, enhances live-action footage, and lets creators train bespoke AI models to match their own artistic direction, with exports into After Effects, Nuke, and other compositing pipelines. The product has since been rebranded and now ships as StyleFrame (www.styleframe.ai), a timeline-based, keyframe-driven video-generation platform where creators place keyframes and prompt tracks to control every frame of an animation. As of this enrichment pass, Glyf/StyleFrame is a consumer-facing creative application with no public API, developer documentation, OpenAPI definition, SDK, or machine-readable discovery surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glyf.png
layout: provider
modified: '2026-10-06'
name: Glyf
nav: Providers
network: true
overview: 'Glyf is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Creative Tools, Motion Design, and Video Generation.


  Glyf''s developer surface includes pricing, engineering blog, signup flow, support, and 7 more developer resources.'
plans:
- name: Glyf Plans Pricing
  plan_count: 8
  slug: glyf-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 8.5
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 12.2
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 12.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/glyf/refs/heads/main/screenshots/glyf-2026-07-25T215940.png
security:
- kind: domain-security
  name: Glyf Domain Security
  slug: glyf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: glyf
tags:
- Company
- Artificial Intelligence
- Creative Tools
- Motion Design
- Video Generation
- Generative AI
- Design
website: https://www.styleframe.ai/
---
