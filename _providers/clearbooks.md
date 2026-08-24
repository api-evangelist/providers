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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: RESTful API for integrating with Clear Books accounting software to manage invoices, payments, contacts, bank transactions, and expenses.
  name: Clear Books REST API
  slug: clear-books-rest-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearbooks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clearbooks.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.clearbooks.co.uk/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/clearbooks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clear-books
- group: company
  title: ''
  type: Blog
  url: https://www.clearbooks.co.uk/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clearbooks.co.uk/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clearbooks.co.uk/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ClearBooks
- group: commercial
  title: ''
  type: Plans
  url: plans/clearbooks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clearbooks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clearbooks-finops.yml
created: '2026-06-13'
description: Clear Books is UK cloud accounting software with a REST API for managing invoices, expenses, bank transactions, contacts, reports, and tax submissions for small businesses.
finops:
- name: Clearbooks Finops
  service_category: ''
  slug: clearbooks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clearbooks.png
jsonld:
- class_count: 28
  name: Clearbooks Context
  property_count: 27
  slug: clearbooks-context
layout: provider
modified: '2026-06-13'
name: Clear Books
nav: Providers
network: true
overview: 'Clear Books publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Invoicing, Finance, UK, and Small Business.


  The Clear Books catalog on APIs.io includes 1 JSON-LD context.


  Clear Books'' developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Clearbooks Plans Pricing
  plan_count: 8
  slug: clearbooks-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Clearbooks Rate Limits
  slug: clearbooks-rate-limits
score:
  band: thin
  composite: 27.7
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 15.5
    developer_ergonomics: 11.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 27.7
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clearbooks/refs/heads/main/screenshots/clearbooks-2026-06-20T174457.png
security:
- kind: domain-security
  name: Clearbooks Domain Security
  slug: clearbooks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clearbooks
tags:
- Accounting
- Invoicing
- Finance
- UK
- Small Business
- MTD
- Tax
website: https://www.clearbooks.co.uk/
---
