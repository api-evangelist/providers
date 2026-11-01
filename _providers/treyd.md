---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Treyd provides financing API documented at their help center.
  name: Treyd API
  slug: treyd-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/treyd/plans/treyd-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/treyd-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/treyd/well-known/treyd-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/treyd-well-known.yml
- group: other
  href: https://artifacts.apis.io/treyd/hosts/treyd-hosts.yml
  title: ''
  type: Hosts
  url: hosts/treyd-hosts.yml
- group: other
  href: https://artifacts.apis.io/treyd/vendors/treyd-vendors.yml
  title: ''
  type: Vendors
  url: vendors/treyd-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.treyd.io/home/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.treyd.io/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.treyd.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://help.treyd.io/kb/article/38-do-i-need-to-invite-other-people-to-complete-onboarding/
- group: docs
  title: ''
  type: Documentation
  url: https://help.treyd.io/
- group: auth
  href: https://artifacts.apis.io/treyd/security/treyd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/treyd-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.treyd.io/
coverage:
  checked: '2026-10-15'
  detail: Help center pages are rendered via JavaScript and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://help.treyd.io/home/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Treyd provides working capital financing solutions for product‑based businesses in Europe. By advancing supplier payments and accelerating customer receivables, Treyd helps brands scale faster while maintaining cash flow control. The platform offers flexible financing options, a self‑service portal, and integrates with various payment systems to streamline funding and repayment processes.
image: https://www.datocms-assets.com/67452/1697457327-treyd.jpg
layout: provider
modified: '2026-10-15'
name: Treyd
nav: Providers
network: true
overview: 'Treyd is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Working Capital, B2B, and Europe.


  Treyd''s developer surface includes support, pricing, getting-started guide, documentation, and 7 more developer resources.'
plans:
- name: Treyd Plans Pricing
  plan_count: 1
  slug: treyd-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 19.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Treyd Domain Security
  slug: treyd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: treyd
tags:
- Company
- Fintech
- Working Capital
- B2B
- Europe
website: https://www.treyd.io/
---
