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
- description: GraphQL API providing programmatic access to Wave accounting features including businesses, customers, invoices, products, accounts, transactions, vendors, taxes, and webhooks.
  name: Wave Financial GraphQL API
  slug: wave-financial-graphql-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wave-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.waveapps.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.waveapps.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/waveapps
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/waveapps
- group: company
  title: ''
  type: Blog
  url: https://www.waveapps.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.waveapps.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.waveapps.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/wave_financial
- group: commercial
  title: ''
  type: Plans
  url: plans/wave-financial-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wave-financial-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wave-financial-finops.yml
created: 2026-06-13
description: Free accounting software for small businesses with a GraphQL API for managing invoices, estimates, customers, products, accounts, and financial reporting. The API uses OAuth 2.0 for authentication and supports operations for businesses, customers, invoices, transactions, vendors, taxes, and webhooks.
finops:
- name: Wave Financial Finops
  service_category: ''
  slug: wave-financial-finops
graphqls:
- description: Wave Financial provides a public GraphQL API for programmatic access to its small-business accounting and invoicing platform. The API covers core business data including businesses, customers, invoice
  name: Wave Financial GraphQL API
  slug: wave-financial-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wave-financial.png
layout: provider
modified: 2026-06-13
name: Wave Financial
nav: Providers
network: true
overview: 'Wave Financial publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Invoicing, Financial, Small Business, and Bookkeeping.


  Wave Financial''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Wave Financial Plans Pricing
  plan_count: 3
  slug: wave-financial-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Wave Financial Rate Limits
  slug: wave-financial-rate-limits
score:
  band: thin
  composite: 33.6
  delta: 7.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 26.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/wave-financial/refs/heads/main/screenshots/wave-financial-2026-06-20T201254.png
security:
- kind: domain-security
  name: Wave Financial Domain Security
  slug: wave-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: wave-financial
tags:
- Accounting
- Invoicing
- Financial
- Small Business
- Bookkeeping
- Payments
website: https://www.waveapps.com
---
