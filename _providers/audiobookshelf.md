---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Audiobookshelf provides a self‑hosted media server for audiobooks and podcasts with a web UI, mobile apps, and library management features.
  name: Audiobookshelf API
  slug: audiobookshelf-api-2
- description: 'Audiobookshelf API as documented publicly: 58 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Audiobookshelf API
  slug: audiobookshelf-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/audiobookshelf/rules/audiobookshelf-rules.yml
  title: ''
  type: Spectral
  url: rules/audiobookshelf-rules.yml
- group: design
  href: https://artifacts.apis.io/audiobookshelf/json-ld/audiobookshelf-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/audiobookshelf-context.jsonld
- group: design
  href: https://artifacts.apis.io/audiobookshelf/vocabulary/audiobookshelf-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/audiobookshelf-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/audiobookshelf/data-model/audiobookshelf-data-model.yml
  title: ''
  type: DataModel
  url: data-model/audiobookshelf-data-model.yml
- group: design
  href: https://artifacts.apis.io/audiobookshelf/conformance/audiobookshelf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audiobookshelf-conformance.yml
- group: other
  href: https://artifacts.apis.io/audiobookshelf/hosts/audiobookshelf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audiobookshelf-hosts.yml
- group: other
  href: https://artifacts.apis.io/audiobookshelf/vendors/audiobookshelf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audiobookshelf-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://audiobookshelf.org/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://audiobookshelf.org/blog
- group: auth
  href: https://artifacts.apis.io/audiobookshelf/security/audiobookshelf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audiobookshelf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audiobookshelf.org/
- group: docs
  title: ''
  type: Documentation
  url: https://audiobookshelf.org/docs/documentation/introduction/
- group: operate
  title: ''
  type: Support
  url: https://audiobookshelf.org/docs/faq/general/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/advplyr
coverage:
  checked: '2026-10-28'
  detail: Documentation is available but provides no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://audiobookshelf.org/docs/documentation/introduction/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Audiobookshelf provides a self‑hosted audiobook and podcast server that lets users organize, stream, and share their personal media collections. It offers a web UI, mobile apps, and integrations for popular platforms, supporting features like library management, playback controls, and metadata fetching from online sources.
json_schemas:
- name: DeleteApiNotificationsIdResponse
  property_count: 7
  slug: audiobookshelf-delete-api-notifications-id-response
- name: GetApiSearchChaptersResponse
  property_count: 7
  slug: audiobookshelf-get-api-search-chapters-response
- name: PostApiNotificationsRequest
  property_count: 7
  slug: audiobookshelf-post-api-notifications-request
- name: PostApiUploadRequest
  property_count: 6
  slug: audiobookshelf-post-api-upload-request
- name: PostApiUsersRequest
  property_count: 13
  slug: audiobookshelf-post-api-users-request
- name: PostLoginResponse
  property_count: 4
  slug: audiobookshelf-post-login-response
jsonld:
- class_count: 74
  name: Audiobookshelf Context
  property_count: 103
  slug: audiobookshelf-context
layout: provider
modified: '2026-10-28'
name: Audiobookshelf
nav: Providers
network: true
overview: 'Audiobookshelf is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Self-Hosted, Audiobooks, Podcasts, and Media Server.


  The Audiobookshelf catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Audiobookshelf''s developer surface includes engineering blog, documentation, support, and 11 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Audiobookshelf API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: audiobookshelf-rules
score:
  band: emerging
  composite: 16.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 8.3
    discoverability: 53.6
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 19.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/audiobookshelf/audiobookshelf-2026-11-03T121305.png
security:
- kind: domain-security
  name: Audiobookshelf Domain Security
  slug: audiobookshelf-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: audiobookshelf
tags:
- Company
- Self-Hosted
- Audiobooks
- Podcasts
- Media Server
website: https://audiobookshelf.org/
---
