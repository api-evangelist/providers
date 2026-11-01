---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Freqblog Com Agentic Access
  operation_count: 92
  slug: freqblog-com-agentic-access
  summary_line: 92 operations · 20 acting
api_count: 2
apis:
- baseURL: https://api.freqblog.com
  baseurl_source: declared
  description: Audio feature extraction
  name: freqblog-com Audio API
  slug: freqblog-com-audio-api
- baseURL: https://api.freqblog.com
  baseurl_source: declared
  description: The Backfill API from freqblog-com — 2 operation(s) for backfill.
  name: freqblog-com Backfill API
  slug: freqblog-com-backfill-api
- baseURL: https://api.freqblog.com
  baseurl_source: declared
  description: Pre-analyzed track catalog — instant name-based lookups
  name: freqblog-com Catalog API
  slug: freqblog-com-catalog-api
- baseURL: https://api.freqblog.com
  baseurl_source: declared
  description: The Me API from freqblog-com — 1 operation(s) for me.
  name: freqblog-com Me API
  slug: freqblog-com-me-api
- baseURL: https://api.freqblog.com
  baseurl_source: declared
  description: The Request Free Key API from freqblog-com — 1 operation(s) for request free key.
  name: freqblog-com Request Free Key API
  slug: freqblog-com-request-free-key-api
- baseURL: https://api.freqblog.com
  baseurl_source: declared
  description: Spotify-shape-compatible routes for endpoints deprecated 2024-11-27. Field names and response structure match Spotify byte-for-byte; numeric values come from this pipeline's open-source analysis and o
  name: freqblog-com Spotify Compat API
  slug: freqblog-com-spotify-compat-api
- baseURL: https://api.freqblog.com
  baseurl_source: declared
  description: Health and operational endpoints
  name: freqblog-com System API
  slug: freqblog-com-system-api
- baseURL: https://api.freqblog.com
  baseurl_source: declared
  description: The Utility API from freqblog-com — 1 operation(s) for utility.
  name: freqblog-com Utility API
  slug: freqblog-com-utility-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/freqblog-com/agentic-access/freqblog-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/freqblog-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/freqblog-com/rules/freqblog-com-rules.yml
  title: ''
  type: Spectral
  url: rules/freqblog-com-rules.yml
- group: design
  href: https://artifacts.apis.io/freqblog-com/json-ld/freqblog-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/freqblog-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/freqblog-com/vocabulary/freqblog-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/freqblog-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/freqblog-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/freqblog-com/data-model/freqblog-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/freqblog-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/freqblog-com/errors/freqblog-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/freqblog-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/freqblog-com/conformance/freqblog-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/freqblog-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/freqblog-com/hosts/freqblog-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/freqblog-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/freqblog-com/vendors/freqblog-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/freqblog-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/freqblog-com/packages/freqblog-com-packages.yml
  title: ''
  type: Packages
  url: packages/freqblog-com-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://freqblog.com/sdk/
- group: auth
  href: https://artifacts.apis.io/freqblog-com/authentication/freqblog-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/freqblog-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/freqblog-com/security/freqblog-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freqblog-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://freqblog.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.freqblog.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.freqblog.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://freqblog.com/#pricing
- group: operate
  title: ''
  type: Support
  url: https://freqblog.com/contact.html
- group: company
  title: ''
  type: Blog
  url: https://freqblog.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stevebirring-star
- group: commercial
  title: ''
  type: Pricing
  url: https://freqblog.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://freqblog.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://freqblog.com/privacy.html
- group: operate
  title: ''
  type: Contact
  url: https://freqblog.com/contact.html
created: '2026-10-30'
description: FreqBlog provides a Music Metadata API that offers BPM, key, mood, and over 25 audio feature fields for tracks queried by name, without requiring a Spotify ID. The service includes free and paid tiers, supports 1,000 to 750,000 requests per month, and covers 1,145+ pre‑analyzed genres across multiple language families. It leverages AcousticBrainz and Essentia for analysis, delivering fast responses and offering back‑fill for missing tracks.
image: https://freqblog.com/og-image.png?v=3
json_schemas:
- name: AudioAnalysisResponse
  property_count: 23
  slug: freqblog-com-audio-analysis-response
- name: BulkLookupResponse
  property_count: 6
  slug: freqblog-com-bulk-lookup-response
- name: EmbeddingResponse
  property_count: 7
  slug: freqblog-com-embedding-response
- name: IdentifyResponse
  property_count: 12
  slug: freqblog-com-identify-response
- name: RecommendationsResponse
  property_count: 5
  slug: freqblog-com-recommendations-response
- name: TrackLookupResponse
  property_count: 44
  slug: freqblog-com-track-lookup-response
jsonld:
- class_count: 48
  name: Freqblog Com Context
  property_count: 155
  slug: freqblog-com-context
layout: provider
modified: '2026-10-30'
name: freqblog-com
nav: Providers
network: true
overview: 'freqblog-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Backfill API, Catalog API, and 5 more. Tagged areas include Company, Music, API, Audio, and Metadata.


  The freqblog-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  freqblog-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 18 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: freqblog-com API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 2
  slug: freqblog-com-rules
score:
  band: developing
  composite: 52.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.7
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 64.4
    developer_ergonomics: 61.2
    discoverability: 66.1
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Freqblog Com Authentication
  slug: freqblog-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Freqblog Com Domain Security
  slug: freqblog-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: freqblog-com-audio-analysis-identify
  slug: freqblog-com-audio-analysis-identify
- name: freqblog-com-backfill-notifications-dismiss
  slug: freqblog-com-backfill-notifications-dismiss
- name: freqblog-com-get-track-details
  slug: freqblog-com-get-track-details
- name: freqblog-com-manage-webhook
  slug: freqblog-com-manage-webhook
- name: freqblog-com-request-free-key-and-view-portal
  slug: freqblog-com-request-free-key-and-view-portal
slug: freqblog-com
tags:
- Company
- Music
- API
- Audio
- Metadata
website: https://freqblog.com/
---
