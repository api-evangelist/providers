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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/mercurial/refs/heads/main/changelog/mercurial-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mercurial-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mercurial/refs/heads/main/packages/mercurial-packages.yml
  title: ''
  type: SDKs
  url: packages/mercurial-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/mercurial/refs/heads/main/packages/mercurial-packages.yml
  title: ''
  type: Packages
  url: packages/mercurial-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.mercurial-scm.org/help/topics.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mercurial-scm
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/mercurial/refs/heads/main/security/mercurial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mercurial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mercurial-scm.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.mercurial-scm.org/guide
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mercurial-scm.org/guide
coverage:
  checked: 2026-09-22
  detail: The Mercurial website provides HTML documentation but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.mercurial-scm.org/guide
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-22'
description: Mercurial is a free, distributed source control management tool. It efficiently handles projects of any size, offering fast, intuitive commands and extensibility through extensions. Written primarily in Python with parts in C and Rust, Mercurial runs on all major platforms and is open‑source under GPL‑2.0 or later.
layout: provider
modified: '2026-09-22'
name: Mercurial
nav: Providers
network: true
overview: 'Mercurial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Version Control, Open Source, Distributed, and Cross-Platform.


  Mercurial''s developer surface includes changelog, support, documentation, getting-started guide, and 5 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 46.3
    operational_transparency: 21.1
  previous_composite: 14.0
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mercurial Domain Security
  slug: mercurial-domain-security
  summary_line: TLSv1.3
slug: mercurial
tags:
- Company
- Version Control
- Open Source
- Distributed
- Cross-Platform
website: https://www.mercurial-scm.org/
---
