---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Iss Api Agentic Access
  operation_count: 4
  slug: iss-api-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Returns a JSON object containing the total count of humans currently in space and an array of crew member objects, each with the person's name and the spacecraft they are aboard. Covers all crewed spa
  name: People in Space Right Now
  slug: astronauts-in-space
- baseURL: http://api.open-notify.org
  baseurl_source: declared
  description: Endpoints for retrieving information about humans currently in space
  name: ISS Location API (Open Notify) Astronauts API
  slug: iss-api-astronauts-api
- baseURL: http://api.open-notify.org
  baseurl_source: declared
  description: Endpoints for retrieving the current position of the International Space Station
  name: ISS Location API (Open Notify) ISS Location API
  slug: iss-api-iss-location-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ISS Location API (Open Notify) Astronauts API
  slug: open-iss-api-astronauts-api
- collection_type: open
  name: API (Open Notify) Astronauts ISS Location API
  slug: open-iss-api-iss-location-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/open-notify/Open-Notify-API/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/iss-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iss-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://open-notify.org/
- group: docs
  title: ''
  type: Documentation
  url: http://open-notify.org/Open-Notify-API/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/open-notify/Open-Notify-API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/open-notify
- group: docs
  title: ''
  type: ReadTheDocs
  url: https://open-notify-api.readthedocs.io/en/latest/
- group: commercial
  title: ''
  type: License
  url: https://github.com/open-notify/Open-Notify-API/blob/master/LICENSE
created: '2026-06-13'
description: Open Notify is a free, open-source project by Nathan Bergey that exposes real-time NASA and ISS data as simple REST endpoints. The service provides the current latitude and longitude of the International Space Station (updated every five seconds as the ISS travels at roughly 28,000 km/h), a count and roster of all humans currently in space across all spacecraft, and historical ISS pass-time predictions for any point on Earth. All endpoints are unauthenticated, return JSON, and are free to use without registration. The ISS pass-time prediction endpoint has been retired; the location and astronaut endpoints remain live and operational.
examples:
- key_count: 3
  name: Astronauts Response
  slug: astronauts-response
- key_count: 3
  name: Iss Location Response
  slug: iss-location-response
finops:
- name: Iss Api Finops
  service_category: Public Open Data / Space Technology
  slug: iss-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iss-api.png
json_schemas:
- name: Astronauts Response
  property_count: 3
  slug: astronauts-response
- name: ISS Location Response
  property_count: 3
  slug: iss-location-response
jsonld:
- class_count: 0
  name: context Context
  property_count: 9
  slug: context
layout: provider
modified: '2026-06-13'
name: ISS Location API (Open Notify)
nav: Providers
network: true
overview: 'ISS Location API (Open Notify) publishes 2 APIs on the [APIs.io](https://apis.io/) network: Astronauts API and ISS Location API. Tagged areas include Space, ISS, International Space Station, NASA, and Location.


  The ISS Location API (Open Notify) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ISS Location API (Open Notify)''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Iss Api Plans
  plan_count: 1
  slug: iss-api-plans
random_paper: 1
rate_limits:
- limit_count: 2
  name: Iss Api Rate Limits
  slug: iss-api-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: ISS Location API (Open Notify) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: iss-api-jsonschema-spectral-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 50.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 53.7
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iss-api/refs/heads/main/screenshots/iss-api-2026-06-20T183624.png
security:
- kind: domain-security
  name: Iss Api Domain Security
  slug: iss-api-domain-security
  summary_line: no transport/DNS hardening detected
slug: iss-api
tags:
- Space
- ISS
- International Space Station
- NASA
- Location
- Geolocation
- Astronauts
- Real-Time
- Open-Source
- Public API
- Free
website: http://open-notify.org/
---
