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
coverage:
  checked: '2026-08-23'
  detail: Intarcia Therapeutics wound down after the FDA's 2020 complete response letter and sold the Medici / ITCA 650 assets to i2o Therapeutics in 2023; intarcia.com and intarciatherapeutics.com are now an Atom.com domain-broker parking page that hard-404s every /.well-known/ and spec path, and api., developer., docs., portal., dev. and app. subdomains do not resolve at all.
  evidence:
  - status: 403
    url: https://intarcia.com/
  - status: 404
    url: https://intarcia.com/zzz-control-nonsense-xyz789
  - status: 404
    url: https://intarcia.com/openapi.json
  - status: 404
    url: https://intarcia.com/llms.txt
  - status: 404
    url: https://intarcia.com/.well-known/agent-card.json
  - status: 404
    url: https://intarciatherapeutics.com/.well-known/agent.json
  - status: 200
    url: https://api.github.com/orgs/intarcia
  - status: 403
    url: https://forgeglobal.com/intarcia-therapeutics_stock/
  reason: defunct
  state: none
created: '2026-08-23'
description: 'Intarcia Therapeutics, Inc. was a Boston-headquartered clinical-stage biopharmaceutical and drug-delivery company, founded in 1997 and once valued at roughly $5.5B, that developed the Medici Drug Delivery System — a matchstick-sized subdermal osmotic mini-pump engineered to stabilize therapeutic proteins and peptides at body temperature and release them continuously for months from a single placement. Its lead candidate, ITCA 650, delivered the GLP-1 receptor agonist exenatide for type 2 diabetes over three- to six-month intervals. The FDA issued complete response letters on the ITCA 650 new drug application in 2017 and again in 2020, after which the company ran out of capital, laid off staff, closed its Boston, Hayward (CA) and Durham (NC) sites and liquidated its manufacturing and laboratory equipment at auction. Its remaining assets — the Medici platform and ITCA 650 — were acquired by i2o Therapeutics in August 2023, and FDA published a final decision refusing to approve
  the ITCA 650 application on 2024-08-23. Intarcia was a drug-device developer rather than a software company: its corporate site carried only Medici System, Pipeline, Newsroom, About, Leadership and Careers sections and never published a developer program, public API, SDK, webhook surface or machine-readable specification of any kind. As of 2026-08-23 both intarcia.com and intarciatherapeutics.com resolve to an Atom.com domain-broker parking page that offers the names for sale and returns HTTP 404 on every path, and no developer-facing subdomain resolves. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-23'
name: Intarcia Therapeutics
nav: Providers
network: true
overview: Intarcia Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Biotechnology, Pharmaceuticals, and Drug Delivery.
random_paper: 1
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
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
slug: intarcia-therapeutics
tags:
- Company
- Defunct
- Biotechnology
- Pharmaceuticals
- Drug Delivery
- Medical Devices
- Diabetes
- Health
- Life Sciences
---
