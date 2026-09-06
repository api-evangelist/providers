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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yuze-semiconductor-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yuze-semiconductor-llms.txt
- group: company
  title: ''
  type: Website
  url: https://en.yzbdt.com/
- group: company
  title: ''
  type: Blog
  url: https://en.yzbdt.com/news.html
- group: operate
  title: ''
  type: Support
  url: https://en.yzbdt.com/contact.html
coverage:
  checked: '2026-09-04'
  detail: Yuze Semiconductor manufactures N-type solar monocrystalline silicon rods and wafers; its only public web presence (en.yzbdt.com / www.yzbdt.com) is a six-section corporate brochure — About, Product, Base, News, Contact, Recruitment — whose full sitemap of 68 URLs contains no developer, API, or documentation page, and no api/dev/docs/developer/open subdomain resolves in DNS.
  evidence:
  - status: 200
    url: https://en.yzbdt.com/sitemap.xml
  - status: 404
    url: https://en.yzbdt.com/.well-known/security.txt
  - status: 403
    url: https://en.yzbdt.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-09-04'
description: 'Yuze Semiconductor — legally Yunnan Yuze New Energy Co., Ltd. (云南宇泽新能源股份有限公司), trading internationally as Unigrace New Energy — is a Chinese photovoltaic materials manufacturer founded in May 2019 and headquartered in Kunming, Yunnan. It produces N-type solar monocrystalline silicon rods and wafers covering the three mainstream N-type cell routes (HJT, TOPCon and IBC), operating manufacturing bases in Chuxiong, Wenshan and Kunming in Yunnan and Yichun in Jiangxi, with a sales centre in Suzhou. The company was named a 2022 Chinese Unicorn Enterprise and its shares trade on secondary private markets. It is a physical-goods manufacturer: its public web presence carries company, product, news and recruitment pages only, with no developer program, no API, and no machine-readable specification of any kind.'
image: https://en.yzbdt.com/favicon.ico
layout: provider
modified: '2026-09-04'
name: Yuze Semiconductor
nav: Providers
network: true
overview: 'Yuze Semiconductor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Solar, Photovoltaics, and Silicon Wafers.


  Yuze Semiconductor''s developer surface includes engineering blog, support, and 3 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 4.7
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
    developer_ergonomics: 7.1
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
  previous_composite: 4.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Yuze Semiconductor Domain Security
  slug: yuze-semiconductor-domain-security
  summary_line: TLSv1.3 · DMARC
slug: yuze-semiconductor
tags:
- Company
- Semiconductors
- Solar
- Photovoltaics
- Silicon Wafers
- Manufacturing
- Materials
- Renewable Energy
- China
website: https://en.yzbdt.com/
---
