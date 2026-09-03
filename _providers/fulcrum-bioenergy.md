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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: Listing
  url: https://forgeglobal.com/fulcrum-bioenergy_stock/
coverage:
  checked: '2026-08-16'
  detail: Fulcrum BioEnergy was a waste-to-SAF plant developer, not a software company; it shut the Sierra BioFuels Plant in May 2024, filed Chapter 11 that September and completed liquidation in May 2025, and today its corporate domain fulcrum-bioenergy.com has no A record at all while the alternate fulcrumbioenergy.com is a GoDaddy for-sale lander that returns the same 114-byte HTML stub with HTTP 200 on every path, including /openapi.json and every /.well-known/ path.
  evidence:
  - status: 200
    url: https://www.fulcrumbioenergy.com/
  - status: 200
    url: https://www.fulcrumbioenergy.com/openapi.json
  - status: 200
    url: https://www.fulcrumbioenergy.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/fulcrum-bioenergy
  - status: 404
    url: https://pypi.org/pypi/fulcrum-bioenergy/json
  - status: 403
    url: https://forgeglobal.com/fulcrum-bioenergy_stock/
  reason: defunct
  state: none
created: '2026-08-16'
description: Fulcrum BioEnergy, Inc. was a Pleasanton, California waste-to-fuels project developer founded in 2007 that converted municipal solid waste into synthetic crude oil for refining into sustainable aviation fuel (SAF) and diesel, using a shred-and-sort feedstock line feeding a gasifier and a Fischer-Tropsch conversion train. Its first and only commercial plant, the Sierra BioFuels Plant in the Tahoe Reno Industrial Center outside Reno, Nevada, was designed to take roughly 175,000-219,000 tons of household garbage a year from an adjacent feedstock processing facility and began production in late 2022. The company raised on the order of a billion dollars in equity, debt and government support over its life, including strategic investments and offtake alliances with United Airlines, Waste Management, Cathay Pacific Airways, Marubeni and bp, plus a US Department of Energy loan guarantee, USDA loan guarantee and Department of Defense grants; E. James Macias led it as president and CEO
  through its build-out years, and it had announced follow-on projects including a Gary, Indiana plant and the NorthPoint facility in the UK. The Sierra plant stopped operating in mid-May 2024 after persistent equipment problems, the company laid off essentially its entire workforce and took its website down, and on 2024-09-09 Fulcrum BioEnergy, Fulcrum Sierra Holdings and Fulcrum Sierra Finance Co. filed voluntary Chapter 11 petitions in the US Bankruptcy Court for the District of Delaware listing more than $456 million owed to over 200 creditors. A November 2024 auction sold the biorefinery to Switch, Ltd. for $55 million and the adjacent feedstock processing facility to Refuse Inc., a WM subsidiary; the plan of liquidation was confirmed in April 2025 and went effective in May 2025. Fulcrum was an industrial energy project developer rather than a software company and never published a developer program, public API, SDK, webhook surface, or machine-readable specification — a Wayback index
  of its corporate site from 2008 through 2024 turns up no developer, reference, or spec path of any kind. Its corporate host fulcrum-bioenergy.com no longer resolves to any web server, and the alternate registration fulcrumbioenergy.com is parked on the GoDaddy/Afternic aftermarket and listed for sale. This profile is retained as a historical record; there is no API surface to enrich.
layout: provider
modified: '2026-08-16'
name: Fulcrum BioEnergy
nav: Providers
network: true
overview: Fulcrum BioEnergy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Energy, Biofuels, and Sustainable Aviation Fuel.
random_paper: 11
score:
  band: minimal
  composite: 1.7
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
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 1.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 0.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
slug: fulcrum-bioenergy
tags:
- Company
- Defunct
- Energy
- Biofuels
- Sustainable Aviation Fuel
- Renewable Fuels
- Waste-to-Energy
- Waste Management
- Cleantech
- Industrial
- Manufacturing
---
