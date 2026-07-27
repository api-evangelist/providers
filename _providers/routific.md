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
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 55.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Routific Agentic Access
  operation_count: 6
  slug: routific-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 4
apis:
- description: Insert new visits into an existing optimized solution.
  name: Routific Fix API
  slug: routific-fix-api
- description: Asynchronous long-running optimization jobs.
  name: Routific Jobs API
  slug: routific-jobs-api
- description: Pickup and Delivery Problem — paired pickup/dropoff routing.
  name: Routific PDP API
  slug: routific-pdp-api
- description: Vehicle Routing Problem — assign and order visits across a fleet.
  name: Routific VRP API
  slug: routific-vrp-api
artifact_total: 22
collections:
- collection_type: open
  name: Routific Route Optimization API
  slug: open-routific-route-optimization-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/routific-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/routific-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/routific-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/routific
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/routific
- group: build
  title: ''
  type: GitHub
  url: https://github.com/routific
- group: start
  title: ''
  type: Portal
  url: https://routific.com
- group: other
  title: ''
  type: Developer
  url: https://dev.routific.com
- group: start
  title: ''
  type: Signup
  url: https://dev.routific.com/signup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.routific.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.routific.com/reference/getting-started
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.routific.com/reference/error-codes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.routific.com
- group: operate
  title: ''
  type: Support
  url: https://help.routific.com
- group: company
  title: ''
  type: Blog
  url: https://routific.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://routific.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://academy.routific.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@routific.com
- group: commercial
  title: ''
  type: Plans
  url: plans/routific-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/routific-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/routific-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/routific-vocabulary.yml
created: '2026-05-25'
description: Routific is a Vancouver-based delivery management and route optimization software provider. Its platform combines smart route optimization, dispatch and live tracking, a driver mobile app, customer delivery notifications with real-time tracking, and proof of delivery. The standalone Route Optimization API exposes the same engine — solving Vehicle Routing Problems (VRP) and Pickup-and-Delivery Problems (PDP) — to SaaS integrators and channel partners. Routific has optimized over 191 million deliveries for more than 1,000 businesses since founding.
examples:
- key_count: 2
  name: Routific Fix Vrp Example
  slug: routific-fix-vrp-example
- key_count: 2
  name: Routific Solve Vrp Example
  slug: routific-solve-vrp-example
- key_count: 2
  name: Routific Solve Vrp Long Example
  slug: routific-solve-vrp-long-example
finops:
- name: Routific Finops
  service_category: ''
  slug: routific-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/routific.png
json_schemas:
- name: Routific Optimization Job
  property_count: 5
  slug: routific-job
- name: Routific Solution
  property_count: 12
  slug: routific-solution
- name: Routific Vehicle
  property_count: 7
  slug: routific-vehicle
- name: Routific Visit
  property_count: 7
  slug: routific-visit
json_structures:
- name: Routific Vrp Structure
  property_count: 3
  slug: routific-vrp-structure
jsonld:
- class_count: 53
  name: Routific Context
  property_count: 0
  slug: routific-context
layout: provider
modified: '2026-05-25'
name: Routific
nav: Providers
network: true
overview: 'Routific publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Fix API, Jobs API, PDP API, and 1 more. Tagged areas include RouteOptimization, VRP, PickupAndDelivery, Logistics, and LastMileDelivery.


  The Routific catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Routific''s developer surface includes authentication, GitHub presence, developer portal, signup flow, documentation, support, engineering blog, and 15 more developer resources.'
plans:
- name: Routific Plans Pricing
  plan_count: 4
  slug: routific-plans-pricing
random_paper: 53
rate_limits:
- limit_count: 0
  name: Routific Rate Limits
  slug: routific-rate-limits
rules:
- name: Routific API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: routific-jsonschema-spectral-rules
- name: Routific API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: routific-rules
score:
  band: strong
  composite: 60.0
  delta: 5.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 79.6
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 54.6
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/routific/refs/heads/main/screenshots/routific-2026-06-20T193228.png
security:
- kind: authentication
  name: Routific Authentication
  slug: routific-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Routific Domain Security
  slug: routific-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: routific
tags:
- RouteOptimization
- VRP
- PickupAndDelivery
- Logistics
- LastMileDelivery
- Delivery
- FleetManagement
- Dispatch
- DeliveryManagement
website: https://routific.com
---
