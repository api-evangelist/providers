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
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: A seller's orders (authenticated).
  name: Tindie order API
  slug: tindie-order-api
- description: Line items within a seller's orders (authenticated).
  name: Tindie orderitem API
  slug: tindie-orderitem-api
- description: Store product listings (public read).
  name: Tindie product API
  slug: tindie-product-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tindie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tindie.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.tindie.com/api/v1/
- group: operate
  title: ''
  type: Support
  url: https://www.tindie.com/help/
- group: company
  title: ''
  type: Blog
  url: https://www.tindie.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tindie.com/about/terms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tindie
- group: auth
  title: ''
  type: Authentication
  url: authentication/tindie-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tindie-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tindie-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tindie-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tindie-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tindie-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tindie-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tindie-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tindie-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tindie-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Tindie is an online marketplace for indie electronics and maker hardware — DIY kits, robotics, 3D-printing gear, IoT boards, and open-source hardware sold directly by independent creators worldwide. Tindie publishes a small public REST API built on Django Tastypie that exposes product listings and, for authenticated sellers, their orders and order line items, using API-key authentication (ApiKey) and standard Tastypie limit/offset pagination with a self-describing per-resource schema surface.
image: https://avatars.githubusercontent.com/u/2267159
layout: provider
mcp_servers:
- description: ''
  name: tindie-mcp.yml
  slug: tindie-mcpyml
modified: '2026-07-21'
name: Tindie
nav: Providers
network: true
overview: 'Tindie publishes 3 APIs on the [APIs.io](https://apis.io/) network: order API, orderitem API, and product API. Tagged areas include Company, Marketplace, Hardware, Electronics, and Maker.


  Tindie''s developer surface includes API reference, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 67
score:
  band: thin
  composite: 34.1
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 60.5
    developer_ergonomics: 27.7
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 34.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Tindie Authentication
  slug: tindie-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Tindie Domain Security
  slug: tindie-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tindie
tags:
- Company
- Marketplace
- Hardware
- Electronics
- Maker
- eCommerce
- Open Source Hardware
- Orders
website: https://www.tindie.com
---
