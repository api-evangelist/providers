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
  url: https://forgeglobal.com/aspiration_stock/
coverage:
  checked: '2026-08-06'
  detail: GreenFi ships only consumer banking apps — its 178-URL sitemap contains no developer, API or integration page, and api.greenfi.com answers a bare "{}" at the root while returning 403 for /openapi.json, /graphql and every /.well-known/ path.
  evidence:
  - status: 200
    url: https://www.greenfi.com/sitemap.xml
  - status: 403
    url: https://api.greenfi.com/openapi.json
  - status: 403
    url: https://www.greenfi.com/.well-known/agent-card.json
  - status: 403
    url: https://www.greenfi.com/llms.txt
  - status: 0
    url: https://developer.greenfi.com/
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'GreenFi is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-08-06'
name: GreenFi
nav: Providers
network: true
overview: GreenFi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 65
score:
  band: minimal
  composite: 3.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.2
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
slug: aspiration
tags:
- Company
website: https://forgeglobal.com/aspiration_stock/
---
