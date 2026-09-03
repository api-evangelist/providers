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
  url: security/sion-power-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sionpower.com/
- group: company
  title: ''
  type: About
  url: https://sionpower.com/company/
- group: other
  title: ''
  type: Product
  url: https://sionpower.com/product/
- group: other
  title: ''
  type: Technology
  url: https://sionpower.com/technology/
- group: company
  title: ''
  type: Partners
  url: https://sionpower.com/partners/
- group: company
  title: ''
  type: News
  url: https://sionpower.com/news/
- group: company
  title: ''
  type: Careers
  url: https://sionpower.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://sionpower.com/contact/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/sion-power_stock/
coverage:
  checked: '2026-08-27'
  detail: Sion Power manufactures physical lithium-metal battery cells under OEM development agreements; sionpower.com is an eight-page WordPress marketing site with no developer, docs or API section, and every contract-discovery probe (/openapi.json, /swagger.json, /api-docs, /graphql, /.well-known/*) returned the theme's 404 page, leaving the WordPress /wp-json/ CMS endpoint (401 rest_api_authentication_required) as the only API-shaped surface on the domain.
  evidence:
  - status: 404
    url: https://sionpower.com/openapi.json
  - status: 404
    url: https://sionpower.com/graphql
  - status: 404
    url: https://sionpower.com/.well-known/agent-card.json
  - status: 401
    url: https://sionpower.com/wp-json/
  - status: 200
    url: https://sionpower.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-27'
description: Sion Power Corporation is a Tucson, Arizona lithium-metal battery developer and manufacturer, spun out of Brookhaven National Laboratory in 1989. Its Licerion platform pairs a protected lithium-metal anode with proprietary electrolyte and cell engineering to deliver rechargeable cells with roughly double the gravimetric energy density of conventional lithium-ion, targeting defense and aerospace systems, uncrewed aircraft, and electrified mobility. The company operates a 115,000-square-foot R&D and pilot manufacturing facility, holds more than 430 international patents and applications, and has raised over $230 million from investors including LG Energy Solution. Sion Power sells physical battery cells under development agreements with OEMs; it publishes no developer program, public API, SDK, or machine-readable API contract of any kind.
layout: provider
modified: '2026-08-27'
name: Sion Power
nav: Providers
network: true
overview: 'Sion Power is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Batteries, Energy Storage, Lithium Metal, and Manufacturing.


  Sion Power''s developer surface includes product news and 9 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 2.9
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
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sion-power/refs/heads/main/screenshots/sion-power-2026-09-02T155637.png
security:
- kind: domain-security
  name: Sion Power Domain Security
  slug: sion-power-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sion-power
tags:
- Company
- Batteries
- Energy Storage
- Lithium Metal
- Manufacturing
- Advanced Materials
- Defense
- Aerospace
- Electric Vehicles
- Hardware
website: https://sionpower.com/
---
