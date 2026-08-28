---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-26'
api_count: 11
apis:
- description: Endpoints to operate on [Depots](/docs/models/depot) resources. This resource is currently read-only on the API.
  name: Circuit Depots API
  slug: circuit-depots-api
- description: Endpoints to operate on [Drivers](/docs/models/driver) resources.
  name: Circuit Drivers API
  slug: circuit-drivers-api
- description: Endpoints to operate on [Plans](/docs/models/plan) resources when it's pending re-optimization and re-distribution. You must use these endpoints to apply the changes when any [Live Stops](#tag/Live-St
  name: Circuit Live Plans API
  slug: circuit-live-plans-api
- description: Endpoints to operate on [Stop](/docs/models/stop) resources when the plan is already optimized and therefore not writable. All the endpoints return the field `pending`. This field indicates whether th
  name: Circuit Live Stops API
  slug: circuit-live-stops-api
- description: Endpoints to operate on Members resources.
  name: Circuit Members API
  slug: circuit-members-api
- description: Endpoints to operate on [Operations](/docs/models/operation) resources.
  name: Circuit Operations API
  slug: circuit-operations-api
- description: Endpoints to operate on [Plans](/docs/models/plan) resources.
  name: Circuit Plans API
  slug: circuit-plans-api
- description: Endpoints to operate on [Routes](/docs/models/route) resources. This resource is currently read-only on the API.
  name: Circuit Routes API
  slug: circuit-routes-api
- description: Endpoints to operate on [Stop](/docs/models/stop) resources. For any [Plans](/docs/models/plan) created before 2023-04-01 the stop collections and all related operations will not be available. For any
  name: Circuit Stops API
  slug: circuit-stops-api
- description: Endpoints to retrieve [Custom Stop Properties](/docs/models/customStopProperty).
  name: Circuit Team API
  slug: circuit-team-api
- description: Endpoints to operate on [Unassigned Stop](/docs/models/unassignedStop) resources.
  name: Circuit Unassigned Stops API
  slug: circuit-unassigned-stops-api
artifact_total: 28
asyncapis:
- description: ''
  name: Circuit Webhooks
  slug: circuit-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spoke Depots API
  slug: open-circuit-depots-api
- collection_type: open
  name: Spoke Depots Drivers API
  slug: open-circuit-drivers-api
- collection_type: open
  name: Spoke Depots Live Plans API
  slug: open-circuit-live-plans-api
- collection_type: open
  name: Spoke Depots Live Stops API
  slug: open-circuit-live-stops-api
- collection_type: open
  name: Spoke Depots Members API
  slug: open-circuit-members-api
- collection_type: open
  name: Spoke Depots Operations API
  slug: open-circuit-operations-api
- collection_type: open
  name: Spoke Depots Plans API
  slug: open-circuit-plans-api
- collection_type: open
  name: Spoke Depots Routes API
  slug: open-circuit-routes-api
- collection_type: open
  name: Spoke Depots Stops API
  slug: open-circuit-stops-api
- collection_type: open
  name: Spoke Depots Team API
  slug: open-circuit-team-api
- collection_type: open
  name: Spoke Depots Unassigned Stops API
  slug: open-circuit-unassigned-stops-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/circuit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/circuit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://spoke.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.dispatch.spoke.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.dispatch.spoke.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dispatch.spoke.com/api/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.dispatch.spoke.com/docs/v1/api-examples
- group: build
  title: ''
  type: Examples
  url: https://developer.dispatch.spoke.com/docs/v1/api-examples
- group: operate
  title: ''
  type: Support
  url: https://help.spoke.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://help.spoke.com/en/collections/385323-spoke-help-products-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spoke.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spoke.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.spoke.com/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/circuit-lifecycle.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/circuit-v1-openapi-original.json
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/circuit-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/circuit-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/circuit-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/circuit-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/circuit-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/circuit-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/circuit-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/circuit-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/circuit-conformance.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/circuit-changelog.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/circuit-v1-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spoke-delivery/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/SpokeDelivery
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Spokeapp
created: '2026-07-17'
description: Circuit (operating publicly as Spoke; legal entity Circuit Routing Limited) builds last-mile delivery route-optimization software. Its products are Route Planner, a free driver app for uploading stops, optimizing multi-stop routes and navigating; Dispatch, a multi-driver delivery-management platform with route planning, live tracking and proof of delivery for courier operations; and Connect, a marketplace that lets retailers discover local couriers and track deliveries. The Spoke Public API (formerly the Circuit for Teams API) is an HTTP/JSON API that lets teams manage plans, stops, unassigned stops, drivers, depots, routes, members and long-running operations programmatically, optimize and distribute plans across drivers, run full-text stop search with a filtering DSL, and subscribe to webhook events for delivery workflows.
image: https://spoke.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Circuit MCP Server
  slug: circuit-mcp-server
modified: '2026-07-18'
name: Circuit
nav: Providers
network: true
overview: 'Circuit publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Depots API, Drivers API, Live Plans API, and 8 more. Tagged areas include Company, Delivery, Logistics, Last Mile, and Route Optimization.


  The Circuit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Circuit''s developer surface includes authentication, documentation, API reference, getting-started guide, code examples, support, pricing, and 23 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 6
  name: Circuit Rate Limits
  slug: circuit-rate-limits
score:
  band: developing
  composite: 53.1
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 68.5
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 78.9
  previous_composite: 53.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/circuit/refs/heads/main/screenshots/circuit-2026-07-25T205411.png
security:
- kind: authentication
  name: Circuit Authentication
  slug: circuit-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Circuit Domain Security
  slug: circuit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: circuit
tags:
- Company
- Delivery
- Logistics
- Last Mile
- Route Optimization
- Dispatch
- Couriers
- Fleet
- Proof of Delivery
- Field Service
website: https://spoke.com/
---
