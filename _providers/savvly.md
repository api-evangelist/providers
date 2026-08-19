---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.6
  scored_at: '2026-08-19'
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
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Savvly Public Comparisons API
  slug: open-savvly-comparisons-api
- collection_type: open
  name: Savvly Public Comparisons Product API
  slug: open-savvly-product-api
- collection_type: open
  name: Savvly Public Comparisons Projections API
  slug: open-savvly-projections-api
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
random_paper: 81
score:
  band: emerging
  composite: 19.0
  delta: -1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 50.1
    developer_ergonomics: 1.8
    discoverability: 40.7
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 20.9
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
