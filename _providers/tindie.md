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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://www.tindie.com/api/v1
  baseurl_source: declared
  description: A seller's orders (authenticated).
  name: Tindie order API
  slug: tindie-order-api
- baseURL: https://www.tindie.com/api/v1
  baseurl_source: declared
  description: Line items within a seller's orders (authenticated).
  name: Tindie orderitem API
  slug: tindie-orderitem-api
- baseURL: https://www.tindie.com/api/v1
  baseurl_source: declared
  description: Store product listings (public read).
  name: Tindie product API
  slug: tindie-product-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tindie order API
  slug: open-tindie-order-api
- collection_type: open
  name: Tindie order orderitem API
  slug: open-tindie-orderitem-api
- collection_type: open
  name: Tindie order product API
  slug: open-tindie-product-api
- collection_type: open
  name: API Collection
  slug: open-tindie-product-schema
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
  name: Tindie MCP Server
  slug: tindie-mcp-server
modified: '2026-07-21'
name: Tindie
nav: Providers
network: true
overview: 'Tindie publishes 3 APIs on the [APIs.io](https://apis.io/) network: order API, orderitem API, and product API. Tagged areas include Company, Marketplace, Hardware, Electronics, and Maker.


  Tindie''s developer surface includes API reference, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 53.1
    developer_ergonomics: 24.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 28.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
- E-Commerce
- Open Source Hardware
- Order
website: https://www.tindie.com
---
