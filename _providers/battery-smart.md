---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/battery-smart-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/battery-smart-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.batterysmart.in/
- group: company
  title: ''
  type: About
  url: https://www.batterysmart.in/aboutUs
- group: operate
  title: ''
  type: Support
  url: https://www.batterysmart.in/contactUs
- group: company
  title: ''
  type: Careers
  url: https://www.batterysmart.in/careers
- group: company
  title: ''
  type: Blog
  url: https://www.batterysmart.in/articles
- group: company
  title: ''
  type: EngineeringBlog
  url: https://batterysmart.tech/
- group: other
  title: ''
  type: Resources
  url: https://www.batterysmart.in/resources
- group: operate
  title: ''
  type: PressReleases
  url: https://www.batterysmart.in/media
- group: other
  title: ''
  type: Awards
  url: https://www.batterysmart.in/awards
- group: company
  title: ''
  type: Partners
  url: https://www.batterysmart.in/partners
- group: other
  title: ''
  type: Fleets
  url: https://www.batterysmart.in/fleets
- group: other
  title: ''
  type: Safety
  url: https://www.batterysmart.in/safetyCenter
- group: other
  title: ''
  type: ESG
  url: https://www.batterysmart.in/esg
- group: other
  title: ''
  type: ImpactReport
  url: https://www.batterysmart.in/impact-report-2025
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.batterysmart.in/tnc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.batterysmart.in/privacy
- group: other
  title: ''
  type: RefundPolicy
  url: https://www.batterysmart.in/refund
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.batterysmart.driver
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.batterysmart.partner
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/BatterySmartIN
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/batterysmart/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@BatterySmartIN
coverage:
  checked: '2026-08-06'
  detail: 'Battery Smart runs a real production API — api.upgrid.in answers {"message":"Battery Smart API"} and a /health check for SQL, Redis, Kafka and Mongo, discovered only through Certificate Transparency on the Upgrid engineering domain — but it exists purely to serve the Driver and Partner Android apps: every spec path on that host returns a JSON 404, batterysmart.in has no /developers, no api./docs./developer. subdomain in DNS at all, and the company publishes no reference, SDK, webhook catalog or specification anywhere.'
  evidence:
  - status: 200
    url: https://api.upgrid.in/
  - status: 404
    url: https://api.upgrid.in/openapi.json
  - status: 404
    url: https://www.batterysmart.in/openapi.json
  - status: 404
    url: https://www.batterysmart.in/llms.txt
  - status: 404
    url: https://www.batterysmart.in/.well-known/agent-card.json
  - status: 0
    url: https://developer.batterysmart.in/
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Battery Smart is India''s largest battery-swapping network for electric two- and three-wheelers, founded in 2019 by Pulkit Khurana and Siddharth Sikka and operated from New Delhi by Upgrid Solutions Private Limited and Upgrid Electrilease Private Limited. It runs an asset-light, partner-led model: local businesses — kirana stores, petrol pumps and neighbourhood shops — host swap points where a driver exchanges a depleted lithium-ion pack for a charged one in roughly two minutes and pays per swap instead of buying the battery with the vehicle, which removes the single largest cost from an electric two- or three-wheeler. The network is concentrated in Delhi NCR, Mumbai, Bengaluru, Hyderabad, Jaipur and Lucknow, and the company has raised across eleven rounds including a USD 65 million Series B led by LeapFrog Investments with MUFG Bank, Panasonic, Ecosystem Integrity Fund, Blume Ventures and British International Investment participating, plus a USD 15 million debt round with
  Mirova in April 2026. Battery Smart''s software ships only as end-user Android applications — Battery Smart Driver and Battery Smart Partner — backed by a production API host at api.upgrid.in that self-identifies as the "Battery Smart API". As of this profile the company publishes no developer portal, API reference, SDK, webhook catalog or machine-readable specification of any kind.'
image: https://www.batterysmart.in/_next/static/media/logo.9f0b8870.webp
layout: provider
modified: '2026-08-06'
name: Battery Smart
nav: Providers
network: true
overview: 'Battery Smart is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Battery Swapping, Electric Vehicles, EV Infrastructure, and Battery as a Service.


  Battery Smart''s developer surface includes support, engineering blog, YouTube channel, and 21 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.3
  delta: -1.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/battery-smart/refs/heads/main/screenshots/battery-smart-2026-08-07T162208.png
security:
- kind: domain-security
  name: Battery Smart Domain Security
  slug: battery-smart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: battery-smart
tags:
- Company
- Battery Swapping
- Electric Vehicles
- EV Infrastructure
- Battery as a Service
- Energy
- Clean Energy
- Mobility
- Two Wheelers
- Three Wheelers
- Last Mile Delivery
- India
website: https://www.batterysmart.in/
---
