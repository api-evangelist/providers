---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 61
  human_in_the_loop: 3
  name: Withings Agentic Access
  operation_count: 62
  slug: withings-agentic-access
  summary_line: 62 operations · 61 acting · 3 human-in-the-loop
api_count: 1
apis:
- description: The Withings Mobile SDK allows developers to integrate Withings health data directly into iOS and Android mobile applications. The SDK handles device pairing, data synchronization, and health metric c
  name: Withings Mobile SDK
  slug: withings-mobile-sdk
- description: The Withings Advanced Research API provides access to detailed and granular health biomarker data for academic and clinical research purposes, including full biomarker packs with extended data sets be
  name: Withings Advanced Research API
  slug: withings-advanced-research-api
- description: These webservices allows you to get user's answers from surveys
  name: Withings answers API
  slug: withings-answers-api
- description: The device API from Withings — 3 operation(s) for device.
  name: Withings device API
  slug: withings-device-api
- description: The following services are part of the Logistics APIs. Refer to [this section](/developer-guide/v3/integration-guide/dropship-only/logistics-api/overview-create-order) for more information. The Logist
  name: Withings dropshipment API
  slug: withings-dropshipment-api
- description: Returns ECG (EKG) signal points in micro-volt (μV). You can use the [Heart - List](#operation/heartv2-list) service to get the list of ECG records and their corresponding ```signalid``` and then use [
  name: Withings heart API
  slug: withings-heart-api
- description: The following services gives access to several types of Health Data collected by a user. The data are only available once a synchronization occured between the device and Withings servers (which might
  name: Withings measure API
  slug: withings-measure-api
- description: These services will allow you to be notified when new data is collected by Withings devices, or when specific events happen. Learn more about our notification services in [the dedicated section](/deve
  name: Withings notify API
  slug: withings-notify-api
- description: These webservices allows you to to manage Health Nudges. Read the [Health Nudges Integration Guide](/developer-guide/v3/integration-guide/health-nudges/health-nudge-overview) for more information.
  name: Withings nudge API
  slug: withings-nudge-api
- description: These webservices allows you to to manage Health Nudges Campaign. Read the [Health Nudges Integration Guide](/developer-guide/v3/integration-guide/health-nudges/health-nudge-overview) for more informa
  name: Withings nudgecampaign API
  slug: withings-nudgecampaign-api
- description: <br>The Withings API uses OAuth 2.0, an industry-standard protocol for authorization.<br> OAuth 2.0 enables your application to access user-specific data with a secure and seamless way without requiri
  name: Withings oauth2 API
  slug: withings-oauth2-api
- description: The following services are part of the Logistics APIs. Refer to [this section](/developer-guide/v3/integration-guide/dropship-only/logistics-api/overview-create-order) for more information.
  name: Withings order API
  slug: withings-order-api
- description: Raw Data webservices are part of the Advanced research API that allows to collect high frequency PPG and accelerometer data (around 25Hz). These APIs are compatible only with the Withings ScanWatch. I
  name: Withings rawdata API
  slug: withings-rawdata-api
- description: The following services are part of the Logistics APIs. Refer to [this section](/developer-guide/v3/integration-guide/dropship-only/logistics-api/overview-create-order) for more information.
  name: Withings signature API
  slug: withings-signature-api
- description: Returns data related to user sleep activities, wether they are captured by an Activity Tracker or a Sleep Monitor. The data are only available once a synchronization occured between the device and Wit
  name: Withings sleep API
  slug: withings-sleep-api
- description: First the [Stetho - List](#operation/stethov2-list) API should be called to fetch the stetho signalIds which should be fetched individually using the [Stetho - Get](#operation/stethov2-get) API.
  name: Withings stetho API
  slug: withings-stetho-api
- description: These webservices allows you to to manage user's surveys
  name: Withings survey API
  slug: withings-survey-api
- description: The user API from Withings — 7 operation(s) for user.
  name: Withings user API
  slug: withings-user-api
artifact_total: 55
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Withings developer documentation answers API
  slug: open-withings-answers-api
- collection_type: open
  name: Withings developer documentation answers device API
  slug: open-withings-device-api
- collection_type: open
  name: Withings developer documentation answers dropshipment API
  slug: open-withings-dropshipment-api
- collection_type: open
  name: Withings developer documentation answers heart API
  slug: open-withings-heart-api
- collection_type: open
  name: Withings developer documentation answers measure API
  slug: open-withings-measure-api
- collection_type: open
  name: Withings developer documentation answers notify API
  slug: open-withings-notify-api
- collection_type: open
  name: Withings developer documentation answers nudge API
  slug: open-withings-nudge-api
- collection_type: open
  name: Withings developer documentation answers nudgecampaign API
  slug: open-withings-nudgecampaign-api
- collection_type: open
  name: Withings developer documentation answers oauth2 API
  slug: open-withings-oauth2-api
- collection_type: open
  name: Withings developer documentation answers order API
  slug: open-withings-order-api
- collection_type: open
  name: Withings developer documentation answers rawdata API
  slug: open-withings-rawdata-api
- collection_type: open
  name: Withings developer documentation answers signature API
  slug: open-withings-signature-api
- collection_type: open
  name: Withings developer documentation answers sleep API
  slug: open-withings-sleep-api
- collection_type: open
  name: Withings developer documentation answers stetho API
  slug: open-withings-stetho-api
- collection_type: open
  name: Withings developer documentation answers survey API
  slug: open-withings-survey-api
- collection_type: open
  name: Withings developer documentation answers user API
  slug: open-withings-user-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/withings-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/withings-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/withings-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.withings.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.withings.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.withings.com/api-reference/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.withings.com/developer-guide/v3/integration-guide/public-health-data-api/get-access/oauth-web-flow/
- group: design
  title: ''
  type: Webhooks
  url: https://developer.withings.com/developer-guide/v3/data-api/notifications/notification-overview/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withings.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/withings
- group: other
  title: ''
  type: X
  url: https://x.com/withings
- group: company
  title: ''
  type: Blog
  url: https://www.withings.com/blog/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/withings/withings-health-solutions/documentation/hx5ar4t/withings-public-api-integration
- group: commercial
  title: ''
  type: Plans
  url: plans/withings-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/withings-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/withings-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/withings-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/withings-context.jsonld
created: '2026-06-13'
description: Withings is a connected health device platform providing a REST API for accessing data from smart scales, blood pressure monitors, sleep trackers, thermometers, and fitness watches. The API uses OAuth2 for authentication and provides access to a wide range of health biomarkers including body composition, cardiovascular data, sleep metrics, activity tracking, and clinical-grade measurements. Partners and developers can integrate Withings health data into their applications for remote patient monitoring, wellness platforms, and research applications.
examples:
- key_count: 3
  name: Withings Activity Example
  slug: withings-activity-example
- key_count: 3
  name: Withings Measure Example
  slug: withings-measure-example
- key_count: 3
  name: Withings Oauth2 Token Example
  slug: withings-oauth2-token-example
- key_count: 3
  name: Withings Sleep Summary Example
  slug: withings-sleep-summary-example
finops:
- name: Withings Finops
  service_category: ''
  slug: withings-finops
graphqls:
- description: This conceptual GraphQL schema models the Withings health platform API, which provides access to data from Withings connected health devices including smart scales, blood pressure monitors, sleep trac
  name: Withings GraphQL Schema
  slug: withings-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/withings.png
json_schemas:
- name: Activity Object
  property_count: 25
  slug: withings-activity-object
- name: Heart Measurement Object
  property_count: 8
  slug: withings-heart-measurement-object
- name: Measure Object
  property_count: 6
  slug: withings-measure-object
- name: Measuregrp Object
  property_count: 12
  slug: withings-measuregrp-object
- name: Notify Object
  property_count: 3
  slug: withings-notify-object
- name: Sleep Summary Object
  property_count: 12
  slug: withings-sleep-summary-object
- name: User Device Object
  property_count: 14
  slug: withings-user-device-object
- name: Workout Object
  property_count: 11
  slug: withings-workout-object
jsonld:
- class_count: 0
  name: Withings Context
  property_count: 65
  slug: withings-context
layout: provider
modified: '2026-06-13'
name: Withings
nav: Providers
network: true
overview: 'Withings publishes 16 APIs on the [APIs.io](https://apis.io/) network, including answers API, device API, dropshipment API, and 13 more. Tagged areas include Health, Wearables, Connected Devices, Body Composition, and Sleep Tracking.


  The Withings catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Withings'' developer surface includes documentation, API reference, authentication, engineering blog, and 14 more developer resources.'
plans:
- name: Withings Plans Pricing
  plan_count: 2
  slug: withings-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Withings Rate Limits
  slug: withings-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Withings API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: withings-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 35.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 25.0
    contract_quality: 64.7
    developer_ergonomics: 19.0
    discoverability: 63.0
    governance: 25.0
    operational_transparency: 28.9
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/withings/refs/heads/main/screenshots/withings-2026-06-20T201529.png
security:
- kind: domain-security
  name: Withings Domain Security
  slug: withings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: withings
tags:
- Health
- Wearables
- Connected Devices
- Body Composition
- Sleep Tracking
- Blood Pressure
- Activity Tracking
- Remote Patient Monitoring
- Authentication
- Webhook
website: https://www.withings.com/
---
