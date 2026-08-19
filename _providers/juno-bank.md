---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/juno-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://juno.com.br
- group: start
  title: ''
  type: Portal
  url: https://dev.juno.com.br
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/autorizacao/
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/cobrancas/
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/pix/
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/pagamento/
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/assinatura/
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/notificacoes/
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/saldo/
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/technicalTerms/
- group: docs
  title: ''
  type: Documentation
  url: https://integracao.juno.com.br/docs/perguntas-frequentes/
- group: company
  title: ''
  type: Blog
  url: https://blog.juno.com.br
- group: start
  title: ''
  type: Signup
  url: https://app.juno.com.br/#/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tamojuno
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tamojuno/direct-checkout-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tamojuno/direct-checkout-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tamojuno/direct-checkout-flutter
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tamojuno/juno-marketplace
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/juno-pagamentos
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/junopagamentos
- group: other
  title: ''
  type: Company
  url: https://www.ebanx.com
- group: operate
  title: ''
  type: PressRelease
  url: https://business.ebanx.com/en/press-room/press-releases/ebanx-acquires-b2b-fintech-juno-in-brazil
created: '2026-05-25'
description: Juno is a Brazilian B2B payments fintech, acquired by EBANX in October 2021, that provides a complete billing and payments platform for Brazilian companies. Founded in 2014 in Maringá, Paraná, Juno powers more than 35,000 small and medium businesses with online sales and collections via Pix, boleto bancário, boleto_pix, and credit cards, plus marketplace payment split, recurring subscriptions, and a digital business account (Conta Juno) with Banking-as-a-Service capabilities. Juno is a participant of the Brazilian Interbank Payments Chamber (CIP). The company exposes a public REST API v2 through the Juno Developer Academy at integracao.juno.com.br, secured with OAuth 2.0 client_credentials, plus HMAC-SHA256 signed webhooks and native mobile Direct Checkout SDKs for Android and iOS for PCI-safe card data encryption.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/juno-bank.png
layout: provider
modified: '2026-05-25'
name: Juno
nav: Providers
network: true
overview: 'Juno is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Billing, Subscriptions, PIX, and Boleto.


  Juno''s developer surface includes developer portal, documentation, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 10.9
  delta: -3.5
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 32.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 14.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Juno Bank Domain Security
  slug: juno-bank-domain-security
  summary_line: no transport/DNS hardening detected
slug: juno-bank
tags:
- Payments
- Billing
- Subscriptions
- PIX
- Boleto
- Boleto Pix
- Credit Cards
- Marketplace
- Payment Split
- Banking as a Service
- Digital Account
- Webhooks
- Brazil
- Fintech
- EBANX
website: https://juno.com.br
---
