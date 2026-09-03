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
  band: agent-native
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
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.8
  scored_at: '2026-09-02'
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
artifact_total: 11
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vehicles-dev-api-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vehicles-dev-api-admin-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/vehicles-dev-api-billing-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/vehicles-dev-api-data-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/vehicles-dev-api-reports-api-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vehicles-dev-api-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/vehicles-dev-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vehicles-dev-api-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vehicles-dev-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/vehicles-dev-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vehicles-dev-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vehicles-dev-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vehicles-dev-api-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vehicles-dev-api-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/vehicles-dev-api-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vehicles-dev-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/vehicles-dev-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vehicles-dev-api-llms.txt
created: '2026-08-15'
description: Automotive vehicle data platform offering a live REST API for VIN decoding, specifications, recalls, market valuation, depreciation, ownership costs, listings, price history, and photos, backed by federal sources (NHTSA vPIC, NHTSA recalls, EPA) and a continuously crawled US dealer-listings store. Ships an OpenAPI 3.1 contract and a local MCP server exposing all ten endpoints as read-only tools.
layout: provider
mcp_servers:
- description: ''
  name: Vehicles.dev MCP Server
  slug: vehiclesdev-mcp-server
modified: '2026-08-16'
name: Vehicles.dev
nav: Providers
network: true
overview: 'Vehicles.dev publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Control API, Employment API, Operations API, and 3 more. Tagged areas include Automotive, Vehicle Data, VIN Decoding, Vehicle Valuation, and Market Value.


  Vehicles.dev''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Vehicles Dev Api Plans Pricing
  plan_count: 3
  slug: vehicles-dev-api-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Vehicles Dev Api Rate Limits
  slug: vehicles-dev-api-rate-limits
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 18
    catalog_gap: 56.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 46.0
    developer_ergonomics: 56.5
    discoverability: 64.8
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 43.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vehicles-dev-api/refs/heads/main/screenshots/vehicles-dev-api-2026-08-17T082722.png
security:
- kind: authentication
  name: Vehicles Dev Api Authentication
  slug: vehicles-dev-api-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Vehicles Dev Api Domain Security
  slug: vehicles-dev-api-domain-security
  summary_line: TLSv1.3
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
- Machine-Learning
website: https://vehicles.dev/
---
