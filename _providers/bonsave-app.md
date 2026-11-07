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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bonsave-app/plans/bonsave-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bonsave-app-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/bonsave-app/changelog/bonsave-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bonsave-app-changelog.yml
- group: agent
  href: https://artifacts.apis.io/bonsave-app/well-known/bonsave-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bonsave-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/bonsave-app/hosts/bonsave-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bonsave-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/bonsave-app/vendors/bonsave-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bonsave-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bonsave.app/terms
- group: operate
  title: ''
  type: Support
  url: https://www.bonsave.app/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bonsave.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bonsave.app/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.bonsave.app/guides/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bonsave.app/changelog/
- group: company
  title: ''
  type: Blog
  url: https://www.bonsave.app/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bonsave
- group: auth
  href: https://artifacts.apis.io/bonsave-app/security/bonsave-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bonsave-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bonsave.app/
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are HTML rendered without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://www.bonsave.app/guides/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: Bonsave is a smart financial planning app that syncs your accounts, tracks net worth, and delivers a daily AI insight. It offers subscription plans with a 14‑day free trial, uses Plaid for secure bank connections, and emphasizes data privacy and encryption.
image: https://www.bonsave.app/api/og?title=Grow%20your%20money.%20Intentionally.&description=Bonsave%20syncs%20your%20financial%20accounts%20and%20delivers%20one%20focused%20insight%20every%20day%20to%20help%20you%20build%20lasting%20wealth.&tagline=One%20insight.%20Every%20day.&screenshot=dashboard
layout: provider
modified: '2026-11-02'
name: Bonsave
nav: Providers
network: true
overview: 'Bonsave is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Planning, Net Worth Tracking, AI Insights, Retirement Planning, and Investment Tracking.


  Bonsave''s developer surface includes changelog, support, pricing, documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Bonsave App Plans Pricing
  plan_count: 2
  slug: bonsave-app-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bonsave App Domain Security
  slug: bonsave-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bonsave-app
tags:
- Financial Planning
- Net Worth Tracking
- AI Insights
- Retirement Planning
- Investment Tracking
website: https://bonsave.app/
---
