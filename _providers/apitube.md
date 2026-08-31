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
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: News search and retrieval — everything, top headlines, trends, companies, journalists, fact-checks and taxonomy suggestion. 26 operations, API key by header or query.
  name: APITube News API
  slug: apitube-news-api
- description: API key balance and subscription plan information.
  name: APITube Account API
  slug: apitube-account-api
- description: Verify factual claims against the live news corpus (retrieval-augmented). Returns per-claim verdicts on an 8-level scale with confidence, explanation, and supporting evidence.
  name: APITube Fact Check API
  slug: apitube-fact-check-api
- description: The Reference API from APITube — 7 operation(s) for reference.
  name: APITube Reference API
  slug: apitube-reference-api
- description: Autocomplete and typeahead suggestions for entities.
  name: APITube Suggest API
  slug: apitube-suggest-api
- description: Health checks and service status.
  name: APITube System API
  slug: apitube-system-api
- description: Helper endpoints for building queries
  name: APITube Utilities API
  slug: apitube-utilities-api
artifact_total: 8
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
overview: APITube publishes 7 APIs on the [APIs.io](https://apis.io/) network, including News API, Account API, Fact Check API, and 4 more. Tagged areas include News, media monitoring, news api, fact check, and journalists.
random_paper: 11
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 4
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 56.7
    developer_ergonomics: 38.1
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 29.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
slug: apitube
tags:
- News
- media monitoring
- news api
- fact check
- journalists
website: https://apitube.io
---
