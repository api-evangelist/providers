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
- group: company
  title: ''
  type: Website
  url: https://dascena.com
coverage:
  checked: '2026-08-11'
  detail: dascena.com still holds a live GoDaddy registration delegating to four Route 53 nameservers, but the hosted zone behind them is gone, so every public resolver returns SERVFAIL and no HTTP request to any Dascena host can complete; the laboratory business was acquired by CirrusDx in August 2022 and the successor host serves no developer surface either.
  evidence:
  - status: 0
    url: https://dascena.com/
  - status: 0
    url: https://dascena.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/dascena
  - status: 404
    url: https://cirrusdx.com/openapi.json
  - status: 200
    url: https://cirrusdx.com/
  reason: defunct
  state: none
created: '2026-08-11'
description: Dascena was an Oakland, California health-technology company that built machine-learning diagnostic and clinical decision support algorithms for hospitals, most notably InSight, a sepsis prediction model that scored electronic health record vitals and labs in real time to flag patients at risk hours before onset, plus FDA breakthrough-designated models for acute kidney injury and gastrointestinal bleeding. The algorithms were delivered as an embedded integration inside a customer hospital's EHR under a services and laboratory agreement rather than as a public developer API, so the company never operated a developer portal, published a machine-readable contract, or shipped client SDKs. CirrusDx acquired the Dascena Labs laboratory business effective 5 August 2022 and the company identity now trades as DBA CirrusDx; the dascena.com domain no longer resolves.
layout: provider
modified: '2026-08-11'
name: Dascena
nav: Providers
network: true
overview: Dascena is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Machine-Learning, and Diagnostics.
random_paper: 5
score:
  band: minimal
  composite: 1.8
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
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
slug: dascena
tags:
- Company
- Healthcare
- Artificial Intelligence
- Machine-Learning
- Diagnostics
- Clinical Decision Support
- Sepsis
- Acquired
website: https://dascena.com
---
