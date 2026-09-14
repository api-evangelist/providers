---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jinsheng-new-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zqjs.cn/
- group: company
  title: ''
  type: About
  url: https://www.zqjs.cn/about.html
- group: other
  title: ''
  type: Products
  url: https://www.zqjs.cn/product.html
- group: company
  title: ''
  type: News
  url: https://www.zqjs.cn/news.html
- group: operate
  title: ''
  type: Contact
  url: https://www.zqjs.cn/contact.html
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/jinsheng-new-energy-stock
coverage:
  checked: '2026-08-23'
  detail: Jinsheng New Energy is a lithium-battery recycling and cathode-materials manufacturer; its only web property is a Chinese corporate CMS site (about / products / news / contact, no developer section), and every REST, GraphQL, MCP and A2A discovery path probed on www.zqjs.cn returned the same 3,679-byte CMS catch-all HTML page rather than a spec.
  evidence:
  - status: 200
    url: https://www.zqjs.cn/openapi.json
  - status: 200
    url: https://www.zqjs.cn/swagger.json
  - status: 200
    url: https://www.zqjs.cn/graphql
  - status: 404
    url: https://www.zqjs.cn/.well-known/agent-card.json
  - status: 404
    url: https://www.zqjs.cn/.well-known/api-catalog
  - status: 403
    url: https://en.zqjs.cn/
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'Guangdong Jinsheng New Energy Co., Ltd. (广东金晟新能源股份有限公司) is a Chinese lithium-battery recycling and materials company headquartered in Zhaoqing, Guangdong, founded in 2010 and originally focused on nickel sulfate production. It operates a closed-loop "urban mine" business: harmless treatment, echelon (second-life) use and hydrometallurgical regeneration of retired lithium-ion batteries into battery-grade nickel sulfate, cobalt sulfate, manganese sulfate and lithium carbonate, plus ternary and iron-phosphate precursors and LFP cathode material, and downstream cells for light mobility, commercial and industrial storage, outdoor power stations and solar street lighting. Production is split across Zhaoqing (Gaoyao) in Guangdong and Yichun/Ganzhou in Jiangxi through the wholly owned subsidiary Jiangxi Ruida New Energy Technology, with approved processing capacity of about 204,000 tonnes of spent lithium battery per year. Both the parent and Jiangxi Ruida appear on MIIT''s echelon-use
  and regeneration white lists. The company completed a Series C, is a Hurun and Forbes unicorn-list member, and has pursued a public listing. It is an industrial materials manufacturer and publishes no developer program, API, or machine-readable API contract of any kind.'
image: https://www.zqjs.cn/upload/sysconfigs/2024-03/6602168302365.png
layout: provider
modified: '2026-08-23'
name: Jinsheng New Energy
nav: Providers
network: true
overview: 'Jinsheng New Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Batteries, Lithium-Ion, and Recycling.


  Jinsheng New Energy''s developer surface includes product news and 6 more developer resources.'
random_paper: 13
security:
- kind: domain-security
  name: Jinsheng New Energy Domain Security
  slug: jinsheng-new-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: jinsheng-new-energy
tags:
- Company
- Energy
- Batteries
- Lithium-Ion
- Recycling
- Circular Economy
- Materials
- Manufacturing
- Electric Vehicles
- Energy Storage
- China
website: https://www.zqjs.cn/
---
