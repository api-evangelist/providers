---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/advancechip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.advancechip.com/
- group: company
  title: ''
  type: WebsiteEnglish
  url: http://en.advancechip.com/
- group: operate
  title: ''
  type: Support
  url: http://en.advancechip.com/technology/technology
- group: other
  title: ''
  type: Downloads
  url: http://en.advancechip.com/download/download
- group: build
  title: ''
  type: DevelopmentTools
  url: http://en.advancechip.com/development/development
- group: company
  title: ''
  type: News
  url: http://en.advancechip.com/news/news
- group: company
  title: ''
  type: Careers
  url: http://en.advancechip.com/join/job
- group: operate
  title: ''
  type: ContactUs
  url: http://en.advancechip.com/cont/contect
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/advancechip/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/advancechip-llms.txt
coverage:
  checked: '2026-09-07'
  detail: Advancechip is a Changsha fabless DSP chip designer whose entire developer surface is silicon and hardware — its "Development tools" page lists evaluation boards and its "Download materials" page serves chip data manuals as PDFs from a bare-IP file host (http://42.48.83.242:25662/), with no API, no developer portal and no machine-readable contract anywhere on the domain; the only JSON endpoint the site touches is its web agency's multi-tenant CMS backend at jxdzkj.api.hnjwglobal.com, which is not an Advancechip product and rejects off-domain callers with {"StatusCode":408,"Message":"访问域名无效"}.
  evidence:
  - status: 200
    url: http://en.advancechip.com/development/development
  - status: 200
    url: http://en.advancechip.com/download/download
  - status: 404
    url: http://www.advancechip.com/openapi.json
  - status: 404
    url: http://www.advancechip.com/.well-known/api-catalog
  - status: 404
    url: http://www.advancechip.com/llms.txt
  - status: 200
    url: https://jxdzkj.api.hnjwglobal.com/
  - status: 404
    url: https://api.github.com/users/advancechip
  reason: no-developer-program
  state: none
created: '2026-09-07'
description: 'Advancechip Technology (Hunan) Co., Ltd. — 进芯科技（湖南）股份有限公司, formerly Hunan Jinxin Electronic Technology Co., Ltd. — is a fabless integrated-circuit design company founded in October 2012 and headquartered in Changsha, Hunan, China. It develops digital signal processor (DSP) chips and embedded solutions, and states that it has taken three DSP families to mass production: 16-bit fixed-point (ADP16), 32-bit fixed-point (ADP32) and 32-bit floating-point (AVP32), alongside single-core and multi-core SoC parts such as the ADM32F036 motor-control family. The company describes its core technologies as DSP core design, compilation technology, large-scale SoC digital integration and core drive algorithms, held as a fully independent intellectual-property stack, and targets automotive electronics, thermal management, smart home and white goods, small household appliances, health equipment and power tools. Its developer-facing surface is hardware, not web software: evaluation and development
  boards (AVP32F379QP176, AVP32F00157QP80, AVP32F0039QP100S, ADM32F036A5Q/A6Q/A7Q low-voltage motor boards), a technical-support page and a download section that serves chip data manuals as PDFs from a third-party file host. As probed on 2026-09-07 Advancechip publishes no public web API, no developer portal or API reference, no OpenAPI/AsyncAPI/GraphQL contract, no SDK in any public package registry, no GitHub organization and no /.well-known documents; the corporate site itself is served over plaintext HTTP only.'
image: https://oss-usa.jingwxcx.com/jxdzkj/upload_files/2025/10/14/9d78c00f818c49a3a65c1ff0f8d3830e.png
layout: provider
modified: '2026-09-07'
name: Advancechip Technology (Hunan) Co., Ltd.
nav: Providers
network: true
overview: 'Advancechip Technology (Hunan) Co., Ltd. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Integrated Circuits, Digital Signal Processing, and Embedded Systems.


  Advancechip Technology (Hunan) Co., Ltd.''s developer surface includes support, product news, and 9 more developer resources.'
random_paper: 8
security:
- kind: domain-security
  name: Advancechip Domain Security
  slug: advancechip-domain-security
  summary_line: DMARC
slug: advancechip
tags:
- Company
- Semiconductors
- Integrated Circuits
- Digital Signal Processing
- Embedded Systems
- System On Chip
- Automotive Electronics
- Motor Control
- Industrial Control
- Hardware
- China
website: http://www.advancechip.com/
---
