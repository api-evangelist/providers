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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/hostplus/conformance/hostplus-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hostplus-conformance.yml
- group: other
  href: https://artifacts.apis.io/hostplus/hosts/hostplus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hostplus-hosts.yml
- group: other
  href: https://artifacts.apis.io/hostplus/vendors/hostplus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hostplus-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hostplus/security/hostplus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hostplus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hostplus.com.au/
- group: operate
  title: ''
  type: Support
  url: https://hostplus.com.au/about-us/contact-us
- group: company
  title: ''
  type: Newsroom
  url: https://hostplus.com.au/about-us/news
- group: commercial
  title: ''
  type: Pricing
  url: https://hostplus.com.au/smsfs/pricing-performance
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hostplus.com.au/about-us/legals/privacy
- group: other
  title: ''
  type: Disclaimer
  url: https://hostplus.com.au/about-us/legals/disclaimer
- group: start
  title: ''
  type: SignUp
  url: https://hostplus.com.au/advisers/register
- group: start
  title: ''
  type: Login
  url: https://www.clearinghouseapp.hostplus.com.au/login
- group: auth
  title: ''
  type: Security
  url: https://hostplus.com.au/about-us/hostplus-online-security
- group: company
  title: ''
  type: Careers
  url: https://hostplus.com.au/about-us/careers
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/HostplusSuper
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@hostplus
created: '2026-10-22'
description: Hostplus is an Australian superannuation fund (self-described as "our leading Australian superannuation fund, committed to putting our members first") offering superannuation, pensions, SMSF investment options and employer clearing-house (QuickSuper) and adviser services. The website is provided by Host-Plus Pty Limited (ABN 79 008 634 704, AFSL 244392) as trustee of the Hostplus Superannuation Fund and the Hostplus Pooled Superannuation Trust. No public developer portal or API documentation was found on hostplus.com.au. First surfaced via the API Evangelist harvest backlog (australia-apidays-2026).
image: https://hostplus.com.au/content/dam/hostplus-program/site/logo/logo-small.png
layout: provider
modified: '2026-10-22'
name: Hostplus
nav: Providers
network: true
overview: 'Hostplus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Superannuation, Financial Services, Retirement, and Pensions.


  Hostplus'' developer surface includes support, pricing, signup flow, YouTube channel, and 12 more developer resources.'
plans:
- name: Hostplus Plans Pricing
  plan_count: 0
  slug: hostplus-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Hostplus Rate Limits
  slug: hostplus-rate-limits
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 49.1
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.1
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hostplus/hostplus-2026-11-03T133456.png
security:
- kind: domain-security
  name: Hostplus Domain Security
  slug: hostplus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hostplus
tags:
- Company
- Superannuation
- Financial Services
- Retirement
- Pensions
- Investment
- Australia
website: https://hostplus.com.au/
---
