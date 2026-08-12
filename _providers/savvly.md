---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Savvly Agentic Access
  operation_count: 12
  slug: savvly-agentic-access
  summary_line: 12 operations
api_count: 3
apis:
- description: The Comparisons API from Savvly — 2 operation(s) for comparisons.
  name: Savvly Comparisons API
  slug: savvly-comparisons-api
- description: The Product API from Savvly — 6 operation(s) for product.
  name: Savvly Product API
  slug: savvly-product-api
- description: The Projections API from Savvly — 4 operation(s) for projections.
  name: Savvly Projections API
  slug: savvly-projections-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/savvly-compare-and-explain.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/savvly-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/savvly-openapi-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/savvly-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://savvly.com/
created: '2026-07-17'
description: Savvly is a company surfaced as a portfolio company of techstars and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: ''
  name: savvly-mcp.yml
  slug: savvly-mcpyml
modified: '2026-07-17'
name: Savvly
nav: Providers
network: true
overview: 'Savvly publishes 3 APIs on the [APIs.io](https://apis.io/) network: Comparisons API, Product API, and Projections API. Tagged areas include Company.'
random_paper: 97
score:
  band: emerging
  composite: 20.9
  delta: 0.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.5
    developer_ergonomics: 10.3
    discoverability: 40.7
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 20.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: domain-security
  name: Savvly Domain Security
  slug: savvly-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: savvly
tags:
- Company
website: https://savvly.com/
---
