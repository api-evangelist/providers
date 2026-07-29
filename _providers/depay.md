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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/depay-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/depay-llms.txt
- group: company
  title: ''
  type: Website
  url: https://depay.us/en/
- group: company
  title: ''
  type: Blog
  url: https://depay.us/en/blog/
- group: start
  title: ''
  type: Login
  url: https://dashboard.depay.us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/depay-us/
created: '2026-07-17'
description: Depay (Depayments S.A.) is a Latin American cross-border payment infrastructure company that connects banks, wallets, and fintechs to the region's instant payment rails through a single API integration, enabling real-time international payments with settlement in local currency. Depay bridges interoperability across PIX (Brazil), Transferencias 3.0 (Argentina), Bre-B (Colombia), QR BCR (Peru), and QR BCB (Bolivia), and offers QR-code collection products for online and in-person checkout. Founded in Buenos Aires and backed by Techstars (Payments Powered by Stellar and MoneyGram), the company raised a $4M round to expand its real-time payment network across LATAM.
image: https://depay.us/wp-content/uploads/2026/06/logo-depay.svg
layout: provider
modified: '2026-07-18'
name: Depay
nav: Providers
network: true
overview: 'Depay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Cross-Border Payments, Fintech, and Instant Payments.


  Depay''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 51
score:
  band: minimal
  composite: 8.9
  delta: -1.4
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/depay/refs/heads/main/screenshots/depay-2026-07-25T211754.png
security:
- kind: domain-security
  name: Depay Domain Security
  slug: depay-domain-security
  summary_line: TLSv1.3 · DMARC
slug: depay
tags:
- Company
- Payments
- Cross-Border Payments
- Fintech
- Instant Payments
- Latin America
- QR Payments
- Payment Infrastructure
website: https://depay.us/en/
---
