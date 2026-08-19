---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://foreveroceans.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/foreveroceans
- group: other
  title: ''
  type: Listing
  url: https://forgeglobal.com/forever-oceans_stock/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forever-oceans-domain-security.yml
coverage:
  checked: '2026-08-16'
  detail: Forever Oceans was an offshore fish-farming company whose investors handed it to liquidation specialists in November 2024; its own domain foreveroceans.com now refuses HTTPS entirely (connection refused on 443) and serves only a Gandi registrar parking page reading "foreveroceans.com is unavailable" over plain HTTP, with no api/docs/developer subdomains resolving and an empty corporate GitHub org.
  evidence:
  - status: 0
    url: https://foreveroceans.com/
  - status: 200
    url: http://foreveroceans.com/
  - status: 200
    url: http://foreveroceans.com/openapi.json
  - status: 0
    url: http://foreveroceans.com/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/foreveroceans
  reason: defunct
  state: none
created: '2026-08-16'
description: 'Forever Oceans Corporation was a US offshore aquaculture company, founded in 2014 and headquartered in Virginia, that raised sushi-grade kanpachi (Seriola rivoliana) in deep water off the Pacific coast of Panama using a patented single-point mooring system that let its submerged pens orient with ocean currents. It raised roughly $170M and held a large Brazilian marine-aquaculture concession, with planned farms in Brazil and Indonesia. Its investors brought in restructuring and liquidation specialists in November 2024, and its corporate domain foreveroceans.com is now a registrar parking page that refuses HTTPS. Seafood production, not software, was the product: the company never published an API, developer portal, SDK or any machine-readable contract, and no such surface survives.'
layout: provider
modified: '2026-08-16'
name: Forever Oceans
nav: Providers
network: true
overview: Forever Oceans is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aquaculture, Seafood, Food Production, and Sustainability.
random_paper: 98
score:
  band: minimal
  composite: 5.0
  delta: -0.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 5.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Forever Oceans Domain Security
  slug: forever-oceans-domain-security
  summary_line: no transport/DNS hardening detected
slug: forever-oceans
tags:
- Company
- Aquaculture
- Seafood
- Food Production
- Sustainability
- Offshore Farming
- Ocean Technology
- Defunct
website: https://foreveroceans.com/
---
