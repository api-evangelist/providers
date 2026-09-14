---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://zunum.aero/
- group: company
  title: ''
  type: Blog
  url: https://zunum.aero/in-the-news/
- group: company
  title: ''
  type: BlogRSS
  url: https://zunum.aero/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/3679319/
- group: other
  title: ''
  type: X
  url: https://twitter.com/zunumaero
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zunum-aero-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zunum-aero-llms.txt
coverage:
  checked: '2026-09-05'
  detail: Zunum Aero builds hybrid-electric regional aircraft; zunum.aero is a WordPress marketing and press site whose only machine-readable surfaces are the stock WordPress CMS endpoint at /wp-json and an RSS feed, and every developer-facing path probed (/openapi.json, /swagger.json, /api-docs, /docs, /graphql, /llms.txt and the /.well-known/ set) returns 404.
  evidence:
  - status: 200
    url: https://zunum.aero/
  - status: 404
    url: https://zunum.aero/openapi.json
  - status: 404
    url: https://zunum.aero/.well-known/security.txt
  - status: 404
    url: https://zunum.aero/llms.txt
  - status: 404
    url: https://zunum.aero/docs
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 'Zunum Aero is an American aerospace company founded in 2013 and based in the Seattle area (Kirkland / Bothell, Washington) that set out to build hybrid-to-electric regional aircraft. Its ZA10 program targeted a six-to-twelve-seat hybrid-electric airplane with a 700-nautical-mile range, aimed at reviving short-haul point-to-point air travel from secondary airports, and it was backed by Boeing HorizonX and JetBlue Technology Ventures. The company laid off nearly all of its staff in late 2018 and paused operations, and it later pursued trade-secret litigation against Boeing. Zunum Aero is an aircraft manufacturer, not a software vendor: its public web presence is a marketing and press site with no developer program, no developer portal, no documentation, and no published machine-readable API contract of any kind.'
image: https://zunum.aero/wp-content/uploads/2017/03/zunum-aero-logo.png
layout: provider
modified: '2026-09-05'
name: Zunum Aero
nav: Providers
network: true
overview: 'Zunum Aero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Aviation, Aircraft Manufacturing, and Electric Aviation.


  Zunum Aero''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 14
security:
- kind: domain-security
  name: Zunum Aero Domain Security
  slug: zunum-aero-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zunum-aero
tags:
- Company
- Aerospace
- Aviation
- Aircraft Manufacturing
- Electric Aviation
- Hybrid Electric Propulsion
- Regional Air Travel
- Transportation
- Hardware
- Startups
website: https://zunum.aero/
---
