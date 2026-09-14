---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: Token-authenticated REST API for the Growatt ShineServer monitoring platform. Exposes plant lists and details, plant energy overview and history, device lists, and per-device energy, detail, history a
  name: Growatt Open API V1
  slug: growatt-open-api-v1
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://growatt.com/
- group: start
  title: ''
  type: Portal
  url: https://openapi.growatt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.showdoc.com.cn/262556420217021/0
- group: docs
  title: ''
  type: APIReference
  url: https://www.showdoc.com.cn/262556420217021/0
- group: build
  title: ''
  type: Packages
  url: packages/growatt-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/growatt-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/growatt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/growatt-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/growatt-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/growatt-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/growatt-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/growatt-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/growatt-domain-security.yml
created: '2026-07-17'
description: Growatt New Energy is a global manufacturer of solar PV inverters, energy storage systems, and smart energy management products for residential, commercial, and utility-scale installations. Growatt operates the ShineServer / ShinePhone cloud monitoring platform and publishes a token-authenticated Open API (V1) that lets third-party systems read plant and device telemetry, retrieve historical energy data, and read or write inverter parameters for MIN (TLX) string inverters and SPH (MIX) hybrid inverters across regional endpoints. Originally surfaced as a portfolio company of IDG Capital; enriched from Growatt's public developer surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/growatt.png
layout: provider
modified: '2026-07-19'
name: Growatt
nav: Providers
network: true
overview: 'Growatt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Technology, Solar, Energy, and Photovoltaic.


  Growatt''s developer surface includes developer portal, documentation, API reference, authentication, and 9 more developer resources.'
random_paper: 20
screenshot: https://raw.githubusercontent.com/api-evangelist/growatt/refs/heads/main/screenshots/growatt-2026-07-25T220401.png
security:
- kind: authentication
  name: Growatt Authentication
  slug: growatt-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Growatt Domain Security
  slug: growatt-domain-security
  summary_line: TLSv1.2 · DMARC
slug: growatt
tags:
- Company
- Consumer Technology
- Solar
- Energy
- Photovoltaic
- Inverters
- Energy Storage
- IoT
- Monitoring
website: https://growatt.com/
---
