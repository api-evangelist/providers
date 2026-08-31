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
  url: security/i-pulse-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ipulse-group.com/
- group: company
  title: ''
  type: About
  url: https://www.ipulse-group.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://www.ipulse-group.com/news/
- group: operate
  title: ''
  type: Support
  url: https://www.ipulse-group.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ipulse-group.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/i-pulse-inc.
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/i-pulse-llms.txt
coverage:
  checked: '2026-08-22'
  detail: I-Pulse is an industrial pulsed-power hardware and process company (I-ROX comminution, G-Pulse geothermal drilling, Bmax metal forming, CSI capacitors); ipulse-group.com is a WordPress marketing site whose only machine-readable HTTP surface is the stock WordPress REST API at /wp-json/ (340 routes across wp/v2, Elementor, Yoast, HubSpot and Complianz plugin namespaces, zero I-Pulse-authored namespaces), and there is no api./developer./docs. host, no developer portal and no OpenAPI anywhere on the domain.
  evidence:
  - status: 404
    url: https://www.ipulse-group.com/openapi.json
  - status: 404
    url: https://www.ipulse-group.com/.well-known/agent-card.json
  - status: 200
    url: https://www.ipulse-group.com/wp-json/
  - status: 0
    url: https://developer.ipulse-group.com/
  - status: 200
    url: https://www.ipulse-group.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-22'
description: I-Pulse Inc. is a U.S.-based industrial technology company founded in 2007 by Robert Friedland and Laurent Frescaline that commercializes High Pulsed Power (HPP) — releasing very short, extremely high-power electrical discharges from small amounts of stored energy to generate magnetic forces, shockwaves, electrical arcs and electric fields. I-Pulse holds 55 patents licensed exclusively to its operating businesses across natural-resource transformation (I-ROX rock comminution, I-Mine, iTerra non-chemical weed control, IPW), the energy transition (G-Pulse pulsed-power geothermal drilling, Blue Spark Geothermal), manufacturing (Bmax electromagnetic metal forming and welding, CSI Technologies high-energy capacitors) and R&D (I-Cube, Typhoon). It operates from Albuquerque, New Mexico and Toulouse, France, with offices in Canada, the UK and Singapore, and signed a $250 million CHIPS R&D award with the U.S. Department of Commerce in 2026 for semiconductor and pulsed-power development.
  I-Pulse is a hardware and industrial-process company; it publishes no developer program, API documentation or machine-readable API contract.
image: https://www.ipulse-group.com/wp-content/uploads/2024/05/iPULSE-Logo.png
layout: provider
modified: '2026-08-22'
name: I-Pulse
nav: Providers
network: true
overview: 'I-Pulse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial, Energy, Mining, and Manufacturing.


  I-Pulse''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: I Pulse Domain Security
  slug: i-pulse-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: i-pulse
tags:
- Company
- Industrial
- Energy
- Mining
- Manufacturing
- Semiconductors
- Geothermal
- Deep Tech
- Pulsed Power
website: https://www.ipulse-group.com/
---
