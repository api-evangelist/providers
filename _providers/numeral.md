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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-24'
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
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Numeral Customers API
  slug: open-numeral-customers-api
- collection_type: open
  name: Numeral Customers Health API
  slug: open-numeral-health-api
- collection_type: open
  name: Numeral Customers Products API
  slug: open-numeral-products-api
- collection_type: open
  name: Numeral Customers Refunds API
  slug: open-numeral-refunds-api
- collection_type: open
  name: Numeral Customers Tax Calculations API
  slug: open-numeral-tax-calculations-api
- collection_type: open
  name: Numeral Customers Transactions API
  slug: open-numeral-transactions-api
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
overview: 'Numeral publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Health API, Products API, and 3 more. Tagged areas include Sales Tax, Tax Compliance, Tax Calculation, E-Commerce, and Software-as-a-Service.


  Numeral''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Numeral Plans Pricing
  plan_count: 3
  slug: numeral-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Numeral Rate Limits
  slug: numeral-rate-limits
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 50.3
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 35.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/numeral/refs/heads/main/screenshots/numeral-2026-08-07T185732.png
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
- E-Commerce
- Software-as-a-Service
website: https://www.numeral.com/
---
