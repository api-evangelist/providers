---
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.yuanfudao.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/yuanfudao_stock/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kanyun-inc
- group: auth
  title: ''
  type: Security
  url: https://security.kanyun.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yuanfudao-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://m.yuanfudao.com/native/help/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://m.yuanfudao.com/native/help/service-agreement
- group: operate
  title: ''
  type: Support
  url: https://www.yuanfudao.com/u/feedback
- group: start
  title: ''
  type: Login
  url: https://www.yuanfudao.com/u/
- group: build
  title: ''
  type: Packages
  url: packages/yuanfudao-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yuanfudao-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yuanfudao-domain-security.yml
coverage:
  checked: '2026-09-04'
  detail: 'Yuanfudao ships only consumer learning apps: www.yuanfudao.com returns a marketing site with no developer link, its robots.txt disallows /api/ and /sdk/, the kanyun-inc GitHub org holds 19 repos of general-purpose OSS and internal AI tooling but zero API clients, and all seven /.well-known/ paths 404 on all six Yuanfudao and Kanyun hosts probed.'
  evidence:
  - status: 200
    url: https://www.yuanfudao.com/
  - status: 404
    url: https://www.yuanfudao.com/openapi.json
  - status: 404
    url: https://ape-api.yuanfudao.com/openapi.json
  - status: 404
    url: https://www.yuanfudao.com/.well-known/api-catalog
  - status: 404
    url: https://www.kanyun.com/llms.txt
  - status: 200
    url: https://security.kanyun.com/
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: Yuanfudao (猿辅导) is a Beijing-based online education technology company founded in 2012 and operated under Kanyun Holdings (看云控股集团). Its consumer products include the Yuanfudao tutoring platform, Zebra AI Learning (斑马AI学), Xiaoyuan AI / Xiaoyuan Kousuan (小猿AI / 小猿口算), Xiaoyuan Souti (小猿搜题), Ape Programming (猿编程) and Haitun Zixi (海豚自习), delivering live classes, smart practice and problem-solving analysis to K-12 and preschool learners in China. The company publishes no public developer program, API reference or machine-readable API contract; its visible public engineering surface is the kanyun-inc GitHub organization of open-source libraries and developer tooling, and the Kanyun Security Response Center (YSRC) vulnerability disclosure program at security.kanyun.com.
image: https://yfdpc.fbcontent.cn/s/logo-563d697805.svg
layout: provider
modified: '2026-09-04'
name: Yuanfudao
nav: Providers
network: true
overview: 'Yuanfudao is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online Learning, and Tutoring.


  Yuanfudao''s developer surface includes support and 11 more developer resources.'
plans:
- name: Yuanfudao Plans Pricing
  plan_count: 0
  slug: yuanfudao-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Yuanfudao Rate Limits
  slug: yuanfudao-rate-limits
security:
- kind: domain-security
  name: Yuanfudao Domain Security
  slug: yuanfudao-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Yuanfudao Vulnerability Disclosure
  slug: yuanfudao-vulnerability-disclosure
  summary_line: contact published
slug: yuanfudao
tags:
- Company
- Education
- EdTech
- Online Learning
- Tutoring
- Artificial Intelligence
- Mobile Applications
- China
website: https://www.yuanfudao.com/
---
