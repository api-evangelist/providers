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
  url: security/rally-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rallyrd.com/
- group: operate
  title: ''
  type: Support
  url: https://rallyrd.com/faq/
- group: company
  title: ''
  type: Blog
  url: https://rallyrd.com/stories-by-rally/
- group: start
  title: ''
  type: SignUp
  url: https://app.rallyrd.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rallyrd.com/privacy/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rallyrd.com/privacy/
created: '2026-07-17'
description: Rally (Rally Rd.) is an alternative-asset investing platform that lets everyday investors buy and sell equity shares in individual collectible assets — classic cars, watches, fine art, wine, sports memorabilia, trading cards, and other rare items. Rally sources and authenticates each item, files it with the SEC as a regulated offering, splits it into shares in an Initial Offering, and then opens a Bid/Ask secondary market roughly 90 days later so shareholders can trade. Founded in 2016 and headquartered in New York, Rally runs iOS, Android, and web apps and raised a $30M Series B led by Accel in 2021. Rally publishes no public developer API, SDKs, or documentation surface; this profile captures its identity and probed domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rally.png
layout: provider
modified: '2026-07-20'
name: Rally
nav: Providers
network: true
overview: 'Rally is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Alternative Assets, Investing, and Collectibles.


  Rally''s developer surface includes support, engineering blog, signup flow, and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rally/refs/heads/main/screenshots/rally-2026-09-02T152829.png
security:
- kind: domain-security
  name: Rally Domain Security
  slug: rally-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rally
tags:
- Company
- E-Commerce
- Alternative Assets
- Investing
- Collectibles
- Fractional Ownership
- Fintech
- Marketplace
website: https://rallyrd.com/
---
