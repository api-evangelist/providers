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
  url: security/cometa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cometaedu.com
- group: company
  title: ''
  type: Blog
  url: https://cometaedu.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cometaedu.com/terminos-y-condiciones
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cometaedu.com/privacidad-web
- group: operate
  title: ''
  type: Support
  url: https://api.whatsapp.com/send/?phone=5215532452644
- group: start
  title: ''
  type: SignUp
  url: https://cometaedu.com/solicitar-demo
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cometa-llms.txt
created: '2026-07-17'
description: 'Cometa (getcometa.com / cometaedu.com) is a Mexican education technology company that provides an operating system for private schools. More than 500 private schools in Mexico use Cometa to run and automate their operations across a set of integrated modules: Cobranzas (tuition collections with WhatsApp and email payment reminders and dashboards), Tienda en linea (an online store for uniforms, materials and services with vendor management), Admisiones y Reinscripciones (admissions and re-enrollment workflows), Comunicaciones (AI-assisted, multi-channel family communications with engagement analytics), Calificaciones (grade entry and SEP-compliant report cards and digital credentials), and Gestion Escolar (attendance, incident logging and administrative workflows). Cometa is a 500 Global portfolio company. It was surfaced as a stub in the API Evangelist network for enrichment; as of this pass Cometa publishes no public API, developer portal, or machine-readable API documentation
  surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cometa.png
layout: provider
modified: '2026-07-18'
name: Cometa
nav: Providers
network: true
overview: 'Cometa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, School Management, and Software-as-a-Service.


  Cometa''s developer surface includes engineering blog, support, signup flow, and 5 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 13.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cometa/refs/heads/main/screenshots/cometa-2026-07-25T210113.png
security:
- kind: domain-security
  name: Cometa Domain Security
  slug: cometa-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cometa
tags:
- Company
- Education
- EdTech
- School Management
- Software-as-a-Service
- Admissions
- Tuition Collections
- Communications
- Payments
- Mexico
website: https://cometaedu.com
---
