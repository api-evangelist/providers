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
  url: security/youtrip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.you.co/sg/
- group: company
  title: ''
  type: Blog
  url: https://www.you.co/sg/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.you.co/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://youtrip.onelink.me/P5AL/youtripsg
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.you.co/sg/terms_and_conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.you.co/sg/privacy_policy/
created: '2026-07-17'
description: YouTrip (You Technologies Group, you.co) is a Singapore-based fintech that operates a multi-currency mobile travel wallet paired with a prepaid Mastercard, letting consumers hold and spend in over 150 currencies with no foreign-exchange fees and competitive in-app exchange rates. Launched in 2018, the company also runs YouBiz, a business account and corporate card product for SMEs, and offers international transfers to more than 40 countries. Backed by Lightspeed Venture Partners, YouTrip processes billions of dollars in transactions annually across Singapore, Thailand, and Australia. As of this enrichment pass YouTrip exposes no public developer API, developer portal, OpenAPI specification, SDKs, or GitHub organization; consumer-facing account access is available only indirectly through open-banking aggregators.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/youtrip.png
layout: provider
modified: '2026-07-21'
name: Youtrip
nav: Providers
network: true
overview: 'Youtrip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Travel, and Multi-Currency Wallet.


  Youtrip''s developer surface includes engineering blog, support, signup flow, and 4 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 11.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/youtrip/refs/heads/main/screenshots/youtrip-2026-09-02T171336.png
security:
- kind: domain-security
  name: Youtrip Domain Security
  slug: youtrip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: youtrip
tags:
- Company
- Fintech
- Payments
- Travel
- Multi-Currency Wallet
- Foreign Exchange
- Prepaid Card
- Singapore
website: https://www.you.co/sg/
---
