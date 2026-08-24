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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atomic-semi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fab2.com/
- group: company
  title: ''
  type: About
  url: https://fab2.com/about/
- group: company
  title: ''
  type: Careers
  url: https://jobs.ashbyhq.com/fab2
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/atomic-semi-stock
coverage:
  checked: '2026-08-06'
  detail: atomicsemi.com 301s to fab2.com, a three-page marketing site (root, /about/, /careers/) whose own sitemap.xml lists no developer surface at all; the company makes chip-fab hardware, its one software product (the Studio in-browser EDA) is used internally rather than sold, and its GitHub org holds only forks of upstream open-source EDA tools with no first-party code.
  evidence:
  - status: 301
    url: https://atomicsemi.com/
  - status: 200
    url: https://fab2.com/sitemap.xml
  - status: 404
    url: https://fab2.com/openapi.json
  - status: 404
    url: https://fab2.com/llms.txt
  - status: 404
    url: https://fab2.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/AtomicSemi/repos
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: Atomic Semi is a semiconductor company founded in 2023 by Sam Zeloof and Jim Keller, now operating publicly as fab2 (atomicsemi.com redirects to fab2.com). It designs and manufactures semiconductor fabrication equipment and the fabs that house it — pumps, valves, sensors, actuators, chambers, heaters, gas lines and robots — with the stated goal of mass-producing small, software-defined chip fabs, a "fab fab". It runs a 120K sq ft chip fab in Austin TX (HQ), a 30K sq ft fab fab in Lockhart TX, and the original 25K sq ft garage fab in San Francisco. Its one software product, Studio (formerly Atomic Studio), is an in-browser collaborative EDA for schematic capture, layout and simulation, used internally rather than sold as a developer platform. The company publishes no API, SDK, developer portal or machine-readable specification.
layout: provider
modified: '2026-08-06'
name: Atomic Semi
nav: Providers
network: true
overview: Atomic Semi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Hardware, Manufacturing, and Electronic Design Automation.
random_paper: 20
score:
  band: minimal
  composite: 4.6
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atomic-semi/refs/heads/main/screenshots/atomic-semi-2026-08-07T161925.png
security:
- kind: domain-security
  name: Atomic Semi Domain Security
  slug: atomic-semi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: atomic-semi
tags:
- Company
- Semiconductors
- Hardware
- Manufacturing
- Electronic Design Automation
- Chip Design
- Deep Tech
website: https://fab2.com/
---
