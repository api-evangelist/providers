---
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://career.wingeat.com/
- group: company
  title: ''
  type: About
  url: https://career.wingeat.com/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wingeat-inc
- group: operate
  title: ''
  type: Support
  url: https://www.wingeat.com/cs-center
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.wingeat.com/cs-center/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wingeat.com/term
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wingeat.com/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agreable-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agreable-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agreable-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/agreable-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agreable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agreable-rate-limits.yml
coverage:
  checked: '2026-09-12'
  detail: Agreable (now 주식회사 윙잇 / Wing Eat, Inc.) is a direct-to-consumer frozen-food retailer whose software is entirely internal — api.wingeat.com answers "Cannot GET" on every path, erp.wingeat.com is a private Vercel SPA, and the wingeat-inc GitHub organization has zero public repositories, so there is no developer portal, no specification and no agent surface to profile.
  evidence:
  - status: 404
    url: https://api.wingeat.com/openapi.json
  - status: 404
    url: https://www.wingeat.com/llms.txt
  - status: 404
    url: https://career.wingeat.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/wingeat-inc
  reason: no-developer-program
  state: none
created: '2026-09-12'
description: 'Agreable (아그레아블) is a South Korean direct-to-consumer brand-commerce company founded by Lim Seung-jin (임승진, "Jason Im") out of a reading-club community of the same name. It has run the frozen convenience-food platform Wingeat (윙잇, wingeat.com) since 2015, and in March 2022 renamed itself after that brand — the operating legal entity is now 주식회사 윙잇 (Wing Eat, Inc.) in Guro-gu, Seoul, and agreable.com and agreable.co.kr both redirect to career.wingeat.com. The company designs, contract-manufactures and fulfils its own private-label food brands — 윙잇Dining, 윙잇Made, 고른, 페이보잇, 랠리 and 방아당 — across more than 200 products. It is a consumer packaged-goods and retail operator, not a software vendor: it builds its storefront, ERP and fulfilment systems in house on private hosts and publishes no developer portal, no public API, no SDK, no machine-readable specification and no agent surface of any kind. Its GitHub organization, wingeat-inc, carries zero public repositories.'
image: https://image.wingeat.com/og/images/0d8f505b-654a-4b48-9a68-31866dee9148.png
layout: provider
modified: '2026-09-12'
name: Agreable
nav: Providers
network: true
overview: 'Agreable is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Food and Beverage, and Convenience Food.


  Agreable''s developer surface includes support and 12 more developer resources.'
plans:
- name: Agreable Plans Pricing
  plan_count: 0
  slug: agreable-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Agreable Rate Limits
  slug: agreable-rate-limits
security:
- kind: domain-security
  name: Agreable Domain Security
  slug: agreable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agreable
tags:
- Company
- E-Commerce
- Retail
- Food and Beverage
- Convenience Food
- Consumer Packaged Goods
- Direct to Consumer
- Private Label
- South Korea
website: https://career.wingeat.com/
---
