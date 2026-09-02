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
coverage:
  checked: '2026-08-26'
  detail: Prescient Co. Inc. wound down after an August 2023 Colorado WARN filing that said the company would be closed once the Arvada plant shutdown finished, and prescientco.com has since been reassigned — it 301s to the unrelated www.mellonaid.com, serves that site's TLS certificate, and answers every /.well-known/, /openapi.json and /llms.txt path with that site's 404 — while 1,872 archived URLs spanning the domain's entire history contain no API, docs, portal, swagger or SDK path, only a WordPress marketing site whose sole JSON route was WordPress core's own /wp-json/oembed.
  evidence:
  - status: 301
    url: https://prescientco.com/
  - status: 404
    url: https://prescientco.com/openapi.json
  - status: 404
    url: https://prescientco.com/.well-known/agent-card.json
  - status: 404
    url: https://prescientco.com/llms.txt
  - status: 200
    url: https://web.archive.org/cdx/search/cdx?url=prescientco.com&matchType=domain
  - status: 200
    url: https://equityzen.com/company/prescient/
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Prescient Co. Inc. was a United States construction-technology and manufacturing company that sold an integrated design, engineering, manufacturing and assembly platform for multi-unit buildings — apartments, condominiums, student and military dormitories, hotels and senior-living communities. Its product was the patented Prescient Solution built on the Unified Truss Construction System (UTCS), a light-gauge steel structural framing system manufactured off-site in panelised components and assembled on-site, marketed as a faster, greener and lower-cost alternative to conventional cast-in-place and wood-frame structures at heights up to roughly twelve stories. The "technology" in the offering was internal design-automation software that linked architectural design, structural engineering, factory manufacturing and field assembly into one digital model; it was delivered as a design-build service to real-estate developers and general contractors, never as a product a third party
  could integrate with. Founded in 2012 (some sources list 2013) and headquartered in North Carolina — Charlotte, later Durham — with manufacturing in Mebane, North Carolina and Arvada, Colorado, the company raised a large private round stack including a $40M Series D and a Series E led by Eldridge Industries at a reported $650M valuation; publicly reported lifetime totals disagree, with EquityZen listing $103M and Crunchbase reporting roughly $375M through Series G. The company contracted sharply: the Mebane plant closed in 2022 with 83 jobs cut, 50 Arvada jobs were cut in April 2023, and a Colorado WARN notice filed on 31 August 2023 announced the permanent closure of the Arvada plant and a further 60 jobs, stating that upon conclusion of the shutdown activities the company would be closed. Prescient never operated a public developer program, API, SDK, webhook surface or machine-readable specification, and prescientco.com has since passed out of the company''s control. This profile is
  retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-26'
name: Prescient
nav: Providers
network: true
overview: Prescient is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Construction, Construction Technology, and Building Technology.
random_paper: 7
score:
  band: minimal
  composite: 4.6
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
  previous_composite: 4.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
slug: prescient
tags:
- Company
- Defunct
- Construction
- Construction Technology
- Building Technology
- Prefabrication
- Modular Construction
- Manufacturing
- Real-Estate
- Multifamily Housing
---
