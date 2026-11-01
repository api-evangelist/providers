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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.8
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/monarchmoney-com/plans/monarchmoney-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/monarchmoney-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.monarch.com/security
- group: agent
  href: https://artifacts.apis.io/monarchmoney-com/llms/monarchmoney-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monarchmoney-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/monarchmoney-com/well-known/monarchmoney-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/monarchmoney-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/monarchmoney-com/hosts/monarchmoney-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monarchmoney-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/monarchmoney-com/vendors/monarchmoney-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monarchmoney-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.monarch.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.monarch.com/hc/en-us
- group: auth
  title: ''
  type: Security
  url: https://www.monarch.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.monarch.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.monarch.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.monarch.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.monarch.com/whats-new
- group: company
  title: ''
  type: Blog
  url: https://www.monarch.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.monarch.com/onboarding-welcome-proxy
- group: docs
  title: ''
  type: Documentation
  url: https://docs.monarchmoney.com/
- group: auth
  href: https://artifacts.apis.io/monarchmoney-com/security/monarchmoney-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/monarchmoney-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/monarchmoney-com/security/monarchmoney-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monarchmoney-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.monarchmoney.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.monarch.com/mcp
  - status: 403
    url: https://docs.monarchmoney.com/api/mcp
  - status: 403
    url: https://www.monarch.com/mcp/v1
  - status: 200
    url: https://www.monarchmoney.com/
  reason: partner-login
  state: gated
created: '2026-10-21'
description: Monarch provides a personal finance app that lets users connect bank accounts, credit cards, loans, real estate, and investments to view all financial data in one place. The app offers tracking, budgeting, goal planning, and collaborative features for partners or advisors at no extra cost. It is available on web, iOS, and Android and syncs with over 13,000 financial institutions.
image: https://cdn.sanity.io/images/mdewiujj/production/42e4e4b2c48f8120fd3102146cfb6cd334b3fd8a-1200x630.jpg?rect=0,2,1200,627&w=1200&h=627&fit=crop&auto=format
layout: provider
modified: '2026-10-21'
name: Monarch Money
nav: Providers
network: true
overview: 'Monarch Money is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Personal Finance, Budgeting, and Financial Planning.


  Monarch Money''s developer surface includes support, pricing, changelog, engineering blog, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Monarchmoney Com Plans Pricing
  plan_count: 2
  slug: monarchmoney-com-plans-pricing
random_paper: 4
score:
  band: thin
  composite: 28.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 41.1
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Monarchmoney Com Domain Security
  slug: monarchmoney-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Monarchmoney Com Trust Center
  slug: monarchmoney-com-trust-center
  summary_line: SOC 2
slug: monarchmoney-com
tags:
- Personal Finance
- Budgeting
- Financial Planning
website: https://www.monarchmoney.com/
---
