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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Tattle describes an open, REST-based API and an API-first design ("Modern REST APIs with comprehensive documentation for custom integrations") enabling two-way data synchronization with restaurant POS
  name: Tattle Open API
  slug: rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tattle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://get.tattleapp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://get.tattleapp.com/integrations/
- group: start
  title: ''
  type: Login
  url: https://gettattle.com/dashboard
- group: commercial
  title: ''
  type: Pricing
  url: https://get.tattleapp.com/pricing/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/gettattle
- group: operate
  title: ''
  type: Support
  url: https://get.tattleapp.com/resources/faq/
- group: company
  title: ''
  type: Blog
  url: https://get.tattleapp.com/blog/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gettattle
- group: other
  title: ''
  type: X
  url: https://x.com/gettattle
- group: commercial
  title: ''
  type: Plans
  url: plans/tattle-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tattle-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tattle-finops.yml
created: '2026-06-02'
description: Tattle is an AI-powered Customer Experience Improvement (CXI) platform built for hospitality, supporting 220+ restaurant and hospitality brands across 11,000+ locations globally — including Chili's, MOD Pizza, Hooters, Freddy's, Mellow Mushroom, and The Halal Guys. It collects real-time guest feedback at the point of transaction across ordering channels, then turns it into actionable insights with smart analytics, an AI Coach that delivers each general manager monthly action plans tied to their own guest feedback and SOPs, guest-recovery tools, cross-platform review management, and item-level menu performance tracking. Pricing is per location per month, starting at $59/location. Tattle markets an open, REST-based, API-first design and integrates with 34+ restaurant technology platforms across POS, online ordering, loyalty/CRM, and kiosk categories — such as Olo, Toast, PAR Brink, Square, Punchh, Paytronix, Revel, Thanx, and Checkmate. Public, self-service API reference documentation
  is not published; the open API and custom integrations are coordinated through Tattle's integrations team (customersuccess@gettattle.com).
finops:
- name: Tattle Finops
  service_category: Customer Experience / Guest Feedback (SaaS)
  slug: tattle-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tattle.png
layout: provider
modified: '2026-06-03'
name: Tattle
nav: Providers
network: true
overview: 'Tattle publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, Guest Feedback, Customer Experience, Review Management, and Analytics.


  Tattle''s developer surface includes documentation, pricing, GitHub presence, support, engineering blog, and 8 more developer resources.'
plans:
- name: Tattle Plans Pricing
  plan_count: 6
  slug: tattle-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 2
  name: Tattle Rate Limits
  slug: tattle-rate-limits
score:
  band: emerging
  composite: 25.0
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 25.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tattle/refs/heads/main/screenshots/tattle-2026-06-20T194928.png
security:
- kind: domain-security
  name: Tattle Domain Security
  slug: tattle-domain-security
  summary_line: TLSv1.3
slug: tattle
tags:
- Restaurant
- Guest Feedback
- Customer Experience
- Review Management
- Analytics
- Integrations
website: https://get.tattleapp.com/
---
