---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://livelovely.com'', ''status'': 301, ''note'': ''declared website redirects to https://ratelimited.apartmentguide.com/ — a different registrable domain (livelovely.com -> apartmentguide.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/homeboodle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://livelovely.com
created: '2026-07-17'
description: Homeboodle was a San Francisco rental marketplace startup that rebranded as "Lovely" around 2012. The product let renters search, apply for, and pay for apartments online, while giving landlords and property managers tools to list units, screen applicants, and collect rent. Backed by 500 Startups (now 500 Global) among other investors, Lovely (livelovely.com) was acquired by RentPath (the owner of Apartment Guide and Rent.com) for roughly $13M in April 2014. The company is now defunct as an independent product; livelovely.com issues a 301 redirect to apartmentguide.com and the former developer/API surface (hub.livelovely.com) is offline. This record is retained for historical and network-graph completeness rather than as an active API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/homeboodle.png
layout: provider
modified: '2026-07-19'
name: Homeboodle
nav: Providers
network: true
overview: Homeboodle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, Rentals, Marketplace, and Property Management.
random_paper: 4
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
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Homeboodle Domain Security
  slug: homeboodle-domain-security
  summary_line: TLSv1.3
slug: homeboodle
tags:
- Company
- Real-Estate
- Rentals
- Marketplace
- Property Management
- PropTech
- Defunct
website: https://livelovely.com
---
