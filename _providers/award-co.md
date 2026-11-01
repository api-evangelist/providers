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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/award-co/plans/award-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/award-co-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/award-co/well-known/award-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/award-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/award-co/hosts/award-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/award-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/award-co/vendors/award-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/award-co-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.awardco.com
- group: operate
  title: ''
  type: Support
  url: https://help.awardco.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.awardco.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.awardco.com/plans
- group: company
  title: ''
  type: Newsroom
  url: https://www.awardco.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://app.awardco.com/start/login
- group: company
  title: ''
  type: Blog
  url: https://www.awardco.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.awardco.com/
- group: auth
  href: https://artifacts.apis.io/award-co/security/award-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/award-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.awardco.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 401
    url: https://help.awardco.com/mcp
  - status: 200
    url: https://www.award.co
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Awardco provides a unified employee recognition, rewards, and engagement platform that helps organizations build culture, incentivize performance, and automate reward distribution. The SaaS solution consolidates recognition, incentives, and engagement tools into one system, offering demos and scalable features for enterprises worldwide.
image: https://cdn.prod.website-files.com/6809c7073641f7a4861d5cc1/681f763600c3fb2ba46fe3a9_c5732a684635194c76d07940fee701db_awardco_main-OG.webp
layout: provider
modified: '2026-10-22'
name: Awardco
nav: Providers
network: true
overview: 'Awardco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, SaaS, Employee Engagement, Rewards, and Recognition.


  Awardco''s developer surface includes support, pricing, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Award Co Plans Pricing
  plan_count: 5
  slug: award-co-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Award Co Domain Security
  slug: award-co-domain-security
  summary_line: TLSv1.3 · HSTS
slug: award-co
tags:
- Company
- SaaS
- Employee Engagement
- Rewards
- Recognition
website: https://www.awardco.com
---
