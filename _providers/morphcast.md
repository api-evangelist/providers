---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: 'We expertly craft safe browser-processing, energy-efficient, accurate Emotion AI solutions to analyze facial emotions, empowering AI Agents and delivering empathetic, data-driven, and dynamic digital '
  name: MorphCast
  slug: morphcast
artifact_total: 5
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/morphcast/refs/heads/main/plans/morphcast-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/morphcast-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/morphcast/refs/heads/main/rate-limits/morphcast-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/morphcast-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/morphcast/refs/heads/main/finops/morphcast-finops.yml
  title: ''
  type: FinOps
  url: finops/morphcast-finops.yml
- group: company
  title: ''
  type: Website
  url: https://morphcast.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/morphcast/refs/heads/main/security/morphcast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/morphcast-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MorphCast
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/morphcast
- group: company
  title: ''
  type: Blog
  url: https://www.morphcast.com/blog/feed/
created: '2025-02-09'
description: We expertly craft safe browser-processing, energy-efficient, accurate Emotion AI solutions to analyze facial emotions, empowering AI Agents and delivering empathetic, data-driven, and dynamic digital experiences.
finops:
- has_sources: false
  method: generated
  name: Morphcast Finops
  primary_unit: ''
  service_category: API
  slug: morphcast-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/morphcast.png
layout: provider
modified: '2026-09-16'
name: MorphCast
nav: Providers
network: true
overview: 'MorphCast is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Emotion AI, Facial Analysis, and SDK.


  MorphCast''s developer surface includes engineering blog and 7 more developer resources.'
plans:
- name: Morphcast Plans Pricing
  plan_count: 3
  slug: morphcast-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Morphcast Rate Limits
  slug: morphcast-rate-limits
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 33.0
    catalog_earned_first_party: 0.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 5.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/morphcast/refs/heads/main/screenshots/morphcast-2026-06-20T185816.png
security:
- kind: domain-security
  name: Morphcast Domain Security
  slug: morphcast-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: morphcast
tags:
- Emotion AI
- Facial Analysis
- SDK
website: https://morphcast.com
---
