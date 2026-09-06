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
  url: security/happytal-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.happytal.com/
- group: company
  title: ''
  type: About
  url: https://www.happytal.com/a-propos
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/happytal
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.happytal.com/legal/cgu-marketplace
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.happytal.com/legal/ppdp
created: '2026-07-17'
description: Happytal is a French healthtech and services company founded in 2013 and acquired by La Poste Group's health division (La Poste Santé) in 2022. It operates a hospital concierge service (conciergerie hospitalière) that combines a digital platform with on-site human concierges to simplify the administrative, medical and hotel journey of each patient. Services include in-room delivery, a comfort-products marketplace, private-room and admission paperwork assistance, and support for patients, their families and hospital staff across French healthcare establishments, alongside elder-care/EHPAD offerings and the careside.care business-to-business product for care facilities. Happytal exposes no public developer API; this profile is maintained in the API Evangelist network as a company record enriched from public sources.
image: https://www.happytal.com/logo-happytal-desktop.svg
layout: provider
modified: '2026-07-19'
name: Happytal
nav: Providers
network: true
overview: Happytal is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Healthcare, Health, and France.
random_paper: 6
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 2
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 9.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/happytal/refs/heads/main/screenshots/happytal-2026-07-25T220701.png
security:
- kind: domain-security
  name: Happytal Domain Security
  slug: happytal-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: happytal
tags:
- Company
- Consumer
- Healthcare
- Health
- France
- Concierge
- Marketplace
- Elder Care
- Patient Experience
- Health Tech
website: https://www.happytal.com/
---
