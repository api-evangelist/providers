---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://welco.me/'', ''status'': 301, ''note'': ''declared website redirects to https://www.dorsia.com:443/newsroom/welcome-tripnotes — a different registrable domain (welco.me -> dorsia.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/welcome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://welco.me/
created: '2026-07-17'
description: 'Welcome (welco.me) was an AI-powered travel planning product (TripNotes) surfaced as a portfolio company of accel, techstars. As of this enrichment pass welco.me 301-redirects to dorsia.com/newsroom/welcome-tripnotes, indicating the standalone product was acquired by / folded into Dorsia; no independent public API, developer portal, documentation, or well-known surface remains. Sector: ai. Retained as a network record with a live domain-security probe.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/welcome.png
layout: provider
modified: '2026-07-21'
name: Welcome
nav: Providers
network: true
overview: Welcome is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Travel, Acquired, and Defunct.
random_paper: 13
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
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
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Welcome Domain Security
  slug: welcome-domain-security
  summary_line: TLSv1.3
slug: welcome
tags:
- Company
- Artificial Intelligence
- Travel
- Acquired
- Defunct
website: https://welco.me/
---
