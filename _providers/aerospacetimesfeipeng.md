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
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.htsdfp.com/
- group: company
  title: ''
  type: About
  url: https://www.htsdfp.com/About
- group: other
  title: ''
  type: Products
  url: https://www.htsdfp.com/Product
- group: operate
  title: ''
  type: Support
  url: https://www.htsdfp.com/ContactUs
- group: company
  title: ''
  type: Blog
  url: https://www.htsdfp.com/New
- group: company
  title: ''
  type: Press
  url: https://www.htsdfp.com/Media
- group: company
  title: ''
  type: Careers
  url: https://www.htsdfp.com/Job/list
- group: company
  title: ''
  type: Partners
  url: https://www.htsdfp.com/Cooperate
- group: other
  title: ''
  type: Copyright
  url: https://www.htsdfp.com/Copyright
- group: commercial
  title: ''
  type: Legal
  url: https://www.htsdfp.com/Disclaimer
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/aerospacetimesfeipeng
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerospacetimesfeipeng-domain-security.yml
coverage:
  checked: '2026-09-12'
  detail: Aerospace Times Feipeng is a CASC/SF Express cargo-UAV manufacturer whose entire public web presence (www.htsdfp.com, Chinese and English) is a hardware marketing site — products, scenarios, news, an AOPA pilot training centre and a sales contact form — with no developer, API, SDK or integration section anywhere in the navigation, no occurrence of "API", "SDK", "接口" or "开发者" in the page source, no GitHub organisation, and NXDOMAIN on api./developer./docs./open.htsdfp.com; its "无人机运行管控系统" (UAV operation control system) is sold as a delivered enterprise system, not as a callable service.
  evidence:
  - status: 200
    url: https://www.htsdfp.com/
  - status: 200
    url: https://www.htsdfp.com/En
  - status: 404
    url: https://www.htsdfp.com/openapi.json
  - status: 404
    url: https://www.htsdfp.com/llms.txt
  - status: 404
    url: https://www.htsdfp.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/htsdfp
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: Aerospace Times Feipeng Co., Ltd. (航天时代飞鹏有限公司) is a Chinese unmanned transport aircraft manufacturer founded in 2020 in the Huaqiao Economic Development Zone of Kunshan, Jiangsu, as a mixed-ownership enterprise launched by the China Aerospace Science and Technology Corporation (CASC) together with SF Express. It designs, manufactures and operates cargo UAV systems across three payload/range classes — the Double 1000 (1000 kg / 1000 km trunk-line), Double 100 (branch-line) and Double 10 (last-mile) series — alongside special aircraft, ground control stations, an unmanned aircraft operation control system, and an AOPA-certified UAV pilot training centre. Its FP-98 "Leo" large fixed-wing UAV received a CAAC type certificate in April 2024. The company publishes a corporate marketing website in Chinese and English; it operates no public developer program and publishes no machine-readable API contract.
image: https://www.htsdfp.com/UploadFiles/2025-07-11/etwwzchg62n8xnq3.png
layout: provider
modified: '2026-09-12'
name: Aerospace Times Feipeng
nav: Providers
network: true
overview: 'Aerospace Times Feipeng is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Drones, UAV, and Logistics.


  Aerospace Times Feipeng''s developer surface includes support, engineering blog, legal docs, and 9 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 0.0
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aerospacetimesfeipeng Domain Security
  slug: aerospacetimesfeipeng-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC
slug: aerospacetimesfeipeng
tags:
- Company
- Aerospace
- Drones
- UAV
- Logistics
- Manufacturing
- Aviation
- Low Altitude Economy
- China
website: https://www.htsdfp.com/
---
