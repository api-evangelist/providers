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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Abacatepay Agentic Access
  operation_count: 12
  slug: abacatepay-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 1
apis:
- description: Outbound webhook event notifications (billing.created, billing.paid, billing.refunded, billing.failed, subscription.created, subscription.canceled) delivered with a webhookSecret query string and HMAC
  name: AbacatePay Webhooks
  slug: abacatepay-webhooks-api
- description: Create and list billings (charges) with a shareable checkout URL.
  name: AbacatePay Billing API
  slug: abacatepay-billing-api
- description: Create and list discount coupons.
  name: AbacatePay Coupon API
  slug: abacatepay-coupon-api
- description: Create and list customers (clients).
  name: AbacatePay Customer API
  slug: abacatepay-customer-api
- description: Create, check, and simulate dynamic Pix QR Code payments.
  name: AbacatePay Pix QR Code API
  slug: abacatepay-pix-qr-code-api
- description: Create, retrieve, and list withdrawals (payouts) to a Pix key.
  name: AbacatePay Withdraw API
  slug: abacatepay-withdraw-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AbacatePay Billing API
  slug: open-abacatepay-billing-api
- collection_type: open
  name: AbacatePay Billing Coupon API
  slug: open-abacatepay-coupon-api
- collection_type: open
  name: AbacatePay Billing Customer API
  slug: open-abacatepay-customer-api
- collection_type: open
  name: AbacatePay Billing Pix QR Code API
  slug: open-abacatepay-pix-qr-code-api
- collection_type: open
  name: AbacatePay Billing Withdraw API
  slug: open-abacatepay-withdraw-api
- collection_type: open
  name: AbacatePay API
  slug: open-abacatepay
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/abacatepay-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abacatepay-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/abacatepay-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AbacatePay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abacatepay
- group: company
  title: ''
  type: Website
  url: https://www.abacatepay.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.abacatepay.com
- group: commercial
  title: ''
  type: Plans
  url: plans/abacatepay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/abacatepay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/abacatepay-finops.yml
created: '2026-06-21'
description: AbacatePay is a Brazilian payment gateway built for developers and indie hackers, focused on instant Pix payments. Its REST API lets you create billings and charges, generate and check Pix QR Codes, manage customers and coupons, request withdrawals, and receive webhooks - charging a flat per-transaction Pix fee with funds available immediately.
finops:
- name: Abacatepay Finops
  service_category: Payment Processing
  slug: abacatepay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/abacatepay.png
layout: provider
modified: '2026-06-21'
name: AbacatePay
nav: Providers
network: true
overview: 'AbacatePay publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Coupon API, Customer API, and 2 more. Tagged areas include Payments, Pix, Brazil, Fintech, and Developers.


  AbacatePay''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Abacatepay Plans Pricing
  plan_count: 2
  slug: abacatepay-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Abacatepay Rate Limits
  slug: abacatepay-rate-limits
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 9
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 57.8
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/abacatepay/refs/heads/main/screenshots/abacatepay-2026-07-25T181328.png
security:
- kind: authentication
  name: Abacatepay Authentication
  slug: abacatepay-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Abacatepay Domain Security
  slug: abacatepay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: abacatepay
tags:
- Payments
- Pix
- Brazil
- Fintech
- Developers
website: https://www.abacatepay.com
---
