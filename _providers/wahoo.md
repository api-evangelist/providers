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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-08-26'
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
artifact_total: 34
asyncapis:
- description: Wahoo Cloud delivers `workout_summary` webhook events to a callback URL registered against a developer application. Webhooks require the `offline_data` OAuth scope. Failed deliveries (non-200) are ret
  name: Wahoo Cloud Webhooks
  slug: wahoo-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wahoo Cloud API
  slug: open-wahoo-cloud-api
- collection_type: open
  name: Wahoo Cloud Permissions API
  slug: open-wahoo-permissions-api
- collection_type: open
  name: Wahoo Cloud Permissions Plans API
  slug: open-wahoo-plans-api
- collection_type: open
  name: Wahoo Cloud Permissions Power Zones API
  slug: open-wahoo-power-zones-api
- collection_type: open
  name: Wahoo Cloud Permissions Routes API
  slug: open-wahoo-routes-api
- collection_type: open
  name: Wahoo Cloud Permissions Users API
  slug: open-wahoo-users-api
- collection_type: open
  name: Wahoo Cloud Permissions Workout File Uploads API
  slug: open-wahoo-workout-file-uploads-api
- collection_type: open
  name: Wahoo Cloud Permissions Workout Summaries API
  slug: open-wahoo-workout-summaries-api
- collection_type: open
  name: Wahoo Cloud Permissions Workouts API
  slug: open-wahoo-workouts-api
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
random_paper: 17
rate_limits:
- limit_count: 6
  name: Wahoo Rate Limits
  slug: wahoo-rate-limits
rules:
- effective_rule_count: 29
  extends:
  - spectral:asyncapi
  name: Wahoo Fitness API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: wahoo-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Wahoo Fitness API Rules
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
  band: strong
  composite: 57.1
  delta: 11.2
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 28.8
    contract_quality: 74.1
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 44.7
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 51.4
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
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
- Webhook
- Authentication
website: https://www.wahoofitness.com/
---
