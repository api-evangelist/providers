---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Particle Io Agentic Access
  operation_count: 32
  slug: particle-io-agentic-access
  summary_line: 32 operations · 18 acting · 1 human-in-the-loop
api_count: 17
apis:
- description: The Particle Device Cloud REST API is the primary interface to the Particle platform. Use it to claim and manage devices, list and call cloud functions, read cloud variables, subscribe to events, mana
  name: Particle Device Cloud API
  slug: particle-device-cloud-api
- description: OAuth 2.0 endpoints for creating, listing, and deleting access tokens used to authenticate against the Particle Device Cloud API.
  name: Particle OAuth 2.0 API
  slug: particle-oauth-api
- description: List, claim, rename, and inspect Particle devices, request remote diagnostics and vitals, and control device signal LEDs.
  name: Particle Devices API
  slug: particle-devices-api
- description: Invoke cloud-callable firmware functions and read cloud-exposed variables on Particle devices.
  name: Particle Functions and Variables API
  slug: particle-functions-variables-api
- description: Publish events from the cloud to devices and subscribe to a Server-Sent Events stream of device, product, or public events.
  name: Particle Events API
  slug: particle-events-api
- description: Create and manage webhooks and integrations that forward device events to external services such as Azure IoT Hub, Google Cloud Pub/Sub, and arbitrary HTTP endpoints.
  name: Particle Webhooks and Integrations API
  slug: particle-webhooks-api
- description: Manage product fleets including importing and listing devices, configuring OAuth clients, and orchestrating OTA firmware releases across product devices.
  name: Particle Products API
  slug: particle-products-api
- description: List, activate, deactivate, and inspect Particle cellular SIM cards including data usage and network status.
  name: Particle SIM Cards API
  slug: particle-sims-api
- description: The Access Tokens API from Particle — 3 operation(s) for access tokens.
  name: Particle Access Tokens API
  slug: particle-io-access-tokens-api
- description: The Clients API from Particle — 2 operation(s) for clients.
  name: Particle Clients API
  slug: particle-io-clients-api
- description: The Devices API from Particle — 5 operation(s) for devices.
  name: Particle Devices API
  slug: particle-io-devices-api
- description: The Diagnostics API from Particle — 3 operation(s) for diagnostics.
  name: Particle Diagnostics API
  slug: particle-io-diagnostics-api
- description: The Oauth API from Particle — 1 operation(s) for oauth.
  name: Particle Oauth API
  slug: particle-io-oauth-api
- description: The Products API from Particle — 2 operation(s) for products.
  name: Particle Products API
  slug: particle-io-products-api
- description: The Serial Numbers API from Particle — 1 operation(s) for serial numbers.
  name: Particle Serial Numbers API
  slug: particle-io-serial-numbers-api
- description: The Sims API from Particle — 3 operation(s) for sims.
  name: Particle Sims API
  slug: particle-io-sims-api
- description: The User API from Particle — 2 operation(s) for user.
  name: Particle User API
  slug: particle-io-user-api
artifact_total: 25
collections:
- collection_type: open
  name: Particle Cloud API
  slug: open-particle-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/particle-io-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/particle-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/particle-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/particle-io-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.particle.io/
- group: other
  title: ''
  type: Developer
  url: https://docs.particle.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.particle.io/reference/cloud-apis/api/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/particle-iot/particle-api-js
- group: build
  title: ''
  type: CLI
  url: https://docs.particle.io/reference/developer-tools/cli/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/particle-iot
- group: company
  title: ''
  type: Blog
  url: https://blog.particle.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.particle.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.particle.io/
- group: operate
  title: ''
  type: Support
  url: https://support.particle.io/
- group: operate
  title: ''
  type: Community
  url: https://community.particle.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.particle.io/legal/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.particle.io/legal/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/particle-
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.particle.io/reference/changelog/
created: '2026-05-23'
description: Particle is an end-to-end IoT platform combining cellular and Wi-Fi connectivity, hardware modules (Photon, Boron, Tracker, B-SoM, M-SoM), firmware, and a Device Cloud. The Particle Device Cloud exposes a REST API for fleet management, device control, cloud functions and variables, webhooks and integrations, OTA firmware updates, SIM management, and customer and product administration.
finops:
- name: Particle Io Finops
  service_category: API
  slug: particle-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/particle-io.png
layout: provider
modified: '2026-05-23'
name: Particle
nav: Providers
network: true
overview: 'Particle publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Access Tokens API, Clients API, Devices API, and 6 more. Tagged areas include Cellular, Cloud Functions, Connectivity, Device Management, and Edge.


  Particle''s developer surface includes authentication, documentation, CLI, GitHub presence, engineering blog, pricing, support, and 12 more developer resources.'
plans:
- name: Particle Io Plans Pricing
  plan_count: 1
  slug: particle-io-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 2
  name: Particle Io Rate Limits
  slug: particle-io-rate-limits
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 54.6
    developer_ergonomics: 39.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 57.9
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/particle-io/refs/heads/main/screenshots/particle-io-2026-06-20T191427.png
security:
- kind: authentication
  name: Particle Io Authentication
  slug: particle-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Particle Io Domain Security
  slug: particle-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Particle Io Vulnerability Disclosure
  slug: particle-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: particle-io
tags:
- Cellular
- Cloud Functions
- Connectivity
- Device Management
- Edge
- Firmware
- Fleet Management
- IoT
- OTA
- Webhooks
- Wi-Fi
website: https://www.particle.io/
---
