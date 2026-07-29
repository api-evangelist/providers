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
  url: security/ziro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://somosziro.com
- group: start
  title: ''
  type: Login
  url: https://creditos.somosziro.com/iniciar-sesion
- group: start
  title: ''
  type: SignUp
  url: https://somosziro.com/eres-un-proveedor
- group: commercial
  title: ''
  type: Pricing
  url: https://somosziro.com/tasas-y-tarifas
- group: commercial
  title: ''
  type: TermsOfService
  url: https://somosziro.com/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://somosziro.com/politica-de-privacidad
- group: operate
  title: ''
  type: Support
  url: https://wa.me/+573142051091
created: '2026-07-17'
description: Zíro (somosziro.com) is a Colombian fintech that provides interest-free credit for small retailers in the traditional commerce channel. Its platform lets distributors and manufacturers extend "crédito sin intereses" to the small shops they supply, while the supplier receives guaranteed payment and Zíro assumes the credit risk. The service bundles identity verification (Colombian cédula), automated credit evaluation, and fraud prevention into the ordering flow. Zíro is a 500 Global portfolio company. As of this enrichment pass the company exposes only a public marketing site and a customer-facing credit application (an Angular SPA at creditos.somosziro.com); no public developer portal, API documentation, OpenAPI/AsyncAPI specification, SDK, or MCP server was found. The api.somosziro.com host exists but responds 403 (internal, not publicly documented).
image: https://framerusercontent.com/assets/NCIFcinoQHWuuNY6cFUiOPXsarM.png
layout: provider
modified: '2026-07-21'
name: Ziro
nav: Providers
network: true
overview: 'Ziro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Credit, Lending, and Embedded Finance.


  Ziro''s developer surface includes signup flow, pricing, support, and 5 more developer resources.'
random_paper: 67
score:
  band: emerging
  composite: 15.9
  delta: -2.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Ziro Domain Security
  slug: ziro-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ziro
tags:
- Company
- Fintech
- Credit
- Lending
- Embedded Finance
- Payments
- SMB
- Colombia
- Latin America
website: https://somosziro.com
---
