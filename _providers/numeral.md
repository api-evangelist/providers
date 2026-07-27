---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
- acting_count: 10
  human_in_the_loop: 0
  name: Numeral Agentic Access
  operation_count: 16
  slug: numeral-agentic-access
  summary_line: 16 operations · 10 acting
api_count: 9
apis:
- description: 'Sales-tax return filing and remittance (Autofile) across all US states, driven by recorded transactions. Filing and remittance are delivered as managed platform services rather than self-serve public '
  name: Numeral Filings API
  slug: filings
- description: State sales-tax registration (Autoregister) and physical/economic nexus monitoring with state-crossing alerts. Provided as managed platform services on top of API-captured transaction data rather than
  name: Numeral Registrations & Nexus API
  slug: registrations-nexus
- description: Event notifications for compliance and transaction lifecycle changes (e.g., filing, registration, and nexus events). Webhook delivery is offered through the Numeral platform; no public webhook subscri
  name: Numeral Webhooks
  slug: webhooks
- description: The Customers API from Numeral — 2 operation(s) for customers.
  name: Numeral Customers API
  slug: numeral-customers-api
- description: The Health API from Numeral — 1 operation(s) for health.
  name: Numeral Health API
  slug: numeral-health-api
- description: The Products API from Numeral — 2 operation(s) for products.
  name: Numeral Products API
  slug: numeral-products-api
- description: The Refunds API from Numeral — 3 operation(s) for refunds.
  name: Numeral Refunds API
  slug: numeral-refunds-api
- description: The Tax Calculations API from Numeral — 2 operation(s) for tax calculations.
  name: Numeral Tax Calculations API
  slug: numeral-tax-calculations-api
- description: The Transactions API from Numeral — 2 operation(s) for transactions.
  name: Numeral Transactions API
  slug: numeral-transactions-api
artifact_total: 16
collections:
- collection_type: open
  name: Numeral API
  slug: open-numeral
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/numeral-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/numeral-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/numeral-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/numeralhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/numeralhq
- group: company
  title: ''
  type: Website
  url: https://www.numeral.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.numeral.com/api-reference/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/numeral-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/numeral-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/numeral-finops.yml
created: '2026-06-21'
description: Numeral (Numeral HQ) is a sales-tax compliance and automation platform for ecommerce and SaaS companies. Its REST API calculates real-time sales tax by customer location at state, county, city, and district granularity, records transactions and refunds, and manages products and customers, while the broader platform handles registrations, nexus monitoring, filing, and remittance. Not to be confused with Numeral (numeral.io), an unrelated payment-operations company now part of Mambu.
finops:
- name: Numeral Finops
  service_category: Tax and Compliance
  slug: numeral-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/numeral.png
layout: provider
modified: '2026-06-21'
name: Numeral
nav: Providers
network: true
overview: 'Numeral publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Health API, Products API, and 3 more. Tagged areas include Sales Tax, Tax Compliance, Tax Calculation, Ecommerce, and SaaS.


  Numeral''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Numeral Plans Pricing
  plan_count: 3
  slug: numeral-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Numeral Rate Limits
  slug: numeral-rate-limits
score:
  band: thin
  composite: 37.6
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 49.6
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Numeral Authentication
  slug: numeral-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Numeral Domain Security
  slug: numeral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: numeral
tags:
- Sales Tax
- Tax Compliance
- Tax Calculation
- Ecommerce
- SaaS
website: https://www.numeral.com/
---
