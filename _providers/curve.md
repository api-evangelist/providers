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
  url: https://www.curve.com
- group: operate
  title: ''
  type: Support
  url: https://help.curve.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.curve.com/
- group: company
  title: ''
  type: Blog
  url: https://www.curve.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.curve.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curve.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curve.com/legal/privacy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curve-domain-security.yml
created: '2026-07-17'
description: Curve is a London-based fintech, founded in 2015 by Shachar Bialick, that consolidates multiple debit and credit cards into a single smart card and mobile wallet. Its "over-the-top" banking platform lets customers spend from any linked Mastercard or Visa card, switch the funding source of a past purchase up to 120 days later with "Go Back in Time", avoid foreign-exchange fees, earn cashback, and pay in instalments with Curve Flex. Premium tiers (Curve Pay X / Pro / Pro+) add insurance, lounge access, and richer rewards. Curve is backed by Seedcamp and Speedinvest among others. Curve does not publish a public developer API — it acts as an open-banking consumer to aggregate customer account balances rather than exposing a provider API.
image: https://cdn.buttercms.com/OZb0mcqMQz6dq1j13OYV
layout: provider
modified: '2026-07-18'
name: Curve
nav: Providers
network: true
overview: 'Curve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Digital Wallet, and Cards.


  Curve''s developer surface includes support, engineering blog, pricing, and 5 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 11.1
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
    operational_transparency: 15.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/curve/refs/heads/main/screenshots/curve-2026-07-25T210952.png
security:
- kind: domain-security
  name: Curve Domain Security
  slug: curve-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: curve
tags:
- Company
- Fintech
- Payments
- Digital Wallet
- Cards
- Open Banking
- Financial-Services
website: https://www.curve.com
---
