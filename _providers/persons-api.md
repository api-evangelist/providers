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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Persons Api Agentic Access
  operation_count: 6
  slug: persons-api-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: Placing and managing of persons placed for persons.
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
  composite: 25.7
  delta: -1.8
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 63.2
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
