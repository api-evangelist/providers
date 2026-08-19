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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 62
  human_in_the_loop: 2
  name: Blues Wireless Agentic Access
  operation_count: 128
  slug: blues-wireless-agentic-access
  summary_line: 128 operations · 62 acting · 2 human-in-the-loop
api_count: 14
apis:
- description: The Notecard API is the firmware-level JSON API for interacting with Blues Notecard hardware modules directly over serial or I2C. It supports card, dfu, env, file, hub, note, ntn, var, and web request
  name: Notecard API
  slug: blues-wireless-notecard-api
- description: The alert API from Blues — 1 operation(s) for alert.
  name: Blues alert API
  slug: blues-wireless-alert-api
- description: Authorization operations
  name: Blues authorization API
  slug: blues-wireless-authorization-api
- description: Billing Account operations
  name: Blues billing_account API
  slug: blues-wireless-billing-account-api
- description: Device operations
  name: Blues device API
  slug: blues-wireless-device-api
- description: Event retrieval operations
  name: Blues event API
  slug: blues-wireless-event-api
- description: APIs for events and sessions for external devices
  name: Blues external devices API
  slug: blues-wireless-external-devices-api
- description: Batch job operations
  name: Blues jobs API
  slug: blues-wireless-jobs-api
- description: The monitor API from Blues — 2 operation(s) for monitor.
  name: Blues monitor API
  slug: blues-wireless-monitor-api
- description: Organization operations
  name: Blues organization API
  slug: blues-wireless-organization-api
- description: Project operations
  name: Blues project API
  slug: blues-wireless-project-api
- description: Route operations
  name: Blues route API
  slug: blues-wireless-route-api
- description: Project Usage information related to events, route logs, sessions, and data usage
  name: Blues usage API
  slug: blues-wireless-usage-api
- description: Webhook APIs for non-notecard event ingestion
  name: Blues webhook API
  slug: blues-wireless-webhook-api
artifact_total: 61
collections:
- collection_type: postman
  name: Notehub alert API
  slug: postman-blues-wireless-alert-api
- collection_type: postman
  name: Notehub alert authorization API
  slug: postman-blues-wireless-authorization-api
- collection_type: postman
  name: Notehub alert billing_account API
  slug: postman-blues-wireless-billing-account-api
- collection_type: postman
  name: Notehub alert device API
  slug: postman-blues-wireless-device-api
- collection_type: postman
  name: Notehub alert event API
  slug: postman-blues-wireless-event-api
- collection_type: postman
  name: Notehub alert external devices API
  slug: postman-blues-wireless-external-devices-api
- collection_type: postman
  name: Notehub alert jobs API
  slug: postman-blues-wireless-jobs-api
- collection_type: postman
  name: Notehub alert monitor API
  slug: postman-blues-wireless-monitor-api
- collection_type: postman
  name: Notehub alert organization API
  slug: postman-blues-wireless-organization-api
- collection_type: postman
  name: Notehub alert project API
  slug: postman-blues-wireless-project-api
- collection_type: postman
  name: Notehub alert route API
  slug: postman-blues-wireless-route-api
- collection_type: postman
  name: Notehub alert usage API
  slug: postman-blues-wireless-usage-api
- collection_type: postman
  name: Notehub alert webhook API
  slug: postman-blues-wireless-webhook-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Notehub alert API
  slug: open-blues-wireless-alert-api
- collection_type: open
  name: Notehub alert authorization API
  slug: open-blues-wireless-authorization-api
- collection_type: open
  name: Notehub alert billing_account API
  slug: open-blues-wireless-billing-account-api
- collection_type: open
  name: Notehub alert device API
  slug: open-blues-wireless-device-api
- collection_type: open
  name: Notehub alert event API
  slug: open-blues-wireless-event-api
- collection_type: open
  name: Notehub alert external devices API
  slug: open-blues-wireless-external-devices-api
- collection_type: open
  name: Notehub alert jobs API
  slug: open-blues-wireless-jobs-api
- collection_type: open
  name: Notehub alert monitor API
  slug: open-blues-wireless-monitor-api
- collection_type: open
  name: Notehub alert organization API
  slug: open-blues-wireless-organization-api
- collection_type: open
  name: Notehub alert project API
  slug: open-blues-wireless-project-api
- collection_type: open
  name: Notehub alert route API
  slug: open-blues-wireless-route-api
