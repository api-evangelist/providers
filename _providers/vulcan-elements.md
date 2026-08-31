---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vulcan-elements-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vulcanelements.com/
- group: company
  title: ''
  type: Blog
  url: https://vulcanelements.com/updates/
- group: company
  title: ''
  type: BlogRSS
  url: https://vulcanelements.com/feed/
- group: company
  title: ''
  type: Careers
  url: https://vulcanelements.com/careers/
coverage:
  checked: '2026-08-05'
  detail: Vulcan Elements manufactures physical sintered NdFeB rare earth magnets, and its entire web presence is a three-page WordPress marketing site (home, Benson site expansion, careers) plus an updates feed — /api, /developers, /docs and every /.well-known/ path return a hard 404, and no api., docs. or developer. subdomain resolves at all.
  evidence:
  - status: 404
    url: https://vulcanelements.com/developers
  - status: 404
    url: https://vulcanelements.com/api
  - status: 404
    url: https://vulcanelements.com/openapi.json
  - status: 404
    url: https://vulcanelements.com/.well-known/agent-card.json
  - status: 200
    url: https://vulcanelements.com/page-sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Vulcan Elements is a United States manufacturer of sintered permanent neodymium-iron-boron (NdFeB) rare earth magnets, founded in 2023 and headquartered in Research Triangle Park, North Carolina. The company produces high-performance rare earth magnets domestically for defense and commercial applications — the components that convert electricity into motion in motors, drones, robotics, vehicles and consumer electronics — as an alternative to a supply chain concentrated in China. In 2025 it announced a $65 million Series A, a $620 million loan from the Pentagon''s Office of Strategic Capital, and a $1.4 billion partnership with the U.S. government and ReElement Technologies to build a vertically integrated domestic magnet supply chain, including a nearly $1 billion, 1,000-job magnet factory in Benson, Johnston County, North Carolina. Vulcan Elements is a physical-goods manufacturer: it publishes no public API, developer portal, SDK or machine-readable specification.'
image: https://vulcanelements.com/wp-content/uploads/2024/06/header-logo.svg
layout: provider
modified: '2026-08-05'
name: Vulcan Elements
nav: Providers
network: true
overview: 'Vulcan Elements is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Rare Earth Magnets, Advanced Materials, and Critical Minerals.


  Vulcan Elements'' developer surface includes engineering blog and 4 more developer resources.'
random_paper: 1
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Vulcan Elements Domain Security
  slug: vulcan-elements-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vulcan-elements
tags:
- Company
- Manufacturing
- Rare Earth Magnets
- Advanced Materials
- Critical Minerals
- Supply Chain
- Defense
- Hardware
website: https://vulcanelements.com/
---
