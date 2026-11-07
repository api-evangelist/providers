---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Cesanta Agentic Access
  operation_count: 12
  slug: cesanta-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- baseURL: https://dash.mongoose-os.com/api/v2
  baseurl_source: declared
  description: Device data storage and retrieval
  name: Cesanta Data API
  slug: cesanta-data-api
- baseURL: https://dash.mongoose-os.com/api/v2
  baseurl_source: declared
  description: Device registration, updates, RPC, and OTA
  name: Cesanta Devices API
  slug: cesanta-devices-api
- baseURL: https://dash.mongoose-os.com/api/v2
  baseurl_source: declared
  description: API key management
  name: Cesanta Keys API
  slug: cesanta-keys-api
- baseURL: https://dash.mongoose-os.com/api/v2
  baseurl_source: declared
  description: Notification logs
  name: Cesanta Logs API
  slug: cesanta-logs-api
artifact_total: 16
collections:
- collection_type: open
  name: Cesanta mDash REST Data API
  slug: open-cesanta-data-api
- collection_type: open
  name: Cesanta mDash REST Data Devices API
  slug: open-cesanta-devices-api
- collection_type: open
  name: Cesanta mDash REST Data Keys API
  slug: open-cesanta-keys-api
- collection_type: open
  name: Cesanta mDash REST Data Logs API
  slug: open-cesanta-logs-api
common:
- group: other
  href: https://artifacts.apis.io/cesanta/capabilities/cesanta-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/cesanta-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/cesanta/plans/cesanta-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cesanta-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://cesanta.com/blog/
- group: docs
  href: https://artifacts.apis.io/cesanta/openapi/_original/cesanta-mdash-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/cesanta-mdash-openapi.yml
- group: auth
  href: https://artifacts.apis.io/cesanta/authentication/cesanta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cesanta-authentication.yml
- group: design
  href: https://artifacts.apis.io/cesanta/conventions/cesanta-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cesanta-conventions.yml
- group: design
  href: https://artifacts.apis.io/cesanta/errors/cesanta-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cesanta-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cesanta/data-model/cesanta-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cesanta-data-model.yml
- group: design
  href: https://artifacts.apis.io/cesanta/lifecycle/cesanta-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cesanta-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/cesanta/conformance/cesanta-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cesanta-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cesanta/mcp/cesanta-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cesanta-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cesanta/llms/cesanta-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cesanta-llms.txt
- group: other
  href: https://artifacts.apis.io/cesanta/overlays/cesanta-mdash-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cesanta-mdash-overlay.yaml
- group: build
  href: https://artifacts.apis.io/cesanta/packages/cesanta-packages.yml
  title: ''
  type: Packages
  url: packages/cesanta-packages.yml
- group: agent
  href: https://artifacts.apis.io/cesanta/well-known/cesanta-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cesanta-well-known.yml
- group: agent
  href: https://artifacts.apis.io/cesanta/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/cesanta/agentic-access/cesanta-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cesanta-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/cesanta/security/cesanta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cesanta-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mdash.net/home/
- group: docs
  title: ''
  type: Documentation
  url: https://mongoose-os.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://mongoose-os.com/docs/mdash/api.md
- group: start
  title: ''
  type: GettingStarted
  url: https://mdash.net/home/tech-guides.html
- group: operate
  title: ''
  type: Support
  url: https://forum.mdash.net
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cesanta
- group: commercial
  title: ''
  type: Pricing
  url: https://mdash.net/home/pricing.html
- group: start
  title: ''
  type: Login
  url: https://mdash.net/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cesanta.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mongoose-os.com/terms.html
- group: company
  title: ''
  type: Website
  url: https://cesanta.com
created: '2026-07-17'
description: Cesanta is an embedded software and IoT company, established in 2013 to develop and support the Mongoose embedded web server and networking library (HTTP, WebSocket, MQTT, CoAP, TCP/IP) that ships in over 100 million devices from vendors such as Siemens, Bosch, Samsung, Schneider Electric, Broadcom, Google, and Caterpillar — and even runs aboard the International Space Station. Alongside the Mongoose library, Cesanta builds Mongoose OS (an IoT firmware development framework for ESP32, ESP8266, STM32 and other microcontrollers with AWS/Azure/Google Cloud integration), VCON.io (remote firmware update and automated firmware testing), and mDash — a managed IoT device cloud offering device management, over-the-air (OTA) updates, a device database/shadow, remote RPC, access control, and a documented REST API for programmatic fleet management.
finops:
- has_sources: true
  method: derived
  name: Cesanta Finops
  primary_unit: device
  service_category: ''
  slug: cesanta-finops
  template: false
image: https://cesanta.com/images/logo1.png
layout: provider
modified: '2026-10-06'
name: Cesanta
nav: Providers
network: true
overview: 'Cesanta publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Data API, Devices API, Keys API, and 1 more. Tagged areas include Company, IoT, Embedded, Device Management, and Firmware.


  The Cesanta catalog on APIs.io includes 1 Spectral governance ruleset.


  Cesanta''s developer surface includes engineering blog, authentication, documentation, API reference, getting-started guide, support, pricing, and 22 more developer resources.'
plans:
- name: Cesanta Plans Pricing
  plan_count: 3
  slug: cesanta-plans-pricing
- name: Cesanta Price Estimates
  plan_count: 0
  slug: cesanta-price-estimates
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Cesanta API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: cesanta-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 72.4
    contract_governance: 18.2
    contract_quality: 52.7
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/cesanta/cesanta-2026-07-25T205012.png
security:
- kind: authentication
  name: Cesanta Authentication
  slug: cesanta-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cesanta Domain Security
  slug: cesanta-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: Manage mDash IoT devices
  slug: cesanta-manage-devices
slug: cesanta
tags:
- Company
- IoT
- Embedded
- Device Management
- Firmware
- OTA
- Networking
- MQTT
website: https://cesanta.com
---
