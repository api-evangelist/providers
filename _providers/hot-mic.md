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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-10-17'
api_count: 5
apis:
- description: API reference for Hot Mic platform covering REST endpoints, authentication, and webhooks.
  name: Hot Mic API
  slug: hot-mic-api
- baseURL: https://public-api.hotmic.io
  baseurl_source: declared
  description: The Presence API from Hot Mic — 1 operation(s) for presence.
  name: Hot Mic Presence API
  slug: hot-mic-presence-api
- baseURL: https://public-api.hotmic.io
  baseurl_source: declared
  description: The Streams API from Hot Mic — 4 operation(s) for streams.
  name: Hot Mic Streams API
  slug: hot-mic-streams-api
- baseURL: https://public-api.hotmic.io
  baseurl_source: declared
  description: The Studio API from Hot Mic — 1 operation(s) for studio.
  name: Hot Mic Studio API
  slug: hot-mic-studio-api
- baseURL: https://public-api.hotmic.io
  baseurl_source: declared
  description: The Users API from Hot Mic — 2 operation(s) for users.
  name: Hot Mic Users API
  slug: hot-mic-users-api
artifact_total: 21
asyncapis:
- description: ''
  name: Hot Mic Webhooks
  slug: hot-mic-webhooks
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/rules/hot-mic-rules.yml
  title: ''
  type: Spectral
  url: rules/hot-mic-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/json-ld/hot-mic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hot-mic-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/vocabulary/hot-mic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hot-mic-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/asyncapi/hot-mic-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hot-mic-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/data-model/hot-mic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hot-mic-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/conventions/hot-mic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hot-mic-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/authentication/hot-mic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hot-mic-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/conformance/hot-mic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hot-mic-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/hosts/hot-mic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hot-mic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/vendors/hot-mic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hot-mic-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/packages/hot-mic-packages.yml
  title: ''
  type: SDKs
  url: packages/hot-mic-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/packages/hot-mic-packages.yml
  title: ''
  type: Packages
  url: packages/hot-mic-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hot-mic/refs/heads/main/security/hot-mic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hot-mic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hotmic.io
- group: docs
  title: ''
  type: Documentation
  url: https://hotmic.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://hotmic.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://hotmic.io/company
coverage:
  checked: '2026-10-12'
  detail: API reference page is a JavaScript‑rendered SPA with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://hotmic.io/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Hot Mic provides a platform that enables apps to integrate creator‑powered video content, offering live streaming, on‑demand video, and interactive tools for creators. Their solution includes SDKs for iOS, Android, and Web, analytics APIs, and monetization features, helping businesses build community‑driven experiences without relying on third‑party social platforms.
json_schemas:
- name: GetStreamsIdResponse
  property_count: 15
  slug: hot-mic-get-streams-id-response
- name: GetStreamsResponse
  property_count: 4
  slug: hot-mic-get-streams-response
- name: GetStudioShowSeriesResponse
  property_count: 2
  slug: hot-mic-get-studio-show-series-response
- name: PostStudioShowSeriesRequest
  property_count: 2
  slug: hot-mic-post-studio-show-series-request
- name: PostStudioShowSeriesResponse
  property_count: 1
  slug: hot-mic-post-studio-show-series-response
- name: PostUsersRequest
  property_count: 7
  slug: hot-mic-post-users-request
- name: PutStreamsIdRequest
  property_count: 6
  slug: hot-mic-put-streams-id-request
- name: PutStreamsIdResponse
  property_count: 7
  slug: hot-mic-put-streams-id-response
- name: PutStudioShowSeriesRequest
  property_count: 2
  slug: hot-mic-put-studio-show-series-request
- name: PutStudioShowSeriesResponse
  property_count: 1
  slug: hot-mic-put-studio-show-series-response
- name: PutUsersIdRequest
  property_count: 5
  slug: hot-mic-put-users-id-request
jsonld:
- class_count: 15
  name: Hot Mic Context
  property_count: 29
  slug: hot-mic-context
layout: provider
modified: '2026-10-12'
name: Hot Mic
nav: Providers
network: true
overview: 'Hot Mic is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Presence API, Streams API, Studio API, and 2 more. Tagged areas include Company, Video, LiveStreaming, CreatorContent, and SDK.


  The Hot Mic catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Hot Mic''s developer surface includes authentication, documentation, pricing, getting-started guide, and 13 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Hot Mic API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: hot-mic-rules
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 58.0
    catalog_earned_first_party: 0.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 33.6
    developer_ergonomics: 40.5
    discoverability: 58.9
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Hot Mic Authentication
  slug: hot-mic-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hot Mic Domain Security
  slug: hot-mic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hot-mic
tags:
- Company
- Video
- LiveStreaming
- CreatorContent
- SDK
website: https://hotmic.io
---
