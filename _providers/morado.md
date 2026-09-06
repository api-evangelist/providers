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
  band: agent-aware
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.6
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/morado-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.moradocolombia.com/
- group: company
  title: ''
  type: About
  url: https://www.moradocolombia.com/sobre-morado
- group: start
  title: ''
  type: SignUp
  url: https://www.moradocolombia.com/solicita-tu-credito
- group: commercial
  title: ''
  type: Pricing
  url: https://www.moradocolombia.com/tasas-y-tarifas
- group: operate
  title: ''
  type: Support
  url: https://www.moradocolombia.com/centro-de-informacion
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moradocolombia.com/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moradocolombia.com/politicas-de-privacidad
- group: agent
  title: ''
  type: MCPServer
  url: mcp/morado-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/morado-llms.txt
created: '2026-07-17'
description: Morado is a Colombian fintech and B2B marketplace for the beauty and wellness industry across Latin America, founded in 2022 by Angela Maria Acosta (an early Rappi employee). It is the "everything store for beauty shops" — giving salons, spas, and independent beauty entrepreneurs (a workforce that is majority women) access to intelligent credit, working-capital lines, inventory supply, inventory management, last-mile logistics, and digital tools through a 100% digital process, even for businesses without a traditional financial history. Credit applications run over WhatsApp with 30/60/90-day revolving lines and 3-12 month term products, serving 32,000+ micro-business clients. Backed by QED Investors, Andreessen Horowitz, Tiger Global, H20 Capital, Latitud, and Village Global. Public surface is the moradocolombia.com marketing/credit site (built on Wix) — no first-party developer API, though the Wix site exposes a hosted MCP endpoint and an llms.txt.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/morado.png
layout: provider
mcp_servers:
- description: ''
  name: Morado Wix Site MCP
  slug: morado-wix-site-mcp
modified: '2026-07-20'
name: Morado
nav: Providers
network: true
overview: 'Morado is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Fintech, Beauty, and Wellness.


  Morado''s developer surface includes signup flow, pricing, support, and 7 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 4
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
  previous_composite: 14.9
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/morado/refs/heads/main/screenshots/morado-2026-08-07T184258.png
security:
- kind: domain-security
  name: Morado Domain Security
  slug: morado-domain-security
  summary_line: TLSv1.3 · HSTS
slug: morado
tags:
- Company
- Marketplace
- Fintech
- Beauty
- Wellness
- Lending
- Credit
- Colombia
- Latin America
- B2B
website: https://www.moradocolombia.com/
---
