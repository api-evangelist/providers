---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Baremetrics Agentic Access
  operation_count: 14
  slug: baremetrics-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 7
apis:
- description: The Annotations API from Baremetrics — 2 operation(s) for annotations.
  name: Baremetrics Annotations API
  slug: baremetrics-annotations-api
- description: The Charges API from Baremetrics — 2 operation(s) for charges.
  name: Baremetrics Charges API
  slug: baremetrics-charges-api
- description: The Customers API from Baremetrics — 2 operation(s) for customers.
  name: Baremetrics Customers API
  slug: baremetrics-customers-api
- description: The Events API from Baremetrics — 1 operation(s) for events.
  name: Baremetrics Events API
  slug: baremetrics-events-api
- description: The Metrics API from Baremetrics — 1 operation(s) for metrics.
  name: Baremetrics Metrics API
  slug: baremetrics-metrics-api
- description: The Plans API from Baremetrics — 2 operation(s) for plans.
  name: Baremetrics Plans API
  slug: baremetrics-plans-api
- description: The Subscriptions API from Baremetrics — 2 operation(s) for subscriptions.
  name: Baremetrics Subscriptions API
  slug: baremetrics-subscriptions-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/baremetrics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/baremetrics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/baremetrics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://baremetrics.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.baremetrics.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/baremetrics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/baremetrics
- group: company
  title: ''
  type: Blog
  url: https://baremetrics.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://baremetrics.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.baremetrics.com
- group: other
  title: ''
  type: X
  url: https://x.com/baremetrics
- group: commercial
  title: ''
  type: Plans
  url: plans/baremetrics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/baremetrics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/baremetrics-finops.yml
created: '2026-06-13'
description: Baremetrics is a subscription analytics platform providing a REST API for accessing MRR, ARR, churn rate, LTV, customer metrics, and revenue forecasting data from Stripe and other billing sources. It helps subscription businesses track, analyze, and improve financial performance with real-time dashboards and automated reporting.
finops:
- name: Baremetrics Finops
  service_category: ''
  slug: baremetrics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/baremetrics.png
layout: provider
modified: '2026-06-13'
name: Baremetrics
nav: Providers
network: true
overview: 'Baremetrics publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Annotations API, Charges API, Customers API, and 4 more. Tagged areas include Subscription Analytics, MRR, ARR, Churn Rate, and LTV.


  Baremetrics'' developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Baremetrics Plans Pricing
  plan_count: 3
  slug: baremetrics-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Baremetrics Rate Limits
  slug: baremetrics-rate-limits
score:
  band: thin
  composite: 44.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.1
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 44.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/baremetrics/refs/heads/main/screenshots/baremetrics-2026-06-20T173000.png
security:
- kind: authentication
  name: Baremetrics Authentication
  slug: baremetrics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Baremetrics Domain Security
  slug: baremetrics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: baremetrics
tags:
- Subscription Analytics
- MRR
- ARR
- Churn Rate
- LTV
- Revenue
- Stripe
- Financial Metrics
- SaaS
website: https://baremetrics.com
---
