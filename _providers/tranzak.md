---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
api_count: 4
apis:
- description: 'REST API for collecting payments from customers via mobile money (MTN MOMO, Orange Money), QR code in-store payments, and web redirect checkout. Supports direct mobile wallet charges, payment request '
  name: TranZak Payment Collections API
  slug: tranzak-payment-collections-api
- description: REST API for sending funds to Tranzak users, mobile money wallets (MTN MOMO, Orange Money), and CEMAC bank accounts. Supports single transfers, payout account top-ups, and transfer history retrieval.
  name: TranZak Transfers (Disbursements) API
  slug: tranzak-transfers-disbursements-api
- description: REST API for sending bulk payments to up to 2,000 recipients in a single request. Supports file-based upload for internal Tranzak users, mobile wallets, and bank accounts, with job status tracking and
  name: TranZak Bulk Payments API
  slug: tranzak-bulk-payments-api
- description: REST API for sending marketing bulk SMS messages and OTP/verification codes. Supports up to 500 recipients per call with per-character pricing (160 characters per SMS unit).
  name: TranZak SMS API
  slug: tranzak-sms-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tranzak-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tranzak.net/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.tranzak.me/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/HolyCorn-Software/tranzak-node
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tranzaktech
- group: company
  title: ''
  type: Blog
  url: https://community.tranzak.net/
- group: commercial
  title: ''
  type: Pricing
  url: https://tranzak.net/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://tranzak.net/
- group: other
  title: ''
  type: X
  url: https://twitter.com/tranzak_fintech
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/tranzak/refs/heads/main/plans/tranzak-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/tranzak/refs/heads/main/rate-limits/tranzak-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/tranzak/refs/heads/main/finops/tranzak-finops.yml
created: '2026-06-13'
description: TranZak is an African fintech platform headquartered in Douala, Cameroon, providing REST APIs for mobile money collections, merchant payments, bulk disbursements, bill payments, and SMS services across sub-Saharan Africa. The platform bridges banked and unbanked populations by supporting MTN Mobile Money, Orange Money, and CEMAC bank networks, with sandbox and production environments, webhook notifications, and support for up to 2,000 recipients in a single bulk payment request.
finops:
- name: Tranzak Finops
  service_category: ''
  slug: tranzak-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tranzak.png
layout: provider
modified: '2026-06-13'
name: TranZak
nav: Providers
network: true
overview: 'TranZak publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Mobile Money, Payments, Africa, and Cameroon.


  TranZak''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Tranzak Plans Pricing
  plan_count: 3
  slug: tranzak-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Tranzak Rate Limits
  slug: tranzak-rate-limits
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 7
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tranzak/refs/heads/main/screenshots/tranzak-2026-06-20T195635.png
security:
- kind: domain-security
  name: Tranzak Domain Security
  slug: tranzak-domain-security
  summary_line: TLSv1.2
slug: tranzak
tags:
- Fintech
- Mobile Money
- Payments
- Africa
- Cameroon
- Disbursements
- SMS
- Bill Payments
website: https://tranzak.net/
---
