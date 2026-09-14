---
api_count: 1
apis:
- description: WeaveGrid markets a partner API that lets aggregators, OEMs and device manufacturers align their software stack with electric utilities and participate in WeaveGrid-operated grid programs. The product
  name: WeaveGrid Partner API
  slug: weavegrid-partner-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.weavegrid.com/
- group: company
  title: ''
  type: Blog
  url: https://www.weavegrid.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.weavegrid.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weavegrid.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://charge.weavegrid.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/weavegrid
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weavegrid-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/weavegrid-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weavegrid-llms.txt
coverage:
  checked: '2026-09-04'
  detail: 'WeaveGrid markets a partner API for aggregators on its partners page but publishes no reference or portal — the only route is the "Become a partner" contact form — and the FastAPI app on api.weavegrid.com keeps its own auto-generated OpenAPI document at /openapi.json and its Swagger UI at /docs behind an HTTP 401 "WWW-Authenticate: Basic" challenge, so the machine-readable contract provably exists and is simply not published.'
  evidence:
  - status: 401
    url: https://api.weavegrid.com/openapi.json
  - status: 401
    url: https://api.weavegrid.com/docs
  - status: 200
    url: https://www.weavegrid.com/partners
  - status: 404
    url: https://www.weavegrid.com/pricing
  reason: sales-gate
  state: gated
created: '2026-09-04'
description: WeaveGrid builds grid-orchestration software that lets electric utilities absorb rapid EV and distributed-energy load growth without overbuilding the distribution system. Its DISCO (Distribution-Integrated System Capacity Orchestration) platform ingests vehicle telematics and cloud-connected device data, then sends hyper-local, individualized charging and dispatch signals to EVs, home batteries, smart thermostats and other flexible loads so they respond to real constraints at the transformer, feeder and substation level. The company runs managed-charging and time-of-use programs for utilities including Pacific Gas and Electric, Dominion Energy, DTE, Xcel Energy, Baltimore Gas and Electric, Alabama Power, Ameren Illinois and Portland General Electric, and integrates directly with OEM and device partners such as Toyota, Lexus, Rivian, Hyundai, Kia, ChargePoint, Wallbox, Emporia, SolarEdge, FranklinWH and ecobee. WeaveGrid markets a partner API for aggregators, but publishes no
  public developer portal, reference or machine-readable specification.
image: https://cdn.prod.website-files.com/62c71c576987c5a343e57279/6303119bf01cad6a5d8540af_wg-meta-image.png
layout: provider
modified: '2026-09-04'
name: WeaveGrid
nav: Providers
network: true
overview: 'WeaveGrid publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Electric Utilities, Electric Vehicles, EV Charging, and Smart Grid.


  WeaveGrid''s developer surface includes engineering blog, support, and 7 more developer resources.'
plans:
- name: Weavegrid Plans Pricing
  plan_count: 0
  slug: weavegrid-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Weavegrid Rate Limits
  slug: weavegrid-rate-limits
security:
- kind: authentication
  name: Weavegrid Authentication
  slug: weavegrid-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Weavegrid Domain Security
  slug: weavegrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: weavegrid
tags:
- Energy
- Electric Utilities
- Electric Vehicles
- EV Charging
- Smart Grid
- Managed Charging
- Distributed Energy Resources
- Demand Response
- Grid Orchestration
- Vehicle Telematics
- Climate Tech
- Company
website: https://www.weavegrid.com/
---
