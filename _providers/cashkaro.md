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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cashkaro/hosts/cashkaro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cashkaro-hosts.yml
- group: other
  href: https://artifacts.apis.io/cashkaro/vendors/cashkaro-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cashkaro-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cashkaro.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://cashkaro.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cashkaro.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://cashkaro.com/page/press
- group: company
  title: ''
  type: Blog
  url: https://cashkaro.com/blog
- group: auth
  href: https://artifacts.apis.io/cashkaro/security/cashkaro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cashkaro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cashkaro.com
coverage:
  checked: '2026-10-07'
  detail: API endpoints return 403 and no OpenAPI spec is available.
  evidence:
  - status: 403
    url: https://api.cashkaro.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-07'
description: CashKaro is India’s largest cashback and coupons platform, helping shoppers save money by offering cash back, discount codes, and deals across thousands of online stores. Users earn cash back on purchases, track earnings, and redeem rewards, while the site provides a comprehensive catalog of offers, a referral program, and a mobile app for convenient shopping.
image: https://asset22.ckassets.com/resources/image/staticpage_images/CK-Logo-1613133688.png
layout: provider
modified: '2026-10-07'
name: Cashkaro
nav: Providers
network: true
overview: 'Cashkaro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cashback, Coupons, E-Commerce, and India.


  Cashkaro''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 10.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cashkaro/cashkaro-2026-11-03T123442.png
security:
- kind: domain-security
  name: Cashkaro Domain Security
  slug: cashkaro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cashkaro
tags:
- Company
- Cashback
- Coupons
- E-Commerce
- India
website: https://cashkaro.com
---
