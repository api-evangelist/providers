---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/21gram-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://21gram.co.kr/
- group: operate
  title: ''
  type: Support
  url: https://21gram.co.kr/customercenter
- group: operate
  title: ''
  type: FAQ
  url: https://21gram.co.kr/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://21gram.co.kr/pricing
- group: company
  title: ''
  type: Blog
  url: https://21gram.co.kr/notice
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/21gram-llms.yml
coverage:
  checked: '2026-09-05'
  detail: 21gram is a Korean pet funeral operator whose only digital product is a consumer booking and consultation site built on the hosted imweb site builder; its 138-URL sitemap contains no developer, API or docs page, the api./developer./docs. subdomains do not resolve, and every named /.well-known/, /openapi.json and /apis.json path 404s.
  evidence:
  - status: 200
    url: https://21gram.co.kr/sitemap.xml
  - status: 404
    url: https://21gram.co.kr/openapi.json
  - status: 404
    url: https://21gram.co.kr/.well-known/api-catalog
  - status: 200
    url: https://21gram.co.kr/llms.txt
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 21gram (21그램) is a South Korean pet end-of-life care company that operates pet funeral homes and an online booking and consultation platform for pet funerals. Founded in Seoul and led by Kwon Shin-gu, it began as an online brokerage letting owners find licensed pet funeral homes nationwide and book a service with 24-hour consultation, reservation and payment, then moved into operating its own facilities — acquiring Korea's first pet funeral hall, Arongi Cheonguk, in Gwangju, Gyeonggi Province — and now runs branches including Gwangju, Namyangju and Cheonan plus a large charnel house. Its consumer surface covers funeral procedures and pricing, cremation, memorial jewelry, hearse and non-attending funeral options, urns, flowers, temporary storage and scattering, and grief-support classes. It is venture-backed and trades on secondary markets. It publishes no developer program, API documentation, or machine-readable API contract; its website runs on the hosted imweb site builder.
image: https://cdn.imweb.me/upload/S202007224b857e097fd31/ebc3471148994.png
layout: provider
modified: '2026-09-05'
name: 21gram
nav: Providers
network: true
overview: '21gram is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pet Care, Pet Loss, Funeral Services, and Consumer Services.


  21gram''s developer surface includes support, FAQ, pricing, engineering blog, and 3 more developer resources.'
plans:
- name: 21Gram Plans Pricing
  plan_count: 0
  slug: 21gram-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: 21Gram Rate Limits
  slug: 21gram-rate-limits
security:
- kind: domain-security
  name: 21Gram Domain Security
  slug: 21gram-domain-security
  summary_line: TLSv1.3
slug: 21gram
tags:
- Company
- Pet Care
- Pet Loss
- Funeral Services
- Consumer Services
- Booking
- Marketplace
- South Korea
website: https://21gram.co.kr/
---
