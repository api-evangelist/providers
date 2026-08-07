---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Generated REST API over a connected database — full CRUD across chosen tables, with auth, pagination and docs handled by the platform.
  name: AmunCore API
  slug: amuncore-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://amuncore.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amuncore-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amuncore-authentication.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/amuncore-plans.yml
created: '2026-08-03'
description: 'AmunCore turns a database into a secure REST API without writing a backend. You connect a database, pick tables, and endpoints go live with routing, authentication, validation, pagination, joins, errors, logs and docs already handled — the layer between a database and HTTP that would otherwise be a two-to-six-week project. It supports SQL Server, MySQL, MariaDB, PostgreSQL, Oracle and SQLite, with a visual builder that is the same regardless of the engine underneath. It is MCP-native by design: the endpoints you build become tools an AI assistant can call under the same keys, permissions and audit trail, and the MCP endpoint is live and token-gated. Full CRUD, a free plan, and Bearer API keys.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amuncore.png
layout: provider
mcp_servers:
- description: ''
  name: amuncore-mcp.yml
  slug: amuncore-mcpyml
modified: '2026-08-03'
name: AmunCore
nav: Providers
network: true
overview: 'AmunCore publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database, API Management, Backend, No Code, and SQL.


  AmunCore''s developer surface includes authentication and 3 more developer resources.'
plans:
- name: Amuncore Plans
  plan_count: 0
  slug: amuncore-plans
random_paper: 67
score:
  band: minimal
  composite: 10.8
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  provenance:
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Amuncore Authentication
  slug: amuncore-authentication
  summary_line: 2 schemes
slug: amuncore
tags:
- Database
- API Management
- Backend
- No Code
- SQL
- PostgreSQL
- MySQL
- Oracle
- MCP
- Agents
- Data
website: https://amuncore.com
---
