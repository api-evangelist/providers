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
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/angel-co/well-known/angel-co-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/angel-co-status-security.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://wellfound.com/recruit/pricing
- group: commercial
  href: https://artifacts.apis.io/angel-co/plans/angel-co-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/angel-co-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/angel-co/well-known/angel-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/angel-co-security.txt
- group: agent
  href: https://artifacts.apis.io/angel-co/well-known/angel-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/angel-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/angel-co/hosts/angel-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/angel-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/angel-co/vendors/angel-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/angel-co-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wellfound.com
- group: start
  title: ''
  type: Login
  url: https://wellfound.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://help.wellfound.com/collection/415-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.wellfound.com/
- group: auth
  href: https://artifacts.apis.io/angel-co/security/angel-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/angel-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wellfound.com
- group: company
  title: ''
  type: Blog
  url: https://wellfound.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wellfound.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wellfound.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://wellfound.com/contact
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://wellfound.com/api/mcp
  - status: 403
    url: https://angel.co/mcp
  - status: 200
    url: https://angel.co
  reason: partner-login
  state: gated
created: '2026-10-25'
description: AngelList, now operating as Wellfound, is a platform that connects startups with investors and talent. It offers job listings, fundraising tools, and a network for founders and investors to discover opportunities. The service provides APIs for accessing startup data, job postings, and investor information, supporting integration with third‑party applications and services.
image: https://reach.wellfound.com/assets/marketing/og/homepage-2fb80e2936cb06211fa7702e4b089510c772d1b887166b884b4720f73445e875.png
layout: provider
modified: '2026-10-25'
name: AngelList
nav: Providers
network: true
overview: 'AngelList is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Startup, Recruiting, JobBoard, VentureCapital, and Platform.


  AngelList''s developer surface includes pricing, getting-started guide, documentation, engineering blog, support, and 12 more developer resources.'
plans:
- name: Angel Co Plans Pricing
  plan_count: 7
  slug: angel-co-plans-pricing
random_paper: 6
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Angel Co Domain Security
  slug: angel-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: angel-co
tags:
- Startup
- Recruiting
- JobBoard
- VentureCapital
- Platform
website: https://wellfound.com
---
