---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acelerate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://acelerate.io/
- group: start
  title: ''
  type: SignUp
  url: https://app.acelerate.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.acelerate.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.acelerate.io/terms-of-service
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/acelerate
coverage:
  checked: '2026-09-06'
  detail: 'Acelerate ships an end-user restaurant purchasing and virtual-brand SaaS and nothing else: its entire public web presence is the authenticated app at app.acelerate.io, whose own production route manifest has no developer, docs or API-reference route, its retired marketing site never carried one, npm and PyPI hold no first-party package, and every /.well-known/ discovery path returns a true 404.'
  evidence:
  - status: 301
    url: https://acelerate.io/
  - status: 404
    url: https://app.acelerate.io/.well-known/api-catalog
  - status: 404
    url: https://app.acelerate.io/.well-known/agent-card.json
  - status: 404
    url: https://app.acelerate.io/llms.txt
  - status: 403
    url: https://app.acelerate.io/api/v1/openapi.json
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=acelerate
  - status: 200
    url: https://api.github.com/users/acelerate
  reason: no-developer-program
  state: none
created: '2026-09-06'
description: Acelerate (acelerate.io) is a Santa Monica, California restaurant technology company founded in 2019 by former DoorDash operator George Jacobs. It launched as a virtual-brand and host-kitchen platform that let existing restaurants run additional delivery-only brands out of their idle kitchen capacity, and raised a USD 14.44M Series A led by Sequoia Capital in July 2021. The product has since moved up the restaurant supply chain -- the production application at app.acelerate.io covers purchasing from distributors, invoices and rebates, supplier offers, a menu manager, an order manager, sales storefronts, payments and bank accounts. Acelerate publishes no public developer program - no developer portal, API reference, OpenAPI or other machine-readable contract, SDK, webhook catalog or MCP server - and the marketing site that once carried its brand and customer pages has been retired, with acelerate.io now redirecting straight into the authenticated application.
image: https://app.acelerate.io/pwa-icons/192.png
layout: provider
modified: '2026-09-06'
name: Acelerate
nav: Providers
network: true
overview: 'Acelerate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurants, Restaurant Technology, Food Service, Hospitality, and Ghost Kitchens.


  Acelerate''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 10
security:
- kind: domain-security
  name: Acelerate Domain Security
  slug: acelerate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: acelerate
tags:
- Restaurants
- Restaurant Technology
- Food Service
- Hospitality
- Ghost Kitchens
- Supply Chain
- Procurement
- Foodservice Distribution
- SaaS
- United States
- Company
website: https://acelerate.io/
---
