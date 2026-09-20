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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.aero-tech.com.cn/
- group: company
  title: ''
  type: Blog
  url: https://www.aero-tech.com.cn/news/1/
- group: operate
  title: ''
  type: Support
  url: https://www.aero-tech.com.cn/service.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aerotech388e/refs/heads/main/security/aerotech388e-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aerotech388e-domain-security.yml
coverage:
  checked: '2026-09-12'
  detail: Aerotech is 中科艾尔（北京）科技有限公司, a Beijing manufacturer of ultra-high-purity semiconductor gas valves, regulators and electropolished tubing whose entire web presence is a twelve-page 300.cn brochure CMS — its own sitemap lists all 225 URLs it serves and not one of them is a developer, api, docs or spec path, the only "documentation" it publishes is twelve PDF hardware catalogues on /download.html, and api/dev/developer/docs/portal subdomains are all NXDOMAIN.
  evidence:
  - status: 200
    url: https://www.aero-tech.com.cn/sitemap.xml
  - status: 404
    url: https://www.aero-tech.com.cn/llms.txt
  - status: 404
    url: https://www.aero-tech.com.cn/.well-known/security.txt
  - status: 200
    url: https://www.aero-tech.com.cn/download.html
  - status: 200
    url: https://equityzen.com/company/aerotech388e/
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: 'Aerotech — 中科艾尔（北京）科技有限公司, Zhongke Aier (Beijing) Technology Co., Ltd., founded in March 2008 as 泰科爱尔（北京）科技有限公司 (Taike Aier) with a Japanese engineering team — is a Beijing semiconductor components manufacturer that researches, produces and sells ultra-high-purity gas line tube and valve hardware: UHP pressure regulators, diaphragm valves, bellows and vacuum angle valves, ball and check valves, EP/BA electropolished stainless tubing and fittings, integrated gas distribution panels, measurement devices and precursor source bottles. The company developed its own EP (electrolytic polishing) process in 2009 and its own industrial electropolishing equipment in 2012, joined the MIIT domestic-substitution program piloted at SMIC in 2018, opened a 10,969 m² class-10 cleanroom plant in the Cangzhou Bohai New Area in September 2020 on a RMB 230M investment, and became a qualified SMIC (中芯国际) supplier in March 2021. Its product is physical hardware for semiconductor fab gas delivery;
  it operates no developer program, no public API, no SDK and no machine-readable API contract.'
image: https://www.aero-tech.com.cn/favicon.ico
layout: provider
modified: '2026-09-12'
name: Aerotech (Beijing)
nav: Providers
network: true
overview: 'Aerotech (Beijing) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Manufacturing, Hardware, and Industrial Equipment.


  Aerotech (Beijing)''s developer surface includes engineering blog, support, and 2 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 6.4
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aerotech388E Domain Security
  slug: aerotech388e-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aerotech388e
tags:
- Company
- Semiconductors
- Manufacturing
- Hardware
- Industrial Equipment
- Valves
- Gas Delivery
- Ultra High Purity
- Electropolishing
- China
website: https://www.aero-tech.com.cn/
---
