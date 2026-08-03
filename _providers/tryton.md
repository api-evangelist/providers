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
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: RESTful API for Tryton ERP providing access to all business modules including financial accounting, stock/inventory, sales, purchasing, and production. Supports standard HTTP methods with JSON payload
  name: Tryton REST API
  slug: tryton-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tryton-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tryton.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tryton.org/latest/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/tryton
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/groups/1313967
- group: company
  title: ''
  type: Blog
  url: https://discuss.tryton.org/c/news/25
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tryton.org/
- group: other
  title: ''
  type: X
  url: https://x.com/TrytonSoftware
- group: commercial
  title: ''
  type: Plans
  url: plans/tryton-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tryton-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tryton-finops.yml
created: '2026-06-13'
description: Tryton is an open-source three-tier ERP (Enterprise Resource Planning) platform built on Python and PostgreSQL, designed for companies of any size. It provides REST APIs for managing a comprehensive suite of business modules including financial accounting, inventory and stock management, purchasing, sales, production, and project management. The REST API supports standard CRUD operations (GET, POST, PUT, DELETE) with JSON responses, user application authentication, context headers for localization, pagination via Range headers, and domain filtering via query parameters. Tryton is licensed under GPL v3 and free to use.
finops:
- name: Tryton Finops
  service_category: ''
  slug: tryton-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tryton.png
layout: provider
modified: '2026-06-13'
name: Tryton
nav: Providers
network: true
overview: 'Tryton publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include ERP, Enterprise Resource Planning, Accounting, Inventory, and Sales.


  Tryton''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Tryton Plans Pricing
  plan_count: 2
  slug: tryton-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Tryton Rate Limits
  slug: tryton-rate-limits
score:
  band: emerging
  composite: 25.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tryton/refs/heads/main/screenshots/tryton-2026-06-20T195813.png
security:
- kind: domain-security
  name: Tryton Domain Security
  slug: tryton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tryton
tags:
- ERP
- Enterprise Resource Planning
- Accounting
- Inventory
- Sales
- Purchasing
- Production
- Project Management
- Open Source
website: https://www.tryton.org/
---
