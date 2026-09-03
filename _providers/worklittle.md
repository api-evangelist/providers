---
agent_readiness:
  band: agent-aware
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
  score: 20.7
  scored_at: '2026-09-02'
api_count: 4
apis:
- baseURL: https://api.worklittle.com
  baseurl_source: declared
  description: The Job Boards API from Worklittle — 8 operation(s) for job boards.
  name: Worklittle Job Boards API
  slug: worklittle-job-boards-api
artifact_total: 2
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.worklittle.com/jobs/mcp
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
overview: 'Worklittle publishes 1 API on the [APIs.io](https://apis.io/) network: Job Boards API. Tagged areas include Job Search, ATS, Recruiting, and Workforce Intelligence.'
random_paper: 13
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 4
    catalog_gap: 82.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 40.1
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/worklittle/refs/heads/main/screenshots/worklittle-2026-09-02T170938.png
slug: worklittle
tags:
- Job Search
- ATS
- Recruiting
- Workforce Intelligence
website: https://worklittle.com
---
