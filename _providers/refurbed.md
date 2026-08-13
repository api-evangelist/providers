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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-08-12'
api_count: 18
apis:
- description: The BuybackBidService API from Refurbed — 8 operation(s) for buybackbidservice.
  name: Refurbed BuybackBidService API
  slug: refurbed-buybackbidservice-api
- description: The BuybackOrderItemService API from Refurbed — 6 operation(s) for buybackorderitemservice.
  name: Refurbed BuybackOrderItemService API
  slug: refurbed-buybackorderitemservice-api
- description: The BuybackOrderService API from Refurbed — 1 operation(s) for buybackorderservice.
  name: Refurbed BuybackOrderService API
  slug: refurbed-buybackorderservice-api
- description: The BuybackProductService API from Refurbed — 1 operation(s) for buybackproductservice.
  name: Refurbed BuybackProductService API
  slug: refurbed-buybackproductservice-api
- description: The BuybackSupplyboxService API from Refurbed — 1 operation(s) for buybacksupplyboxservice.
  name: Refurbed BuybackSupplyboxService API
  slug: refurbed-buybacksupplyboxservice-api
- description: The CatalogService API from Refurbed — 1 operation(s) for catalogservice.
  name: Refurbed CatalogService API
  slug: refurbed-catalogservice-api
- description: The CurrencyService API from Refurbed — 2 operation(s) for currencyservice.
  name: Refurbed CurrencyService API
  slug: refurbed-currencyservice-api
- description: The InstanceService API from Refurbed — 4 operation(s) for instanceservice.
  name: Refurbed InstanceService API
  slug: refurbed-instanceservice-api
- description: The MarketOfferService API from Refurbed — 10 operation(s) for marketofferservice.
  name: Refurbed MarketOfferService API
  slug: refurbed-marketofferservice-api
- description: The MarketService API from Refurbed — 4 operation(s) for marketservice.
  name: Refurbed MarketService API
  slug: refurbed-marketservice-api
- description: The MerchantService API from Refurbed — 4 operation(s) for merchantservice.
  name: Refurbed MerchantService API
  slug: refurbed-merchantservice-api
- description: The OfferService API from Refurbed — 9 operation(s) for offerservice.
  name: Refurbed OfferService API
  slug: refurbed-offerservice-api
- description: The OrderItemReturnService API from Refurbed — 1 operation(s) for orderitemreturnservice.
  name: Refurbed OrderItemReturnService API
  slug: refurbed-orderitemreturnservice-api
- description: The OrderItemService API from Refurbed — 8 operation(s) for orderitemservice.
  name: Refurbed OrderItemService API
  slug: refurbed-orderitemservice-api
- description: The OrderService API from Refurbed — 13 operation(s) for orderservice.
  name: Refurbed OrderService API
  slug: refurbed-orderservice-api
- description: The ProductService API from Refurbed — 2 operation(s) for productservice.
  name: Refurbed ProductService API
  slug: refurbed-productservice-api
- description: The ShippingProfileService API from Refurbed — 6 operation(s) for shippingprofileservice.
  name: Refurbed ShippingProfileService API
  slug: refurbed-shippingprofileservice-api
- description: The TicketService API from Refurbed — 10 operation(s) for ticketservice.
  name: Refurbed TicketService API
  slug: refurbed-ticketservice-api
artifact_total: 22
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/refurbed-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/refurbed-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.refurbed.com
- group: docs
  title: ''
  type: Documentation
  url: https://gitlab.com/refurbed-community/public-apis
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/refurbed-community/public-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/refurbed
- group: operate
  title: ''
  type: Support
  url: mailto:integrations@refurbed.com
- group: docs
  title: ''
  type: APIReference
  url: https://gitlab.com/refurbed-community/public-apis/-/tree/master/refurbed_merchant_api/refb/merchant/v1/services
- group: start
  title: ''
  type: GettingStarted
  url: https://gitlab.com/refurbed-community/public-apis/-/blob/master/refurbed_merchant_api/refb/merchant/v1/README.md
- group: design
  title: ''
  type: Conventions
  url: conventions/refurbed-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/refurbed-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/refurbed-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/refurbed-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/refurbed-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/refurbed-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/refurbed-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/refurbed-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/refurbed-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/refurbed-merchant-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/refurbed-affiliate-overlay.yaml
- group: other
  title: ''
  type: Protobuf
  url: grpc/refurbed_merchant_api/refb/merchant/v1/services
created: '2026-07-17'
description: Refurbed is a European online marketplace for professionally refurbished electronics and other sustainable goods, headquartered in Vienna, Austria and operating across Europe. Merchants sell refurbished phones, laptops, tablets, wearables and more to consumers through the refurbed platform, and refurbed exposes public partner APIs so merchants and affiliates can integrate programmatically. The Merchant API lets sellers manage offers, prices, stock, orders, returns, refunds, shipping profiles, tickets and buyback flows, while the Affiliate Partner API exposes the marketplace catalog (markets, products, instances and BuyBox data) for affiliates. Both APIs are offered as gRPC with an equivalent HTTP/JSON transport, defined by published Protobuf and OpenAPI (Swagger 2.0) specifications, and are authenticated with a secret token passed in the Authorization header.
image: https://www.refurbed.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: refurbed-mcp.yml
  slug: refurbed-mcpyml
modified: '2026-07-21'
name: Refurbed
nav: Providers
network: true
overview: 'Refurbed publishes 18 APIs on the [APIs.io](https://apis.io/) network, including BuybackBidService API, BuybackOrderItemService API, BuybackOrderService API, and 15 more. Tagged areas include Company, Marketplace, E-Commerce, Refurbished Electronics, and Sustainability.


  Refurbed''s developer surface includes authentication, documentation, support, API reference, getting-started guide, and 17 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 0
  name: Refurbed Rate Limits
  slug: refurbed-rate-limits
score:
  band: thin
  composite: 32.0
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 54.9
    developer_ergonomics: 45.1
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 32.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Refurbed Authentication
  slug: refurbed-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Refurbed Domain Security
  slug: refurbed-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: refurbed
tags:
- Company
- Marketplace
- E-Commerce
- Refurbished Electronics
- Sustainability
- Circular Economy
- Retail
- Merchant API
- Affiliate
- gRPC
website: https://www.refurbed.com
---
