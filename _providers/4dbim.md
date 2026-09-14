---
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
