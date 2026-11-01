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
- description: Bazarr provides subtitle management integration via its web UI and documented endpoints.
  name: Bazarr API
  slug: bazarr-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bazarr/hosts/bazarr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bazarr-hosts.yml
- group: other
  href: https://artifacts.apis.io/bazarr/vendors/bazarr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bazarr-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/bazarr/bazarr.github.io/releases/latest/download/bazarr.zip
- group: start
  title: ''
  type: GettingStarted
  url: http://wiki.bazarr.media/Getting-Started/First-time-installation-configuration/
- group: auth
  href: https://artifacts.apis.io/bazarr/security/bazarr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bazarr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bazarr.media/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.bazarr.media/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/bazarr
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/morpheus65535/bazarr
created: '2026-10-28'
description: Bazarr is an open-source companion application for Sonarr and Radarr that automates subtitle management. It searches for missing subtitles, downloads them in the desired language, and can upgrade existing subtitles automatically. Available for Linux, Windows, and macOS, Bazarr runs from Python sources, Docker containers, or as a service, offering automatic updates and extensive configuration options. The project includes a web-based UI, Discord community, and extensive documentation to help users integrate subtitle handling into their media workflows.
image: http://www.bazarr.media/assets/img/banner.png
layout: provider
modified: '2026-10-28'
name: Bazarr
nav: Providers
network: true
overview: 'Bazarr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Subtitle, Media, Open-Source, Automation, and Docker.


  Bazarr''s developer surface includes changelog, getting-started guide, documentation, support, and 5 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 12.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 21.1
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
  name: Bazarr Domain Security
  slug: bazarr-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bazarr
tags:
- Subtitle
- Media
- Open-Source
- Automation
- Docker
- Company
website: https://www.bazarr.media/
---
