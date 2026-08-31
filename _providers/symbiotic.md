---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.1
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Symbiotic Agentic Access
  operation_count: 22
  slug: symbiotic-agentic-access
  summary_line: 22 operations · 1 acting
api_count: 2
apis:
- description: The SymbioticAPIService API from Symbiotic — 22 operation(s) for symbioticapiservice.
  name: Symbiotic SymbioticAPIService API
  slug: symbiotic-symbioticapiservice-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: v1/api.proto SymbioticAPIService API
  slug: open-symbiotic-symbioticapiservice-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/symbiotic-query-validator-set.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/symbiotic-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/symbiotic-relay-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/symbiotic-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://symbiotic.fi
created: '2026-07-17'
description: 'Symbiotic is a company surfaced as a portfolio company of paradigm and added to the API Evangelist network as a stub for enrichment. Sector: crypto-defi. This profile is a lead awaiting the enrichment pipeline.'
layout: provider
mcp_servers:
- description: ''
  name: Symbiotic MCP Server
  slug: symbiotic-mcp-server
modified: '2026-07-17'
name: Symbiotic
nav: Providers
network: true
overview: 'Symbiotic publishes 1 API on the [APIs.io](https://apis.io/) network: SymbioticAPIService API. Tagged areas include Company and Crypto Defi.'
random_paper: 13
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 95.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 36.1
    developer_ergonomics: 1.8
    discoverability: 44.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 14.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Symbiotic Domain Security
  slug: symbiotic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Symbiotic Vulnerability Disclosure
  slug: symbiotic-vulnerability-disclosure
  summary_line: disclosure policy published
slug: symbiotic
tags:
- Company
- Crypto Defi
website: https://symbiotic.fi
---
