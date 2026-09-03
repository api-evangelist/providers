---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/modern-electron-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://modernhydrogen.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/modernelectron
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/modern-electron-llms.txt
coverage:
  checked: '2026-08-25'
  detail: Modern Electron (now trading as Modern Hydrogen) sells physical energy hardware — thermionic converters and behind-the-meter methane-pyrolysis units installed at customer sites — and runs no developer program; its brand domain modernelectron.com 302s every path to modernhydrogen.com, which at probe time answered the Pantheon platform "404 - Unknown site" for the site root itself behind a default *.pantheonsite.io certificate that does not cover the domain.
  evidence:
  - status: 302
    url: http://modernelectron.com/
  - status: 404
    url: https://modernhydrogen.com/
  - status: 404
    url: https://modernhydrogen.com/openapi.json
  - status: 404
    url: https://modernhydrogen.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/modernelectron
  reason: not-a-software-company
  state: none
created: '2026-08-25'
description: Modern Electron is a Bothell, Washington energy-hardware company founded in 2015 by Tony Pan (CEO) and Max Mankin (CTO) as a spin-out of Intellectual Ventures. It was built to commercialize advanced thermionic energy converters — solid-state, direct heat-to-electricity devices intended to add on-site generation to combustion and thermal equipment. The company now operates publicly as Modern Hydrogen, applying methane pyrolysis behind the meter to crack natural gas into hydrogen and solid carbon before combustion, for industrial heat and steam, on-site power, data-center energy, asphalt products and heavy-duty fleet fueling. The product is physical equipment installed at customer sites; Modern Electron / Modern Hydrogen operates no developer program, publishes no public API, SDK or machine-readable specification, and its public GitHub organization holds only forks of open-source scientific-computing projects (WarpX, AMReX, PICMI, GPy) used in its own R&D.
layout: provider
modified: '2026-08-25'
name: Modern Electron
nav: Providers
network: true
overview: Modern Electron is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Hydrogen, Clean Energy, and Hardware.
random_paper: 17
score:
  band: minimal
  composite: 4.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 4.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: domain-security
  name: Modern Electron Domain Security
  slug: modern-electron-domain-security
  summary_line: DMARC
slug: modern-electron
tags:
- Company
- Energy
- Hydrogen
- Clean Energy
- Hardware
- Manufacturing
- Climate Tech
- Thermionics
website: https://modernhydrogen.com/
---
