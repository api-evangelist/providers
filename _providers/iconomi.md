---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
api_count: 1
apis:
- description: Platform API for ICONOMI offering REST and WebSocket endpoints.
  name: Iconomi API
  slug: iconomi-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/iconomi/plans/iconomi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iconomi-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/iconomi/hosts/iconomi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/iconomi-hosts.yml
- group: other
  href: https://artifacts.apis.io/iconomi/vendors/iconomi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/iconomi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iconomi.com/legal/terms-and-conditions
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iconomi.com/
- group: start
  title: ''
  type: Login
  url: https://www.iconomi.com/login
- group: auth
  href: https://artifacts.apis.io/iconomi/security/iconomi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iconomi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iconomi.com/
- group: company
  title: ''
  type: Blog
  url: https://www.iconomi.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.iconomi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.iconomi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.iconomi.com/
created: '2026-10-27'
description: ICONOMI is a crypto asset management platform that enables users to buy, sell, and copy top-performing cryptocurrency investment strategies. It offers a marketplace of curated crypto strategies, portfolio management tools, and a suite of services for both retail and institutional investors, including business accounts, financial advisor solutions, and compliance features. The platform provides real-time market data, performance tracking, and educational resources to help users navigate the cryptocurrency market.
image: https://static.iconomi.com/img/og_meta_image.jpg
layout: provider
modified: '2026-10-27'
name: ICONOMI
nav: Providers
network: true
overview: 'ICONOMI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Asset Management, Investment, Platform, and Financial Services.


  ICONOMI''s developer surface includes engineering blog, documentation, getting-started guide, and 9 more developer resources.'
plans:
- name: Iconomi Plans Pricing
  plan_count: 23
  slug: iconomi-plans-pricing
random_paper: 6
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/iconomi/iconomi-2026-11-03T133616.png
security:
- kind: domain-security
  name: Iconomi Domain Security
  slug: iconomi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iconomi
tags:
- Cryptocurrency
- Asset Management
- Investment
- Platform
- Financial Services
- Company
website: https://iconomi.com/
---
