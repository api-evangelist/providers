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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'Channels DVR apps API as documented publicly: 40 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Channels DVR apps API
  slug: apps-api
- description: 'Channels DVR server API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Channels DVR server API
  slug: server-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/channels-dvr/rules/channels-dvr-rules.yml
  title: ''
  type: Spectral
  url: rules/channels-dvr-rules.yml
- group: design
  href: https://artifacts.apis.io/channels-dvr/json-ld/channels-dvr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/channels-dvr-context.jsonld
- group: design
  href: https://artifacts.apis.io/channels-dvr/vocabulary/channels-dvr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/channels-dvr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/channels-dvr/data-model/channels-dvr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/channels-dvr-data-model.yml
- group: design
  href: https://artifacts.apis.io/channels-dvr/conformance/channels-dvr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/channels-dvr-conformance.yml
- group: other
  href: https://artifacts.apis.io/channels-dvr/hosts/channels-dvr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/channels-dvr-hosts.yml
- group: other
  href: https://artifacts.apis.io/channels-dvr/vendors/channels-dvr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/channels-dvr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://community.getchannels.com/tos
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getchannels.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://community.getchannels.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://getchannels.com/press/
- group: start
  title: ''
  type: Login
  url: https://community.getchannels.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/home
- group: operate
  title: ''
  type: ChangeLog
  url: https://getchannels.com/releases/
- group: auth
  href: https://artifacts.apis.io/channels-dvr/security/channels-dvr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/channels-dvr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getchannels.com/
- group: docs
  title: ''
  type: Documentation
  url: https://getchannels.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://getchannels.com/support/
- group: company
  title: ''
  type: Blog
  url: https://getchannels.com/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://getchannels.com/docs/getting-started/quick-start-guide/
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided as HTML pages without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://getchannels.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Channels DVR provides a cloud-based live TV streaming and DVR service, allowing users to watch, record, and organize television content across devices. Founded in 2015, the company offers a customizable channel lineup, multiview capabilities, and integration with smart home platforms. Their platform includes APIs for automation, smart rules, and third‑party integrations, supporting developers to build custom experiences and manage media libraries.
image: https://getchannels.com/a/images/og/root.jpg?v11
json_schemas:
- name: GetApiStatusResponse
  property_count: 4
  slug: channels-dvr-get-api-status-response
- name: GetApiV1EpisodesResponse
  property_count: 33
  slug: channels-dvr-get-api-v1-episodes-response
- name: GetApiV1JobsIdResponse
  property_count: 10
  slug: channels-dvr-get-api-v1-jobs-id-response
- name: GetApiV1MoviesResponse
  property_count: 29
  slug: channels-dvr-get-api-v1-movies-response
- name: GetApiV1ShowsResponse
  property_count: 17
  slug: channels-dvr-get-api-v1-shows-response
- name: GetApiV1VideosResponse
  property_count: 25
  slug: channels-dvr-get-api-v1-videos-response
- name: PostApiNotifyRequest
  property_count: 3
  slug: channels-dvr-post-api-notify-request
jsonld:
- class_count: 7
  name: Channels Dvr Context
  property_count: 54
  slug: channels-dvr-context
layout: provider
modified: '2026-10-28'
name: Channels DVR
nav: Providers
network: true
overview: 'Channels DVR is listed with 2 APIs on the [APIs.io](https://apis.io/) network: apps API and server API. Tagged areas include Company, Streaming, DVR, TV, and Automation.


  The Channels DVR catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Channels DVR''s developer surface includes changelog, documentation, support, engineering blog, getting-started guide, and 15 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Channels DVR API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: channels-dvr-rules
score:
  band: emerging
  composite: 22.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 23.4
    developer_ergonomics: 14.3
    discoverability: 58.0
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/channels-dvr/channels-dvr-2026-11-03T123837.png
security:
- kind: domain-security
  name: Channels Dvr Domain Security
  slug: channels-dvr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: channels-dvr
tags:
- Company
- Streaming
- DVR
- TV
- Automation
website: https://getchannels.com/
---
