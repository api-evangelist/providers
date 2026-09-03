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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tienda-pago-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tiendapago.com
- group: start
  title: ''
  type: SignUp
  url: https://onboarding.tiendapago.net/es-MX/auth
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tiendapago.com/es-MX/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tiendapago.com/es-MX/contract
created: '2026-07-17'
description: 'Tienda Pago is a fintech lender providing working capital and short-term inventory financing to small retailers - bodegas, convenience stores, bars and restaurants - across Mexico and Peru. Operating as a non-regulated financial entity (SOFOM E.N.R.), it offers three core products: LanaYa instant cash deposits, buy-now-pay-later 7-day terms for buying inventory from distributors, and no-upfront-cash mobile phone top-up (recargas). The platform reports serving over 80,000 businesses and more than 18 million families through mobile apps and a web onboarding portal. It is backed by QED Investors. No public API, developer portal, or SDK surface has been identified.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tienda-pago.png
layout: provider
modified: '2026-07-21'
name: Tienda Pago
nav: Providers
network: true
overview: 'Tienda Pago is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Lending, Fintech, Payments, and Working Capital.


  Tienda Pago''s developer surface includes signup flow and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tienda-pago/refs/heads/main/screenshots/tienda-pago-2026-09-02T163721.png
security:
- kind: domain-security
  name: Tienda Pago Domain Security
  slug: tienda-pago-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tienda-pago
tags:
- Company
- Lending
- Fintech
- Payments
- Working Capital
- Buy Now Pay Later
- Mexico
- Peru
- Small Business
website: https://tiendapago.com
---
