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
  url: security/swiftmile-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swiftmile-llms.txt
- group: company
  title: ''
  type: Website
  url: https://swiftmile.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swiftmile-inc/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/swiftmile_stock/
coverage:
  checked: '2026-08-29'
  detail: swiftmile.com no longer serves the Swiftmile website — it answers HTTP 200 with a Nexcess hosting placeholder behind a TLS certificate issued for nxcli.net, has returned that same placeholder in every Internet Archive snapshot since 2025-07-09 (the real WordPress site was still live on 2025-04-21), every interior path including /wp-json/ now 404s, and no api., developer., docs., app., dashboard. or portal. subdomain resolves.
  evidence:
  - status: 200
    url: https://swiftmile.com/
  - status: 404
    url: https://swiftmile.com/wp-json/
  - status: 403
    url: https://swiftmile.com/.well-known/agent-card.json
  - status: 404
    url: https://swiftmile.com/openapi.json
  reason: defunct
  state: none
created: '2026-08-29'
description: Swiftmile is a California-based hardware and IoT company building universal charging and parking infrastructure for micromobility — docking stations that power, secure and organize shared and privately owned e-bikes and e-scooters, including solar-powered units and integrated digital advertising panels. Founded around 2014 and headquartered on the San Francisco Peninsula, it supplied secure charging docks to the New York City DOT public e-bike charging pilot alongside PopWheels and Swobbee. Company interviews describe a fleet- and battery-management backend with integrations offered to micromobility operators, but Swiftmile has never published a public developer program, API reference, SDK, or machine-readable contract of any kind, and as of 2026-08-29 swiftmile.com no longer serves the company website at all — the domain answers with a Nexcess hosting placeholder and a TLS certificate that does not match the hostname.
layout: provider
modified: '2026-08-29'
name: Swiftmile
nav: Providers
network: true
overview: Swiftmile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Micromobility, Electric Vehicle Charging, Transportation, and Internet of Things.
plans:
- name: Swiftmile Plans Pricing
  plan_count: 0
  slug: swiftmile-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Swiftmile Rate Limits
  slug: swiftmile-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/swiftmile/refs/heads/main/screenshots/swiftmile-2026-09-02T161356.png
security:
- kind: domain-security
  name: Swiftmile Domain Security
  slug: swiftmile-domain-security
  summary_line: no transport/DNS hardening detected
slug: swiftmile
tags:
- Company
- Micromobility
- Electric Vehicle Charging
- Transportation
- Internet of Things
- Hardware
- Smart Cities
- Fleet Management
website: https://swiftmile.com/
---
