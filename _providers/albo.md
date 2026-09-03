---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  url: security/albo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.albo.com/
- group: operate
  title: ''
  type: Support
  url: https://ayuda.albo.mx/hc/es-419
- group: commercial
  title: ''
  type: Pricing
  url: https://www.albo.com/albo/costos-y-comisiones.html
- group: start
  title: ''
  type: SignUp
  url: https://onboarding.albo.live/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.albo.com/albo/terminos-y-condiciones.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.albo.com/albo/aviso-de-privacidad.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/albomx/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/albomx
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCBG0r1P06VUp8XrbN_OPNpA
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/albo-llms.txt
coverage:
  checked: '2026-08-06'
  detail: Albo ships only end-user apps — every developer-shaped hostname (api., developers., developer., docs., business., negocios. on both albo.com and albo.mx) fails to resolve, and the Webflow marketing site answers 404 for /openapi.json, /llms.txt, /api-docs and every /.well-known/ path.
  evidence:
  - status: 0
    url: https://developers.albo.com/
  - status: 0
    url: https://api.albo.mx/
  - status: 404
    url: https://www.albo.com/openapi.json
  - status: 404
    url: https://www.albo.com/.well-known/agent-card.json
  - status: 404
    url: https://www.albo.com/developers
  reason: no-developer-program
  state: none
created: '2026-08-06'
description: 'Albo (albo.com, formerly albo.mx) is a Mexican digital financial services company founded in 2016 and operating since 2022 as an Institución de Fondos de Pago Electrónico (IFPE) authorized by the Comisión Nacional Bancaria y de Valores (CNBV) and regulated by Banco de México. Albo ships a mobile-first personal account with a Mastercard debit card — SPEI transfers, bill payments, cash deposit and withdrawal at partner locations, and real-time notifications — alongside "albo empresa", a business account for payroll, employee cards, and bulk dispersion of up to 3,000 transactions at a time. Adjacent credit (abea, by Aureo Lab) and crypto (albit, by Indigo DeFi) products are offered by independent partners. Albo publishes no public developer program: no developer portal, API reference, OpenAPI/AsyncAPI specification, SDK, webhook catalog, or sandbox was found on any albo.com, albo.mx or albo.live host.'
image: https://cdn.prod.website-files.com/6a0bcc576e3f8669b332d482/6a456f99a236466733228c78_logo_albo.png
layout: provider
modified: '2026-08-06'
name: Albo
nav: Providers
network: true
overview: 'Albo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Financial-Services, Fintech, and Neobank.


  Albo''s developer surface includes support, pricing, signup flow, YouTube channel, and 7 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/albo/refs/heads/main/screenshots/albo-2026-08-07T161145.png
security:
- kind: domain-security
  name: Albo Domain Security
  slug: albo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: albo
tags:
- Company
- Banking
- Financial-Services
- Fintech
- Neobank
- Digital Banking
- Payments
- Mexico
- Latin America
- Consumer Finance
website: https://www.albo.com/
---
