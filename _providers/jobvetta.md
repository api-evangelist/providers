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
  scored_at: '2026-08-03'
api_count: 2
apis:
- description: REST access to live, vetted India job openings. `GET /jobs` searches by keyword (`q`), Indian city or state (`location`), posting age in days (`days`, 1–365) and result count (`limit`, 1–20, default 1
  name: Jobvetta REST API
  slug: jobvetta-rest-api
- description: 'Hosted MCP server over Streamable HTTP with two tools — `search_jobs` (q, location, days, limit) and `get_job` (job_id). Discovery is public: tools/list answers without credentials, so a client can en'
  name: Jobvetta MCP Server
  slug: jobvetta-mcp-server
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.jobvetta.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.jobvetta.com/api
- group: start
  title: ''
  type: SignUp
  url: https://www.jobvetta.com/dashboard
created: '2026-08-02'
description: 'Jobvetta is a jobs API for India — live openings gathered and checked against official employer sources, exposed as a REST API and a hosted MCP server that share one key. Search by keyword, Indian city or state, and posting age; fetch full structured detail for a single job. It is India-only by design: non-Indian locations return no results. The MCP server answers tools/list without credentials, so an agent can discover the two tools before signing up, and installation is a single documented `claude mcp add` command. Free during early access, with a shared limit of 50 tool calls per day and up to 20 jobs per search across both surfaces.'
layout: provider
modified: '2026-08-02'
name: Jobvetta
nav: Providers
network: true
overview: 'Jobvetta publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Jobs, Recruitment, Job Search, India, and Employment.


  Jobvetta''s developer surface includes documentation, signup flow, and 1 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 10.3
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.9
  scored_at: '2026-08-03'
slug: jobvetta
tags:
- Jobs
- Recruitment
- Job Search
- India
- Employment
- MCP
- Agent-native
- Developer Tools
website: https://www.jobvetta.com
---
