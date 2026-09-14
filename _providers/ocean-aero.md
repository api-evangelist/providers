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
  url: security/ocean-aero-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oceanaero.com
- group: company
  title: ''
  type: About
  url: https://www.oceanaero.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.oceanaero.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oceanaero.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oceanaero.com/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/ocean-aero-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ocean-aero-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/ocean-aero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ocean-aero-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Ocean Aero's entire web presence is a 13-page Squarespace marketing site for the Triton AUSV with no developer, docs or API section; fleets are run from the company's own proprietary mission-control GUI, and api./developer./docs./portal./data.oceanaero.com do not resolve in DNS.
  evidence:
  - status: 200
    url: https://www.oceanaero.com/sitemap.xml
  - status: 404
    url: https://www.oceanaero.com/openapi.json
  - status: 404
    url: https://www.oceanaero.com/llms.txt
  - status: 404
    url: https://www.oceanaero.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Ocean Aero is a Gulfport, Mississippi maritime robotics manufacturer that designs, builds and operates the Triton, an environmentally powered Autonomous Underwater and Surface Vehicle (AUSV) that can both sail on the surface and submerge to collect data above and below the waterline and relay it back to shore. The 14-foot platform harvests wind and solar energy, carries pre-packaged or custom payloads for defense, ocean research and offshore energy missions, and is managed through Ocean Aero's own proprietary mission-control GUI with fleet-wide waypoint and payload management. As of this profile Ocean Aero sells vehicles, payloads and mission services — it publishes no public developer program, no API reference and no machine-readable API contract.
image: https://static1.squarespace.com/static/6a563a75f3daa06a8c545fa3/t/6a5643493543696e32b268b7/1784038217324/Option_5.png?format=1500w
layout: provider
modified: '2026-08-26'
name: Ocean Aero
nav: Providers
network: true
overview: 'Ocean Aero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Maritime, Autonomous Vehicles, Uncrewed Systems, and Robotics.


  Ocean Aero''s developer surface includes support and 9 more developer resources.'
plans:
- name: Ocean Aero Plans Pricing
  plan_count: 0
  slug: ocean-aero-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Ocean Aero Rate Limits
  slug: ocean-aero-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/ocean-aero/refs/heads/main/screenshots/ocean-aero-2026-09-02T150821.png
security:
- kind: domain-security
  name: Ocean Aero Domain Security
  slug: ocean-aero-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ocean-aero
tags:
- Company
- Maritime
- Autonomous Vehicles
- Uncrewed Systems
- Robotics
- Ocean Data
- Defense
- Hardware
website: https://www.oceanaero.com
---
