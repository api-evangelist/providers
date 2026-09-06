---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Licensed client REST API delivering StatsBomb event data, 360 freeze frames, player-location data, and derived metrics (xG, OBV, HOPS) for contracted competitions. Access is granted under commercial a
  name: StatsBomb Data API
  slug: data-api
- description: Hosted analytics platform layered on top of StatsBomb Data for recruitment, tactical analysis, and performance evaluation. Includes customizable visualizations and native integration with Hudl Sportsc
  name: StatsBomb IQ
  slug: iq-platform
- description: Free, publicly released sample of StatsBomb event data (and selected 360 data) distributed via GitHub for academic and community research. JSON files keyed by competition, season, and match.
  name: StatsBomb Open Data
  slug: open-data
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/statsbomb-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/statsbomb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.hudl.com/en_gb/products/statsbomb
- group: build
  title: ''
  type: GitHub
  url: https://github.com/statsbomb
- group: other
  title: ''
  type: OpenData
  url: https://github.com/statsbomb/open-data
- group: other
  title: Hudl (parent company)
  type: Parent
  url: https://www.hudl.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/statsbomb
- group: operate
  title: ''
  type: Contact
  url: https://www.hudl.com/en_gb/products/statsbomb
created: '2026-05-23'
description: StatsBomb, now part of Hudl, supplies advanced football (soccer) analytics and data to professional clubs, federations, broadcasters, and media. The StatsBomb Data product captures 3,400+ events per match across 190+ competitions with proprietary models (Expected Goals, On-Ball Value, HOPS) and bundled player-location and 360 data. Delivery is sales-led through licensed client APIs and standard file formats (JSON, XML, CSV), with the StatsBomb Open Data set published publicly on GitHub for the research community.
finops:
- name: Statsbomb Finops
  service_category: API
  slug: statsbomb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/statsbomb.png
layout: provider
modified: '2026-05-23'
name: StatsBomb (Hudl)
nav: Providers
network: true
overview: 'StatsBomb (Hudl) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Football, Soccer, Analytics, Event Data, and Tracking.


  StatsBomb (Hudl)''s developer surface includes GitHub presence and 7 more developer resources.'
plans:
- name: Statsbomb Plans Pricing
  plan_count: 1
  slug: statsbomb-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Statsbomb Rate Limits
  slug: statsbomb-rate-limits
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/statsbomb/refs/heads/main/screenshots/statsbomb-2026-06-20T194528.png
security:
- kind: domain-security
  name: Statsbomb Domain Security
  slug: statsbomb-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Statsbomb Trust Center
  slug: statsbomb-trust-center
  summary_line: SOC 2, GDPR
slug: statsbomb
tags:
- Football
- Soccer
- Analytics
- Event Data
- Tracking
- xG
- On-Ball Value
- Hudl
website: https://www.hudl.com/en_gb/products/statsbomb
---
