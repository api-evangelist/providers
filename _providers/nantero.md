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
  checked: '2026-08-26'
  detail: Nantero ceased operations in mid-to-late 2024 (assets partly to Micron, remainder auctioned) and nantero.com has since been re-registered by an unrelated party that answers HTTP 200 with the same 719,496-byte Thai gambling page for every path, so its /.well-known/ and /openapi.json 200s are a catch-all rather than any surface Nantero ever served.
  evidence:
  - status: 301
    url: https://nantero.com/
  - status: 200
    url: https://nantero.com/.well-known/agent-card.json
  - status: 0
    url: https://nanterotech.com/
  - status: 200
    url: http://web.archive.org/web/20240116172446/https://www.nantero.com/
  reason: defunct
  state: none
created: '2026-08-26'
description: 'Nantero, Inc. was a Woburn, Massachusetts nanotechnology company founded in 2001 by Greg Schmergel, Thomas Rueckes and Brent Segal to commercialize NRAM, a high-density non-volatile random-access memory that stores bits in the physical position of carbon nanotubes deposited on a conventional CMOS substrate. Its business was semiconductor intellectual-property licensing, not software: it raised more than $40 million through a Schlumberger-backed Series D in 2013 and a further ~$31.5 million Series E in 2015 from investors including Charles River Ventures and Draper Fisher Jurvetson, licensed NRAM to Fujitsu Semiconductor in 2016, granted Lockheed Martin an exclusive government-applications license in 2008, and collaborated with imec and Nano-C, but shipped its technology to foundry partners as process IP and test wafers rather than as any product a developer could call. Nantero ceased operations in mid-to-late 2024; its assets were partially acquired by Micron Technology and
  the remainder sold at auction. It never published a developer portal, API, SDK, or machine-readable specification of any kind, and the nantero.com domain has since been re-registered by an unrelated party. This profile is retained as a historical record; there is no API surface to enrich.'
layout: provider
modified: '2026-08-26'
name: Nantero
nav: Providers
network: true
overview: Nantero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Semiconductors, Memory, and Nanotechnology.
random_paper: 3
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
  scored_at: '2026-09-02'
  trend: flat
slug: nantero
tags:
- Company
- Defunct
- Semiconductors
- Memory
- Nanotechnology
- Hardware
- Intellectual Property
- Carbon Nanotubes
---
