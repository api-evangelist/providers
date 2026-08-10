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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Vori Agentic Access
  operation_count: 9
  slug: vori-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- description: The Store products API from Vori — 7 operation(s) for store products.
  name: Vori Store products API
  slug: vori-store-products-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.vori.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.vori.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.vori.com/api-reference/store-products/list-store-products
- group: start
  title: ''
  type: GettingStarted
  url: https://help.vori.com/api/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.vori.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vori.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voriteam
- group: start
  title: ''
  type: Login
  url: https://app.vori.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vori.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vori.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/vori-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vori-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vori-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/vori-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vori-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vori-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vori-store-products-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/vori-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vori-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vori-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vori-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vori-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Vori is a connected point-of-sale and operations platform built exclusively for independent grocery stores, unifying checkout, payments (EBT, eWIC, contactless, gift cards), loyalty and SMS marketing, ordering, receiving, invoice processing, inventory, pricing automation, and reporting in one system. The Vori REST API at api.vori.com lets grocers and their integrations read and manage store catalog data — store products, pricing rules, product history, and search — using bearer-token authentication.
image: https://cdn.prod.website-files.com/696a48a7323254ea5a7ab884/696a48a7323254ea5a7ab8c0_logo.png
layout: provider
mcp_servers:
- description: ''
  name: vori-mcp.yml
  slug: vori-mcpyml
modified: '2026-07-21'
name: Vori
nav: Providers
network: true
overview: 'Vori publishes 1 API on the [APIs.io](https://apis.io/) network: Store products API. Tagged areas include Company, Applications, Grocery, Point of Sale, and Retail.


  Vori''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 100
score:
  band: thin
  composite: 40.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 55.8
    developer_ergonomics: 47.3
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Vori Authentication
  slug: vori-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vori Domain Security
  slug: vori-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vori
tags:
- Company
- Applications
- Grocery
- Point of Sale
- Retail
- Inventory
- Payments
- Commerce
website: https://www.vori.com
---
