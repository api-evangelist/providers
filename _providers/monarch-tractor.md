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
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.monarchtractor.com/
- group: company
  title: ''
  type: Blog
  url: https://www.monarchtractor.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.monarchtractor.com/en/kb
- group: operate
  title: ''
  type: Support
  url: https://www.monarchtractor.com/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.monarchtractor.com/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monarchtractor.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.monarchtractor.com/terms-of-use
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Monarch-Tractor
- group: other
  title: ''
  type: Product
  url: https://www.monarchtractor.com/digital-solutions
- group: start
  title: ''
  type: Login
  url: https://wingspanai.com/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monarch-tractor-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/monarch-tractor-llms.txt
coverage:
  checked: '2026-08-04'
  detail: Monarch ships software (WingspanAI) but publishes no developer surface at all — /developers, /api, /integrations and every /.well-known/ and spec path 404 on www.monarchtractor.com, and the only product endpoint it links, wingspanai.com/login, no longer resolves because all four of the domain's Route 53 nameservers answer REFUSED (lame delegation).
  evidence:
  - status: 404
    url: https://www.monarchtractor.com/developers
  - status: 404
    url: https://www.monarchtractor.com/.well-known/api-catalog
  - status: 404
    url: https://www.monarchtractor.com/openapi.json
  - status: 0
    url: https://wingspanai.com/login
  - status: 404
    url: https://api.monarchtractor.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-04'
description: Monarch Tractor is a Livermore, California agricultural-technology company that builds the MK-V, a fully electric, driver-optional smart tractor, together with WingspanAI (Wingspan Ag Intelligence) — an AWS-hosted farm-management and fleet-telemetry platform that collects in-field video, machine telemetry, energy and emissions data from connected tractors and presents it to growers through web and mobile apps. The company markets an "open ecosystem" in which third parties integrate with the MK-V and WingspanAI, and has pivoted toward selling autonomy as software and licensing its autonomy stack to other equipment makers. Monarch publishes no public developer portal, API reference, or machine-readable specification; the WingspanAI platform is reachable only through a customer login.
image: https://www.monarchtractor.com/hubfs/logo_horizontal_rgb.png
layout: provider
modified: '2026-08-04'
name: Monarch Tractor
nav: Providers
network: true
overview: 'Monarch Tractor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, AgTech, Robotics, and Autonomous Vehicles.


  Monarch Tractor''s developer surface includes engineering blog, documentation, support, and 9 more developer resources.'
random_paper: 66
score:
  band: emerging
  composite: 16.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monarch-tractor/refs/heads/main/screenshots/monarch-tractor-2026-08-07T184137.png
security:
- kind: domain-security
  name: Monarch Tractor Domain Security
  slug: monarch-tractor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: monarch-tractor
tags:
- Company
- Agriculture
- AgTech
- Robotics
- Autonomous Vehicles
- Electric Vehicles
- Farm Management
- Telemetry
- Internet of Things
- Artificial Intelligence
website: https://www.monarchtractor.com/
---
