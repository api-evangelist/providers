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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://boltthreads.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boltthreads
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/bolt-threads_stock/
coverage:
  checked: '2026-08-08'
  detail: boltthreads.com now serves a single 1.4KB wind-down page reading "The Company is no longer operating" with a creditor-contact email at vlpc.com; api./developer./docs. subdomains do not resolve in DNS, and the boltthreads GitHub org holds 17 repositories that are all forks of third-party Ruby/JS open source, last pushed in 2020.
  evidence:
  - status: 200
    url: https://boltthreads.com/
  - status: 404
    url: https://boltthreads.com/developers
  - status: 404
    url: https://boltthreads.com/openapi.json
  - status: 404
    url: https://boltthreads.com/.well-known/agent-card.json
  - status: 0
    url: https://api.boltthreads.com/
  reason: defunct
  state: none
created: '2026-08-08'
description: Bolt Threads, Inc. was a San Francisco Bay Area biomaterials company founded in 2009 to engineer protein- and mycelium-based materials. It is best known for Microsilk, a bioengineered spider-silk fiber; Mylo, a mycelium-derived leather alternative developed with partners including adidas, Kering, Lululemon, Patagonia and Stella McCartney; and b-silk protein, a silk-protein ingredient for beauty and personal care. The company went public on Nasdaq in August 2024 via a SPAC business combination under the ticker BSLK, halted Mylo production, was suspended from Nasdaq in January 2026, and now trades OTC Pink while deregistering with the SEC. Its website serves only a notice that the company is no longer operating. Bolt Threads was a materials manufacturer, not a software vendor, and never operated a developer program, public API, SDK, or machine-readable specification.
layout: provider
modified: '2026-08-08'
name: Bolt Threads
nav: Providers
network: true
overview: Bolt Threads is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biomaterials, Biotechnology, Materials Science, and Sustainability.
random_paper: 65
score:
  band: minimal
  composite: 5.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 5.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
slug: bolt-threads
tags:
- Company
- Biomaterials
- Biotechnology
- Materials Science
- Sustainability
- Personal Care
- Textiles
- Defunct
website: https://boltthreads.com/
---
