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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Routific Agentic Access
  operation_count: 6
  slug: routific-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.routific.com
  baseurl_source: declared
  description: Insert new visits into an existing optimized solution.
  name: Routific Fix API
  slug: routific-fix-api
- baseURL: https://api.routific.com
  baseurl_source: declared
  description: Asynchronous long-running optimization jobs.
  name: Routific Jobs API
  slug: routific-jobs-api
- baseURL: https://api.routific.com
  baseurl_source: declared
  description: Pickup and Delivery Problem — paired pickup/dropoff routing.
  name: Routific PDP API
  slug: routific-pdp-api
- baseURL: https://api.routific.com
  baseurl_source: declared
  description: Vehicle Routing Problem — assign and order visits across a fleet.
  name: Routific VRP API
  slug: routific-vrp-api
artifact_total: 31
collections:
- collection_type: postman
  name: Routific Route Optimization Fix API
  slug: postman-routific-fix-api
- collection_type: postman
  name: Routific Route Optimization Fix Jobs API
  slug: postman-routific-jobs-api
- collection_type: postman
  name: Routific Route Optimization Fix PDP API
  slug: postman-routific-pdp-api
- collection_type: postman
  name: Routific Route Optimization Fix VRP API
  slug: postman-routific-vrp-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Routific Route Optimization Fix API
  slug: open-routific-fix-api
- collection_type: open
  name: Routific Route Optimization Fix Jobs API
  slug: open-routific-jobs-api
- collection_type: open
  name: Routific Route Optimization Fix PDP API
  slug: open-routific-pdp-api
- collection_type: open
  name: Routific Route Optimization API
  slug: open-routific-route-optimization-api
- collection_type: open
  name: Routific Route Optimization Fix VRP API
  slug: open-routific-vrp-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/routific-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/routific/overview
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
overview: 'Routific publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Fix API, Jobs API, PDP API, and 1 more. Tagged areas include Route Optimization, VRP, Pickup and Delivery, Logistics, and Last Mile Delivery.


  The Routific catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Routific''s developer surface includes authentication, GitHub presence, developer portal, signup flow, documentation, support, engineering blog, and 17 more developer resources.'
plans:
- name: Routific Plans Pricing
  plan_count: 4
  slug: routific-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Routific Rate Limits
  slug: routific-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Routific API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: routific-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: Routific API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 3
  slug: routific-rules
score:
  band: strong
  composite: 55.4
  coverage:
    artifact_dirs: 19
    catalog_gap: 27.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 28.8
    contract_quality: 74.3
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 42.1
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
- Route Optimization
- VRP
- Pickup and Delivery
- Logistics
- Last Mile Delivery
- Delivery
- Fleet Management
- Dispatch
- Delivery Management
website: https://routific.com
---
