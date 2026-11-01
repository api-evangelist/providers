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
api_count: 1
apis:
- description: Pagure provides a read‑only archive of its former code‑hosting platform; the documentation indicates the service was sunset in 2024 and now serves a static snapshot.
  name: Pagure API
  slug: pagure-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/pagure/hosts/pagure-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pagure-hosts.yml
- group: company
  title: ''
  type: Blog
  url: https://pagure.io/Blog
- group: start
  title: ''
  type: GettingStarted
  url: https://pagure.io/ARM-getting-started-guide
- group: auth
  href: https://artifacts.apis.io/pagure/security/pagure-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pagure-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pagure.io/
- group: docs
  title: ''
  type: Documentation
  url: https://pagure.io/docs
coverage:
  checked: '2026-10-27'
  detail: Documentation is a static read‑only archive with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://pagure.io/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Pagure is an open-source, Fedora‑based code hosting platform that provides Git repositories, issue tracking, pull requests, and CI integration. Historically used for many Fedora projects, Pagure offered a web interface for collaborative development and served as the upstream for several open‑source initiatives. The service was sunset in mid‑2024, and the site now hosts a static archive of its former content, preserving project histories for reference.
layout: provider
modified: '2026-10-27'
name: Pagure
nav: Providers
network: true
overview: 'Pagure is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Code Hosting, Open Source, Fedora, Git, and Collaboration.


  Pagure''s developer surface includes engineering blog, getting-started guide, documentation, and 3 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pagure Domain Security
  slug: pagure-domain-security
  summary_line: TLSv1.3 · HSTS
slug: pagure
tags:
- Code Hosting
- Open Source
- Fedora
- Git
- Collaboration
- Archive
website: https://pagure.io/
---
