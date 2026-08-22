---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 30
  human_in_the_loop: 4
  name: Uc Davis Agentic Access
  operation_count: 81
  slug: uc-davis-agentic-access
  summary_line: 81 operations · 30 acting · 4 human-in-the-loop
api_count: 12
apis:
- description: Information and Educational Technology (IET) Middleware Web Service APIs provide campus integration and identity-related middleware services. Usage instructions are published via the IET Application D
  name: IET Middleware Web Service APIs
  slug: iet-middleware
- description: 'UC Davis Health offers Epic (EHR), HL7 FHIR, and custom APIs accessed via SOAP or REST using JSON/XML. Authentication methods include API Key, OAuth2, and Direct Interconnect for existing Epic users, '
  name: UC Davis Health Systems Integration APIs
  slug: health-integration
- description: The CAES Computing Resources Unit publishes the ACE API with documentation supporting college administrative and content workflows.
  name: CAES ACE API
  slug: ace
- description: The Access API from University of California, Davis — 10 operation(s) for access.
  name: University of California, Davis Access API
  slug: uc-davis-access-api
- description: The Documents API from University of California, Davis — 6 operation(s) for documents.
  name: University of California, Davis Documents API
  slug: uc-davis-documents-api
- description: The Equipment API from University of California, Davis — 17 operation(s) for equipment.
  name: University of California, Davis Equipment API
  slug: uc-davis-equipment-api
- description: The Keys API from University of California, Davis — 10 operation(s) for keys.
  name: University of California, Davis Keys API
  slug: uc-davis-keys-api
- description: The KeySerials API from University of California, Davis — 11 operation(s) for keyserials.
  name: University of California, Davis KeySerials API
  slug: uc-davis-keyserials-api
- description: The People API from University of California, Davis — 4 operation(s) for people.
  name: University of California, Davis People API
  slug: uc-davis-people-api
- description: The PeopleAdmin API from University of California, Davis — 4 operation(s) for peopleadmin.
  name: University of California, Davis PeopleAdmin API
  slug: uc-davis-peopleadmin-api
- description: The Spaces API from University of California, Davis — 6 operation(s) for spaces.
  name: University of California, Davis Spaces API
  slug: uc-davis-spaces-api
- description: The Workstations API from University of California, Davis — 13 operation(s) for workstations.
  name: University of California, Davis Workstations API
  slug: uc-davis-workstations-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PEAKS API v1 Access API
  slug: open-uc-davis-access-api
- collection_type: open
  name: PEAKS API v1 Access Documents API
  slug: open-uc-davis-documents-api
- collection_type: open
  name: PEAKS API v1 Access Equipment API
  slug: open-uc-davis-equipment-api
- collection_type: open
  name: PEAKS API v1 Access Keys API
  slug: open-uc-davis-keys-api
- collection_type: open
  name: PEAKS API v1 Access KeySerials API
  slug: open-uc-davis-keyserials-api
- collection_type: open
  name: PEAKS API v1 Access People API
  slug: open-uc-davis-people-api
- collection_type: open
  name: PEAKS API v1 Access PeopleAdmin API
  slug: open-uc-davis-peopleadmin-api
- collection_type: open
  name: PEAKS API v1 Access Spaces API
  slug: open-uc-davis-spaces-api
- collection_type: open
  name: PEAKS API v1 Access Workstations API
  slug: open-uc-davis-workstations-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uc-davis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uc-davis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uc-davis-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucdavis.edu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ucdavis.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/ucdavis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/uc-davis/
- group: operate
  title: ''
  type: Status
  url: https://status.ucdavis.edu/
- group: commercial
  title: ''
  type: Plans
  url: plans/uc-davis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uc-davis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uc-davis-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The University of California, Davis (UC Davis) is a public land-grant research university located in Davis, California, and ranked #48 in the QS World University Rankings 2025. Its public developer footprint is decentralized across campus units rather than a single unified developer portal. Confirmed surfaces include IET Middleware Web Service APIs (identity/integration middleware), a UC Davis Health systems-integration program offering Epic/FHIR and custom REST/SOAP APIs, the CAES Computing Resources Unit APIs (PEAKS, ACE), an internal developer SIG community at developers.ucdavis.edu, and the official ucdavis GitHub organization with 441+ public repositories. Most administrative and identity APIs are gated behind institutional affiliation, SSO, or partner agreements rather than open self-service signup.'
examples:
- key_count: 4
  name: Uc Davis Equipment Create Example
  slug: uc-davis-equipment-create-example
- key_count: 4
  name: Uc Davis Keys List Example
  slug: uc-davis-keys-list-example
finops:
- name: Uc Davis Finops
  service_category: Education
  slug: uc-davis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uc-davis.png
json_schemas:
- name: PEAKS Equipment
  property_count: 15
  slug: uc-davis-equipment
- name: PEAKS Key
  property_count: 8
  slug: uc-davis-key
- name: PEAKS Person
  property_count: 14
  slug: uc-davis-person
- name: PEAKS Space
  property_count: 18
  slug: uc-davis-space
json_structures:
- name: Uc Davis Equipment Structure
  property_count: 15
  slug: uc-davis-equipment-structure
- name: Uc Davis Key Structure
  property_count: 8
  slug: uc-davis-key-structure
jsonld:
- class_count: 33
  name: Uc Davis Context
  property_count: 1
  slug: uc-davis-context
layout: provider
modified: '2026-06-03'
name: University of California, Davis
nav: Providers
network: true
overview: 'University of California, Davis publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Access API, Documents API, Equipment API, and 6 more. Tagged areas include Education, Higher Education, University, Research, and United States.


  The University of California, Davis catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  University of California, Davis'' developer surface includes authentication, GitHub presence, status page, and 9 more developer resources.'
plans:
- name: Uc Davis Plans Pricing
  plan_count: 2
  slug: uc-davis-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Uc Davis Rate Limits
  slug: uc-davis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: University of California, Davis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: uc-davis-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: University of California, Davis API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: uc-davis-rules
score:
  band: thin
  composite: 34.5
  delta: -2.4
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 9.8
    contract_quality: 51.0
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 31.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uc-davis/refs/heads/main/screenshots/uc-davis-2026-06-20T195938.png
security:
- kind: authentication
  name: Uc Davis Authentication
  slug: uc-davis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Uc Davis Domain Security
  slug: uc-davis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uc-davis
tags:
- Education
- Higher Education
- University
- Research
- United States
- California
- Identity
- Health
website: https://www.ucdavis.edu/
---
