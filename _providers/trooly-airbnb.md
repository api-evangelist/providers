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
    well_known_catalog: true
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trooly-airbnb/refs/heads/main/security/trooly-airbnb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trooly-airbnb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trooly.com
- group: other
  title: ''
  type: Archive
  url: https://web.archive.org/web/20170301/https://www.trooly.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trooly-airbnb/refs/heads/main/lifecycle/trooly-airbnb-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trooly-airbnb-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trooly-airbnb/refs/heads/main/well-known/trooly-airbnb-well-known.yml
  title: ''
  type: WellKnownProbe
  url: well-known/trooly-airbnb-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trooly-airbnb/refs/heads/main/llms/trooly-airbnb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trooly-airbnb-llms.txt
created: '2026-07-17'
description: Trooly, Inc. was a machine-learning trust and safety startup that scored the trustworthiness of individuals using publicly available data and digital footprints, offering its Instant Trust screening service to businesses for trust and safety management, risk assessment, and customer relationship use cases. Backed by Bain Capital Ventures, Trooly was acquired by Airbnb and ceased operations on June 19, 2017, shutting down its external APIs; its technology was absorbed into Airbnb's trust and safety systems and Trooly, Inc. remains an Airbnb subsidiary. trooly.com is now a parked domain and no living API surface exists.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trooly-airbnb.png
layout: provider
modified: '2026-07-21'
name: Trooly (Airbnb)
nav: Providers
network: true
overview: Trooly (Airbnb) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Trust and Safety, Machine Learning, and Background Checks.
random_paper: 6
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/trooly-airbnb/refs/heads/main/screenshots/trooly-airbnb-2026-09-02T164311.png
security:
- kind: domain-security
  name: Trooly Airbnb Domain Security
  slug: trooly-airbnb-domain-security
  summary_line: TLSv1.3
slug: trooly-airbnb
tags:
- Company
- Ai Apps
- Trust and Safety
- Machine Learning
- Background Checks
- Risk Assessment
- Acquired
- Defunct
website: https://trooly.com
---
