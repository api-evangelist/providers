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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Tano Agentic Access
  operation_count: 17
  slug: tano-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 1
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
  name: Tano
  slug: tano
modified: '2026-07-17'
name: Tano
nav: Providers
network: true
overview: Tano publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Brand Signups API, Contact API, Creator Signups API, and 2 more. Tagged areas include Company.
random_paper: 14
score:
  band: emerging
  composite: 17.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 100.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 51.8
    developer_ergonomics: 1.8
    discoverability: 35.2
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 17.9
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
