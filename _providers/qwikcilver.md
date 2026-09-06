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
api_count: 1
apis:
- description: QwikCilver / Woohoo gift card and prepaid commerce API for browsing brand catalogs, placing gift card orders, activating and redeeming cards, checking balances, and running reward programs. OAuth2 cli
  name: Woohoo Gift Card API
  slug: woohoo-gift-card-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qwikcilver-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qwikcilver-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://www.woohoo.in
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.qwikcilver.in
- group: company
  title: ''
  type: Blog
  url: https://blog.woohoo.in/
- group: operate
  title: ''
  type: Support
  url: https://woohoo.in/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://woohoo.in/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://woohoo.in/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://woohoo.in/privacy
created: '2026-07-17'
description: QwikCilver is India's largest gift card and prepaid commerce company, founded in 2006 and acquired by Pine Labs in 2019. It powers gift card issuance, distribution, and redemption for retailers, banks, and enterprises, and operates the consumer and corporate gifting marketplace Woohoo (woohoo.in), which sells digital and physical gift cards from 300+ brands. Its API platform (hosted on woohoo.in) lets partners programmatically browse catalogs, place bulk gift card orders, activate and redeem cards, check balances, and run reward, incentive, and channel-engagement programs. QwikCilver is an Accel portfolio company in the consumer / fintech sector.
image: https://b2cstatic.woohoo.in/media/favicon/websites/2/Woohoo_Favicon_2.png
layout: provider
modified: '2026-07-20'
name: QwikCilver
nav: Providers
network: true
overview: 'QwikCilver publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gift Cards, Prepaid, and Payments.


  QwikCilver''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 13.3
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 13.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qwikcilver/refs/heads/main/screenshots/qwikcilver-2026-09-02T152726.png
security:
- kind: domain-security
  name: Qwikcilver Domain Security
  slug: qwikcilver-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qwikcilver
tags:
- Company
- Consumer
- Gift Cards
- Prepaid
- Payments
- Fintech
- Rewards
- Corporate Gifting
- India
website: https://www.woohoo.in
---
