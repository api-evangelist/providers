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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Website
  url: https://www.nasdaqprivatemarket.com/
coverage:
  checked: '2026-08-06'
  detail: Athos is a clinical-stage biotech whose only software product, the Chiron AI Labs omics suite (formerly AthosOmics.AI), is marketed explicitly as "no-code" and is pre-launch behind a demo-waitlist email form; the eight-page athostx.com sitemap contains no developer, docs or API page and every well-known/spec path on both hosts returns 404.
  evidence:
  - status: 200
    url: https://athostx.com/page-sitemap.xml
  - status: 404
    url: https://athostx.com/openapi.json
  - status: 404
    url: https://athostx.com/.well-known/agent-card.json
  - status: 404
    url: https://chironailabs.com/openapi.json
  - status: 404
    url: https://chironailabs.com/llms.txt
  - status: 0
    url: https://api.athostx.com/
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Athos Therapeutics is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-08-06'
name: Athos Therapeutics
nav: Providers
network: true
overview: Athos Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 77
score:
  band: minimal
  composite: 2.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 27.8
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
slug: athos-therapeutics
tags:
- Company
website: https://www.nasdaqprivatemarket.com/
---
