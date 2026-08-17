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
  url: security/phantom-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://phantomspace.com/
- group: company
  title: ''
  type: About
  url: https://phantomspace.com/about-us/
- group: other
  title: ''
  type: Products
  url: https://phantomspace.com/products/
- group: operate
  title: ''
  type: Contact
  url: https://phantomspace.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://phantomspace.bamboohr.com/careers
- group: company
  title: ''
  type: Blog
  url: https://phantomspace.com/phantom-news/
- group: company
  title: ''
  type: BlogFeeds
  url: https://phantomspace.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/phantom-space
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/phantomspace/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/phantomspaceco/
coverage:
  checked: '2026-08-05'
  detail: Phantom Space builds Daytona launch vehicles and satellite buses and sells launch capacity and spacecraft builds by direct contract — its entire public surface is a twelve-page WordPress marketing site where no api./docs./developer. subdomain even resolves in DNS, and the only machine-readable endpoint on the origin is bare WordPress core at /wp-json.
  evidence:
  - status: 404
    url: https://phantomspace.com/openapi.json
  - status: 404
    url: https://phantomspace.com/.well-known/agent-card.json
  - status: 404
    url: https://phantomspace.com/.well-known/security.txt
  - status: 404
    url: https://phantomspace.com/llms.txt
  - status: 200
    url: https://phantomspace.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Phantom Space Corporation is an American space transportation and satellite manufacturing company founded in 2019 and headquartered at 1816 S Research Loop in Tucson, Arizona. Co-founded by Jim Cantrell, Michael D'Angelo and Michal Prywata, it is developing the Daytona family of small-lift orbital launch vehicles — Daytona I, II and III — alongside modular satellite buses, spacecraft manufacturing and constellation deployment services, pursuing a mass-manufacturing, fully US-based supply chain approach to launch and spacecraft production. The company acquired StratSpace and Micro Aerospace Solutions in 2021 to build out its satellite supply chain. Phantom Space sells launch capacity and satellite build programs through direct commercial contracts; it publishes no public developer program, API, SDK or machine-readable specification of any kind.
image: https://phantomspace.com/wp-content/uploads/2024/12/Phantom-Space-Logo-BW-Black-clear.png
layout: provider
modified: '2026-08-05'
name: Phantom Space
nav: Providers
network: true
overview: 'Phantom Space is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Aerospace, Satellites, and Spacecraft.


  Phantom Space''s developer surface includes engineering blog and 10 more developer resources.'
random_paper: 136
score:
  band: minimal
  composite: 5.4
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Phantom Space Domain Security
  slug: phantom-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: phantom-space
tags:
- Company
- Space
- Aerospace
- Satellites
- Spacecraft
- Launch Services
- Small Satellites
- Manufacturing
website: https://phantomspace.com/
---
