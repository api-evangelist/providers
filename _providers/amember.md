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
  href: https://artifacts.apis.io/amember/plans/amember-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amember-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/amember/hosts/amember-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amember-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.amember.com/amember/signup/demo
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.amember.com/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amember.com//Product_Billing_Setup_Fee_Recurring
- group: auth
  href: https://artifacts.apis.io/amember/security/amember-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amember-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amember.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.amember.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.amember.com/order/
- group: operate
  title: ''
  type: Support
  url: https://www.amember.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.amember.com/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amember.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amember.com/privacy/
coverage:
  checked: '2026-10-26'
  detail: aMember provides a self‑hosted membership platform but offers no public developer API or documentation.
  evidence:
  - status: 404
    url: https://docs.amember.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: aMember provides a self‑hosted membership and subscription software solution called aMember Pro. It enables website owners to sell memberships, subscriptions, digital products, and services directly from their own servers, supporting over 237 payment systems, multiple languages, and extensive integration options. The platform includes features such as affiliate programs, helpdesk, newsletters, licensing, and detailed reporting, catering to businesses of all sizes.
layout: provider
modified: '2026-10-26'
name: aMember
nav: Providers
network: true
overview: 'aMember is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Membership Software, Subscription Management, Self-Hosted, Payment Integration, and Affiliate Program.


  aMember''s developer surface includes signup flow, changelog, getting-started guide, documentation, pricing, support, engineering blog, and 6 more developer resources.'
plans:
- name: Amember Plans Pricing
  plan_count: 3
  slug: amember-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 17.5
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 44.6
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/amember/amember-2026-11-03T120808.png
security:
- kind: domain-security
  name: Amember Domain Security
  slug: amember-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: amember
tags:
- Membership Software
- Subscription Management
- Self-Hosted
- Payment Integration
- Affiliate Program
- Team Accounts
website: https://amember.com/
---
