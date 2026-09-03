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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 0
common:
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/universal-hydrogen
coverage:
  checked: '2026-09-02'
  detail: 'Universal Hydrogen Co. ran out of cash and shut down on 27 June 2024, and both of its web hosts are gone: hydrogen.aero and www.hydrogen.aero answer a bare HTTP 404 "Unknown site" page on the root and on every /.well-known/ and specification path despite the A record still resolving, while universalhydrogen.com has been re-pointed to a Sedo parking lander whose wildcard catch-all returns the same parking HTML with a 200 on /llms.txt and /api-docs and CHEQ bot-filter 440/441 codes elsewhere. Its real GitHub organization is still live but holds zero public repositories, api./docs./developers.hydrogen.aero do not resolve, and the Wayback archive of the domain contains no developer or specification path — the company was a hydrogen fuel-capsule and powertrain hardware business that never published an API.'
  evidence:
  - status: 404
    url: https://hydrogen.aero/
  - status: 404
    url: https://www.hydrogen.aero/
  - status: 404
    url: https://hydrogen.aero/openapi.json
  - status: 404
    url: https://hydrogen.aero/llms.txt
  - status: 404
    url: https://hydrogen.aero/.well-known/agent-card.json
  - status: 404
    url: https://hydrogen.aero/.well-known/agent.json
  - status: 404
    url: https://hydrogen.aero/.well-known/security.txt
  - status: 200
    url: https://universalhydrogen.com/
  - status: 441
    url: https://universalhydrogen.com/openapi.json
  - status: 200
    url: https://api.github.com/orgs/universal-hydrogen
  - status: 404
    url: https://registry.npmjs.org/universal-hydrogen
  reason: defunct
  state: none
created: '2026-09-02'
description: 'Universal Hydrogen Co. was a Hawthorne, California hydrogen-aviation startup founded in 2020 by former Airbus CTO Paul Eremenko to decarbonize regional air travel. Rather than building a hydrogen pipeline network, it proposed a modular capsule model: lightweight hydrogen capsules loaded into aircraft with existing cargo handling equipment, paired with fuel-cell powertrain conversion kits for regional turboprops such as the ATR 72 and De Havilland Dash 8. In March 2023 it flew a converted Dash 8-300 testbed with one propeller driven by a hydrogen fuel cell. The company raised roughly $100 million from backers including GE Aviation, American Airlines, JetBlue Ventures, Airbus Ventures, Toyota Ventures and Mitsubishi. Unable to raise further equity or debt or to find a buyer, it ceased operations on 27 June 2024 and liquidated. It was a hardware and fuel-logistics business and never shipped a public API, SDK, developer portal or machine-readable specification; its domains no longer
  serve a site.'
layout: provider
modified: '2026-09-02'
name: Universal Hydrogen
nav: Providers
network: true
overview: Universal Hydrogen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Aviation, Aerospace, and Hydrogen.
random_paper: 4
score:
  band: minimal
  composite: 2.4
  coverage:
    artifact_dirs: 1
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
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 2.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 0.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
slug: universal-hydrogen
tags:
- Company
- Defunct
- Aviation
- Aerospace
- Hydrogen
- Clean Energy
- Fuel Cells
- Sustainability
- Decarbonization
- Hardware
- Logistics
---
