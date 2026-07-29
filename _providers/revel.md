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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for the Revel Systems iPad POS platform, covering orders, payments, products, inventory, customers, employees, scheduling, cash management, discounts, tax, tables, purchase orders, house acco
  name: Revel Systems API
  slug: revel-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://revelsystems.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.revelsystems.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/letsrevel
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revel-systems
- group: company
  title: ''
  type: Blog
  url: https://revelsystems.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://revelsystems.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.revelsystems.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/RevelSystems
- group: commercial
  title: ''
  type: Plans
  url: plans/revel-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revel-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/revel-finops.yml
- group: operate
  title: ''
  type: Support
  url: https://support.revelsystems.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.revelsystems.com/s/article/Revel-Systems-Change-Log
created: '2026-06-13'
description: Revel Systems is an iPad-based point-of-sale platform for restaurants and retail businesses. Its REST API provides programmatic access to menus, orders, inventory, loyalty programs, customer data, employee scheduling, cash management, and business analytics. The API supports approximately 140 public endpoints and returns responses in JSON. Authentication uses either API key/secret headers or Bearer tokens via OAuth 2.0 client credentials. Revel is now part of Shift4 Payments.
finops:
- name: Revel Finops
  service_category: ''
  slug: revel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revel.png https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-06-13'
name: Revel Systems
nav: Providers
network: true
overview: 'Revel Systems publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include POS, Point of Sale, Restaurant, Retail, and iPad.


  Revel Systems'' developer surface includes documentation, engineering blog, pricing, support, changelog, and 9 more developer resources.'
plans:
- name: Revel Plans Pricing
  plan_count: 2
  slug: revel-plans-pricing
random_paper: 68
rate_limits:
- limit_count: 0
  name: Revel Rate Limits
  slug: revel-rate-limits
score:
  band: emerging
  composite: 20.6
  delta: -2.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revel/refs/heads/main/screenshots/revel-2026-06-20T193052.png
security:
- kind: domain-security
  name: Revel Domain Security
  slug: revel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revel
tags:
- POS
- Point of Sale
- Restaurant
- Retail
- iPad
- Orders
- Inventory
- Loyalty
- Payments
website: https://revelsystems.com/
---
