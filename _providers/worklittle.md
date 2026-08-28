---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.2
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Job discovery, auto-apply, commute search on a geocoded map, plus an employer workspace with postings, ATS pipeline, employees, HR docs and webhooks. 59 operations, bearer auth.
  name: Worklittle API
  slug: worklittle-api
artifact_total: 2
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/worklittle-llms.txt
- group: other
  title: ''
  type: AgentManifest
  url: a2a/worklittle-agent-manifest.json
- group: company
  title: ''
  type: Website
  url: https://worklittle.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.worklittle.com
created: '2026-08-24'
description: 'Worklittle is a workforce-intelligence platform covering job discovery, auto-apply, embedded careers boards, ATS sync and sourcing over one API. It splits into two halves: Jobs, the market-wide index plus candidate-facing apply and document tools including commute search on a geocoded job map, and Business, an employer hiring workspace with postings, an ATS pipeline, employees, HR documents and webhooks. The public contract is an OpenAPI 3.1 document of 59 paths and 59 operations served from api.worklittle.com with bearer authentication. Worklittle also operates an MCP server documented for Cursor, Claude and VS Code, and publishes a 1.4MB agent manifest alongside a 97KB llms.txt.'
layout: provider
mcp_servers:
- description: ''
  name: Worklittle MCP Server
  slug: worklittle-mcp-server
modified: '2026-08-24'
name: Worklittle
nav: Providers
network: true
overview: Worklittle publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Jobs, Recruiting, ATS, Workforce, and MCP.
random_paper: 13
score:
  band: emerging
  composite: 15.0
  delta: -1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 31.3
    developer_ergonomics: 0.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.9
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
slug: worklittle
tags:
- Jobs
- Recruiting
- ATS
- Workforce
- MCP
- Agents
- HR
website: https://worklittle.com
---
