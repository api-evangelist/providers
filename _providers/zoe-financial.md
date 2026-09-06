---
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoe-financial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zoefinancial.com/
- group: company
  title: ''
  type: Blog
  url: https://zoefinancial.com/articles
- group: operate
  title: ''
  type: Support
  url: https://zoefinancial.com/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://zoefinancial.com/fee-schedule
- group: start
  title: ''
  type: SignUp
  url: https://my.zoefin.com/find-an-advisor
- group: start
  title: ''
  type: Login
  url: https://app.zoefin.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zoefinancial.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zoefinancial.com/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoefinancial
- group: design
  title: ''
  type: Conformance
  url: conformance/zoe-financial-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/zoe-financial-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zoe-financial-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 'Zoe Financial ships software only as an end-user product — a consumer advisor-match site and an authenticated advisor platform — and runs no developer program at all: none of the 61 pages in its public sitemap is developer facing, and its one API host api.zoefin.com answers 401 from a blanket authorizer even for a fabricated control path, so nothing about a contract can be read there.'
  evidence:
  - status: 401
    url: https://api.zoefin.com/api/v1/openapi.json
  - status: 401
    url: https://api.zoefin.com/api/v1/zzz-nonexistent-control-9f3a
  - status: 404
    url: https://zoefinancial.com/openapi.json
  - status: 404
    url: https://zoefinancial.com/.well-known/agent-card.json
  - status: 200
    url: https://zoefinancial.com/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 'Zoe Financial is a New York based wealth management technology company operating a two-sided platform: Advisor Match, a concierge and algorithmic service connecting individuals with vetted independent fiduciary financial advisors, and the Zoe Wealth Platform, an all-in-one TAMP for registered investment advisers covering digital account opening, funding and ACAT transfers, sub-advisory trade execution, household-level automated rebalancing, tax-loss harvesting, a model marketplace, high-yield cash accounts, private labeling and outsourced middle-office operations. Zoe Financial, Inc. is an SEC-registered investment adviser (CRD 285158) and affiliate Zoe Securities LLC is a FINRA and SIPC member broker-dealer (CRD 326979), custodying through Apex Clearing and Charles Schwab. Zoe consumes partner APIs (BridgeFT, Salesforce, eMoney) but publishes no public API, SDK, developer portal or machine-readable contract of its own.'
image: https://framerusercontent.com/images/j8kosDjvH3CZOxN2ElANyw2FXLg.png
layout: provider
modified: '2026-09-05'
name: Zoe Financial
nav: Providers
network: true
overview: 'Zoe Financial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Wealth Management, Financial Advisors, TAMP, Investment Management, and Registered Investment Adviser.


  Zoe Financial''s developer surface includes engineering blog, support, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Zoe Financial Plans Pricing
  plan_count: 0
  slug: zoe-financial-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Zoe Financial Rate Limits
  slug: zoe-financial-rate-limits
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 2.6
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Zoe Financial Domain Security
  slug: zoe-financial-domain-security
  summary_line: TLSv1.3 · HSTS
slug: zoe-financial
tags:
- Wealth Management
- Financial Advisors
- TAMP
- Investment Management
- Registered Investment Adviser
- Brokerage
- Financial Services
- Portfolio Management
- Fintech
website: https://zoefinancial.com/
---
