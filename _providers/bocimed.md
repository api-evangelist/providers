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
  url: security/bocimed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.bocimed.com/
- group: company
  title: ''
  type: WebsiteEnglish
  url: http://en.bocimed.com/
- group: company
  title: ''
  type: About
  url: http://en.bocimed.com/index.php/List/2.html
- group: other
  title: ''
  type: Services
  url: http://en.bocimed.com/index.php/List/3.html
- group: company
  title: ''
  type: Blog
  url: http://en.bocimed.com/index.php/List/5.html
- group: operate
  title: ''
  type: Support
  url: http://en.bocimed.com/index.php/List/6.html
- group: company
  title: ''
  type: Careers
  url: http://en.bocimed.com/index.php/List/29.html
coverage:
  checked: '2026-08-08'
  detail: BociMed is a Shanghai pharmaceutical CRO/CDMO selling lab, drug-delivery, clinical and manufacturing services; its only web presence is a ThinkPHP marketing site in Chinese and English with no developer, API or documentation section, and every contract-discovery path (/openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt, /.well-known/*) returns a hard 404 on both hosts.
  evidence:
  - status: 200
    url: http://www.bocimed.com/
  - status: 200
    url: http://en.bocimed.com/
  - status: 404
    url: http://www.bocimed.com/openapi.json
  - status: 404
    url: http://en.bocimed.com/openapi.json
  - status: 404
    url: http://en.bocimed.com/.well-known/agent-card.json
  - status: 404
    url: http://en.bocimed.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/bocimed
  reason: not-a-software-company
  state: none
created: '2026-08-08'
description: 'Shanghai BociMed Pharmaceutical Research Co., Ltd. (上海博志研新药物研究有限公司) is a Chinese pharmaceutical CRO/CDMO founded in 2012 in the Zhangjiang Pharmaceutical Valley, Shanghai, with an R&D headquarters in Zhangjiang, a production base in Lingang, and a clinical subsidiary in Chengdu. BociMed offers small-molecule chemistry, CMC and process development, a portfolio of drug delivery technology platforms (oral, injectable, nasal, pulmonary, transdermal, ocular, implant, liposome and exosome), clinical research and SMO services, global regulatory registration consulting, and commercial API, intermediate and solid-dosage manufacturing. It is a laboratory and manufacturing services business rather than a software vendor: it publishes a marketing website in Chinese and English and no developer program, public API, SDK or machine-readable specification of any kind.'
layout: provider
modified: '2026-08-08'
name: BociMed
nav: Providers
network: true
overview: 'BociMed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Life Sciences, Contract Research Organization, and CDMO.


  BociMed''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/bocimed/refs/heads/main/screenshots/bocimed-2026-09-02T144932.png
security:
- kind: domain-security
  name: Bocimed Domain Security
  slug: bocimed-domain-security
  summary_line: no transport/DNS hardening detected
slug: bocimed
tags:
- Company
- Pharmaceuticals
- Life Sciences
- Contract Research Organization
- CDMO
- Drug Delivery
- Clinical Research
- Manufacturing
- China
- Shanghai
website: http://www.bocimed.com/
---
