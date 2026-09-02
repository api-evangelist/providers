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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/powertap-hydrogen-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.powertapfuels.com/
- group: company
  title: ''
  type: About
  url: https://www.powertapfuels.com/company-overview.php
- group: other
  title: ''
  type: Technology
  url: https://www.powertapfuels.com/powertap.php
- group: operate
  title: ''
  type: Contact
  url: https://www.powertapfuels.com/contact.php
- group: company
  title: ''
  type: InvestorRelations
  url: https://powertapcapital.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/powertap-hydrogen-fueling-corp
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/powertap-hydrogen-stock
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/powertap-hydrogen-llms.txt
coverage:
  checked: '2026-08-26'
  detail: PowerTap builds physical on-site hydrogen production and dispensing stations; its two corporate sites are a static PHP brochure and a WordPress investor site with no developer, API or documentation section, and every openapi/swagger/graphql/llms.txt/.well-known probe on both hosts returned a genuine 404.
  evidence:
  - status: 404
    url: https://www.powertapfuels.com/openapi.json
  - status: 404
    url: https://www.powertapfuels.com/.well-known/agent-card.json
  - status: 404
    url: https://powertapcapital.com/openapi.json
  - status: 404
    url: https://powertapcapital.com/llms.txt
  - status: 200
    url: https://powertapcapital.com/wp-json/
  - status: 200
    url: https://www.powertapfuels.com/
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'PowerTap Hydrogen Fueling Corp. is an Aliso Viejo, California hydrogen fueling technology company founded in 2020 and operated as a wholly owned subsidiary of the publicly traded PowerTap Hydrogen Capital Corp. (NEO: MOVE, OTC: MOTNF, FWB: 2K6B). PowerTap designs and deploys distributed, on-site "blue hydrogen" production and dispensing stations built on a patented small-scale steam methane reforming (SMR) platform with embedded carbon capture, converting natural gas and municipal water into high-purity hydrogen at the point of use rather than trucking it in. The modular station design is marketed as deployable in weeks instead of months, and the company positions it for heavy-duty trucking and light-vehicle refueling as well as baseload power for data centers. PowerTap technology-based stations operate at private enterprise sites and at a public station near LAX, with additional deployments cited in California, Texas, Massachusetts and Maryland. The company publishes no developer
  program, no API, and no machine-readable contract of any kind; it is profiled here as an energy-infrastructure company, not an API provider.'
image: https://www.powertapfuels.com/img/logo.png
layout: provider
modified: '2026-08-26'
name: PowerTap Hydrogen
nav: Providers
network: true
overview: PowerTap Hydrogen is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Hydrogen, Clean Energy, and Fueling Infrastructure.
random_paper: 6
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Powertap Hydrogen Domain Security
  slug: powertap-hydrogen-domain-security
  summary_line: TLSv1.2
slug: powertap-hydrogen
tags:
- Company
- Energy
- Hydrogen
- Clean Energy
- Fueling Infrastructure
- Transportation
- Carbon Capture
- Heavy Duty Trucking
website: https://www.powertapfuels.com/
---
