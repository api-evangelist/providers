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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://nironmagnetics.com/
- group: company
  title: ''
  type: About
  url: https://nironmagnetics.com/about/
- group: company
  title: ''
  type: Blog
  url: https://nironmagnetics.com/news-press/
- group: company
  title: ''
  type: PressCoverage
  url: https://nironmagnetics.com/press-coverage/
- group: operate
  title: ''
  type: Contact
  url: https://nironmagnetics.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://nironmagnetics.com/careers/
- group: other
  title: ''
  type: Leadership
  url: https://nironmagnetics.com/leadership/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nironmagnetics.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nironmagnetics.com/terms/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/niron-magnetics-inc./
- group: company
  title: ''
  type: Twitter
  url: https://x.com/NironMagnetics
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@nironmagnetics1012/videos/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/niron-magnetics-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/niron-magnetics-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/niron-magnetics_stock/
coverage:
  checked: '2026-08-04'
  detail: Niron Magnetics manufactures Iron Nitride permanent magnets; its entire web presence is a WordPress marketing site whose only machine-readable endpoint is the stock WordPress /wp-json/ core route (oembed, jetpack, rankmath, HubSpot leadin) — there is no product API, no developer subdomain (api./developer./docs. all fail to resolve), and no published contract.
  evidence:
  - status: 200
    url: https://nironmagnetics.com/llms.txt
  - status: 404
    url: https://nironmagnetics.com/openapi.json
  - status: 404
    url: https://nironmagnetics.com/.well-known/agent-card.json
  - status: 0
    url: https://api.nironmagnetics.com/
  - status: 0
    url: https://developer.nironmagnetics.com/
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'Niron Magnetics is a U.S. advanced-manufacturing company commercializing high-performance permanent magnets made from Iron Nitride rather than rare-earth elements. Spun out of University of Minnesota and U.S. Department of Energy ARPA-E research and founded in 2013, the company holds 150+ patents around its Clean Earth Magnet technology and is building the first full-scale Iron Nitride magnet plant in Sartell, Minnesota, alongside its Minneapolis headquarters and a Washington, D.C. policy office. Its magnets target electric-motor, automotive, consumer-audio, industrial and defense applications, with announced collaborations including Stellantis, Moog, Aspina, FaitalPRO, MATTER and Bimotal. Niron Magnetics is a materials and hardware manufacturer: it publishes no developer program, no public API, and no machine-readable API contract.'
image: https://nironmagnetics.com/wp-content/uploads/2026/04/NironHrzGrnLogoBlckType-1.svg
layout: provider
modified: '2026-08-04'
name: Niron Magnetics
nav: Providers
network: true
overview: 'Niron Magnetics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Advanced Materials, Permanent Magnets, and Rare Earth Alternatives.


  Niron Magnetics'' developer surface includes engineering blog, YouTube channel, and 13 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/niron-magnetics/refs/heads/main/screenshots/niron-magnetics-2026-08-07T185336.png
security:
- kind: domain-security
  name: Niron Magnetics Domain Security
  slug: niron-magnetics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: niron-magnetics
tags:
- Company
- Manufacturing
- Advanced Materials
- Permanent Magnets
- Rare Earth Alternatives
- Electric Motors
- Clean Energy
- Industrial
- Defense
website: https://nironmagnetics.com/
---
