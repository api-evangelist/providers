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
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/caastle_stock/
coverage:
  checked: '2026-08-08'
  detail: CaaStle filed Chapter 7 in June 2025 and liquidated; caastle.com no longer belongs to the company and now 301s every path — /openapi.json, every /.well-known/ path and a nonsense control path alike — to an unrelated Indonesian-language site that answers 200 with one byte-identical HTML page, none of the archived api-*.caastle.com tenant hosts still resolve in DNS, and 6,000 Wayback records for the domain contain no developer, docs, or specification path.
  evidence:
  - status: 301
    url: https://caastle.com/
  - status: 301
    url: https://caastle.com/openapi.json
  - status: 301
    url: https://caastle.com/.well-known/agent-card.json
  - status: 301
    url: https://www.caastle.com/.well-known/security.txt
  reason: defunct
  state: none
created: '2026-08-08'
description: 'CaaStle Inc. was a New York based business-to-business "Clothing-as-a-Service" company that built white-label clothing rental, subscription and resale infrastructure for apparel retailers, operating tenant-branded storefronts and reverse-logistics for partner brands rather than selling directly to consumers. The company collapsed in 2025: its board confirmed financial distress and furloughed staff in April 2025, and it filed for Chapter 7 bankruptcy in the District of Delaware on 20 June 2025 (case 25-11187), electing liquidation over reorganization. Founder and chief executive Christine Hunsicker resigned amid allegations of fabricated financial disclosures and later pleaded guilty to a fraud scheme prosecutors valued in the hundreds of millions of dollars. CaaStle never operated a public developer program, and the caastle.com domain has since passed out of the company''s control.'
layout: provider
modified: '2026-08-08'
name: CaaStle
nav: Providers
network: true
overview: CaaStle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Fashion, E-Commerce, and Subscription.
random_paper: 19
score:
  band: minimal
  composite: 4.6
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
      reason: venue_as_website
    - owner: catalog
      reason: never_enriched
  previous_composite: 4.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
slug: caastle
tags:
- Company
- Retail
- Fashion
- E-Commerce
- Subscription
- Rental
- Logistics
- Defunct
website: https://forgeglobal.com/caastle_stock/
---
