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
- group: company
  title: ''
  type: Website
  url: https://www.eargo.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://lxehearing.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@eargo.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.eargo.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/eargo/refs/heads/main/llms/eargo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eargo-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/eargo/refs/heads/main/security/eargo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eargo-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/eargo/refs/heads/main/lifecycle/eargo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/eargo-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/eargo/refs/heads/main/packages/eargo-packages.yml
  title: ''
  type: Packages
  url: packages/eargo-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/eargo/refs/heads/main/plans/eargo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eargo-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/eargo/refs/heads/main/rate-limits/eargo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/eargo-rate-limits.yml
coverage:
  checked: '2026-08-12'
  detail: 'Round two enumerated eargo.com by DNS and found four hosts the first pass missed — app.eargo.com still serves a live Rails "Eargo Web App" storefront and help.eargo.com serves a real 16.6KB llms.txt of 106 consumer support articles — but there is still no API anywhere: api.eargo.com answers 403 on /openapi.json, /swagger.json, /api-docs and /graphql behind a Cloudflare bot challenge, and every other host is a soft-404 shell or an unreachable retired storefront.'
  evidence:
  - status: 200
    url: https://help.eargo.com/llms.txt
  - status: 200
    url: https://app.eargo.com/
  - status: 403
    url: https://api.eargo.com/openapi.json
  - status: 403
    url: https://api.eargo.com/graphql
  - status: 200
    url: https://www.eargo.com/
  - status: 301
    url: https://shop.eargo.com/
  - status: 0
    url: https://store.eargo.com/
  - status: 0
    url: https://developer.eargo.com/
  - status: 404
    url: https://api.github.com/orgs/eargo
  reason: defunct
  state: none
created: '2026-08-12'
description: 'Eargo was a San Jose, California direct-to-consumer medical device company that designed and sold rechargeable, virtually invisible in-canal hearing aids for adults with mild to moderate hearing loss, founded in 2010 as Aria Innovations and listed on Nasdaq in 2020. In 2025 Eargo merged with South Africa''s hearX Group to form LXE Hearing, combining Eargo''s direct-to-consumer platform with the Lexie and Go Hearing over-the-counter brands. In 2026 LXE Hearing began winding down its US operations after restructuring efforts failed, and the eargo.com website has been reduced to a single wind-down notice page. Eargo never operated a public developer program, developer portal, or documented API: the hearing aids paired with a consumer mobile application backed by a private, undocumented service host at api.eargo.com.'
image: https://www.eargo.com/assets/content/dam/eargo/samples/logo_white.png
layout: provider
modified: '2026-09-15'
name: Eargo
nav: Providers
network: true
overview: 'Eargo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hearing Aids, Medical Devices, Consumer Health, and Direct to Consumer.


  Eargo''s developer surface includes support and 9 more developer resources.'
plans:
- name: Eargo Plans Pricing
  plan_count: 0
  slug: eargo-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Eargo Rate Limits
  slug: eargo-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/eargo/refs/heads/main/screenshots/eargo-2026-09-02T145316.png
security:
- kind: domain-security
  name: Eargo Domain Security
  slug: eargo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eargo
tags:
- Company
- Hearing Aids
- Medical Devices
- Consumer Health
- Direct to Consumer
- Hearing Health
- Digital Health
- Defunct
website: https://www.eargo.com/
---
