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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Shopup Agentic Access
  operation_count: 7
  slug: shopup-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- baseURL: https://openapi.redx.com.bd/v1.0.0-beta
  baseurl_source: declared
  description: Deliverable areas / zones
  name: ShopUp Areas API
  slug: shopup-areas-api
- baseURL: https://openapi.redx.com.bd/v1.0.0-beta
  baseurl_source: declared
  description: Create, track and inspect parcels
  name: ShopUp Parcels API
  slug: shopup-parcels-api
- baseURL: https://openapi.redx.com.bd/v1.0.0-beta
  baseurl_source: declared
  description: Merchant pickup store management
  name: ShopUp Pickup Stores API
  slug: shopup-pickup-stores-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: REDX Open Areas API
  slug: open-shopup-areas-api
- collection_type: open
  name: REDX Open Areas Parcels API
  slug: open-shopup-parcels-api
- collection_type: open
  name: REDX Open Areas Pickup Stores API
  slug: open-shopup-pickup-stores-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shopup-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://shopup.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://redx.com.bd/developer-api/
- group: docs
  title: ''
  type: Documentation
  url: https://redx.com.bd/developer-api/
- group: docs
  title: ''
  type: APIReference
  url: https://redx.com.bd/developer-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://redx.com.bd/developer-api/
- group: company
  title: ''
  type: Blog
  url: https://shopup.org/blog
- group: operate
  title: ''
  type: Support
  url: https://redx.com.bd/faq/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redx.com.bd/privacy-policy/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shopup-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopup-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopup-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shopup-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shopup-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shopup-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shopup-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shopup-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/shopup-redx-overlay.yaml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shopup-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shopup-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/shopup-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shopup-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/shopup-create-parcel.md
created: '2026-07-17'
description: ShopUp is a Bangladesh technology company that digitizes the country's small-business supply chain, connecting mills and manufacturers to a network of hundreds of thousands of neighbourhood shops. It operates Mokam, a B2B commerce platform where small retailers source fast-moving consumer goods at fair prices, and REDX, a nationwide last-mile logistics and courier network reaching sub-districts across all 64 districts. REDX publishes a public merchant Open API that lets e-commerce sellers create and track parcels and manage pickup stores programmatically. ShopUp is backed by Prosus Ventures and in 2025 combined with Saudi Arabia's Sary to form the SILQ Group.
image: https://cdn.prod.website-files.com/6538a2c4ccf1fed5a7d6e311/661e20ec03673cb2f41ff4c2_ShopUp-open-graph.jpg
layout: provider
mcp_servers:
- description: ''
  name: ShopUp MCP Server
  slug: shopup-mcp-server
modified: '2026-07-21'
name: ShopUp
nav: Providers
network: true
overview: 'ShopUp publishes 3 APIs on the [APIs.io](https://apis.io/) network: Areas API, Parcels API, and Pickup Stores API. Tagged areas include Company, Marketplace, Logistics, Couriers, and Last Mile Delivery.


  ShopUp''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 16 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 55.8
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 37.4
  provenance:
    agentic_access: derived
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
screenshot: https://raw.githubusercontent.com/api-evangelist/shopup/refs/heads/main/screenshots/shopup-2026-09-02T155307.png
security:
- kind: authentication
  name: Shopup Authentication
  slug: shopup-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Shopup Domain Security
  slug: shopup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shopup
tags:
- Company
- Marketplace
- Logistics
- Couriers
- Last Mile Delivery
- B2B Commerce
- Bangladesh
- E-Commerce
- Fintech
website: https://shopup.org
---
