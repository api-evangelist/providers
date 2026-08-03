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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Creem Agentic Access
  operation_count: 22
  slug: creem-agentic-access
  summary_line: 22 operations · 13 acting
api_count: 7
apis:
- description: The Checkouts API from Creem — 1 operation(s) for checkouts.
  name: Creem Checkouts API
  slug: creem-checkouts-api
- description: The Customers API from Creem — 2 operation(s) for customers.
  name: Creem Customers API
  slug: creem-customers-api
- description: The Discounts API from Creem — 2 operation(s) for discounts.
  name: Creem Discounts API
  slug: creem-discounts-api
- description: The Licenses API from Creem — 3 operation(s) for licenses.
  name: Creem Licenses API
  slug: creem-licenses-api
- description: The Products API from Creem — 2 operation(s) for products.
  name: Creem Products API
  slug: creem-products-api
- description: The Subscriptions API from Creem — 7 operation(s) for subscriptions.
  name: Creem Subscriptions API
  slug: creem-subscriptions-api
- description: The Transactions API from Creem — 2 operation(s) for transactions.
  name: Creem Transactions API
  slug: creem-transactions-api
artifact_total: 15
collections:
- collection_type: open
  name: Creem API
  slug: open-creem
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/creem-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/creem-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/creem-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/creem-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/armitage-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/creem-io
- group: company
  title: ''
  type: Website
  url: https://www.creem.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.creem.io
- group: commercial
  title: ''
  type: Plans
  url: plans/creem-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/creem-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/creem-finops.yml
created: '2026-06-21'
description: Creem is a merchant-of-record payments platform built for SaaS and AI startups. Its REST API handles products, hosted checkouts, customers, subscriptions, transactions, discounts, and software license keys, while Creem acts as the merchant of record to manage global sales tax, VAT, fraud, and compliance on the seller's behalf.
finops:
- name: Creem Finops
  service_category: Payments and Billing
  slug: creem-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/creem.png
layout: provider
modified: '2026-06-21'
name: Creem
nav: Providers
network: true
overview: 'Creem publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Checkouts API, Customers API, Discounts API, and 4 more. Tagged areas include Payments, Merchant of Record, Subscriptions, SaaS, and Billing.


  Creem''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Creem Plans Pricing
  plan_count: 1
  slug: creem-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 1
  name: Creem Rate Limits
  slug: creem-rate-limits
score:
  band: thin
  composite: 34.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 28.1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/creem/refs/heads/main/screenshots/creem-2026-07-25T210726.png
security:
- kind: authentication
  name: Creem Authentication
  slug: creem-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Creem Domain Security
  slug: creem-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Creem Vulnerability Disclosure
  slug: creem-vulnerability-disclosure
  summary_line: disclosure policy published
slug: creem
tags:
- Payments
- Merchant of Record
- Subscriptions
- SaaS
- Billing
website: https://www.creem.io/
---
