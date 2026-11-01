---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 114
  human_in_the_loop: 3
  name: Sonarr Agentic Access
  operation_count: 242
  slug: sonarr-agentic-access
  summary_line: 242 operations · 114 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: Sonarr API (v5) – programmatic interface for Sonarr v5.
  name: Sonarr API
  slug: sonarr-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/sonarr/rules/sonarr-rules.yml
  title: ''
  type: Spectral
  url: rules/sonarr-rules.yml
- group: design
  href: https://artifacts.apis.io/sonarr/json-ld/sonarr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sonarr-context.jsonld
- group: design
  href: https://artifacts.apis.io/sonarr/vocabulary/sonarr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sonarr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sonarr/conformance/sonarr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sonarr-conformance.yml
- group: design
  href: https://artifacts.apis.io/sonarr/data-model/sonarr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sonarr-data-model.yml
- group: auth
  href: https://artifacts.apis.io/sonarr/authentication/sonarr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sonarr-authentication.yml
- group: design
  href: https://artifacts.apis.io/sonarr/lifecycle/sonarr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sonarr-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sonarr/errors/sonarr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sonarr-problem-types.yml
- group: other
  href: https://artifacts.apis.io/sonarr/hosts/sonarr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sonarr-hosts.yml
- group: other
  href: https://artifacts.apis.io/sonarr/vendors/sonarr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sonarr-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sonarr.tv/
- group: auth
  href: https://artifacts.apis.io/sonarr/security/sonarr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sonarr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sonarr.tv/
- group: docs
  title: ''
  type: APIReference
  url: https://sonarr.tv/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://sonarr.tv/docs/api/#v5/description/introduction
- group: operate
  title: ''
  type: Support
  url: https://forums.sonarr.tv
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sonarr
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/Sonarr/Sonarr/milestones
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/postman-atlas/workspace/sonarr
created: '2026-10-28'
description: Sonarr is an open-source PVR (Personal Video Recorder) application that automates the download, organization, and management of TV series. It integrates with Usenet and torrent indexers, monitors RSS feeds for new episodes, and automatically retrieves them via configured download clients. Sonarr provides a web-based UI, extensive quality and naming profiles, and supports multiple platforms through Docker, Windows, macOS, and Linux installations. The project is community-driven, with frequent updates, a rich plugin ecosystem, and detailed API documentation for developers to build integrations and automation tools.
image: https://sonarr.tv/img/logo.png
json_schemas:
- name: ConnectionResource
  property_count: 39
  slug: sonarr-connection-resource
- name: GeneralSettingsResource
  property_count: 45
  slug: sonarr-general-settings-resource
- name: QueueResource
  property_count: 29
  slug: sonarr-queue-resource
- name: SeriesResource
  property_count: 55
  slug: sonarr-series-resource
- name: StatisticsResource
  property_count: 23
  slug: sonarr-statistics-resource
- name: SystemResource
  property_count: 31
  slug: sonarr-system-resource
jsonld:
- class_count: 120
  name: Sonarr Context
  property_count: 371
  slug: sonarr-context
layout: provider
modified: '2026-10-28'
name: Sonarr
nav: Providers
network: true
overview: 'Sonarr publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PVR, TV, Usenet, and Torrent.


  The Sonarr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sonarr''s developer surface includes authentication, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 0
  name: Sonarr Rate Limits
  slug: sonarr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Sonarr API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: sonarr-rules
scopes:
- name: Sonarr Scopes
  scope_count: 0
  slug: sonarr-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 48.8
    catalog_earned_first_party: 0.0
    catalog_gap: 66.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 80
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Sonarr Authentication
  slug: sonarr-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Sonarr Domain Security
  slug: sonarr-domain-security
  summary_line: TLSv1.3
slug: sonarr
tags:
- Company
- PVR
- TV
- Usenet
- Torrent
- Automation
website: https://sonarr.tv/
---
