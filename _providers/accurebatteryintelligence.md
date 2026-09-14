---
api_count: 1
apis:
- description: 'The authenticated API gateway behind the ACCURE battery analytics platform. Established by probe, not by documentation: the platform single-page application at accure-platform.com declares VITE_AUTH0_'
  name: ACCURE Battery Intelligence Platform API
  slug: accurebatteryintelligence-platform
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/accurebatteryintelligence-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.accure.net/
- group: company
  title: ''
  type: Blog
  url: https://www.accure.net/company/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.accure.net/company/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accure.net/privacy
- group: start
  title: ''
  type: Login
  url: https://accure-platform.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/accurebatteryintelligence-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/accurebatteryintelligence-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/accurebatteryintelligence-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/accurebatteryintelligence-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/accurebatteryintelligence-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/accurebatteryintelligence-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/accurebatteryintelligence-llms.txt
coverage:
  checked: '2026-09-06'
  detail: ACCURE's only API is the gateway behind its customer platform — accure-platform.com is an Auth0-protected SPA and its gateway at gateway.accure-platform.com answers every anonymous request with an nginx 403 or a Fastify JSON 404 — and there is no developer portal, reference or spec anywhere on accure.net, whose 216-URL sitemap contains no developer, API, docs or pricing page at all.
  evidence:
  - status: 403
    url: https://gateway.accure-platform.com/openapi.json
  - status: 404
    url: https://gateway.accure-platform.com/swagger.json
  - status: 200
    url: https://accure-platform.com/
  - status: 200
    url: https://www.accure.net/sitemap.xml
  reason: customer-only-docs
  state: gated
created: '2026-09-06'
description: ACCURE Battery Intelligence GmbH (Aachen, Germany, founded 2020) builds cloud battery analytics software for grid-scale battery energy storage systems (BESS), electric vehicle fleets and stationary storage. Its platform ingests telemetry from BMS, EMS and PCS systems and applies predictive models for safety, performance, state-of-charge accuracy, lifetime and warranty management. The customer-facing product is the ACCURE platform at accure-platform.com, an Auth0-protected single-page application backed by an API gateway at gateway.accure-platform.com. ACCURE states the platform offers open REST and OPC-UA interfaces, SFTP and API endpoints for historical BMS logs, single sign-on and webhooks, but publishes no public developer portal, API reference or machine-readable contract.
image: https://cdn.prod.website-files.com/67f3b2b2af7509d6ee127613/67f3b2b2af7509d6ee127a0b_ACCURE_favicon.png
layout: provider
modified: '2026-09-06'
name: ACCURE Battery Intelligence
nav: Providers
network: true
overview: 'ACCURE Battery Intelligence publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Battery, Energy Storage, and Analytics.


  ACCURE Battery Intelligence''s developer surface includes engineering blog, support, authentication, and 10 more developer resources.'
plans:
- name: Accurebatteryintelligence Plans Pricing
  plan_count: 0
  slug: accurebatteryintelligence-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Accurebatteryintelligence Rate Limits
  slug: accurebatteryintelligence-rate-limits
security:
- kind: authentication
  name: Accurebatteryintelligence Authentication
  slug: accurebatteryintelligence-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Accurebatteryintelligence Domain Security
  slug: accurebatteryintelligence-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: accurebatteryintelligence
tags:
- Company
- Energy
- Battery
- Energy Storage
- Analytics
- Artificial Intelligence
- Internet of Things
- Electric Vehicles
- Germany
website: https://www.accure.net/
---
