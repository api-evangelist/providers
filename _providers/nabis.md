---
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 28.0
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: The current Nabis Platform API. A read-only JSON REST API authenticated with a static x-nabis-access-token header, covering inventory and inventory history, orders, invoices, retailers, warehouses and
  name: Nabis Platform API v2
  slug: nabis-platform-api-v2
- description: The original Nabis Platform API, published as a Redoc reference at developers.nabis.com and titled "Nabis Platform Api [DEPRECATED]" in its own specification. Four read-only operations — orders, detai
  name: Nabis Platform API v1 (deprecated)
  slug: nabis-platform-api-v1-deprecated
- description: 'A first-party OpenAPI 3.0.0 domain model Nabis publishes in its public GitLab group for the Universal QR Code / Universal Cannabis API problem space — collections, sku batches and skus — with contact '
  name: Nabis Universal QR Code API (design specification)
  slug: nabis-universal-qr-code-api-design-specification
artifact_total: 9
collections:
- collection_type: postman
  name: NABIS Platform API v2
  slug: postman-nabis-platform-api-v2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nabis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nabis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.nabis.com/v2/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.nabis.com/v2/docs/overview/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.nabis.com/v2/docs/category/endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.nabis.com/v2/docs/overview/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/nabis-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://www.nabis.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.nabis.com/newsroom/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.nabis.com/roadmap
- group: start
  title: ''
  type: SignUp
  url: https://www.nabis.com/contact
- group: start
  title: ''
  type: Login
  url: https://www.nabis.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nabis.com/legal/license-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nabis.com/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://developers.nabis.com/v2/assets/NABIS-Platform-API-v2.postman_collection.json
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nabis.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nabis-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nabis-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nabis-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nabis-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nabis-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nabis-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nabis-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/nabis-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nabis-plans-pricing.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nabis-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nabis-llms.txt
- group: build
  title: ''
  type: Examples
  url: examples/nabis-examples.yml
created: '2026-08-26'
description: Nabis is a licensed cannabis wholesale distributor and B2B marketplace founded in 2018 by Vince C. Ning and Jun S. Lee, operating in California, New York and Nevada. It runs distribution and fulfillment warehouses, an ordering marketplace connecting 400+ cannabis brands to licensed retailers, an analytics layer, and Nabis Capital, an invoice-based financing product, plus Nabis BillPay and Nabis Tracker for retailers. The company reports that 99% of retailers in the three states it serves receive product through Nabis and that it fulfills 3,500+ wholesale orders a week. For developers it publishes the Nabis Platform API — a read-only, API-key-authenticated JSON REST API for brands and retailers covering inventory, inventory history, orders, invoices, retailers, warehouses and the Nabis delivery calendar, with separate California and New York route trees, and an implementation of the Universal Cannabis API labeling standard for order manifests and QR-code regulator events.
image: https://cdn.prod.website-files.com/5c253860fd28a73e98ee5416/639cbabbb5d9b23d53a27b01_nabis_ogimage.jpg
layout: provider
mcp_servers:
- description: ''
  name: Nabis Platform API — MCP
  slug: nabis-platform-api-mcp
modified: '2026-08-26'
name: Nabis
nav: Providers
network: true
overview: 'Nabis publishes 3 APIs on the [APIs.io](https://apis.io/) network: Platform API v2, Platform API v1 (deprecated), and Universal QR Code API (design specification). Tagged areas include Cannabis, Distribution, Wholesale, Marketplace, and Logistics.


  Nabis'' developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 22 more developer resources.'
plans:
- name: Nabis Plans Pricing
  plan_count: 0
  slug: nabis-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Nabis Rate Limits
  slug: nabis-rate-limits
score:
  band: developing
  composite: 50.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 30.3
    contract_quality: 45.8
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 63.2
  provenance:
    conformance: first-party
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
security:
- kind: authentication
  name: Nabis Authentication
  slug: nabis-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nabis Domain Security
  slug: nabis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nabis
tags:
- Cannabis
- Distribution
- Wholesale
- Marketplace
- Logistics
- Supply Chain
- Inventory
- Orders
- Invoicing
- Retail
- Compliance
- Track and Trace
- California
- New York
website: https://www.nabis.com/
---
