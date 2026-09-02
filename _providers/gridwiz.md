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
- group: company
  title: ''
  type: Website
  url: https://www.gridwiz.com/en/
- group: operate
  title: ''
  type: Support
  url: https://www.gridwiz.com/en/contact/contact.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gridwiz.com/en/etc/privacy.php
- group: company
  title: ''
  type: Blog
  url: https://www.gridwiz.com/en/media/media.php
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gridwiz-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gridwiz-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gridwiz-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gridwiz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gridwiz-rate-limits.yml
coverage:
  checked: '2026-08-22'
  detail: Gridwiz sells demand response aggregation, ESS, renewable-energy advisory and CCS/V2G EV charging hardware, all through a contact form and a phone number; contract discovery against every host it controls found no OpenAPI, GraphQL, MCP, A2A or .well-known surface, and gridwiz.com answers every nonexistent subdomain (api., dev., openapi., portal.) from one wildcard catch-all returning HTTP 406 behind a self-signed certificate, so there is no API host to document.
  evidence:
  - status: 200
    url: https://www.gridwiz.com/en/
  - status: 404
    url: https://www.gridwiz.com/openapi.json
  - status: 404
    url: https://em.gridwiz.com/openapi.json
  - status: 406
    url: https://api.gridwiz.com/
  - status: 404
    url: https://www.gridwiz.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-22'
description: Gridwiz Inc. is a South Korean clean-energy software and hardware company founded in 2013 and headquartered in Seoul. It operates one of Korea's largest demand response (DR) aggregation portfolios, gathering electricity that industrial and commercial customers curtail and selling it into the national power market, and it pairs that with energy storage (ESS), renewable energy / RE100 and PPA advisory, and an e-mobility line covering EV charging controllers, CCS communication modems (EVCC/SECC), bidirectional V2G chargers and the Skyblue consumer charging service. Its e-mobility products are built to the international EV charging standards DIN SPEC 70121, ISO 15118 (including 15118-20 AC/DC) and OCPP, and its demand response management system is described as OpenADR-based. Gridwiz sells energy services and certified hardware to utilities, EVSE suppliers and enterprises; it publishes no public developer program, API reference, or machine-readable API contract.
image: https://www.gridwiz.com/data/og-image/gridwiz-min.jpg
layout: provider
modified: '2026-08-22'
name: Gridwiz
nav: Providers
network: true
overview: 'Gridwiz is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Demand Response, Electric Vehicles, and EV Charging.


  Gridwiz''s developer surface includes support, engineering blog, and 7 more developer resources.'
plans:
- name: Gridwiz Plans Pricing
  plan_count: 0
  slug: gridwiz-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Gridwiz Rate Limits
  slug: gridwiz-rate-limits
score:
  band: emerging
  composite: 11.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 11.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Gridwiz Domain Security
  slug: gridwiz-domain-security
  summary_line: TLSv1.2
slug: gridwiz
tags:
- Company
- Energy
- Demand Response
- Electric Vehicles
- EV Charging
- Smart Grid
- Energy Storage
- Renewable Energy
- Vehicle-to-Grid
- South Korea
website: https://www.gridwiz.com/en/
---
