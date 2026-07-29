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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 12
  human_in_the_loop: 1
  name: Otonomo Agentic Access
  operation_count: 18
  slug: otonomo-agentic-access
  summary_line: 18 operations · 12 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The EU API from Otonomo — 15 operation(s) for eu.
  name: Otonomo EU API
  slug: otonomo-eu-api
- description: The US API from Otonomo — 2 operation(s) for us.
  name: Otonomo US API
  slug: otonomo-us-api
artifact_total: 8
asyncapis:
- description: ''
  name: Otonomo Events Webhooks
  slug: otonomo-events-webhooks
common:
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
modified: '2026-07-20'
name: Otonomo
nav: Providers
network: true
overview: 'Otonomo publishes 2 APIs on the [APIs.io](https://apis.io/) network: EU API and US API. Tagged areas include Company, Connected Vehicles, Automotive, Fleet Management, and Telematics.


  The Otonomo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Otonomo''s developer surface includes documentation, API reference, getting-started guide, support, and 6 more developer resources.'
random_paper: 50
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
  composite: 35.0
  delta: 1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 72.0
    developer_ergonomics: 34.8
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 33.9
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
