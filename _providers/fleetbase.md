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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 27
  human_in_the_loop: 1
  name: Fleetbase Agentic Access
  operation_count: 46
  slug: fleetbase-agentic-access
  summary_line: 46 operations · 27 acting · 1 human-in-the-loop
api_count: 10
apis:
- description: Customer and facilitator contacts.
  name: Fleetbase Contacts API
  slug: fleetbase-contacts-api
- description: Drivers and their assignments.
  name: Fleetbase Drivers API
  slug: fleetbase-drivers-api
- description: Groupings of drivers and vehicles.
  name: Fleetbase Fleets API
  slug: fleetbase-fleets-api
- description: Create, dispatch, and manage delivery orders.
  name: Fleetbase Orders API
  slug: fleetbase-orders-api
- description: Addressable geocoded locations.
  name: Fleetbase Places API
  slug: fleetbase-places-api
- description: Pricing rules and delivery quotes.
  name: Fleetbase Service Rates API
  slug: fleetbase-service-rates-api
- description: Tracking status and telemetry.
  name: Fleetbase Tracking API
  slug: fleetbase-tracking-api
- description: Vehicles in the fleet.
  name: Fleetbase Vehicles API
  slug: fleetbase-vehicles-api
- description: Event subscription endpoints.
  name: Fleetbase Webhooks API
  slug: fleetbase-webhooks-api
- description: Service-area geofences.
  name: Fleetbase Zones API
  slug: fleetbase-zones-api
artifact_total: 17
collections:
- collection_type: open
  name: Fleetbase API
  slug: open-fleetbase
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fleetbase-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fleetbase-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fleetbase-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fleetbase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fleetbase
- group: company
  title: ''
  type: Website
  url: https://www.fleetbase.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fleetbase.io
- group: commercial
  title: ''
  type: Plans
  url: plans/fleetbase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fleetbase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fleetbase-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://fleetbase.io/blog
created: '2026-06-21'
description: Fleetbase is an open-source, modular logistics and supply chain operating system (LSOS) for managing orders, drivers, vehicles, fleets, and last-mile delivery. Its RESTful API at https://api.fleetbase.io/v1 exposes orders, places, contacts, drivers, vehicles, fleets, zones, service rates, tracking, and webhooks, available both self-hosted under AGPL-3.0 and as a managed Fleetbase Cloud offering.
finops:
- name: Fleetbase Finops
  service_category: Logistics and Supply Chain
  slug: fleetbase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fleetbase.png
layout: provider
modified: '2026-06-21'
name: Fleetbase
nav: Providers
network: true
overview: 'Fleetbase publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Drivers API, Fleets API, and 7 more. Tagged areas include Logistics, Fleet Management, Supply Chain, Last Mile Delivery, and Open Source.


  Fleetbase''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Fleetbase Plans Pricing
  plan_count: 4
  slug: fleetbase-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 4
  name: Fleetbase Rate Limits
  slug: fleetbase-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.8
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Fleetbase Authentication
  slug: fleetbase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fleetbase Domain Security
  slug: fleetbase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fleetbase
tags:
- Logistics
- Fleet Management
- Supply Chain
- Last Mile Delivery
- Open Source
website: https://www.fleetbase.io
---
