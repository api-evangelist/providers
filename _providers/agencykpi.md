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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.agencykpi.com/
coverage:
  checked: '2026-08-06'
  detail: agencykpi.com now serves one static "AgencyKPI Services Are No Longer Available" notice page and soft-404s every other path — /openapi.json, /llms.txt, /.well-known/security.txt and /.well-known/agent-card.json all return HTTP 200 with shutdown-notice HTML byte-identical to a random control path, and the old marketing mirror akpi-public-website.webflow.io now hard-404s at its root.
  evidence:
  - status: 200
    url: https://www.agencykpi.com/
  - status: 200
    url: https://www.agencykpi.com/openapi.json
  - status: 200
    url: https://www.agencykpi.com/.well-known/agent-card.json
  - status: 0
    url: https://api.agencykpi.com/
  - status: 0
    url: https://docs.agencykpi.com/
  - status: 404
    url: https://akpi-public-website.webflow.io/
  reason: defunct
  state: none
created: '2026-08-06'
description: 'AgencyKPI, Inc. was an Austin, Texas insurtech founded in 2017 by Trent Richmond and Bobby Billman, building a business intelligence and benchmarking platform for the independent insurance distribution channel — agency networks, independent agencies, carriers and wholesalers. The platform (marketed as Harmony) ingested, cleaned and normalized policy, premium and commission data out of agency management systems and carrier feeds, then presented benchmarking, collaborative planning and operational reporting on top of it, plus a managed insurance data lake for customer data teams. The company raised a Series A in 2020 from insurance industry investors and a Series B in 2022 that included Live Oak Ventures. As of 2026 AgencyKPI has ceased operations: agencykpi.com serves only a single-page service notice stating the platform has been discontinued effective immediately, and no developer, documentation or API surface remains reachable.'
layout: provider
modified: '2026-08-06'
name: AgencyKPI
nav: Providers
network: true
overview: AgencyKPI is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Business Intelligence, and Analytics.
random_paper: 10
score:
  band: minimal
  composite: 0.5
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
      reason: never_enriched
  previous_composite: 0.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agencykpi/refs/heads/main/screenshots/agencykpi-2026-08-07T161130.png
slug: agencykpi
tags:
- Company
- Insurance
- Insurtech
- Business Intelligence
- Analytics
- Benchmarking
- Data Aggregation
- Agency Management
- Defunct
website: https://www.agencykpi.com/
---
