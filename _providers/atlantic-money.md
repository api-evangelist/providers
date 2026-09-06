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
- group: company
  title: ''
  type: Website
  url: https://atlantic.money/
- group: operate
  title: ''
  type: Support
  url: https://support.atlantic.money/
- group: company
  title: ''
  type: Blog
  url: https://news.atlantic.money/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atlantic.money/l/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atlantic.money/l/user-agreement
- group: start
  title: ''
  type: SignUp
  url: https://app.atlantic.money/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atlantic-money-domain-security.yml
created: '2026-07-17'
description: Atlantic Money is a London-based fintech, founded in 2020 by Robinhood alumni and backed by Index Ventures, offering international money transfers at a flat GBP 3 fee with the live mid-market exchange rate and no FX markup. The service supports transfers across ten currencies with direct bank deposits and standard or express delivery, for both consumers and businesses, and is authorized and regulated by the UK FCA as a payment institution. Atlantic Money is a consumer- and business-facing mobile and web application; it publishes no public developer API, OpenAPI, or SDK surface, so this network profile is limited to company identity, website property links, and probed domain-security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/atlantic-money.png
layout: provider
modified: '2026-07-18'
name: Atlantic Money
nav: Providers
network: true
overview: 'Atlantic Money is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Money Transfer, Payments, and Foreign Exchange.


  Atlantic Money''s developer surface includes support, engineering blog, signup flow, and 4 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 9.1
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
    - europe
    - united-kingdom-ireland
  previous_composite: 9.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atlantic-money/refs/heads/main/screenshots/atlantic-money-2026-07-25T201543.png
security:
- kind: domain-security
  name: Atlantic Money Domain Security
  slug: atlantic-money-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atlantic-money
tags:
- Company
- Fintech
- Money Transfer
- Payments
- Foreign Exchange
- Remittance
- Financial-Services
- FCA Regulated
website: https://atlantic.money/
---
