---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Tano Agentic Access
  operation_count: 17
  slug: tano-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 5
apis:
- description: Brand signups for product offerings (Creator Partnership Ads, Content Analysis Framework, Creator Discovery Guide, USA waitlist).
  name: Tano Brand Signups API
  slug: tano-brand-signups-api
- description: Contact form submissions and updates.
  name: Tano Contact API
  slug: tano-contact-api
- description: Creator-side signups.
  name: Tano Creator Signups API
  slug: tano-creator-signups-api
- description: Static discovery files for AI agents (llms.txt, manifests, sitemap).
  name: Tano Discovery API
  slug: tano-discovery-api
- description: Webinar and event registrations.
  name: Tano Events API
  slug: tano-events-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tano Public Brand Signups API
  slug: open-tano-brand-signups-api
- collection_type: open
  name: Tano Public Brand Signups Contact API
  slug: open-tano-contact-api
- collection_type: open
  name: Tano Public Brand Signups Creator Signups API
  slug: open-tano-creator-signups-api
- collection_type: open
  name: Tano Public Brand Signups Discovery API
  slug: open-tano-discovery-api
- collection_type: open
  name: Tano Public Brand Signups Events API
  slug: open-tano-events-api
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/tano-agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tano-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tano-openapi-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/tano-a2a.yml
- group: company
  title: ''
  type: Website
  url: http://tano.ai
created: '2026-07-17'
description: Tano is a company surfaced as a portfolio company of seedcamp and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline.
layout: provider
mcp_servers:
- description: ''
  name: tano-mcp.yml
  slug: tano-mcpyml
modified: '2026-07-17'
name: Tano
nav: Providers
network: true
overview: Tano publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Brand Signups API, Contact API, Creator Signups API, and 2 more. Tagged areas include Company.
random_paper: 136
score:
  band: emerging
  composite: 19.7
  delta: -1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 16.7
    contract_quality: 53.2
    developer_ergonomics: 1.8
    discoverability: 40.7
    governance: 16.7
    operational_transparency: 0.0
  previous_composite: 21.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Tano Authentication
  slug: tano-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Tano Domain Security
  slug: tano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tano
tags:
- Company
website: http://tano.ai
---
