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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/smash-gg/hosts/smash-gg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smash-gg-hosts.yml
- group: other
  href: https://artifacts.apis.io/smash-gg/vendors/smash-gg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/smash-gg-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.start.gg/about/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.start.gg/about/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.start.gg/
- group: company
  title: ''
  type: Blog
  url: https://blog.start.gg/ggu/home
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.start.gg/docs/intro
- group: docs
  title: ''
  type: Documentation
  url: https://developer.smash.gg/
- group: auth
  href: https://artifacts.apis.io/smash-gg/security/smash-gg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smash-gg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.start.gg
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.smash.gg
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Start.gg (formerly Smash.gg) is a leading esports platform that enables creators, organizers, and players to create, run, watch, and monetize competitive gaming tournaments and events across a wide range of titles. It provides tools for bracket management, live streaming integration, participant registration, and community engagement, serving both amateur and professional esports ecosystems.
image: https://www.start.gg/__static/images/wordmark_echo_background.png
layout: provider
modified: '2026-10-21'
name: Smashgg
nav: Providers
network: true
overview: 'Smashgg is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Smashgg''s developer surface includes engineering blog, getting-started guide, documentation, and 7 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Smash Gg Domain Security
  slug: smash-gg-domain-security
  summary_line: TLSv1.3 · DMARC
slug: smash-gg
tags:
- Company
website: https://www.start.gg
---
