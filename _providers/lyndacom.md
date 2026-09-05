---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://www.lynda.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.linkedin.com/learning/?trk=lynda_redirect_learning — a different registrable domain (lynda.com -> linkedin.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/lyndacom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.lynda.com
created: '2026-07-17'
description: Lynda.com was an online video learning platform founded in 1995 by Lynda Weinman and Bruce Heavin, offering courses in software, creative, and business skills. LinkedIn acquired Lynda.com in 2015 (~$1.5B) and folded it into LinkedIn Learning; the standalone Lynda.com service has been retired and www.lynda.com now 301-redirects to linkedin.com/learning. The brand exposes no public developer program or API surface of its own. This profile was surfaced as an Accel portfolio company and enriched as a lead; the honest result is a defunct brand with no first-party API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lyndacom.png
layout: provider
modified: '2026-07-20'
name: Lynda.com
nav: Providers
network: true
overview: Lynda.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Education, EdTech, and Online Learning.
random_paper: 15
score:
  band: minimal
  composite: 2.5
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
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lyndacom/refs/heads/main/screenshots/lyndacom-2026-07-25T225750.png
security:
- kind: domain-security
  name: Lyndacom Domain Security
  slug: lyndacom-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lyndacom
tags:
- Company
- Consumer
- Education
- EdTech
- Online Learning
- Video Courses
- Acquired
- LinkedIn
website: http://www.lynda.com
---
