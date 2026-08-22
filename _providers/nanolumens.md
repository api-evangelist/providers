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
  url: security/nanolumens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nanolumens.com/
- group: company
  title: ''
  type: About
  url: https://www.nanolumens.com/about/
- group: other
  title: ''
  type: Products
  url: https://www.nanolumens.com/products/
- group: operate
  title: ''
  type: Support
  url: https://www.nanolumens.com/support/
- group: operate
  title: ''
  type: FAQ
  url: https://www.nanolumens.com/faqs/
- group: company
  title: ''
  type: Blog
  url: https://www.nanolumens.com/blog/
- group: other
  title: ''
  type: Resources
  url: https://www.nanolumens.com/resources/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nanolumens.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nanolumens.com/privacy-policy
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://www.nanolumens.com/service-level-agreement
- group: company
  title: ''
  type: Partners
  url: https://www.nanolumens.com/channel-partners
- group: company
  title: ''
  type: Careers
  url: https://www.nanolumens.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.nanolumens.com/connect-with-us
- group: company
  title: ''
  type: Investors
  url: https://forgeglobal.com/nanolumens_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nanolumens-llms.txt
coverage:
  checked: '2026-08-04'
  detail: NanoLumens markets a "JSON REST API" on the NanoSuite product page, and its AWARE production API gateway resolves at api.nanolumens.com (a WSO2 ELB in us-west-2), but there is no public developer portal or reference anywhere on nanolumens.com and the gateway refused every connection on 80/443/8243/9443 — the contract is only available to display owners with an authenticated NanoSuite tenant.
  evidence:
  - status: 200
    url: https://www.nanolumens.com/nanosuite/
  - status: 404
    url: https://www.nanolumens.com/openapi.json
  - status: 404
    url: https://www.nanolumens.com/swagger.json
  - status: 404
    url: https://www.nanolumens.com/llms.txt
  - status: 404
    url: https://www.nanolumens.com/.well-known/agent-card.json
  - status: 0
    url: https://api.nanolumens.com/openapi.json
  reason: customer-only-docs
  state: gated
created: '2026-08-04'
description: NanoLumens is an American designer and manufacturer of direct-view LED (dvLED) displays and video walls, headquartered in Atlanta, Georgia and founded in 2006 by Rick Cope. It builds fixed and flexible indoor and outdoor displays in custom sizes, shapes and curvatures across the Engage Pro, Engage, NXT, Nixel, NanoPanel 55, Captivate, Performance, CLRVision, CLRVU and NanoBanner product lines, together with Aurora video processing and the NanoSuite display-management software. Its displays are deployed in retail, casinos, higher education, sports and arenas, control rooms, hospitality, themed entertainment, government, corporate and transportation environments. The software side of the business — the AWARE platform and NanoSuite, powered by the ISAAC ecosystem — markets a JSON REST API and webhook-based alerting for remote diagnostics, content scheduling and display-fleet monitoring, but that API is delivered to display owners through an authenticated tenant and has no public
  developer portal, API reference or machine-readable specification.
image: https://www.nanolumens.com/logo.svg
layout: provider
modified: '2026-08-04'
name: NanoLumens
nav: Providers
network: true
overview: 'NanoLumens is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Digital Signage, LED Displays, Display Manufacturing, and Audio Visual.


  NanoLumens'' developer surface includes support, FAQ, engineering blog, and 13 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 11.4
  delta: 0.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nanolumens/refs/heads/main/screenshots/nanolumens-2026-08-07T184621.png
security:
- kind: domain-security
  name: Nanolumens Domain Security
  slug: nanolumens-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nanolumens
tags:
- Company
- Digital Signage
- LED Displays
- Display Manufacturing
- Audio Visual
- Digital Out Of Home
- Device Management
- Remote Monitoring
- Hardware
website: https://www.nanolumens.com/
---
