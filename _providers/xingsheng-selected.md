---
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
