---
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agrourbana-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/agrourbana-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/agrourbana-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agrourbana-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.agrourbana.ag/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agrourbana.ag/terminos-y-condiciones
- group: operate
  title: ''
  type: ContactUs
  url: https://www.agrourbana.ag/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://cl.linkedin.com/company/agrourbana
- group: other
  title: ''
  type: x-SecondaryMarket
  url: https://equityzen.com/company/agrourbana
coverage:
  checked: '2026-09-13'
  detail: 'AgroUrbana sells physical produce, not software: its only public digital surface is the Urban Rabbit consumer storefront on the hosted Bootic platform, whose own product, cart and customer routes now 404, and no developer portal, API host, OpenAPI document or .well-known document exists on agrourbana.ag, www.agrourbana.ag or agrourbana.cl.'
  evidence:
  - status: 200
    url: https://www.agrourbana.ag/
  - status: 404
    url: https://agrourbana.ag/openapi.json
  - status: 404
    url: https://agrourbana.ag/.well-known/security.txt
  - status: 404
    url: https://www.agrourbana.ag/docs
  - status: 404
    url: https://api.github.com/orgs/agrourbana
  reason: not-a-software-company
  state: none
created: '2026-09-13'
description: AgroUrbana SpA is a Chilean vertical-farming company founded in 2018 in Santiago by Pablo Bunster and Cristian Sjogren, and widely described as the first commercial vertical farm in Latin America. It runs climate-controlled indoor grow facilities combining hydroponics, spectrum-programmed LED lighting, renewable energy, automation and data analytics to produce leafy greens year round, reporting up to twelve growing cycles a year and up to 95% less water use than open-field agriculture. Produce is sold to Chilean retailers including Cencosud and Walmart Chile, and direct to consumers under the Urban Rabbit brand through a hosted online store. The company has raised roughly USD 12 million, including a USD 4 million Series A led by Kayyak Ventures and a USD 6 million pre-Series B led by ALB Inversiones. AgroUrbana operates its technology internally to run its own farms and publishes no public API, SDK, developer portal or machine-readable API contract.
image: https://static.bolder.run/23001/logo/original/logo-logo-UR_AU-para-notificacionepurp.png
layout: provider
modified: '2026-09-13'
name: AgroUrbana
nav: Providers
network: true
overview: AgroUrbana is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Vertical Farming, and Food and Beverage.
plans:
- name: Agrourbana Plans Pricing
  plan_count: 0
  slug: agrourbana-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Agrourbana Rate Limits
  slug: agrourbana-rate-limits
security:
- kind: domain-security
  name: Agrourbana Domain Security
  slug: agrourbana-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agrourbana
tags:
- Company
- Agriculture
- AgTech
- Vertical Farming
- Food and Beverage
- Controlled Environment Agriculture
- Chile
- Latin America
- Sustainability
website: https://www.agrourbana.ag/
---
