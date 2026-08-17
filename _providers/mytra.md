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
  url: security/mytra-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mytra.ai/
- group: company
  title: ''
  type: About
  url: https://mytra.ai/company
- group: company
  title: ''
  type: News
  url: https://mytra.ai/news
- group: company
  title: ''
  type: Careers
  url: https://mytra.ai/careers
- group: other
  title: ''
  type: Patents
  url: https://mytra.ai/patents
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mytra.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mytra.ai/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mytra-llms.txt
coverage:
  checked: '2026-08-04'
  detail: mytra.ai is a 24-URL Nuxt marketing site whose only sections are news, company, careers, patents and legal; there is no developer page, and api./docs./developer./ mcp.mytra.ai do not resolve in DNS at all, so the robots (bots, cells, operating system) are sold and integrated as installed infrastructure rather than behind a public API.
  evidence:
  - status: 200
    url: https://mytra.ai/sitemap.xml
  - status: 404
    url: https://mytra.ai/.well-known/agent-card.json
  - status: 404
    url: https://mytra.ai/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-08-04'
description: 'Mytra, Inc. is a Brisbane, California robotics company founded in 2022 by former Tesla robotics lead Chris Walti, building what it calls software-defined warehousing: a three-part system of low-profile MytraBots that travel in X, Y and Z through a modular steel "cell" matrix up to 80 feet tall, and an AI-driven operating system that plans routes, resolves conflicts and dynamically reconfigures the matrix to store and retrieve anything from cases to full 3,000 lb pallets. The company raised a $120M Series C led by Avenir Growth in January 2026 (roughly $200M total) and sells the system as installed industrial infrastructure to enterprise distribution and food-and-beverage operators. Mytra publishes no developer program, no public API, and no machine-readable API contract.'
image: https://image-cdn.mytra.ai/images/xg8bw7px/production/ff82fd7bd29f5c4aeedee58b8a8bad63321d0201-1920x1080.png
layout: provider
modified: '2026-08-04'
name: Mytra
nav: Providers
network: true
overview: 'Mytra is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Robotics, Warehouse Automation, Supply Chain, and Logistics.


  Mytra''s developer surface includes product news and 8 more developer resources.'
random_paper: 110
score:
  band: minimal
  composite: 10.0
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mytra/refs/heads/main/screenshots/mytra-2026-08-07T184551.png
security:
- kind: domain-security
  name: Mytra Domain Security
  slug: mytra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mytra
tags:
- Company
- Robotics
- Warehouse Automation
- Supply Chain
- Logistics
- Material Handling
- Industrial Automation
- Artificial Intelligence
website: https://mytra.ai/
---
