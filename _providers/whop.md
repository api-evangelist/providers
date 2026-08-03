---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Whop Agentic Access
  operation_count: 51
  slug: whop-agentic-access
  summary_line: 51 operations · 30 acting
api_count: 12
apis:
- description: Whop's GraphQL API at api.whop.com/public-graphql, positioned as the current primary interface for building apps - search/discovery, access passes, plans, memberships, users, and messaging - authentic
  name: Whop GraphQL API
  slug: whop-graphql-api
- description: 'Bidirectional realtime WebSocket for Whop apps - custom app messages and chat/feed updates - connected and authenticated through the @whop/react and @whop/api SDKs. Whop does not publish a raw wss:// '
  name: Whop Realtime WebSocket API
  slug: whop-realtime-websocket-api
- description: Reusable checkout / payment flow configurations.
  name: Whop Checkout Configurations API
  slug: whop-checkout-configurations-api
- description: Seller companies (whops) and sub-merchant onboarding.
  name: Whop Companies API
  slug: whop-companies-api
- description: A user's access to a product; lifecycle and access management.
  name: Whop Memberships API
  slug: whop-memberships-api
- description: Charges, refunds, retries, and voids.
  name: Whop Payments API
  slug: whop-payments-api
- description: Pricing plans attached to products.
  name: Whop Plans API
  slug: whop-plans-api
- description: Products (access passes) that companies sell.
  name: Whop Products API
  slug: whop-products-api
- description: Discount / promo codes applied at checkout.
  name: Whop Promo Codes API
  slug: whop-promo-codes-api
- description: Programmatic payouts to users and connected accounts.
  name: Whop Transfers API
  slug: whop-transfers-api
- description: Whop users and their access checks.
  name: Whop Users API
  slug: whop-users-api
- description: Webhook endpoint registration for platform events.
  name: Whop Webhooks API
  slug: whop-webhooks-api
artifact_total: 22
asyncapis:
- description: AsyncAPI 2.6 description of Whop's **realtime WebSocket** surface, used by Whop apps for bidirectional realtime messaging (custom app messages plus chat / feed updates) between connected clients and W
  name: Whop Realtime WebSocket
  slug: whop-asyncapi
collections:
- collection_type: open
  name: Whop REST API (v1)
  slug: open-whop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whop-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/whopio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whop
- group: company
  title: ''
  type: Website
  url: https://whop.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.whop.com/developer/api/getting-started
- group: commercial
  title: ''
  type: Plans
  url: plans/whop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/whop-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://whop.com/blog/
created: '2026-07-05'
description: 'Whop is a marketplace and commerce platform for selling digital products, memberships, and access to online communities, courses, software, and other creator offerings. Sellers ("companies") list products (access passes) with pricing plans, take payments, and manage member access - often gating Discord or Telegram communities, apps, and content. Whop exposes a public developer platform: a current REST API (v1) at api.whop.com/api/v1 and a GraphQL API at api.whop.com/public-graphql, covering memberships, products, plans, payments, users, companies, checkout, transfers/payouts, webhooks, and more, plus an app framework, JavaScript/Python/Ruby SDKs, OAuth, and a realtime WebSocket for apps. Whop is free to start and monetizes through transaction fees rather than a subscription for API access.'
finops:
- name: Whop Finops
  service_category: Commerce and Payments
  slug: whop-finops
graphqls:
- description: Whop exposes a public GraphQL API alongside its REST v1 API. GraphQL is
  name: Whop GraphQL API
  slug: whop-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whop.png
layout: provider
modified: '2026-07-05'
name: Whop
nav: Providers
network: true
overview: 'Whop publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Realtime WebSocket API, Checkout Configurations API, Companies API, and 8 more. Tagged areas include Memberships, Payments, Creator Economy, Marketplace, and Digital Products.


  The Whop catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Whop''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Whop Plans Pricing
  plan_count: 3
  slug: whop-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 4
  name: Whop Rate Limits
  slug: whop-rate-limits
rules:
- name: Whop API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: whop-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Whop Authentication
  slug: whop-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Whop Domain Security
  slug: whop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: whop
tags:
- Memberships
- Payments
- Creator Economy
- Marketplace
- Digital Products
- Access Control
- Commerce
website: https://whop.com
---
