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
  url: security/venus-aerospace-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/venus-aerospace-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.venusaero.com/
- group: other
  title: ''
  type: Product
  url: https://www.venusaero.com/rdre
- group: other
  title: ''
  type: Product
  url: https://www.venusaero.com/vdr
- group: other
  title: ''
  type: Team
  url: https://www.venusaero.com/team
- group: company
  title: ''
  type: Careers
  url: https://www.venusaero.com/careers
- group: company
  title: ''
  type: Investors
  url: https://www.venusaero.com/investors
- group: company
  title: ''
  type: Newsroom
  url: https://www.venusaero.com/newsroom
- group: operate
  title: ''
  type: Contact
  url: https://www.venusaero.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/venusaero/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/VenusAerospace
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/venusaero/
coverage:
  checked: '2026-08-05'
  detail: Venus Aerospace builds rocket engines, not software — venusaero.com is a seven-page Webflow marketing site (RDRE, VDR, team, investors, newsroom, careers, contact) where /developers, /api, /docs, /openapi.json and /llms.txt all return a real 404, every /.well-known/* path returns "Invalid .well-known request", and api./docs./developer.venusaero.com do not resolve in DNS.
  evidence:
  - status: 404
    url: https://www.venusaero.com/developers
  - status: 404
    url: https://www.venusaero.com/openapi.json
  - status: 404
    url: https://www.venusaero.com/llms.txt
  - status: 404
    url: https://www.venusaero.com/.well-known/agent-card.json
  - status: 404
    url: https://www.venusaero.com/.well-known/security.txt
  - status: 200
    url: https://www.venusaero.com/
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Venus Aerospace is a propulsion company building the Venus Rotating Detonation Rocket Engine (RDRE) and the Venus Detonation Ramjet (VDR), a hybrid that pairs the RDRE with air-breathing ramjet technology to carry a vehicle from takeoff through hypersonic cruise on a single engine. The company positions detonation-based propulsion — supersonic detonation waves propagating around an annular combustor rather than conventional subsonic combustion — for defense munitions and uncrewed systems, space upper stages, orbital transfer vehicles and landers, and commercial high-speed flight. Venus Aerospace is a hardware and flight-test organization: it publishes a public marketing site covering the RDRE, the VDR, its team, investors and newsroom, but no developer program, API, SDK or machine-readable specification of any kind.'
image: https://cdn.prod.website-files.com/689185f14513f9a00c297276/6896545ad4a23ab7d7b49564_Frame%2067.png
layout: provider
modified: '2026-08-05'
name: Venus Aerospace
nav: Providers
network: true
overview: Venus Aerospace is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Propulsion, Hypersonics, and Rocket Engines.
random_paper: 20
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Venus Aerospace Domain Security
  slug: venus-aerospace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: venus-aerospace
tags:
- Company
- Aerospace
- Propulsion
- Hypersonics
- Rocket Engines
- Defense
- Space
website: https://www.venusaero.com/
---
