---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for managing music collections, as documented in the Lidarr API Docs.
  name: Lidarr API
  slug: lidarr-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/lidarr/conformance/lidarr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lidarr-conformance.yml
- group: other
  href: https://artifacts.apis.io/lidarr/hosts/lidarr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lidarr-hosts.yml
- group: other
  href: https://artifacts.apis.io/lidarr/vendors/lidarr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lidarr-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lidarr.audio/
- group: auth
  href: https://artifacts.apis.io/lidarr/security/lidarr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lidarr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lidarr.audio/
- group: docs
  title: ''
  type: Documentation
  url: https://lidarr.audio/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://lidarr.audio/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://lidarr.audio/#download
- group: operate
  title: ''
  type: Support
  url: https://lidarr.audio/#support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Lidarr/Lidarr
created: '2026-10-28'
description: Lidarr is an open-source music collection manager that automates the downloading, organization, and tagging of music files. It monitors your favorite artists and releases, integrates with download clients, and ensures metadata is correctly applied, providing a convenient way to keep your music library up to date.
layout: provider
modified: '2026-10-28'
name: Lidarr
nav: Providers
network: true
overview: 'Lidarr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Media, Automation, OpenSource, and DownloadManager.


  Lidarr''s developer surface includes documentation, API reference, getting-started guide, support, and 7 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 14.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 53.6
    operational_transparency: 21.1
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Lidarr Domain Security
  slug: lidarr-domain-security
  summary_line: TLSv1.3
slug: lidarr
tags:
- Music
- Media
- Automation
- OpenSource
- DownloadManager
website: https://lidarr.audio/
---
