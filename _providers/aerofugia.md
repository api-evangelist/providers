---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aerofugia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aerofugia.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aerofugia.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.aerofugia.com/newslist
coverage:
  checked: '2026-09-10'
  detail: 'Aerofugia builds and will operate eVTOL aircraft, not software products: every URL in its own sitemap.xml (66 of them) is marketing, news, recruitment or a partnership contact form, there is no /developers, /docs or /api path, no GitHub organization exists under the name, and the origin nginx 301-redirects every /api* path to itself so nothing under /api can ever resolve.'
  evidence:
  - status: 200
    url: https://www.aerofugia.com/sitemap.xml
  - status: 404
    url: https://www.aerofugia.com/openapi.json
  - status: 301
    url: https://www.aerofugia.com/api-docs
  - status: 404
    url: https://www.aerofugia.com/.well-known/api-catalog
  - status: 404
    url: https://www.aerofugia.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/aerofugia
  reason: no-developer-program
  state: none
created: '2026-09-10'
description: 'Aerofugia (沃飞长空, Sichuan Aerofugia Technology Development Co., Ltd.) is a Chengdu-based advanced air mobility company founded in 2020 under Zhejiang Geely Holding Group''s Geely Technology Group, focused on the research, certification and commercial operation of low-altitude passenger aircraft. Its flagship product is the AE200 series, a six-seat all-electric piloted eVTOL with a roughly 200 km range aimed at intercity air mobility, low-altitude tourism and emergency medical transport; the AE200 was the first piloted eVTOL type certificate application accepted by the Civil Aviation Administration of China, has completed full tilt-transition flight testing, and the company holds a CCAR-135 air operator certificate. As of this profile Aerofugia publishes no public developer program, API documentation or machine-readable API contract: it is an aircraft manufacturer and future air-mobility operator, not a platform vendor.'
image: https://aerogw.obs.cn-east-3.myhuaweicloud.com/media/logo/02hui2.png
layout: provider
modified: '2026-09-10'
name: Aerofugia
nav: Providers
network: true
overview: 'Aerofugia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, Aerospace, eVTOL, Advanced Air Mobility, and Urban Air Mobility.


  Aerofugia''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 2
security:
- kind: domain-security
  name: Aerofugia Domain Security
  slug: aerofugia-domain-security
  summary_line: TLSv1.3
slug: aerofugia
tags:
- Aviation
- Aerospace
- eVTOL
- Advanced Air Mobility
- Urban Air Mobility
- Electric Aircraft
- Transportation
- Manufacturing
- China
- Company
website: https://www.aerofugia.com/
---
