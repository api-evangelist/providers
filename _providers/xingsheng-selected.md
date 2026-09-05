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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xingsheng-selected-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/xingsheng-selected-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xingsheng-selected-llms.txt
- group: company
  title: ''
  type: Website
  url: https://xsyxsc.com/
coverage:
  checked: '2026-09-04'
  detail: Xingsheng Selected sells groceries to consumers and onboards suppliers, stores and service managers through web forms and a hotline — xsyxsc.com carries no developer section, its supplier system at gys.xsyxsc.com is a login-walled internal app, and its live application backend mall.xsyxsc.com answers every conventional specification path (/v3/api-docs, /openapi.json, /swagger.json, /api-docs, /swagger-resources, /doc.html, /actuator) with a Spring Boot JSON 404, so there is no published contract, portal or .well-known document anywhere on the estate — the only public code it ships is the @xsyx npm scope of internal front-end libraries, last released 2021-03-11, which are not clients for any API.
  evidence:
  - status: 200
    url: https://xsyxsc.com/
  - status: 404
    url: https://mall.xsyxsc.com/v3/api-docs
  - status: 404
    url: https://mall.xsyxsc.com/openapi.json
  - status: 404
    url: https://mall.xsyxsc.com/.well-known/api-catalog
  - status: 404
    url: https://api.github.com/orgs/xsyx
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: 'Xingsheng Selected (兴盛优选, Hunan Xingsheng Youxuan E-Commerce Co., Ltd.) is a Changsha, Hunan-based Chinese community group-buying platform, grown out of the Furong Xingsheng convenience-store chain and built on a "pre-sale plus self-pickup" model: consumers order groceries and daily necessities online by 23:00 and collect them the next morning from a neighborhood convenience store acting as a pickup point, supplied through the company''s own central-warehouse, grid-station and store logistics network. It has raised roughly USD 5.4B from investors including Tencent, KKR, Primavera Capital, Temasek and Ontario Teachers'' Pension Plan, and has contracted out of loss-making provinces since 2022. Xingsheng Selected operates no developer program: probing found no portal, documentation, OpenAPI, webhook or .well-known document on any host it controls, and its supplier system is login-walled.'
image: https://front-xps-cdn.xsyx.xyz/custom/xsyx_protal/icon.png
layout: provider
modified: '2026-09-04'
name: Xingsheng Selected
nav: Providers
network: true
overview: Xingsheng Selected is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Grocery, and Community Group Buying.
random_paper: 9
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Xingsheng Selected Domain Security
  slug: xingsheng-selected-domain-security
  summary_line: TLSv1.2
slug: xingsheng-selected
tags:
- Company
- E-Commerce
- Retail
- Grocery
- Community Group Buying
- Logistics
- Consumer
- China
website: https://xsyxsc.com/
---
