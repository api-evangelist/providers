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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dreamwidth/hosts/dreamwidth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dreamwidth-hosts.yml
- group: other
  href: https://artifacts.apis.io/dreamwidth/vendors/dreamwidth-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dreamwidth-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.dreamwidth.org/
- group: start
  title: ''
  type: Login
  url: https://www.dreamwidth.org/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/sass/dart-sass/releases
- group: docs
  title: ''
  type: Documentation
  url: https://doc.dreamwidth.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dreamwidth
- group: auth
  href: https://artifacts.apis.io/dreamwidth/security/dreamwidth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreamwidth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dreamwidth.org/
- group: docs
  title: ''
  type: APIReference
  url: https://www.dreamwidth.org/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dreamwidth.org/create
- group: operate
  title: ''
  type: Support
  url: https://www.dreamwidth.org/support/
- group: company
  title: ''
  type: Blog
  url: https://dw-news.dreamwidth.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dreamwidth.org/legal/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dreamwidth.org/legal/privacy
coverage:
  checked: '2026-10-28'
  detail: Documentation pages return HTML without machine‑readable OpenAPI or other contracts.
  evidence:
  - status: 200
    url: https://www.dreamwidth.org/api/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Dreamwidth Studios is an independent, open‑source, community‑centric service that provides a platform for creative artists to share writing, artwork, and thoughts. It offers fine‑grained privacy controls, diverse communities, and supports a wide range of topics. The service is free to join, with optional paid features, and emphasizes diversity, open‑source development, and user‑driven content.
layout: provider
modified: '2026-10-28'
name: Dreamwidth
nav: Providers
network: true
overview: 'Dreamwidth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OpenSource, Community, Creative, and Platform.


  Dreamwidth''s developer surface includes changelog, documentation, API reference, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 44.6
    operational_transparency: 21.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dreamwidth Domain Security
  slug: dreamwidth-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dreamwidth
tags:
- Company
- OpenSource
- Community
- Creative
- Platform
website: https://www.dreamwidth.org/
---
