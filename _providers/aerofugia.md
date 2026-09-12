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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerofugia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aerofugia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerofugia.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.aerofugia.com/newslist
coverage:
  checked: '2026-09-10'
  detail: 'Aerofugia builds and will operate eVTOL aircraft, not software products: every URL in its own sitemap.xml (66 of them) is marketing, news, recruitment or a partnership contact form, there is no /developers, /docs or /api path, no GitHub organization exists under the name, and the origin nginx 301-redirects every /api* path to itself so nothing under /api can ever resolve.'
  evidence:
  - status: 200
    url: https://www.aerofugia.com/sitemap.xml
  - status: 404
    url: https://www.aerofugia.com/openapi.json
  - status: 301
    url: https://www.aerofugia.com/api-docs
  - status: 404
    url: https://www.aerofugia.com/.well-known/api-catalog
  - status: 404
    url: https://www.aerofugia.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/aerofugia
  reason: no-developer-program
  state: none
created: '2026-09-10'
description: 'Aerofugia (沃飞长空, Sichuan Aerofugia Technology Development Co., Ltd.) is a Chengdu-based advanced air mobility company founded in 2020 under Zhejiang Geely Holding Group''s Geely Technology Group, focused on the research, certification and commercial operation of low-altitude passenger aircraft. Its flagship product is the AE200 series, a six-seat all-electric piloted eVTOL with a roughly 200 km range aimed at intercity air mobility, low-altitude tourism and emergency medical transport; the AE200 was the first piloted eVTOL type certificate application accepted by the Civil Aviation Administration of China, has completed full tilt-transition flight testing, and the company holds a CCAR-135 air operator certificate. As of this profile Aerofugia publishes no public developer program, API documentation or machine-readable API contract: it is an aircraft manufacturer and future air-mobility operator, not a platform vendor.'
image: https://aerogw.obs.cn-east-3.myhuaweicloud.com/media/logo/02hui2.png
layout: provider
modified: '2026-09-10'
name: Aerofugia
nav: Providers
network: true
overview: 'Aerofugia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, Aerospace, eVTOL, Advanced Air Mobility, and Urban Air Mobility.


  Aerofugia''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 2
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
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 7.6
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aerofugia Domain Security
  slug: aerofugia-domain-security
  summary_line: TLSv1.3
slug: aerofugia
tags:
- Aviation
- Aerospace
- eVTOL
- Advanced Air Mobility
- Urban Air Mobility
- Electric Aircraft
- Transportation
- Manufacturing
- China
- Company
website: https://www.aerofugia.com/
---
