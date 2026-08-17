---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Samsung Agentic Access
  operation_count: 24
  slug: samsung-agentic-access
  summary_line: 24 operations · 12 acting
api_count: 12
apis:
- description: 'Samsung Knox provides enterprise-grade device management and security APIs. Knox Cloud APIs enable programmatic access to Knox Deployment Program, Knox Mobile Enrollment, Knox Configure, Knox Manage, '
  name: Knox Cloud APIs
  slug: knox-cloud
- description: 'The Samsung Health SDK enables developers to create health and fitness applications for Galaxy Watch and smartphones, providing access to health data including steps, heart rate, sleep, workouts, and '
  name: Samsung Health SDK
  slug: health-sdk
- description: Samsung Galaxy mobile SDKs provide access to device-specific hardware and software features including S Pen Remote, DeX desktop mode, AR Emoji, foldable device optimization, Samsung Blockchain, eSE (e
  name: Galaxy Mobile SDKs
  slug: galaxy-mobile
- description: The Samsung Smart TV developer platform enables development of Tizen-based applications for Samsung Smart TVs, including access to TV-specific APIs for media playback, user interface, smart signage, h
  name: Samsung Smart TV SDK
  slug: smart-tv
- description: The Bixby developer platform allows developers to integrate Samsung's voice assistant into their applications and create custom Bixby capsules (skills) that respond to natural language commands across
  name: Bixby Developer API
  slug: bixby
- description: Samsung Wallet API allows developers to add digital passes, tickets, boarding passes, loyalty cards, coupons, and payment cards to the Samsung Wallet app on Galaxy devices.
  name: Samsung Wallet API
  slug: samsung-wallet
- description: SmartApp registration and management.
  name: Samsung Apps API
  slug: samsung-apps-api
- description: Connected device management and control.
  name: Samsung Devices API
  slug: samsung-devices-api
- description: Location and room management.
  name: Samsung Locations API
  slug: samsung-locations-api
- description: Automation rule management.
  name: Samsung Rules API
  slug: samsung-rules-api
- description: Scene activation and management.
  name: Samsung Scenes API
  slug: samsung-scenes-api
- description: Device event subscriptions.
  name: Samsung Subscriptions API
  slug: samsung-subscriptions-api
artifact_total: 49
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Samsung SmartThings Apps API
  slug: open-samsung-apps-api
- collection_type: open
  name: Samsung SmartThings Apps Devices API
  slug: open-samsung-devices-api
- collection_type: open
  name: Samsung SmartThings Apps Locations API
  slug: open-samsung-locations-api
- collection_type: open
  name: Samsung SmartThings Apps Rules API
  slug: open-samsung-rules-api
- collection_type: open
  name: Samsung SmartThings Apps Scenes API
  slug: open-samsung-scenes-api
- collection_type: open
  name: Samsung SmartThings API
  slug: open-samsung-smartthings
- collection_type: open
  name: Samsung SmartThings Apps Subscriptions API
  slug: open-samsung-subscriptions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/samsung-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/samsung-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/samsung-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://developer.samsung.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/samsung-electronics
- group: docs
  title: Samsung Developer Portal
  type: Documentation
  url: https://developer.samsung.com/
- group: docs
  title: Samsung Knox Developer Documentation
  type: Documentation
  url: https://docs.samsungknox.com/dev/
- group: docs
  title: SmartThings Developer Documentation
  type: Documentation
  url: https://developer.smartthings.com/docs/
- group: build
  title: SmartThings Community GitHub
  type: GitHubOrganization
  url: https://github.com/SmartThingsCommunity
- group: build
  title: Samsung GitHub Organization
  type: GitHubOrganization
  url: https://github.com/samsung
- group: design
  title: Samsung API Spectral Rules
  type: SpectralRules
  url: rules/samsung-rules.yml
- group: docs
  title: Samsung SmartThings Device Schema
  type: JSONSchema
  url: json-schema/samsung-smartthings-device-schema.json
- group: design
  title: Samsung SmartThings Device Structure
  type: JSONStructure
  url: json-structure/samsung-smartthings-device-structure.json
- group: design
  title: Samsung JSON-LD Context
  type: JSONLDContext
  url: json-ld/samsung-context.jsonld
- group: build
  title: Samsung SmartThings List Devices Example
  type: Examples
  url: examples/samsung-list-devices-example.json
- group: build
  title: Samsung SmartThings Execute Device Command Example
  type: Examples
  url: examples/samsung-execute-device-command-example.json
- group: design
  title: Samsung Developer Vocabulary
  type: Vocabulary
  url: vocabulary/samsung-vocabulary.yml
created: '2025-02-08'
description: Samsung Electronics is a global technology leader offering developer platforms for building applications and services across mobile devices, IoT, smart home, enterprise security, and entertainment. The Samsung Developer ecosystem spans SmartThings (IoT and smart home platform), Knox (enterprise device security and management), Galaxy mobile SDKs, Smart TV, and Tizen cross-platform development. Samsung provides REST APIs, SDKs, and tools that enable developers to create connected experiences for hundreds of millions of Galaxy devices and Samsung smart home products worldwide.
examples:
- key_count: 4
  name: Samsung Execute Device Command Example
  slug: samsung-execute-device-command-example
- key_count: 6
  name: Samsung Executedevicecommands Example
  slug: samsung-executedevicecommands-example
- key_count: 4
  name: Samsung List Devices Example
  slug: samsung-list-devices-example
finops:
- name: Samsung Finops
  service_category: Consumer Electronics / IoT Platform
  slug: samsung-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/samsung.png
json_schemas:
- name: App
  property_count: 9
  slug: samsung-app
- name: CreateLocationRequest
  property_count: 8
  slug: samsung-createlocationrequest
- name: CreateRuleRequest
  property_count: 3
  slug: samsung-createrulerequest
- name: CreateSubscriptionRequest
  property_count: 2
  slug: samsung-createsubscriptionrequest
- name: Device
  property_count: 10
  slug: samsung-device
- name: DeviceCommandRequest
  property_count: 1
  slug: samsung-devicecommandrequest
- name: DeviceComponent
  property_count: 4
  slug: samsung-devicecomponent
- name: DeviceStatus
  property_count: 1
  slug: samsung-devicestatus
- name: Links
  property_count: 2
  slug: samsung-links
- name: Location
  property_count: 9
  slug: samsung-location
- name: Room
  property_count: 4
  slug: samsung-room
- name: Rule
  property_count: 6
  slug: samsung-rule
- name: Scene
  property_count: 9
  slug: samsung-scene
- name: Samsung SmartThings Device
  property_count: 13
  slug: samsung-smartthings-device
- name: Subscription
  property_count: 4
  slug: samsung-subscription
json_structures:
- name: Samsung Smartthings Device Structure
  property_count: 0
  slug: samsung-smartthings-device-structure
- name: Samsung Structure
  property_count: 0
  slug: samsung-structure
jsonld:
- class_count: 43
  name: Samsung Context
  property_count: 0
  slug: samsung-context
layout: provider
modified: '2026-05-19'
name: Samsung
nav: Providers
network: true
overview: 'Samsung publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Devices API, Locations API, and 3 more. Tagged areas include Consumer Electronics, Developer Platform, IoT, Mobile, and Smart Home.


  The Samsung catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Samsung''s developer surface includes authentication, engineering blog, documentation, code examples, and 13 more developer resources.'
plans:
- name: Samsung Plans Pricing
  plan_count: 1
  slug: samsung-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 1
  name: Samsung Rate Limits
  slug: samsung-rate-limits
rules:
- name: Samsung API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: samsung-jsonschema-spectral-rules
- name: Samsung API Rules
  rule_count: 13
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 9
  slug: samsung-rules
score:
  band: thin
  composite: 40.7
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 67.5
    developer_ergonomics: 21.7
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 10.5
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/samsung/refs/heads/main/screenshots/samsung-2026-06-20T193400.png
security:
- kind: authentication
  name: Samsung Authentication
  slug: samsung-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Samsung Domain Security
  slug: samsung-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: samsung
tags:
- Consumer Electronics
- Developer Platform
- IoT
- Mobile
- Smart Home
- Smart TV
- Wearables
website: https://developer.samsung.com/
---
