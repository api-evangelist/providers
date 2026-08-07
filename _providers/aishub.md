---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aishub Agentic Access
  operation_count: 2
  slug: aishub-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Metadata about the receiving stations that make up the network.
  name: AISHub Stations API
  slug: aishub-stations-api
- description: Latest known positions and voyage data for vessels tracked by the network.
  name: AISHub Vessel Positions API
  slug: aishub-vessel-positions-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aishub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aishub-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aishub.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aishub.net/api
- group: start
  title: ''
  type: SignUp
  url: https://www.aishub.net/join-us
- group: other
  title: ''
  type: Coverage
  url: https://www.aishub.net/coverage
- group: commercial
  title: ''
  type: Plans
  url: plans/aishub-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aishub-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aishub-finops.yml
created: '2026-07-11'
description: AISHub is a cooperative AIS (Automatic Identification System) data sharing network for vessel tracking. Members who contribute a raw NMEA AIS feed from their own receiver (via UDP) get free access in return - a real-time aggregated feed from 1,500+ stations across 80 countries, plus an HTTP web service that returns vessel positions and station metadata as XML, JSON, or CSV. There is no pay-for-access tier; API credentials are earned by sharing a feed that meets coverage and uptime quality thresholds.
finops:
- name: Aishub Finops
  service_category: Analytics and Data Streaming
  slug: aishub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aishub.png
layout: provider
modified: '2026-07-11'
name: AISHub
nav: Providers
network: true
overview: 'AISHub publishes 2 APIs on the [APIs.io](https://apis.io/) network: Stations API and Vessel Positions API. Tagged areas include Vessel Tracking, Maritime, AIS, Shipping, and Geospatial.


  AISHub''s developer surface includes documentation, signup flow, and 7 more developer resources.'
plans:
- name: Aishub Plans Pricing
  plan_count: 1
  slug: aishub-plans-pricing
random_paper: 71
rate_limits:
- limit_count: 3
  name: Aishub Rate Limits
  slug: aishub-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 55.0
    developer_ergonomics: 8.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aishub/refs/heads/main/screenshots/aishub-2026-07-25T195448.png
security:
- kind: domain-security
  name: Aishub Domain Security
  slug: aishub-domain-security
  summary_line: TLSv1.3
slug: aishub
tags:
- Vessel Tracking
- Maritime
- AIS
- Shipping
- Geospatial
- Data Sharing
website: https://www.aishub.net/
---
