---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_commerce: false
    auth_clarity: false
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
  score: 15.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'RESTful API providing access to all Rentvine property management data including properties, units, leases, tenants, maintenance requests, work orders, financials, owner accounts, and portals. Enables '
  name: Rentvine REST API
  slug: rentvine-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentvine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rentvine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rentvine.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rentvine.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rentvine.com/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rentvine
- group: other
  title: ''
  type: X
  url: https://twitter.com/Rentvine_
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Launch-Engine/rentvine
- group: design
  title: ''
  type: JSONLD
  url: json-ld/rentvine.json
- group: commercial
  title: ''
  type: Plans
  url: plans/rentvine-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rentvine-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rentvine-finops.yml
created: 2026-06-13
description: Rentvine is a modern property management platform offering a fully open RESTful API for managing properties, leases, tenants, maintenance requests, financials, and owner portals. The API provides real-time data access and supports custom integrations, workflow automation, and third-party software connectivity. API access is included with all subscriptions at no additional cost, with no usage restrictions or rate limit quotas published.
finops:
- name: Rentvine Finops
  service_category: ''
  slug: rentvine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rentvine.png
layout: provider
modified: 2026-06-13
name: Rentvine
nav: Providers
network: true
overview: 'Rentvine publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Property Management, Real-Estate, Leasing, Tenant Management, and Maintenance.


  Rentvine''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Rentvine Plans Pricing
  plan_count: 1
  slug: rentvine-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Rentvine Rate Limits
  slug: rentvine-rate-limits
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 7
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rentvine/refs/heads/main/screenshots/rentvine-2026-06-20T192858.png
security:
- kind: domain-security
  name: Rentvine Domain Security
  slug: rentvine-domain-security
  summary_line: TLSv1.2 · DMARC
slug: rentvine
tags:
- Property Management
- Real-Estate
- Leasing
- Tenant Management
- Maintenance
- Trust Accounting
- Owner Portals
- REST API
website: https://www.rentvine.com/
---
