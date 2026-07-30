---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Keeptrack Agentic Access
  operation_count: 5
  slug: keeptrack-agentic-access
  summary_line: 5 operations
api_count: 5
apis:
- description: Keep Track is the free, open source tool that makes space exploration accessible to all - professionals and amateurs alike. With its user-friendly interface, you can simulate satellite launches, visua
  name: KeepTrack
  slug: keeptrack
- description: Bulk catalog and listings.
  name: KeepTrack Catalog API
  slug: keeptrack-catalog-api
- description: Retrieve orbital elements (TLE, OMM).
  name: KeepTrack Orbits API
  slug: keeptrack-orbits-api
- description: Compute real-time positions and ephemerides.
  name: KeepTrack Positions API
  slug: keeptrack-positions-api
- description: Search and retrieve catalog data about tracked space objects.
  name: KeepTrack Satellites API
  slug: keeptrack-satellites-api
artifact_total: 12
collections:
- collection_type: open
  name: KeepTrack Space API
  slug: open-keeptrack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/keeptrack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/keeptrack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/keeptrack-authentication.yml
created: '2024-11-07T00:00:00.000Z'
description: Keep Track is the free, open source tool that makes space exploration accessible to all - professionals and amateurs alike. With its user-friendly interface, you can simulate satellite launches, visualize debris patterns, and explore a catalog of 30,000+ real satellites and debris. Zoom through geosynchronous orbits, run collision scenarios, and track debris fragmentation over time.
finops:
- name: Keeptrack Finops
  service_category: API
  slug: keeptrack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keeptrack.png
layout: provider
modified: '2026-04-28'
name: KeepTrack
nav: Providers
network: true
overview: 'KeepTrack publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Orbits API, Positions API, and 1 more. Tagged areas include Satellites and Space.


  KeepTrack''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: Keeptrack Plans Pricing
  plan_count: 3
  slug: keeptrack-plans-pricing
random_paper: 52
rate_limits:
- limit_count: 5
  name: Keeptrack Rate Limits
  slug: keeptrack-rate-limits
score:
  band: thin
  composite: 34.6
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.9
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/keeptrack/refs/heads/main/screenshots/keeptrack-2026-06-20T183941.png
security:
- kind: authentication
  name: Keeptrack Authentication
  slug: keeptrack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Keeptrack Domain Security
  slug: keeptrack-domain-security
  summary_line: TLSv1.3 · DMARC
slug: keeptrack
tags:
- Satellites
- Space
---
