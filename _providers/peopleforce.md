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
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Peopleforce Agentic Access
  operation_count: 15
  slug: peopleforce-agentic-access
  summary_line: 15 operations · 4 acting
api_count: 7
apis:
- description: Recruitment candidate management.
  name: PeopleForce Candidates API
  slug: peopleforce-candidates-api
- description: Departments within the organization.
  name: PeopleForce Departments API
  slug: peopleforce-departments-api
- description: Divisions within the organization.
  name: PeopleForce Divisions API
  slug: peopleforce-divisions-api
- description: Employee profiles, positions, and compensation.
  name: PeopleForce Employees API
  slug: peopleforce-employees-api
- description: Time off and leave management.
  name: PeopleForce Leave Requests API
  slug: peopleforce-leave-requests-api
- description: Job positions.
  name: PeopleForce Positions API
  slug: peopleforce-positions-api
- description: Open positions and vacancies.
  name: PeopleForce Vacancies API
  slug: peopleforce-vacancies-api
artifact_total: 14
collections:
- collection_type: open
  name: PeopleForce API
  slug: open-peopleforce
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/peopleforce-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peopleforce-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/peopleforce-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://peopleforce.io/blog
created: '2025-02-08'
description: PeopleForce is an HR platform whose REST API allows retrieving information about HR entities such as employees, candidates, vacancies, leave requests, departments, divisions, and positions, and performing actions on them.
finops:
- name: Peopleforce Finops
  service_category: API
  slug: peopleforce-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peopleforce.png
layout: provider
modified: '2026-05-19'
name: PeopleForce
nav: Providers
network: true
overview: 'PeopleForce publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Candidates API, Departments API, Divisions API, and 4 more. Tagged areas include HR, Human Resources, Recruitment, and Employees.


  PeopleForce''s developer surface includes authentication, engineering blog, and 2 more developer resources.'
plans:
- name: Peopleforce Plans Pricing
  plan_count: 3
  slug: peopleforce-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Peopleforce Rate Limits
  slug: peopleforce-rate-limits
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.7
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peopleforce/refs/heads/main/screenshots/peopleforce-2026-06-20T191548.png
security:
- kind: authentication
  name: Peopleforce Authentication
  slug: peopleforce-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Peopleforce Domain Security
  slug: peopleforce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peopleforce
tags:
- HR
- Human Resources
- Recruitment
- Employees
---
