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
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/selency-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/selency-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/selency-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.selency.fr
- group: operate
  title: ''
  type: HelpCenter
  url: https://selency.frontkb.com/fr
- group: company
  title: ''
  type: Blog
  url: https://www.selency.fr/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.selency.fr/auth/login
- group: start
  title: ''
  type: Login
  url: https://www.selency.fr/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://share.selency.com/CGV/cgv.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://share.selency.com/CGV/privacy-statement-2021-03.pdf
created: '2026-07-17'
description: 'Selency is the leading European online marketplace for vintage furniture and second-hand home decor. Founded in Paris in 2014 (formerly Brocante Lab), it connects individual sellers and professional antique dealers with buyers around a curated catalog of more than 300,000 unique pieces: Scandinavian, art deco, mid-century, 20th-century and contemporary design, lighting, mirrors, rugs and decorative objects. Selency acts as a trusted third party, editorially validating each listing and arranging specialized furniture delivery across Europe. It is a B Corp certified consumer marketplace with French, UK and Netherlands storefronts. No public developer API is offered.'
image: https://images.selency.com/8c4c71d3-ed0c-413d-a11f-35f253b56998
layout: provider
modified: '2026-07-21'
name: Selency
nav: Providers
network: true
overview: 'Selency is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Marketplace, Furniture, and Home Decor.


  Selency''s developer surface includes engineering blog, signup flow, and 8 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 10.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/selency/refs/heads/main/screenshots/selency-2026-09-02T154816.png
security:
- kind: domain-security
  name: Selency Domain Security
  slug: selency-domain-security
  summary_line: TLSv1.3 · DMARC
slug: selency
tags:
- Company
- Consumer
- Marketplace
- Furniture
- Home Decor
- Secondhand
- Vintage
- E-Commerce
- France
website: https://www.selency.fr
---
