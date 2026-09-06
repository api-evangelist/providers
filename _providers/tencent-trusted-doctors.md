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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.doctorwork.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doctorwork
- group: build
  title: ''
  type: Packages
  url: packages/tencent-trusted-doctors-packages.yml
coverage:
  checked: '2026-08-30'
  detail: The company was absorbed into Medlinker on 2021-01-01 and its brand retired in April 2021; its own primary domain www.xingren.com now returns a blanket HTTP 301 to www.medlinker.com, and the only surviving "开发者中心" at developer.doctorwork.com is internal employee tooling behind the company's own SSO (the page loads /_/sso/internal/user and an app bundle named "oa-dev-tools"), not a public developer portal.
  evidence:
  - status: 301
    url: https://www.xingren.com/
  - status: 200
    url: https://developer.doctorwork.com/
  - status: 404
    url: https://api.xingren.com/openapi.json
  - status: 301
    url: https://www.doctorwork.com/openapi.json
  - status: 404
    url: https://developer.doctorwork.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/doctorwork
  reason: defunct
  state: none
created: '2026-08-30'
description: Tencent Trusted Doctors (企鹅杏仁) was a Chinese digital-health group formed in August 2018 by merging Tencent's medical unit Tencent Doctorwork (企鹅医生) with the Shanghai doctor platform Trusted Doctors (杏仁医生). It combined an online consultation and doctor-social platform with a network of bricks-and-mortar clinics, connecting roughly 440,000 verified physicians to more than 10 million patients, and reached unicorn valuation on a USD 250M round in April 2019 backed by Tencent and Country Garden Ventures. The company was acquired by Medlinker (医联) with the deal completing 2021-01-01, and the 企鹅杏仁 brand was retired in April 2021 in favour of 未来医生 (Future Doctor). It never published a public developer program, API reference, or machine-readable contract, and its primary domain xingren.com now redirects wholesale to the acquirer.
layout: provider
modified: '2026-08-30'
name: Tencent Trusted Doctors
nav: Providers
network: true
overview: Tencent Trusted Doctors is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telemedicine, and Digital Health.
random_paper: 15
score:
  band: minimal
  composite: 2.2
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
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
slug: tencent-trusted-doctors
tags:
- Company
- Health
- Healthcare
- Telemedicine
- Digital Health
- Clinics
- China
- Acquired
website: https://www.doctorwork.com/
---
