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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Shipday Agentic Access
  operation_count: 11
  slug: shipday-agentic-access
  summary_line: 11 operations · 9 acting
api_count: 1
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
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Shipday Assignment API
  slug: open-shipday-assignment-api
- collection_type: open
  name: Shipday Assignment Drivers API
  slug: open-shipday-drivers-api
- collection_type: open
  name: Shipday Assignment On-Demand Delivery API
  slug: open-shipday-on-demand-delivery-api
- collection_type: open
  name: Shipday Assignment Orders API
  slug: open-shipday-orders-api
- collection_type: open
  name: Shipday API
  slug: open-shipday
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/shipday-capability-edges.yml
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


  Shipday''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Shipday Plans Pricing
  plan_count: 5
  slug: shipday-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Shipday Rate Limits
  slug: shipday-rate-limits
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 27.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
