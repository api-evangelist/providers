---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for managing rental properties, tenants, leases, maintenance requests, accounting, and online rent payment processing on the TenantCloud platform.
  name: TenantCloud API
  slug: tenantcloud-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tenantcloud-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/tenantcloud/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/tenantcloud/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/tenantcloud/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tenantcloud.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tenantcloud.com/
- group: company
  title: ''
  type: Blog
  url: https://www.tenantcloud.com/blog
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://support.tenantcloud.com/product_updates
- group: operate
  title: ''
  type: Support
  url: https://support.tenantcloud.com/
- group: start
  title: ''
  type: Signup
  url: https://app.tenantcloud.com/register
- group: start
  title: ''
  type: Login
  url: https://app.tenantcloud.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.api.tenantcloud.com/
created: '2026-06-13'
description: Cloud-based property management platform with a REST API for managing rentals, tenants, leases, maintenance, accounting, and online rent payment processing. The API enables landlords, property managers, and developers to automate daily tasks and build integrations on top of the TenantCloud platform.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tenantcloud.png
layout: provider
modified: '2026-06-13'
name: TenantCloud
nav: Providers
network: true
overview: 'TenantCloud publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Real Estate, Rental, Tenant Management, and Lease Management.


  TenantCloud''s developer surface includes pricing, engineering blog, release notes, support, signup flow, getting-started guide, and 6 more developer resources.'
random_paper: 65
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 28.8
  delta: -3.8
  facets:
    commercial_clarity: 31.6
    contract_quality: 32.3
    developer_ergonomics: 17.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 32.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tenantcloud/refs/heads/main/screenshots/tenantcloud-2026-06-20T195109.png
security:
- kind: domain-security
  name: Tenantcloud Domain Security
  slug: tenantcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: tenantcloud
tags:
- Property Management
- Real Estate
- Rental
- Tenant Management
- Lease Management
- Maintenance
- Accounting
- Rent Payments
---
