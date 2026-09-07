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
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acchromtech-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/acchromtech-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.acchrom-tech.com/?l=en-us
- group: operate
  title: ''
  type: Support
  url: https://www.acchrom-tech.com/fuwu1.html?l=en-us
- group: company
  title: ''
  type: Blog
  url: https://www.acchrom-tech.com/news.html?l=en-us
coverage:
  checked: '2026-09-06'
  detail: Acchrom Tech is a Beijing chromatography-instrument maker whose only software product, the Chromloong CDS, is sold as an installed end-user laboratory system with no public API, SDK or developer portal — every developer-shaped host (api./developer./docs./open.) fails to resolve and every spec and well-known path on the one live web host 404s.
  evidence:
  - status: 404
    url: https://www.acchrom-tech.com/openapi.json
  - status: 404
    url: https://www.acchrom-tech.com/.well-known/api-catalog
  - status: 404
    url: https://www.acchrom-tech.com/llms.txt
  - status: 200
    url: https://www.acchrom-tech.com/goods6/231.html?l=en-us
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: 'Acchromtech (Acchrom Tech, legally Huapu Instrument (Beijing) Technology Co., Ltd.) is a Beijing-based analytical-instrument company founded in 2015 that develops, manufactures and services high-end chromatographic separation products: high-performance and ultra-high-performance liquid chromatography systems, triple-quadrupole LC-MS/MS, preparative and online-SPE instruments, and Alphasil / StarCore / SelectPrep / Marsil chromatographic columns and consumables. It also ships Chromloong, a self-developed chromatography data system (CDS) for chromatographic information management with distributed storage, network deployment and full-link audit. Its products are used in pharmaceutical, food-safety, environmental, disease-control, clinical-testing, inspection-and-quarantine, petrochemical and academic laboratories. It publishes no public API, SDK, developer portal or machine-readable contract; Chromloong is distributed as an end-user laboratory product.'
layout: provider
modified: '2026-09-06'
name: Acchromtech
nav: Providers
network: true
overview: 'Acchromtech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Chromatography, Analytical Instruments, Scientific Instruments, and Laboratory.


  Acchromtech''s developer surface includes support, engineering blog, and 3 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 5.1
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Acchromtech Domain Security
  slug: acchromtech-domain-security
  summary_line: TLSv1.2
slug: acchromtech
tags:
- Company
- Chromatography
- Analytical Instruments
- Scientific Instruments
- Laboratory
- Life Sciences
- Manufacturing
- China
website: https://www.acchrom-tech.com/?l=en-us
---
