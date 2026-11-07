---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
api_count: 1
apis:
- description: UrBackup provides a backup solution with a web‑based management interface. The API is documented on the website but no machine‑readable specification was found.
  name: UrBackup API
  slug: urbackup-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/urbackup/changelog/urbackup-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/urbackup-changelog.yml
- group: other
  href: https://artifacts.apis.io/urbackup/hosts/urbackup-hosts.yml
  title: ''
  type: Hosts
  url: hosts/urbackup-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/uroni/urbackup_restore_cd/releases/tag/2021-07-18_19-53-18
- group: auth
  href: https://artifacts.apis.io/urbackup/security/urbackup-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/urbackup-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.urbackup.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.urbackup.org/documentation.html
- group: other
  title: ''
  type: Download
  url: https://www.urbackup.org/download.html
- group: company
  title: ''
  type: Blog
  url: https://blog.urbackup.org
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uroni
created: '2026-10-28'
description: UrBackup provides an open-source client/server backup solution for Windows, Linux, macOS and FreeBSD. It offers image and file backups, fast incremental restores, web‑based management, and commercial extensions such as change‑block tracking and cloud‑appliance options. The software is licensed under AGPL‑v3+, with both free and paid features for enterprises.
layout: provider
modified: '2026-10-28'
name: UrBackup
nav: Providers
network: true
overview: 'UrBackup is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Backup, Open Source, Client-Server, Windows, and Linux.


  UrBackup''s developer surface includes changelog, documentation, engineering blog, and 6 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 53.6
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/urbackup/urbackup-2026-11-03T145509.png
security:
- kind: domain-security
  name: Urbackup Domain Security
  slug: urbackup-domain-security
  summary_line: TLSv1.3 · DMARC
slug: urbackup
tags:
- Backup
- Open Source
- Client-Server
- Windows
- Linux
- FreeBSD
website: https://www.urbackup.org/
---
