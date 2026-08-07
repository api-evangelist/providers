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
  url: https://forgeglobal.com/astrobotic_stock/
coverage:
  checked: '2026-08-06'
  detail: Astrobotic sells lunar delivery missions, landers, rovers and surface power hardware; its entire public web presence is a 27-page WordPress marketing site with no developer, docs or API section, and every contract-discovery probe (well-known, openapi, llms.txt, api/docs/developer subdomains) missed on both www.astrobotic.com and astrobotic.com.
  evidence:
  - status: 200
    url: https://www.astrobotic.com/
  - status: 404
    url: https://www.astrobotic.com/developers
  - status: 404
    url: https://www.astrobotic.com/openapi.json
  - status: 404
    url: https://www.astrobotic.com/.well-known/agent-card.json
  - status: 404
    url: https://www.astrobotic.com/.well-known/security.txt
  - status: 404
    url: https://www.astrobotic.com/llms.txt
  - status: 0
    url: https://api.astrobotic.com/
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Astrobotic is a company surfaced via the API Evangelist harvest backlog (source: secondary-market) and added to the network as a stub for full-pipeline profiling.'
layout: provider
modified: '2026-08-06'
name: Astrobotic
nav: Providers
network: true
overview: Astrobotic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 65
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
slug: astrobotic
tags:
- Company
website: https://forgeglobal.com/astrobotic_stock/
---
