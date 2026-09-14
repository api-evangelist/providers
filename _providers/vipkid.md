---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vipkid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vipkid.com/
- group: company
  title: ''
  type: About
  url: https://www.vipkid.com/mkt/about-us
- group: operate
  title: ''
  type: Support
  url: https://www.vipkid.com/mkt/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://www.vipkid.com/mkt/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.vipkid.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vipkid.com/landing/teach-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vipkid.com/landing/teach-privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VIPKID-OpenSource
- group: build
  title: ''
  type: Packages
  url: packages/vipkid-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vipkid-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/vipkid-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vipkid-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/vipkid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vipkid-rate-limits.yml
coverage:
  checked: '2026-09-04'
  detail: VIPKid ships only consumer apps and a teacher portal — there is no developer subdomain at all (developer/docs/developers/openapi .vipkid.com and .vipkid.com.cn all fail to resolve), /openapi.json and /swagger.json return 404 or 502 on all nine VIPKid and VIPTeacher hosts, and every /.well-known/* request on the main domains is 302'd to Akamai's domain-control-validation host rather than answered with a document.
  evidence:
  - status: 404
    url: https://api.vipkid.com/openapi.json
  - status: 502
    url: https://www.vipkid.com/openapi.json
  - status: 302
    url: https://www.vipkid.com/.well-known/security.txt
  - status: 404
    url: https://www.vipteacher.com/.well-known/agent-card.json
  - status: 404
    url: https://open.vipkid.com.cn/swagger.json
  - status: 500
    url: https://blog.vipkid.com/
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: VIPKid (Beijing Dami Technology Co., Ltd. / 北京大米科技有限公司) is an online language-education company founded in 2013 that connects children with English teachers over one-to-one live video lessons, and runs a global teacher-marketplace side (VIPTeacher) alongside consumer learning brands including Lingo Bus, VIPKID AI 双师智学, VIPKID 国际教育 and the Dino parent-child reading rooms. The product is delivered entirely as consumer web and mobile apps and a teacher portal; VIPKid publishes no public developer program, API reference, or machine-readable contract of any kind.
image: https://img.vipkidstatic.com/teacher/FBShare_Image_1200x630.png
layout: provider
modified: '2026-09-04'
name: VIPKid
nav: Providers
network: true
overview: 'VIPKid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online Learning, and Language Learning.


  VIPKid''s developer surface includes support, signup flow, and 13 more developer resources.'
plans:
- name: Vipkid Plans Pricing
  plan_count: 0
  slug: vipkid-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Vipkid Rate Limits
  slug: vipkid-rate-limits
security:
- kind: domain-security
  name: Vipkid Domain Security
  slug: vipkid-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vipkid
tags:
- Company
- Education
- EdTech
- Online Learning
- Language Learning
- English Language Teaching
- Tutoring
- K-12
- Consumer
- China
website: https://www.vipkid.com/
---
