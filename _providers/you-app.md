---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://you-app.com'', ''status'': 302, ''note'': ''declared website redirects to https://www.hintsa.com/ — a different registrable domain (you-app.com -> hintsa.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/you-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://you-app.com
created: '2026-07-17'
description: YOU-app was a mobile wellbeing application built by Fifth Corner (Helsinki, Finland) that delivered daily "micro-actions" across food, mindfulness, movement, and mental wellbeing, blending social-media style photo sharing with habit-building and originally aligned to the UN Sustainable Development Goals. The company was acquired and is no longer operated as an independent product; the you-app.com domain now 302-redirects to Hintsa Performance (hintsa.com). No public API, developer portal, documentation, SDKs, or machine-readable specification was found during enrichment — this remains a consumer-app profile with no developer surface to catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/you-app.png
layout: provider
modified: '2026-07-21'
name: YOU-app
nav: Providers
network: true
overview: YOU-app is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wellbeing, Health, Wellness, and Mobile App.
random_paper: 1
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/you-app/refs/heads/main/screenshots/you-app-2026-09-02T171322.png
security:
- kind: domain-security
  name: You App Domain Security
  slug: you-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: you-app
tags:
- Company
- Wellbeing
- Health
- Wellness
- Mobile App
- Consumer
- Habit Tracking
- Acquired
website: https://you-app.com
---
