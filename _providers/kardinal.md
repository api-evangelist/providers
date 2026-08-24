---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.4
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 26
  human_in_the_loop: 4
  name: Kardinal Agentic Access
  operation_count: 40
  slug: kardinal-agentic-access
  summary_line: 40 operations · 26 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: The Kardinal Always-on Route Optimization (ARO) v2 REST API. Create and update optimization plans, manage the resources (vehicles) and orders (stops) inside them, drive the optimization lifecycle, and
  name: Kardinal ARO API
  slug: aro
artifact_total: 7
common:
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
overview: 'Kardinal publishes 1 API on the [APIs.io](https://apis.io/) network: ARO API. Tagged areas include Company, Software-as-a-Service, Route Optimization, Vehicle Routing, and Last Mile Delivery.


  Kardinal''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, FAQ, and 24 more developer resources.'
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
  composite: 47.7
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 16.7
    contract_quality: 51.8
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 47.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
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
