---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 5
apis:
- description: Open Finance Brasil endpoints registered by Nubank in the Central Bank directory. Provides consent-driven access to account, credit-card, loan, and payment-initiation data for authorised TPPs under th
  name: Nubank Open Finance Brasil API
  slug: open-finance
- description: 'REST API for creating and managing NuPay checkout orders, querying payment status, cancelling unpaid orders, and processing refunds for completed transactions. Built for Brazilian merchants accepting '
  name: NuPay for Business - Checkout API
  slug: nupay-checkout
- description: OAuth2 app-based authorization, CIBA (Client-Initiated Backchannel Authentication) for web flows, OTP validation, and token issuance / refresh for NuPay merchant integrations.
  name: NuPay for Business - Authentication API
  slug: nupay-auth
- description: Register, query, and version final beneficiaries on NuPay orders with document validation across CPF, CNPJ, and international identifier types.
  name: NuPay for Business - Beneficiary Management API
  slug: nupay-beneficiaries
- description: Signed webhook callbacks delivering payment-status and refund-status updates to merchant-configured endpoints. Includes signature validation headers so merchants can verify NuPay as the sender.
  name: NuPay for Business - Event Webhooks
  slug: nupay-webhook
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nubank-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nubank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nubank.com.br/
- group: company
  title: ''
  type: Investor Relations
  url: https://investors.nu/
- group: company
  title: ''
  type: Engineering Blog
  url: https://building.nubank.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/nubank
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nubank
- group: other
  title: ''
  type: Open Finance Directory
  url: https://openfinance.dev.br/provider/Nubank
- group: docs
  title: ''
  type: NuPay Documentation
  url: https://docs.nupaybusiness.com.br/
created: '2026-05-23'
description: Nu Holdings (Nubank) is Latin America's largest digital bank, with tens of millions of customers across Brazil, Mexico, and Colombia. Its core product surface - credit card, account, lending, investments, and insurance - is consumer-facing through the Nu mobile app, and Nubank does not publish a general-purpose public developer portal. Nubank participates in Brazil's Open Finance (Open Banking Brasil) regime, which standardises consent-driven access to account, transaction, and payment-initiation APIs for authorised third parties; Nubank's Open Finance endpoints are registered with the Brazilian Central Bank's directory. For merchant acceptance, Nubank operates NuPay for Business, a REST API for checkout payments, refunds, OAuth2/CIBA-based authorization, beneficiary management, and webhook event notifications, hosted at api.spinpay.com.br.
finops:
- name: Nubank Finops
  service_category: API
  slug: nubank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nubank.png
layout: provider
modified: '2026-05-23'
name: Nu (Nubank)
nav: Providers
network: true
overview: 'Nu (Nubank) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Neobank, Banking, Credit Cards, Open Finance, and Payments.


  Nu (Nubank)''s developer surface includes GitHub presence and 8 more developer resources.'
plans:
- name: Nubank Plans Pricing
  plan_count: 1
  slug: nubank-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 2
  name: Nubank Rate Limits
  slug: nubank-rate-limits
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 15.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nubank/refs/heads/main/screenshots/nubank-2026-06-20T190506.png
security:
- kind: domain-security
  name: Nubank Domain Security
  slug: nubank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nubank Vulnerability Disclosure
  slug: nubank-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nubank
tags:
- Neobank
- Banking
- Credit Cards
- Open Finance
- Payments
- Brazil
- Mexico
- Colombia
- Latin America
website: https://nubank.com.br/
---
