---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.2
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 4
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/superset-create-workspace-and-run-agent.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superset-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/superset-a2a.yml
created: '2026-07-17'
description: Superset is a company surfaced as a portfolio company of y-combinator and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: ''
  name: Superset MCP Server
  slug: superset-mcp-server
modified: '2026-07-17'
name: Superset
nav: Providers
network: true
overview: Superset is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 9
scopes:
- name: Superset Scopes
  scope_count: 4
  slug: superset-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: minimal
  composite: 7.2
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.8
    discoverability: 46.3
    governance: 18.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 7.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Superset Authentication
  slug: superset-authentication
  summary_line: oauth2/openIdConnect/apiKey · 3 schemes
- kind: domain-security
  name: Superset Domain Security
  slug: superset-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: superset
tags:
- Company
---
