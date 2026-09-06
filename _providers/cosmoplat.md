---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The MQTT publish/subscribe surface of the COSMOPlat IoT development platform, documented in 数据流转引擎 (data flow engine). Devices publish telemetry to iot.cosmoplat.com:1883 on v1/devices/me/telemetry; t
  name: COSMOPlat IoT Telemetry (MQTT)
  slug: cosmoplat-iot-telemetry-mqtt
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The Alarm Records API from Cosmoplat — 2 operation(s) for alarm records.
  name: Cosmoplat Alarm Records API
  slug: cosmoplat-alarm-records-api
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The Alarm Rules API from Cosmoplat — 3 operation(s) for alarm rules.
  name: Cosmoplat Alarm Rules API
  slug: cosmoplat-alarm-rules-api
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The Attribute Data API from Cosmoplat — 1 operation(s) for attribute data.
  name: Cosmoplat Attribute Data API
  slug: cosmoplat-attribute-data-api
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The Device Management API from Cosmoplat — 4 operation(s) for device management.
  name: Cosmoplat Device Management API
  slug: cosmoplat-device-management-api
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The Device RPC API from Cosmoplat — 2 operation(s) for device rpc.
  name: Cosmoplat Device RPC API
  slug: cosmoplat-device-rpc-api
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The Product Management API from Cosmoplat — 3 operation(s) for product management.
  name: Cosmoplat Product Management API
  slug: cosmoplat-product-management-api
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The Rule Chains API from Cosmoplat — 3 operation(s) for rule chains.
  name: Cosmoplat Rule Chains API
  slug: cosmoplat-rule-chains-api
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The Thing Model (Telemetry Profile) API from Cosmoplat — 6 operation(s) for thing model (telemetry profile).
  name: Cosmoplat Thing Model (Telemetry Profile) API
  slug: cosmoplat-thing-model-telemetry-profile-api
- baseURL: mqtt://iot-mqtt.cosmoplat.com:11883
  baseurl_source: declared
  description: The Time-series Data API from Cosmoplat — 1 operation(s) for time-series data.
  name: Cosmoplat Time-series Data API
  slug: cosmoplat-time-series-data-api
artifact_total: 17
asyncapis:
- description: ''
  name: Cosmoplat Event Surface
  slug: cosmoplat-event-surface
- description: Machine-readable transcription of the COSMOPlat 物联开发平台 (IoT development platform) 数据流转引擎 / "data flow engine" documentation published at https://www.cosmoplat.com/help/detail/304/1064 That page publis
  name: COSMOPlat IoT Telemetry (MQTT)
  slug: cosmoplat-iot-telemetry-asyncapi
collections:
- collection_type: open
  name: COSMOPlat IoT Platform OpenAPI
  slug: open-cosmoplat-iot-platform
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cosmoplat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cosmoplat.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openlab.cosmoplat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cosmoplat.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://www.cosmoplat.com/help/detail/304/1038
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cosmoplat.com/help/detail/304/1026
- group: operate
  title: ''
  type: Support
  url: https://tianyun.cosmoplat.com/#/crworkorder
- group: company
  title: ''
  type: Blog
  url: https://openlab.cosmoplat.com/article-list
- group: company
  title: ''
  type: News
  url: https://www.cosmoplat.com/news/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cosmoplat-dev
- group: start
  title: ''
  type: Login
  url: https://tianyun.cosmoplat.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sec.cosmoplat.com/api/agreement/service/1641867039600051
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sec.cosmoplat.com/api/agreement/private/1641867039600051
- group: other
  title: ''
  type: Products
  url: https://www.cosmoplat.com/product
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cosmoplat-event-surface.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/cosmoplat-iot-telemetry-asyncapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cosmoplat-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cosmoplat-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cosmoplat-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cosmoplat-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cosmoplat-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/cosmoplat-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cosmoplat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cosmoplat-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cosmoplat-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cosmoplat-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cosmoplat-iot-platform-overlay.yaml
created: '2026-08-11'
description: COSMOPlat (卡奥斯 COSMOPlat) is the industrial internet platform incubated by Haier Group and operated by COSMOPlat Digital Technology (Qingdao) Co., Ltd. Launched in 2017, it was China's first self-developed industrial internet platform built around mass customization, digitally integrating user interaction, R&D, procurement, production and service across a factory and its supply chain. Its product line spans smart-factory and MES systems, industrial IoT device connectivity, chemical-park management, smart energy control, equipment health management and a D3OS digital-twin offering, and it has been applied across roughly twenty industries and more than twenty countries. The developer-facing surface is the 物联开发平台 (IoT development platform), which publishes a public HTML API reference covering product, device, alarm, rule-chain, thing-model, telemetry and device-RPC operations, alongside an MQTT telemetry publish/subscribe surface. COSMOPlat also runs an open-source developer community
  at openlab.cosmoplat.com and a GitHub organization at cosmoplat-dev.
image: https://www.cosmoplat.com/_nuxt/img/logo_blue_no.7350967.svg
layout: provider
modified: '2026-08-11'
name: Cosmoplat
nav: Providers
network: true
overview: 'Cosmoplat publishes 10 APIs on the [APIs.io](https://apis.io/) network, including IoT Telemetry (MQTT), Alarm Records API, Alarm Rules API, and 7 more. Tagged areas include Company, Industrial Internet, Industrial IoT, Internet of Things, and Manufacturing.


  The Cosmoplat catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Cosmoplat''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, product news, authentication, and 21 more developer resources.'
plans:
- name: Cosmoplat Plans Pricing
  plan_count: 0
  slug: cosmoplat-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Cosmoplat Rate Limits
  slug: cosmoplat-rate-limits
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 22.6
    developer_ergonomics: 42.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 28.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cosmoplat/refs/heads/main/screenshots/cosmoplat-2026-08-17T123144.png
security:
- kind: authentication
  name: Cosmoplat Authentication
  slug: cosmoplat-authentication
  summary_line: userPassword/deviceToken · 3 schemes
- kind: domain-security
  name: Cosmoplat Domain Security
  slug: cosmoplat-domain-security
  summary_line: TLSv1.3
slug: cosmoplat
tags:
- Company
- Industrial Internet
- Industrial IoT
- Internet of Things
- Manufacturing
- Smart Factory
- Device Management
- Digital Transformation
- MQTT
- Telemetry
- China
website: https://www.cosmoplat.com/
---
