---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  url: security/getboxy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getboxy.co/
coverage:
  checked: '2026-08-17'
  detail: SAS Storelift, the company behind the Boxy autonomous-store brand, entered liquidation judiciaire on 2024-11-06 and its getboxy.co domain is now parked on ParkingCrew nameservers answering HTTP 410 Gone on every path, so there is no surface left to profile and none was ever published.
  evidence:
  - status: 410
    url: http://www.getboxy.co/
  - status: 410
    url: http://www.getboxy.co/openapi.json
  - status: 410
    url: http://www.getboxy.co/llms.txt
  - status: 410
    url: http://www.getboxy.co/.well-known/agent-card.json
  - status: 200
    url: https://storelift.com/.well-known/agent-card.json
  - status: 200
    url: https://www.pappers.fr/entreprise/storelift-838729192
  reason: defunct
  state: none
created: '2026-08-17'
description: Boxy, operated by the French company SAS Storelift (founded 2018 in Ivry-sur-Seine by David Gabai and Tom Hayat), built unstaffed 24/7 convenience stores inside 15-20 square metre shipping containers, using computer vision, weight-sensing shelves and an on-site compute node so a shopper could unlock the door with a QR code from the Boxy mobile app, take products off the shelf and walk out to be invoiced automatically. The company raised roughly 5M EUR in 2020 and a 25M EUR Series A in February 2022 led by Serena with CapHorn and LocalGlobe, targeting 1,000 stores. It shut its entire store estate by the end of April 2024, and SAS Storelift entered liquidation judiciaire on 6 November 2024 after sauvegarde and redressement procedures earlier that year; the store containers were auctioned in early 2025. The getboxy.co domain is now parked and returns HTTP 410 Gone on every path, and no developer program, API documentation or machine-readable contract was ever published. This profile
  records that absence.
layout: provider
modified: '2026-08-17'
name: Boxy (ex-Storelift)
nav: Providers
network: true
overview: Boxy (ex-Storelift) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, Convenience Stores, and Autonomous Stores.
random_paper: 14
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 4.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Getboxy Domain Security
  slug: getboxy-domain-security
  summary_line: no transport/DNS hardening detected
slug: getboxy
tags:
- Company
- Consumer
- Retail
- Convenience Stores
- Autonomous Stores
- Computer-Vision
- France
- Defunct
website: https://www.getboxy.co/
---
