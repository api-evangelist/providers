---
access_model:
  confidence: high
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: RuhAN exposes two HTTP endpoints under https://www.ruhan.co/api and publishes no contract for either. GET /api/health returns 200 application/json and is named in the provider's own llms.txt; on 2026-
  name: RuhAN Platform
  slug: ruhan-platform
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.ruhan.co
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ruhan.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.ruhan.co/onboarding
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ruhan.co/legal/kullanim-kosullari
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ruhan.co/legal/gizlilik
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ruhan-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ruhan-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ruhan-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ruhan-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ruhan-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ruhan-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ruhan-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ruhan-packages.yml
created: '2026-07-26'
description: 'RuhAN (ruhan.co) is a Turkish mining and underground-sciences platform covering mining licence workflows, MAPEG and Turkish mining legislation, tender and field reports, geology and mineral exploration, geophysics data processing, GIS and remote sensing, and the YTK, CED (EIA), technical-supervisor, drilling and field-service market, plus a marketplace for sites, ore, equipment, jobs and expert services. It is a Next.js application on Vercel and is pre-launch: its own /api/health endpoint reports that the Supabase and Gemini backends are not configured, the iyzico payment integration is not live, and all seven commerce and privacy documents under /legal are labelled draft text. RuhAN publishes no OpenAPI, AsyncAPI, GraphQL SDL, MCP server or agent card. Its only machine-readable document is an llms.txt, and its only reachable HTTP surface is two undocumented endpoints -- GET /api/health and POST /api/lead.'
image: https://www.ruhan.co/brand/ruhan-crystal-mark.png
layout: provider
modified: '2026-08-27'
name: RuhAN
nav: Providers
network: true
overview: 'RuhAN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Mining, Geology, Geophysics, GIS, and Remote Sensing.


  RuhAN''s developer surface includes pricing, signup flow, authentication, and 10 more developer resources.'
plans:
- name: Ruhan Plans Pricing
  plan_count: 3
  slug: ruhan-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Ruhan Rate Limits
  slug: ruhan-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/ruhan/refs/heads/main/screenshots/ruhan-2026-09-02T154200.png
security:
- kind: authentication
  name: Ruhan Authentication
  slug: ruhan-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ruhan Domain Security
  slug: ruhan-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ruhan
tags:
- Mining
- Geology
- Geophysics
- GIS
- Remote Sensing
- Mining Licensing
- Marketplace
- Turkey
website: https://www.ruhan.co
---
