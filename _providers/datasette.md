---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://latest.datasette.io
  baseurl_source: declared
  description: 'Datasette API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Datasette API
  slug: datasette-api
artifact_total: 8
common:
- group: other
  href: https://artifacts.apis.io/datasette/vendors/datasette-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datasette-vendors.yml
- group: design
  href: https://artifacts.apis.io/datasette/rules/datasette-rules.yml
  title: ''
  type: Spectral
  url: rules/datasette-rules.yml
- group: design
  href: https://artifacts.apis.io/datasette/json-ld/datasette-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datasette-context.jsonld
- group: design
  href: https://artifacts.apis.io/datasette/vocabulary/datasette-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datasette-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datasette/data-model/datasette-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datasette-data-model.yml
- group: operate
  href: https://artifacts.apis.io/datasette/changelog/datasette-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/datasette-changelog.yml
- group: auth
  href: https://artifacts.apis.io/datasette/authentication/datasette-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datasette-authentication.yml
- group: design
  href: https://artifacts.apis.io/datasette/conformance/datasette-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datasette-conformance.yml
- group: other
  href: https://artifacts.apis.io/datasette/hosts/datasette-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datasette-hosts.yml
- group: build
  href: https://artifacts.apis.io/datasette/packages/datasette-packages.yml
  title: ''
  type: SDKs
  url: packages/datasette-packages.yml
- group: build
  href: https://artifacts.apis.io/datasette/packages/datasette-packages.yml
  title: ''
  type: Packages
  url: packages/datasette-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/simonw/datasette/security/advisories/GHSA-h547-rmjf-5m2m
- group: company
  title: ''
  type: Newsroom
  url: https://datasette.io/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rdslw
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/simonw/llm/releases/tag/0.36
- group: company
  title: ''
  type: Blog
  url: https://datasette.io/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datasette.io/en/stable/getting_started.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datasette.io/
- group: auth
  href: https://artifacts.apis.io/datasette/security/datasette-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datasette-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datasette.io/
created: '2026-10-20'
description: Datasette is an open source multi‑tool for exploring and publishing data. It enables data journalists, archivists, researchers, and anyone with data to quickly analyze, visualize, and share it via interactive websites and JSON APIs. The platform supports plugins, tutorials, and deployment to cloud providers, making data publishing accessible and extensible.
image: https://datasette.io/static/datasette-card.png
json_schemas:
- name: GetActorJsonResponse
  property_count: 1
  slug: datasette-get-actor-json-response
- name: PostMydatabaseAddMessageRequest
  property_count: 1
  slug: datasette-post-mydatabase-add-message-request
- name: PostMydatabaseAddMessageResponse
  property_count: 3
  slug: datasette-post-mydatabase-add-message-response
jsonld:
- class_count: 3
  name: Datasette Context
  property_count: 4
  slug: datasette-context
layout: provider
modified: '2026-10-20'
name: Datasette
nav: Providers
network: true
overview: 'Datasette is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include OpenSource, DataTools, Publishing, Visualization, and Community.


  The Datasette catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Datasette''s developer surface includes changelog, authentication, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Datasette API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: datasette-rules
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.6
    developer_ergonomics: 42.9
    discoverability: 67.9
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datasette Authentication
  slug: datasette-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Datasette Domain Security
  slug: datasette-domain-security
  summary_line: TLSv1.3
slug: datasette
tags:
- OpenSource
- DataTools
- Publishing
- Visualization
- Community
website: https://datasette.io/
---
