---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.toyota-global.com/'', ''status'': 302, ''note'': ''declared website redirects to https://global.toyota/en/ — a different registrable domain (toyota-global.com -> global.toyota), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  url: security/toyota-motor-corporation-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Toyota-Motor-North-America
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toyota
- group: company
  title: ''
  type: Website
  url: https://www.toyota-global.com/
- group: company
  title: ''
  type: Blog
  url: https://pressroom.toyota.com/feed/
created: '2026-05-05'
description: The world's largest automobile manufacturer by production volume, producing a wide range of vehicles from sedans and SUVs to hybrids and hydrogen fuel cell cars. Pioneer of lean manufacturing and hybrid technology through the iconic Prius.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toyota-motor-corporation.png
layout: provider
modified: '2026-05-05'
name: Toyota Motor Corporation
nav: Providers
network: true
overview: 'Toyota Motor Corporation is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Manufacturing, Electric Vehicles, and Hybrid.


  Toyota Motor Corporation''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 19.0
    catalog_earned_first_party: 0.0
    catalog_gap: 96.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 35.2
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 4.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/toyota-motor-corporation/refs/heads/main/screenshots/toyota-motor-corporation-2026-06-20T195510.png
security:
- kind: domain-security
  name: Toyota Motor Corporation Domain Security
  slug: toyota-motor-corporation-domain-security
  summary_line: TLSv1.2
slug: toyota-motor-corporation
tags:
- Automobiles
- Manufacturing
- Electric Vehicles
- Hybrid
website: https://www.toyota-global.com/
---
