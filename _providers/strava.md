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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Strava Agentic Access
  operation_count: 22
  slug: strava-agentic-access
  summary_line: 22 operations · 3 acting
api_count: 1
apis:
- baseURL: https://www.strava.com/api/v3
  baseurl_source: declared
  description: Create, read, update, and delete workout activities. Activities represent recorded workouts including runs, rides, swims, and 200+ other sport types.
  name: Strava Activities API
  slug: strava-activities-api
- baseURL: https://www.strava.com/api/v3
  baseurl_source: declared
  description: Access athlete profiles and statistics. Retrieve the authenticated athlete's profile and update their preferences.
  name: Strava Athletes API
  slug: strava-athletes-api
- baseURL: https://www.strava.com/api/v3
  baseurl_source: declared
  description: Access Strava clubs — groups of athletes. View club details, members, and recent club activities.
  name: Strava Clubs API
  slug: strava-clubs-api
- baseURL: https://www.strava.com/api/v3
  baseurl_source: declared
  description: Access athlete gear (bikes and shoes) used during activities.
  name: Strava Gear API
  slug: strava-gear-api
- baseURL: https://www.strava.com/api/v3
  baseurl_source: declared
  description: Access and manage athlete-created routes. Routes are planned courses for rides or runs.
  name: Strava Routes API
  slug: strava-routes-api
- baseURL: https://www.strava.com/api/v3
  baseurl_source: declared
  description: Access segment efforts — an athlete's attempt at a specific segment. Includes time, pace, and power data for each effort.
  name: Strava Segment Efforts API
  slug: strava-segment-efforts-api
- baseURL: https://www.strava.com/api/v3
  baseurl_source: declared
  description: Access segments — specific sections of road or trail that athletes compete on. View segment details, starred segments, and leaderboards.
  name: Strava Segments API
  slug: strava-segments-api
- baseURL: https://www.strava.com/api/v3
  baseurl_source: declared
  description: Access time-series data streams for activities and segments, including GPS coordinates, heart rate, power, cadence, speed, and altitude.
  name: Strava Streams API
  slug: strava-streams-api
artifact_total: 37
asyncapis:
- description: 'AsyncAPI definition for Strava''s Webhook Events API. Strava uses a push subscription model: an application creates a single push subscription with a callback URL and an application-defined verify_toke'
  name: Strava Webhooks API
  slug: strava-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Strava Activities API
  slug: open-strava-activities-api
- collection_type: open
  name: Strava Activities Athletes API
  slug: open-strava-athletes-api
- collection_type: open
  name: Strava Activities Clubs API
  slug: open-strava-clubs-api
- collection_type: open
  name: Strava Activities Gear API
  slug: open-strava-gear-api
- collection_type: open
  name: Strava Activities Routes API
  slug: open-strava-routes-api
- collection_type: open
  name: Strava Activities Segment Efforts API
  slug: open-strava-segment-efforts-api
- collection_type: open
  name: Strava Activities Segments API
  slug: open-strava-segments-api
- collection_type: open
  name: Strava Activities Streams API
  slug: open-strava-streams-api
- collection_type: open
  name: Strava API
  slug: open-strava
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/strava-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/strava-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strava-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/strava-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/strava-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strava
- group: company
  title: ''
  type: Website
  url: https://www.strava.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.strava.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.strava.com/docs/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.strava.com/docs/authentication/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.strava.com/legal/api
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.strava.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.strava.com
- group: company
  title: ''
  type: Blog
  url: https://blog.strava.com
- group: operate
  title: ''
  type: Forums
  url: https://communityhub.strava.com/developers
- group: start
  title: ''
  type: Signup
  url: https://www.strava.com/register
- group: start
  title: ''
  type: Login
  url: https://www.strava.com/login
- group: other
  title: ''
  type: App Registration
  url: https://www.strava.com/settings/api
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/openapi/strava-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/asyncapi/strava-webhooks-asyncapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/json-schema/strava-activity-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/json-ld/strava-context.jsonld
created: '2025-03-01'
description: 'Strava is a popular fitness tracking app and social network that allows athletes to track and analyze workouts including running, cycling, swimming, and 200+ other sport types. The Strava API enables developers to access athlete profiles, activities, segments, routes, clubs, gear, and time-series data streams. OAuth 2.0 is used for authentication with granular scope control. Rate limits apply: 100 requests per 15 minutes, 1000 per day.'
examples:
- key_count: 2
  name: Strava Get Athlete Example
  slug: strava-get-athlete-example
- key_count: 2
  name: Strava Get Segment Leaderboard Example
  slug: strava-get-segment-leaderboard-example
- key_count: 2
  name: Strava List Activities Example
  slug: strava-list-activities-example
finops:
- name: Strava Finops
  service_category: API
  slug: strava-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Strava API. Strava is a fitness tracking app and social network enabling athletes to track and analyze workouts including running, cycling, swimming, and 20
  name: Strava GraphQL Schema
  slug: strava-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/strava.png
json_schemas:
- name: Strava Activity
  property_count: 30
  slug: strava-activity
json_structures:
- name: Strava Activity Structure
  property_count: 0
  slug: strava-activity-structure
jsonld:
- class_count: 0
  name: Strava Context
  property_count: 5
  slug: strava-context
layout: provider
modified: '2026-05-30'
name: Strava
nav: Providers
network: true
overview: 'Strava publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Athletes API, Clubs API, and 5 more. Tagged areas include Cycling, Fitness, Fitness Tracking, Running, and Sports.


  The Strava catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Strava''s developer surface includes authentication, documentation, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Strava Plans Pricing
  plan_count: 3
  slug: strava-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Strava Rate Limits
  slug: strava-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Strava API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: strava-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Strava API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: strava-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Strava API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 5
    warn: 4
  slug: strava-rules
scopes:
- name: Strava Scopes
  scope_count: 7
  slug: strava-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 59.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 13.6
    contract_quality: 72.5
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 34.2
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/strava/refs/heads/main/screenshots/strava-2026-06-20T194613.png
security:
- kind: authentication
  name: Strava Authentication
  slug: strava-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Strava Domain Security
  slug: strava-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Strava Vulnerability Disclosure
  slug: strava-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: strava
tags:
- Cycling
- Fitness
- Fitness Tracking
- Running
- Sports
website: https://www.strava.com
---
