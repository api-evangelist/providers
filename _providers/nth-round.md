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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/nth-round/plans/nth-round-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nth-round-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/nth-round/hosts/nth-round-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nth-round-hosts.yml
- group: other
  href: https://artifacts.apis.io/nth-round/vendors/nth-round-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nth-round-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nthround.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://www.nthround.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nthround.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nthround.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.nthround.com/category/press
- group: company
  title: ''
  type: Blog
  url: https://www.nthround.com/blog/what-is-asc-718
- group: auth
  href: https://artifacts.apis.io/nth-round/security/nth-round-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nth-round-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nthround.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.nthround.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Nth Round provides a comprehensive shareholder management platform for private businesses and family enterprises, offering cap table management, cost basis tracking, digital ledger, and shareholder portal features to streamline equity administration, communications, and compliance.
image: https://cdn.prod.website-files.com/5c9ee576b7e3ed6b7c1a60b3/66bfb021c42c024d5047bda7_Nth_Round_Meta_Image.png
layout: provider
modified: '2026-10-22'
name: Nth Round
nav: Providers
network: true
overview: 'Nth Round is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Shareholder-Management, Cap Table, Private-Business, and Equity-Administration.


  Nth Round''s developer surface includes pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Nth Round Plans Pricing
  plan_count: 3
  slug: nth-round-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 14.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/nth-round/nth-round-2026-11-03T140341.png
security:
- kind: domain-security
  name: Nth Round Domain Security
  slug: nth-round-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nth-round
tags:
- Company
- Shareholder-Management
- Cap Table
- Private-Business
- Equity-Administration
website: https://www.nthround.com/
---
