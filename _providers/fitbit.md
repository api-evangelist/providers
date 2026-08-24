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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.3
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Fitbit Agentic Access
  operation_count: 55
  slug: fitbit-agentic-access
  summary_line: 55 operations · 18 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Read and update the authorized Fitbit user's profile including display name, gender, birthday, height, weight, locale, timezone, and unit preferences (distance, weight, water, glucose, temperature).
  name: Fitbit User API
  slug: fitbit-user-api
- description: The Foods API from Fitbit — 1 operation(s) for foods.
  name: Fitbit Foods API
  slug: fitbit-foods-api
- description: The Oauth2 API from Fitbit — 4 operation(s) for oauth2.
  name: Fitbit Oauth2 API
  slug: fitbit-oauth2-api
artifact_total: 53
asyncapis:
- description: Fitbit's Subscription API streams sync notifications to a registered Subscriber endpoint each time a user has new data available for a subscribed collection. Five collections are subscribable per user
  name: Fitbit Subscriptions Webhooks
  slug: fitbit-subscriptions-asyncapi
collections:
- collection_type: postman
  name: Fitbit Activity Foods API
  slug: postman-fitbit-foods-api
- collection_type: postman
  name: Fitbit Activity Foods Oauth2 API
  slug: postman-fitbit-oauth2-api
- collection_type: postman
  name: Fitbit Activity Foods User API
  slug: postman-fitbit-user-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fitbit Activity API
  slug: open-fitbit-activity-api
- collection_type: open
  name: Fitbit Authorization API
  slug: open-fitbit-authorization-api
- collection_type: open
  name: Fitbit Body API
  slug: open-fitbit-body-api
- collection_type: open
  name: Fitbit Devices API
  slug: open-fitbit-devices-api
- collection_type: open
  name: Fitbit ECG and Irregular Rhythm Notifications API
  slug: open-fitbit-ecg-irn-api
- collection_type: open
  name: Fitbit Activity Foods API
  slug: open-fitbit-foods-api
- collection_type: open
  name: Fitbit Friends API
  slug: open-fitbit-friends-api
- collection_type: open
  name: Fitbit Heart Rate API
  slug: open-fitbit-heart-rate-api
- collection_type: open
  name: Fitbit Nutrition API
  slug: open-fitbit-nutrition-api
- collection_type: open
  name: Fitbit Activity Foods Oauth2 API
  slug: open-fitbit-oauth2-api
- collection_type: open
  name: Fitbit Sleep API
  slug: open-fitbit-sleep-api
- collection_type: open
  name: Fitbit SpO2 / Breathing Rate / Temperature / HRV / VO2 Max API
  slug: open-fitbit-spo2-breathing-temperature-api
- collection_type: open
  name: Fitbit Subscriptions API
  slug: open-fitbit-subscriptions-api
- collection_type: open
  name: Fitbit Activity Foods User API
  slug: open-fitbit-user-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/fitbit/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fitbit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fitbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fitbit-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fitbit-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.fitbit.com
- group: start
  title: ''
  type: Portal
  url: https://dev.fitbit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fitbit.com/build/reference/web-api/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fitbit.com/build/reference/device-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.fitbit.com/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fitbit.com/build/reference/web-api/authorization/
- group: operate
  title: ''
  type: Support
  url: https://dev.fitbit.com/build/reference/web-api/troubleshooting-guide/
- group: design
  title: ''
  type: ErrorCodes
  url: https://dev.fitbit.com/build/reference/web-api/troubleshooting-guide/error-handling/
- group: design
  title: ''
  type: ErrorCodes
  url: https://dev.fitbit.com/build/reference/web-api/troubleshooting-guide/error-messages/
- group: operate
  title: ''
  type: RateLimits
  url: https://dev.fitbit.com/build/reference/web-api/rate-limits/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fitbit.com/build/reference/web-api/intraday/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.fitbit.com/build/reference/web-api/subscription/
- group: start
  title: ''
  type: Signup
  url: https://dev.fitbit.com/apps/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fitbit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fitbit/fitbit-sdk-toolchain
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Fitbit/create-fitbit-app
- group: build
  title: ''
  type: Tools
  url: https://github.com/Fitbit/developer-bridge
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Fitbit/sdk-oauth
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Fitbit/sdk-hr-meter
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Fitbit/ossapps
- group: build
  title: ''
  type: Tools
  url: https://github.com/Fitbit/golden-gate
- group: build
  title: ''
  type: Tools
  url: https://github.com/Fitbit/bitgatt
- group: commercial
  title: ''
  type: Plans
  url: https://www.fitbit.com/global/us/products/premium
- group: commercial
  title: ''
  type: Pricing
  url: https://store.google.com/category/watches_trackers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fitbit
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/fitbit
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/fitbit
- group: operate
  title: ''
  type: Support
  url: https://help.fitbit.com/
- group: operate
  title: ''
  type: Forums
  url: https://community.fitbit.com/
- group: operate
  title: ''
  type: Forums
  url: https://community.fitbit.com/t5/Web-API-Development/bd-p/dev
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fitbit.com/global/us/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fitbit.com/global/us/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dev.fitbit.com/legal/platform-terms-of-service/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/health
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/health/migration
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.google.com/health/release-notes
- group: company
  title: ''
  type: Blog
  url: https://community.fitbit.com/t5/Web-API-Development/Introducing-the-next-phase-of-the-Fitbit-Web-API/td-p/5821061
- group: start
  title: ''
  type: Portal
  url: https://about.google/intl/en/products/devices-services/fitbit/
