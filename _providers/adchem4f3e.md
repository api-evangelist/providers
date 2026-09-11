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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adchem4f3e-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.adchem-tech.com/
- group: company
  title: ''
  type: About
  url: https://www.adchem-tech.com/About.html
- group: company
  title: ''
  type: Blog
  url: https://www.adchem-tech.com/news_list.html
- group: operate
  title: ''
  type: Support
  url: https://www.adchem-tech.com/contact.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adchem4f3e-llms.txt
coverage:
  checked: '2026-09-07'
  detail: Anhui ADChem Semi-Tech manufactures electronic-grade ALD/CVD precursor chemicals and source canisters for chip fabs; its entire 136-URL corporate site is product, news and careers pages with no developer section, and every OpenAPI, GraphQL, llms.txt and /.well-known/ probe against www.adchem-tech.com returned a 404 or a Tencent CDN 403 interstitial.
  evidence:
  - status: 200
    url: https://www.adchem-tech.com/
  - status: 200
    url: https://www.adchem-tech.com/sitemap.xml
  - status: 404
    url: https://www.adchem-tech.com/llms.txt
  - status: 404
    url: https://www.adchem-tech.com/.well-known/security.txt
  - status: 403
    url: https://www.adchem-tech.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: Anhui ADChem Semi-Tech Co., Ltd. (安徽安德科铭半导体科技股份有限公司) is a Hefei, China based manufacturer of electronic-grade semiconductor thin-film precursor materials, founded in 2018 and operating an R&D base in Hefei with production sites in Tongling plus sales and market-development offices in Shanghai and Wuhan. The company develops and produces high-purity ALD and CVD precursors — silicon-based precursors (BDEAS, BTBAS, DIPAS, DIS), High-K hafnium and zirconium precursors (TDMAHf, TEMAHf, CpHf, HfCl4, TEMAZ, CpZr, ZrCl4), metal and conductive-film precursors (TMA, TBTDEN, WCl5, MoCl5, CCTBA, Ru(EtCp)2) and perovskite photovoltaic precursors — alongside custom source canisters, liquid delivery systems and thin-film process solutions for integrated-circuit manufacturing, advanced display and new-energy customers. ADChem sells physical chemical products; it operates no public developer program, API, or software platform.
image: https://omo-oss-image1.thefastimg.com/portal-saas/pg2024072614393773562/cms/image/3c87a474-05c5-4098-8248-b6938a476638.jpg?vf=B7gH3s
layout: provider
modified: '2026-09-07'
name: ADChem Semi-Tech
nav: Providers
network: true
overview: 'ADChem Semi-Tech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Electronic Materials, Specialty Chemicals, and Thin Film.


  ADChem Semi-Tech''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 6.4
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
  previous_composite: 6.4
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Adchem4F3E Domain Security
  slug: adchem4f3e-domain-security
  summary_line: TLSv1.3
slug: adchem4f3e
tags:
- Company
- Semiconductors
- Electronic Materials
- Specialty Chemicals
- Thin Film
- ALD
- CVD
- Precursors
- Manufacturing
- China
website: https://www.adchem-tech.com/
---
