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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/suiteness-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suiteness.com/privacy
- group: company
  title: ''
  type: Website
  url: https://www.suiteness.com
created: '2026-07-17'
description: Suiteness is a hotel booking platform specializing in connecting rooms and suites that hotels do not make public. Through partnerships with hotels, it surfaces adjoining rooms and suites - marked with a "+" symbol - so families and groups can book twice the space at roughly half the price of booking multiple standard rooms. It combines suite inventory, a concierge collaboration service, and a membership program. Suiteness is a consumer travel booking company backed by Bullpen Capital; it exposes no public developer API, SDK, or partner API surface at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/suiteness.png
layout: provider
modified: '2026-07-21'
name: Suiteness
nav: Providers
network: true
overview: Suiteness is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Hospitality, Hotels, and Booking.
random_paper: 8
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/suiteness/refs/heads/main/screenshots/suiteness-2026-09-02T161112.png
security:
- kind: domain-security
  name: Suiteness Domain Security
  slug: suiteness-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: suiteness
tags:
- Company
- Travel
- Hospitality
- Hotels
- Booking
- Suites
- Consumer
website: https://www.suiteness.com
---