- collection_type: open
  name: Notehub alert usage API
  slug: open-blues-wireless-usage-api
- collection_type: open
  name: Notehub alert webhook API
  slug: open-blues-wireless-webhook-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/blues/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blues-wireless-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blues-wireless-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blues-wireless-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://blues.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.blues.io
- group: docs
  title: ''
  type: Documentation
  url: https://dev.blues.io/api-reference/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blues
- group: company
  title: ''
  type: Blog
  url: https://dev.blues.io/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://dev.blues.io/blog/whats-new-in-notehub/
- group: commercial
  title: ''
  type: Pricing
  url: https://blues.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.notehub.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/buildwithblues
- group: other
  title: ''
  type: X
  url: https://twitter.com/buildwithblues
- group: build
  title: ''
  type: SDKs
  url: https://blues.github.io/opensource/
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/blues-wireless/refs/heads/main/plans/blues-wireless-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/blues-wireless/refs/heads/main/rate-limits/blues-wireless-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/blues-wireless/refs/heads/main/finops/blues-wireless-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/blues-wireless/refs/heads/main/vocabulary/blues-wireless-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/blues-wireless/refs/heads/main/json-ld/blues-wireless-context.jsonld
created: '2026-06-12'
description: Blues (formerly Blues Wireless) is an IoT connectivity platform that provides hardware modules called Notecards and a cloud service called Notehub for routing device data from edge devices to cloud applications. The Notehub REST API enables developers to manage fleets of cellular, satellite, LoRa, and Wi-Fi connected devices across 130+ countries. Developers can use the API to retrieve device events, manage projects and fleets, configure routes to downstream cloud services, and monitor device health. Blues follows a consumption-based pricing model with no subscription fees, charging per ingressed event beyond a free monthly allowance bundled with each Notecard hardware purchase.
examples:
- key_count: 14
  name: Blues Wireless Notehub Api Examples
  slug: blues-wireless-notehub-api-examples
finops:
- name: Blues Wireless Finops
  service_category: ''
  slug: blues-wireless-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blues-wireless.png
json_schemas:
- name: BillingAccount
  property_count: 3
  slug: blues-wireless-billing-account
- name: Device
  property_count: 20
  slug: blues-wireless-device
- name: Event
  property_count: 60
  slug: blues-wireless-event
- name: Firmware
  property_count: 11
  slug: blues-wireless-firmware
- name: Fleet
  property_count: 8
  slug: blues-wireless-fleet
- name: Job
  property_count: 7
  slug: blues-wireless-job
- name: Monitor
  property_count: 21
  slug: blues-wireless-monitor
- name: Note
  property_count: 7
  slug: blues-wireless-note
- name: Notefile
  property_count: 3
  slug: blues-wireless-notefile
- name: Project
  property_count: 6
  slug: blues-wireless-project
- name: HttpRoute
  property_count: 8
  slug: blues-wireless-route
jsonld:
- class_count: 0
  name: Blues Wireless Context
  property_count: 36
  slug: blues-wireless-context
layout: provider
modified: '2026-06-12'
name: Blues
nav: Providers
network: true
overview: 'Blues publishes 13 APIs on the [APIs.io](https://apis.io/) network, including alert API, authorization API, billing_account API, and 10 more. Tagged areas include IoT, Cellular, Connectivity, Device Management, and Fleet Management.


  The Blues catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Blues'' developer surface includes authentication, documentation, engineering blog, changelog, pricing, and 15 more developer resources.'
plans:
- name: Blues Wireless Plans Pricing
  plan_count: 2
  slug: blues-wireless-plans-pricing
random_paper: 121
rate_limits:
- limit_count: 3
  name: Blues Wireless Rate Limits
  slug: blues-wireless-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Blues API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: blues-wireless-jsonschema-spectral-rules
score:
  band: developing
  composite: 50.8
  delta: -5.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 62.0
    developer_ergonomics: 45.2
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 65.8
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/blues-wireless/refs/heads/main/screenshots/blues-wireless-2026-06-20T173533.png
security:
- kind: authentication
  name: Blues Wireless Authentication
  slug: blues-wireless-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Blues Wireless Domain Security
  slug: blues-wireless-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blues-wireless
tags:
- IoT
- Cellular
- Connectivity
- Device Management
- Fleet Management
- Satellite
- LoRa
- WiFi
- Notecard
- Notehub
website: https://blues.com
---
