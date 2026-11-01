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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://gpodder.net
  baseurl_source: declared
  description: 'gpodder.net API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: gpodder.net API
  slug: gpodder-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/gpodder/rules/gpodder-rules.yml
  title: ''
  type: Spectral
  url: rules/gpodder-rules.yml
- group: design
  href: https://artifacts.apis.io/gpodder/json-ld/gpodder-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gpodder-context.jsonld
- group: design
  href: https://artifacts.apis.io/gpodder/vocabulary/gpodder-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gpodder-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gpodder/data-model/gpodder-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gpodder-data-model.yml
- group: design
  href: https://artifacts.apis.io/gpodder/conformance/gpodder-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gpodder-conformance.yml
- group: other
  href: https://artifacts.apis.io/gpodder/hosts/gpodder-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gpodder-hosts.yml
- group: other
  href: https://artifacts.apis.io/gpodder/vendors/gpodder-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gpodder-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://gpodder.net/login/
- group: auth
  href: https://artifacts.apis.io/gpodder/security/gpodder-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gpodder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gpodder.net/
- group: docs
  title: ''
  type: Documentation
  url: https://gpoddernet.readthedocs.io/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://gpoddernet.readthedocs.io/en/latest/api/reference/index.html
- group: docs
  title: ''
  type: IntegrationGuide
  url: https://gpoddernet.readthedocs.io/en/latest/api/integration.html
- group: other
  title: ''
  type: Repository
  url: https://github.com/gpodder
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://gpoddernet.readthedocs.io/en/latest/api/reference/index.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: gpodder.net is a free, open-source podcast syncing service that lets users discover, subscribe to, and track podcasts across devices. It provides a web interface and API for managing podcast subscriptions, fetching episode metadata, and sharing lists. The platform is community‑driven, offers public directories, and supports integration with third‑party podcast apps.
json_schemas:
- name: GetApi2DataPodcastJsonResponse
  property_count: 8
  slug: gpodder-get-api2-data-podcast-json-response
- name: GetApi2FavoritesResponse
  property_count: 8
  slug: gpodder-get-api2-favorites-response
- name: GetSuggestionsResponse
  property_count: 8
  slug: gpodder-get-suggestions-response
- name: GetSuggestions10OpmlResponse
  property_count: 8
  slug: gpodder-get-suggestions10-opml-response
- name: GetToplist50JsonResponse
  property_count: 4
  slug: gpodder-get-toplist50-json-response
- name: PostApi2EpisodesSomeUserJsonRequest
  property_count: 8
  slug: gpodder-post-api2-episodes-some-user-json-request
jsonld:
- class_count: 16
  name: Gpodder Context
  property_count: 28
  slug: gpodder-context
layout: provider
modified: '2026-10-28'
name: gpodder.net
nav: Providers
network: true
overview: 'gpodder.net is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Podcast, Open-Source, Sync, API, and Community.


  The gpodder.net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  gpodder.net''s developer surface includes documentation, API reference, and 12 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: gpodder.net API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: gpodder-rules
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 24.8
    developer_ergonomics: 16.7
    discoverability: 62.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: derived
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
  name: Gpodder Domain Security
  slug: gpodder-domain-security
  summary_line: TLSv1.2 · HSTS
slug: gpodder
tags:
- Podcast
- Open-Source
- Sync
- API
- Community
website: https://gpodder.net/
---
