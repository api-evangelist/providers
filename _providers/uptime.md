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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-17'
  detail: Uptime SAS was put into liquidation judiciaire by the Paris Commercial Court on 2022-10-20 with a plan de cession to SAS Otis, and its uptime.ac domain has since lapsed — every path, including /openapi.json and /.well-known/*, now 301-redirects to https://www.investwithcoin.com/how-it-works/ and on to an unrelated gambling site, so the prior common[] Website pointer to www.uptime.ac was removed rather than left pointing at a third party's server.
  evidence:
  - status: 301
    url: https://www.uptime.ac/
  - status: 301
    url: https://www.uptime.ac/openapi.json
  - status: 301
    url: https://www.uptime.ac/.well-known/agent-card.json
  - status: 200
    url: https://www.serena.vc/portfolio-profile/uptime/
  reason: defunct
  state: none
created: '2026-08-17'
description: Uptime (Uptime SAS, Paris, SIREN 822006839) was a French elevator predictive-maintenance company founded in 2016 by Augustin and Amaury Celier. It fitted 4G-connected sensors to existing elevators and used the resulting telemetry to predict failures, dispatch technicians and report availability to building managers, backed by Serena and angels including Jacques-Antoine Granjon, David Amsellem, Yvan Wibaux and Antoine Martin across roughly EUR 10M of funding. The Paris Commercial Court opened a redressement judiciaire on 2022-07-26 and pronounced liquidation judiciaire with a plan de cession to SAS Otis on 2022-10-20; the elevator-maintenance activity and a minority of staff transferred to Otis. The company never published a public developer program, API reference or machine-readable specification, and the uptime.ac domain has since lapsed — it now 301-redirects every path to unrelated third-party sites. This profile is retained as an honest record of a defunct company with no
  API surface.
layout: provider
modified: '2026-08-17'
name: Uptime
nav: Providers
network: true
overview: Uptime is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Data, Predictive Maintenance, Elevators, and Internet of Things.
random_paper: 9
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 0
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 4.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
slug: uptime
tags:
- Company
- Ai Data
- Predictive Maintenance
- Elevators
- Internet of Things
- PropTech
- Building Management
- France
- Defunct
---
