---
api_count: 0
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/360leiliang-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/360leiliang-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.360leiliang.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.360leiliang.com/userAgreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.360leiliang.com/privacyPolicy.html
coverage:
  checked: '2026-09-05'
  detail: '360leiliang runs a lace and textile-trim storefront, not a platform: the site has no /developers, /docs or API-reference path (its 200s on /docs, /api-docs, /redoc and /graphql all return the 102,881-byte storefront homepage verbatim), GitHub user and repository search for the name return zero results, no registry carries a client library, and api.360leiliang.com — the private backend for its own web and mobile clients, fronted by an Aliyun ALB and identifying itself as "EZmvc 1.1.9" — 404s every OpenAPI, Swagger, GraphQL and /.well-known/ path probed.'
  evidence:
  - status: 404
    url: https://api.360leiliang.com/openapi.json
  - status: 404
    url: https://api.360leiliang.com/v3/api-docs
  - status: 404
    url: https://api.360leiliang.com/swagger-ui.html
  - status: 404
    url: https://www.360leiliang.com/.well-known/api-catalog
  - status: 404
    url: https://www.360leiliang.com/llms.txt
  - status: 200
    url: https://api.github.com/search/repositories?q=360leiliang
  - status: 200
    url: https://www.360leiliang.com/
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 360leiliang (辅布司 / "Fubusi") is a Chinese S2B self-operated business-to-business e-commerce platform for textile trim and accessories — principally lace, embroidery and knitted narrow fabrics in nylon, polyester, rayon and cotton — sold by the yard to garment manufacturers. The storefront and companion mobile app are owned and operated by 福建东南西北网络科技有限公司 (Fujian Dongnanxibei Network Technology Co., Ltd.) of Mawei District, Fuzhou, Fujian, China; the company was founded in 2014. 360leiliang.com lists per-pattern finished-goods and greige pricing, image-based product lookup, stock and made-to-order availability, and Alipay/WeChat checkout. As of this profile it publishes no public developer program, API documentation, machine-readable contract or SDK; api.360leiliang.com is the private backend for its own clients. It consumes third-party APIs — WeChat login, Alipay, JPush, Vivo/Huawei push — rather than producing one.
image: https://www.360leiliang.com/statics/css/images/logo.png
layout: provider
modified: '2026-09-05'
name: 360leiliang
nav: Providers
network: true
overview: 360leiliang is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Textiles, Lace, Fabric, Apparel, and Manufacturing.
random_paper: 3
security:
- kind: domain-security
  name: 360Leiliang Domain Security
  slug: 360leiliang-domain-security
  summary_line: TLSv1.2
slug: 360leiliang
tags:
- Textiles
- Lace
- Fabric
- Apparel
- Manufacturing
- B2B Marketplace
- E-Commerce
- Supply Chain
- China
- Company
website: https://www.360leiliang.com/
---
