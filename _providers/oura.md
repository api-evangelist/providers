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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Oura Agentic Access
  operation_count: 75
  slug: oura-agentic-access
  summary_line: 75 operations · 4 acting
api_count: 21
apis:
- description: The Daily Activity scope includes daily activity summary values and detailed activity levels. Activity levels are expressed in [metabolic equivalent of task minutes](https://en.wikipedia.org/wiki/Meta
  name: Oura Ring Daily Activity Routes API
  slug: oura-daily-activity-routes-api
- description: Cardiovascular Age is an estimate of the health of your cardiovascular system in relation to your actual age. See more details [here](https://support.ouraring.com/hc/en-us/articles/28451491040019-Card
  name: Oura Ring Daily Cardiovascular Age Routes API
  slug: oura-daily-cardiovascular-age-routes-api
- description: Readiness tells how ready you are for the day.
  name: Oura Ring Daily Readiness Routes API
  slug: oura-daily-readiness-routes-api
- description: Resilience is an estimate of your ability to withstand physiological stress and recover from it over time.
  name: Oura Ring Daily Resilience Routes API
  slug: oura-daily-resilience-routes-api
- description: Sleep period is a nearly continuous, longish period of time spent lying down in bed.
  name: Oura Ring Daily Sleep Routes API
  slug: oura-daily-sleep-routes-api
- description: The Daily SpO2 (blood oxygenation) routes include daily SpO2 average. Data will only be available for users with a Gen 3 Oura Ring
  name: Oura Ring Daily Spo2 Routes API
  slug: oura-daily-spo2-routes-api
- description: 'The daily stress route includes a summary of the number of minutes the user spends in high stress and high recovery each day. This is a great way to see how your stress and recovery are trending over '
  name: Oura Ring Daily Stress Routes API
  slug: oura-daily-stress-routes-api
- description: The Enhanced Tags data scope includes tags that Oura users enter within the Oura mobile app. Enhanced Tags can be added for any lifestyle choice, habit, mood change, or environmental factor an Oura us
  name: Oura Ring Enhanced Tag Routes API
  slug: oura-enhanced-tag-routes-api
- description: The Heart Rate data scope includes time-series heart rate data throughout the day and night. Heart rate is provided at 5-minute increments. For heart rate data recorded from a Session, see Sessions en
  name: Oura Ring Heart Rate Routes API
  slug: oura-heart-rate-routes-api
- description: The Personal Info scope includes personal information (e.g. age, email, weight, and height) about the user. You can access the id on the personal_info route with any access token (no scopes are requir
  name: Oura Ring Personal Info Routes API
  slug: oura-personal-info-routes-api
- description: The Rest Mode scope includes information about rest mode periods. This includes the start, end time and detaials of the rest mode period.
  name: Oura Ring Rest Mode Period Routes API
  slug: oura-rest-mode-period-routes-api
- description: The Ring Battery Level Routes API from Oura Ring — 1 operation(s) for ring battery level routes.
  name: Oura Ring Ring Battery Level Routes API
  slug: oura-ring-battery-level-routes-api
- description: The Ring Configuration scope includes information about the user's ring(s). This includes the model, size, color, etc.
  name: Oura Ring Ring Configuration Routes API
  slug: oura-ring-configuration-routes-api
- description: 'Fake user data that you can access without an Oura account. There is a corresponding sandbox endpoint to each available data type. This is useful for testing and development purposes. The data is not '
  name: Oura Ring Sandbox Routes API
  slug: oura-sandbox-routes-api
- description: The Sessions data scope provides information on how users engage with guided and unguided sessions in the Oura app, including the user's biometric trends during the sessions.
  name: Oura Ring Session Routes API
  slug: oura-session-routes-api
- description: Returns Oura Sleep data for the specified Oura user within a given timeframe. A user can have multiple sleep periods per day.
  name: Oura Ring Sleep Routes API
  slug: oura-sleep-routes-api
- description: Recommendations for the optimal bedtime window that is calculated based on sleep data.
  name: Oura Ring Sleep Time Routes API
  slug: oura-sleep-time-routes-api
- description: <span className='text-important'>**Note:** Tag is deprecated. We recommend transitioning to [Enhanced Tag](#tag/Enhanced-Tag-Routes).</span> ~~The Tags data scope includes tags that Oura users enter w
  name: Oura Ring Tag Routes API
  slug: oura-tag-routes-api
- description: VO2 Max is a measure of the maximum volume of oxygen that an individual can use during intense exercise. See more details [here](https://support.ouraring.com/hc/en-us/articles/28336620578835-Cardio-Ca
  name: Oura Ring VO2 Max Routes API
  slug: oura-vo2-max-routes-api
- description: '# Webhooks for Real-Time Data Updates ## What are Webhooks? Webhooks are a way for the Oura API to notify your application when new data is available, instead of requiring your application to constant'
  name: Oura Ring Webhook Subscription Routes API
  slug: oura-webhook-subscription-routes-api
- description: The Workout data scope includes information about user workouts. This is a diverse, growing list of workouts that help inform how the user is training and exercising.
  name: Oura Ring Workout Routes API
  slug: oura-workout-routes-api
artifact_total: 62
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oura-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/oura-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oura-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oura-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oura-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oura-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://ouraring.com
- group: other
  title: ''
  type: Developer
  url: https://ouraring.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.ouraring.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/oura-health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oura
- group: company
  title: ''
  type: Blog
  url: https://ouraring.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ouraring.com/product
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ouraring.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/ouraring
- group: commercial
  title: ''
  type: Plans
  url: plans/oura-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oura-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/oura-finops.yml
- group: company
  title: ''
  type: BlogFeed
  url: blogs/blogs.json
created: '2026-06-13'
description: Oura Ring is a smart ring health tracking platform that provides a REST API for accessing sleep, activity, readiness, heart rate, daily health scores, and 50+ biometric metrics via OAuth2. Developers can build integrations that allow users to share their Oura Ring data with third-party services, supporting endpoints for sleep stages, workout detection, SpO2, heart rate variability, body temperature, and more. The platform also supports webhooks for near real-time data updates.
examples:
- key_count: 4
  name: Oura Dailyresiliencemodel Example
  slug: oura-dailyresiliencemodel-example
- key_count: 6
  name: Oura Personalinforesponse Example
  slug: oura-personalinforesponse-example
- key_count: 10
  name: Oura Publicdailyactivity Example
  slug: oura-publicdailyactivity-example
- key_count: 7
  name: Oura Publicdailyreadiness Example
  slug: oura-publicdailyreadiness-example
- key_count: 5
  name: Oura Publicdailysleep Example
  slug: oura-publicdailysleep-example
- key_count: 5
  name: Oura Publicdailystress Example
  slug: oura-publicdailystress-example
- key_count: 4
  name: Oura Publicheartraterow Example
  slug: oura-publicheartraterow-example
- key_count: 9
  name: Oura Publicsession Example
  slug: oura-publicsession-example
- key_count: 5
  name: Oura Publicsleeptime Example
  slug: oura-publicsleeptime-example
- key_count: 4
  name: Oura Publicvo2Max Example
  slug: oura-publicvo2max-example
- key_count: 10
  name: Oura Publicworkout Example
  slug: oura-publicworkout-example
- key_count: 5
  name: Oura Webhooksubscriptionmodel Example
  slug: oura-webhooksubscriptionmodel-example
finops:
- name: Oura Finops
  service_category: ''
  slug: oura-finops
graphqls:
- description: Oura Ring is a smart ring for sleep, recovery, and activity tracking. The API covers sleep stages, readiness scores, activity metrics, heart rate, HRV, SpO2, and workout detection for health and welln
  name: Oura Ring GraphQL API
  slug: oura-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oura.png
json_schemas:
- name: DailyResilienceModel
  property_count: 4
  slug: oura-dailyresiliencemodel
- name: EnhancedTagModel
  property_count: 8
  slug: oura-enhancedtagmodel
- name: PersonalInfoResponse
  property_count: 6
  slug: oura-personalinforesponse
- name: PublicDailyActivity
  property_count: 26
  slug: oura-publicdailyactivity
- name: PublicDailyCardiovascularAge
  property_count: 4
  slug: oura-publicdailycardiovascularage
- name: PublicDailyReadiness
  property_count: 7
  slug: oura-publicdailyreadiness
- name: PublicDailySleep
  property_count: 5
  slug: oura-publicdailysleep
- name: PublicDailySpO2
  property_count: 4
  slug: oura-publicdailyspo2
- name: PublicDailyStress
  property_count: 5
  slug: oura-publicdailystress
- name: PublicHeartRateRow
  property_count: 4
  slug: oura-publicheartraterow
- name: PublicRestModePeriod
  property_count: 6
  slug: oura-publicrestmodeperiod
- name: PublicRingConfiguration
  property_count: 7
  slug: oura-publicringconfiguration
- name: PublicSession
  property_count: 9
  slug: oura-publicsession
- name: PublicSleepTime
  property_count: 5
  slug: oura-publicsleeptime
- name: PublicVO2Max
  property_count: 4
  slug: oura-publicvo2max
- name: PublicWorkout
  property_count: 10
  slug: oura-publicworkout
- name: WebhookSubscriptionModel
  property_count: 5
  slug: oura-webhooksubscriptionmodel
jsonld:
- class_count: 18
  name: Oura Context
  property_count: 48
  slug: oura-context
layout: provider
modified: '2026-06-13'
name: Oura Ring
nav: Providers
network: true
overview: 'Oura Ring publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Daily Activity Routes API, Daily Cardiovascular Age Routes API, Daily Readiness Routes API, and 18 more. Tagged areas include Health, Wearables, Sleep, Fitness, and Heart Rate.


  The Oura Ring catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Oura Ring''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Oura Plans Pricing
  plan_count: 2
  slug: oura-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 3
  name: Oura Rate Limits
  slug: oura-rate-limits
rules:
- name: Oura Ring API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: oura-jsonschema-spectral-rules
scopes:
- name: Oura Scopes
  scope_count: 8
  slug: oura-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: developing
  composite: 52.6
  delta: -7.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 67.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 56.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/oura/refs/heads/main/screenshots/oura-2026-06-20T191225.png
security:
- kind: authentication
  name: Oura Authentication
  slug: oura-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Oura Domain Security
  slug: oura-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oura Vulnerability Disclosure
  slug: oura-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Oura Trust Center
  slug: oura-trust-center
  summary_line: SOC 2, HIPAA
slug: oura
tags:
- Health
- Wearables
- Sleep
- Fitness
- Heart Rate
- Readiness
- Smart Ring
- Biometrics
website: https://ouraring.com
---
