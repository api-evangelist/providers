---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
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
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/unisuper/plans/unisuper-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/unisuper-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/unisuper/hosts/unisuper-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unisuper-hosts.yml
- group: other
  href: https://artifacts.apis.io/unisuper/vendors/unisuper-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unisuper-vendors.yml
- group: auth
  href: https://artifacts.apis.io/unisuper/security/unisuper-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unisuper-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unisuper.com.au/
- group: company
  title: ''
  type: About
  url: https://www.unisuper.com.au/about-us/who-we-are
- group: operate
  title: ''
  type: Support
  url: https://www.unisuper.com.au/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.unisuper.com.au/news-and-insights
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unisuper.com.au/super/fees-and-costs
- group: start
  title: ''
  type: SignUp
  url: https://join.unisuper.com.au/personal-account/get-started
- group: start
  title: ''
  type: Login
  url: https://memberonline.unisuper.com.au/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unisuper.com.au/about-us/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unisuper.com.au/about-us/privacy/privacy-statement
- group: company
  title: ''
  type: Careers
  url: https://www.unisuper.com.au/about-us/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/unisuper
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/au/app/unisuper/id1614758946
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=au.com.unisuper
created: '2026-10-22'
description: UniSuper is an Australian superannuation (retirement savings) fund, originally for employees in the higher education and research sector, offering accumulation super accounts, retirement income and pension products, investment options, insurance through super and financial advice. Its website states it has helped Australians prepare for retirement since 1982 and does not pay profits to shareholders or commissions to advisers. UniSuper does not publish a public developer portal or API documentation; members, employers and advisers use its online portals and mobile app.
image: https://media.licdn.com/dms/image/v2/D560BAQE_ErqyAuD4Fw/company-logo_200_200/B56ZcUggqRG0AI-/0/1748395756867/unisuper_logo?e=2147483647&v=beta&t=04nOLaJLo-uFP4u7NqkLXLcz7fUo6P2aAucvMa81GjQ
layout: provider
modified: '2026-10-22'
name: UniSuper
nav: Providers
network: true
overview: 'UniSuper is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Superannuation, Retirement, Pensions, and Investment.


  UniSuper''s developer surface includes support, engineering blog, pricing, signup flow, and 13 more developer resources.'
plans:
- name: Unisuper Plans Pricing
  plan_count: 1
  slug: unisuper-plans-pricing
random_paper: 3
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
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
  previous_composite: 18.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Unisuper Domain Security
  slug: unisuper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unisuper
tags:
- Company
- Superannuation
- Retirement
- Pensions
- Investment
- Financial Services
- Insurance
- Australia
website: https://www.unisuper.com.au/
---
