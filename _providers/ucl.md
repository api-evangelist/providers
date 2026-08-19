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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ucl Agentic Access
  operation_count: 29
  slug: ucl-agentic-access
  summary_line: 29 operations
api_count: 14
apis:
- description: Fetch personal and module timetables with various filters for departments, modules, and student groups. Part of the UCL API platform.
  name: UCL API Timetable
  slug: timetable
- description: Search for staff (people) directory information within UCL. Part of the UCL API platform.
  name: UCL API Search
  slug: search
- description: Fetch library study-space (workspace) availability, sensor data, and maps throughout UCL; availability is updated approximately every two minutes.
  name: UCL API Workspaces
  slug: workspaces
- description: Fetch desktop / computer availability throughout UCL. Part of the UCL API platform.
  name: UCL API Resources
  slug: resources
- description: Authenticate and authorise applications for UCL users via OAuth2; tokens are issued through the UCL login system and used across all UCL API services.
  name: UCL API OAuth
  slug: oauth
- description: UCL Discovery is UCL's open-access institutional repository of research outputs. It exposes an OAI-PMH metadata-harvesting endpoint (EPrints). Access to the OAI endpoint was protected (HTTP 403) at th
  name: UCL Discovery (OAI-PMH)
  slug: discovery-oai
- description: The UCL Research Data Repository is UCL's institutional data repository, built on Figshare, used to deposit, archive, publish and assign DOIs to research datasets and outputs. Figshare exposes a publi
  name: UCL Research Data Repository
  slug: research-data-repository
- description: View analytics and stats about your app or API services
  name: UCL Analytics API
  slug: ucl-analytics-api
- description: Authenticate and authorise applications for users
  name: UCL OAuth API
  slug: ucl-oauth-api
- description: Fetch desktop availability throughout UCL
  name: UCL Resources API
  slug: ucl-resources-api
- description: Fetch details of room bookings within UCL
  name: UCL Room Bookings API
  slug: ucl-room-bookings-api
- description: Search for staff in UCL
  name: UCL Search API
  slug: ucl-search-api
- description: Fetch timetables with various filters for various groups
  name: UCL Timetable API
  slug: ucl-timetable-api
- description: Fetch workspace availablility and maps throughout UCL
  name: UCL Workspaces API
  slug: ucl-workspaces-api
artifact_total: 54
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: UCL Analytics API
  slug: open-ucl-analytics-api
- collection_type: open
  name: UCL Analytics OAuth API
  slug: open-ucl-oauth-api
- collection_type: open
  name: UCL Analytics Resources API
  slug: open-ucl-resources-api
- collection_type: open
  name: UCL Analytics Room Bookings API
  slug: open-ucl-room-bookings-api
- collection_type: open
  name: UCL Analytics Search API
  slug: open-ucl-search-api
- collection_type: open
  name: UCL Analytics Timetable API
  slug: open-ucl-timetable-api
- collection_type: open
  name: UCL Analytics Workspaces API
  slug: open-ucl-workspaces-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/uclapi/uclapi/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ucl-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ucl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ucl-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ucl-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.ucl.ac.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://uclapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://uclapi.com/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uclapi
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/uclapi/uclapi
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/uclapi/uclapi-openapi
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/ucl-uclapi.yaml
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/ucl-api
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/
- group: build
  title: ''
  type: Examples
  url: examples/
- group: design
  title: ''
  type: Rules
  url: rules/ucl-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ucl-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ucl-context.jsonld
- group: company
  title: ''
  type: LinkedIn
  url: https://uk.linkedin.com/company/uclapi
- group: commercial
  title: ''
  type: Plans
  url: plans/ucl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ucl-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ucl-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: '12 entries retired: uclapi.com no longer answers (https=000, http=000).'
  reason: surface_retired
  state: none
