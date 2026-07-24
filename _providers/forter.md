---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Forter Agentic Access
  operation_count: 8
  slug: forter-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 4
apis:
- description: Signup and login (account takeover) decisions.
  name: Forter Accounts API
  slug: forter-accounts-api
- description: Data-subject profile access for privacy and compliance.
  name: Forter Data Privacy API
  slug: forter-data-privacy-api
- description: Chargeback disputes and customer compensation requests.
  name: Forter Disputes API
  slug: forter-disputes-api
- description: Order and checkout fraud/abuse decisions and order status.
  name: Forter Orders API
  slug: forter-orders-api
artifact_total: 11
collections:
- collection_type: open
  name: Forter API
  slug: open-forter
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forter-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forter-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/forter
- group: company
  title: ''
  type: Website
  url: https://www.forter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.forter.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/forter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/forter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/forter-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.forter.com/blog/
created: '2026-07-12'
description: Forter is a fraud prevention and digital identity platform for online commerce. Its Decision API returns real-time trust-or-not decisions for orders, payments, account signups, and logins, drawing on a global identity graph and machine learning trained across a large network of merchants. Beyond fraud management, Forter covers chargeback recovery, abuse prevention, payment optimization, 3DS orchestration, and identity protection. Access is enterprise / contact-sales - API credentials (a per-account site ID and API key) are provisioned by Forter during onboarding, and requests are sent to a dedicated per-tenant host.
finops:
- name: Forter Finops
  service_category: Fraud Prevention and Identity
  slug: forter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forter.png
layout: provider
modified: '2026-07-12'
name: Forter
nav: Providers
network: true
overview: 'Forter publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Data Privacy API, Disputes API, and 1 more. Tagged areas include Fraud Detection, Fraud Prevention, Identity, Trust, and Payments.


  Forter''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Forter Plans Pricing
  plan_count: 1
  slug: forter-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 2
  name: Forter Rate Limits
  slug: forter-rate-limits
score:
  band: thin
  composite: 33.6
  delta: -1.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 61.1
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.9
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Forter Authentication
  slug: forter-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Forter Domain Security
  slug: forter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: forter
tags:
- Fraud Detection
- Fraud Prevention
- Identity
- Trust
- Payments
- Chargebacks
- Account Protection
- E-commerce
- Risk
- Machine Learning
website: https://www.forter.com/
---
