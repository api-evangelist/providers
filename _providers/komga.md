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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Komga REST API providing access to libraries, series, books and user management.
  name: Komga API
  slug: komga-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/komga/conformance/komga-conformance.yml
  title: ''
  type: Conformance
  url: conformance/komga-conformance.yml
- group: other
  href: https://artifacts.apis.io/komga/hosts/komga-hosts.yml
  title: ''
  type: Hosts
  url: hosts/komga-hosts.yml
- group: other
  href: https://artifacts.apis.io/komga/vendors/komga-vendors.yml
  title: ''
  type: Vendors
  url: vendors/komga-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://komga.org/docs/openapi/releases
- group: auth
  href: https://artifacts.apis.io/komga/security/komga-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/komga-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://komga.org/
- group: docs
  title: ''
  type: APIReference
  url: https://komga.org/docs/openapi/komga-api
- group: start
  title: ''
  type: GettingStarted
  url: https://komga.org/docs/introduction
- group: company
  title: ''
  type: Blog
  url: https://komga.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gotson/komga
- group: operate
  title: ''
  type: Support
  url: https://komga.org/docs/category/guides
created: '2026-10-28'
description: Komga is an open-source media server for comics, mangas, BDs, magazines and eBooks. It organizes CBZ, CBR, PDF and EPUB files into libraries, collections or reading lists, and provides a web interface, OPDS feeds, and integrations with various clients. Users can read content via the built-in web reader, Mihon extension, or other compatible readers. The server runs on any system supporting Java or Docker, including Windows, macOS, Linux, and popular NAS devices.
layout: provider
modified: '2026-10-28'
name: Komga
nav: Providers
network: true
overview: 'Komga is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Media Server, Comics, Manga, Ebooks, and Open Source.


  Komga''s developer surface includes changelog, API reference, getting-started guide, engineering blog, support, and 6 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 62.5
    operational_transparency: 10.5
  previous_composite: 14.1
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/komga/komga-2026-11-03T134508.png
security:
- kind: domain-security
  name: Komga Domain Security
  slug: komga-domain-security
  summary_line: TLSv1.3
slug: komga
tags:
- Media Server
- Comics
- Manga
- Ebooks
- Open Source
- Community
website: https://komga.org/
---
