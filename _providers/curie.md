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
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: The Catalog API from Curie — 1 operation(s) for catalog.
  name: Curie Catalog API
  slug: curie-catalog-api
- description: The Products API from Curie — 6 operation(s) for products.
  name: Curie Products API
  slug: curie-products-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://curie.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://chat.curie.app
- group: docs
  title: ''
  type: Documentation
  url: https://chat.curie.app/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://chat.curie.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chat.curie.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chat.curie.app/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/curie-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/curie-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/curie-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/curie-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/curie-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curie-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/curie-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/curie-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/curie-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/curie-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/curie-lifecycle.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/curie-overlay.yaml
- group: design
  title: ''
  type: Components
  url: components/curie-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Curie (Curie Vision, Inc.) is the commerce layer for AI — it connects AI assistants like ChatGPT, Claude, and Gemini to real product catalogs from 5.6M+ Shopify stores via the Model Context Protocol (MCP). Results carry live prices, real inventory, affiliate purchase links, and interactive 3D digital twins (GLB/USDZ) that shoppers can rotate and view in AR. Curie publishes a public REST catalog API, a hosted MCP server exposing 30 commerce tools, and cross-protocol discovery profiles (MCP, UCP, A2A, OpenAI Apps SDK). Most discovery and tool calls run on a free public tier with no auth; a Pro Bearer is required only for premium tools such as checkout. Backed by 500 Global.
image: https://cdn.prod.website-files.com/631a7e6c04b8fc3228d60317/631a7e6c04b8fc759ad60333_App%20Icon%20Main%20-%2032x32.png
layout: provider
mcp_servers:
- description: ''
  name: curie-mcp.yml
  slug: curie-mcpyml
modified: '2026-07-18'
name: Curie
nav: Providers
network: true
overview: 'Curie publishes 2 APIs on the [APIs.io](https://apis.io/) network: Catalog API and Products API. Tagged areas include Company, Commerce, E-Commerce, Shopify, and Artificial Intelligence.


  Curie''s developer surface includes documentation, pricing, authentication, and 17 more developer resources.'
random_paper: 72
scopes:
- name: Curie Scopes
  scope_count: 1
  slug: curie-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 41.7
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 65.9
    developer_ergonomics: 38.6
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 0.0
  previous_composite: 41.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curie/refs/heads/main/screenshots/curie-2026-07-25T210955.png
security:
- kind: authentication
  name: Curie Authentication
  slug: curie-authentication
  summary_line: none/http-bearer/oauth2 · 1 scheme
- kind: domain-security
  name: Curie Domain Security
  slug: curie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: curie
tags:
- Company
- Commerce
- E-Commerce
- Shopify
- Artificial Intelligence
- Model Context Protocol
- Agentic Commerce
- Product Discovery
- 3D
website: https://curie.co
---
