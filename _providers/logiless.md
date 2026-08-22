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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-19'
api_count: 9
apis:
- description: 商品マスタ / 商品対応表 — product master and mapping
  name: Logiless Articles API
  slug: logiless-articles-api
- description: 入荷予定伝票 — expected inbound shipments
  name: Logiless Inbound Deliveries API
  slug: logiless-inbound-deliveries-api
- description: 倉庫間移動伝票 — stock transfers between warehouses
  name: Logiless Inter-Warehouse Transfers API
  slug: logiless-inter-warehouse-transfers-api
- description: 在庫 / 保管状況 / 日次在庫表 / 在庫操作ログ / 倉庫別発注点 — inventory & storage summaries
  name: Logiless Inventory API
  slug: logiless-inventory-api
- description: 店舗 / 倉庫 / ロケーション — stores, warehouses and locations
  name: Logiless Locations API
  slug: logiless-locations-api
- description: 出荷伝票 — shipment records
  name: Logiless Outbound Deliveries API
  slug: logiless-outbound-deliveries-api
- description: 受注伝票 — order intake, editing, confirmation and reversal
  name: Logiless Sales Orders API
  slug: logiless-sales-orders-api
- description: 売上返品 — returns
  name: Logiless Sales Returns API
  slug: logiless-sales-returns-api
- description: 仕入先マスタ — supplier master
  name: Logiless Suppliers API
  slug: logiless-suppliers-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LOGILESS Articles API
  slug: open-logiless-articles-api
- collection_type: open
  name: LOGILESS Articles Inbound Deliveries API
  slug: open-logiless-inbound-deliveries-api
- collection_type: open
  name: LOGILESS Articles Inter-Warehouse Transfers API
  slug: open-logiless-inter-warehouse-transfers-api
- collection_type: open
  name: LOGILESS Articles Inventory API
  slug: open-logiless-inventory-api
- collection_type: open
  name: LOGILESS Articles Locations API
  slug: open-logiless-locations-api
- collection_type: open
  name: LOGILESS Articles Outbound Deliveries API
  slug: open-logiless-outbound-deliveries-api
- collection_type: open
  name: LOGILESS Articles Sales Orders API
  slug: open-logiless-sales-orders-api
- collection_type: open
  name: LOGILESS Articles Sales Returns API
  slug: open-logiless-sales-returns-api
- collection_type: open
  name: LOGILESS Articles Suppliers API
  slug: open-logiless-suppliers-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/logiless-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/logiless-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/logiless-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/logiless-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/logiless-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/logiless-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/logiless-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/logiless-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/logiless-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/logiless-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/logiless-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/logiless-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/logiless-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logiless-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app2.logiless.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://support.logiless.com/
- group: docs
  title: ''
  type: APIReference
  url: https://app2.logiless.com/developer/documents/specifications
- group: start
  title: ''
  type: GettingStarted
  url: https://app2.logiless.com/developer/documents/authentication
- group: operate
  title: ''
  type: Support
  url: https://support.logiless.com/
- group: company
  title: ''
  type: Blog
  url: https://www.logiless.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.logiless.com/price/
- group: start
  title: ''
  type: SignUp
  url: https://app2.logiless.com/merchant/sign_up
- group: start
  title: ''
  type: Login
  url: https://app2.logiless.com/merchant/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.logiless.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.logiless.com/legal/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://go.logiless.com/contact
- group: company
  title: ''
  type: Website
  url: https://www.logiless.com
created: '2026-07-17'
description: LOGILESS (ロジレス) is a Japanese cloud EC logistics platform that unifies order management (OMS) and warehouse management (WMS) for e-commerce merchants — automating order intake from marketplaces and shopping carts (Rakuten, Shopify, ColorMe, futureshop, ec-force and more), inventory synchronization, allocation, shipping-label issuance and warehouse operations. LOGILESS exposes a RESTful, OAuth2-protected API (scoped per merchant) for reading and writing sales orders, outbound and inbound deliveries, sales returns, inter-warehouse transfers, articles (product master), multi-layer inventory summaries, warehouses, stores and suppliers. The company is a 500 Global portfolio company. This profile was enriched by the API Evangelist pipeline from LOGILESS's public developer documentation; the OpenAPI here is derived and not an official LOGILESS artifact.
image: https://support.logiless.com/wp-content/uploads/2021/06/ogp.png
layout: provider
mcp_servers:
- description: ''
  name: logiless-mcp.yml
  slug: logiless-mcpyml
modified: '2026-07-20'
name: Logiless
nav: Providers
network: true
overview: 'Logiless publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Articles API, Inbound Deliveries API, Inter-Warehouse Transfers API, and 6 more. Tagged areas include Logistics, E-commerce, Order Management, Warehouse Management, and Inventory.


  Logiless'' developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 1
  name: Logiless Rate Limits
  slug: logiless-rate-limits
scopes:
- name: Logiless Scopes
  scope_count: 0
  slug: logiless-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.6
  delta: 0.5
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 47.8
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 47.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logiless/refs/heads/main/screenshots/logiless-2026-07-25T225502.png
security:
- kind: authentication
  name: Logiless Authentication
  slug: logiless-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Logiless Domain Security
  slug: logiless-domain-security
  summary_line: TLSv1.2 · DMARC
slug: logiless
tags:
- Logistics
- E-commerce
- Order Management
- Warehouse Management
- Inventory
- Fulfillment
- Shipping
- OMS
- WMS
- Japan
website: https://www.logiless.com
---
