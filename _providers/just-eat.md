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
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-08-11'
api_count: 24
apis:
- description: The Attempted Delivery API API from Just Eat — 2 operation(s) for attempted delivery api.
  name: Just Eat Attempted Delivery API API
  slug: just-eat-attempted-delivery-api-api
- description: The Attempted Delivery Webhooks API from Just Eat — 2 operation(s) for attempted delivery webhooks.
  name: Just Eat Attempted Delivery Webhooks API
  slug: just-eat-attempted-delivery-webhooks-api
- description: The Checkout API from Just Eat — 2 operation(s) for checkout.
  name: Just Eat Checkout API
  slug: just-eat-checkout-api
- description: The Consumer Queries Webhooks API from Just Eat — 2 operation(s) for consumer queries webhooks.
  name: Just Eat Consumer Queries Webhooks API
  slug: just-eat-consumer-queries-webhooks-api
- description: The ConsumerQueries API from Just Eat — 2 operation(s) for consumerqueries.
  name: Just Eat ConsumerQueries API
  slug: just-eat-consumerqueries-api
- description: The Consumers API from Just Eat — 4 operation(s) for consumers.
  name: Just Eat Consumers API
  slug: just-eat-consumers-api
- description: The Delivery Pools API API from Just Eat — 5 operation(s) for delivery pools api.
  name: Just Eat Delivery Pools API API
  slug: just-eat-delivery-pools-api-api
- description: The DeliveryFee API from Just Eat — 1 operation(s) for deliveryfee.
  name: Just Eat DeliveryFee API
  slug: just-eat-deliveryfee-api
- description: The Order Acceptance API API from Just Eat — 7 operation(s) for order acceptance api.
  name: Just Eat Order Acceptance API API
  slug: just-eat-order-acceptance-api-api
- description: The Order Acceptance Webhooks API from Just Eat — 5 operation(s) for order acceptance webhooks.
  name: Just Eat Order Acceptance Webhooks API
  slug: just-eat-order-acceptance-webhooks-api
- description: The Order API API from Just Eat — 1 operation(s) for order api.
  name: Just Eat Order API API
  slug: just-eat-order-api-api
- description: The Order Delivery API API from Just Eat — 10 operation(s) for order delivery api.
  name: Just Eat Order Delivery API API
  slug: just-eat-order-delivery-api-api
- description: The Order Delivery Webhooks API from Just Eat — 8 operation(s) for order delivery webhooks.
  name: Just Eat Order Delivery Webhooks API
  slug: just-eat-order-delivery-webhooks-api
- description: The Order Webhooks API from Just Eat — 3 operation(s) for order webhooks.
  name: Just Eat Order Webhooks API
  slug: just-eat-order-webhooks-api
- description: The publicly-accessible API from Just Eat — 85 operation(s) for publicly-accessible.
  name: Just Eat publicly-accessible API
  slug: just-eat-publicly-accessible-api
- description: The Restaurant Claims API from Just Eat — 4 operation(s) for restaurant claims.
  name: Just Eat Restaurant Claims API
  slug: just-eat-restaurant-claims-api
- description: The Restaurant Events API from Just Eat — 2 operation(s) for restaurant events.
  name: Just Eat Restaurant Events API
  slug: just-eat-restaurant-events-api
- description: The Restaurant Events Webhooks API from Just Eat — 2 operation(s) for restaurant events webhooks.
  name: Just Eat Restaurant Events Webhooks API
  slug: just-eat-restaurant-events-webhooks-api
- description: The Restaurant OrderTimes API from Just Eat — 2 operation(s) for restaurant ordertimes.
  name: Just Eat Restaurant OrderTimes API
  slug: just-eat-restaurant-ordertimes-api
- description: The Restaurant Webhooks API from Just Eat — 2 operation(s) for restaurant webhooks.
  name: Just Eat Restaurant Webhooks API
  slug: just-eat-restaurant-webhooks-api
- description: The RestaurantQueries API from Just Eat — 1 operation(s) for restaurantqueries.
  name: Just Eat RestaurantQueries API
  slug: just-eat-restaurantqueries-api
- description: The RestaurantQueries Webhooks API from Just Eat — 1 operation(s) for restaurantqueries webhooks.
  name: Just Eat RestaurantQueries Webhooks API
  slug: just-eat-restaurantqueries-webhooks-api
- description: The Restaurants API from Just Eat — 15 operation(s) for restaurants.
  name: Just Eat Restaurants API
  slug: just-eat-restaurants-api
- description: The Search API from Just Eat — 2 operation(s) for search.
  name: Just Eat Search API
  slug: just-eat-search-api
artifact_total: 28
asyncapis:
- description: ''
  name: Just Eat Webhooks
  slug: just-eat-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/just-eat-uk-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/just-eat-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/just-eat-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/just-eat-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/just-eat-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/just-eat-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/just-eat-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/just-eat-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/just-eat-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/just-eat-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/just-eat-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.just-eat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://uk.api.just-eat.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://uk.api.just-eat.io/docs/jetconnect/index.html
- group: company
  title: ''
  type: Blog
  url: https://tech.justeattakeaway.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/justeattakeaway
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.justeattakeaway.com/privacy-statement/
- group: company
  title: ''
  type: Website
  url: http://www.just-eat.com/
created: '2026-07-17'
description: 'Just Eat Takeaway.com is a leading global online food-delivery marketplace, formed by the 2020 merger of Just Eat and Takeaway.com and headquartered in Amsterdam. It connects consumers with local restaurants and a last-mile delivery network across the UK, Europe, Australia/New Zealand and North America. Its public developer surface (developers.just-eat.com) exposes the Just Eat UK API for restaurant discovery and search, product catalogue and menu ingestion, order-lifecycle management, delivery-state tracking, checkout and basket, and consumer communication preferences, plus specialised partner integrations: JET Connect (point-of-sale) and JET Go (delivery as a service). Order-lifecycle and delivery-state events are pushed to partners through an extensive webhook surface, including async webhooks that use a callback URL.'
image: https://logo.clearbit.com/just-eat.com
layout: provider
mcp_servers:
- description: ''
  name: just-eat-mcp.yml
  slug: just-eat-mcpyml
modified: '2026-07-19'
name: Just Eat
nav: Providers
network: true
overview: 'Just Eat publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Attempted Delivery API API, Attempted Delivery Webhooks API, Checkout API, and 21 more. Tagged areas include Food Delivery, Restaurants, Marketplace, Logistics, and Orders.


  The Just Eat catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Just Eat''s developer surface includes authentication, documentation, API reference, engineering blog, and 15 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 37.9
  delta: -0.6
  facets:
    commercial_clarity: 10.5
    contract_quality: 65.5
    developer_ergonomics: 40.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 38.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Just Eat Authentication
  slug: just-eat-authentication
  summary_line: apiKey/http/openIdConnect · 4 schemes
- kind: domain-security
  name: Just Eat Domain Security
  slug: just-eat-domain-security
  summary_line: TLSv1.2 · DMARC
slug: just-eat
tags:
- Food Delivery
- Restaurants
- Marketplace
- Logistics
- Orders
- Delivery
- Point of Sale
- E-commerce
website: http://www.just-eat.com/
---
