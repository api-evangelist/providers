---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/plan4all-z-s/authentication/plan4all-z-s-authentication.yml
  title: ''
  type: Authentication
  url: authentication/plan4all-z-s-authentication.yml
- group: other
  href: https://artifacts.apis.io/plan4all-z-s/hosts/plan4all-z-s-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plan4all-z-s-hosts.yml
- group: auth
  href: https://artifacts.apis.io/plan4all-z-s/security/plan4all-z-s-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plan4all-z-s-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.plan4all.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.plan4all.eu/
- group: company
  title: ''
  type: Blog
  url: https://www.plan4all.eu/news-and-events/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.plan4all.eu/about/data-protection-policy/
created: '2026-10-23'
description: Plan4All z.s. is a European fintech company offering a comprehensive platform for financial planning, budgeting, and investment management. The service integrates personal and corporate finance tools, enabling users to create detailed financial plans, track expenses, and optimize investment portfolios. Their API provides access to account data, transaction histories, budgeting categories, and forecasting models, supporting developers to build custom financial applications and services. Plan4All emphasizes data security, regulatory compliance, and seamless integration with banking institutions across the EU.
image: https://www.plan4all.eu/media/images/plan4all_logo_4black_bg.original.png
layout: provider
modified: '2026-10-23'
name: Plan4All z.s.
nav: Providers
network: true
overview: 'Plan4All z.s. is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial Planning, and EU.


  Plan4All z.s.''s developer surface includes authentication, engineering blog, and 5 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 39.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 11.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/plan4all-z-s/plan4all-z-s-2026-11-03T141254.png
security:
- kind: authentication
  name: Plan4All Z S Authentication
  slug: plan4all-z-s-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Plan4All Z S Domain Security
  slug: plan4all-z-s-domain-security
  summary_line: TLSv1.3
slug: plan4all-z-s
tags:
- Company
- Fintech
- Financial Planning
- EU
website: https://www.plan4all.eu/
---
