---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
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
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: These webservices allows you to get user's answers from surveys
  name: Withings Answers API
  slug: withings-answers-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: The device API from Withings — 3 operation(s) for device.
  name: Withings Device API
  slug: withings-device-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: The following services are part of the Logistics APIs. Refer to [this section](/developer-guide/v3/integration-guide/dropship-only/logistics-api/overview-create-order) for more information. The Logist
  name: Withings Dropshipment API
  slug: withings-dropshipment-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: Returns ECG (EKG) signal points in micro-volt (μV). You can use the [Heart - List](#operation/heartv2-list) service to get the list of ECG records and their corresponding ```signalid``` and then use [
  name: Withings Heart API
  slug: withings-heart-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: The following services gives access to several types of Health Data collected by a user. The data are only available once a synchronization occured between the device and Withings servers (which might
  name: Withings Measure API
  slug: withings-measure-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: These services will allow you to be notified when new data is collected by Withings devices, or when specific events happen. Learn more about our notification services in [the dedicated section](/deve
  name: Withings Notify API
  slug: withings-notify-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: These webservices allows you to to manage Health Nudges. Read the [Health Nudges Integration Guide](/developer-guide/v3/integration-guide/health-nudges/health-nudge-overview) for more information.
  name: Withings Nudge API
  slug: withings-nudge-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: These webservices allows you to to manage Health Nudges Campaign. Read the [Health Nudges Integration Guide](/developer-guide/v3/integration-guide/health-nudges/health-nudge-overview) for more informa
  name: Withings Nudgecampaign API
  slug: withings-nudgecampaign-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: The following services are part of the Logistics APIs. Refer to [this section](/developer-guide/v3/integration-guide/dropship-only/logistics-api/overview-create-order) for more information.
  name: Withings Order API
  slug: withings-order-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: The following services are part of the Logistics APIs. Refer to [this section](/developer-guide/v3/integration-guide/dropship-only/logistics-api/overview-create-order) for more information.
  name: Withings Signature API
  slug: withings-signature-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: Returns data related to user sleep activities, wether they are captured by an Activity Tracker or a Sleep Monitor. The data are only available once a synchronization occured between the device and Wit
  name: Withings Sleep API
  slug: withings-sleep-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: First the [Stetho - List](#operation/stethov2-list) API should be called to fetch the stetho signalIds which should be fetched individually using the [Stetho - Get](#operation/stethov2-get) API.
  name: Withings Stetho API
  slug: withings-stetho-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: These webservices allows you to to manage user's surveys
  name: Withings Survey API
  slug: withings-survey-api
- baseURL: https://wbsapi.withings.net
  baseurl_source: declared
  description: The user API from Withings — 7 operation(s) for user.
  name: Withings User API
  slug: withings-user-api
- baseURL: https://developer.withings.com
  baseurl_source: declared
  description: <br>The Withings API uses OAuth 2.0, an industry-standard protocol for authorization.<br> OAuth 2.0 enables your application to access user-specific data with a secure and seamless way without requiri
  name: Withings Oauth2 API
  slug: withings-oauth2-api
- baseURL: https://developer.withings.com
  baseurl_source: declared
  description: Raw Data webservices are part of the Advanced research API that allows to collect high frequency PPG and accelerometer data (around 25Hz). These APIs are compatible only with the Withings ScanWatch. I
  name: Withings Raw Data API
  slug: withings-raw-data-api
artifact_total: 53
collections:
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
- group: company
  title: ''
  type: Blog
  url: https://www.withings.com/en-us/blogs/withings-blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.withings.com/en-us/blogs/withings-blog.atom
- group: other
  href: https://artifacts.apis.io/withings/capabilities/withings-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/withings-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/withings/agentic-access/withings-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/withings-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/withings/security/withings-domain-security.yml
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
  href: https://artifacts.apis.io/withings/plans/withings-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/withings-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/withings/rate-limits/withings-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/withings-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/withings/finops/withings-finops.yml
  title: ''
  type: FinOps
  url: finops/withings-finops.yml
- group: design
  href: https://artifacts.apis.io/withings/vocabulary/withings-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/withings-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/withings/json-ld/withings-context.jsonld
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
- has_sources: false
  method: generated
  name: Withings Finops
  primary_unit: ''
  service_category: ''
  slug: withings-finops
  template: true
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
modified: '2026-10-06'
name: Withings
nav: Providers
network: true
overview: 'Withings publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Answers API, Device API, Dropshipment API, and 15 more. Tagged areas include Health, Wearables, Connected Devices, Body Composition, and Sleep Tracking.


  The Withings catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Withings'' developer surface includes engineering blog, documentation, API reference, authentication, and 16 more developer resources.'
plans:
- name: Withings Plans Pricing
  plan_count: 2
  slug: withings-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Withings Rate Limits
  slug: withings-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Withings — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: withings-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.5
  facets:
    access_clarity: 5.3
    contract_governance: 23.5
    contract_quality: 58.7
    developer_ergonomics: 33.3
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/withings/withings-2026-06-20T201529.png
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
- OAuth
- Webhook
- Wellness
- Authentication
website: https://www.withings.com/
---
