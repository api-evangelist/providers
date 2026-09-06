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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: http://www.4dbim.ren/zh
- group: operate
  title: ''
  type: Support
  url: http://www.4dbim.ren/zh/about/contact
- group: company
  title: ''
  type: Blog
  url: http://www.4dbim.ren/zh/news
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4dbim-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4dbim-llms.txt
coverage:
  checked: '2026-09-05'
  detail: The 4DBIM Cloud product page markets an "API开放平台" (API open platform) as a platform capability but links to no reference and no specification, and the site has no /docs, /developers, /pricing, login or sign-up path at all — the only route offered anywhere on www.4dbim.ren is the business-cooperation address market@4dbim.ren on the contact page.
  evidence:
  - status: 200
    url: http://www.4dbim.ren/zh/products/cloud
  - status: 200
    url: http://www.4dbim.ren/zh/about/contact
  - status: 404
    url: http://www.4dbim.ren/openapi.json
  - status: 404
    url: http://www.4dbim.ren/swagger.json
  - status: 404
    url: http://www.4dbim.ren/api-docs
  - status: 404
    url: http://www.4dbim.ren/.well-known/api-catalog
  - status: 404
    url: http://www.4dbim.ren/.well-known/agent-card.json
  - status: 404
    url: http://www.4dbim.ren/llms.txt
  - status: 403
    url: http://www.4dbim.cn/.well-known/api-catalog
  reason: sales-gate
  state: gated
created: '2026-09-05'
description: 4DBIM is the product brand of Beijing Yunjianxin Technology Co., Ltd. (北京云建信科技有限公司), a Beijing construction-technology company founded in 2015 that commercializes Tsinghua University 4D-BIM and BIM-FM research as a full-lifecycle Building Information Modeling platform for infrastructure. Its 4DBIM Cloud data centre combines a lightweight BIM+GIS graphics engine, multi-source model fusion and IoT ingestion on a microservice architecture, packaged as Power4D (construction management), Wonder4D (operations and maintenance), Skill4D (3D work instructions) and Smart4D (smart precast beam yards), plus a BIM consulting practice. It targets municipal and "national lifeline" infrastructure — metro, bridge, highway, tunnel and utility corridors — and has raised about USD 13.7M through a Series B. The 4DBIM Cloud page markets an "API开放平台" (API open platform), but 4DBIM publishes no developer portal, API reference or machine-readable contract, and www.4dbim.ren is an HTTP-only marketing
  site.
image: http://www.4dbim.ren/images/logo.png
layout: provider
modified: '2026-09-05'
name: 4DBIM
nav: Providers
network: true
overview: '4DBIM is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Construction, Construction Technology, Building Information Modeling, and BIM.


  4DBIM''s developer surface includes support, engineering blog, and 3 more developer resources.'
plans:
- name: 4Dbim Plans Pricing
  plan_count: 0
  slug: 4dbim-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: 4Dbim Rate Limits
  slug: 4dbim-rate-limits
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 6.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 4Dbim Domain Security
  slug: 4dbim-domain-security
  summary_line: no transport/DNS hardening detected
slug: 4dbim
tags:
- Company
- Construction
- Construction Technology
- Building Information Modeling
- BIM
- Digital Twin
- Infrastructure
- Engineering
- Internet of Things
- SaaS
- China
website: http://www.4dbim.ren/zh
---
