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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.4
  scored_at: '2026-08-26'
api_count: 17
apis:
- description: The csv API from Canal — 3 operation(s) for csv.
  name: Canal csv API
  slug: canal-csv-api
- description: The fulfillments API from Canal — 2 operation(s) for fulfillments.
  name: Canal fulfillments API
  slug: canal-fulfillments-api
- description: The markets API from Canal — 1 operation(s) for markets.
  name: Canal markets API
  slug: canal-markets-api
- description: The max-shipping-rates API from Canal — 1 operation(s) for max-shipping-rates.
  name: Canal max-shipping-rates API
  slug: canal-max-shipping-rates-api
- description: The orders API from Canal — 6 operation(s) for orders.
  name: Canal orders API
  slug: canal-orders-api
- description: The product_sets API from Canal — 2 operation(s) for product_sets.
  name: Canal product_sets API
  slug: canal-product-sets-api
- description: The products API from Canal — 5 operation(s) for products.
  name: Canal products API
  slug: canal-products-api
- description: The refunds API from Canal — 2 operation(s) for refunds.
  name: Canal refunds API
  slug: canal-refunds-api
- description: The returns API from Canal — 4 operation(s) for returns.
  name: Canal returns API
  slug: canal-returns-api
- description: The selection API from Canal — 1 operation(s) for selection.
  name: Canal selection API
  slug: canal-selection-api
- description: The shipping API from Canal — 1 operation(s) for shipping.
  name: Canal shipping API
  slug: canal-shipping-api
- description: The shipping-rates API from Canal — 1 operation(s) for shipping-rates.
  name: Canal shipping-rates API
  slug: canal-shipping-rates-api
- description: The shops API from Canal — 2 operation(s) for shops.
  name: Canal shops API
  slug: canal-shops-api
- description: The tax-and-shipping API from Canal — 2 operation(s) for tax-and-shipping.
  name: Canal tax-and-shipping API
  slug: canal-tax-and-shipping-api
- description: The tax API from Canal — 1 operation(s) for tax.
  name: Canal tax API
  slug: canal-tax-api
- description: The variants API from Canal — 2 operation(s) for variants.
  name: Canal variants API
  slug: canal-variants-api
- description: The webhooks API from Canal — 2 operation(s) for webhooks.
  name: Canal webhooks API
  slug: canal-webhooks-api
artifact_total: 39
asyncapis:
- description: ''
  name: Canal Webhooks
  slug: canal-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rokt Catalog csv API
  slug: open-canal-csv-api
- collection_type: open
  name: Rokt Catalog csv fulfillments API
  slug: open-canal-fulfillments-api
- collection_type: open
  name: Rokt Catalog csv markets API
  slug: open-canal-markets-api
- collection_type: open
  name: Rokt Catalog csv max-shipping-rates API
  slug: open-canal-max-shipping-rates-api
- collection_type: open
  name: Rokt Catalog csv orders API
  slug: open-canal-orders-api
- collection_type: open
  name: Rokt Catalog csv product_sets API
  slug: open-canal-product-sets-api
- collection_type: open
  name: Rokt Catalog csv products API
  slug: open-canal-products-api
- collection_type: open
  name: Rokt Catalog csv refunds API
  slug: open-canal-refunds-api
- collection_type: open
  name: Rokt Catalog csv returns API
  slug: open-canal-returns-api
- collection_type: open
  name: Rokt Catalog csv selection API
  slug: open-canal-selection-api
- collection_type: open
  name: Rokt Catalog csv shipping API
  slug: open-canal-shipping-api
- collection_type: open
  name: Rokt Catalog csv shipping-rates API
  slug: open-canal-shipping-rates-api
- collection_type: open
  name: Rokt Catalog csv shops API
  slug: open-canal-shops-api
- collection_type: open
  name: Rokt Catalog csv tax-and-shipping API
  slug: open-canal-tax-and-shipping-api
- collection_type: open
  name: Rokt Catalog csv tax API
  slug: open-canal-tax-api
- collection_type: open
  name: Rokt Catalog csv variants API
  slug: open-canal-variants-api
- collection_type: open
  name: Rokt Catalog csv webhooks API
  slug: open-canal-webhooks-api
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canal-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/canal-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/canal-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canal-llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canal-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/canal-data-model.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/canal-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/canal-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canal-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/canal-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canal-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/canal-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/canal-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shopcanal.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shopcanal.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shopcanal.com/reference/brand
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shopcanal.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://shopcanalhelp.zendesk.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.shopcanal.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopcanal
- group: start
  title: ''
  type: SignUp
  url: https://app.shopcanal.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shopcanal.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shopcanal.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.shopcanal.com/
created: '2026-07-17'
description: Canal (now Rokt Catalog, following Rokt's acquisition of Canal) is a dropship and marketplace commerce platform that lets brands, retailers, and platforms sell curated third-party products without holding inventory. Suppliers (Brands) list products into Canal's vetted network; Storefronts (Partners) surface those products, and Canal forwards each order to the Supplier who ships directly to the customer. The Rokt Catalog Platform API (api.shopcanal.com/platform) exposes products, variants, orders, fulfillments, refunds, returns, shops, shipping/tax calculation, and webhooks so custom, headless, and marketplace backends can integrate alongside the native Shopify, WooCommerce, and BigCommerce apps. Canal was an a16z portfolio company.
image: https://cdn.prod.website-files.com/633617b15a78ccbe02dcf627/657cdf8810129b1d520e01c1_Site%20Opengrap%20Image.png
layout: provider
mcp_servers:
- description: ''
  name: Canal MCP Server
  slug: canal-mcp-server
modified: '2026-07-18'
name: Canal
nav: Providers
network: true
overview: 'Canal publishes 17 APIs on the [APIs.io](https://apis.io/) network, including csv API, fulfillments API, markets API, and 14 more. Tagged areas include Company, E-Commerce, Dropshipping, Marketplace, and Commerce.


  The Canal catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Canal''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 42.6
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 59.4
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 10.5
  previous_composite: 42.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canal/refs/heads/main/screenshots/canal-2026-07-25T204329.png
security:
- kind: authentication
  name: Canal Authentication
  slug: canal-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Canal Domain Security
  slug: canal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: canal
tags:
- Company
- E-Commerce
- Dropshipping
- Marketplace
- Commerce
- Retail
- Fulfillment
- Order
- Product
- Webhook
website: https://www.shopcanal.com/
---
