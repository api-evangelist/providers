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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Baremetrics Agentic Access
  operation_count: 14
  slug: baremetrics-agentic-access
  summary_line: 14 operations · 2 acting
api_count: 1
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
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Baremetrics Annotations API
  slug: open-baremetrics-annotations-api
- collection_type: open
  name: Baremetrics Annotations Charges API
  slug: open-baremetrics-charges-api
- collection_type: open
  name: Baremetrics Annotations Customers API
  slug: open-baremetrics-customers-api
- collection_type: open
  name: Baremetrics Annotations Events API
  slug: open-baremetrics-events-api
- collection_type: open
  name: Baremetrics Annotations Metrics API
  slug: open-baremetrics-metrics-api
- collection_type: open
  name: Baremetrics Annotations Plans API
  slug: open-baremetrics-plans-api
- collection_type: open
  name: Baremetrics Annotations Subscriptions API
  slug: open-baremetrics-subscriptions-api
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
random_paper: 14
rate_limits:
- limit_count: 1
  name: Baremetrics Rate Limits
  slug: baremetrics-rate-limits
score:
  band: developing
  composite: 39.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 54.8
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Software-as-a-Service
website: https://baremetrics.com
---
