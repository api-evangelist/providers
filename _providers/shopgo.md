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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-02'
api_count: 2
apis:
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: Obtain and test API keys
  name: ShopGo Authentication API
  slug: shopgo-authentication-api
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: Order, payment and shipment management
  name: ShopGo Orders API
  slug: shopgo-orders-api
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: Store availability, legal and webhook settings
  name: ShopGo Store API
  slug: shopgo-store-api
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: The Tenants API from ShopGo — 2 operation(s) for tenants.
  name: ShopGo Tenants API
  slug: shopgo-tenants-api
- baseURL: https://api.shopgo.me/v1/management
  baseurl_source: declared
  description: Dashboard user and tenant information
  name: ShopGo Users API
  slug: shopgo-users-api
artifact_total: 15
asyncapis:
- description: ''
  name: Shopgo Webhooks
  slug: shopgo-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ShopGo Management Authentication API
  slug: open-shopgo-authentication-api
- collection_type: open
  name: ShopGo Management Authentication Orders API
  slug: open-shopgo-orders-api
- collection_type: open
  name: ShopGo Management Authentication Store API
  slug: open-shopgo-store-api
- collection_type: open
  name: ShopGo Management Authentication Tenants API
  slug: open-shopgo-tenants-api
- collection_type: open
  name: ShopGo Management Authentication Users API
  slug: open-shopgo-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://shopgo.me
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shopgo.me
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shopgo.me
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shopgo.me/management-api/orders
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopgo
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopgo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shopgo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shopgo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shopgo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shopgo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shopgo-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shopgo-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/shopgo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shopgo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shopgo-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/shopgo-management-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopgo-domain-security.yml
created: '2026-07-17'
description: 'ShopGo (now branded Makane) is a MENA-focused eCommerce SaaS platform based in Amman, Jordan and founded in 2012, backed by 500 Global. It lets merchants build and run online stores with integrated payment and shipment options across the Middle East and North Africa. For developers, ShopGo publishes a GitBook developer portal (docs.shopgo.me) documenting two REST APIs served from api.shopgo.me: a Management API for store, order, payment and shipment administration, and an internal Platform API for SaaS tenant control. Both use API-key authentication and a JSON result/payload envelope, and the platform supports configurable checkout webhooks (custom shipping rates, order confirmation).'
image: https://github.com/shopgo.png
layout: provider
mcp_servers:
- description: ''
  name: ShopGo MCP Server
  slug: shopgo-mcp-server
modified: '2026-07-21'
name: ShopGo
nav: Providers
network: true
overview: 'ShopGo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Orders API, Store API, and 2 more. Tagged areas include Company, E-Commerce, Online Stores, Payments, and Shipping.


  The ShopGo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShopGo''s developer surface includes documentation, API reference, authentication, and 15 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 60.4
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 31.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shopgo/refs/heads/main/screenshots/shopgo-2026-09-02T155259.png
security:
- kind: authentication
  name: Shopgo Authentication
  slug: shopgo-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Shopgo Domain Security
  slug: shopgo-domain-security
  summary_line: TLSv1.3
slug: shopgo
tags:
- Company
- E-Commerce
- Online Stores
- Payments
- Shipping
- Software-as-a-Service
- MENA
- Order
website: https://shopgo.me
---
