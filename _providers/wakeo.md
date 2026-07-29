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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Wakeo Agentic Access
  operation_count: 10
  slug: wakeo-agentic-access
  summary_line: 10 operations · 4 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Register and manage tracked shipments / transport orders across sea, air, road, rail, and parcel. (Modeled.)
  name: Wakeo Shipments API
  slug: wakeo-shipments-api
- description: Predictive ETAs, positions, and milestone events for a tracked shipment. (Modeled.)
  name: Wakeo Tracking API
  slug: wakeo-tracking-api
- description: Subscriptions that push tracking and ETA updates to a customer endpoint. (Modeled.)
  name: Wakeo Webhooks API
  slug: wakeo-webhooks-api
artifact_total: 10
collections:
- collection_type: open
  name: Wakeo Visibility API (Modeled)
  slug: open-wakeo
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wakeo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wakeo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wakeo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wakeo
- group: company
  title: ''
  type: Website
  url: https://wakeo.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wakeo.co/docs/getting-started
- group: commercial
  title: ''
  type: Plans
  url: plans/wakeo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wakeo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wakeo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://wakeo.co/blog/
created: '2026-07-12'
description: Wakeo is a Paris-based SaaS platform for real-time multimodal supply-chain visibility across sea, air, road, rail, and parcel. It combines carrier, telematics, and AIS tracking data with data-science predictions to deliver predictive door-to-door ETAs, milestone events, congestion and disruption alerts, carbon-footprint reporting, and route reliability scoring. Wakeo's REST API and webhooks let customers pull transport orders and push enriched ETAs and tracking updates into a TMS, ERP, or MRP. The API is enterprise and customer-provisioned - the reference at docs.wakeo.co is behind a password wall and access is granted by Wakeo Customer Success or support@wakeo.co.
finops:
- name: Wakeo Finops
  service_category: Supply Chain Visibility
  slug: wakeo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wakeo.png
layout: provider
modified: '2026-07-12'
name: Wakeo
nav: Providers
network: true
overview: 'Wakeo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Shipments API, Tracking API, and Webhooks API. Tagged areas include Supply Chain, Transportation Visibility, Real-Time Visibility, Multimodal, and Logistics.


  Wakeo''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Wakeo Plans Pricing
  plan_count: 1
  slug: wakeo-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 2
  name: Wakeo Rate Limits
  slug: wakeo-rate-limits
score:
  band: thin
  composite: 35.3
  delta: -2.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 37.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Wakeo Authentication
  slug: wakeo-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Wakeo Domain Security
  slug: wakeo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wakeo
tags:
- Supply Chain
- Transportation Visibility
- Real-Time Visibility
- Multimodal
- Logistics
- Shipment Tracking
- ETA
- Freight
- Supply Chain Visibility
- SaaS
website: https://wakeo.co
---
