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
  url: security/firsty-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://firsty.app
- group: company
  title: ''
  type: About
  url: https://firsty.app/about-us
- group: commercial
  title: ''
  type: Pricing
  url: https://firsty.app/plans/classic
- group: operate
  title: ''
  type: Support
  url: https://firsty.app/help
- group: company
  title: ''
  type: Blog
  url: https://firsty.app/the-wanderer
- group: commercial
  title: ''
  type: TermsOfService
  url: https://firsty.app/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firsty.app/privacy-policy
created: '2026-07-17'
description: Firsty is an Amsterdam-based eSIM and mobile connectivity provider founded in 2023 that positions internet access as a basic human right. Its consumer app delivers free, ad-supported global data alongside affordable Classic (pay-per-GB) and Unlimited (daily/monthly) plans, plus international calling, across 170+ countries with automatic connection to the best available network and no physical SIM required. Firsty has surpassed one million users and lists partnerships with brands including Uber, Grab, Mastercard, KBC and Belfius. Backed by Speedinvest, it is a consumer travel-connectivity app with no public developer API or programmatic surface at this time.
image: https://firsty.app/press-kit
layout: provider
modified: '2026-07-19'
name: Firsty
nav: Providers
network: true
overview: 'Firsty is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, eSIM, Mobile, Connectivity, and Telecommunications.


  Firsty''s developer surface includes pricing, support, engineering blog, and 5 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 4
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/firsty/refs/heads/main/screenshots/firsty-2026-07-25T214624.png
security:
- kind: domain-security
  name: Firsty Domain Security
  slug: firsty-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: firsty
tags:
- Company
- eSIM
- Mobile
- Connectivity
- Telecommunications
- Travel
- Roaming
- Data
- Consumer
website: https://firsty.app
---
