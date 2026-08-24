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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Smartthings Agentic Access
  operation_count: 65
  slug: smartthings-agentic-access
  summary_line: 65 operations · 35 acting
api_count: 14
apis:
- description: SmartApp registrations (Lambda or webhook endpoints).
  name: Samsung SmartThings Apps API
  slug: smartthings-apps-api
- description: Standard and custom capability definitions.
  name: Samsung SmartThings Capabilities API
  slug: smartthings-capabilities-api
- description: Execute commands, create events, and read device/component/capability status.
  name: Samsung SmartThings Device Commands & Status API
  slug: smartthings-device-commands-status-api
- description: Access, control, install, update, and delete devices.
  name: Samsung SmartThings Devices API
  slug: smartthings-devices-api
- description: Event history for devices and locations.
  name: Samsung SmartThings History API
  slug: smartthings-history-api
- description: Per-user installations of a SmartApp.
  name: Samsung SmartThings Installed Apps API
  slug: smartthings-installed-apps-api
- description: Locations (homes) and their Modes.
  name: Samsung SmartThings Locations API
  slug: smartthings-locations-api
- description: Device presentation and configuration metadata.
  name: Samsung SmartThings Presentations API
  slug: smartthings-presentations-api
- description: Groupings of devices within a Location.
  name: Samsung SmartThings Rooms API
  slug: smartthings-rooms-api
- description: Condition/action Automations over connected devices.
  name: Samsung SmartThings Rules API
  slug: smartthings-rules-api
- description: Saved sets of device states that can be executed on demand.
  name: Samsung SmartThings Scenes API
  slug: smartthings-scenes-api
- description: Future/cron executions for Installed Apps.
  name: Samsung SmartThings Schedules API
  slug: smartthings-schedules-api
- description: Event subscriptions for Installed Apps.
  name: Samsung SmartThings Subscriptions API
  slug: smartthings-subscriptions-api
- description: Software devices for testing automations and integrations.
  name: Samsung SmartThings Virtual Devices API
  slug: smartthings-virtual-devices-api
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Samsung SmartThings Apps API
  slug: open-smartthings-apps-api
- collection_type: open
  name: Samsung SmartThings Apps Capabilities API
  slug: open-smartthings-capabilities-api
- collection_type: open
  name: Samsung SmartThings Apps Device Commands & Status API
  slug: open-smartthings-device-commands-status-api
- collection_type: open
  name: Samsung SmartThings Apps Devices API
  slug: open-smartthings-devices-api
- collection_type: open
  name: Samsung SmartThings Apps History API
  slug: open-smartthings-history-api
- collection_type: open
  name: Samsung SmartThings Apps Installed Apps API
  slug: open-smartthings-installed-apps-api
- collection_type: open
  name: Samsung SmartThings Apps Locations API
  slug: open-smartthings-locations-api
- collection_type: open
  name: Samsung SmartThings Apps Presentations API
  slug: open-smartthings-presentations-api
- collection_type: open
  name: Samsung SmartThings Apps Rooms API
  slug: open-smartthings-rooms-api
- collection_type: open
  name: Samsung SmartThings Apps Rules API
  slug: open-smartthings-rules-api
- collection_type: open
  name: Samsung SmartThings Apps Scenes API
  slug: open-smartthings-scenes-api
- collection_type: open
  name: Samsung SmartThings Apps Schedules API
  slug: open-smartthings-schedules-api
- collection_type: open
  name: Samsung SmartThings Apps Subscriptions API
  slug: open-smartthings-subscriptions-api
- collection_type: open
  name: Samsung SmartThings Apps Virtual Devices API
  slug: open-smartthings-virtual-devices-api
- collection_type: open
  name: Samsung SmartThings API
  slug: open-smartthings
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smartthings-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smartthings-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smartthings-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smartthings-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/smartthings-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SmartThingsCommunity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/smartthings
- group: company
  title: ''
  type: Website
  url: https://www.smartthings.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.smartthings.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/smartthings-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smartthings-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smartthings-finops.yml
created: '2026-07-03'
description: Samsung SmartThings is a smart-home IoT platform for connecting, controlling, and automating devices across a home. The SmartThings API is a RESTful interface (base https://api.smartthings.com/v1) that lets integrations control devices, read device status, manage locations, rooms, and modes, build automations with Rules and Scenes, define and inspect capabilities, and build SmartApps that subscribe to events and run schedules. Authentication is via a Personal Access Token (PAT) for testing or OAuth 2.0 for production integrations. SmartThings publishes a real OpenAPI/Swagger definition at swagger.api.smartthings.com/public/st-api.yml. Event delivery is push-based over HTTP webhooks (SmartApp lifecycle callbacks and the Enterprise Eventing API sinks/subscriptions), not a public WebSocket.
finops:
- name: Smartthings Finops
  service_category: IoT and Smart Home Platform
  slug: smartthings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smartthings.png
layout: provider
modified: '2026-07-03'
name: Samsung SmartThings
nav: Providers
network: true
overview: 'Samsung SmartThings publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Capabilities API, Device Commands & Status API, and 11 more. Tagged areas include Smart Home, IoT, Home Automation, Devices, and Samsung.


  Samsung SmartThings'' developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Smartthings Plans Pricing
  plan_count: 2
  slug: smartthings-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 17
  name: Smartthings Rate Limits
  slug: smartthings-rate-limits
scopes:
- name: Smartthings Scopes
  scope_count: 8
  slug: smartthings-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: thin
  composite: 36.1
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 56.9
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Smartthings Authentication
  slug: smartthings-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Smartthings Domain Security
  slug: smartthings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Smartthings Vulnerability Disclosure
  slug: smartthings-vulnerability-disclosure
  summary_line: Bugcrowd
slug: smartthings
tags:
- Smart Home
- IoT
- Home Automation
- Devices
- Samsung
website: https://www.smartthings.com
---
