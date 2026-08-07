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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: 'REST API for managing the full subscription lifecycle in Maxio Advanced Billing (formerly Chargify): customers, products, components, subscriptions, invoices, transactions, coupons, and webhooks. Auth'
  name: Maxio Advanced Billing API
  slug: advanced-billing-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/maxio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maxio-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wearemaxio
- group: company
  title: ''
  type: Website
  url: https://www.maxio.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.maxio.com/
- group: operate
  title: ''
  type: Help Center
  url: https://docs.maxio.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maxio-com
- group: start
  title: ''
  type: Signup
  url: https://www.maxio.com/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.maxio.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://maxio.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.maxio.com/blog
created: '2026-05-11'
description: Maxio is a SaaS billing and financial operations platform formed from the merger of Chargify and SaaSOptics, providing subscription management, recurring billing, revenue recognition, and SaaS metrics for B2B software companies. Maxio Advanced Billing (formerly Chargify) exposes a REST API for managing customers, subscriptions, products, components, invoices, and events. Authentication uses HTTP Basic auth with a per-site API key as the username.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maxio.png
layout: provider
modified: '2026-05-11'
name: Maxio
nav: Providers
network: true
overview: 'Maxio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Billing, Subscriptions, Recurring Billing, Revenue Recognition, and SaaS Metrics.


  Maxio''s developer surface includes documentation, signup flow, pricing, engineering blog, and 7 more developer resources.'
random_paper: 90
score:
  band: emerging
  composite: 14.7
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maxio/refs/heads/main/screenshots/maxio-2026-06-20T185049.png
security:
- kind: domain-security
  name: Maxio Domain Security
  slug: maxio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Maxio Trust Center
  slug: maxio-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: maxio
tags:
- Billing
- Subscriptions
- Recurring Billing
- Revenue Recognition
- SaaS Metrics
- Payments
website: https://www.maxio.com
---
