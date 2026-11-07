---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Anisongs Jp Agentic Access
  operation_count: 5
  slug: anisongs-jp-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- baseURL: https://anisongs.jp/site/api.php
  baseurl_source: declared
  description: The Check Purity API from Anisongs — 1 operation(s) for check purity.
  name: Anisongs Check Purity API
  slug: anisongs-jp-check-purity-api
- baseURL: https://anisongs.jp/site/api.php
  baseurl_source: declared
  description: The Create Playlist API from Anisongs — 1 operation(s) for create playlist.
  name: Anisongs Create Playlist API
  slug: anisongs-jp-create-playlist-api
- baseURL: https://anisongs.jp/site/api.php
  baseurl_source: declared
  description: The Get Artist API from Anisongs — 1 operation(s) for get artist.
  name: Anisongs Get Artist API
  slug: anisongs-jp-get-artist-api
- baseURL: https://anisongs.jp/site/api.php
  baseurl_source: declared
  description: The Get Program API from Anisongs — 1 operation(s) for get program.
  name: Anisongs Get Program API
  slug: anisongs-jp-get-program-api
- baseURL: https://anisongs.jp/site/api.php
  baseurl_source: declared
  description: The Search Tracks API from Anisongs — 1 operation(s) for search tracks.
  name: Anisongs Search Tracks API
  slug: anisongs-jp-search-tracks-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/anisongs-jp/agentic-access/anisongs-jp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anisongs-jp-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/anisongs-jp/rules/anisongs-jp-rules.yml
  title: ''
  type: Spectral
  url: rules/anisongs-jp-rules.yml
- group: design
  href: https://artifacts.apis.io/anisongs-jp/json-ld/anisongs-jp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anisongs-jp-context.jsonld
- group: design
  href: https://artifacts.apis.io/anisongs-jp/vocabulary/anisongs-jp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anisongs-jp-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anisongs-jp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anisongs-jp/data-model/anisongs-jp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anisongs-jp-data-model.yml
- group: design
  href: https://artifacts.apis.io/anisongs-jp/conformance/anisongs-jp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anisongs-jp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anisongs-jp/well-known/anisongs-jp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anisongs-jp-well-known.yml
- group: other
  href: https://artifacts.apis.io/anisongs-jp/hosts/anisongs-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anisongs-jp-hosts.yml
- group: other
  href: https://artifacts.apis.io/anisongs-jp/vendors/anisongs-jp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anisongs-jp-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://anisongs.jp/news/2026-10-29-kono-oto-tomare-finale-music-project-koto-cd-waon
- group: auth
  href: https://artifacts.apis.io/anisongs-jp/security/anisongs-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anisongs-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anisongs.jp/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anisongs.jp/privacy.php
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anisongs.jp/terms.php
- group: company
  title: ''
  type: Blog
  url: https://anisongs.jp/news/
created: '2026-11-01'
description: Anisongs is a comprehensive anime song database that aggregates information on works, tracks, and artists. It contains over 5,548 works and 15,145 songs, offering playlists, news, and detailed metadata for anime music fans. The service is available via its website and mobile applications for iOS and Android, providing searchable access to the full catalog.
image: https://anisongs.jp/ogp-default.png
json_schemas:
- name: Track
  property_count: 10
  slug: anisongs-jp-track
jsonld:
- class_count: 1
  name: Anisongs Jp Context
  property_count: 10
  slug: anisongs-jp-context
layout: provider
modified: '2026-11-01'
name: Anisongs
nav: Providers
network: true
overview: 'Anisongs publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Check Purity API, Create Playlist API, Get Artist API, and 2 more. Tagged areas include Anime, Music, Database, Japanese, and Entertainment.


  The Anisongs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Anisongs'' developer surface includes engineering blog and 15 more developer resources.'
plans:
- name: Anisongs Jp Plans Pricing
  plan_count: 0
  slug: anisongs-jp-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Anisongs Jp Rate Limits
  slug: anisongs-jp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Anisongs API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: anisongs-jp-rules
scopes:
- name: Anisongs Jp Scopes
  scope_count: 0
  slug: anisongs-jp-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.2
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 7.6
    discoverability: 67.0
    operational_transparency: 0.0
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anisongs Jp Authentication
  slug: anisongs-jp-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anisongs Jp Domain Security
  slug: anisongs-jp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: check-purity
  slug: anisongs-jp-check-purity
- name: create-playlist
  slug: anisongs-jp-create-playlist
- name: get-artist
  slug: anisongs-jp-get-artist
- name: get-program
  slug: anisongs-jp-get-program
- name: search-tracks
  slug: anisongs-jp-search-tracks
slug: anisongs-jp
tags:
- Anime
- Music
- Database
- Japanese
- Entertainment
website: https://anisongs.jp/
---
