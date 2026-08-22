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
  url: https://forgeglobal.com/nexa3d_stock/
coverage:
  checked: '2026-08-04'
  detail: Nexa3D sold its IP, inventory and equipment to Stratasys in July 2025 and stopped operating; nexa3d.com now 301-redirects off-brand to the am-material-marketplace / iAM Marketplace storefront, its docs/api/developer subdomains no longer resolve in DNS, and its GitHub organization has zero public repositories, so there is no API surface left to profile.
  evidence:
  - status: 301
    url: https://nexa3d.com/
  - status: 404
    url: https://nexa3d.com/openapi.json
  - status: 404
    url: https://nexa3d.com/llms.txt
  - status: 404
    url: https://nexa3d.com/.well-known/agent-card.json
  - status: 404
    url: https://nexa3d.com/.well-known/agent.json
  - status: 404
    url: https://nexa3d.com/.well-known/security.txt
  - status: 301
    url: https://www.am-material-marketplace.com/
  - status: 200
    url: https://github.com/nexa3d
  reason: defunct
  state: none
created: '2026-08-04'
description: 'Nexa3D was a Ventura, California additive-manufacturing company that built ultrafast photopolymer 3D printers (NXE 400, XiP, XiP Pro) around its Lubricant Sublayer Photo-curing (LSPc) process, QLS selective-laser-sintering systems, and the NexaX print-preparation and print-management software. The company disclosed severe funding challenges in late 2024, withdrew from Formnext, scaled back operations, and in July 2025 sold select assets — intellectual property, inventory and equipment, but not personnel — to Stratasys, with customer support and materials continuity moving to Stratasys subsidiary iSQUARED. Nexa3D no longer operates as an independent company: nexa3d.com now 301-redirects to a third-party additive-manufacturing materials marketplace, and no public developer portal, API reference, or machine-readable specification (OpenAPI, AsyncAPI, GraphQL SDL, MCP manifest, agent card) was found on any Nexa3D host, live or archived.'
layout: provider
modified: '2026-08-04'
name: Nexa3D
nav: Providers
network: true
overview: Nexa3D is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, 3D Printing, Additive Manufacturing, Manufacturing, and Hardware.
random_paper: 12
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
slug: nexa3d
tags:
- Company
- 3D Printing
- Additive Manufacturing
- Manufacturing
- Hardware
- Industrial
- Defunct
website: https://forgeglobal.com/nexa3d_stock/
---
