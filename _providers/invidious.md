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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Public REST API for Invidious, documented at https://docs.invidious.io/api/.
  name: Invidious API
  slug: invidious-api-2
- description: 'Invidious API as documented publicly: 55 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Invidious API
  slug: invidious-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/invidious/rules/invidious-rules.yml
  title: ''
  type: Spectral
  url: rules/invidious-rules.yml
- group: design
  href: https://artifacts.apis.io/invidious/json-ld/invidious-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/invidious-context.jsonld
- group: design
  href: https://artifacts.apis.io/invidious/vocabulary/invidious-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/invidious-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/invidious/data-model/invidious-data-model.yml
  title: ''
  type: DataModel
  url: data-model/invidious-data-model.yml
- group: auth
  href: https://artifacts.apis.io/invidious/authentication/invidious-authentication.yml
  title: ''
  type: Authentication
  url: authentication/invidious-authentication.yml
- group: design
  href: https://artifacts.apis.io/invidious/conformance/invidious-conformance.yml
  title: ''
  type: Conformance
  url: conformance/invidious-conformance.yml
- group: other
  href: https://artifacts.apis.io/invidious/hosts/invidious-hosts.yml
  title: ''
  type: Hosts
  url: hosts/invidious-hosts.yml
- group: build
  href: https://artifacts.apis.io/invidious/packages/invidious-packages.yml
  title: ''
  type: SDKs
  url: packages/invidious-packages.yml
- group: build
  href: https://artifacts.apis.io/invidious/packages/invidious-packages.yml
  title: ''
  type: Packages
  url: packages/invidious-packages.yml
- group: auth
  href: https://artifacts.apis.io/invidious/security/invidious-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/invidious-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://invidious.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.invidious.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.invidious.io/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.invidious.io/installation/
- group: operate
  title: ''
  type: Support
  url: https://invidious.io/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iv-org
coverage:
  checked: '2026-10-28'
  detail: The Invidious documentation is publicly available HTML but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://docs.invidious.io/api/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Invidious is an open-source, privacy-focused front-end for YouTube that allows users to watch videos without a Google account, avoids tracking, and provides a fully documented REST API for developers. The project is licensed under AGPL-3.0, supports multiple languages, and offers features such as ad-free playback, SponsorBlock integration, and playlist management. It can be self-hosted or accessed via public instances listed on its site.
image: https://invidious.io/invidious-colored-vector.svg
json_schemas:
- name: GetApiV1AuthPreferencesResponse
  property_count: 25
  slug: invidious-get-api-v1-auth-preferences-response
- name: GetApiV1ChannelsIdResponse
  property_count: 18
  slug: invidious-get-api-v1-channels-id-response
- name: GetApiV1PostIdCommentsResponse
  property_count: 14
  slug: invidious-get-api-v1-post-id-comments-response
- name: GetApiV1SearchResponse
  property_count: 26
  slug: invidious-get-api-v1-search-response
- name: GetApiV1TrendingResponse
  property_count: 15
  slug: invidious-get-api-v1-trending-response
- name: GetApiV1VideosIdResponse
  property_count: 39
  slug: invidious-get-api-v1-videos-id-response
jsonld:
- class_count: 38
  name: Invidious Context
  property_count: 119
  slug: invidious-context
layout: provider
modified: '2026-10-28'
name: Invidious
nav: Providers
network: true
overview: 'Invidious is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include video, open-source, privacy, api, and frontend.


  The Invidious catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Invidious'' developer surface includes authentication, documentation, API reference, getting-started guide, support, and 11 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Invidious API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: invidious-rules
scopes:
- name: Invidious Scopes
  scope_count: 0
  slug: invidious-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 23.0
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 22
      marker_coverage: 100.0
      total: 22
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
  name: Invidious Authentication
  slug: invidious-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Invidious Domain Security
  slug: invidious-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: invidious
tags:
- video
- open-source
- privacy
- api
- frontend
- youtube
website: https://invidious.io/
---
