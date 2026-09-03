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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-08-23'
  detail: InterPrice Technologies wound down during 2025 and its only company domain, interpricetech.com, now has an empty DNS delegation — the .com registry still points at two Route 53 nameservers but both answer REFUSED, so all 160 contract-discovery probes across ten hosts (root, www, api, app, demo, docs, developer, auth, addins, status) failed at name resolution rather than returning any HTTP status, leaving no host to run discovery against.
  evidence:
  - status: 0
    url: https://interpricetech.com/
  - status: 0
    url: https://api.interpricetech.com/openapi.json
  - status: 0
    url: https://interpricetech.com/.well-known/agent-card.json
  - status: 0
    url: https://interpricetech.com/.well-known/agent.json
  - status: 0
    url: https://interpricetech.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/interprice
  - status: 404
    url: https://pypi.org/pypi/interprice/json
  - status: 200
    url: https://web.archive.org/web/20250126162047/https://interpricetech.com/
  - status: 200
    url: https://www.linkedin.com/company/interprice-technologies
  reason: defunct
  state: none
created: '2026-08-23'
description: InterPrice Technologies, Inc. was a New York City debt capital markets fintech that gave corporate treasury teams a single web platform for new-issue financing decisions. Founded by Olga Chin and commercially launched in 2020, its treasury capital markets platform aggregated the indicative pricing that banks and financing partners supplied for bonds, commercial paper, loans and hedging, normalized it across currencies and products, and presented it in comparison dashboards so CFOs and treasurers could read funding costs side by side instead of collecting them by email and spreadsheet. The company was WBENC-certified as a woman-owned business, raised roughly $9.8M — a $2.5M seed in March 2021 and a $7.3M Series A in November 2022 co-led by Nasdaq Ventures and DRW Venture Capital with Bowery Capital participating — and named HP Inc., McCormick & Company and Takeda Pharmaceuticals among its corporate treasury customers. In March 2023 it announced bank API connectivity, but that
  was an inbound integration through which relationship banks delivered pricing indications into the InterPrice platform for its own tenants; no public developer portal, API reference, key issuance, or machine-readable specification was ever published, and none appears anywhere in the 983 archived URLs captured for the domain. The company wound down during 2025 — founder and chief executive Olga Chin left in February 2025 and is now a managing director at Tradeweb, the last Wayback capture of the site is 2025-01-26, and interpricetech.com now has an empty DNS delegation — so this profile is retained as a historical record and there is no API surface to enrich.
layout: provider
modified: '2026-08-23'
name: InterPrice Technologies
nav: Providers
network: true
overview: InterPrice Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Financial-Services, Fintech, and Capital Markets.
random_paper: 12
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
slug: interprice-technologies
tags:
- Company
- Defunct
- Financial-Services
- Fintech
- Capital Markets
- Debt Capital Markets
- Corporate Treasury
- Bonds
- Pricing
---
