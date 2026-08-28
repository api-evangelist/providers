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
  url: security/nanotech-energy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nanotechenergy.com/
- group: company
  title: ''
  type: Blog
  url: https://nanotechenergy.com/about-us/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://nanotechenergy.com/about-us/blog/feed
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nanotechenergy.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nanotechenergy.com/privacy-policy/
- group: company
  title: ''
  type: Press
  url: https://nanotechenergy.com/about-us/press-release/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/nanotech-energy_stock/
coverage:
  checked: '2026-08-04'
  detail: Nanotech Energy sells graphene powders, pastes, inks and battery cells as physical goods; its WordPress marketing site has no developer section and no api., developer. or docs. subdomain resolves in DNS at all.
  evidence:
  - status: 404
    url: https://nanotechenergy.com/developers
  - status: 404
    url: https://nanotechenergy.com/openapi.json
  - status: 404
    url: https://nanotechenergy.com/graphql
  - status: 404
    url: https://nanotechenergy.com/.well-known/agent-card.json
  - status: 404
    url: https://nanotechenergy.com/.well-known/security.txt
  - status: 0
    url: https://api.nanotechenergy.com/
  reason: not-a-software-company
  state: none
created: '2026-08-04'
description: 'Nanotech Energy is an advanced materials manufacturer that develops and produces graphene-based super materials and the energy-storage products built from them. Its catalog spans graphene powders, graphene oxide pastes, dispersions, conductive inks and conductive adhesives, silver nanowires, and non-flammable lithium-ion battery cells and packs aimed at home and grid energy storage, marine, household and electric-vehicle applications. The company also offers customer-facing testing, analysis and product development services to help customers scale a graphene formulation from concept to full production. It is a physical-goods manufacturer: it publishes a marketing and product website but no developer program, public API, SDK or machine-readable specification of any kind.'
layout: provider
modified: '2026-08-04'
name: Nanotech Energy
nav: Providers
network: true
overview: 'Nanotech Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Materials, Graphene, and Nanotechnology.


  Nanotech Energy''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 9.3
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nanotech-energy/refs/heads/main/screenshots/nanotech-energy-2026-08-07T184623.png
security:
- kind: domain-security
  name: Nanotech Energy Domain Security
  slug: nanotech-energy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nanotech-energy
tags:
- Company
- Manufacturing
- Materials
- Graphene
- Nanotechnology
- Batteries
- Energy Storage
- Energy
website: https://nanotechenergy.com/
---
