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
random_paper: 11
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ziro/refs/heads/main/screenshots/ziro-2026-09-02T171810.png
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
