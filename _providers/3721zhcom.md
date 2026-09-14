---
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/3721zhcom-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/3721zhcom-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/3721zhcom-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.3721zh.com/
- group: company
  title: ''
  type: About
  url: https://www.3721zh.com/aboutUS.html
- group: operate
  title: ''
  type: Support
  url: https://www.3721zh.com/contactUs.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://v.3721zh.com/zhkjgysys.html
- group: company
  title: ''
  type: Careers
  url: https://www.3721zh.com/joinUs.html
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/3721zhcom
coverage:
  checked: '2026-09-05'
  detail: 3721zh.com markets "API接口" (API interfaces) on its own About page as one delivery mode of its merchant SaaS and runs a live first-party gateway at gw.3721zh.com, but publishes no developer portal, reference or spec anywhere; the only route to an integration is the 商户入驻 merchant-onboarding lead form and the 400-720-0000 sales line.
  evidence:
  - status: 200
    url: https://www.3721zh.com/aboutUS.html
  - status: 200
    url: https://www.3721zh.com/merchantEntry.html
  - status: 400
    url: https://gw.3721zh.com/v2/api-docs
  - status: 404
    url: https://www.3721zh.com/openapi.json
  - status: 404
    url: https://www.3721zh.com/.well-known/agent-card.json
  reason: sales-gate
  state: gated
created: '2026-09-05'
description: 3721zh.com is the public domain of 转换商城 (Zhuanhuan Mall / "Conversion Mall"), the local-life private-domain e-commerce platform operated by 转换空间（上海）电子商务有限公司 (Zhuanhuan Space (Shanghai) E-Commerce Co., Ltd.), founded in 2018 and headquartered in Shanghai, China. It bundles a free-to-merchant SaaS with a branded-goods supply chain, fulfilment, and private-domain traffic build-out and agency operation, so catering, property-management, beauty, hotel, foot-bath, tea-house, education and retail-chain merchants can turn in-store spend into equivalent-value goods, vouchers, coupons and memberships. Company materials list WeCom, WeCom communities, WeChat mini programs, API interfaces and private deployment as the delivery modes of that service system. As of the 2026-09-05 probe the company publishes no developer portal, API reference or machine-readable contract; integration is arranged through its onboarding forms and a sales conversation.
image: https://zhkj1-1392913282.cos.ap-shanghai.myqcloud.com/nHelp/zh_logo.png
layout: provider
modified: '2026-09-05'
name: 3721zh.com
nav: Providers
network: true
overview: '3721zh.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, SaaS, and Marketing.


  3721zh.com''s developer surface includes support and 8 more developer resources.'
plans:
- name: 3721Zhcom Plans Pricing
  plan_count: 0
  slug: 3721zhcom-plans-pricing
random_paper: 15
security:
- kind: domain-security
  name: 3721Zhcom Domain Security
  slug: 3721zhcom-domain-security
  summary_line: TLSv1.2 · DMARC
slug: 3721zhcom
tags:
- Company
- E-Commerce
- Retail
- SaaS
- Marketing
- Loyalty
- Supply Chain
- Food and Beverage
- Local Commerce
- Private Domain Traffic
- WeChat Mini Programs
- China
website: https://www.3721zh.com/
---
