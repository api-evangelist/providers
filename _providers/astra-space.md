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
  url: security/astra-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astra.com/
- group: company
  title: ''
  type: About
  url: https://astra.com/about
- group: company
  title: ''
  type: Blog
  url: https://astra.com/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astra.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://astra.com/contact
- group: company
  title: ''
  type: Careers
  url: https://astra.com/careers
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/astra-space-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/astra-space_stock/
coverage:
  checked: '2026-08-06'
  detail: Astra builds launch vehicles and Hall-effect satellite thrusters, not software — astra.com is a Webflow marketing site whose own llms.txt indexes every page it publishes and names no developer, API, or documentation resource, docs.astra.com is an unconfigured Apache "It works!" default page behind an invalid certificate, and the Astra-Space GitHub org holds zero public repositories.
  evidence:
  - status: 200
    url: https://astra.com/llms.txt
  - status: 404
    url: https://astra.com/developers
  - status: 404
    url: https://astra.com/docs
  - status: 404
    url: https://astra.com/openapi.json
  - status: 404
    url: https://astra.com/.well-known/agent-card.json
  - status: 200
    url: https://docs.astra.com/
  - status: 200
    url: https://api.github.com/orgs/Astra-Space/repos
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Astra is a commercial space company providing dedicated small satellite launch services and flight-proven electric propulsion systems. Founded in 2016 and headquartered in Alameda, California, Astra sells two products: Launch Services on Rocket 4 — targeting roughly 600 kg to low Earth orbit at a weekly cadence — and the Astra Spacecraft Engine, a flight-proven Hall-effect electric propulsion system sold in single- and multi-thruster configurations for satellite constellations. Astra became the fastest privately funded U.S. company to reach orbit in 2021 and returned to private ownership in July 2024. Astra publishes no public developer API, SDK, or machine-readable specification; its buyer-facing surface is a set of launch-services and spacecraft-engine inquiry forms alongside a published Rocket 4 Payload User''s Guide and engine data sheet.'
image: https://cdn.prod.website-files.com/6939ba79cc2078e5f2e84582/6967ec5d0af94e30264c8800_astra-launch.jpeg
layout: provider
modified: '2026-08-06'
name: Astra Space
nav: Providers
network: true
overview: 'Astra Space is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Space, Aerospace, Satellite, and Launch Services.


  Astra Space''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 64
score:
  band: minimal
  composite: 8.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astra-space/refs/heads/main/screenshots/astra-space-2026-08-07T161829.png
security:
- kind: domain-security
  name: Astra Space Domain Security
  slug: astra-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astra-space
tags:
- Company
- Space
- Aerospace
- Satellite
- Launch Services
- Electric Propulsion
- Manufacturing
- Defense
website: https://astra.com/
---
