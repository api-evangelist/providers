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
overview: 'Qualtera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Acquired, Semiconductor, and Manufacturing Analytics.


  Qualtera''s developer surface includes product news and 3 more developer resources.'
random_paper: 118
score:
  band: minimal
  composite: 4.6
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
    - owner: catalog
      reason: never_enriched
  schema_version: 0.12.0
  scored_at: '2026-08-19'
slug: qualtera
tags:
- Company
- Defunct
- Acquired
- Semiconductor
- Manufacturing Analytics
- Test Data
- Yield Management
- Big Data
- France
---
