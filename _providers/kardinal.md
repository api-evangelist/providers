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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 26
  human_in_the_loop: 4
  name: Kardinal Agentic Access
  operation_count: 40
  slug: kardinal-agentic-access
  summary_line: 40 operations · 26 acting · 4 human-in-the-loop
api_count: 1
apis:
- baseURL: https://app.kardinal.ai/api/v2
  baseurl_source: declared
  description: How to authenticate, and manage the access and refresh tokens.
  name: Kardinal Authenticate API
  slug: kardinal-authenticate-api
- baseURL: https://app.kardinal.ai/api/v2
  baseurl_source: declared
  description: The Core API from Kardinal — 4 operation(s) for core.
  name: Kardinal Core API
  slug: kardinal-core-api
- baseURL: https://app.kardinal.ai/api/v2
  baseurl_source: declared
  description: The Management API from Kardinal — 5 operation(s) for management.
  name: Kardinal Management API
  slug: kardinal-management-api
- baseURL: https://app.kardinal.ai/api/v2
  baseurl_source: declared
  description: How to create, retrieve, update and delete orders in a plan.
  name: Kardinal Order API
  slug: kardinal-order-api
- baseURL: https://app.kardinal.ai/api/v2
  baseurl_source: declared
  description: How to create, retrieve, update and delete plans.
  name: Kardinal Plan API
  slug: kardinal-plan-api
- baseURL: https://app.kardinal.ai/api/v2
  baseurl_source: declared
  description: How to create, retrieve, update and delete resources in a plan.
  name: Kardinal Resource API
  slug: kardinal-resource-api
- baseURL: https://app.kardinal.ai/api/v2
  baseurl_source: declared
  description: How to create a plan through the use of a simple plan.
  name: Kardinal Simple Plan API
  slug: kardinal-simpleplan-api
- baseURL: https://app.kardinal.ai/api/v2
  baseurl_source: declared
  description: The Solution API from Kardinal — 2 operation(s) for solution.
  name: Kardinal Solution API
  slug: kardinal-solution-api
artifact_total: 14
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/kardinal-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://kardinal.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.kardinal.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.kardinal.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.kardinal.ai/api-reference/authenticate/request-a-password-token
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.kardinal.ai/getting-started/first-api-call
- group: operate
  title: ''
  type: Support
  url: https://kardinal.ai/contact/
- group: company
  title: ''
  type: Blog
  url: https://kardinal.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://kardinal.ai/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/KardinalAI
- group: commercial
  title: ''
  type: Pricing
  url: https://kardinal.ai/route-optimization-api/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kardinal.ai/terms-of-service-laskar/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kardinal.ai/privacy-policy/
- group: commercial
  title: ''
  type: LegalNotice
  url: https://kardinal.ai/legal-notice/
- group: operate
  title: ''
  type: FAQ
  url: https://kardinal.ai/fr/faq-route-optimization/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kardinal-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/kardinal-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/kardinal-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kardinal-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/kardinal-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kardinal-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kardinal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kardinal-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kardinal-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kardinal-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kardinal-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kardinal-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kardinal-plans-pricing.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/kardinal-aro-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kardinal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kardinal-domain-security.yml
created: '2026-08-17'
description: Kardinal is a Paris-based logistics optimization company whose Always-on Route Optimization (ARO) API solves vehicle routing problems for last-mile delivery, post and parcel, waste and bulk transport, fresh delivery, field services and retail operators. Integrators submit a plan — resources (vehicles), orders (stops) and constraints such as capacities, time windows, driver skills and breaks — with a single idempotent PUT, and the engine optimizes it continuously rather than in a nightly batch, so new orders, cancellations, traffic and field updates are absorbed into the running solution instead of forcing a rerun. The REST API is documented with a published OpenAPI 3.0.3 definition covering 40 operations across authentication, plans, resources, orders and solutions, and is reachable per customer environment at https://<env>.kardinal.ai/api/v2 using short-lived JWT bearer tokens.
image: https://kardinal.ai/wp-content/uploads/2020/01/cropped-Icon-blue-270x270.png
layout: provider
mcp_servers:
- description: ''
  name: Kardinal MCP Server
  slug: kardinal-mcp-server
modified: '2026-08-17'
name: Kardinal
nav: Providers
network: true
overview: 'Kardinal publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Authenticate API, Core API, Management API, and 5 more. Tagged areas include Company, Software-as-a-Service, Route Optimization, Vehicle Routing, and Last Mile Delivery.


  Kardinal''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, FAQ, and 25 more developer resources.'
plans:
- name: Kardinal Plans Pricing
  plan_count: 2
  slug: kardinal-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Kardinal Rate Limits
  slug: kardinal-rate-limits
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 4.5
    contract_quality: 50.4
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 45.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kardinal/refs/heads/main/screenshots/kardinal-2026-09-02T150130.png
security:
- kind: authentication
  name: Kardinal Authentication
  slug: kardinal-authentication
  summary_line: http · 5 schemes
- kind: domain-security
  name: Kardinal Domain Security
  slug: kardinal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kardinal
tags:
- Company
- Software-as-a-Service
- Route Optimization
- Vehicle Routing
- Last Mile Delivery
- Logistics
- Supply Chain
- Transportation
- Fleet Management
- Optimization
website: https://kardinal.ai/
---
