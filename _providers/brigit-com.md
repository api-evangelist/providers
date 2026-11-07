---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  href: https://artifacts.apis.io/brigit-com/plans/brigit-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brigit-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/brigit-com/hosts/brigit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brigit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/brigit-com/vendors/brigit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brigit-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.hellobrigit.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://www.hellobrigit.com/press
- group: auth
  href: https://artifacts.apis.io/brigit-com/security/brigit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brigit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brigit.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.hellobrigit.com/learn
- group: operate
  title: ''
  type: Support
  url: https://help.hellobrigit.com/hc/en-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellobrigit.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellobrigit.com/terms
created: '2026-10-24'
description: Brigit is a fintech company offering cash advances, credit building, and financial management tools to help everyday Americans avoid overdraft fees, build credit, and save money. Their mobile app provides instant cash, credit builder, budgeting assistance, and personalized financial guidance, serving over 15 million users.
image: https://www.hellobrigit.com/wp-content/uploads/2023/09/BannerBackground-Credit-2.png
layout: provider
modified: '2026-10-24'
name: Brigit
nav: Providers
network: true
overview: 'Brigit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Personal Finance, Cash Advance, Credit Building, and Budgeting.


  Brigit''s developer surface includes documentation, support, and 9 more developer resources.'
plans:
- name: Brigit Com Plans Pricing
  plan_count: 3
  slug: brigit-com-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 49.1
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.5
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/brigit-com/brigit-com-2026-11-03T122636.png
security:
- kind: domain-security
  name: Brigit Com Domain Security
  slug: brigit-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: brigit-com
tags:
- Fintech
- Personal Finance
- Cash Advance
- Credit Building
- Budgeting
website: https://brigit.com
---
