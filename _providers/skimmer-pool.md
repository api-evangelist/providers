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
- acting_count: 22
  human_in_the_loop: 0
  name: Skimmer Pool Agentic Access
  operation_count: 50
  slug: skimmer-pool-agentic-access
  summary_line: 50 operations · 22 acting
api_count: 9
apis:
- description: Pools and other bodies of water Skimmer services.
  name: Skimmer Bodies of Water API
  slug: skimmer-pool-bodies-of-water-api
- description: Pool-service customers and their activity logs.
  name: Skimmer Customers API
  slug: skimmer-pool-customers-api
- description: Invoices and billable service activity.
  name: Skimmer Invoices API
  slug: skimmer-pool-invoices-api
- description: Product catalog, categories, and prices.
  name: Skimmer Products API
  slug: skimmer-pool-products-api
- description: Sales quotes / estimates.
  name: Skimmer Quotes API
  slug: skimmer-pool-quotes-api
- description: Technician routes of service stops by date.
  name: Skimmer Routes API
  slug: skimmer-pool-routes-api
- description: Physical service sites; the unit Skimmer bills on.
  name: Skimmer Service Locations API
  slug: skimmer-pool-service-locations-api
- description: Account users - owners, admins, and technicians.
  name: Skimmer Users API
  slug: skimmer-pool-users-api
- description: Repair and service jobs, and work order types.
  name: Skimmer Work Orders API
  slug: skimmer-pool-work-orders-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/skimmer-pool-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skimmer-pool-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skimmer-pool-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.getskimmer.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skimmer-pool-service-software
- group: docs
  title: ''
  type: Documentation
  url: https://devportal.getskimmer.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://devportal.getskimmer.com/api
- group: start
  title: ''
  type: SignUp
  url: https://www.getskimmer.com/enterprise
- group: commercial
  title: ''
  type: Plans
  url: plans/skimmer-pool-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skimmer-pool-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/skimmer-pool-finops.yml
created: '2026-07-04'
description: Skimmer is pool-service business management software (customers, bodies of water, service stops and routes, work orders, quotes, invoices, and billing) used by residential and commercial pool-service companies. Skimmer exposes a real, documented public REST API at https://publicapi.getskimmer.com, with a Zudoku-based developer portal at https://devportal.getskimmer.com. The API is enterprise-oriented and access is sales-led - it is available only on Skimmer's top ("Owning the Market" / Enterprise) tier and provisioned through Skimmer's sales team rather than self-service signup. Authentication is via a per-account skimmer-api-key request header, and the API is rate limited to 500 requests per minute per key.
finops:
- name: Skimmer Pool Finops
  service_category: Business Application Software
  slug: skimmer-pool-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skimmer-pool.png
layout: provider
modified: '2026-07-04'
name: Skimmer
nav: Providers
network: true
overview: 'Skimmer publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Bodies of Water API, Customers API, Invoices API, and 6 more. Tagged areas include Pool Service, Field Service Management, Pool Maintenance, Scheduling, and Routes.


  Skimmer''s developer surface includes authentication, documentation, API reference, signup flow, and 7 more developer resources.'
plans:
- name: Skimmer Pool Plans Pricing
  plan_count: 3
  slug: skimmer-pool-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 1
  name: Skimmer Pool Rate Limits
  slug: skimmer-pool-rate-limits
score:
  band: thin
  composite: 38.1
  delta: -2.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 48.9
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Skimmer Pool Authentication
  slug: skimmer-pool-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Skimmer Pool Domain Security
  slug: skimmer-pool-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skimmer-pool
tags:
- Pool Service
- Field Service Management
- Pool Maintenance
- Scheduling
- Routes
- Work Orders
- Invoicing
- Vertical SaaS
website: https://www.getskimmer.com
---
