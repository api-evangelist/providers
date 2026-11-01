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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.vehicles.dev
  baseurl_source: declared
  description: The Control API from Vehicles.dev — 23 operation(s) for control.
  name: Vehicles.dev Control API
  slug: vehicles-dev-api-control-api
- baseURL: https://api.vehicles.dev
  baseurl_source: declared
  description: The Employment API from Vehicles.dev — 2 operation(s) for employment.
  name: Vehicles.dev Employment API
  slug: vehicles-dev-api-employment-api
- baseURL: https://api.vehicles.dev
  baseurl_source: declared
  description: The operations API from Vehicles.dev — 3 operation(s) for operations.
  name: Vehicles.dev Operations API
  slug: vehicles-dev-api-operations-api
- baseURL: https://api.vehicles.dev
  baseurl_source: declared
  description: The Operator API from Vehicles.dev — 11 operation(s) for operator.
  name: Vehicles.dev Operator API
  slug: vehicles-dev-api-operator-api
- baseURL: https://api.vehicles.dev
  baseurl_source: declared
  description: The Vehicles API from Vehicles.dev — 14 operation(s) for vehicles.
  name: Vehicles.dev Vehicles API
  slug: vehicles-dev-api-vehicles-api
- baseURL: https://api.vehicles.dev
  baseurl_source: declared
  description: The Webhooks API from Vehicles.dev — 1 operation(s) for webhooks.
  name: Vehicles.dev Webhooks API
  slug: vehicles-dev-api-webhooks-api
artifact_total: 17
common:
- group: other
  href: https://artifacts.apis.io/vehicles-dev-api/capabilities/vehicles-dev-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/vehicles-dev-api-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/vehicles-dev-api/overlays/vehicles-dev-api-admin-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vehicles-dev-api-admin-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/vehicles-dev-api/overlays/vehicles-dev-api-billing-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vehicles-dev-api-billing-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/vehicles-dev-api/overlays/vehicles-dev-api-data-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vehicles-dev-api-data-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/vehicles-dev-api/overlays/vehicles-dev-api-reports-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vehicles-dev-api-reports-api-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/vehicles-dev-api/security/vehicles-dev-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vehicles-dev-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/vehicles-dev-api/authentication/vehicles-dev-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vehicles-dev-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vehicles.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://vehicles.dev/dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://vehicles.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://vehicles.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://vehicles.dev/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://vehicles.dev/docs#support
- group: commercial
  title: ''
  type: Pricing
  url: https://vehicles.dev/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://vehicles.dev/auth/sign-up
- group: start
  title: ''
  type: Login
  url: https://vehicles.dev/auth/sign-in
- group: commercial
  title: ''
  type: UsageTerms
  url: https://vehicles.dev/docs#support-terms
- group: commercial
  href: https://artifacts.apis.io/vehicles-dev-api/plans/vehicles-dev-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vehicles-dev-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/vehicles-dev-api/rate-limits/vehicles-dev-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vehicles-dev-api-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/vehicles-dev-api/conventions/vehicles-dev-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vehicles-dev-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/vehicles-dev-api/conventions/vehicles-dev-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/vehicles-dev-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/vehicles-dev-api/errors/vehicles-dev-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vehicles-dev-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vehicles-dev-api/lifecycle/vehicles-dev-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vehicles-dev-api-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/vehicles-dev-api/conformance/vehicles-dev-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vehicles-dev-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/vehicles-dev-api/data-model/vehicles-dev-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vehicles-dev-api-data-model.yml
- group: build
  href: https://artifacts.apis.io/vehicles-dev-api/packages/vehicles-dev-api-packages.yml
  title: ''
  type: Packages
  url: packages/vehicles-dev-api-packages.yml
- group: agent
  href: https://artifacts.apis.io/vehicles-dev-api/mcp/vehicles-dev-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vehicles-dev-api-mcp.yml
- group: build
  href: https://artifacts.apis.io/vehicles-dev-api/mcp/vehicles-dev-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/vehicles-dev-api-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/vehicles-dev-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/vehicles-dev-api/llms/vehicles-dev-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vehicles-dev-api-llms.txt
created: '2026-08-15'
description: Automotive vehicle data platform offering a live REST API for VIN decoding, specifications, recalls, market valuation, depreciation, ownership costs, listings, price history, and photos, backed by federal sources (NHTSA vPIC, NHTSA recalls, EPA) and a continuously crawled US dealer-listings store. Ships an OpenAPI 3.1 contract and a local MCP server exposing all ten endpoints as read-only tools.
finops:
- has_sources: true
  method: derived
  name: Vehicles Dev Api Finops
  primary_unit: platform tier
  service_category: ''
  slug: vehicles-dev-api-finops
  template: false
layout: provider
mcp_servers:
- description: Local (stdio) MCP server requiring an API key; 10 tools listed.
  name: Vehicles.dev MCP Server
  slug: vehicles-dev
modified: '2026-08-16'
name: Vehicles.dev
nav: Providers
network: true
overview: 'Vehicles.dev publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Control API, Employment API, Operations API, and 3 more. Tagged areas include Automotive, Vehicle Data, VIN Decoding, Vehicle Valuation, and Market Value.


  Vehicles.dev''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Vehicles Dev Api Plans Pricing
  plan_count: 3
  slug: vehicles-dev-api-plans-pricing
- name: Vehicles Dev Api Price Estimates
  plan_count: 0
  slug: vehicles-dev-api-price-estimates
random_paper: 14
rate_limits:
- limit_count: 3
  name: Vehicles Dev Api Rate Limits
  slug: vehicles-dev-api-rate-limits
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.0
    catalog_earned_first_party: 24.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 63.2
    contract_governance: 4.5
    contract_quality: 44.3
    developer_ergonomics: 56.5
    discoverability: 61.7
    operational_transparency: 31.6
  previous_composite: 44.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/vehicles-dev-api/vehicles-dev-api-2026-08-17T082722.png
security:
- kind: authentication
  name: Vehicles Dev Api Authentication
  slug: vehicles-dev-api-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Vehicles Dev Api Domain Security
  slug: vehicles-dev-api-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: Check safety recalls and running costs
  slug: vehicles-dev-api-check-safety-and-running-costs
- name: Identify and value a VIN
  slug: vehicles-dev-api-identify-and-value-a-vin
- name: Order a vehicle history report
  slug: vehicles-dev-api-order-a-vehicle-history-report
- name: Search dealer listings and read price history
  slug: vehicles-dev-api-search-listings-and-price-history
slug: vehicles-dev-api
tags:
- Automotive
- Vehicle Data
- VIN Decoding
- Vehicle Valuation
- Market Value
- Vehicle Listings
- Recalls
- NHTSA
- vPIC
- Vehicle Specifications
- Depreciation
- Ownership Costs
- Job
- Labor Market Data
- REST
- OpenAPI
- Vehicle Safety
- Car Listings
- Marketplace
- Pricing
- Cost of Ownership
- Vehicle Images
- MCP
- Agent Tools
- Machine Learning
website: https://vehicles.dev/
---
