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
- acting_count: 22
  human_in_the_loop: 0
  name: Efi Bank Agentic Access
  operation_count: 34
  slug: efi-bank-agentic-access
  summary_line: 34 operations · 22 acting
api_count: 7
apis:
- description: OAuth2 client-credentials token endpoints (per host).
  name: Efí Authorization API
  slug: efi-bank-authorization-api
- description: Installment booklets. Host cobrancas.api.efipay.com.br, no mTLS.
  name: Efí Carnê API
  slug: efi-bank-carn-api
- description: Boleto / card / Pix charges. Host cobrancas.api.efipay.com.br, no mTLS.
  name: Efí Cobranças API
  slug: efi-bank-cobran-as-api
- description: Pix payment initiation via Open Finance. Host openfinance.api.efipay.com.br, mTLS required.
  name: Efí Open Finance API
  slug: efi-bank-open-finance-api
- description: Immediate (cob) and dated (cobv) Pix charges and payload locations. Host pix.api.efipay.com.br, mTLS required.
  name: Efí Pix Charges API
  slug: efi-bank-pix-charges-api
- description: Received Pix, sent Pix, and refunds. Host pix.api.efipay.com.br, mTLS required.
  name: Efí Pix Payments API
  slug: efi-bank-pix-payments-api
- description: Webhook registration for received-Pix notifications. Host pix.api.efipay.com.br, mTLS required.
  name: Efí Pix Webhooks API
  slug: efi-bank-pix-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: Efí (formerly Gerencianet) Payments API
  slug: open-efi-bank
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/efi-bank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/efi-bank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/efi-bank-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sejaefi.com.br
- group: docs
  title: ''
  type: Documentation
  url: https://dev.efipay.com.br
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/efibank
- group: commercial
  title: ''
  type: Plans
  url: plans/efi-bank-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/efi-bank-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/efi-bank-finops.yml
created: '2026-07-12'
description: Efí (formerly Gerencianet) is a Brazilian payment institution and digital bank that exposes well-documented public REST APIs for the Brazilian financial system - Pix (immediate and dated charges, send/receive, refunds, webhooks), Boletos and Charges (Cobranças), Carnê installment booklets, subscriptions and payment links, Pix via Open Finance, and account financial services. Pix and Open Finance APIs require OAuth2 client-credentials plus a mutual TLS (mTLS) client certificate as mandated by the Brazilian Central Bank; the Cobranças API uses OAuth2 without mTLS.
finops:
- name: Efi Bank Finops
  service_category: Financial Services and Payments
  slug: efi-bank-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/efi-bank.png
layout: provider
modified: '2026-07-12'
name: Efí
nav: Providers
network: true
overview: 'Efí publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Carnê API, Cobranças API, and 4 more. Tagged areas include Payments, Pix, Boleto, Banking, and Brazil.


  Efí''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Efi Bank Plans Pricing
  plan_count: 4
  slug: efi-bank-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Efi Bank Rate Limits
  slug: efi-bank-rate-limits
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.6
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
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/efi-bank/refs/heads/main/screenshots/efi-bank-2026-07-25T212946.png
security:
- kind: authentication
  name: Efi Bank Authentication
  slug: efi-bank-authentication
  summary_line: oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Efi Bank Domain Security
  slug: efi-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: efi-bank
tags:
- Payments
- Pix
- Boleto
- Banking
- Brazil
- Latin America
- Charges
- Digital Account
- Financial Infrastructure
- Fintech
website: https://sejaefi.com.br
---
