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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.0
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: News search and retrieval — everything, top headlines, trends, companies, journalists, fact-checks and taxonomy suggestion. 26 operations, API key by header or query.
  name: APITube News API
  slug: apitube-news-api
artifact_total: 2
common:
- group: other
  title: ''
  type: APICatalog
  url: well-known/apitube-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/apitube-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/apitube-mcp-server-card.json
- group: company
  title: ''
  type: Website
  url: https://apitube.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.apitube.io
created: '2026-08-21'
description: APITube is a news data API providing search and retrieval across news articles, top headlines, trends, companies, journalists, and fact-checks, with taxonomy resolution for entities, topics and locations. The public contract is an OpenAPI 3.1 document of 26 operations served from api.apitube.io, authenticated with an API key by header or query parameter. APITube also operates a first-party MCP server at mcp.apitube.io over streamable HTTP, whose tool list is readable anonymously, and publishes an RFC 9727 api-catalog linkset at the apex that names the specification, the documentation, the llms.txt and the MCP server card.
layout: provider
mcp_servers:
- description: Search and filter global news articles by language, category, sentiment, entities, media and more.
  name: APITube MCP Server
  slug: apitube-mcp-server
modified: '2026-08-21'
name: APITube
nav: Providers
network: true
overview: 'APITube publishes 1 API on the [APIs.io](https://apis.io/) network: News API. Tagged areas include News, Media, Data, Search, and Fact Checking.'
random_paper: 11
score:
  band: thin
  composite: 28.6
  delta: 5.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 57.1
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.8
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
slug: apitube
tags:
- News
- Media
- Data
- Search
- Fact Checking
- Entities
- MCP
- Agents
website: https://apitube.io
---
