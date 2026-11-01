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
- group: agent
  href: https://artifacts.apis.io/shiori/llms/shiori-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shiori-llms.txt
- group: other
  href: https://artifacts.apis.io/shiori/hosts/shiori-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shiori-hosts.yml
- group: other
  href: https://artifacts.apis.io/shiori/vendors/shiori-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shiori-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.shioriapp.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/AppitStudio/shiori-updates/releases/download/v1.0.3/Shiori.dmg
- group: company
  title: ''
  type: Blog
  url: https://shioriapp.io/blog
- group: auth
  href: https://artifacts.apis.io/shiori/security/shiori-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shiori-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shioriapp.io
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/go-shiori/shiori/blob/master/docs/index.md
- group: commercial
  title: ''
  type: Pricing
  url: https://shioriapp.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://shioriapp.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://shioriapp.io/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable API contract is published on shioriapp.io or its subdomains.
  evidence:
  - status: 404
    url: https://shioriapp.io/openapi.json
  - status: 404
    url: https://shioriapp.io/openapi.yaml
  - status: 404
    url: https://shioriapp.io/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Shiori is an open-source, self‑hosted bookmark manager written in Go. It offers a simple web interface and command‑line tool for adding, editing, deleting, and searching bookmarks, with support for SQLite, PostgreSQL, MariaDB, and MySQL. Shiori can archive page content for offline reading, import from Pocket, and provides optional browser extensions. The project is MIT‑licensed and aims to give users a fast, organized place for all their links.
image: https://raw.githubusercontent.com/go-shiori/shiori/master/docs/assets/screenshots/cover.png
layout: provider
modified: '2026-10-28'
name: Shiori
nav: Providers
network: true
overview: 'Shiori is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Bookmarks, Self-hosted, Open-source, Go, and CLI.


  Shiori''s developer surface includes changelog, engineering blog, documentation, pricing, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 15.8
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
  name: Shiori Domain Security
  slug: shiori-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shiori
tags:
- Bookmarks
- Self-hosted
- Open-source
- Go
- CLI
website: https://shioriapp.io
---
