---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Polar Agentic Access
  operation_count: 70
  slug: polar-agentic-access
  summary_line: 70 operations · 13 acting
api_count: 19
apis:
- description: The Polar BLE SDK enables iOS and Android applications to stream live data from Polar sensors over Bluetooth Low Energy. Supports H10, H9, Verity Sense, OH1, Ignite 3, Polar 360/Loop, Vantage V3, Vant
  name: Polar BLE SDK
  slug: polar-ble-sdk
- description: Cardio load is based on training impulse calculation (TRIMP), a commonly accepted and scientifically proven method to quantify training load. Your Cardio load value tells you how much strain your trai
  name: Polar Cardio load API
  slug: polar-cardio-load-api
- description: 'This resource allows partners to access their users'' continuous heart rate data. Continuous heart rate is recorded with supported devices when the heart rate tracking is turned on in device settings. '
  name: Polar Continuous Heart Rate API
  slug: polar-continuous-heart-rate-api
- description: This resource allows partners to access their users' daily activity data. Webhooks are used to notify partners when new data is available.
  name: Polar Daily activity API
  slug: polar-daily-activity-api
- description: This resource allows partners to access their users' daily activity data. During the transfer, the activity data is copied also into the AccessLink database so the end-users cannot change the data tha
  name: Polar Daily activity (deprecated) API
  slug: polar-daily-activity-deprecated-api
- description: This resource allows partners to access their users' Elixir&trade; Biosensing data. All time values are UTC times. Elixir&trade; Biosensing data consists of body temperature data, sleep skin temperatu
  name: Polar Elixir&trade; Biosensing API
  slug: polar-elixir-trade-biosensing-api
- description: Resources for getting information about exercise. These endpoints do not require an active transaction, but they use hashed id.
  name: Polar Exercises API
  slug: polar-exercises-api
- description: 'This resource allows partners to access their users'' training data. All time values are UTC except start-time. Start-time is the time set on the training computer. Each transaction will consist of at '
  name: Polar Exercises (deprecated) API
  slug: polar-exercises-deprecated-api
- description: 'Nightly Recharge&trade; is a recovery measurement that shows how well your body recovers from daily training and stress. It is based on heart rate variability (HRV) and overnight heart rate data. The '
  name: Polar Nightly Recharge API
  slug: polar-nightly-recharge-api
- description: This resource allows partners to access their users' physical information.
  name: Polar Physical info API
  slug: polar-physical-info-api
- description: This resource allows partners to access their users' physical information. Whenever some user's physical information changes, new entry containing full physical info is stored to AccessLink. Pull noti
  name: Polar Physical info (deprecated) API
  slug: polar-physical-info-deprecated-api
- description: Endpoints for getting players training session and details. <aside class='notice'> Only training sessions that are done during time the player has been linked to team roster will be visible here. </as
  name: Polar Player training sessions API
  slug: polar-player-training-sessions-api
- description: This resource allows partners to check if their users have available data for downloading. Use client credentials authentication. Returns object holding list of available data objects.
  name: Polar Pull notifications API
  slug: polar-pull-notifications-api
