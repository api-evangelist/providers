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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://newageeats.com
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/new-age-eats_stock/
coverage:
  checked: '2026-08-26'
  detail: New Age Eats was a cultivated-pork food startup that shut down in March 2023; its surviving domain newageeats.com serves a static archived copy of the old Shopify storefront and returns a real 404 on every /.well-known/, OpenAPI and llms.txt path, while the pre-rebrand domain newagemeats.com 301s to ojkgas.com, which does not resolve in DNS.
  evidence:
  - status: 200
    url: https://newageeats.com/
  - status: 404
    url: https://newageeats.com/openapi.json
  - status: 404
    url: https://newageeats.com/.well-known/api-catalog
  - status: 301
    url: https://newagemeats.com/
  - status: 403
    url: https://forgeglobal.com/new-age-eats_stock/
  reason: defunct
  state: none
created: '2026-08-26'
description: 'New Age Eats (founded 2018 in Berkeley, California as New Age Meats, rebranded to New Age Eats in 2022) was a cultivated-meat startup building cell-cultured pork sausage, combining plant protein with its own cultivated pork and a "sensomics" flavor program. It raised roughly $32 million, including a $25 million Series A in 2021 led by Hanwha Solutions, and was completing a pilot manufacturing plant in Alameda, California. Founder and CEO Brian Spears announced the company was winding down in March 2023, citing an inability to raise further capital in a turbulent market before it had any product to sell. It was a food-science company, never a software or API company: it published no developer portal, no documentation, no SDKs and no machine-readable contract of any kind. Its remaining domain, newageeats.com, now serves a static archived copy of the former direct-to-consumer marketing site; the pre-rebrand domain newagemeats.com redirects to a host that no longer resolves.'
layout: provider
modified: '2026-08-26'
name: New Age Eats
nav: Providers
network: true
overview: New Age Eats is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Cultivated Meat, Alternative Protein, and Biotechnology.
random_paper: 16
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
  previous_composite: 4.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: new-age-eats
tags:
- Company
- Food and Beverage
- Cultivated Meat
- Alternative Protein
- Biotechnology
- Consumer Packaged Goods
- Defunct
website: https://newageeats.com
---
