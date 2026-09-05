---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Persons Api Agentic Access
  operation_count: 6
  slug: persons-api-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: http://apis.example.com
  baseurl_source: declared
  description: Placing and managing of persons placed for persons.
  name: Persons Persons API
  slug: persons-api-persons-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Persons API
  slug: open-persons-api-persons-api
- collection_type: open
  name: Persons API
  slug: open-persons-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/persons-api-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/persons-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: http://apievangelist.com
created: '2024-12-29'
description: This is a template APIs.json for a persons API, to be used in storytelling, training, and knowledge bases.
finops:
- name: Persons Api Finops
  service_category: API
  slug: persons-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/persons-api.png
layout: provider
modified: '2026-05-19'
name: Persons
nav: Providers
network: true
overview: 'Persons publishes 1 API on the [APIs.io](https://apis.io/) network: Persons API. Tagged areas include Application Programming Interface and Persons.


  Persons'' developer surface includes authentication and 2 more developer resources.'
plans:
- name: Persons Api Plans Pricing
  plan_count: 3
  slug: persons-api-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Persons Api Rate Limits
  slug: persons-api-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 61.5
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 25.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/persons-api/refs/heads/main/screenshots/persons-api-2026-06-20T191617.png
security:
- kind: authentication
  name: Persons Api Authentication
  slug: persons-api-authentication
  summary_line: apiKey · 1 scheme
slug: persons-api
tags:
- Application Programming Interface
- Persons
website: http://apievangelist.com
---
