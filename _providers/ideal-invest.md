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
  url: security/ideal-invest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pravaler.com.br/
- group: company
  title: ''
  type: About
  url: https://www.pravaler.com.br/sobre-o-pravaler/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.pravaler.com.br/financiamento-estudantil/
- group: company
  title: ''
  type: Blog
  url: https://www.pravaler.com.br/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.pravaler.com.br/ajuda/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.pravaler.com.br/ajuda/
- group: start
  title: ''
  type: SignUp
  url: https://cadastro.pravaler.com.br/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pravaler.com.br/politica-de-privacidade/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ideal-invest-llms.txt
created: '2026-07-17'
description: Ideal Invest (operating as Pravaler) is a Brazilian fintech founded in 2002 and headquartered in Sao Paulo that provides private student financing for higher education. Through its Pravaler platform, students can split tuition payments across roughly twice the duration of a course, with a 100% digital, low-bureaucracy application, competitive monthly interest rates, and no ENEM requirement. Pravaler works with a network of 500+ partner higher-education institutions and has financed more than 400,000 students, channeling over R$12 billion into Brazilian education. The company is backed by Ribbit Capital. As of this enrichment pass Pravaler exposes a consumer web platform (simulation, application, digital signature) but publishes no public developer API, OpenAPI, SDK, or partner integration surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ideal-invest.png
layout: provider
modified: '2026-07-19'
name: Ideal Invest
nav: Providers
network: true
overview: 'Ideal Invest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Student Financing, Lending, and Education.


  Ideal Invest''s developer surface includes getting-started guide, engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 12.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ideal-invest/refs/heads/main/screenshots/ideal-invest-2026-07-25T222019.png
security:
- kind: domain-security
  name: Ideal Invest Domain Security
  slug: ideal-invest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ideal-invest
tags:
- Company
- Fintech
- Student Financing
- Lending
- Education
- Brazil
- Consumer Finance
website: https://www.pravaler.com.br/
---
