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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nelo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nelo.mx
- group: operate
  title: ''
  type: Support
  url: https://nelo.mx/es/preguntas-frecuentes
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nelo.mx/es/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nelo.mx/es/legal/privacy
created: '2026-07-17'
description: 'Nelo is a Mexican fintech offering consumer credit that lets shoppers buy now and pay later in bi-weekly installments (quincenas). Its mobile app (iOS and Android) provides instant credit approval, an in-app marketplace (Tienda Nelo), bill payment for utilities such as CFE, water, gas and internet, phone recharges, cash withdrawals, and a premium Nelo VIP tier with a physical credit card. Backed by Homebrew, Nelo operates primarily as a consumer mobile product and, as of this enrichment pass, publishes no public developer API, developer portal, or API documentation. Sector: fintech / buy-now-pay-later (BNPL).'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nelo.png
layout: provider
modified: '2026-07-20'
name: Nelo
nav: Providers
network: true
overview: 'Nelo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, BNPL, Consumer Credit, and Payments.


  Nelo''s developer surface includes support and 4 more developer resources.'
random_paper: 82
score:
  band: minimal
  composite: 11.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nelo/refs/heads/main/screenshots/nelo-2026-08-07T184825.png
security:
- kind: domain-security
  name: Nelo Domain Security
  slug: nelo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nelo
tags:
- Company
- Fintech
- BNPL
- Consumer Credit
- Payments
- Mexico
- Mobile App
website: https://www.nelo.mx
---
