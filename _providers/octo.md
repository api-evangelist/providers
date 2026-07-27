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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Octo Agentic Access
  operation_count: 12
  slug: octo-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 4
apis:
- description: The Availability API from Open Connectivity for Tours, Activities, and Attractions — 2 operation(s) for availability.
  name: Open Connectivity for Tours, Activities, and Attractions Availability API
  slug: octo-availability-api
- description: The Bookings API from Open Connectivity for Tours, Activities, and Attractions — 5 operation(s) for bookings.
  name: Open Connectivity for Tours, Activities, and Attractions Bookings API
  slug: octo-bookings-api
- description: The Products API from Open Connectivity for Tours, Activities, and Attractions — 2 operation(s) for products.
  name: Open Connectivity for Tours, Activities, and Attractions Products API
  slug: octo-products-api
- description: The Supplier API from Open Connectivity for Tours, Activities, and Attractions — 1 operation(s) for supplier.
  name: Open Connectivity for Tours, Activities, and Attractions Supplier API
  slug: octo-supplier-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/octo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/octo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OctoConsulting
- group: docs
  title: ''
  type: Documentation
  url: https://docs.octo.travel/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.octo.travel/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.octo.travel/getting-started/authentication
- group: operate
  title: ''
  type: Support
  url: https://docs.octo.travel/getting-started/development-support
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.octo.travel/llms.txt
created: '2024-06-07'
description: OCTO (Open Connectivity for Tours, Activities, and Attractions) is an open standard API specification for the in-destination experiences sector of the travel industry. The standard defines agreed-upon schemas, endpoints, and capabilities commonly needed when connecting platforms, resellers, OTAs, and other technologies in tours, activities, and attractions. OCTO is open source.
finops:
- name: Octo Finops
  service_category: API
  slug: octo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octo.png
layout: provider
modified: '2026-05-19'
name: Open Connectivity for Tours, Activities, and Attractions
nav: Providers
network: true
overview: 'Open Connectivity for Tours, Activities, and Attractions publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Products API, and 1 more. Tagged areas include Activities, Attractions, Open Standard, Tours, and Travel.


  Open Connectivity for Tours, Activities, and Attractions'' developer surface includes authentication, documentation, getting-started guide, support, and 5 more developer resources.'
plans:
- name: Octo Plans Pricing
  plan_count: 3
  slug: octo-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 5
  name: Octo Rate Limits
  slug: octo-rate-limits
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 51.3
    developer_ergonomics: 34.8
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/octo/refs/heads/main/screenshots/octo-2026-06-20T190610.png
security:
- kind: authentication
  name: Octo Authentication
  slug: octo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Octo Domain Security
  slug: octo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: octo
tags:
- Activities
- Attractions
- Open Standard
- Tours
- Travel
---
