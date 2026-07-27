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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Shipday Agentic Access
  operation_count: 11
  slug: shipday-agentic-access
  summary_line: 11 operations · 9 acting
api_count: 4
apis:
- description: The Assignment API from Shipday — 2 operation(s) for assignment.
  name: Shipday Assignment API
  slug: shipday-assignment-api
- description: The Drivers API from Shipday — 2 operation(s) for drivers.
  name: Shipday Drivers API
  slug: shipday-drivers-api
- description: The On-Demand Delivery API from Shipday — 2 operation(s) for on-demand delivery.
  name: Shipday On-Demand Delivery API
  slug: shipday-on-demand-delivery-api
- description: The Orders API from Shipday — 3 operation(s) for orders.
  name: Shipday Orders API
  slug: shipday-orders-api
artifact_total: 11
collections:
- collection_type: open
  name: Shipday API
  slug: open-shipday
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shipday-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shipday-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shipday-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shipday
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shipday
- group: company
  title: ''
  type: Website
  url: https://www.shipday.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shipday.com
- group: commercial
  title: ''
  type: Plans
  url: plans/shipday-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shipday-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shipday-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.shipday.com/blog
created: '2026-06-21'
description: Shipday is a local delivery management platform for restaurants, retailers, and on-demand businesses. Its REST API lets you create and track delivery and pickup orders, manage drivers (carriers), assign orders to your own fleet, and tap a network of on-demand delivery providers (Uber, DoorDash) for last-mile fulfillment, with webhooks for real-time order and driver-location updates.
finops:
- name: Shipday Finops
  service_category: Logistics and Delivery Management
  slug: shipday-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shipday.png
layout: provider
modified: '2026-06-21'
name: Shipday
nav: Providers
network: true
overview: 'Shipday publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assignment API, Drivers API, On-Demand Delivery API, and 1 more. Tagged areas include Delivery, Logistics, Last Mile, Local Delivery, and Dispatch.


  Shipday''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Shipday Plans Pricing
  plan_count: 5
  slug: shipday-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Shipday Rate Limits
  slug: shipday-rate-limits
score:
  band: thin
  composite: 39.4
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.9
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Shipday Authentication
  slug: shipday-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shipday Domain Security
  slug: shipday-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shipday
tags:
- Delivery
- Logistics
- Last Mile
- Local Delivery
- Dispatch
website: https://www.shipday.com
---
