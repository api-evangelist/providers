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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Keeptrack Agentic Access
  operation_count: 5
  slug: keeptrack-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- description: Keep Track is the free, open source tool that makes space exploration accessible to all - professionals and amateurs alike. With its user-friendly interface, you can simulate satellite launches, visua
  name: KeepTrack
  slug: keeptrack
- baseURL: https://www.keeptrack.space/api
  baseurl_source: declared
  description: Bulk catalog and listings.
  name: KeepTrack Catalog API
  slug: keeptrack-catalog-api
- baseURL: https://www.keeptrack.space/api
  baseurl_source: declared
  description: Retrieve orbital elements (TLE, OMM).
  name: KeepTrack Orbits API
  slug: keeptrack-orbits-api
- baseURL: https://www.keeptrack.space/api
  baseurl_source: declared
  description: Compute real-time positions and ephemerides.
  name: KeepTrack Positions API
  slug: keeptrack-positions-api
- baseURL: https://www.keeptrack.space/api
  baseurl_source: declared
  description: Search and retrieve catalog data about tracked space objects.
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
random_paper: 9
rate_limits:
- limit_count: 5
  name: Keeptrack Rate Limits
  slug: keeptrack-rate-limits
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 13.1
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 17.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
