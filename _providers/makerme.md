---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 12.6
  scored_at: '2026-08-11'
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
- description: ''
  name: makerme-mcp.yml
  slug: makerme-mcpyml
modified: '2026-07-17'
name: Maker.me
nav: Providers
network: true
overview: Maker.me is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 42
scopes:
- name: Makerme Scopes
  scope_count: 0
  slug: makerme-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.6
  delta: 0.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 35.2
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 5.0
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
