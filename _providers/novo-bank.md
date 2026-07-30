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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Novo business checking account data - account identity, balances, and auth. Novo does not expose a public first-party Accounts API; account connectivity is provided through the Plaid aggregator (Asset
  name: Novo Accounts
  slug: novo-accounts
- description: Novo transaction history and categorization used for bookkeeping and reconciliation. There is no documented public Novo Transactions API; transaction data is accessed via aggregators such as Plaid, or
  name: Novo Transactions
  slug: novo-transactions
- description: Novo money movement - invoicing, ACH transfers, and faster payouts (Express ACH). These capabilities are delivered through the Novo app and partner rails; no public payments API is documented for thir
  name: Novo Payments
  slug: novo-payments
artifact_total: 9
collections:
- collection_type: open
  name: Novo API
  slug: open-novo-bank
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/novo-bank-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novo-bank-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/banknovo
- group: company
  title: ''
  type: Website
  url: https://www.novo.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.novo.co/integrations
- group: commercial
  title: ''
  type: Plans
  url: plans/novo-bank-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/novo-bank-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/novo-bank-finops.yml
created: '2026-06-20'
description: Novo is a U.S. business banking platform built for small businesses, freelancers, and self-employed professionals, offering a free business checking account, invoicing, reserves, AI-assisted bookkeeping, a business credit card, and funding. Banking services are provided by Middlesex Federal Savings, F.A. Novo does not publish a public self-service developer API; programmatic access to Novo account data is currently delivered through third-party aggregators (Plaid), and product integrations connect Novo accounts to tools like Stripe, Shopify, QuickBooks, Xero, Wise, and Square.
finops:
- name: Novo Bank Finops
  service_category: Financial Services
  slug: novo-bank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novo-bank.png
layout: provider
modified: '2026-07-25'
name: Novo
nav: Providers
network: true
overview: 'Novo publishes 3 APIs on the [APIs.io](https://apis.io/) network: Accounts, Transactions, and Payments. Tagged areas include Banking, Business Banking, Fintech, Small Business, and Freelancers.


  Novo''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Novo Bank Plans Pricing
  plan_count: 4
  slug: novo-bank-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Novo Bank Rate Limits
  slug: novo-bank-rate-limits
score:
  band: emerging
  composite: 26.3
  delta: -4.6
  facets:
    commercial_clarity: 47.4
    contract_quality: 32.3
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 30.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 13.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/novo-bank/refs/heads/main/screenshots/novo-bank-2026-06-20T190435.png
security:
- kind: domain-security
  name: Novo Bank Domain Security
  slug: novo-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Novo Bank Trust Center
  slug: novo-bank-trust-center
  summary_line: SOC 2
slug: novo-bank
tags:
- Banking
- Business Banking
- Fintech
- Small Business
- Freelancers
- Payments
website: https://www.novo.co/
---
