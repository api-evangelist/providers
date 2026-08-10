---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Homebase REST API provides programmatic access to employee scheduling, time tracking, payroll synchronization, and team management features. Authenticated via API key, it enables third-party devel
  name: Homebase API
  slug: homebase-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/homebase-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/homebase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/homebase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.joinhomebase.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.joinhomebase.com/api-docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/homebase-app
- group: company
  title: ''
  type: Blog
  url: https://www.joinhomebase.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.joinhomebase.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joinhomebase.com/
- group: other
  title: ''
  type: X
  url: https://x.com/joinhomebase
- group: operate
  title: ''
  type: Support
  url: https://support.joinhomebase.com/s/
- group: commercial
  title: ''
  type: Plans
  url: plans/homebase-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/homebase-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/homebase-finops.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/homebase-context.jsonld
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: 2026-06-12
description: Homebase is an all-in-one workforce management platform for small businesses, offering employee scheduling, time tracking, payroll, team communication, and HR tools designed for hourly teams. Founded in 2014 and headquartered in San Francisco, California, Homebase serves over 100,000 small businesses across restaurants, retail, and service industries. The platform provides a REST API that enables third-party integrations and custom applications to access scheduling, time tracking, payroll sync, and team management data. Developers can authenticate via API key obtained through the Homebase account settings portal, with the base endpoint at app.joinhomebase.com/api/public. Homebase integrates natively with major point-of-sale systems, payroll providers, and HR platforms including Square, Toast, Clover, Gusto, ADP, and QuickBooks.
finops:
- name: Homebase Finops
  service_category: ''
  slug: homebase-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/homebase.png
jsonld:
- class_count: 15
  name: Homebase Context
  property_count: 1
  slug: homebase-context
layout: provider
modified: 2026-06-12
name: Homebase
nav: Providers
network: true
overview: 'Homebase publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include scheduling, time-tracking, payroll, HR, and workforce-management.


  The Homebase catalog on APIs.io includes 1 JSON-LD context.


  Homebase''s developer surface includes documentation, engineering blog, pricing, support, and 12 more developer resources.'
plans:
- name: Homebase Plans Pricing
  plan_count: 4
  slug: homebase-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 2
  name: Homebase Rate Limits
  slug: homebase-rate-limits
score:
  band: thin
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 12.9
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 29.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/homebase/refs/heads/main/screenshots/homebase-2026-06-20T182820.png
security:
- kind: domain-security
  name: Homebase Domain Security
  slug: homebase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Homebase Vulnerability Disclosure
  slug: homebase-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Homebase Trust Center
  slug: homebase-trust-center
  summary_line: SOC 2, PCI DSS
slug: homebase
tags:
- scheduling
- time-tracking
- payroll
- HR
- workforce-management
- team-communication
- employee-scheduling
- small-business
- hourly-workers
- integrations
website: https://www.joinhomebase.com/
---
