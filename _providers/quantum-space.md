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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantum-space-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quantumspaceinc.com/
- group: company
  title: ''
  type: About
  url: https://www.quantumspaceinc.com/about
- group: operate
  title: ''
  type: Contact
  url: https://www.quantumspaceinc.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.quantumspaceinc.com/updates
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/quantumspacellc
- group: company
  title: ''
  type: Investors
  url: https://investors.quantumspace.us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quantumspace-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quantum-space-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Quantum Space manufactures Ranger spacecraft and sells missions through defense contract vehicles, so there is no product an API could front — every OpenAPI, GraphQL, MCP and /.well-known/ probe on both of its hosts returned 404 and its api./docs./developer. subdomains are NXDOMAIN.
  evidence:
  - status: 404
    url: https://www.quantumspaceinc.com/openapi.json
  - status: 404
    url: https://www.quantumspaceinc.com/.well-known/agent-card.json
  - status: 200
    url: https://www.quantumspaceinc.com/llms.txt
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: Quantum Space is a space defense and orbital mobility company headquartered in Rockville, Maryland, building Ranger — a maneuverable spacecraft designed to operate across LEO, MEO, GEO and cislunar orbits. Per the company's own published material, Ranger carries up to 4,000 kg of storable propellant, uses multi-mode chemical and electric propulsion for up to 12 km/s of delta-V, is designed for a 15-year on-station operational life, supports on-orbit refueling in both directions, and exposes a modular five-port payload architecture. The company sells space domain awareness, satellite servicing, satellite life extension and on-orbit refueling to national security, civil and commercial customers, with engineering in Rockville, propulsion and integration in Hawthorne, California and Huntsville, Alabama, and spacecraft production in Tulsa, Oklahoma. Leadership includes CEO Jim Bridenstine (former NASA Administrator), Executive Chairman Kam Ghaffarian and President Kerry Wisnosky.
  Quantum Space publishes no public developer program, API reference or machine-readable API contract; the only machine-readable artifact served from its own hosts is an llms.txt at the website root.
image: https://cdn.prod.website-files.com/69f390c049b974c2b472c40d/69f80fb70fcbd647826bf04b_1200x630%20Quantum.png
layout: provider
modified: '2026-08-26'
name: Quantum Space
nav: Providers
network: true
overview: 'Quantum Space is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Space, Aerospace, Defense, Satellites, and Spacecraft.


  Quantum Space''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Quantum Space Plans Pricing
  plan_count: 0
  slug: quantum-space-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Quantum Space Rate Limits
  slug: quantum-space-rate-limits
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Quantum Space Domain Security
  slug: quantum-space-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quantum-space
tags:
- Space
- Aerospace
- Defense
- Satellites
- Spacecraft
- Orbital Mobility
- National Security
- Space Domain Awareness
- Company
website: https://www.quantumspaceinc.com/
---
