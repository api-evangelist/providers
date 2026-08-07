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
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 42
  human_in_the_loop: 1
  name: Wish Agentic Access
  operation_count: 102
  slug: wish-agentic-access
  summary_line: 102 operations · 42 acting · 1 human-in-the-loop
api_count: 21
apis:
- description: The Brands API from Wish — 1 operation(s) for brands.
  name: Wish Brands API
  slug: wish-brands-api
- description: Products endpoints which process requests asynchronously and triggers a running job
  name: Wish Bulk Products API
  slug: wish-bulk-products-api
- description: The Currencies API from Wish — 1 operation(s) for currencies.
  name: Wish Currencies API
  slug: wish-currencies-api
- description: APIs that support EU Product Compliance -- EU Regulation 2019/1020 on Market Surveillance and Compliance of Products (MSR).</br> For a product to be compliant with the MSR, a product must be linked wi
  name: Wish EU Product Compliance API
  slug: wish-eu-product-compliance-api
- description: 'APIs that support France Extended Producer Responsibility (EPR) Compliance.</br> For a merchant to be compliant with the EPR regulation, a product category they intend to sell must be linked with one '
  name: Wish France EPR Compliance API
  slug: wish-france-epr-compliance-api
- description: 'APIs that support Germany Extended Producer Responsibility (EPR) Compliance.</br> For a merchant to be compliant with the EPR regulation, their applicable products must be linked with one or more EPR '
  name: Wish Germany EPR Compliance API
  slug: wish-germany-epr-compliance-api
- description: Merchant APIs
  name: Wish Merchant API
  slug: wish-merchant-api
- description: The OAuth API from Wish — 3 operation(s) for oauth.
  name: Wish OAuth API
  slug: wish-oauth-api
- description: The Orders API from Wish — 9 operation(s) for orders.
  name: Wish Orders API
  slug: wish-orders-api
- description: Payments APIs
  name: Wish Payments API
  slug: wish-payments-api
- description: The Penalties API from Wish — 3 operation(s) for penalties.
  name: Wish Penalties API
  slug: wish-penalties-api
- description: The ProductBoost API from Wish — 7 operation(s) for productboost.
  name: Wish ProductBoost API
  slug: wish-productboost-api
- description: Products APIs
  name: Wish Products API
  slug: wish-products-api
- description: The Promotions Platform API from Wish — 6 operation(s) for promotions platform.
  name: Wish Promotions Platform API
  slug: wish-promotions-platform-api
- description: The Ratings API from Wish — 2 operation(s) for ratings.
  name: Wish Ratings API
  slug: wish-ratings-api
- description: Taxonomy APIs
  name: Wish Taxonomy API
  slug: wish-taxonomy-api
- description: For each consumer question or complaint, a ticket is created to manage the dialogue between you, Wish, and the consumer. With this API, you can fetch tickets awaiting your response, fetch a specific t
  name: Wish Tickets API
  slug: wish-tickets-api
- description: Unification Initiative APIs
  name: Wish Unification Initiative API
  slug: wish-unification-initiative-api
- description: Variations APIs
  name: Wish Variations API
  slug: wish-variations-api
- description: Merchant Videos APIs
  name: Wish Videos API
  slug: wish-videos-api
- description: APIs for managing webhook subscriptions. Merchants can use webhook subscriptions to receive notifications about particular events, instead of having to make API calls periodically to check their statu
  name: Wish Webhook API
  slug: wish-webhook-api
artifact_total: 27
asyncapis:
- description: ''
  name: Wish Webhooks
  slug: wish-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wish-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wish-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/wish-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wish-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wish-llms.txt
- group: company
  title: ''
  type: Website
  url: https://wish.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://merchant.wish.com/
- group: docs
  title: ''
  type: Documentation
  url: https://merchant.wish.com/documentation/api/v3/reference
- group: docs
  title: ''
  type: APIReference
  url: https://merchant.wish.com/documentation/api/v3/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://merchant.wish.com/documentation/api/v3/oauth
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ContextLogic
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wish.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wish.com/privacy_policy
- group: start
  title: ''
  type: SignUp
  url: https://merchant.wish.com/
created: '2026-07-17'
description: 'Wish, operated by ContextLogic Inc., is a global mobile-first e-commerce marketplace that connects value-conscious consumers with merchants and manufacturers around the world, with a large share of inventory shipped direct from suppliers. The Wish Marketplace V3 API lets sellers and ERP partners programmatically manage their storefront and operations: create and update products and variations, synchronize inventory and pricing, retrieve and fulfill orders, modify tracking and shipping-carrier assignments, run bulk create/download jobs, manage support tickets, penalties and infractions, run ProductBoost and promotion campaigns, meet EU/EPR product compliance obligations, and subscribe to webhooks for real-time order and product events. Authentication is OAuth 2.0 (authorization code flow with 37 scopes) plus OpenID Connect, using bearer access tokens over HTTPS, with production and sandbox environments.'
image: https://logo.clearbit.com/wish.com
layout: provider
modified: '2026-07-21'
name: Wish
nav: Providers
network: true
overview: 'Wish publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Brands API, Bulk Products API, Currencies API, and 18 more. Tagged areas include Company, E-Commerce, Marketplace, Retail, and Merchants.


  The Wish catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wish''s developer surface includes documentation, API reference, getting-started guide, signup flow, and 10 more developer resources.'
random_paper: 104
rate_limits:
- limit_count: 0
  name: Wish Rate Limits
  slug: wish-rate-limits
scopes:
- name: Wish Scopes
  scope_count: 39
  slug: wish-scopes
  summary_line: 39 scopes · authorizationCode
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 73.8
    developer_ergonomics: 34.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Wish Authentication
  slug: wish-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Wish Domain Security
  slug: wish-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wish
tags:
- Company
- E-Commerce
- Marketplace
- Retail
- Merchants
- Orders
- Products
- Fulfillment
- Shopping
- OAuth
website: https://wish.com
---
