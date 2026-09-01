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
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.enevate.com/
coverage:
  checked: '2026-08-12'
  detail: enevate.com 302s to a "Website Temporarily Unavailable" notice saying the prior Enevate Corporation website has been retired and the domain is under new ownership after an asset acquisition, and the host now answers 200 with that same 11,883-byte placeholder for every path including /openapi.json and /llms.txt.
  evidence:
  - status: 302
    url: https://www.enevate.com/
  - status: 200
    url: https://www.enevate.com/index.html
  - status: 200
    url: https://www.enevate.com/openapi.json
  - status: 404
    url: https://www.enevate.com/.well-known/agent-card.json
  - status: 404
    url: https://www.enevate.com/.well-known/security.txt
  - status: 404
    url: https://github.com/enevate
  reason: defunct
  state: none
created: '2026-08-12'
description: 'Enevate Corporation was an Irvine, California battery technology company that developed and licensed silicon-dominant lithium-ion anode and cell technology — marketed as HD-Energy and XFC-Energy — aimed at extreme fast charging (roughly five minutes to a substantial state of charge), high energy density, and cold-weather performance for electric vehicles, with a licensing rather than cell-manufacturing business model. It was a materials and cell-chemistry licensor, not a software vendor, and it never operated a developer program, public API, SDK or webhook surface. As of an August 2026 probe the company''s own domain no longer serves a company website: enevate.com redirects to a "Website Temporarily Unavailable" domain notice stating the prior Enevate Corporation website has been retired and the domain is now under new ownership following an asset acquisition process, and that all previously published statements about products, services, partnerships and company operations
  should no longer be considered current. This profile is retained as a recorded absence with the probe evidence attached.'
layout: provider
modified: '2026-08-12'
name: Enevate
nav: Providers
network: true
overview: Enevate is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Battery Technology, Lithium-Ion, Electric Vehicles, and Energy Storage.
random_paper: 9
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
  previous_composite: 1.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 0.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
slug: enevate
tags:
- Company
- Battery Technology
- Lithium-Ion
- Electric Vehicles
- Energy Storage
- Advanced Materials
- Technology Licensing
- Defunct
website: https://www.enevate.com/
---
