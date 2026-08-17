---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: true
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
  score: 17.1
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 4
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/moss-mcp-integration.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moss-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/moss-a2a.yml
created: '2026-07-17'
description: Moss is a company surfaced as a portfolio company of y-combinator and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: ''
  name: moss-mcp.yml
  slug: moss-mcpyml
modified: '2026-07-17'
name: Moss
nav: Providers
network: true
overview: Moss is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 3
score:
  band: minimal
  composite: 8.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 35.2
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 8.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Moss Authentication
  slug: moss-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Moss Domain Security
  slug: moss-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Moss Trust Center
  slug: moss-trust-center
  summary_line: SOC 2, HIPAA
slug: moss
tags:
- Company
---
