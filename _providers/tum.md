---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Tum Agentic Access
  operation_count: 19
  slug: tum-agentic-access
  summary_line: 19 operations · 4 acting
api_count: 9
apis:
- description: 'Backend for the TUM Campus App, written in Go and exposing a gRPC API interface used by the official cross-platform (Flutter/Dart) campus clients. Source is public; the production endpoint is used by '
  name: TUM Campus App Backend (gRPC)
  slug: campus-backend
- description: APIs to access calendar-data
  name: Technical University of Munich calendar API
  slug: tum-calendar-api
- description: APIs to give feedback
  name: Technical University of Munich feedback API
  slug: tum-feedback-api
- description: API to access/search for location information
  name: Technical University of Munich locations API
  slug: tum-locations-api
- description: API to access for map-data
  name: Technical University of Munich maps API
  slug: tum-maps-api
- description: Get information about dish plans
  name: Technical University of Munich menu API
  slug: tum-menu-api
- description: The Openapi.json API from Technical University of Munich — 1 operation(s) for openapi.json.
  name: Technical University of Munich Openapi.json API
  slug: tum-openapi-json-api
- description: Static information regarding canteens, labels and languages
  name: Technical University of Munich static API
  slug: tum-static-api
- description: The Status API from Technical University of Munich — 1 operation(s) for status.
  name: Technical University of Munich Status API
  slug: tum-status-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tum-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tum-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tum.de/en/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/TUM-Dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tum.dev/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/technische-universitat-munchen/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/TUM-Dev
- group: commercial
  title: ''
  type: Plans
  url: plans/tum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tum-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tum-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
- group: design
  title: ''
  type: x-vocabulary
  url: vocabulary/tum-vocabulary.yml
- group: design
  title: ''
  type: x-rules
  url: rules/tum-rules.yml
- group: design
  title: ''
  type: x-json-ld
  url: json-ld/tum-context.jsonld
created: '2026-06-03'
description: 'The Technical University of Munich (TUM) is a public research university in Munich, Germany, ranked #47 in the QS World University Rankings 2025. TUM does not operate a single centralized, commercial developer portal; instead its most visible public API footprint is community- and student-driven through the TUM-Dev open-source organization on GitHub, which builds and operates the Campus App ecosystem. Confirmed public, unauthenticated APIs include NavigaTUM (a Rust/MeiliSearch service to search rooms, buildings, and places, documented with an OpenAPI 3.0 spec) and eat-api (a static JSON API for Munich student canteen menus and prices). The institution''s central research information system, TUMFIS, runs on Elsevier Pure but exposes no documented public API.'
examples:
- key_count: 2
  name: Tum Canteen Menu Example
  slug: tum-canteen-menu-example
- key_count: 2
  name: Tum Canteens Enum Example
  slug: tum-canteens-enum-example
- key_count: 2
  name: Tum Search Example
  slug: tum-search-example
finops:
- name: Tum Finops
  service_category: Education
  slug: tum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tum.png
json_schemas:
- name: eat-api CanteenMenu
  property_count: 6
  slug: tum-canteen-menu
- name: NavigaTUM SearchResponse
  property_count: 2
  slug: tum-search-response
json_structures:
- name: Tum Canteen Menu Structure
  property_count: 3
  slug: tum-canteen-menu-structure
- name: Tum Search Response Structure
  property_count: 2
  slug: tum-search-response-structure
jsonld:
- class_count: 40
  name: Tum Context
  property_count: 0
  slug: tum-context
layout: provider
modified: '2026-06-03'
name: Technical University of Munich
nav: Providers
network: true
overview: 'Technical University of Munich publishes 8 APIs on the [APIs.io](https://apis.io/) network, including calendar API, feedback API, locations API, and 5 more. Tagged areas include Education, Higher Education, University, Germany, and Open Source.


  The Technical University of Munich catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Technical University of Munich''s developer surface includes GitHub presence and 14 more developer resources.'
plans:
- name: Tum Plans Pricing
  plan_count: 2
  slug: tum-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 1
  name: Tum Rate Limits
  slug: tum-rate-limits
rules:
- name: Technical University of Munich API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: tum-jsonschema-spectral-rules
- name: Technical University of Munich API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: tum-rules
score:
  band: thin
  composite: 41.4
  delta: -0.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 54.7
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 26.3
  previous_composite: 42.2
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tum/refs/heads/main/screenshots/tum-2026-06-20T195827.png
security:
- kind: domain-security
  name: Tum Domain Security
  slug: tum-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Tum Vulnerability Disclosure
  slug: tum-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tum
tags:
- Education
- Higher Education
- University
- Germany
- Open Source
- Campus
- Open Data
website: https://www.tum.de/en/
---
