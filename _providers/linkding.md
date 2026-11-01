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
- description: REST API for managing bookmarks, providing resources such as authentication, bookmarks, tags, bundles, and users.
  name: Linkding API
  slug: linkding-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/linkding/hosts/linkding-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linkding-hosts.yml
- group: other
  href: https://artifacts.apis.io/linkding/vendors/linkding-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linkding-vendors.yml
- group: auth
  href: https://artifacts.apis.io/linkding/security/linkding-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linkding-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://linkding.link/
- group: docs
  title: ''
  type: Documentation
  url: https://linkding.link/installation
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/sissbruecker/linkding
- group: start
  title: ''
  type: Demo
  url: https://demo.linkding.link
coverage:
  checked: '2026-10-28'
  detail: Documentation provides HTML pages but no machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://linkding.link/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Linkding is a self‑hosted bookmark manager designed to be minimal, fast, and easy to set up. It offers features such as customizable UI, automatic metadata fetching, archiving, bulk editing, multi‑user support, and browser extensions for Firefox and Chrome. The service provides a REST API for developers to integrate bookmarking functionality into scripts or third‑party applications, and can be deployed via a single Docker container using SQLite as the database.
layout: provider
modified: '2026-10-28'
name: linkding
nav: Providers
network: true
overview: 'linkding is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bookmark, Self-hosted, Open-source, and Docker.


  linkding''s developer surface includes documentation and 6 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 62.5
    operational_transparency: 5.3
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
  name: Linkding Domain Security
  slug: linkding-domain-security
  summary_line: TLSv1.3 · HSTS
slug: linkding
tags:
- Company
- Bookmark
- Self-hosted
- Open-source
- Docker
website: https://linkding.link/
---
