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
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: REST API providing property-level data including AVM valuations, rental value, land value, LTV, sales history, tax history, flood data, school info, and geographic features for US residential properti
  name: HouseCanary Analytics API
  slug: housecanary-analytics-api
- description: REST API for clients and partners to programmatically create valuation and inspection orders, receive status updates via webhook, export results, and download reports. Includes a sandbox environment f
  name: HouseCanary Order Manager API
  slug: housecanary-order-manager-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/housecanary-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.housecanary.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.housecanary.com/resources/developer-tools
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/housecanary
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/housecanary-inc
- group: other
  title: ''
  type: X
  url: https://twitter.com/housecanary
- group: company
  title: ''
  type: Blog
  url: https://www.housecanary.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.housecanary.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.housecanary.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/housecanary-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/housecanary-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/housecanary-finops.yml
created: 2026-06-12
description: HouseCanary is a property analytics platform providing REST APIs for automated valuation model (AVM) data, property details, rental estimates, market forecasts, and flood/risk data across more than 100 million US residential properties. The Analytics API supports property-level endpoints including value, rental value, land value, sales history, tax history, and LTV calculations accessed via HTTP Basic Authentication. The Order Manager API allows clients to programmatically order HouseCanary valuation and inspection products and receive results via webhook. HouseCanary also offers a Python SDK and a Postman collection for integration testing.
finops:
- name: Housecanary Finops
  service_category: ''
  slug: housecanary-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/housecanary.png
jsonld:
- class_count: 19
  name: Housecanary Context
  property_count: 0
  slug: housecanary-context
layout: provider
modified: 2026-06-12
name: HouseCanary
nav: Providers
network: true
overview: 'HouseCanary publishes 1 API on the [APIs.io](https://apis.io/) network: Analytics API. Tagged areas include Real Estate, Property Analytics, AVM, Valuation, and Rental Estimates.


  The HouseCanary catalog on APIs.io includes 1 JSON-LD context.


  HouseCanary''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Housecanary Plans Pricing
  plan_count: 4
  slug: housecanary-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 5
  name: Housecanary Rate Limits
  slug: housecanary-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 37.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/housecanary/refs/heads/main/screenshots/housecanary-2026-06-20T182847.png
security:
- kind: domain-security
  name: Housecanary Domain Security
  slug: housecanary-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: housecanary
tags:
- Real Estate
- Property Analytics
- AVM
- Valuation
- Rental Estimates
- Market Forecasts
- Mortgage
- Property Data
website: https://www.housecanary.com
---
