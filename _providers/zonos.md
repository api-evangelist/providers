---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-08-11'
api_count: 6
apis:
- description: The Zonos Graph is the company's supported integration surface — a single GraphQL endpoint covering landed cost, classification, country of origin, export control, item and party restriction screening
  name: Zonos Graph (GraphQL API)
  slug: zonos-graph-graphql-api
- description: Legacy REST endpoint that returns a complete breakdown of the duties, taxes and fees making up a total landed cost for a shipment. Requires a `zonos-version` request header. Zonos documents its REST l
  name: Zonos Landed Cost REST API (legacy)
  slug: zonos-landed-cost-rest-api
- description: Legacy REST endpoints for harmonizing a catalog to HS codes one item at a time or in bulk, with a group identifier for retrieving bulk results. Documented paths are /v1/classify, /v1/classify/:id, /v1
  name: Zonos Classify REST API (legacy)
  slug: zonos-classify-rest-api
- description: Legacy REST endpoint returning international shipping rates for carriers and service levels. Documented path is /v1/shipment_rating. Declared end-of-life in favor of the Graph.
  name: Zonos Rating REST API (legacy)
  slug: zonos-rating-rest-api
- description: Legacy REST endpoint that accepts the details of a shopper's completed order and returns the Zonos-specific order ID. Documented path is /v1/orders. Declared end-of-life in favor of the Graph.
  name: Zonos Order Complete REST API (legacy)
  slug: zonos-order-complete-rest-api
- description: Legacy REST integration surface for Zonos Checkout, listed on the Zonos REST API reference index. No base URL or endpoint path was resolvable from the public reference page on 2026-07-30, so none is a
  name: Zonos Checkout REST API (legacy)
  slug: zonos-checkout-rest-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://zonos.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zonos.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://zonos.com/developer
- group: docs
  title: ''
  type: GraphQL
  url: graphql/zonos-graphql-schema.json
- group: auth
  title: ''
  type: Authentication
  url: https://zonos.com/docs/account/retrieve-graphql-key
- group: auth
  title: ''
  type: OAuth
  url: https://zonos.com/docs/supply-chain/oauth
- group: operate
  title: ''
  type: RateLimits
  url: https://zonos.com/docs/supply-chain/rate-limiting
- group: design
  title: ''
  type: Webhooks
  url: https://zonos.com/docs/supply-chain/webhooks
- group: commercial
  title: ''
  type: Pricing
  url: https://zonos.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://account.zonos.com/register
- group: start
  title: ''
  type: Portal
  url: https://dashboard.zonos.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zonos.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Zonos
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zonos
- group: company
  title: ''
  type: Blog
  url: https://zonos.com/all-posts
- group: company
  title: ''
  type: About
  url: https://zonos.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://zonos.com/contact-support
- group: agent
  title: ''
  type: LLMSTxt
  url: https://zonos.com/llms.txt
- group: other
  title: ''
  type: Sitemap
  url: https://zonos.com/sitemap.xml
created: '2026-07-30'
description: Zonos is a cross-border trade technology company headquartered in St. George, Utah, United States, that sells customs and trade compliance as an API. Its products calculate landed cost (duty, tax, brokerage and carrier fees), classify goods to HS codes with AI, screen parties and items against restricted and denied lists, rate and label international parcels, generate customs documents, submit postal PDDP declarations to destination posts, and file CBP entries for consolidated air consignments. It sits in the middle of the chain — between merchants, carriers, postal operators and freight consolidators on one side and customs authorities on the other — and is one of the few organizations in this tier whose integration surface is genuinely public rather than a customer-contract portal. A single unified GraphQL endpoint at https://api.zonos.com/graphql answers unauthenticated introspection (1,396 types, 170 queries, 153 mutations, harvested 2026-07-30), the reference is browsable
  without login at https://zonos.com/developer, and a legacy REST v1 layer remains documented but is declared end-of-life. Calling anything real still requires a credential token from the Zonos Dashboard, which is self-serve only for Shopify merchants; every other platform is routed through sales and an account agreement.
image: https://zonos.com/images/zonos-logo-social-sharing.webp
layout: provider
modified: '2026-07-30'
name: Zonos
nav: Providers
network: true
overview: 'Zonos publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Supply Chain, United States, Customs, and Trade Compliance.


  Zonos'' developer surface includes documentation, API reference, authentication, pricing, signup flow, developer portal, engineering blog, and 12 more developer resources.'
random_paper: 105
score:
  band: emerging
  composite: 23.2
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 23.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
slug: zonos
tags:
- Logistics
- Supply Chain
- United States
- Customs
- Trade Compliance
- Landed Cost
- Duty and Tax
- HS Classification
- Cross-Border Commerce
- Parcel
- Postal
- Track and Trace
- Standards
website: https://zonos.com/
---
