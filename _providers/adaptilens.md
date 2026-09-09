---
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
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adaptilens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adaptilens.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adaptilens/
coverage:
  checked: '2026-09-07'
  detail: Adaptilens is a pre-clinical ophthalmic device developer whose product is a physical implant, the A-IOL accommodating intraocular lens, and adaptilens.com is a five-page WordPress marketing site that currently returns HTTP 500 with the body "There has been a critical error on this website" for every path except / and /team/ -- including its own /our-technology/, /news/ and /contact/ pages, /wp-json/ and every /.well-known/ path -- so there is no developer surface to read and no host that answers one.
  evidence:
  - status: 200
    url: https://adaptilens.com/
  - status: 500
    url: https://adaptilens.com/.well-known/adaptilens-negative-control-4b19cd7e.json
  - status: 500
    url: https://adaptilens.com/openapi.json
  - status: 500
    url: https://adaptilens.com/wp-json/
  - status: 404
    url: https://api.github.com/orgs/adaptilens
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: Adaptilens is a privately held, pre-clinical ophthalmic medical device company based in Chestnut Hill, Massachusetts, developing the Adaptilens A-IOL, described by the company as the first biomimetic accommodating intraocular lens. The soft, flexible lens is built around a patent-protected bottlebrush polymer intended to mimic the young natural crystalline lens, responding to the eye's own ciliary muscles and natural signal to focus so that cataract patients regain near, intermediate and distance vision without glasses. The company raised $1.6M in seed funding led by Pillar VC and a $17.5M Series A led by Perceptive Xontogeny Venture Funds with Pillar VC, 380 Cap and Accanto Partners. Its own site states the Adaptilens is in the development phase and is not yet approved for investigational or commercial use. Adaptilens is a device developer, not a software company, and publishes no developer program, no API documentation and no machine-readable API contract of any kind.
image: https://adaptilens.com/wp-content/uploads/2024/11/Share-Image-1.jpg
layout: provider
modified: '2026-09-07'
name: Adaptilens
nav: Providers
network: true
overview: Adaptilens is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Medical Devices, Ophthalmology, Intraocular Lens, Health, and Life Sciences.
random_paper: 11
score:
  band: minimal
  composite: 3.3
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adaptilens Domain Security
  slug: adaptilens-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: adaptilens
tags:
- Medical Devices
- Ophthalmology
- Intraocular Lens
- Health
- Life Sciences
- Biotechnology
- Vision
- Cataract Surgery
- Massachusetts
- Company
website: https://adaptilens.com/
---
