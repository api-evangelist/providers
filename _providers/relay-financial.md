---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: 'Online business checking and high-yield savings, with up to 20-50 checking accounts per business for envelope-style cash management. Delivered as an in-app product feature; no public developer API is '
  name: Relay Business Banking
  slug: relay-business-banking
- description: Issuance of virtual and physical Visa debit and credit cards with per-card spend limits, role-based controls, and real-time transaction tracking. Card management is an in-app feature; no public card-i
  name: Relay Cards
  slug: relay-cards
- description: Accounts payable and bill pay workflow - upload bills, route approvals, and pay vendors via ACH, check, and wire, including batch vendor payments on higher tiers. Operated through the Relay web and mo
  name: Relay Bill Pay / Accounts Payable
  slug: relay-bill-pay
- description: Native one-way data sync of transaction data and statements into accounting and back-office tools - QuickBooks Online, Xero, and Gusto - plus account data sharing to third-party money apps via Plaid a
  name: Relay Accounting Integrations
  slug: relay-accounting-integrations
artifact_total: 9
collections:
- collection_type: open
  name: Relay API
  slug: open-relay-financial
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relay-financial-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/relayfi
- group: company
  title: ''
  type: Website
  url: https://relayfi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.relayfi.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/relay-financial-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/relay-financial-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/relay-financial-finops.yml
created: '2026-06-20'
description: Relay is an online business banking and cash-flow management platform for small and medium-sized businesses, offering up to 20-50 checking accounts, virtual and physical Visa debit/credit cards, accounts payable and bill pay, and one-way data integrations with accounting and payroll tools such as QuickBooks Online, Xero, and Gusto. Banking services are provided by Thread Bank, Member FDIC. Relay does not publish a public developer API; the surfaces below are product features and inbound integrations rather than developer-facing APIs.
finops:
- name: Relay Financial Finops
  service_category: Financial Services
  slug: relay-financial-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relay-financial.png
layout: provider
modified: '2026-06-20'
name: Relay
nav: Providers
network: true
overview: 'Relay publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Business Banking, Fintech, SMB, Cash Flow, and Bill Pay.


  Relay''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Relay Financial Plans Pricing
  plan_count: 3
  slug: relay-financial-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 1
  name: Relay Financial Rate Limits
  slug: relay-financial-rate-limits
score:
  band: emerging
  composite: 19.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/relay-financial/refs/heads/main/screenshots/relay-financial-2026-06-20T192825.png
security:
- kind: domain-security
  name: Relay Financial Domain Security
  slug: relay-financial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: relay-financial
tags:
- Business Banking
- Fintech
- SMB
- Cash Flow
- Bill Pay
website: https://relayfi.com/
---
