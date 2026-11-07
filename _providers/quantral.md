---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API providing access to Quantral's investment signals and alternative data.
  name: Quantral API
  slug: quantral-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/quantral/plans/quantral-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quantral-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/quantral/llms/quantral-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/quantral-llms.txt
- group: agent
  href: https://artifacts.apis.io/quantral/well-known/quantral-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quantral-well-known.yml
- group: other
  href: https://artifacts.apis.io/quantral/hosts/quantral-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quantral-hosts.yml
- group: other
  href: https://artifacts.apis.io/quantral/vendors/quantral-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quantral-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://quantral.com/support
- group: company
  title: ''
  type: Newsroom
  url: https://quantral.com/press
- group: auth
  href: https://artifacts.apis.io/quantral/security/quantral-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quantral-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://quantral.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.quantral.com
- group: docs
  title: ''
  type: Documentation
  url: https://quantral.com/learn
- group: start
  title: ''
  type: GettingStarted
  url: https://quantral.com/features
- group: company
  title: ''
  type: Blog
  url: https://quantral.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://quantral.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quantral.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quantral.com/privacy
coverage:
  checked: '2026-10-30'
  detail: Docs page redirects to a login screen, requiring authentication to view API documentation.
  evidence:
  - status: 307
    url: https://app.quantral.com/docs
  reason: auth-required
  state: gated
created: '2026-10-30'
description: Quantral is an investment‑ideas platform that aggregates alternative data from finance X, Reddit, Substack, YouTube finance shows, Korean Naver blogs, Telegram broker research, U.S. Congress stock disclosures, and insider trades. It scores each company from 0‑100 and grades each voice on historical accuracy, surfacing the strongest signals for investors. The service offers a web portal, iOS and Android apps, and a public API if available.
image: https://quantral.com/og.png
layout: provider
modified: '2026-10-30'
name: Quantral
nav: Providers
network: true
overview: 'Quantral is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, Analytics, and Artificial Intelligence.


  Quantral''s developer surface includes support, documentation, getting-started guide, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Quantral Plans Pricing
  plan_count: 3
  slug: quantral-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Quantral Rate Limits
  slug: quantral-rate-limits
scopes:
- name: Quantral Scopes
  scope_count: 0
  slug: quantral-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 58.0
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/quantral/quantral-2026-11-03T141817.png
security:
- kind: authentication
  name: Quantral Authentication
  slug: quantral-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Quantral Domain Security
  slug: quantral-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quantral
tags:
- Company
- Finance
- Data
- Analytics
- Artificial Intelligence
website: https://quantral.com
---
