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
  url: security/noodle-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://noodle.cx
- group: operate
  title: ''
  type: Support
  url: https://ajuda.noodle.cx/
- group: company
  title: ''
  type: Blog
  url: https://noodle.cx/news/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://noodle.cx/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://noodle.cx/termos
- group: start
  title: ''
  type: Login
  url: https://split.noodle.cx
created: '2026-07-17'
description: Noodle is a Brazilian fintech building financial infrastructure for the creator economy. It provides automated payouts to creators, influencers, and vendors; FastPay early access to future earnings; noodleOS, a unified platform for campaigns, creator data, payments, and asset tracking; global payouts powered by Ebanx; foreign-exchange settlement; and credit and capital products underwritten in part on a creator's social presence. Backed by QED Investors, Noodle serves media companies, agencies, and platforms that pay content creators. The company references API-based integrations but publishes no public developer portal or API documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/noodle.png
layout: provider
modified: '2026-07-20'
name: Noodle
nav: Providers
network: true
overview: 'Noodle is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Payouts, and Creator Economy.


  Noodle''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 10.4
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
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/noodle/refs/heads/main/screenshots/noodle-2026-08-07T185450.png
security:
- kind: domain-security
  name: Noodle Domain Security
  slug: noodle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: noodle
tags:
- Company
- Fintech
- Payments
- Payouts
- Creator Economy
- Brazil
- Foreign Exchange
- Financial-Services
website: https://noodle.cx
---
