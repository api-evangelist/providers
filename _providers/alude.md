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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alude-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alude.com.br/
- group: start
  title: ''
  type: SignUp
  url: https://app.alude.com.br
- group: start
  title: ''
  type: Login
  url: https://app.alude.com.br
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alude.com.br/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.alude.com.br/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alude.com.br/termos-de-uso-de-politica-de-privacidade-e-de-tratamento-de-dados-pessoais.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.alude.com.br/termos-de-uso-de-politica-de-privacidade-e-de-tratamento-de-dados-pessoais.pdf
created: '2026-07-17'
description: Alude is a Brazilian proptech (real estate technology) SaaS platform that digitizes the day-to-day operations of imobiliárias (real estate agencies), brokers, and property managers. Serving more than 20,000 agencies, the platform bundles rental management with automated payment collection and reporting, instant CPF/CNPJ tenant background screening (análise de ficha), legally valid electronic signatures without digital certificates, fast fire-insurance (seguro incêndio) issuance, automated property capture and lead generation, and capitalization bonds as an alternative to traditional rental deposits. Alude is LGPD-compliant, free to try without a credit card, and backed by Ribbit Capital, Y Combinator, Global Founders Capital, and MAYA Capital. It operates as an end-to-end web application rather than a public API-first product; no developer portal, OpenAPI, or public API surface was found during enrichment.
image: https://cdn.sanity.io/images/68gmuo7j/landing_page/36d11cb4cee1c9d002e42c9f8a0fe5c4129f3335-89x18.svg
layout: provider
modified: '2026-07-17'
name: Alude
nav: Providers
network: true
overview: 'Alude is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-Estate, PropTech, Software-as-a-Service, and Property Management.


  Alude''s developer surface includes signup flow, pricing, engineering blog, and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alude/refs/heads/main/screenshots/alude-2026-07-25T195855.png
security:
- kind: domain-security
  name: Alude Domain Security
  slug: alude-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alude
tags:
- Company
- Real-Estate
- PropTech
- Software-as-a-Service
- Property Management
- Rental Management
- Electronic Signature
- Insurance
- Brazil
- Fintech
website: https://www.alude.com.br/
---
