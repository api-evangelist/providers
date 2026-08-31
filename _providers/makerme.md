---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 4
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/makerme-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/makerme-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://maker.co
created: '2026-07-17'
description: Maker.me is a company surfaced as a portfolio company of 500-global and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: Maker publishes an official hosted, remote MCP (Model Context Protocol) server that connects AI assistants directly to a user's Maker account. The assistant can do roughly anything a user can do in th
  name: Maker MCP Server
  slug: maker-mcp-server
modified: '2026-07-17'
name: Maker.me
nav: Providers
network: true
overview: Maker.me is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 3
scopes:
- name: Makerme Scopes
  scope_count: 0
  slug: makerme-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 100.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.2
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 4.1
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/makerme/refs/heads/main/screenshots/makerme-2026-07-25T225948.png
security:
- kind: authentication
  name: Makerme Authentication
  slug: makerme-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Makerme Domain Security
  slug: makerme-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: makerme
tags:
- Company
website: https://maker.co
---
