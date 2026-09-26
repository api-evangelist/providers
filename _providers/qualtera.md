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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: other
  title: ''
  type: Acquirer
  url: https://www.synopsys.com/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.synopsys.com/solutions/silicon-lifecycle-management.html
- group: company
  title: ''
  type: News
  url: https://news.synopsys.com/2020-06-10-Synopsys-Acquires-Semiconductor-Analytics-Innovator-Qualtera
- group: company
  title: ''
  type: Investors
  url: https://www.serena.vc/portfolio-profile/qualtera/
coverage:
  checked: '2026-08-17'
  detail: Qualtera was absorbed into Synopsys in June 2020; qualtera.com is now delegated to Synopsys nameservers and 301-redirects every path — including /.well-known/agent-card.json, /openapi.json and /llms.txt — to the Synopsys Silicon Lifecycle Management page, while https://qualtera.com refuses the TLS handshake, so no Qualtera-owned surface remains to read.
  evidence:
  - status: 301
    url: http://www.qualtera.com/
  - status: 0
    url: https://qualtera.com/
  - status: 301
    url: http://qualtera.com/openapi.json
  - status: 301
    url: http://qualtera.com/.well-known/agent-card.json
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=qualtera
  - status: 404
    url: https://pypi.org/pypi/qualtera/json
  reason: defunct
  state: none
created: '2026-08-17'
description: 'Qualtera was a French software company, founded in 2010 and backed by Serena, that built high-volume big data analytics platforms for semiconductor test and manufacturing — giving IDMs, foundries and OSATs real-time observability, traceability and production control over test and assembly data across worldwide operations, processing the data of tens of millions of wafers and billions of parts a year. Its products included SiliconDash, an automated decision-support system for test, quality and yield analysis. Synopsys acquired Qualtera on June 10, 2020 and folded its analytics into Yield Explorer and TestMAX, which now ship as part of the Synopsys Silicon Lifecycle Management family. The Qualtera brand and any surface it once had are gone: qualtera.com now resolves to Synopsys nameservers and 301-redirects every path to the Synopsys Silicon Lifecycle Management marketing page, and the host refuses a TLS handshake on port 443 entirely. Qualtera never published a public developer
  portal, API reference, OpenAPI definition, SDK or package on any registry, and no machine-readable contract survives under its own name. This profile is retained as a historical record; the live analytics API surface, where one exists, belongs to Synopsys and is profiled there rather than credited here.'
layout: provider
modified: '2026-08-17'
name: Qualtera
nav: Providers
network: true
overview: 'Qualtera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Acquired, Semiconductors, and Manufacturing Analytics.


  Qualtera''s developer surface includes product news and 3 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/qualtera/refs/heads/main/screenshots/qualtera-2026-09-02T152604.png
slug: qualtera
tags:
- Company
- Defunct
- Acquired
- Semiconductors
- Manufacturing Analytics
- Test Data
- Yield Management
- Big Data
- France
---
