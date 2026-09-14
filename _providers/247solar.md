---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/247solar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://247solar.com/
- group: company
  title: ''
  type: About
  url: https://247solar.com/about/
- group: company
  title: ''
  type: Blog
  url: https://247solar.com/solar-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://247solar.com/feed/
- group: operate
  title: ''
  type: ContactUs
  url: https://247solar.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://247solar.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://247solar.com/privacy-policy/
- group: company
  title: ''
  type: InvestorRelations
  url: https://247solar.com/our-investors/
- group: company
  title: ''
  type: Careers
  url: https://247solar.com/solar-energy-careers/
coverage:
  checked: '2026-09-05'
  detail: 247Solar sells concentrated-solar-power plants, Heat2Power turbines and HeatStore thermal storage as capital equipment and power purchase agreements, so there is no software product to put an API on; the only machine-readable surface on 247solar.com is the stock WordPress core REST API at /wp-json, whose 404 routes are entirely CMS plugin namespaces (Divi, Yoast, Wordfence, Newfold, Contact Form 7) and not a 247Solar product.
  evidence:
  - status: 404
    url: https://247solar.com/openapi.json
  - status: 404
    url: https://247solar.com/.well-known/agent-card.json
  - status: 404
    url: https://247solar.com/llms.txt
  - status: 200
    url: https://247solar.com/wp-json
  - status: 404
    url: https://api.github.com/users/247solar
  - status: 200
    url: https://247solar.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 247Solar, Inc. is a zero-carbon energy technology company with MIT origins that designs and builds modular third-generation concentrated solar power (CSP) systems delivering round-the-clock clean electricity and industrial-grade heat. Its 247Solar Plant couples a high-temperature solar receiver (~970C) with the Heat2Power turbine and HeatStore thermal storage, holding energy in ceramic pellets or ordinary sand for 20+ hours without batteries or molten salts. The company targets mining, microgrids, off-grid and rural electrification, industrial heat, economic development zones, grid support, data centers and green hydrogen, and sells through power purchase agreements as well as equipment. Headquartered in Great Falls, Virginia, 247Solar is a hardware and project-development business; it publishes no public API, developer program or machine-readable specification.
image: https://247solar.com/wp-content/uploads/2021/10/logo.png
layout: provider
modified: '2026-09-05'
name: 247Solar
nav: Providers
network: true
overview: '247Solar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Solar, Concentrated Solar Power, and Renewable Energy.


  247Solar''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 9
security:
- kind: domain-security
  name: 247Solar Domain Security
  slug: 247solar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 247solar
tags:
- Company
- Energy
- Solar
- Concentrated Solar Power
- Renewable Energy
- Thermal Energy Storage
- Clean Technology
- Industrial Heat
- Microgrids
- Green Hydrogen
- Mining
- Climate Tech
website: https://247solar.com/
---
