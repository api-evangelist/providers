---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - '{''url'': ''https://nest.com'', ''status'': 301, ''note'': ''declared website redirects to https://store.google.com/us/category/connected_home?hl=en-US&GoogleNest&utm_source=nest_redirect&utm_medium=google_oo&utm_campaign=homepage — a different registrable domain (nest.com -> google.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Google Nest Device Access REST API for accessing, controlling, and managing authorized Nest devices (thermostats, cameras, doorbells, Hub Max) via enterprises/structures/rooms/devices resources and a '
  name: Smart Device Management (SDM) API
  slug: smart-device-management-sdm-api
artifact_total: 9
asyncapis:
- description: ''
  name: Nest Events
  slug: nest-events
common:
- group: commercial
  href: https://artifacts.apis.io/nest/plans/nest-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nest-plans-pricing.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/google/
- group: auth
  href: https://artifacts.apis.io/nest/security/nest-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nest.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.google.com/nest/device-access
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/nest/device-access
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/nest/device-access/reference/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/nest/device-access/registration
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/nest/device-access/support
- group: start
  title: ''
  type: SignUp
  url: https://console.nest.google.com/device-access
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.google.com/nest/device-access/registration
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: auth
  href: https://artifacts.apis.io/nest/authentication/nest-authentication.yml
  title: ''
  type: Authentication
  url: authentication/nest-authentication.yml
- group: auth
  href: https://artifacts.apis.io/nest/scopes/nest-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/nest-scopes.yml
- group: design
  href: https://artifacts.apis.io/nest/conventions/nest-conventions.yml
  title: ''
  type: Conventions
  url: conventions/nest-conventions.yml
- group: design
  href: https://artifacts.apis.io/nest/errors/nest-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nest-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nest/data-model/nest-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nest-data-model.yml
- group: design
  href: https://artifacts.apis.io/nest/lifecycle/nest-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/nest-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/nest/lifecycle/nest-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/nest-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/nest/conformance/nest-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nest-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nest/mcp/nest-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nest-mcp.yml
- group: build
  href: https://artifacts.apis.io/nest/packages/nest-packages.yml
  title: ''
  type: Packages
  url: packages/nest-packages.yml
- group: build
  href: https://artifacts.apis.io/nest/packages/nest-packages.yml
  title: ''
  type: SDKs
  url: packages/nest-packages.yml
- group: agent
  href: https://artifacts.apis.io/nest/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/nest/asyncapi/nest-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/nest-events.yml
- group: agent
  href: https://artifacts.apis.io/nest/llms/nest-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nest-llms.txt
created: '2026-07-17'
description: Nest is Google's smart home brand — thermostats, cameras, doorbells, and the Nest Hub — originally founded as Nest Labs (a Lightspeed Venture Partners portfolio company) and acquired by Google. Developers integrate with authorized Nest devices through the Google Nest Device Access program and its Smart Device Management (SDM) API, a Google Cloud REST API authorized with Google OAuth 2.0. The API lets partner apps list structures, rooms, and devices, read device traits (temperature, humidity, camera, doorbell), and execute trait commands, with asynchronous device events delivered via Google Cloud Pub/Sub. The legacy "Works with Nest" API was retired and superseded by Device Access.
finops:
- has_sources: true
  method: derived
  name: Nest Finops
  primary_unit: account
  service_category: ''
  slug: nest-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nest.png
layout: provider
modified: '2026-07-20'
name: Nest
nav: Providers
network: true
overview: 'Nest is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Smart Home, IoT, and Home Automation.


  The Nest catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nest''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, authentication, and 21 more developer resources.'
plans:
- name: Nest Plans Pricing
  plan_count: 1
  slug: nest-plans-pricing
random_paper: 10
scopes:
- name: Nest Scopes
  scope_count: 1
  slug: nest-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 5.8
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 63.7
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 47.2
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nest/nest-2026-08-07T184913.png
security:
- kind: authentication
  name: Nest Authentication
  slug: nest-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nest Domain Security
  slug: nest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Control a Nest thermostat
  slug: nest-control-thermostat
- name: List and read Nest devices
  slug: nest-list-devices
slug: nest
tags:
- Company
- Hardware
- Smart Home
- IoT
- Home Automation
- Thermostat
- Google
- Device Access
website: https://nest.com
---
