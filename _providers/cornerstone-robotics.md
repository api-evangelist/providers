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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cornerstone-robotics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cornerstone-robotics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.csrbtx.com/
- group: company
  title: ''
  type: Website
  url: https://en.csrbtx.com/
- group: company
  title: ''
  type: About
  url: https://en.csrbtx.com/about-us
- group: other
  title: ''
  type: Product
  url: https://en.csrbtx.com/sentire
- group: operate
  title: ''
  type: Support
  url: https://en.csrbtx.com/contact-us
- group: company
  title: ''
  type: News
  url: https://en.csrbtx.com/news
- group: operate
  title: ''
  type: PressRelease
  url: https://en.csrbtx.com/press-release
- group: other
  title: ''
  type: Events
  url: https://en.csrbtx.com/events
- group: company
  title: ''
  type: Careers
  url: https://en.csrbtx.com/join-us
- group: learn
  title: ''
  type: Training
  url: https://en.csrbtx.com/professional-education
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CornerstoneRobotics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cornerstone-robotics-limited/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://en.csrbtx.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://en.csrbtx.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://en.csrbtx.com/cookies-policy
- group: other
  title: ''
  type: WhistleblowingPolicy
  url: https://en.csrbtx.com/whistleblowing-policy
- group: other
  title: ''
  type: SiteMap
  url: https://en.csrbtx.com/sitemap
coverage:
  checked: '2026-08-11'
  detail: Cornerstone Robotics sells the Sentire endoscopic surgical robot as a regulated physical medical device — the whole 41-page csrbtx.com sitemap is product, clinical, news, careers and policy pages with no developer section, and api/developer/docs/portal subdomains do not resolve at all.
  evidence:
  - status: 200
    url: https://en.csrbtx.com/sitemap.xml
  - status: 500
    url: https://en.csrbtx.com/openapi.json
  - status: 404
    url: https://en.csrbtx.com/api-docs
  - status: 404
    url: https://en.csrbtx.com/graphql
  - status: 500
    url: https://en.csrbtx.com/.well-known/agent-card.json
  - status: 404
    url: https://en.csrbtx.com/.well-known/api-catalog
  - status: 200
    url: https://api.github.com/orgs/CornerstoneRobotics
  reason: no-developer-program
  state: none
created: '2026-08-11'
description: 'Cornerstone Robotics (CSR) is a Hong Kong-headquartered surgical robotics manufacturer founded in 2019 at Hong Kong Science Park, building the Sentire Endoscopic Surgical System (C1000) — a multi-specialty, minimally invasive robot-assisted surgery platform developed entirely in-house and indicated for general surgery, gynecology, thoracic and urology. The Sentire system has received regulatory clearance in China (NMPA), the European Union and Singapore, and has completed multicenter clinical trials in China and the United Kingdom. The company operates three global R&D hubs, six business centers and a 30,000 square meter manufacturing facility, and sells a regulated physical medical device rather than software: it publishes no developer portal, no public API, no SDKs and no machine-readable specifications.'
image: https://en.csrbtx.com/static/home/svg/LOGO.svg
layout: provider
modified: '2026-08-11'
name: Cornerstone Robotics
nav: Providers
network: true
overview: 'Cornerstone Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Surgical Robotics, Medical Devices, and Healthcare.


  Cornerstone Robotics'' developer surface includes support, product news, training material, and 16 more developer resources.'
random_paper: 30
score:
  band: minimal
  composite: 12.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Cornerstone Robotics Domain Security
  slug: cornerstone-robotics-domain-security
  summary_line: TLSv1.2
slug: cornerstone-robotics
tags:
- Company
- Robotics
- Surgical Robotics
- Medical Devices
- Healthcare
- Health
- Medical Technology
- Minimally Invasive Surgery
- Hong Kong
- Manufacturing
website: https://www.csrbtx.com/
---
