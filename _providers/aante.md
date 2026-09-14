---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aante-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ant-fa.com/
- group: company
  title: ''
  type: Blog
  url: https://ant-fa.com/notice/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ant-fa.com/notice/notice-detail/44/?id=44
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ant-fa.com/notice/notice-detail/254/?id=254
- group: start
  title: ''
  type: SignUp
  url: https://ant-fa.com/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aante-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/aante-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aante-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: Aante sells factory-automation components through a Chinese-language Nuxt storefront at ant-fa.com and ships no developer surface at all — /openapi.json, /swagger.json and /llms.txt return 404, /graphql, /api-docs, /docs and every /.well-known/ path return the site's 31KB single-page-application HTML shell with HTTP 200, and api./open./developer./ docs./gateway.ant-fa.com are all NXDOMAIN.
  evidence:
  - status: 404
    url: https://ant-fa.com/openapi.json
  - status: 404
    url: https://ant-fa.com/llms.txt
  - status: 404
    url: https://ant-fa.com/.well-known/agent-card.json
  - status: 404
    url: https://ant-fa.com/.well-known/security.txt
  - status: 200
    url: https://ant-fa.com/graphql
  - status: 200
    url: https://ant-fa.com/
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: Aante (爱安特) is a Chinese factory-automation (FA) parts distributor and one-stop industrial e-commerce procurement platform, operated by Aante (Changzhou) Precision Machinery Co., Ltd. (爱安特（常州）精密机械有限公司) and headquartered in Changzhou, Jiangsu. Established in 2002 as the successor to Sandi Automation, it sells linear motion, transmission, standard, machined, framing, motion-unit, electrical and pneumatic components across 96 product categories and roughly two million SKUs, distributing 30+ international brands including SMC and THK alongside its own Aante-branded line. It serves customers in semiconductors, new energy, 3C electronics, photovoltaics, LCD, automotive, medical and food manufacturing from three production bases and 30+ service centers, and in 2026 acquired software firm Zhuiguang Geometry to pair components with design software. The storefront at ant-fa.com is a Chinese-language Nuxt commerce site; no public developer program, API reference, or machine-readable contract
  is published.
image: https://dioguwdgf472v.cloudfront.net/media/logos/equityinvest/Company/aante_logo-55305772a85f0ab3.png
layout: provider
modified: '2026-09-05'
name: Aante
nav: Providers
network: true
overview: 'Aante is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial Automation, Factory Automation, Manufacturing, and Distribution.


  Aante''s developer surface includes engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Aante Plans Pricing
  plan_count: 0
  slug: aante-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Aante Rate Limits
  slug: aante-rate-limits
security:
- kind: domain-security
  name: Aante Domain Security
  slug: aante-domain-security
  summary_line: TLSv1.2 · DMARC
slug: aante
tags:
- Company
- Industrial Automation
- Factory Automation
- Manufacturing
- Distribution
- E-Commerce
- Procurement
- Industrial Components
- China
website: https://ant-fa.com/
---
