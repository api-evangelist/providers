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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.8
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: Provides access to music metadata, credits, and licensing information via REST endpoints.
  name: Music Story API
  slug: music-story-api-2
- baseURL: https://api.v2.music-story.com
  baseurl_source: declared
  description: The Artist API from Music Story — 2 operation(s) for artist.
  name: Music Story Artist API
  slug: music-story-artist-api
- baseURL: https://api.v2.music-story.com
  baseurl_source: declared
  description: The Music Story API API from Music Story — 2 operation(s) for music story api.
  name: Music Story Music Story API
  slug: music-story-music-story-api-api
artifact_total: 9
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/rules/music-story-rules.yml
  title: ''
  type: Spectral
  url: rules/music-story-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/json-ld/music-story-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/music-story-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/vocabulary/music-story-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/music-story-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/data-model/music-story-data-model.yml
  title: ''
  type: DataModel
  url: data-model/music-story-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/changelog/music-story-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/music-story-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/conformance/music-story-conformance.yml
  title: ''
  type: Conformance
  url: conformance/music-story-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/llms/music-story-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/music-story-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/hosts/music-story-hosts.yml
  title: ''
  type: Hosts
  url: hosts/music-story-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/packages/music-story-packages.yml
  title: ''
  type: SDKs
  url: packages/music-story-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/packages/music-story-packages.yml
  title: ''
  type: Packages
  url: packages/music-story-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://doc.music-story.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/music-story
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/music-story/refs/heads/main/security/music-story-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/music-story-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://music-story.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://music-story.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://doc.music-story.com
- group: docs
  title: ''
  type: APIReference
  url: https://doc.music-story.com/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://music-story.com/en
- group: operate
  title: ''
  type: Support
  url: https://music-story.com/en/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://music-story.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://music-story.com/en/privacy
- group: start
  title: ''
  type: SignUp
  url: https://metadata.music-story.com/sign-up
coverage:
  checked: '2026-10-12'
  detail: API reference page provides HTML docs but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec.
  evidence:
  - status: 200
    url: https://doc.music-story.com/api/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Music Story provides a comprehensive music metadata infrastructure, offering APIs and services that enable detailed metadata access for songs, artists, and related licensing information. Their platform supports metadata monitoring, rich credit information, and tailored solutions for music services, labels, distributors, and automotive applications, aiming to preserve the value and story behind every piece of music.
image: https://music-story.com/og-default.jpeg
json_schemas:
- name: GetApiApiidResponse
  property_count: 3
  slug: music-story-get-api-apiid-response
- name: GetApiArtistIdIdResponse
  property_count: 4
  slug: music-story-get-api-artist-id-id-response
- name: GetApiArtistIdResponse
  property_count: 29
  slug: music-story-get-api-artist-id-response
jsonld:
- class_count: 3
  name: Music Story Context
  property_count: 36
  slug: music-story-context
layout: provider
modified: '2026-10-12'
name: Music Story
nav: Providers
network: true
overview: 'Music Story is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Artist API, Music Story API, and 1 more. Tagged areas include Company, Music, Metadata, and Services.


  The Music Story catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Music Story''s developer surface includes changelog, documentation, API reference, getting-started guide, support, signup flow, and 16 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Music Story API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: music-story-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 35.6
    contract_quality: 23.6
    developer_ergonomics: 50.0
    discoverability: 60.7
    operational_transparency: 21.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Music Story Domain Security
  slug: music-story-domain-security
  summary_line: TLSv1.3 · DMARC
slug: music-story
tags:
- Company
- Music
- Metadata
- Services
website: https://music-story.com/
---
