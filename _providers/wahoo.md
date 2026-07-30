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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 1
  name: Wahoo Agentic Access
  operation_count: 28
  slug: wahoo-agentic-access
  summary_line: 28 operations · 16 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Native iOS SDK for interacting with Wahoo devices directly over BLE/ANT+ and integrating with the Wahoo Cloud. Documented at the Wahoo developer portal under the iOS product. Access is gated by the Wa
  name: Wahoo iOS API
  slug: wahoo-ios-api
- description: Native Android SDK for interacting with Wahoo devices over BLE/ANT+ and integrating with the Wahoo Cloud. Documented at the Wahoo developer portal under the Android product. Access is gated by the Wah
  name: Wahoo Android API
  slug: wahoo-android-api
- description: Revoke OAuth app access.
  name: Wahoo Fitness Permissions API
  slug: wahoo-permissions-api
- description: Structured workout plans.
  name: Wahoo Fitness Plans API
  slug: wahoo-plans-api
- description: Cycling power training zones.
  name: Wahoo Fitness Power Zones API
  slug: wahoo-power-zones-api
- description: Navigation / course data backed by FIT files.
  name: Wahoo Fitness Routes API
  slug: wahoo-routes-api
- description: Authenticated user profile.
  name: Wahoo Fitness Users API
  slug: wahoo-users-api
- description: Asynchronous FIT-file ingestion.
  name: Wahoo Fitness Workout File Uploads API
  slug: wahoo-workout-file-uploads-api
- description: Aggregate results for a completed workout.
  name: Wahoo Fitness Workout Summaries API
  slug: wahoo-workout-summaries-api
- description: Workout records (CRUD + listing).
  name: Wahoo Fitness Workouts API
  slug: wahoo-workouts-api
artifact_total: 25
asyncapis:
- description: Wahoo Cloud delivers `workout_summary` webhook events to a callback URL registered against a developer application. Webhooks require the `offline_data` OAuth scope. Failed deliveries (non-200) are ret
  name: Wahoo Cloud Webhooks
  slug: wahoo-webhooks-asyncapi
collections:
- collection_type: open
  name: Wahoo Cloud API
  slug: open-wahoo-cloud-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wahoo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wahoo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wahoo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wahoo-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.wahoofitness.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.wahooligan.com/
- group: docs
  title: ''
  type: APIReference
  url: https://cloud-api.wahooligan.com/
- group: commercial
  title: ''
  type: APIAgreement
  url: https://www.wahoofitness.com/wahoo-api-agreement
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wahoofitness
- group: operate
  title: ''
  type: Support
  url: https://support.wahoofitness.com/
- group: learn
  title: ''
  type: TrainingApp
  url: https://www.wahoofitness.com/devices/training-app
- group: other
  title: ''
  type: WahooX
  url: https://wahooxsystm.com/
- group: company
  title: ''
  type: Blog
  url: https://www.wahoofitness.com/blog
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/wahoofitness
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/wahoofitness/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/WahooFitness
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wahoo-fitness/
created: '2026-05-25'
description: 'Wahoo Fitness is an Atlanta, Georgia endurance-training hardware and software company building cycling and run-training products: the ELEMNT family of GPS bike computers (ACE, ROAM, BOLT), the KICKR family of smart trainers and bikes (KICKR BIKE PRO/SHIFT, KICKR MOVE, KICKR CORE, KICKR ROLLR, KICKR RUN treadmill), TICKR and TRACKR heart-rate monitors and sensors (including TRACKR RADAR rear-facing radar), and SPEEDPLAY road and power pedals. Wahoo publishes a public Cloud API at api.wahooligan.com that allows third-party applications to authenticate Wahoo users via OAuth 2.0 and read/write user profiles, workouts, workout summaries, FIT-file uploads, structured workout plans, GPS routes, and cycling power zones. The Cloud API delivers workout_summary webhook events when the offline_data scope is granted. Companion AppleHealth / native iOS and Android APIs round out the developer surface; access is gated by the Wahoo API Agreement and an app-approval workflow that promotes integrations
  from sandbox to production.'
examples:
- key_count: 13
  name: Wahoo Power Zones Example
  slug: wahoo-power-zones-example
- key_count: 4
  name: Wahoo Workout Summary Event Example
  slug: wahoo-workout-summary-event-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wahoo.png
json_schemas:
- name: Wahoo Workout
  property_count: 11
  slug: wahoo-workout
- name: Wahoo Workout Summary
  property_count: 13
  slug: wahoo-workout-summary
jsonld:
- class_count: 0
  name: Wahoo Context
  property_count: 6
  slug: wahoo-context
layout: provider
modified: '2026-05-25'
name: Wahoo Fitness
nav: Providers
network: true
overview: 'Wahoo Fitness publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Permissions API, Plans API, Power Zones API, and 5 more. Tagged areas include Fitness, Cycling, Endurance Training, Bike Computers, and Smart Trainers.


  The Wahoo Fitness catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Wahoo Fitness'' developer surface includes authentication, API reference, GitHub presence, support, engineering blog, YouTube channel, and 11 more developer resources.'
plans:
- name: Wahoo Plans Pricing
  plan_count: 2
  slug: wahoo-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 6
  name: Wahoo Rate Limits
  slug: wahoo-rate-limits
rules:
- name: Wahoo Fitness API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: wahoo-asyncapi-spectral-rules
- name: Wahoo Fitness API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wahoo-jsonschema-spectral-rules
scopes:
- name: Wahoo Scopes
  scope_count: 12
  slug: wahoo-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: developing
  composite: 46.9
  delta: -3.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 74.6
    developer_ergonomics: 32.6
    discoverability: 64.8
    governance: 52.1
    operational_transparency: 36.8
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wahoo/refs/heads/main/screenshots/wahoo-2026-06-20T201201.png
security:
- kind: authentication
  name: Wahoo Authentication
  slug: wahoo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wahoo Domain Security
  slug: wahoo-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: wahoo
tags:
- Fitness
- Cycling
- Endurance Training
- Bike Computers
- Smart Trainers
- Indoor Cycling
- Heart Rate
- Power Meters
- GPS
- Wearables
- Hardware
- FIT Files
- Webhooks
- OAuth
website: https://www.wahoofitness.com/
---
