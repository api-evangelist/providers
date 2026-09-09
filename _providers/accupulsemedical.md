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
- group: company
  title: ''
  type: Website
  url: https://accupulse.com/
- group: company
  title: ''
  type: About
  url: https://accupulse.com/h-col-101.html
- group: other
  title: ''
  type: x-products
  url: https://accupulse.com/h-col-103.html
- group: company
  title: ''
  type: Newsroom
  url: https://accupulse.com/h-col-104.html
- group: company
  title: ''
  type: Careers
  url: https://accupulse.com/h-col-102.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/78468867
- group: other
  title: ''
  type: x-instructions-for-use
  url: https://eifu.accupulse.com/
- group: other
  title: ''
  type: x-secondary-market-listing
  url: https://equityzen.com/company/accupulsemedical
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accupulsemedical-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accupulsemedical-llms.txt
coverage:
  checked: '2026-09-06'
  detail: AccuPulse manufactures regulated cardiac ablation hardware — the AccuBlator PFA generator, the AccuPulse catheter and the Accu-System 3D mapping console — and its entire public surface is a five-page site-builder marketing site (home, about, products, news, careers) plus a language-gated eIFU portal that serves device manuals as documents; there is no developer, API, docs or integration link anywhere in the nav, footer or sitemap, no GitHub organization, and no package under the AccuPulse name in npm or PyPI.
  evidence:
  - status: 200
    url: https://accupulse.com/
  - status: 200
    url: https://accupulse.com/sitemap.xml
  - status: 404
    url: https://accupulse.com/openapi.json
  - status: 404
    url: https://accupulse.com/swagger.json
  - status: 404
    url: https://accupulse.com/graphql
  - status: 404
    url: https://accupulse.com/api-docs
  - status: 404
    url: https://accupulse.com/developers
  - status: 404
    url: https://accupulse.com/llms.txt
  - status: 404
    url: https://accupulse.com/.well-known/agent-card.json
  - status: 404
    url: https://accupulse.com/.well-known/agent.json
  - status: 404
    url: https://accupulse.com/.well-known/api-catalog
  - status: 404
    url: https://accupulse.com/.well-known/security.txt
  - status: 404
    url: https://accupulse.com/zz-api-evangelist-control-9f3a
  - status: 404
    url: https://eifu.accupulse.com/.well-known/agent-card.json
  - status: 200
    url: https://eifu.accupulse.com/zz-api-evangelist-control-9f3a
  - status: 404
    url: https://api.github.com/orgs/accupulse
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: AccuPulse Medical Technology Co., Ltd. (Suzhou AccuPulse, 艾科脉) is a cardiac electrophysiology medical device company in Suzhou Industrial Park, Jiangsu, China, founded in November 2020 to treat atrial fibrillation with non-thermal ablation. It is developing a pulsed electric field ablation (PFA) system — the AccuBlator generator and AccuPulse catheter — using high-voltage fields to induce irreversible electroporation in endocardial cells instead of the thermal injury caused by radiofrequency and cryoablation, plus Accu-System, a 3D cardiac electroanatomic mapping and navigation platform with magnetic/electrical localization and high-channel intracardiac EGM acquisition. The founding team came out of Johnson & Johnson, GE, Abbott, Acutus Medical and MicroPort, with R&D in China and the United States. AccuPulse sells regulated devices to hospitals; it runs no developer program and publishes no public API, SDK or machine-readable API contract on any host it controls.
image: https://28415683.s21i.faiusr.com/4/ABUIABAEGAAgn8iajgYoqNjpvAYw_gE4Ug.png
layout: provider
modified: '2026-09-06'
name: AccuPulse Medical Technology Co., Ltd.
nav: Providers
network: true
overview: AccuPulse Medical Technology Co., Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Health Care, Cardiology, and Electrophysiology.
random_paper: 4
score:
  band: minimal
  composite: 3.3
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
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
  name: Accupulsemedical Domain Security
  slug: accupulsemedical-domain-security
  summary_line: TLSv1.2
slug: accupulsemedical
tags:
- Company
- Medical Devices
- Health Care
- Cardiology
- Electrophysiology
- Cardiac Ablation
- Medical Imaging
- Manufacturing
- China
website: https://accupulse.com/
---
