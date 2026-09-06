---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.fishwatch.gov/developers'', ''status'': 301, ''note'': ''declared website redirects to https://www.fisheries.noaa.gov/topic/sustainable-seafood — a different registrable domain (fishwatch.gov -> noaa.gov), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- description: Information and pictures about individual fish species
  name: FishWatch
  slug: fishwatch
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fishwatch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fishwatch.gov/developers
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Information and pictures about individual fish species
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fishwatch.png
layout: provider
modified: '2026-05-28'
name: FishWatch
nav: Providers
network: true
overview: FishWatch publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Animals and Public APIs.
random_paper: 16
score:
  band: minimal
  composite: 5.7
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fishwatch/refs/heads/main/screenshots/fishwatch-2026-06-20T181254.png
security:
- kind: domain-security
  name: Fishwatch Domain Security
  slug: fishwatch-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: fishwatch
tags:
- Animals
- Public APIs
website: https://www.fishwatch.gov/developers
---
