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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The Rentec Direct Open API v3 provides RESTful access to property management data including properties, tenants, leases, payments, maintenance requests, contacts, and messaging. Available to Pro and P
  name: Rentec Direct Open API
  slug: rentec-direct-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentec-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/rentec/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/rentec/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/rentec/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rentecdirect.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.rentecdirect.com/blog/
- group: operate
  title: ''
  type: Status
  url: https://status.rentecdirect.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rentecdirect.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rentecdirect.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://help.rentecdirect.com/
- group: operate
  title: ''
  type: Contact
  url: https://www.rentecdirect.com/contact/
- group: company
  title: ''
  type: BlogPosts
  url: https://raw.githubusercontent.com/api-evangelist/rentec/refs/heads/main/blogs/blogs.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/rentec/refs/heads/main/json-ld/rentec-direct.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/rentec/refs/heads/main/json-ld/rentec-direct-api.json
created: '2026-06-13'
description: Rentec Direct provides property management software with a REST API for managing rental properties, tenant screening, online payments, maintenance requests, and financial reporting. The Open API (v3) is available to all Pro and PM plan subscribers at no additional cost, enabling workflow automation, data analysis, and custom application development.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rentec.png
layout: provider
modified: '2026-06-13'
name: Rentec Direct
nav: Providers
network: true
overview: 'Rentec Direct publishes 1 API on the [APIs.io](https://apis.io/) network: Open API. Tagged areas include Property Management, Real Estate, Rental, Tenant Screening, and Payments.


  Rentec Direct''s developer surface includes pricing, engineering blog, status page, support, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 29
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 33.6
  delta: -0.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 37.7
    developer_ergonomics: 6.5
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 34.2
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 30.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rentec/refs/heads/main/screenshots/rentec-2026-06-20T192855.png
security:
- kind: domain-security
  name: Rentec Domain Security
  slug: rentec-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rentec
tags:
- Property Management
- Real Estate
- Rental
- Tenant Screening
- Payments
- Maintenance
- Financial Reporting
---
