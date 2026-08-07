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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cornell Agentic Access
  operation_count: 15
  slug: cornell-agentic-access
  summary_line: 15 operations
api_count: 10
apis:
- description: Public read-only API (version 2.0) for Cornell Class Roster data, providing scheduled classes with Course of Study details plus configuration lookups for rosters, academic careers, academic groups, cl
  name: Cornell Class Roster API
  slug: class-roster
- description: eCommons is Cornell University Library's institutional repository, running on DSpace 7+. It exposes a public DSpace REST API for items, communities, collections, and bitstreams, and an OAI-PMH endpoin
  name: eCommons Digital Repository (DSpace REST and OAI-PMH)
  slug: ecommons
- description: arXiv, hosted and stewarded by Cornell University, provides a long-running public API for programmatic search and retrieval of e-print metadata across physics, mathematics, computer science, and other
  name: arXiv API
  slug: arxiv
- description: The config API from Cornell University — 6 operation(s) for config.
  name: Cornell University config API
  slug: cornell-config-api
- description: The dining API from Cornell University — 2 operation(s) for dining.
  name: Cornell University dining API
  slug: cornell-dining-api
- description: The events API from Cornell University — 1 operation(s) for events.
  name: Cornell University events API
  slug: cornell-events-api
- description: The location API from Cornell University — 1 operation(s) for location.
  name: Cornell University location API
  slug: cornell-location-api
- description: The map items API from Cornell University — 1 operation(s) for map items.
  name: Cornell University map items API
  slug: cornell-map-items-api
- description: The search API from Cornell University — 2 operation(s) for search.
  name: Cornell University search API
  slug: cornell-search-api
- description: The tags API from Cornell University — 1 operation(s) for tags.
  name: Cornell University tags API
  slug: cornell-tags-api
artifact_total: 30
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cornell-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cornell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cornell-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.cornell.edu/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cornell-data
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/cornell-university/
- group: auth
  title: ''
  type: Authentication
  url: https://shibidp.cit.cornell.edu/idp/shibboleth
- group: commercial
  title: ''
  type: Plans
  url: plans/cornell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cornell-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cornell-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Cornell University is a private Ivy League and statutory land-grant research university based in Ithaca, New York, ranked #16 in the QS World University Rankings 2025. Its public developer footprint is decentralized rather than served through a single API gateway: the Class Roster team publishes a documented Class Roster API for course and scheduling data, the Cornell University Library operates the eCommons digital repository on DSpace with REST and OAI-PMH access, and Cornell hosts arXiv with its long-standing public arXiv API. The student-led Cornell Open Data Initiative (CODI) additionally exposes campus map, transit, dining, and events datasets, though parts of that platform are archived or marked as likely outdated.'
examples:
- key_count: 2
  name: Cornell Eateries Example
  slug: cornell-eateries-example
- key_count: 2
  name: Cornell Events Example
  slug: cornell-events-example
- key_count: 2
  name: Cornell Locations Example
  slug: cornell-locations-example
- key_count: 2
  name: Cornell Search Classes Example
  slug: cornell-search-classes-example
finops:
- name: Cornell Finops
  service_category: Education
  slug: cornell-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cornell.png
json_schemas:
- name: Cornell Class
  property_count: 23
  slug: cornell-class
- name: Cornell Eatery
  property_count: 27
  slug: cornell-eatery
- name: Cornell Event
  property_count: 33
  slug: cornell-event
- name: Cornell Map Location
  property_count: 8
  slug: cornell-location
json_structures:
- name: Cornell Class Structure
  property_count: 14
  slug: cornell-class-structure
- name: Cornell Eatery Structure
  property_count: 17
  slug: cornell-eatery-structure
- name: Cornell Event Structure
  property_count: 20
  slug: cornell-event-structure
jsonld:
- class_count: 36
  name: Cornell Context
  property_count: 0
  slug: cornell-context
layout: provider
modified: '2026-06-03'
name: Cornell University
nav: Providers
network: true
overview: 'Cornell University publishes 7 APIs on the [APIs.io](https://apis.io/) network, including config API, dining API, events API, and 4 more. Tagged areas include Education, Higher Education, University, Open Data, and Course Catalog.


  The Cornell University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cornell University''s developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: Cornell Plans Pricing
  plan_count: 2
  slug: cornell-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 1
  name: Cornell Rate Limits
  slug: cornell-rate-limits
rules:
- name: Cornell University API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cornell-jsonschema-spectral-rules
- name: Cornell University API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: cornell-rules
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 39.0
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
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cornell/refs/heads/main/screenshots/cornell-2026-06-20T175031.png
security:
- kind: authentication
  name: Cornell Authentication
  slug: cornell-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cornell Domain Security
  slug: cornell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cornell
tags:
- Education
- Higher Education
- University
- Open Data
- Course Catalog
- Library
- Research
- United States
website: https://www.cornell.edu/
---
