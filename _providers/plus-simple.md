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
  url: security/plus-simple-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plussimple.com/
- group: company
  title: ''
  type: Blog
  url: https://plussimple.com/blog
- group: operate
  title: ''
  type: Support
  url: https://plussimple.com/fr/nous-contacter
- group: start
  title: ''
  type: Login
  url: https://app.simplifieurs.pro/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plussimple.com/fr/legal/conditions-generales
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plussimple.com/fr/legal/charte-confidentialite
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simple-france/
created: '2026-07-17'
description: +Simple (Plus Simple) is a French digital insurance underwriting agency (agence de souscription) founded in 2015 and headquartered in Marseille. Operating as one of France's largest wholesale insurance brokers, it runs a fully digital extranet platform that lets partner insurance brokers prospect, price, underwrite, issue, and manage professional insurance contracts across more than 1,200 covered activities and 30+ niche product lines, including RC Décennale (ten-year construction liability) coverage. +Simple distributes on a 100% brokerage model in partnership with carriers such as Hiscox, Allianz, Wakam, QBE and Beazley, serving a network of 8,000+ partner brokers. The company is backed by Anthemis and Speedinvest and was added to the API Evangelist network as a venture-portfolio lead; it publishes no public API or developer surface at this time (its broker and insured portals are authenticated web applications, not open APIs).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plus-simple.png
layout: provider
modified: '2026-07-20'
name: Plus Simple
nav: Providers
network: true
overview: 'Plus Simple is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Insurtech, Fintech, and Brokerage.


  Plus Simple''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
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
  previous_composite: 11.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plus-simple/refs/heads/main/screenshots/plus-simple-2026-09-02T151546.png
security:
- kind: domain-security
  name: Plus Simple Domain Security
  slug: plus-simple-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plus-simple
tags:
- Company
- Insurance
- Insurtech
- Fintech
- Brokerage
- Underwriting
- France
- B2B
website: https://plussimple.com/
---
