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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/booksloth/refs/heads/main/hosts/booksloth-hosts.yml
  title: ''
  type: Hosts
  url: hosts/booksloth-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/booksloth
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booksloth/refs/heads/main/security/booksloth-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/booksloth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.booksloth.com/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@booksloth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.booksloth.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.booksloth.com/privacy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.booksloth.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Booksloth is a community-driven platform that connects readers through personalized book recommendations, book clubs, and a store offering curated selections. Users can join the BookSloth app to track their reading history, discover new titles, and engage with fellow book enthusiasts. The service provides a blog, mobile apps for iPhone and Android, and integrates social media channels to foster a vibrant literary community. Founded in 2018, BookSloth aims to make reading a shared, enjoyable experience for all.
layout: provider
modified: '2026-10-12'
name: Booksloth
nav: Providers
network: true
overview: 'Booksloth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Book, Community, Reading, and App.


  Booksloth''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Booksloth Domain Security
  slug: booksloth-domain-security
  summary_line: TLSv1.3
slug: booksloth
tags:
- Company
- Book
- Community
- Reading
- App
website: https://www.booksloth.com/
---
