---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Whoop Co Agentic Access
  operation_count: 20
  slug: whoop-co-agentic-access
  summary_line: 20 operations · 6 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Utility endpoints for activity ID mapping
  name: WHOOP Activity ID Mapping API
  slug: whoop-co-activity-id-mapping-api
- description: The Cycle API from WHOOP — 3 operation(s) for cycle.
  name: WHOOP Cycle API
  slug: whoop-co-cycle-api
- description: Endpoints for trusted WHOOP partner operations
  name: WHOOP Partner API
  slug: whoop-co-partner-api
- description: The Recovery API from WHOOP — 2 operation(s) for recovery.
  name: WHOOP Recovery API
  slug: whoop-co-recovery-api
- description: The Sleep API from WHOOP — 2 operation(s) for sleep.
  name: WHOOP Sleep API
  slug: whoop-co-sleep-api
- description: Endpoints for retrieving user profile and measurement data.
  name: WHOOP User API
  slug: whoop-co-user-api
- description: The Workout API from WHOOP — 2 operation(s) for workout.
  name: WHOOP Workout API
  slug: whoop-co-workout-api
artifact_total: 47
collections:
- collection_type: open
  name: WHOOP API
  slug: open-whoop-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whoop-co-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whoop-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whoop-co-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/whoop-co-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.whoop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.whoop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.whoop.com/docs/introduction/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.whoop.com/docs/developing/oauth/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.whoop.com/docs/developing/oauth/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.whoop.com/docs/developing/rate-limiting/
- group: design
  title: ''
  type: Webhooks
  url: https://developer.whoop.com/docs/developing/webhooks/
- group: operate
  title: ''
  type: Support
  url: https://developer.whoop.com/docs/developing/support/
- group: operate
  title: ''
  type: Migration
  url: https://developer.whoop.com/docs/developing/v1-v2-migration/
- group: other
  title: ''
  type: DeveloperDashboard
  url: https://developer-dashboard.whoop.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.whoop.com/us/en/membership/
- group: operate
  title: ''
  type: Support
  url: https://support.whoop.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whoop/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/whoop
- group: operate
  title: ''
  type: ContactUs
  url: https://www.whoop.com/us/en/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.whoop.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.whoop.com/legal/terms-of-use/
- group: commercial
  title: ''
  type: APITerms
  url: https://www.whoop.com/legal/api-terms/
- group: commercial
  title: ''
  type: Plans
  url: plans/whoop-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whoop-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/whoop-co-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/whoop-co-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://www.whoop.com/us/en/thelocker/
created: '2026-05-25'
description: WHOOP is a wearable health and performance company whose wrist-worn strap (WHOOP 5.0 and medical-grade WHOOP MG) measures heart rate, HRV, respiratory rate, skin temperature, and SpO2 24/7 to compute daily Recovery, Strain, and Sleep Performance scores. The WHOOP Developer Platform exposes member fitness data through an OAuth-protected REST API (v2) covering physiological cycles, sleep, workouts, recovery, and body measurements, plus webhooks for resource updates and a Trusted Partner API for lab/diagnostics integrations.
examples:
- key_count: 2
  name: Whoop Get Recovery Example
  slug: whoop-get-recovery-example
- key_count: 2
  name: Whoop List Sleep Example
  slug: whoop-list-sleep-example
- key_count: 2
  name: Whoop List Workouts Example
  slug: whoop-list-workouts-example
- key_count: 4
  name: Whoop Webhook Sleep Updated Example
  slug: whoop-webhook-sleep-updated-example
features:
- WHOOP 5.0 — fifth-generation wrist-worn strap with 14-day battery life and on-skin sensor improvements
- WHOOP MG — medical-grade variant adding ECG and blood-pressure readings
- Continuous 24/7 monitoring of heart rate, HRV, respiratory rate, skin temperature, and SpO2
- Daily Recovery score based on HRV, resting heart rate, and sleep performance
- Daily Strain score capturing cardiovascular load across all activities
- Sleep coaching with stage-by-stage analysis (light, deep, REM) and Sleep Performance %
- Workout auto-detection with heart-rate zone breakdowns
- Stress Monitor and Daily Outlook AI coaching
- Health Monitor with vitals trends and abnormality alerts
- WHOOP Coach generative AI assistant for personalized insights
- Three subscription tiers — ONE ($199/yr), PEAK ($239/yr), LIFE ($359/yr)
- Developer Platform with OAuth 2.0 (authorization code) member-data API
- Trusted Partner program with client-credentials OAuth for lab and diagnostics integrations
- v2 REST API with UUID resource identifiers and pagination cursors
- Webhooks for recovery, sleep, and workout updated/deleted events with HMAC SHA-256 signing
- Six member-data scopes — read:recovery, read:cycles, read:workout, read:sleep, read:profile, read:body_measurement
- Rate limits — 100 requests/minute and 10,000 requests/day per client, with X-RateLimit-* headers
- v1-to-v2 activity-mapping endpoint for migration
- Mobile apps for iOS, Android, and Wear OS / Apple Watch companion experience
- Garmin, Strava, TrainingPeaks, Apple Health, and Google Health Connect integrations
- Community SDKs (Python `hedgertronic/whoop`, MCP server `shashankswe2020-ux/whoop-mcp`)
finops:
- name: Whoop Co Finops
  service_category: Fitness and Wellness
  slug: whoop-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whoop-co.png
json_schemas:
- name: WHOOP Cycle
  property_count: 9
  slug: whoop-cycle
- name: WHOOP Recovery
  property_count: 7
  slug: whoop-recovery
- name: WHOOP Sleep
  property_count: 12
  slug: whoop-sleep
- name: WHOOP Workout
  property_count: 11
  slug: whoop-workout
jsonld:
- class_count: 0
  name: Whoop Co Context
  property_count: 6
  slug: whoop-co-context
layout: provider
modified: '2026-05-25'
name: WHOOP
nav: Providers
network: true
overview: 'WHOOP publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Activity ID Mapping API, Cycle API, Partner API, and 4 more. Tagged areas include Fitness, Wearables, Health, Recovery, and Sleep.


  The WHOOP catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  WHOOP''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, pricing, engineering blog, and 20 more developer resources.'
plans:
- name: Whoop Co Plans Pricing
  plan_count: 3
  slug: whoop-co-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 2
  name: Whoop Co Rate Limits
  slug: whoop-co-rate-limits
rules:
- name: WHOOP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: whoop-co-jsonschema-spectral-rules
- name: WHOOP API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 3
  slug: whoop-rules
scopes:
- name: Whoop Co Scopes
  scope_count: 7
  slug: whoop-co-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 67.6
  delta: 4.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 74.3
    developer_ergonomics: 45.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 28.9
  previous_composite: 63.0
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whoop-co/refs/heads/main/screenshots/whoop-co-2026-06-20T201452.png
security:
- kind: authentication
  name: Whoop Co Authentication
  slug: whoop-co-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Whoop Co Domain Security
  slug: whoop-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: whoop-co
tags:
- Fitness
- Wearables
- Health
- Recovery
- Sleep
- Strain
- Heart Rate
- Workout
- Biometrics
website: https://www.whoop.com/
---
