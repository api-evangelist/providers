---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planetspark-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.planetspark.in/
- group: company
  title: ''
  type: Blog
  url: https://www.planetspark.in/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.planetspark.in/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.planetspark.in/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.planetspark.in/privacy
- group: start
  title: ''
  type: Login
  url: https://www.planetspark.in/account/sign_in
- group: commercial
  title: ''
  type: Plans
  url: plans/planetspark-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/planetspark-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/planetspark-llms.txt
coverage:
  checked: '2026-08-26'
  detail: PlanetSpark sells live 1:1 tutoring subscriptions direct to parents and has no developer programme at all — /developers, /api, /openapi.json, /graphql and every /.well-known/ path 404 on both www.planetspark.in and the wildcard api.planetspark.in, which answers with the same marketing SPA rather than an API.
  evidence:
  - status: 404
    url: https://www.planetspark.in/developers
  - status: 404
    url: https://www.planetspark.in/openapi.json
  - status: 404
    url: https://api.planetspark.in/openapi.json
  - status: 404
    url: https://www.planetspark.in/.well-known/agent-card.json
  - status: 404
    url: https://api.planetspark.in/graphql
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: PlanetSpark is an Indian education-technology company headquartered in Gurugram, founded in 2017 by Kunal Malik and Maneesh Dhooper, that delivers live 1:1 online classes in public speaking, spoken English, creative writing, grammar, debating and vlogging to K-8 learners, along with mental and Vedic mathematics, abacus and school-excellence programmes, plus communication courses for working professionals. It sells directly to parents and learners through www.planetspark.in as a consumer subscription; it operates no public developer programme, publishes no API documentation or machine-readable contract, and its only external integration surface is an affiliate registration programme.
image: https://cdn.planetspark.in/images/planetspark-logo-po.png
layout: provider
modified: '2026-08-26'
name: PlanetSpark
nav: Providers
network: true
overview: 'PlanetSpark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online Learning, and Tutoring.


  PlanetSpark''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Planetspark Plans Pricing
  plan_count: 0
  slug: planetspark-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Planetspark Rate Limits
  slug: planetspark-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/planetspark/refs/heads/main/screenshots/planetspark-2026-09-02T151412.png
security:
- kind: domain-security
  name: Planetspark Domain Security
  slug: planetspark-domain-security
  summary_line: TLSv1.3 · DMARC
slug: planetspark
tags:
- Company
- Education
- EdTech
- Online Learning
- Tutoring
- Public Speaking
- English Language
- Mathematics
- Consumer
- India
website: https://www.planetspark.in/
---
