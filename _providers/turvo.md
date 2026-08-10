---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Turvo Agentic Access
  operation_count: 24
  slug: turvo-agentic-access
  summary_line: 24 operations · 13 acting
api_count: 7
apis:
- description: Customers, shippers, and business partners.
  name: Turvo Accounts API
  slug: turvo-accounts-api
- description: OAuth 2.0 token exchange for the Public API.
  name: Turvo Authentication API
  slug: turvo-authentication-api
- description: Transportation providers hauling freight.
  name: Turvo Carriers API
  slug: turvo-carriers-api
- description: Facility and address master used as shipment stops.
  name: Turvo Locations API
  slug: turvo-locations-api
- description: Customer demand records planned into shipments.
  name: Turvo Orders API
  slug: turvo-orders-api
- description: Freight loads - the core shipment object in Turvo.
  name: Turvo Shipments API
  slug: turvo-shipments-api
- description: Real-time location updates and status milestones on a shipment.
  name: Turvo Tracking API
  slug: turvo-tracking-api
artifact_total: 14
collections:
- collection_type: open
  name: Turvo Public API
  slug: open-turvo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/turvo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turvo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/turvo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/turvo
- group: company
  title: ''
  type: Website
  url: https://turvo.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.turvo.com/hc/en-us/sections/12970447299987-API-Documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/turvo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/turvo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/turvo-finops.yml
created: '2026-07-05'
description: Turvo is a collaborative cloud transportation management system (TMS) that unifies shippers, freight brokers, and carriers on a single real-time platform. Its self-service Public API is a JSON REST interface (base https://publicapi.turvo.com) secured with OAuth 2.0 plus a per-tenant API key, covering shipments, orders, locations, accounts (customers), and carriers, with event-driven webhooks for status changes and location updates. API credentials and the interactive reference are provisioned per tenant from the API profile inside the Turvo application, so the surface is self-serve for Turvo customers rather than openly public.
finops:
- name: Turvo Finops
  service_category: Logistics and Supply Chain Software
  slug: turvo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turvo.png
layout: provider
modified: '2026-07-05'
name: Turvo
nav: Providers
network: true
overview: 'Turvo publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Authentication API, Carriers API, and 4 more. Tagged areas include Logistics, Transportation Management System, TMS, Supply Chain, and Freight.


  Turvo''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Turvo Plans Pricing
  plan_count: 1
  slug: turvo-plans-pricing
random_paper: 112
rate_limits:
- limit_count: 3
  name: Turvo Rate Limits
  slug: turvo-rate-limits
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Turvo Authentication
  slug: turvo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Turvo Domain Security
  slug: turvo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: turvo
tags:
- Logistics
- Transportation Management System
- TMS
- Supply Chain
- Freight
- Shipments
- Carriers
website: https://turvo.com
---
