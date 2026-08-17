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
  url: https://www.bluewhite.ai/
- group: company
  title: ''
  type: About
  url: https://www.bluewhite.ai/about
- group: other
  title: ''
  type: Technology
  url: https://www.bluewhite.ai/technology
- group: company
  title: ''
  type: Blog
  url: https://www.bluewhite.ai/blog
- group: company
  title: ''
  type: Press
  url: https://www.bluewhite.ai/press
- group: operate
  title: ''
  type: Support
  url: https://www.bluewhite.ai/contact
- group: start
  title: ''
  type: Login
  url: https://compass.bluewhite.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bluewhite.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bluewhite.ai/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.bluewhite.ai/cookie-policy
- group: company
  title: ''
  type: Careers
  url: https://www.bluewhite.ai/careers
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blue-white-robotics-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blue-white-robotics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blue-white-robotics-llms.txt
coverage:
  checked: '2026-08-07'
  detail: Bluewhite advertises a "Software SDK" and an "API platform" on its technology page but publishes no reference behind them — the only route is the contact form, and the Compass operator platform 302s every path, including /openapi.json, to a Keycloak OIDC login.
  evidence:
  - status: 200
    url: https://www.bluewhite.ai/technology
  - status: 302
    url: https://compass.bluewhite.ai/openapi.json
  - status: 503
    url: https://auth.bluewhite.ai/realms/maia-cloud/.well-known/openid-configuration
  - status: 404
    url: https://www.bluewhite.ai/.well-known/agent-card.json
  - status: 404
    url: https://www.bluewhite.ai/llms.txt
  reason: sales-gate
  state: gated
created: '2026-08-07'
description: 'Blue White Robotics Ltd. — operating as Bluewhite — is an Israeli off-road autonomy company founded in 2017 by Ben Alfi, Yair Shahar and Aviram Shmueli, headquartered in Tel Aviv with a US operation in Fresno, California. Bluewhite builds an OEM-agnostic autonomy stack that retrofits conventional vehicles into unmanned ground vehicles: Pathfinder, an aftermarket autonomy kit combining control, intelligence and perception modules over a distributed CAN network, and Compass, a cloud fleet-operations SaaS that lets operators remotely supervise, task and monitor an autonomous fleet. The company began in permanent-crop agriculture — autonomous spraying, mowing and harvest support across roughly 150,000 US acres for 20-plus growers — and has since extended the same GPS-denied navigation and perception stack to defense and homeland-security ground robotics. Elbit Systems'' FUSE acquired 100% of Blue White Robotics in 2026. Bluewhite markets a Software SDK and an "API platform" for
  OEM and system integration, but publishes no public developer portal, API reference, or machine-readable specification; the Compass operator platform sits behind a Keycloak/OIDC login and integration access runs through a contact-sales form.'
image: https://cdn.prod.website-files.com/63bbd401d9936c49d2edf55f/686fed1ea1aabd319517cf1b_BLUEWHITE-LOGO-HORIZONTAL-FULL_COLOR.png
layout: provider
modified: '2026-08-07'
name: Blue White Robotics
nav: Providers
network: true
overview: 'Blue White Robotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Autonomous Vehicles, Agriculture, and Agricultural Technology.


  Blue White Robotics'' developer surface includes engineering blog, support, and 12 more developer resources.'
random_paper: 140
score:
  band: emerging
  composite: 13.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blue-white-robotics/refs/heads/main/screenshots/blue-white-robotics-2026-08-07T162645.png
security:
- kind: domain-security
  name: Blue White Robotics Domain Security
  slug: blue-white-robotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blue-white-robotics
tags:
- Company
- Robotics
- Autonomous Vehicles
- Agriculture
- Agricultural Technology
- Artificial Intelligence
- Fleet Management
- Defense
- Unmanned Ground Vehicles
- Israel
website: https://www.bluewhite.ai/
---
