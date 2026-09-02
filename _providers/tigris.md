---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.0
  scored_at: '2026-09-01'
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
  name: Tigris MCP Server
  slug: tigris-mcp-server
modified: '2026-07-17'
name: Tigris
nav: Providers
network: true
overview: Tigris is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 7
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 15
    catalog_gap: 95.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 1.8
    discoverability: 44.4
    governance: 18.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 7.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