- description: Sleep endpoints support [Polar Sleep Plus&trade;](https://www.polar.com/en/smart-coaching/polar-sleep-plus) and [Sleep Plus Stages&trade;](https://www.polar.com/en/smart-coaching/sleep-plus-stages). A
  name: Polar Sleep API
  slug: polar-sleep-api
- description: This resource allows partners to access their users' SleepWise&trade; data. All time values are UTC times. SleepWise&trade; data is calculated for [SleepWise&trade;](https://support.polar.com/en/polar
  name: Polar SleepWise&trade; API
  slug: polar-sleepwise-trade-api
- description: Endpoints for getting teams and team details.
  name: Polar Team API
  slug: polar-team-api
- description: Endpoints for getting team training sessions and details.
  name: Polar Team training sessions API
  slug: polar-team-training-sessions-api
- description: This resource provides all the necessary functions to manage users.
  name: Polar Users API
  slug: polar-users-api
- description: Webhook resources provides endpoints for creating, modifying and deleting webhooks.
  name: Polar Webhooks API
  slug: polar-webhooks-api
artifact_total: 64
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Polar AccessLink API
  slug: open-polar-accesslink-api
- collection_type: open
  name: Polar AccessLink Webhooks
  slug: open-polar-accesslink-webhooks-asyncapi
- collection_type: open
  name: Polar AccessLink Cardio load API
  slug: open-polar-cardio-load-api
- collection_type: open
  name: Polar AccessLink Cardio load Continuous Heart Rate API
  slug: open-polar-continuous-heart-rate-api
- collection_type: open
  name: Polar AccessLink Cardio load Daily activity API
  slug: open-polar-daily-activity-api
- collection_type: open
  name: Polar AccessLink Cardio load Daily activity (deprecated) API
  slug: open-polar-daily-activity-deprecated-api
- collection_type: open
  name: Polar AccessLink Cardio load Elixir&trade; Biosensing API
  slug: open-polar-elixir-trade-biosensing-api
- collection_type: open
  name: Polar AccessLink Cardio load Exercises API
  slug: open-polar-exercises-api
- collection_type: open
  name: Polar AccessLink Cardio load Exercises (deprecated) API
  slug: open-polar-exercises-deprecated-api
- collection_type: open
  name: Polar AccessLink Cardio load Nightly Recharge API
  slug: open-polar-nightly-recharge-api
- collection_type: open
  name: Polar AccessLink Cardio load Physical info API
  slug: open-polar-physical-info-api
- collection_type: open
  name: Polar AccessLink Cardio load Physical info (deprecated) API
  slug: open-polar-physical-info-deprecated-api
- collection_type: open
  name: Polar AccessLink Cardio load Player training sessions API
  slug: open-polar-player-training-sessions-api
- collection_type: open
  name: Polar AccessLink Cardio load Pull notifications API
  slug: open-polar-pull-notifications-api
- collection_type: open
  name: Polar AccessLink Cardio load Sleep API
  slug: open-polar-sleep-api
- collection_type: open
  name: Polar AccessLink Cardio load SleepWise&trade; API
  slug: open-polar-sleepwise-trade-api
- collection_type: open
  name: Polar AccessLink Cardio load Team API
  slug: open-polar-team-api
- collection_type: open
  name: Polar AccessLink Cardio load Team training sessions API
  slug: open-polar-team-training-sessions-api
- collection_type: open
  name: TeamPro API
  slug: open-polar-teampro-api
- collection_type: open
  name: Polar AccessLink Cardio load Users API
  slug: open-polar-users-api
- collection_type: open
  name: Polar AccessLink Cardio load Webhooks API
  slug: open-polar-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/polar-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/polar-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polar-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/polar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/polar-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.polar.com/en
- group: start
  title: ''
  type: Portal
  url: https://www.polar.com/en/developers
- group: start
  title: ''
  type: Portal
  url: https://www.polar.com/en/business/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.polar.com/accesslink-api/
- group: docs
  title: ''
  type: Documentation
  url: https://www.polar.com/teampro-api/
- group: start
  title: ''
  type: Signup
  url: https://admin.polaraccesslink.com/
- group: build
  title: ''
  type: SDKs
  url: https://www.polar.com/en/business/sdk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/polarofficial
- group: build
  title: ''
  type: SDKs
  url: https://github.com/polarofficial/polar-ble-sdk
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/polarofficial/accesslink-example-python
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/polarofficial/create-mobile-app-for-polar-sensors
- group: start
  title: ''
  type: Portal
  url: https://flow.polar.com/
- group: operate
  title: ''
  type: Support
  url: https://support.polar.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.polar.com/en/compatible-apps
- group: company
  title: ''
  type: Partners
  url: https://www.polar.com/en/science/collaborate-with-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.polar.com/en/legal/polar-api-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.polar.com/en/legal/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.polar.com/en/legal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/polar-electro
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/PolarGlobal
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/PolarGlobalOfficial
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/polarglobal
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/polarglobal/
- group: company
  title: ''
  type: Blog
  url: https://www.polar.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://www.polar.com/en/products
created: '2026-05-25T00:00:00.000Z'
description: Polar Electro Oy (operating as Polar Global) is a Finnish sports and fitness technology company founded in 1977 and headquartered in Kempele, Finland. Polar invented the first wireless wearable heart rate monitor — the Sport Tester PE 2000 in 1982 — and remains one of the longest-standing brands in consumer heart rate sensing, GPS sports watches, and fitness wearables. The Polar device portfolio includes the H10 and H9 chest straps, the Verity Sense and OH1 optical sensors, the Polar 360 and Loop fitness bands, and the Vantage, Grit X, Pacer, Ignite, and Unite watch lines, along with a dedicated equine sensor line. Developers access Polar data through the Polar AccessLink API for consumer Polar Flow data, the Polar TeamPro API for team and player training sessions, and the open-source Polar BLE SDK for iOS and Android applications that stream live sensor data over Bluetooth Low Energy.
features:
- Polar AccessLink API with OAuth2 access to Polar Flow user training, activity, sleep, and biosensing data
- Continuous heart rate (5-minute samples), Nightly Recharge, SleepWise alertness, and circadian bedtime endpoints
- Cardio Load training-impulse calculation across days and months
- Elixir biosensing endpoints — ECG, SpO2, body and skin temperature, skin contacts
- Exercise downloads in JSON, FIT, TCX, and GPX formats
- Webhook subscriptions for real-time delivery of new training, activity, and sleep data
- Transactional endpoints (data is discarded after commit) and non-transactional persistent endpoints
- Polar TeamPro API for coaches with team and player training session data
- OAuth2 authorization-code flow with team_read scope for TeamPro and accesslink.read_all for AccessLink
- Partner registration and OAuth credential management at admin.polaraccesslink.com
- Polar BLE SDK for iOS (Swift) and Android (Kotlin/Java) streaming live HR, ECG, ACC, PPG, gyro, magnetometer, PPI
- Supported sensors include H10, H9, Verity Sense, OH1, Polar 360/Loop, Vantage V3, Vantage M3, Grit X2 Pro, Pacer Pro
- Heart-rate monitoring pioneer — first wireless wearable HR monitor (Sport Tester PE 2000, 1982)
- Google Fit and Apple HealthKit integration paths for consumer data sharing
- Dynamic rate limiting on AccessLink based on registered user count (15-minute and 24-hour windows)
- TeamPro API rate limit of 1 request/second with 100-request burst
- Polar Flow ecosystem (web at flow.polar.com plus iOS, Android, and Huawei mobile apps)
graphqls:
- description: Polar is a creator monetization platform for newsletters and digital products. The API covers subscriptions, products, benefits, orders, customers, and analytics for newsletter writers and indie devel
  name: Polar GraphQL API
  slug: polar-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/polar.png
layout: provider
modified: '2026-05-30'
name: Polar
nav: Providers
network: true
overview: 'Polar publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Cardio load API, Continuous Heart Rate API, Daily activity API, and 15 more. Tagged areas include Fitness, Health, Wearables, Heart Rate, and Sports.


  Polar''s developer surface includes authentication, developer portal, documentation, signup flow, code examples, support, YouTube channel, and 23 more developer resources.'
random_paper: 95
scopes:
- name: Polar Scopes
  scope_count: 2
  slug: polar-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 43.1
  delta: 3.6
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 59.0
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 94.7
      derived: 0
      marker_coverage: 0.0
      total: 19
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 53.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/polar/refs/heads/main/screenshots/polar-2026-06-20T191849.png
security:
- kind: authentication
  name: Polar Authentication
  slug: polar-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Polar Domain Security
  slug: polar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Polar Vulnerability Disclosure
  slug: polar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: polar
tags:
- Fitness
- Health
- Wearables
- Heart Rate
- Sports
- Training
- Sleep
- Activity Tracking
- Sensors
- Bluetooth
website: https://www.polar.com/en
---
