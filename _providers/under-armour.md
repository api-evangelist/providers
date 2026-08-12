---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Under Armour Agentic Access
  operation_count: 19
  slug: under-armour-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 6
apis:
- description: Fitness device registration and management
  name: Under Armour Devices API
  slug: under-armour-devices-api
- description: Heart rate zone configuration and calculations
  name: Under Armour Heart Rate Zones API
  slug: under-armour-heart-rate-zones-api
- description: Manage running, cycling, and other fitness routes
  name: Under Armour Routes API
  slug: under-armour-routes-api
- description: User profile management and social connections
  name: Under Armour Users API
  slug: under-armour-users-api
- description: Event-driven webhook subscriptions
  name: Under Armour Webhooks API
  slug: under-armour-webhooks-api
- description: Create, retrieve, update, and delete fitness workouts
  name: Under Armour Workouts API
  slug: under-armour-workouts-api
artifact_total: 20
collections:
- collection_type: open
  name: MapMyFitness API
  slug: open-mapmyfitness
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/under-armour-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/under-armour-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/under-armour-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/under-armour-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/under-armour
- group: company
  title: ''
  type: Website
  url: https://www.under-armour.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.mapmyfitness.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.mapmyfitness.com/docs/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.mapmyfitness.com/docs/v71_OAuth_2_Intro/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.mapmyfitness.com/Terms_Of_Service/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/underarmour
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/mapmyfitness-openapi.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/under-armour-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/under-armour-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/under-armour-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/under-armour-workout-schema.json
created: '2026-03-24'
description: Under Armour is an American company that manufactures footwear, sports, and casual apparel known for its performance products designed for athletes. Under Armour operates a Connected Fitness platform — powered by MapMyFitness — that provides developer APIs for integrating workout tracking, route data, user profiles, heart rate zones, and fitness devices into third-party applications.
examples:
- key_count: 3
  name: Mapmyfitness List Workouts Example
  slug: mapmyfitness-list-workouts-example
finops:
- name: Under Armour Finops
  service_category: Apparel / Commerce
  slug: under-armour-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/under-armour.png
json_schemas:
- name: Under Armour Workout
  property_count: 6
  slug: under-armour-workout
json_structures:
- name: Under Armour Workout Structure
  property_count: 0
  slug: under-armour-workout-structure
jsonld:
- class_count: 15
  name: Under Armour Context
  property_count: 18
  slug: under-armour-context
layout: provider
modified: '2026-05-19'
name: Under Armour
nav: Providers
network: true
overview: 'Under Armour publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Heart Rate Zones API, Routes API, and 3 more. Tagged areas include Fitness, Health, Wearables, Connected Fitness, and Sports.


  The Under Armour catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Under Armour''s developer surface includes authentication, documentation, and 14 more developer resources.'
plans:
- name: Under Armour Plans Pricing
  plan_count: 1
  slug: under-armour-plans-pricing
press:
- date: '2026-05-25'
  title: Corporate Governance
  url: https://about.underarmour.com/en/investors/corporate-governance.html
- date: '2026-05-25'
  title: UNDER ARMOUR REPORTS FOURTH QUARTER AND ...
  url: https://www.prnewswire.com/news-releases/under-armour-reports-fourth-quarter-and-full-year-fiscal-2026-results-provides-initial-fiscal-2027-outlook-302768815.html
- date: '2026-05-25'
  title: Forever Is Made Now
  url: https://about.underarmour.com/en/stories/2024/03/forever-is-made-now.html
- date: '2026-05-25'
  title: Under Armour Creates the Ultimate Team Talk Using ...
  url: https://about.underarmour.com/en/stories/2023/08/under-armour-creates-the-ultimate-team-talk-using-the-power-of-a.html
- date: '2026-05-25'
  title: Under Armour's digital push continues through slumped ...
  url: https://www.ciodive.com/news/under-armours-digital-push-continues-through-slumped-financials/586002/
random_paper: 89
rate_limits:
- limit_count: 1
  name: Under Armour Rate Limits
  slug: under-armour-rate-limits
rules:
- name: Under Armour API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: under-armour-jsonschema-spectral-rules
- name: Under Armour API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 6
  slug: under-armour-rules
scopes:
- name: Under Armour Scopes
  scope_count: 2
  slug: under-armour-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.2
  delta: -5.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 69.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 10.5
  previous_composite: 50.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 47.5
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/under-armour/refs/heads/main/screenshots/under-armour-2026-06-20T200017.png
security:
- kind: authentication
  name: Under Armour Authentication
  slug: under-armour-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Under Armour Domain Security
  slug: under-armour-domain-security
  summary_line: TLSv1.3 · DMARC
slug: under-armour
tags:
- Fitness
- Health
- Wearables
- Connected Fitness
- Sports
- Fortune 1000
website: https://www.under-armour.com
---
