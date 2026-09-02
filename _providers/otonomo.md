---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Otonomo Agentic Access
  operation_count: 18
  slug: otonomo-agentic-access
  summary_line: 18 operations · 12 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The EU API from Otonomo — 15 operation(s) for eu.
  name: Otonomo EU API
  slug: otonomo-eu-api
- description: The US API from Otonomo — 2 operation(s) for us.
  name: Otonomo US API
  slug: otonomo-us-api
artifact_total: 12
asyncapis:
- description: ''
  name: Otonomo Events Webhooks
  slug: otonomo-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Otonomo Fleet EU API
  slug: open-otonomo-eu-api
- collection_type: open
  name: Otonomo Fleet EU US API
  slug: open-otonomo-us-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/otonomo-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/otonomo-check-vehicle-connectivity.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/otonomo-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/otonomo-fleet-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/otonomo-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/otonomo-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://otonomo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.otonomo.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.otonomo.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.otonomo.io/docs/consumption-methods
- group: operate
  title: ''
  type: Support
  url: mailto:support@otonomo.io
- group: build
  title: ''
  type: Postman
  url: https://docs.otonomo.io/docs/postman-collection-get-car-status
- group: build
  title: ''
  type: Packages
  url: packages/otonomo-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/otonomo-domain-security.yml
created: '2026-07-17'
description: Otonomo operates a connected-vehicle data platform that aggregates, normalizes and delivers telematics and mobility data from millions of connected cars to fleets, insurers, cities and mobility developers. Its Fleet ("Personal Data for Fleets") API exposes OAuth2-secured endpoints for vehicle onboarding (VIN upload / enablement / consent), near-real-time vehicle status, historical fleet points and trips reporting, connectivity checks, an attribute explorer, custom event rules with callbacks, and a streaming interface — across separate US and EU data regions. Otonomo was acquired by Urgently (Urgent.ly) in 2023; the connected-car Fleet data API remains operational and documented on ReadMe at docs.otonomo.io. Originally surfaced as a Bessemer Venture Partners portfolio company and enriched from its live developer surface.
image: https://otonomo.io/
layout: provider
mcp_servers:
- description: ''
  name: Otonomo MCP Server
  slug: otonomo-mcp-server
modified: '2026-07-20'
name: Otonomo
nav: Providers
network: true
overview: 'Otonomo publishes 2 APIs on the [APIs.io](https://apis.io/) network: EU API and US API. Tagged areas include Company, Connected Vehicles, Automotive, Fleet Management, and Telematics.


  The Otonomo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Otonomo''s developer surface includes documentation, API reference, getting-started guide, support, and 10 more developer resources.'
random_paper: 2
rate_limits:
- limit_count: 0
  name: Otonomo Rate Limits
  slug: otonomo-rate-limits
scopes:
- name: Otonomo Scopes
  scope_count: 0
  slug: otonomo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 61.7
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Otonomo Authentication
  slug: otonomo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Otonomo Domain Security
  slug: otonomo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: otonomo
tags:
- Company
- Connected Vehicles
- Automotive
- Fleet Management
- Telematics
- Vehicle Data
- Mobility
- IoT
- Location
- Connected Car
website: https://otonomo.io/
---
