---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
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
  score: 13.7
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 4
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/tigris-fork-for-agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tigris-mcp.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/tigris-a2a.yml
created: '2026-07-17'
description: Tigris is a company surfaced as a portfolio company of a16z, general-catalyst and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: ''
  name: tigris-mcp.yml
  slug: tigris-mcpyml
modified: '2026-07-17'
name: Tigris
nav: Providers
network: true
overview: Tigris is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 58
score:
  band: minimal
  composite: 8.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.3
    discoverability: 44.4
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 8.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Tigris Authentication
  slug: tigris-authentication
  summary_line: apiKey/awsSignatureV4 · 1 scheme
- kind: domain-security
  name: Tigris Domain Security
  slug: tigris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tigris Trust Center
  slug: tigris-trust-center
  summary_line: SOC 2
slug: tigris
tags:
- Company
---
