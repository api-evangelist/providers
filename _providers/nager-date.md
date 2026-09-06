---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://date.nager.at'', ''status'': 301, ''note'': ''declared website redirects to https://nagerholidays.com/ — a different registrable domain (nager.at -> nagerholidays.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
api_count: 1
apis:
- description: Public holidays for more than 90 countries
  name: Nager.Date
  slug: nagerdate
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nager-date-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://date.nager.at
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Public holidays for more than 90 countries
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nager-date.png
layout: provider
modified: '2026-05-28'
name: Nager.Date
nav: Providers
network: true
overview: Nager.Date publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Calendar and Public APIs.
random_paper: 18
score:
  band: minimal
  composite: 7.6
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
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nager-date/refs/heads/main/screenshots/nager-date-2026-06-20T185926.png
security:
- kind: domain-security
  name: Nager Date Domain Security
  slug: nager-date-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nager-date
tags:
- Calendar
- Public APIs
website: https://date.nager.at
---
