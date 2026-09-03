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
- group: commercial
  title: ''
  type: License
  url: https://github.com/medly/medly-components/blob/master/LICENSE
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/medly
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/medly/medly-components
- group: build
  title: ''
  type: Packages
  url: packages/medly-pharmacy-packages.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/medly-pharmacy_stock/
coverage:
  checked: '2026-08-25'
  detail: Medly Health Inc. was liquidated under Chapter 7 on 2023-04-26 after selling its prescription files, inventory and IP to Walgreens, and medly.com is now the acquirer's redirector — port 443 has no listener at all and port 80 answers HTTP 301 to https://www.walgreens.com/ for every path including /openapi.json and every /.well-known/ path, so no probe can reach a Medly-served document.
  evidence:
  - status: 301
    url: http://medly.com/
  - status: 301
    url: http://medly.com/.well-known/agent-card.json
  - status: 0
    url: https://medly.com/openapi.json
  - status: 301
    url: http://api.medly.com/
  - status: 200
    url: https://api.github.com/orgs/medly
  reason: defunct
  state: none
created: '2026-08-25'
description: Medly Pharmacy (Medly Health Inc.) was a Brooklyn, New York digital pharmacy founded in 2017 by Marg Patel, a second-generation pharmacist. It operated a hybrid model — physical retail pharmacy locations paired with free same-day prescription delivery — supported by a consumer mobile app for refills, prescription status and pharmacist chat, and a prescriber-facing e-prescribing workflow it marketed to physician practices. The company raised a $100M Series B in July 2020, expanded into several US metros, and in 2021 acquired the health-and-wellness retailer Pharmaca. It never published a developer program, public API, SDK, machine-readable specification or partner integration reference; the platform was an internal product, not a product sold to developers. Medly Health filed for Chapter 11 bankruptcy on 9 December 2022 along with 31 affiliates, agreed on 9 February 2023 to sell its remaining prescription files, inventory and intellectual property to Walgreens for $19.35M, wound
  down all retail and e-commerce operations by 31 March 2023, and converted to a Chapter 7 liquidation on 26 April 2023. In September 2024 the SEC charged three former executives, including the founder, in connection with the company's capital raises. The medly.com domain is now controlled by the acquirer and blanket-redirects every path to walgreens.com. What survives publicly is the company's engineering open source — the GitHub `medly` organization and its npm and Maven Central packages — none of which is an API client. This profile is retained as a historical record; there is no API surface to enrich.
image: https://avatars.githubusercontent.com/u/54950577?v=4
layout: provider
modified: '2026-08-25'
name: Medly Pharmacy
nav: Providers
network: true
overview: Medly Pharmacy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Healthcare, Pharmacy, and Prescription Delivery.
random_paper: 9
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
slug: medly-pharmacy
tags:
- Company
- Defunct
- Healthcare
- Pharmacy
- Prescription Delivery
- Digital Health
- E-Commerce
- Retail
- Consumer
- Open-Source
---
