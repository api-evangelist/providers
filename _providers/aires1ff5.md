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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aires1ff5/refs/heads/main/security/aires1ff5-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aires1ff5-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.iris-amoi.com/
- group: company
  title: ''
  type: About
  url: https://www.iris-amoi.com/aboutus.aspx?ClassID=2
- group: company
  title: ''
  type: Partners
  url: https://www.iris-amoi.com/partner.aspx?ClassID=5
- group: operate
  title: ''
  type: Support
  url: https://www.iris-amoi.com/Contact.aspx?ClassID=7
coverage:
  checked: '2026-09-19'
  detail: IRIS (Xiamen) Science is a contact-lens factory selling ODM/OEM manufacturing to consumer brands; its only web presence, iris-amoi.com, is a Chinese-language ASP.NET brochure site whose every non-page path — openapi.json, llms.txt, all eight /.well-known/ documents and a control path that cannot exist — returns the same 200 soft-404 stub "[404]", and no api./developer. host, GitHub org or package exists.
  evidence:
  - status: 200
    url: https://www.iris-amoi.com/
  - status: 200
    url: https://www.iris-amoi.com/sitemap.xml
  - status: 200
    url: https://www.iris-amoi.com/openapi.json
  - status: 200
    url: https://www.iris-amoi.com/llms.txt
  - status: 200
    url: https://www.iris-amoi.com/.well-known/agent-card.json
  - status: 200
    url: https://www.iris-amoi.com/this-path-cannot-exist-x9z
  - status: 403
    url: https://equityzen.com/company/aires1ff5
  reason: not-a-software-company
  state: none
created: '2026-09-19'
description: 'Aires is the EquityZen listing name for 爱睿思（厦门）科技有限公司 — IRIS (Xiamen) Science Co., Ltd. (ISC), a contact-lens research, development and manufacturing company founded in 2020 in Tong''an District, Xiamen, China. It runs a fully automated colour contact lens factory (22,500 m² phase-one plant, RMB 600 million-plus investment) with in-house-designed equipment, automated optical inspection and sterile filling, and sells 38% and 55% water-content daily and semi-annual clear and colour lenses as ODM/OEM contract manufacturing — lens and pattern design, licensing support, logistics — to consumer brands. Built as the captive supply chain of the moody colour-lens brand, it holds high-tech enterprise certification and 18 patents, and closed a RMB 100 million-plus B+ round led by Qianqi Capital in March 2026. It is a physical-goods manufacturer: iris-amoi.com is a Chinese-language brochure site with no developer program, API, SDK, webhook surface or machine-readable specification of any
  kind.'
image: https://www.iris-amoi.com/upload/img/20230424105439.png
layout: provider
modified: '2026-09-19'
name: Aires (IRIS Xiamen Science)
nav: Providers
network: true
overview: 'Aires (IRIS Xiamen Science) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Contact Lenses, Manufacturing, Medical Devices, and Vision Care.


  Aires (IRIS Xiamen Science)''s developer surface includes support and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 4.3
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aires1Ff5 Domain Security
  slug: aires1ff5-domain-security
  summary_line: TLSv1.2
slug: aires1ff5
tags:
- Company
- Contact Lenses
- Manufacturing
- Medical Devices
- Vision Care
- Optics
- Consumer Goods
- ODM
- China
website: https://www.iris-amoi.com/
---
