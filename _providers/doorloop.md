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
- description: REST API for DoorLoop property management software. Provides access to properties, units, leases, tenants, rent collection, maintenance requests, accounting, and tenant communication. Authenticated vi
  name: DoorLoop API
  slug: doorloop-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/doorloop-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/doorloop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.doorloop.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.doorloop.com/reference/introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/mezbahalam/doorloop
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/doorloop/
- group: company
  title: ''
  type: Blog
  url: https://www.doorloop.com/blogs/doorloop
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doorloop.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doorloop.com
- group: other
  title: ''
  type: X
  url: https://x.com/doorloopapp
- group: commercial
  title: ''
  type: Plans
  url: plans/doorloop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/doorloop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/doorloop-finops.yml
created: '2026-06-13'
description: DoorLoop is property management software with a REST API for managing properties, units, leases, rent collection, maintenance requests, accounting, and tenant communication. The API provides two-way access to read and write data across nearly every DoorLoop feature, with predictable resource-oriented URLs, JSON-encoded request and response bodies, and standard HTTP response codes. API access is included on the Premium plan.
finops:
- name: Doorloop Finops
  service_category: ''
  slug: doorloop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doorloop.png
layout: provider
modified: '2026-06-13'
name: DoorLoop
nav: Providers
network: true
overview: 'DoorLoop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Real Estate, Leases, Rent Collection, and Maintenance.


  DoorLoop''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Doorloop Plans Pricing
  plan_count: 4
  slug: doorloop-plans-pricing
random_paper: 87
rate_limits:
- limit_count: 0
  name: Doorloop Rate Limits
  slug: doorloop-rate-limits
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 21.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/screenshots/doorloop-2026-06-20T180153.png
security:
- kind: domain-security
  name: Doorloop Domain Security
  slug: doorloop-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Doorloop Vulnerability Disclosure
  slug: doorloop-vulnerability-disclosure
  summary_line: disclosure policy published
slug: doorloop
tags:
- Property Management
- Real Estate
- Leases
- Rent Collection
- Maintenance
- Accounting
- Tenant Communication
website: https://www.doorloop.com
---
