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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
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
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: KeepTrack Space Catalog API
  slug: open-keeptrack-catalog-api
- collection_type: open
  name: KeepTrack Space Catalog Orbits API
  slug: open-keeptrack-orbits-api
- collection_type: open
  name: KeepTrack Space Catalog Positions API
  slug: open-keeptrack-positions-api
- collection_type: open
  name: KeepTrack Space Catalog Satellites API
  slug: open-keeptrack-satellites-api
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
random_paper: 60
rate_limits:
- limit_count: 5
  name: Keeptrack Rate Limits
  slug: keeptrack-rate-limits
score:
  band: thin
  composite: 26.5
  delta: -0.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 53.8
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
