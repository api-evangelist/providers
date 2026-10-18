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
api_count: 1
apis:
- description: Internet Archive provides access to digital library resources via its website.
  name: Internet Archive API
  slug: internet-archive-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/internet-archive/refs/heads/main/hosts/internet-archive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/internet-archive-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/internet-archive/refs/heads/main/packages/internet-archive-packages.yml
  title: ''
  type: SDKs
  url: packages/internet-archive-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/internet-archive/refs/heads/main/packages/internet-archive-packages.yml
  title: ''
  type: Packages
  url: packages/internet-archive-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/internet-archive/refs/heads/main/security/internet-archive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/internet-archive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://archive.org
created: '2026-10-14'
description: Internet Archive is a non-profit digital library offering free access to millions of books, movies, software, music, and archived web pages. It provides services such as the Wayback Machine, Open Library, and various APIs for searching and retrieving digital content, supporting researchers, historians, and the general public.
layout: provider
modified: '2026-10-14'
name: Internet Archive
nav: Providers
network: true
overview: Internet Archive is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Library, Non-Profit, Archival, Open Access, and Research.
random_paper: 6
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Internet Archive Domain Security
  slug: internet-archive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: internet-archive
tags:
- Digital Library
- Non-Profit
- Archival
- Open Access
- Research
website: https://archive.org
---
