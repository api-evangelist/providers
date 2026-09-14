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
api_count: 1
apis:
- description: 'Google Nest Device Access REST API for accessing, controlling, and managing authorized Nest devices (thermostats, cameras, doorbells, Hub Max) via enterprises/structures/rooms/devices resources and a '
  name: Smart Device Management (SDM) API
  slug: smart-device-management-sdm-api
artifact_total: 5
asyncapis:
- description: ''
  name: Nest Events
  slug: nest-events
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/google/
- group: auth
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
  title: ''
  type: Authentication
  url: authentication/nest-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nest-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nest-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nest-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nest-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nest-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nest-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nest-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/nest-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/nest-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nest-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/nest-events.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nest-llms.txt
created: '2026-07-17'
description: Nest is Google's smart home brand — thermostats, cameras, doorbells, and the Nest Hub — originally founded as Nest Labs (a Lightspeed Venture Partners portfolio company) and acquired by Google. Developers integrate with authorized Nest devices through the Google Nest Device Access program and its Smart Device Management (SDM) API, a Google Cloud REST API authorized with Google OAuth 2.0. The API lets partner apps list structures, rooms, and devices, read device traits (temperature, humidity, camera, doorbell), and execute trait commands, with asynchronous device events delivered via Google Cloud Pub/Sub. The legacy "Works with Nest" API was retired and superseded by Device Access.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nest.png
layout: provider
modified: '2026-07-20'
name: Nest
nav: Providers
network: true
overview: 'Nest publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Smart Home, IoT, and Home Automation.


  The Nest catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Nest''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, pricing, authentication, and 20 more developer resources.'
random_paper: 1
scopes:
- name: Nest Scopes
  scope_count: 1
  slug: nest-scopes
  summary_line: 1 scope · authorizationCode
screenshot: https://raw.githubusercontent.com/api-evangelist/nest/refs/heads/main/screenshots/nest-2026-08-07T184913.png
security:
- kind: authentication
  name: Nest Authentication
  slug: nest-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Nest Domain Security
  slug: nest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
