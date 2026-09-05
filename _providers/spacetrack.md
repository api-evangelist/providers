---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - security
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Spacetrack Agentic Access
  operation_count: 22
  slug: spacetrack-agentic-access
  summary_line: 22 operations · 1 acting
api_count: 1
apis:
- baseURL: https://www.space-track.org
  baseurl_source: declared
  description: Launch sites, boxscore, announcements, and other reference data
  name: Space-Track Ancillary API
  slug: spacetrack-ancillary-api
- baseURL: https://www.space-track.org
  baseurl_source: declared
  description: Session-based authentication via cookie
  name: Space-Track Authentication API
  slug: spacetrack-authentication-api
- baseURL: https://www.space-track.org
  baseurl_source: declared
  description: Spaceflight safety conjunction data messages (CDM)
  name: Space-Track Conjunction Data API
  slug: spacetrack-conjunction-data-api
- baseURL: https://www.space-track.org
  baseurl_source: declared
  description: Satellite reentry and decay predictions
  name: Space-Track Decay Predictions API
  slug: spacetrack-decay-predictions-api
- baseURL: https://www.space-track.org
  baseurl_source: declared
  description: Current and historical SGP4 keplerian element sets (TLE/OMM)
  name: Space-Track General Perturbations API
  slug: spacetrack-general-perturbations-api
- baseURL: https://www.space-track.org
  baseurl_source: declared
  description: Catalog metadata for all tracked Earth-orbiting objects
  name: Space-Track Satellite Catalog API
  slug: spacetrack-satellite-catalog-api
- baseURL: https://www.space-track.org
  baseurl_source: declared
  description: Reentry tracking and impact prediction messages (TIP)
  name: Space-Track Tracking and Impact Prediction API
  slug: spacetrack-tracking-and-impact-prediction-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Space-Track Ancillary API
  slug: open-spacetrack-ancillary-api
- collection_type: open
  name: Space-Track Ancillary Authentication API
  slug: open-spacetrack-authentication-api
- collection_type: open
  name: Space-Track Ancillary Conjunction Data API
  slug: open-spacetrack-conjunction-data-api
- collection_type: open
  name: Space-Track Ancillary Decay Predictions API
  slug: open-spacetrack-decay-predictions-api
- collection_type: open
  name: Space-Track Ancillary General Perturbations API
  slug: open-spacetrack-general-perturbations-api
- collection_type: open
  name: Space-Track Ancillary Satellite Catalog API
  slug: open-spacetrack-satellite-catalog-api
- collection_type: open
  name: Space-Track Ancillary Tracking and Impact Prediction API
  slug: open-spacetrack-tracking-and-impact-prediction-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spacetrack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spacetrack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spacetrack-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.space-track.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.space-track.org/documentation
- group: start
  title: ''
  type: Login
  url: https://www.space-track.org/auth/login
- group: other
  title: ''
  type: Registration
  url: https://www.space-track.org/auth/createAccount
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.space-track.org/documentation#user-agreement
- group: operate
  title: ''
  type: Contact
  url: https://www.space-track.org/contactus/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/finops/finops.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/openapi/openapi.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/json-ld/context.jsonld
created: '2026-06-13'
description: US military space surveillance REST API providing Two-Line Element (TLE) sets, conjunction data messages, orbital element sets, satellite catalog data, and decay predictions for tracked satellites and debris operated by the 18th Space Control Squadron.
examples:
- key_count: 4
  name: Cdm Query
  slug: cdm-query
- key_count: 3
  name: Gp Iss
  slug: gp-iss
- key_count: 4
  name: Login
  slug: login
- key_count: 3
  name: Satcat Query
  slug: satcat-query
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.space-track.org/favicon.ico
json_schemas:
- name: GP Record
  property_count: 33
  slug: gp-record
- name: SATCAT Record
  property_count: 24
  slug: satcat-record
jsonld:
- class_count: 0
  name: context Context
  property_count: 43
  slug: context
layout: provider
modified: '2026-06-13'
name: Space-Track
nav: Providers
network: true
overview: 'Space-Track publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Ancillary API, Authentication API, Conjunction Data API, and 4 more. Tagged areas include Space, Satellites, TLE, Orbital Data, and Space Surveillance.


  The Space-Track catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Space-Track''s developer surface includes authentication, developer portal, documentation, and 11 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 7
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Space-Track API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spacetrack-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 74.3
    catalog_earned_first_party: 0.0
    catalog_gap: 40.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 25.0
    contract_quality: 69.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 0.0
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spacetrack/refs/heads/main/screenshots/spacetrack-2026-06-20T194237.png
security:
- kind: authentication
  name: Spacetrack Authentication
  slug: spacetrack-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spacetrack Domain Security
  slug: spacetrack-domain-security
  summary_line: TLSv1.3
slug: spacetrack
tags:
- Space
- Satellites
- TLE
- Orbital Data
- Space Surveillance
- Debris Tracking
- Conjunction Data
- US Military
website: https://www.space-track.org
---
