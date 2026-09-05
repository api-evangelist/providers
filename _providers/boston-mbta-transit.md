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
api_count: 1
apis:
- description: Stations and predicted arrivals for MBTA
  name: Boston MBTA Transit
  slug: boston-mbta-transit
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boston-mbta-transit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mbta.com/developers/v3-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://www.mbta.com/news/rss.xml
created: '2026-05-28'
description: Stations and predicted arrivals for MBTA
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boston-mbta-transit.png
layout: provider
modified: '2026-05-28'
name: Boston MBTA Transit
nav: Providers
network: true
overview: 'Boston MBTA Transit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation and Public APIs.


  Boston MBTA Transit''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boston-mbta-transit/refs/heads/main/screenshots/boston-mbta-transit-2026-06-20T173613.png
security:
- kind: domain-security
  name: Boston Mbta Transit Domain Security
  slug: boston-mbta-transit-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: boston-mbta-transit
tags:
- Transportation
- Public APIs
website: https://www.mbta.com/developers/v3-api
---
