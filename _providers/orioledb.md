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
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/orioledb/refs/heads/main/changelog/orioledb-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/orioledb-changelog.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/orioledb/refs/heads/main/hosts/orioledb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orioledb-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/orioledb/refs/heads/main/vendors/orioledb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orioledb-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/orioledb/refs/heads/main/packages/orioledb-packages.yml
  title: ''
  type: SDKs
  url: packages/orioledb-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/orioledb/refs/heads/main/packages/orioledb-packages.yml
  title: ''
  type: Packages
  url: packages/orioledb-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://orioledb.com/blog/tags/release-notes
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/orioledb/refs/heads/main/security/orioledb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orioledb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.orioledb.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.orioledb.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.orioledb.com/docs/usage/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.orioledb.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orioledb
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.orioledb.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'OrioleDB is an open-source PostgreSQL extension and storage engine (Apache/PostgreSQL-licensed, github.com/orioledb) that combines the advantages of on-disk and in-memory engines: a copy-on-write, undo-log based table access method with row-level WAL, lock-less page reads and decoupled S3 storage. It is consumed as SQL inside PostgreSQL and shipped as source releases and a Docker image; it publishes no HTTP API.'
image: https://orioledb.com/img/logo-vertical.png
layout: provider
modified: '2026-10-13'
name: OrioleDB
nav: Providers
network: true
overview: 'OrioleDB is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Database, PostgreSQL, Storage Engines, and Open Source.


  OrioleDB''s developer surface includes changelog, documentation, getting-started guide, engineering blog, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 48.2
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Orioledb Domain Security
  slug: orioledb-domain-security
  summary_line: TLSv1.3
slug: orioledb
tags:
- Company
- Database
- PostgreSQL
- Storage Engines
- Open Source
- Extensions
website: https://www.orioledb.com
---
