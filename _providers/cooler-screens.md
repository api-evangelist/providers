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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cooler-screens-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cooler-screens-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.coolerx.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coolerx.com/privacy-policy/
coverage:
  checked: '2026-08-09'
  detail: CoolerX runs api.coolerx.com and portal.coolerx.com — both resolve to Azure address 13.67.211.230 and both refuse connections on 80 and 443 — while the public site has no developer, docs, or API page of any kind, leaving the "Request a Demo" contact form as the only route to the platform.
  evidence:
  - status: 0
    url: https://api.coolerx.com/
  - status: 404
    url: https://www.coolerx.com/developers
  - status: 404
    url: https://www.coolerx.com/.well-known/api-catalog
  - status: 200
    url: https://www.coolerx.com/demo/
  reason: sales-gate
  state: gated
created: '2026-08-09'
description: CoolerX — formerly Cooler Screens — is an in-store retail media and merchandising technology company that turns cooler doors, endcaps, checkout coolers and pharmacy fixtures into IoT-connected digital screens. The platform pairs an AI "Intent Engine" for contextual targeting and conversion-funnel optimization with a Dynamic Content Engine for creative optimization, alongside campaign management, real-time measurement, and a data integration hub for product, price, promotion and context data. It is deployed with retailers including Kroger, Walgreens, Giant Eagle's GetGo, Chevron and Western Union, and is built on Microsoft Azure with NVIDIA, BOE, LG, Samsung and Foxconn as hardware and infrastructure partners. CoolerX sells to retailers and brands through a demo and sales motion; as of this profile it publishes no public developer program, API reference, SDK, or machine-readable specification.
image: https://www.coolerx.com/wp-content/uploads/2025/01/white-on-black-coolerX-logo.png
layout: provider
modified: '2026-08-09'
name: CoolerX
nav: Providers
network: true
overview: CoolerX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Retail Media, Advertising, and Digital Signage.
random_paper: 52
score:
  band: minimal
  composite: 7.8
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: domain-security
  name: Cooler Screens Domain Security
  slug: cooler-screens-domain-security
  summary_line: TLSv1.3
slug: cooler-screens
tags:
- Company
- Retail
- Retail Media
- Advertising
- Digital Signage
- In-Store Media
- Merchandising
- Artificial Intelligence
- Internet of Things
website: https://www.coolerx.com/
---
