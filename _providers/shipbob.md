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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Shipbob Agentic Access
  operation_count: 72
  slug: shipbob-agentic-access
  summary_line: 72 operations · 30 acting
api_count: 10
apis:
- description: The subpackage_billing API from ShipBob — 4 operation(s) for subpackage_billing.
  name: ShipBob subpackage_billing API
  slug: shipbob-subpackage-billing-api
- description: The subpackage_channels API from ShipBob — 1 operation(s) for subpackage_channels.
  name: ShipBob subpackage_channels API
  slug: shipbob-subpackage-channels-api
- description: The subpackage_inventory API from ShipBob — 9 operation(s) for subpackage_inventory.
  name: ShipBob subpackage_inventory API
  slug: shipbob-subpackage-inventory-api
- description: The subpackage_locations API from ShipBob — 1 operation(s) for subpackage_locations.
  name: ShipBob subpackage_locations API
  slug: shipbob-subpackage-locations-api
- description: The subpackage_orders API from ShipBob — 21 operation(s) for subpackage_orders.
  name: ShipBob subpackage_orders API
  slug: shipbob-subpackage-orders-api
- description: The subpackage_products API from ShipBob — 11 operation(s) for subpackage_products.
  name: ShipBob subpackage_products API
  slug: shipbob-subpackage-products-api
- description: The subpackage_receiving API from ShipBob — 8 operation(s) for subpackage_receiving.
  name: ShipBob subpackage_receiving API
  slug: shipbob-subpackage-receiving-api
- description: The subpackage_returns API from ShipBob — 3 operation(s) for subpackage_returns.
  name: ShipBob subpackage_returns API
  slug: shipbob-subpackage-returns-api
- description: The subpackage_simulations API from ShipBob — 2 operation(s) for subpackage_simulations.
  name: ShipBob subpackage_simulations API
  slug: shipbob-subpackage-simulations-api
- description: The subpackage_webhooks API from ShipBob — 2 operation(s) for subpackage_webhooks.
  name: ShipBob subpackage_webhooks API
  slug: shipbob-subpackage-webhooks-api
artifact_total: 21
asyncapis:
- description: AsyncAPI 2.6 specification modeling the ShipBob webhook event surface. ShipBob webhooks allow applications to subscribe to events that occur in a ShipBob merchant account (order shipments, returns, wa
  name: ShipBob Webhooks
  slug: shipbob-webhooks-asyncapi
collections:
- collection_type: open
  name: API Reference
  slug: open-shipbob
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shipbob-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/shipbob-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipbob-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shipbob-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipbob.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.shipbob.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shipbob.com/pricing/
- group: other
  title: ''
  type: AppStore
  url: https://www.shipbob.com/integrations/
- group: start
  title: ''
  type: SupportPortal
  url: https://support.shipbob.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShipBob
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shipbob
- group: commercial
  title: ''
  type: Plans
  url: plans/shipbob-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shipbob-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shipbob-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.shipbob.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.shipbob.com/blog/feed/
created: '2026-05-08'
description: ShipBob is a Chicago-based global ecommerce fulfillment network and 3PL operating 60+ fulfillment centers, providing distributed warehousing, inventory, B2B/EDI, and shipping operations for direct-to-consumer brands with a developer-friendly REST API.
finops:
- name: Shipbob Finops
  service_category: Logistics
  slug: shipbob-finops
graphqls:
- description: 'ShipBob is a global ecommerce fulfillment network and third-party logistics (3PL) provider operating 60+ fulfillment centers. This conceptual GraphQL schema models the core domain objects surfaced by '
  name: ShipBob GraphQL Schema
  slug: shipbob-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipbob.png
layout: provider
modified: '2026-05-30'
name: ShipBob
nav: Providers
network: true
overview: 'ShipBob publishes 10 APIs on the [APIs.io](https://apis.io/) network, including subpackage_billing API, subpackage_channels API, subpackage_inventory API, and 7 more. Tagged areas include Logistics, Fulfillment, 3PL, Ecommerce, and Inventory.


  The ShipBob catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  ShipBob''s developer surface includes authentication, documentation, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Shipbob Plans Pricing
  plan_count: 1
  slug: shipbob-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Shipbob Rate Limits
  slug: shipbob-rate-limits
rules:
- name: ShipBob API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: shipbob-asyncapi-spectral-rules
score:
  band: developing
  composite: 47.1
  delta: -2.4
  facets:
    commercial_clarity: 47.4
    contract_quality: 69.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 26.3
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shipbob/refs/heads/main/screenshots/shipbob-2026-06-20T193812.png
security:
- kind: authentication
  name: Shipbob Authentication
  slug: shipbob-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shipbob Domain Security
  slug: shipbob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Shipbob Trust Center
  slug: shipbob-trust-center
  summary_line: SOC 2, ISO 27001
slug: shipbob
tags:
- Logistics
- Fulfillment
- 3PL
- Ecommerce
- Inventory
- Warehousing
- Shipping
- Direct-to-Consumer
website: https://www.shipbob.com/
---
