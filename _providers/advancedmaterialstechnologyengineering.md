---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: http://openapi.amteglobal.cn
  baseurl_source: declared
  description: The Object API from Advanced Materials Technology & Engineering — 1 operation(s) for object.
  name: Advanced Materials Technology & Engineering Object API
  slug: advancedmaterialstechnologyengineering-object-api
artifact_total: 5
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/advancedmaterialstechnologyengineering/refs/heads/main/security/advancedmaterialstechnologyengineering-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/advancedmaterialstechnologyengineering-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amteglobal.cn/
- group: company
  title: ''
  type: Blog
  url: https://www.amteglobal.cn/enews/31.html
- group: operate
  title: ''
  type: Support
  url: https://www.amteglobal.cn/econtact/32.html
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/advancedmaterialstechnologyengineering/refs/heads/main/plans/advancedmaterialstechnologyengineering-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/advancedmaterialstechnologyengineering-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/advancedmaterialstechnologyengineering/refs/heads/main/rate-limits/advancedmaterialstechnologyengineering-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/advancedmaterialstechnologyengineering-rate-limits.yml
created: '2026-09-07'
description: Advanced Materials Technology & Engineering, Inc. (AMTE; Chinese entity 无锡邑文微电子科技股份有限公司, Wuxi Yiwen Microelectronics Technology / 邑文科技) is a Chinese semiconductor capital-equipment maker founded in 2011 and headquartered at No. 1 Guanshan Road, Wuxi, Jiangsu, with a production center at No. 1 Jinshan Road, Rudong, Nantong that runs more than 2,000 square meters of class-10,000 cleanroom plus a class-1,000 specialty-gas process laboratory. AMTE designs and manufactures front-end wafer-fabrication equipment — plasma etch systems and thin-film deposition (PECVD) systems — for IC and OSD production, with a stated focus on compound semiconductor, MEMS and advanced-packaging process lines; the company says its tools qualified into 12-inch fabs including SMIC and SK Hynix from 2016-2017, and it holds Chinese national high-tech enterprise status (2017) and ISO 9001 certification (2015). It raised a Series D of more than RMB 550 million (about USD 70.5 million) in 2024, co-led by CICC
  Capital and a Haitong Securities alternative-investment vehicle, and its shares appear on the EquityZen secondary marketplace, which is how the company entered the API Evangelist harvest backlog. AMTE sells physical process equipment, refurbished tools, spare parts and field service — not software. It operates no developer program, publishes no public API, and serves no machine-readable API contract of any kind.
image: https://www.amteglobal.cn/Public/bnimg/5f4c4e4d5825a.png
layout: provider
modified: '2026-09-07'
name: Advanced Materials Technology & Engineering
nav: Providers
network: true
overview: 'Advanced Materials Technology & Engineering publishes 1 API on the [APIs.io](https://apis.io/) network: Object API. Tagged areas include Company, Semiconductors, Semiconductor Equipment, Wafer Fabrication, and Thin Film Deposition.


  Advanced Materials Technology & Engineering''s developer surface includes engineering blog, support, and 4 more developer resources.'
plans:
- name: Advancedmaterialstechnologyengineering Plans Pricing
  plan_count: 0
  slug: advancedmaterialstechnologyengineering-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Advancedmaterialstechnologyengineering Rate Limits
  slug: advancedmaterialstechnologyengineering-rate-limits
score:
  band: emerging
  composite: 20.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 40.8
    developer_ergonomics: 19.0
    discoverability: 68.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 19.0
  provenance:
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Advancedmaterialstechnologyengineering Authentication
  slug: advancedmaterialstechnologyengineering-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Advancedmaterialstechnologyengineering Domain Security
  slug: advancedmaterialstechnologyengineering-domain-security
  summary_line: TLSv1.3 · HSTS
slug: advancedmaterialstechnologyengineering
tags:
- Company
- Semiconductors
- Semiconductor Equipment
- Wafer Fabrication
- Thin Film Deposition
- Plasma Etch
- MEMS
- Compound Semiconductors
- Advanced Packaging
- Manufacturing
- Industrial Hardware
- China
website: https://www.amteglobal.cn/
---
