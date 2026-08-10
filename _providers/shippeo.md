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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Shippeo Agentic Access
  operation_count: 11
  slug: shippeo-agentic-access
  summary_line: 11 operations · 5 acting
api_count: 4
apis:
- description: Retrieve predictive ETAs, statuses, and milestone events (Events-out, pull).
  name: Shippeo ETA and Status API
  slug: shippeo-eta-and-status-api
- description: Manage webhook subscriptions for real-time Events-out notifications.
  name: Shippeo Event Subscriptions API
  slug: shippeo-event-subscriptions-api
- description: Feed and retrieve geolocation positions for tracked transports.
  name: Shippeo Positions API
  slug: shippeo-positions-api
- description: Submit and manage transport orders (tours) for real-time tracking.
  name: Shippeo Transport Orders API
  slug: shippeo-transport-orders-api
artifact_total: 11
collections:
- collection_type: open
  name: Shippeo Real-Time Transportation Visibility API
  slug: open-shippeo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/shippeo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shippeo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shippeo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.shippeo.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shippeo.com
- group: start
  title: ''
  type: SignUp
  url: https://developers.shippeo.com
- group: operate
  title: ''
  type: StatusPage
  url: https://shippeo.statuspage.io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/shippeo
- group: commercial
  title: ''
  type: Plans
  url: plans/shippeo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/shippeo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/shippeo-finops.yml
created: '2026-07-12'
description: Shippeo is a real-time transportation and multimodal supply-chain visibility platform, giving shippers, carriers, and logistics teams predictive and real-time information for all their deliveries across road, rail, sea, and air. Through its developer portal (developers.shippeo.com) Shippeo exposes REST APIs and webhooks so TMS, ERP, and control-tower systems can submit transport orders (tours) for tracking, feed GPS positions, retrieve predictive ETAs, statuses, and milestone events, and subscribe to real-time "Events-out" notifications. API access is enterprise and customer-provisioned - applications and OAuth2 client IDs are created in the portal after contracting with Shippeo.
finops:
- name: Shippeo Finops
  service_category: Supply Chain Visibility
  slug: shippeo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/shippeo.png
layout: provider
modified: '2026-07-12'
name: Shippeo
nav: Providers
network: true
overview: 'Shippeo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including ETA and Status API, Event Subscriptions API, Positions API, and 1 more. Tagged areas include Supply Chain, Transportation Visibility, Real-Time Visibility, Logistics, and Shipment Tracking.


  Shippeo''s developer surface includes authentication, documentation, signup flow, and 8 more developer resources.'
plans:
- name: Shippeo Plans Pricing
  plan_count: 1
  slug: shippeo-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 3
  name: Shippeo Rate Limits
  slug: shippeo-rate-limits
score:
  band: thin
  composite: 41.8
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Shippeo Authentication
  slug: shippeo-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Shippeo Domain Security
  slug: shippeo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shippeo
tags:
- Supply Chain
- Transportation Visibility
- Real-Time Visibility
- Logistics
- Shipment Tracking
- ETA
- Freight
- Supply Chain Visibility
- SaaS
website: https://www.shippeo.com
---