created: '2026-06-03'
description: 'University College London (UCL) is a public research university in London, United Kingdom, ranked #9 in the QS World University Rankings 2025. UCL has a notably mature public developer footprint via UCL API (uclapi.com), a student-built but Information Services Division (ISD) backed, open-source, OAuth2-secured platform that exposes UCL digital services such as room bookings, timetables, staff search, desktop/study-space availability, and workspaces. UCL also operates open-research infrastructure including UCL Discovery (open-access repository) and the UCL Research Data Repository (Figshare-powered). The UCL API is free to use and requires UCL affiliation for authentication.'
examples:
- key_count: 9
  name: Ucl Oauth User Data Example
  slug: ucl-oauth-user-data-example
- key_count: 2
  name: Ucl Resources Desktops Example
  slug: ucl-resources-desktops-example
- key_count: 4
  name: Ucl Roombookings Bookings Example
  slug: ucl-roombookings-bookings-example
- key_count: 2
  name: Ucl Roombookings Equipment Example
  slug: ucl-roombookings-equipment-example
- key_count: 2
  name: Ucl Roombookings Rooms Example
  slug: ucl-roombookings-rooms-example
- key_count: 2
  name: Ucl Search People Example
  slug: ucl-search-people-example
- key_count: 2
  name: Ucl Timetable Personal Example
  slug: ucl-timetable-personal-example
- key_count: 2
  name: Ucl Workspaces Sensors Example
  slug: ucl-workspaces-sensors-example
- key_count: 2
  name: Ucl Workspaces Surveys Example
  slug: ucl-workspaces-surveys-example
finops:
- name: Ucl Finops
  service_category: Education
  slug: ucl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ucl.png
json_schemas:
- name: UCL API booking
  property_count: 10
  slug: ucl-booking
- name: UCL API desktop_data
  property_count: 4
  slug: ucl-desktop-data
- name: UCL API equipment
  property_count: 3
  slug: ucl-equipment
- name: UCL API event
  property_count: 10
  slug: ucl-event
- name: UCL API person
  property_count: 4
  slug: ucl-person
- name: UCL API room
  property_count: 9
  slug: ucl-room
- name: UCL API sensor
  property_count: 22
  slug: ucl-sensor
- name: UCL API survey
  property_count: 8
  slug: ucl-survey
- name: UCL API user_data
  property_count: 9
  slug: ucl-user-data
json_structures:
- name: Ucl Booking Structure
  property_count: 10
  slug: ucl-booking-structure
- name: Ucl Person Structure
  property_count: 4
  slug: ucl-person-structure
- name: Ucl Room Structure
  property_count: 9
  slug: ucl-room-structure
- name: Ucl User Data Structure
  property_count: 9
  slug: ucl-user-data-structure
jsonld:
- class_count: 51
  name: Ucl Context
  property_count: 1
  slug: ucl-context
layout: provider
modified: '2026-06-03'
name: UCL
nav: Providers
network: true
overview: 'UCL publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, OAuth API, Resources API, and 4 more. Tagged areas include Education, Higher Education, University, United Kingdom, and Open Data.


  The UCL catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  UCL''s developer surface includes authentication, documentation, GitHub presence, engineering blog, code examples, and 19 more developer resources.'
plans:
- name: Ucl Plans Pricing
  plan_count: 2
  slug: ucl-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 1
  name: Ucl Rate Limits
  slug: ucl-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: UCL API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ucl-jsonschema-spectral-rules
- effective_rule_count: 6
  extends: []
  name: UCL API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ucl-rules
scopes:
- name: Ucl Scopes
  scope_count: 2
  slug: ucl-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 40.7
  delta: -5.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 56.7
    developer_ergonomics: 22.6
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 26.3
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/ucl/refs/heads/main/screenshots/ucl-2026-06-20T195940.png
security:
- kind: authentication
  name: Ucl Authentication
  slug: ucl-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Ucl Domain Security
  slug: ucl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ucl
tags:
- Education
- Higher Education
- University
- United Kingdom
- Open Data
- Research
- Library
- Timetable
website: https://www.ucl.ac.uk/
---
