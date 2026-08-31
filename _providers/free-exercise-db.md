---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.7
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Read-only, unauthenticated dataset surface. The provider's own README documents consumption as an HTTPS GET of the combined exercises.json array (873 records) or of a single exercise document, with im
  name: Free Exercise DB Dataset
  slug: free-exercise-db-dataset
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://yuhonas.github.io/free-exercise-db/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/yuhonas/free-exercise-db#readme
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/yuhonas/free-exercise-db/blob/main/schema.json
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/yuhonas/free-exercise-db#how-do-i-use-them
- group: operate
  title: ''
  type: Support
  url: https://github.com/yuhonas/free-exercise-db/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yuhonas
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/yuhonas/free-exercise-db
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/yuhonas/free-exercise-db/blob/main/LICENSE.md
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/free-exercise-db-vocabulary.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/free-exercise-db-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/free-exercise-db-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/free-exercise-db-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/free-exercise-db-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/free-exercise-db-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/free-exercise-db-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/free-exercise-db-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/free-exercise-db-llms.txt
created: '2026-08-27'
description: 'Free Exercise DB is an open, public-domain exercise dataset published by yuhonas on GitHub: 873 individual JSON documents describing strength, stretching, plyometric, powerlifting, olympic-weightlifting, strongman and cardio exercises, each with a stable id, name, difficulty level, force and mechanic classification, required equipment, primary and secondary muscle groups, step-by-step instructions and demonstration images. Every record validates against a published JSON Schema (draft-04) that also acts as the project''s controlled vocabulary for muscles, equipment and categories. There is no REST API and no OpenAPI: consumption is by unauthenticated HTTPS GET of the combined dist/exercises.json array (or of a single exercise document) from raw.githubusercontent.com, with images served from the same host. A Vue.js browsable/searchable frontend is published to GitHub Pages. The whole dataset is released under the Unlicense.'
examples:
- key_count: 11
  name: Free Exercise Db Alternate Incline Dumbbell Curl
  slug: free-exercise-db-alternate-incline-dumbbell-curl
image: https://raw.githubusercontent.com/yuhonas/free-exercise-db/main/site/public/screenshot.png
json_schemas:
- name: Free Exercise Db Exercise
  property_count: 11
  slug: free-exercise-db-exercise
layout: provider
modified: '2026-08-27'
name: Free Exercise DB
nav: Providers
network: true
overview: 'Free Exercise DB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open Data, Fitness, Exercise, and Health.


  Free Exercise DB''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 12 more developer resources.'
plans:
- name: Free Exercise Db Plans Pricing
  plan_count: 0
  slug: free-exercise-db-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Free Exercise Db Rate Limits
  slug: free-exercise-db-rate-limits
score:
  band: emerging
  composite: 26.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 33.3
    contract_quality: 14.7
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 33.3
    operational_transparency: 2.6
  previous_composite: 26.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Free Exercise Db Authentication
  slug: free-exercise-db-authentication
  summary_line: 0 schemes
slug: free-exercise-db
tags:
- Company
- Open Data
- Fitness
- Exercise
- Health
- Public Domain
- Dataset
- JSON-Schema
- Workouts
website: https://yuhonas.github.io/free-exercise-db/
---
