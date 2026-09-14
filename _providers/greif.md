---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://www.greif.com/wp-json
  baseurl_source: declared
  description: The WordPress REST API served by Greif's corporate website at https://www.greif.com/wp-json — 554 routes across 39 namespaces, 182 of them under wp/v2, discovered by probing the API host root on 2026-
  name: Greif WordPress REST API
  slug: greif-wordpress-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greif-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greif
- group: company
  title: ''
  type: Website
  url: https://www.greif.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/greif-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/greif-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/greif-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/greif-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/greif-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/greif-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/greif-mcp.yml
- group: agent
  title: ''
  type: x-well-known-probe
  url: well-known/greif-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/greif-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/greif-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/greif-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/greif-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.greif.com/category/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.greif.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.greif.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greif.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greif.com/privacy-policy/
- group: start
  title: ''
  type: x-customer-portal
  url: https://www.greif.com/greif-plus/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCFa1IzCyPcTp-ckGTcIMwNw
created: '2026-03-24'
description: Greif is an industrial packaging products and services leader with a vision to be the best performing customer service company in the world. Greif also offers digital tools such as the Greif Green Tool carbon footprint calculator and the Greif+ online platform for customers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greif.png
layout: provider
modified: '2026-09-12'
name: Greif
nav: Providers
network: true
overview: 'Greif publishes 1 API on the [APIs.io](https://apis.io/) network: WordPress REST API. Tagged areas include Packaging, Industrial, Manufacturing, Sustainability, and Fortune 1000.


  Greif''s developer surface includes authentication, engineering blog, support, YouTube channel, and 19 more developer resources.'
plans:
- name: Greif Plans Pricing
  plan_count: 0
  slug: greif-plans-pricing
press:
- date: '2026-05-25'
  title: Greif Inc. Acquires Reliance Products Ltd.
  url: https://www.prnewswire.com/news-releases/greif-inc-acquires-reliance-products-ltd-301943699.html
- date: '2026-05-25'
  title: Mayer Brown Advises Packaging Corporation Of America On ...
  url: https://www.mondaq.com/pressrelease/169358/mayer-brown-advises-packaging-corporation-of-america-on-%2418-billion-acquisition-of-greif-incs-containerboard-business
- date: '2026-05-25'
  title: Automation & Digital Technology
  url: https://www.greif.com/sustainability-2024/sustainability-strategies/addressing-risk/automation-digital-technology/
- date: '2026-05-25'
  title: Mayer Brown advises Packaging Corporation of America ...
  url: https://www.mayerbrown.com/en/news/2025/07/mayer-brown-advises-packaging-corporation-of-america-on-18-billion-acquisition-of-greif-incs-containerboard-business
- date: '2026-05-25'
  title: Greif Inc. Class A (GEF) reports earnings - Quartz
  url: https://qz.com/greif-inc-class-a-gef-reports-earnings-1851727534
random_paper: 0
rate_limits:
- limit_count: 0
  name: Greif Rate Limits
  slug: greif-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/greif/refs/heads/main/screenshots/greif-2026-06-20T182402.png
security:
- kind: authentication
  name: Greif Authentication
  slug: greif-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Greif Domain Security
  slug: greif-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: greif
tags:
- Packaging
- Industrial
- Manufacturing
- Sustainability
- Fortune 1000
website: https://www.greif.com
---
