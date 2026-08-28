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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bright-silicon-technologies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bright-si-tech.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bright-silicon-technologies/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/BrightSiTech
- group: other
  title: ''
  type: Email
  url: mailto:Contact@Bright-Si-Tech.com
coverage:
  checked: '2026-08-08'
  detail: Bright Silicon sells a silicon micromirror chip and optical terminals, not software — its entire site is a single-route base44 SPA whose JavaScript bundle contains only Home, About, Technology, Team, Careers and Contact pages, with no developer, API, SDK or docs page anywhere in it.
  evidence:
  - status: 200
    url: https://www.bright-si-tech.com/
  - status: 404
    url: https://www.bright-si-tech.com/openapi.json
  - status: 404
    url: https://www.bright-si-tech.com/.well-known/agent-card.json
  - status: 525
    url: https://docs.bright-si-tech.com/
  reason: not-a-software-company
  state: none
created: '2026-08-08'
description: Bright Silicon Technologies is a Pleasanton, California photonics and semiconductor company, founded in 2020 out of work at Lawrence Livermore National Laboratory, that builds solid-state optical beam control. Its Lightfield Directing Array (LDA) is a chip-scale segmented micromirror array — described by the company as "400 micro-gimbals on a chip" — that steers light with no moving parts, offering a plus-or-minus 30 degree optical field of regard at sub-microradian precision, a 350k degrees/second slew rate and 100ns settling time. The company positions the LDA as a replacement for bulky mechanical gimbals and conventional MEMS mirrors in free-space optical communication terminals, LIDAR, counter-UAS tracking, adaptive optics and metal 3D printing. The product is silicon and optical hardware sold to aerospace, defense and datacenter customers; the company publishes no public developer program, API, or SDK.
image: https://media.base44.com/images/public/69f2bc7be8bc1a13a0f66e49/68798cfdb_Bright_Logo_20.png
layout: provider
modified: '2026-08-08'
name: Bright Silicon Technologies
nav: Providers
network: true
overview: Bright Silicon Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Photonics, Semiconductors, Optical Communications, and Beam Steering.
random_paper: 16
score:
  band: minimal
  composite: 5.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Bright Silicon Technologies Domain Security
  slug: bright-silicon-technologies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bright-silicon-technologies
tags:
- Company
- Photonics
- Semiconductors
- Optical Communications
- Beam Steering
- MEMS
- LiDAR
- Hardware
- Aerospace and Defense
website: https://www.bright-si-tech.com/
---
