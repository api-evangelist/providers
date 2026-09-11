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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.advsolarpower.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.advsolarpower.com/en/index.php/news
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advancedsolarpower-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advancedsolarpower-llms.txt
coverage:
  checked: '2026-09-09'
  detail: Advanced Solar Power (Hangzhou) Inc. manufactures and sells CdTe thin-film photovoltaic modules and BIPV hardware from a single PHP brochure site with no developer, API, or partner-integration section anywhere in its navigation, and no GitHub organization or package-registry presence.
  evidence:
  - status: 200
    url: https://www.advsolarpower.com/en/
  - status: 404
    url: https://www.advsolarpower.com/openapi.json
  - status: 404
    url: https://www.advsolarpower.com/.well-known/api-catalog
  - status: 200
    url: https://api.github.com/search/users?q=advsolarpower+OR+advancedsolarpower
  reason: not-a-software-company
  state: none
created: '2026-09-09'
description: Advanced Solar Power (Hangzhou) Inc. is a Chinese photovoltaic manufacturer founded in 2008 that researches, produces and sells cadmium telluride (CdTe) thin-film solar modules, photovoltaic system engineering, and building-integrated photovoltaic (BIPV) application products. It was the first CdTe thin-film module manufacturer in China, is led by former CdTe conversion-efficiency world-record holder Professor Xuanzhi Wu, and has developed its own deposition equipment and process technology. Its S1, S2 and S4 standard modules and BIPV lines (photovoltaic floor tiles, imitation-aluminum and imitation-marble facade modules, shaped and insulated modules) carry ISO, TUV, CE, UL, CQC, Australia CEC and California CEC certifications, and have been deployed on the China Pavilion of the 2019 Beijing Horticultural Expo and other landmark facade and rooftop projects. The company sells physical hardware and system integration; it publishes no developer program, API, or machine-readable
  interface of any kind.
image: https://www.advsolarpower.com/en/static/web/img/logo.jpg?v=v3
layout: provider
modified: '2026-09-09'
name: Advanced Solar Power
nav: Providers
network: true
overview: 'Advanced Solar Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Solar, Photovoltaics, Renewable Energy, and Thin Film.


  Advanced Solar Power''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 4.5
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Advancedsolarpower Domain Security
  slug: advancedsolarpower-domain-security
  summary_line: TLSv1.2
slug: advancedsolarpower
tags:
- Company
- Solar
- Photovoltaics
- Renewable Energy
- Thin Film
- BIPV
- Energy
- Manufacturing
- Hardware
- China
website: https://www.advsolarpower.com/en/
---
