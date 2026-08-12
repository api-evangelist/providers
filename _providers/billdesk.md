---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
  pricing: enterprise
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
api_count: 3
apis:
- description: Pre-built hosted checkout solution for one-time and recurring online payments. Merchants redirect customers to BillDesk-hosted pages, minimizing PCI DSS scope.
  name: BillDesk Neo Full Redirect API
  slug: neo-payments-api
- description: SDK-based payment integration for Android, iOS, Flutter, and web. Provides embedded payment experiences with BillDesk handling payment orchestration.
  name: BillDesk Ace SDK API
  slug: ace-sdk-api
- description: Direct REST API access for advanced payment processing, giving merchants full control over checkout UX. Supports transactions, mandates, refunds, card tokenization, invoices, payment links, and settle
  name: BillDesk CX+ Deep API
  slug: cx-plus-deep-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/billdesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.billdesk.com/web/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.billdesk.io/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/billdesk
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/billdesk
- group: company
  title: ''
  type: Blog
  url: https://www.billdesk.com/web/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.billdesk.com/web/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://uptime.com/billdesk.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/billdesk
- group: commercial
  title: ''
  type: Plans
  url: plans/billdesk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/billdesk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/billdesk-finops.yml
created: '2026-06-13'
description: BillDesk is an Indian integrated payment solutions platform founded in 2000, offering REST APIs for bill payments, recurring mandates, UPI payments, net banking, card payments, and enterprise payment gateway integrations. The platform provides three integration tiers (Neo full-redirect, Ace SDK, and CX+ deep API), supporting online payments, e-Mandate setup, invoicing, refunds, tokenization, and 150+ payment methods across web, mobile, and third-party e-commerce plugins.
finops:
- name: Billdesk Finops
  service_category: ''
  slug: billdesk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/billdesk.png
layout: provider
modified: '2026-06-13'
name: BillDesk
nav: Providers
network: true
overview: 'BillDesk publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, India, Payment Gateway, UPI, and Recurring Payments.


  BillDesk''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Billdesk Plans Pricing
  plan_count: 1
  slug: billdesk-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 3
  name: Billdesk Rate Limits
  slug: billdesk-rate-limits
score:
  band: emerging
  composite: 22.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 22.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/billdesk/refs/heads/main/screenshots/billdesk-2026-06-20T173307.png
security:
- kind: domain-security
  name: Billdesk Domain Security
  slug: billdesk-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: billdesk
tags:
- Payments
- India
- Payment Gateway
- UPI
- Recurring Payments
- Mandates
- Net Banking
- Bill Payments
- Fintech
website: https://www.billdesk.com/web/
---