- group: company
  title: ''
  type: Blog
  url: https://blog.google/products/fitbit/
- group: commercial
  title: ''
  type: Plans
  url: plans/fitbit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fitbit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fitbit-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Fitbit is a wearable health and fitness platform — devices (trackers, smartwatches, smart scales) plus a companion mobile app and cloud data services. Founded in 2007 and acquired by Google in January 2021, Fitbit is now operated as part of Google's hardware portfolio alongside the Pixel Watch. The Fitbit Web API exposes user activity, exercise, heart rate (including intraday and HRV), sleep with stage breakdowns, body and weight, nutrition and water, devices, friends and leaderboards, and advanced sensor metrics — SpO2, breathing rate, skin and core temperature, ECG, Irregular Rhythm Notifications, and Cardio Fitness Score (VO2 Max). Authentication is OAuth 2.0 Authorization Code Grant with PKCE; default quota is 150 requests per hour per authorized user per app. A webhook subscription system streams sync notifications for the activities, body, foods, sleep, and userRevokedAccess collections. The Fitbit OS SDK lets developers ship apps and clock faces directly to Versa, Sense,
  and other Fitbit devices using JavaScript/CSS/SVG. The legacy Fitbit Web API is scheduled for deprecation in September 2026; new and migrated integrations should target the successor Google Health API at developers.google.com/health, which uses Google OAuth 2.0 and Google's modern infrastructure.
features:
- Wearable-native API surface covering activity, exercise, heart rate, sleep, body, nutrition, devices, and social
- Advanced sensor data — SpO2, breathing rate, skin and core temperature, heart rate variability (RMSSD), VO2 Max
- Electrocardiogram (ECG) readings and Irregular Rhythm Notifications (IRN) on supported devices
- Active Zone Minutes (AZM) as Fitbit's modern engagement metric
- Time-series endpoints with day, week, month, quarter, half-year, and year periods
- Intraday endpoints (1-second / 1-minute / 5-minute / 15-minute resolution) on case-by-case approval
- Webhook subscriptions for activities, body, foods, sleep, and userRevokedAccess — eliminates polling
- OAuth 2.0 Authorization Code Grant with PKCE, plus Implicit Grant and Client Credentials (Commerce only)
- Fine-grained scopes — activity, heartrate, location, nutrition, profile, settings, sleep, social, weight, oxygen_saturation, respiratory_rate, temperature, electrocardiogram, irregular_rhythm_notifications, cardio_fitness
- Three application types — Personal (developer's own data), Client (mobile/single-page), Server (multi-user backend)
- Default 150 requests-per-hour-per-user quota; 429 + Retry-After on overage
- Fitbit OS SDK (JavaScript/CSS/SVG) for on-device apps and clock faces on Versa/Sense/Inspire/Charge devices
- Fitbit SDK toolchain (TypeScript) and create-fitbit-app scaffolder published on GitHub
- Fitbit Premium consumer tier ($9.99/month, $79.99/year) adds Daily Readiness, advanced sleep, mindfulness, workouts
- Cross-platform mobile apps (iOS, Android) and Fitbit web dashboard
- Acquired by Google in January 2021; now part of Google's hardware portfolio alongside Pixel Watch
- Successor platform — Google Health API — launched on Google's modern infrastructure with Google OAuth 2.0
- Legacy Fitbit Web API scheduled for turndown in September 2026; migration guides published on developers.google.com/health
finops:
- name: Fitbit Finops
  service_category: Health and Wearables
  slug: fitbit-finops
graphqls:
- description: Conceptual GraphQL schema for the Fitbit Web API — a wearable health and fitness platform acquired by Google in January 2021 and now part of Google's hardware portfolio alongside Pixel Watch. The lega
  name: Fitbit GraphQL Schema
  slug: fitbit-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fitbit.png
json_schemas:
- name: Fitbit Activity Daily Summary
  property_count: 3
  slug: fitbit-activity-summary
- name: Fitbit Sleep Log
  property_count: 2
  slug: fitbit-sleep-log
jsonld:
- class_count: 0
  name: Fitbit Context
  property_count: 10
  slug: fitbit-context
layout: provider
modified: '2026-05-30'
name: Fitbit
nav: Providers
network: true
overview: 'Fitbit publishes 3 APIs on the [APIs.io](https://apis.io/) network: User API, Foods API, and Oauth2 API. Tagged areas include Wearable, Health, Fitness, Activity Tracking, and Heart Rate.


  The Fitbit catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Fitbit''s developer surface includes authentication, developer portal, documentation, getting-started guide, support, signup flow, tooling, and 40 more developer resources.'
plans:
- name: Fitbit Plans Pricing
  plan_count: 6
  slug: fitbit-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Fitbit Rate Limits
  slug: fitbit-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Fitbit API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: fitbit-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Fitbit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: fitbit-jsonschema-spectral-rules
scopes:
- name: Fitbit Scopes
  scope_count: 15
  slug: fitbit-scopes
  summary_line: 15 scopes · authorizationCode
score:
  band: exemplar
  composite: 67.5
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 13.6
    contract_quality: 78.6
    developer_ergonomics: 61.9
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 67.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fitbit/refs/heads/main/screenshots/fitbit-2026-06-20T181253.png
security:
- kind: authentication
  name: Fitbit Authentication
  slug: fitbit-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fitbit Domain Security
  slug: fitbit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: fitbit
tags:
- Wearable
- Health
- Fitness
- Activity Tracking
- Heart Rate
- Sleep
- Google
- IoT
website: https://www.fitbit.com
---
