---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Rent Manager Web API (WAPI12) is a RESTful API that provides both read and write access to the Rent Manager Online (RMO) database. It supports property management operations including tenants, lea
  name: Rent Manager Web API
  slug: rent-manager-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rent-manager-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rentmanager.com
- group: docs
  title: ''
  type: Documentation
  url: https://uprop.api.rentmanager.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.rentmanager.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rentmanager.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lcs.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rentmanager
- group: other
  title: ''
  type: X
  url: https://x.com/RentManager
- group: operate
  title: ''
  type: Support
  url: https://www.rentmanager.com/support/
- group: operate
  title: ''
  type: APISupport
  url: https://www.rentmanager.com/submit-api-support-request/
- group: commercial
  title: ''
  type: Plans
  url: plans/rent-manager-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rent-manager-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rent-manager-finops.yml
created: '2026-06-13'
description: Rent Manager is property management software with a REST API (WAPI12) for managing properties, tenants, leases, work orders, accounting, billing, and maintenance workflows for residential and commercial portfolios. The API provides both read and write access to the Rent Manager Online (RMO) database, enabling integration with 200+ PropTech partner solutions.
finops:
- name: Rent Manager Finops
  service_category: ''
  slug: rent-manager-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rent-manager.png
jsonld:
- class_count: 0
  name: Rent Manager Context
  property_count: 8
  slug: rent-manager-context
layout: provider
modified: '2026-06-13'
name: Rent Manager
nav: Providers
network: true
overview: 'Rent Manager publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Real Estate, Tenants, Leases, and Work Orders.


  The Rent Manager catalog on APIs.io includes 1 JSON-LD context.


  Rent Manager''s developer surface includes documentation, engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Rent Manager Plans Pricing
  plan_count: 5
  slug: rent-manager-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 0
  name: Rent Manager Rate Limits
  slug: rent-manager-rate-limits
score:
  band: emerging
  composite: 24.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 24.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rent-manager/refs/heads/main/screenshots/rent-manager-2026-06-20T192855.png
security:
- kind: domain-security
  name: Rent Manager Domain Security
  slug: rent-manager-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rent-manager
tags:
- Property Management
- Real Estate
- Tenants
- Leases
- Work Orders
- Accounting
- Maintenance
- Residential
- Commercial
- HOA
- Multifamily
website: https://www.rentmanager.com
---
