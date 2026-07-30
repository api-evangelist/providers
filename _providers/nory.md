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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-07-28'
api_count: 10
apis:
- description: The Authorization API from Nory — 1 operation(s) for authorization.
  name: Nory Authorization API
  slug: nory-authorization-api
- description: The Branch API from Nory — 1 operation(s) for branch.
  name: Nory Branch API
  slug: nory-branch-api
- description: The Brands API from Nory — 1 operation(s) for brands.
  name: Nory Brands API
  slug: nory-brands-api
- description: The Employee Punch API from Nory — 2 operation(s) for employee punch.
  name: Nory Employee Punch API
  slug: nory-employee-punch-api
- description: The Integration API from Nory — 1 operation(s) for integration.
  name: Nory Integration API
  slug: nory-integration-api
- description: The Inventory API from Nory — 4 operation(s) for inventory.
  name: Nory Inventory API
  slug: nory-inventory-api
- description: The Inventory Orders API from Nory — 2 operation(s) for inventory orders.
  name: Nory Inventory Orders API
  slug: nory-inventory-orders-api
- description: The Location Settings API from Nory — 1 operation(s) for location settings.
  name: Nory Location Settings API
  slug: nory-location-settings-api
- description: The Refresh token API from Nory — 1 operation(s) for refresh token.
  name: Nory Refresh token API
  slug: nory-refresh-token-api
- description: The Templates API from Nory — 5 operation(s) for templates.
  name: Nory Templates API
  slug: nory-templates-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://nory.ai/
- group: start
  title: ''
  type: Login
  url: https://app.nory.ai/
- group: company
  title: ''
  type: Blog
  url: https://nory.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://nory.ai/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nory.ai/legal/terms-privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nory.ai/legal/terms-and-conditions
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/nory-middleware-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/nory-middleware-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nory-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nory-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nory-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nory-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nory-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nory-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nory-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nory-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nory-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nory-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nory-llms.txt
created: '2026-07-17'
description: Nory is an AI-powered restaurant management platform (an "agentic AI restaurant operating system") founded in Ireland in 2019 by Conor Sheridan. It unifies business intelligence, inventory, workforce scheduling and payroll into one control centre, using real-time data and predictive AI (demand-based ordering, live P&L, labour forecasting) to cut food waste and labour cost across single-site and multi-location restaurant groups. Nory connects to POS and hospitality systems such as Toast, Lightspeed, Square, SumUp, Vita Mojo, Clover, Zonal, Revel, Oracle Micros and Shift4, and exposes a partner-facing Middleware API (published as a Swagger 2.0 sandbox definition) covering brands, branches, inventory counts/deliveries/suppliers, AI recommended purchase orders, employee punch/labour data, location settings and scheduling templates. Nory raised a $37M Series B in 2025 and is backed by Accel.
image: https://nory.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: nory-mcp.yml
  slug: nory-mcpyml
modified: '2026-07-20'
name: Nory
nav: Providers
network: true
overview: 'Nory publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Branch API, Brands API, and 7 more. Tagged areas include Company, Restaurant, Hospitality, Inventory, and Workforce.


  Nory''s developer surface includes engineering blog, support, authentication, sandbox, and 16 more developer resources.'
random_paper: 46
score:
  band: thin
  composite: 31.1
  delta: -3.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 32.3
    developer_ergonomics: 27.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 34.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Nory Authentication
  slug: nory-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nory Domain Security
  slug: nory-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nory
tags:
- Company
- Restaurant
- Hospitality
- Inventory
- Workforce
- Payroll
- Point of Sale
- Artificial Intelligence
- Food and Beverage
website: https://nory.ai/
---
