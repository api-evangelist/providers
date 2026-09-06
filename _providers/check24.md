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
  url: security/check24-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.check24.de
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CHECK24
- group: operate
  title: ''
  type: Support
  url: https://www.check24.de/unternehmen/kontakt/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.check24.de/popup/datenschutz-check24-gmbh/
created: '2026-07-17'
description: CHECK24 is Germany's largest online comparison portal (Vergleichsportal), founded in 1999 and headquartered in Munich. It lets more than 20 million customers compare prices and switch providers across over 50 categories, including car, life and health insurance, loans and bank accounts, electricity and gas, DSL and mobile tariffs, travel, rental cars, and online shopping. CHECK24 runs its own comparison calculators and a licensed bank (CHECK24 Bank), and integrates partner providers such as Allianz Direct through API-based connections. Backed by Accel, it is profiled in the API Evangelist network as a consumer company. CHECK24 maintains a verified GitHub organization and a GenDev developer scholarship program but publishes no public developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/check24.png
layout: provider
modified: '2026-07-18'
name: Check24
nav: Providers
network: true
overview: 'Check24 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Comparison, Insurance, and Fintech.


  Check24''s developer surface includes support and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 6.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/check24/refs/heads/main/screenshots/check24-2026-07-25T205132.png
security:
- kind: domain-security
  name: Check24 Domain Security
  slug: check24-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: check24
tags:
- Company
- Consumer
- Comparison
- Insurance
- Fintech
- Marketplace
- Price Comparison
- Germany
website: https://www.check24.de
---
