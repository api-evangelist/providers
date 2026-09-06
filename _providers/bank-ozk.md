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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: start
  title: ''
  type: Login
  url: https://www.ozk.com/login
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bank-ozk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ozk.com/
- group: operate
  title: ''
  type: Support
  url: https://www.ozk.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ozk.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ozk.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.ozk.com/learning-center/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bank-ozk
created: '2026-07-23'
description: Bank OZK is a regional bank headquartered in Little Rock, Arkansas, tracing its charter to 1903 and today operating roughly 265 offices across Arkansas, Georgia, Florida, North Carolina, Texas, and New York. It is a state-chartered commercial bank and the wholly owned subsidiary of Bank OZK holding company, publicly traded on the Nasdaq Global Select Market under the symbol OZK, with about $40.8 billion in total assets as of year-end 2025 and a national reputation in commercial real estate lending. Bank OZK runs no first-party public developer portal and publishes no downloadable OpenAPI/Swagger specifications; it is not a documented Financial Data Exchange (FDX) participant and has not published a specific CFPB Section 1033 data-access posture. Consumer-permissioned account data is reached only indirectly through third-party aggregators, with Plaid documented as the supporting aggregator. This is an honest identity-only profile with no public API surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Bank OZK
nav: Providers
network: true
overview: 'Bank OZK is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Regional Bank, and Commercial Real Estate Lending.


  Bank OZK''s developer surface includes support, engineering blog, and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 9.9
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
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Bank Ozk Domain Security
  slug: bank-ozk-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bank-ozk
tags:
- Financial-Services
- Banking
- United States
- Regional Bank
- Commercial Real Estate Lending
- Open Finance
- Data Aggregation
website: https://www.ozk.com/
---
